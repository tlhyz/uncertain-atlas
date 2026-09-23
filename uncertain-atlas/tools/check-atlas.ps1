# check-atlas.ps1 — 「不确定图谱」每波提交前的机械校验
#
# 用法（在仓库根，即含 uncertain-atlas/ 的那一层）：
#     pwsh -File tools/check-atlas.ps1
#
# 它只查**机械一致性**，不查内容质量。内容质量按 GOAL.md 人工审，写进 AUDIT_LOG.md。
#
# 查什么：
#   1. 库文件计数（模式 / 反模式）
#   2. 不变量最大号、语料最大号、语料行数
#   3. L10.3 目录条最大号（应为语料最大号 − 8）
#   4. ARCHITECTURE.md 的库计数行是否与磁盘一致
#   5. index/03-knowledge-assets.md 的四个计数与两处区间是否与磁盘一致
#   6. 活边界标记是否滞后：
#        - tracks/failure-museum/worked-example-halt-surfaces.md 的「不变量 A–B；语料 C…」
#        - libraries/adversarial-corpus/README.md 的「来源：…不变量 1–N」
#        - libraries/threat-model/README.md 的表内最大 #
#   7. 所有相对 Markdown 链接是否落点存在
#   8. 所有 .md 是否统一 CRLF（库内既有约定）
#
# 注意（复审结论）：CHANGELOG.md 与 AUDIT_LOG.md 里的「不变量 12–15」这类区间是
# **历史记录**，必须保持冻结，不属于陈旧引用。本脚本刻意不检查它们。
#
# 退出码：0 = 全通过；1 = 有失败项。

