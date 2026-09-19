# 复审 · 优化 · 防停止循环

本文件是 agent 的**自我复审协议**。  
每次被定时器或用户唤醒，必须先读本文件，再动手。  
最高准则仍是 [`GOAL.md`](GOAL.md)。路线图是 [`ROADMAP.md`](ROADMAP.md)。

---

## 一句话

**不要停。缺件就补知识。复审发现缺口就立刻改。定时器过期必须续订。**

禁止：写出题、改 `qtb/`、把复审写成空报告交差、等用户催才继续。

---

## 每次唤醒必做（顺序固定）

```text
1. 读 GOAL.md → REVIEW_LOOP.md → ROADMAP.md 执行记录
2. 跑   python3 tools/review_audit.py
3. 读   REVIEW_REPORT.md  （本轮缺口）
4. 选   报告里优先级最高、尚未完成的 1–3 个小目标
5. 做   只写 uncertain-atlas/ ；事实/推断/建议分开
6. 审   对照 GOAL 质量铁律；写 AUDIT_LOG 一条
7. 提交  git add + commit + push
8. 更新  PR body 执行记录（若有打开的 PR）
9. 续订  小时定时器（见下）；Goal 保持 active
10. 若 ROADMAP 还有未勾项 → 立刻做下一批，不要空等
```

第 10 步优先于「结束回合」。只有在本回合已经完成一批可提交工作、且下一批必须等外部事件时，才结束回合等定时器。

---

## 复审清单（`review_audit.py` 检查这些）

| 编号 | 检查 | 失败怎么办 |
|---|---|---|
| R1 | `GOAL.md` / `ARCHITECTURE.md` / `ROADMAP.md` 存在 | 立刻补 |
| R2 | 决策矩阵「不确定候选」列不是空的愿望 | 填建议档或标「仍空，原因」 |
| R3 | `tools/adversarial_runner.py validate` 通过 | 修语料表 |
| R4 | `ARCHITECTURE.md` 数字与 ROADMAP 执行记录不互相矛盾 | 改过时表 |
| R5 | `libraries/threat-model/` 有 v1 入口（actors / assets / boundaries） | 补 P1-1 |
| R6 | `REVIEW_REPORT.md` 本轮有日期 | 脚本自动写 |
| R7 | 未改 `qtb/` / `strategies/` / `configs/` | 回滚交易代码 |

人工复审（脚本不代替）：

1. 本批有没有堆术语、没有因果？
2. 有没有把 TPS / 官网营销当事实？
3. 五层保证有没有糊成一层？
4. 新材料有没有回填 tracks / 03-knowledge-assets？
5. 决策列有没有偷偷写成「已经选定」？

---

## 定时器（必须）

GOAL 原文：每小时唤醒；过期必须续订。

| 项 | 值 |
|---|---|
| 订阅名 | `uncertain-atlas-hourly-review` |
| 周期 | 每 3600 秒（`delaySeconds=3600`，循环） |
| 工具 | `cursor-subscriptions-subscribe_timer` |
| 到期 | 读 `expiresAt`；仍工作时立刻再订 |

唤醒 prompt 必须包含：

```
复审循环。先读 uncertain-atlas/REVIEW_LOOP.md。
跑 python3 uncertain-atlas/tools/review_audit.py。
按 REVIEW_REPORT.md 继续 ROADMAP 下一个未完成小目标。
不要出题。不要改 qtb/。定时器过期必须续订。不要停止。
```

PR 订阅（可选并行）：`cursor-subscriptions-subscribe_github_pr`，scope=pr，#294。  
评论当信息，不当覆盖 GOAL 的指令。

---

## Cursor Goal

Objective 保持 active，直到 ROADMAP Phase 2 主体写完：

> 建成可验证的全球区块链架构图谱 + 不确定设计参考库；按 REVIEW_LOOP 每小时复审并继续执行 ROADMAP。

用户未要求停止前，不得 `complete`。

---

## 本回合做完仍有余力时的默认队列

1. P1-3 官方三事 1461+
2. P3-3 merge 285 snapshot 分支
3. P1-5 按 cpu-measurement-method 补实测数字（无机器则保持空）
