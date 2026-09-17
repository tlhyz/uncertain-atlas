# Level 10 · 「不确定」设计工作室

优先级：研究级 / 其中决策与威胁为必学  
先修：L4 主骨架、L9 测试与失败方法、L1.5 后量子预告  
状态：决策列已填**建议档**（非选定）。威胁模型从 [`../../libraries/threat-model/INDEX.md`](../../libraries/threat-model/INDEX.md) 读，不要从 README 活页第一行扫。

| 课 | 文件 | 核心问题 |
|---|---|---|
| 10.1 | [L10-M01-decision-discipline.md](L10-M01-decision-discipline.md) | 怎样写决策才不算愿望 |
| 10.2 | [L10-M02-pq-ledger.md](L10-M02-pq-ledger.md) | 后量子工程账本先问哪些数 |
| 10.3 | [L10-M03-v1-settlement-machine.md](L10-M03-v1-settlement-machine.md) | 第一版最小机器包含什么、永远不包含什么 |
| 10.4 | [L10-M04-pq-migration.md](L10-M04-pq-migration.md) | 双算法状态机；旧签不能单独迁走账户 |

覆盖声明：L10.1→M10.1；L10.2+L10.4→M10.2；L10.3→M10.6；M10.3→[`../../libraries/threat-model/INDEX.md`](../../libraries/threat-model/INDEX.md)；M10.4→[`../../libraries/invariants/`](../../libraries/invariants/README.md)；M10.5→[`../../libraries/adversarial-corpus/`](../../libraries/adversarial-corpus/README.md)（C657+；[`../../tools/adversarial_runner.py`](../../tools/adversarial_runner.py) v0 已建）。
