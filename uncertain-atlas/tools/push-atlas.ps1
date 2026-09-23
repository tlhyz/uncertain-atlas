# push-atlas.ps1 — 推送前自动探测网络，必要时走本地代理
#
# 背景（2026-09-17 实测）：本机 `github.com:443` 直连不通，但
# `api.github.com` / `raw.githubusercontent.com` 通，且本地 `127.0.0.1:7897`
# 有代理（Clash 默认端口）。SSH 22 与 ssh.github.com:443 也通。
# 于是 `git push` 会报 `Failed to connect to github.com port 443`。
#
# 本脚本：先直连试推；失败则探测本地代理端口并重试；最后用
# `git ls-remote` 驗證远程真实 ref（不看本地缓存）。
#
# 用法（在仓库根，含 uncertain-atlas/ 的那一层）：
#     & .\uncertain-atlas\tools\push-atlas.ps1
#
# 注意：本脚本含中文，必须带 UTF-8 BOM 保存（Windows PowerShell 5.1
# 会把无 BOM 的 .ps1 按 ANSI 解码）。

$ErrorActionPreference = 'Continue'
$OutputEncoding = [Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$repo = Split-Path -Parent (Split-Path -Parent $here)   # tools -> uncertain-atlas -> repo
if (-not (Test-Path -LiteralPath (Join-Path $repo '.git'))) {
    # 回退：也许仓库根就在上一层
    $alt = Split-Path -Parent $here
    if (Test-Path -LiteralPath (Join-Path $alt '.git')) { $repo = $alt }
    else { Write-Host "找不到 git 仓库根（脚本位置: $here）" -ForegroundColor Red; exit 1 }
}
Set-Location -LiteralPath $repo

function Get-LocalHead { (git rev-parse HEAD).Trim() }
function Get-RemoteHead {
    $r = git ls-remote --heads origin main 2>$null
    if (-not $r) { return $null }
    return ($r -split "`t")[0].Trim()
}

# 候选代理端口（按常见度排序）
$proxyCandidates = @(7897, 7890, 10809, 10808, 2080, 1080, 8080)

Write-Host "`n=== push-atlas ===" -ForegroundColor Cyan
$head = Get-LocalHead
Write-Host "本地 HEAD: $head"

# 先看是否已经推过
$remote = Get-RemoteHead
if ($remote -eq $head) { Write-Host "远程已是同一提交，无需推送。" -ForegroundColor Green; exit 0 }

# 1) 直连
Write-Host "[1] 直连推送…"
$out = git push origin main 2>&1 | Out-String
if ($LASTEXITCODE -eq 0 -or $out -match 'main -> main' -or $out -match 'up-to-date') {
    Write-Host "    直连成功" -ForegroundColor Green
} else {
    Write-Host "    直连失败" -ForegroundColor Yellow

    # 2) 逐个探测本地代理
    $ok = $false
    foreach ($port in $proxyCandidates) {
        $open = Test-NetConnection -ComputerName 127.0.0.1 -Port $port `
                -WarningAction SilentlyContinue -InformationLevel Quiet -ErrorAction SilentlyContinue
        if (-not $open) { continue }
        Write-Host "[2] 发现本地代理 127.0.0.1:$port，经代理推送…"
        $p = "http://127.0.0.1:$port"
        $out2 = git -c "http.proxy=$p" -c "https.proxy=$p" push origin main 2>&1 | Out-String
        if ($LASTEXITCODE -eq 0 -or $out2 -match 'main -> main' -or $out2 -match 'up-to-date') {
            Write-Host "    经代理成功（$p）" -ForegroundColor Green
            # 记进本仓库 local 配置，后续波次免手动
            git config --local "http.https://github.com/.proxy" $p
            Write-Host "    已写入 local 配置 http.https://github.com/.proxy = $p"
            $ok = $true
            break
        }
        Write-Host "    经 $p 失败" -ForegroundColor Yellow
    }
    if (-not $ok) {
        Write-Host "`n推送失败：直连与所有候选代理都不通。" -ForegroundColor Red
        Write-Host "检查：github.com:443 是否可达；本地代理是否在运行。"
        exit 1
    }
}

# 3) 验证远程真实 ref
Start-Sleep -Seconds 1
$remote2 = Get-RemoteHead
if ($remote2 -eq $head) {
    Write-Host "`n验证通过：origin/main == $remote2" -ForegroundColor Green
    exit 0
} else {
    Write-Host "`n验证失败：远程 $remote2 ≠ 本地 $head" -ForegroundColor Red
    exit 1
}