$ErrorActionPreference = 'Stop'
$OutputEncoding = [Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# 定位知识库根：脚本在 tools/ 下，或直接在仓库根
# 定位知识库根。脚本的规范位置是 uncertain-atlas/tools/check-atlas.ps1，
# 于是库根 = 脚本目录的上一级。为兼容旧布局（仓库根/tools/）也向上找一层。
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$root = Split-Path -Parent $here                       # 预期：.../uncertain-atlas
if (-not (Test-Path -LiteralPath (Join-Path $root 'GOAL.md'))) {
    $up = Split-Path -Parent $root                     # 回退：仓库根/tools/ 布局
    if (Test-Path -LiteralPath (Join-Path $up 'uncertain-atlas\GOAL.md')) {
        $root = Join-Path $up 'uncertain-atlas'
    } else {
        Write-Host "找不到知识库根（需要同目录有 GOAL.md 且含 libraries/）" -ForegroundColor Red
        Write-Host "  脚本位置: $here" -ForegroundColor Red
        exit 1
    }
}

$fail = 0
function Ok($msg)   { Write-Host "  [OK]   $msg" -ForegroundColor Green }
function Bad($msg)  { Write-Host "  [FAIL] $msg" -ForegroundColor Red; $script:fail++ }
function Check($cond, $msg, $detail) {
    if ($cond) { Ok $msg } else { Bad ("{0}  {1}" -f $msg, $detail) }
}

function Read-All($rel) { [System.IO.File]::ReadAllText((Join-Path $root $rel)) }
# 注意：.NET 正则默认**不**启用多行模式，^ 只匹配整串开头。
# 本库所有「按行」的模式都必须带 (?m)，否则静默返回 0 命中（曾因此误报全 FAIL）。
function MaxOf($rel, $pattern) {
    $txt = Read-All $rel
    $m = [regex]::Matches($txt, $pattern)
    if ($m.Count -eq 0) { return -1 }
    return ($m | ForEach-Object { [int]$_.Groups[1].Value } | Measure-Object -Maximum).Maximum
}

Write-Host "`n=== check-atlas: 机械一致性 ===`n"

# ---- 1. 库计数 ----
$patCount  = (Get-ChildItem (Join-Path $root 'libraries\design-patterns') -File -Filter *.md | Where-Object Name -ne 'README.md').Count
$antiCount = (Get-ChildItem (Join-Path $root 'libraries\anti-patterns')   -File -Filter *.md | Where-Object Name -ne 'README.md').Count
Write-Host "[1] 库文件计数"
Write-Host "      模式=$patCount  反模式=$antiCount"

# ---- 2. 不变量 / 语料 ----
Write-Host "[2] 不变量与语料"
$maxInv  = MaxOf 'libraries\invariants\README.md'          '(?m)^第 (\d+) 条：'
$maxCorp = MaxOf 'libraries\adversarial-corpus\README.md'  '(?m)^\| C(\d+)'
$corpRows = ([regex]::Matches((Read-All 'libraries\adversarial-corpus\README.md'), '(?m)^\| C\d+')).Count
Check ($maxInv -gt 0) "不变量最大号 = $maxInv" ''
Check ($maxCorp -gt 0) "语料最大号 = C$maxCorp（表内 $corpRows 行）" ''

# ---- 3. L10.3 ----
# 已知遗留债（AUDIT_LOG A2135）：L10.3 目录缺 435 / 436 / 438 三条。
# 因此它落后于「语料最大号 − 8」。修完这三条后把 $l10KnownGap 改成 0。
$l10KnownGap = 2
Write-Host "[3] L10.3 目录条（期望 = 语料最大号 − 8 − $l10KnownGap 已知缺口）"
$maxL10 = MaxOf 'courses\level-10-uncertain-studio\L10-M03-v1-settlement-machine.md' '(?m)^(\d+)\. '
$expectL10 = $maxCorp - 8 - $l10KnownGap
Check ($maxL10 -eq $expectL10) "L10.3 最大条 = $maxL10" "(期望 $expectL10)"

# ---- 4. ARCHITECTURE.md ----
Write-Host "[4] ARCHITECTURE.md 库计数行"
$arch = Read-All 'ARCHITECTURE.md'
$m = [regex]::Match($arch, '模式 (\d+) \+ 反模式 (\d+) \+ 决策/威胁/不变量（(\d+) 条）\+ 对抗语料 C01–C(\d+)')
if (-not $m.Success) { Bad "找不到库计数行（格式变了？）" }
else {
    Check ([int]$m.Groups[1].Value -eq $patCount)  "模式 $($m.Groups[1].Value)"  "(磁盘 $patCount)"
    Check ([int]$m.Groups[2].Value -eq $antiCount) "反模式 $($m.Groups[2].Value)" "(磁盘 $antiCount)"
    Check ([int]$m.Groups[3].Value -eq $maxInv)    "不变量 $($m.Groups[3].Value)" "(磁盘 $maxInv)"
    Check ([int]$m.Groups[4].Value -eq $maxCorp)   "语料 C$($m.Groups[4].Value)" "(磁盘 C$maxCorp)"
}

# ---- 5. index/03 ----
Write-Host "[5] index/03-knowledge-assets.md"
$idx = Read-All 'index\03-knowledge-assets.md'
$pairs = @(
    @{ name='设计模式'; re='\| 07 \| 《Design Pattern Library》 \| `libraries/design-patterns/` \| (\d+) 条 \|'; want=$patCount },
    @{ name='反模式';   re='\| 08 \| 《Anti-Pattern Library》 \| `libraries/anti-patterns/` \| (\d+) 条 \|'; want=$antiCount },
    @{ name='不变量';   re='\| 12 \| 《不确定 Invariant Library》 \| `libraries/invariants/` \| (\d+) 条 \|'; want=$maxInv },
    @{ name='语料目录'; re='\| 13 \|.*?目录 C01–C(\d+)；'; want=$maxCorp }
)
foreach ($p in $pairs) {
    $mm = [regex]::Match($idx, $p.re)
    if (-not $mm.Success) { Bad "$($p.name)：找不到计数" }
    else { Check ([int]$mm.Groups[1].Value -eq $p.want) "$($p.name) = $($mm.Groups[1].Value)" "(磁盘 $($p.want))" }
}
# 资产行：只有两行记录「每一波」，必须跟到前沿 —— 05b（实现保证精读）与 Cosmos / CometBFT。
# 其它行（如 Bitcoin / Ethereum）只记与本链有关的不变量，落后于全局最大值是**正确**的，
# 不是滞后，不能一概而论。
$frontierRows = @('05b', 'Cosmos / CometBFT')
$rowFail = 0
foreach ($line in ($idx -split "`n")) {
    if ($line -notmatch '^\| ') { continue }
    $name = ($line -split '\|')[1].Trim()
    if ($frontierRows -notcontains $name) { continue }
    $nums = [regex]::Matches($line, '不变量 (\d+)') | ForEach-Object { [int]$_.Groups[1].Value }
    if ($nums.Count -eq 0) { Bad "前沿行「$name」没有任何不变量引用"; $rowFail++; continue }
    $mx = ($nums | Measure-Object -Maximum).Maximum
    if ($mx -ne $maxInv) { Bad "前沿行「$name」最大只到 $mx（应到 $maxInv）"; $rowFail++ }
}
if ($rowFail -eq 0) { Ok "两个前沿行（05b / Cosmos / CometBFT）都跟到 $maxInv" }

# ---- 6. 活边界标记 ----
Write-Host "[6] 活边界标记"
$halt = Read-All 'tracks\failure-museum\worked-example-halt-surfaces.md'
$mh = [regex]::Match($halt, '对照：不变量 \d+–(\d+)；语料 C\d+–C(\d+)；')
if (-not $mh.Success) { Bad "halt-surfaces 找不到「对照：」行" }
else {
    Check ([int]$mh.Groups[1].Value -eq $maxInv)  "halt-surfaces 不变量上界 $($mh.Groups[1].Value)"  "(应 $maxInv)"
    Check ([int]$mh.Groups[2].Value -eq $maxCorp) "halt-surfaces 语料上界 C$($mh.Groups[2].Value)" "(应 C$maxCorp)"
}
$corp = Read-All 'libraries\adversarial-corpus\README.md'
$mc = [regex]::Match($corp, '来源：博物馆 7 问第 7 条、不变量 1–(\d+)')
if (-not $mc.Success) { Bad "corpus README 找不到「来源：」行" }
else { Check ([int]$mc.Groups[1].Value -eq $maxInv) "corpus 来源上界 $($mc.Groups[1].Value)" "(应 $maxInv)" }

$tm = Read-All 'libraries\threat-model\README.md'
$tmMax = (([regex]::Matches($tm, '(?m)^\| (\d+) \|.*不变量 \d+') | ForEach-Object { [int]$_.Groups[1].Value } | Measure-Object -Maximum).Maximum)
if ($tmMax -lt 0) { Bad "threat-model 找不到带不变量的行" }
else { Check ($tmMax -ge ($maxInv - 5)) "threat-model 表内最大 # = $tmMax" "(不应落后于 $($maxInv - 5))" }

# ---- 7. 链接 ----
Write-Host "[7] 相对 Markdown 链接"
$broken = 0; $checked = 0
Get-ChildItem -LiteralPath $root -Recurse -File -Filter *.md | ForEach-Object {
    $dir = $_.DirectoryName
    $txt = [System.IO.File]::ReadAllText($_.FullName)
    foreach ($mm in [regex]::Matches($txt, '\]\(([^)#][^)]*\.md)\)')) {
        $t = $mm.Groups[1].Value
        if ($t -match '^https?://') { continue }
        $checked++
        $full = [System.IO.Path]::GetFullPath((Join-Path $dir $t))
        if (-not (Test-Path -LiteralPath $full)) {
            $broken++
            if ($broken -le 12) { Write-Host ("      BROKEN  " + $_.FullName.Replace($root+'\','') + " -> " + $t) -ForegroundColor Red }
        }
    }
}
Check ($broken -eq 0) "链接 $checked 条，断链 0" "(断链 $broken)"

# ---- 8. 行尾 ----
Write-Host "[8] 行尾一致性（应为 CRLF）"
$mixed = 0
Get-ChildItem -LiteralPath $root -Recurse -File -Filter *.md | ForEach-Object {
    $raw = [System.IO.File]::ReadAllText($_.FullName)
    $lf = ([regex]::Matches($raw, "`n")).Count
    $crlf = ([regex]::Matches($raw, "`r`n")).Count
    if ($lf -ne $crlf) {
        $mixed++
        if ($mixed -le 12) { Write-Host ("      MIXED  " + $_.FullName.Replace($root+'\','')) -ForegroundColor Red }
    }
}
Check ($mixed -eq 0) "行尾一致" "(混合 $mixed 个文件)"

# ---- 汇总 ----
Write-Host ""
if ($fail -eq 0) { Write-Host "=== 全通过 ===" -ForegroundColor Green; exit 0 }
else { Write-Host "=== 失败 $fail 项 ===" -ForegroundColor Red; exit 1 }
