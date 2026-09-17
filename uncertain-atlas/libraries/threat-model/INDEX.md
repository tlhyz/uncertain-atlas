# 「不确定」威胁模型 v1

状态：**v1 结构已立**（2026-09-17）。建议档，不是已选型。  
对照：[`GOAL.md`](../../GOAL.md)、[`L10-M03`](../../courses/level-10-uncertain-studio/L10-M03-v1-settlement-machine.md)、[`settlement-copy.md`](../settlement-copy.md)。

`README.md` 仍是「看见 X 被写成已经 Y」的活页清单（与语料同步）。**读威胁模型从本页开始，不要从 README 第一行扫。**

---

## 三页

| 页 | 问什么 |
|---|---|
| [actors.md](actors.md) | 谁能对结算机做什么 |
| [assets.md](assets.md) | 什么被保护、失去会怎样 |
| [boundaries.md](boundaries.md) | 五层保证与四门切在哪 |

---

## v1 默认假设（建议）

1. 结算角色 = **全节点**。轻客户端是另写的产品句，不是默认安全。
2. 一种最终性对象 **Y** = BFT commit + 该高度 AppHash（见决策矩阵 consensus 列）。
3. 应用 / 共识分离。CheckTx ≠ Prepare ≠ Process ≠ Finalize+Commit。
4. 用户签与投票签分域。
5. 第一版不做：通用世界计算机、域外 PBS、配对 KZG 当默认 DA、Altair 抽样轻客户端。

推翻任一条必须走 L10.1 记录，不得在产品文案里静默改。

---

## 与复审循环

定时器唤醒时：`review_audit.py` 检查本目录四文件是否存在。  
缺页 = P1-1 未完成。
