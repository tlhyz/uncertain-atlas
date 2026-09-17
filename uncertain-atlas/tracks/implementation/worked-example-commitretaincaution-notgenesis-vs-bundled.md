# 例：看见 all nodes remove historical blocks is not already bootstrap from genesis interchangeable / not already non-zero retain is pruning interchangeable / not already entered consensus has full history interchangeable

**层次**：实现 / Commit Usage all nodes remove historical blocks not bootstrap from genesis / not non-zero retain is pruning / not entered consensus has full history 正式三事（491 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Commit Usage all nodes remove historical blocks not bootstrap from genesis / not non-zero retain is pruning / not entered consensus has full history 正式三事（491 余量）/ not 693 commitretaincaution-notgenesis interchangeable / not 491 commitretaincaution-vs-kept bundled interchangeable」，不是 Commit Usage retain_height caution 正式三事 bundled（491），也不是切进共识就已经有完整历史（323）或从创世再装（38）。不要另写怎样填 retain_height、怎样删块、怎样开 state sync。

## 官方三件事

规范把 Commit Usage 里 If all nodes in the network remove historical blocks then this data is permanently lost … unless state sync is enabled 和「已经能从创世再装（366 / 323 / 38） interchangeable / 已经 retain_height 回了非零高度就等于已经在剪 interchangeable / 已经切进共识就已经有完整历史（323） interchangeable」分开写成三件独立的实现事，不是「看见 all nodes remove 就已经能从创世再装 interchangeable / 就已经非零高度就等于已经在剪 interchangeable / 就已经切进共识就有完整历史 interchangeable」一件事：

1. **看见 If all nodes in the network remove historical blocks then this data is permanently lost, and no new nodes will be able to join the network and bootstrap, unless state sync is enabled on the chain / 看见全网都删历史块会永久丢、除非开了 state sync 否则新节点加不进来 / all nodes is not already 已经能从创世再装（366 / 323 / 38） interchangeable / 366 retain interchangeable / 323 snaptransition interchangeable / 38 genesisreplay interchangeable / 已经单节点删完就代表全网已经剪 interchangeable，也不是已经 Commit Usage retain_height caution 正式三事 bundled（491） interchangeable / 693 commitretaincaution-notgenesis interchangeable / 692 commitretaincaution-notdefault interchangeable / 491 commitretaincaution item 1 caution interchangeable，也不是已经 all nodes remove not bootstrap from genesis / not non-zero retain is pruning / not entered consensus has full history 正式三事 bundled（491 item 2 余量） interchangeable / 491 commitretaincaution item 2 interchangeable。**  
   官方 Usage 写：If all nodes in the network remove historical blocks then this data is permanently lost … unless state sync is enabled on the chain。看见 all nodes remove，不是已经能从创世再装 interchangeable——366 钉能剪 vs 从创世装，本页从 491 item 2 侧钉 not genesis bootstrap 单句。491 commitretaincaution vs kept bundled unbundling 在本页 item 2 续。

2. **看见 all nodes remove historical blocks / 看见 permanently lost / 看见 unless state sync is not already 已经 retain_height 回了非零高度就等于已经在剪 interchangeable / 已经 caution 回了高度就等于已经在剪 interchangeable，也不是已经 Commit Usage retain_height caution 正式三事 bundled（491） interchangeable / 693 commitretaincaution-notgenesis interchangeable / 491 commitretaincaution item 3 Historical blocks interchangeable / 694 commitretaincaution-nothistorical interchangeable。**  
   官方把 Usage 全网后果和「非零 retain_height 就等于已经在剪」路径分开——491 bundled 第二件事常与 366 混成「看见 permanently lost 就已经回了非零高度就等于已经在剪 interchangeable」，本页钉 not non-zero retain is pruning 单句。看见 permanently lost / no bootstrap unless state sync，不是已经开了 state sync 就等于已经能给轻客户端验 interchangeable。

3. **看见 unless state sync is enabled / 看见 no new nodes will be able to join / 看见 all nodes is not already 已经切进共识就已经有完整历史（323） interchangeable / 323 snaptransition interchangeable / 已经 Transition to Consensus 就代表历史还在 interchangeable，也不是已经 Commit Usage retain_height caution 正式三事 bundled（491） interchangeable / 693 commitretaincaution-notgenesis interchangeable / 692 commitretaincaution-notdefault interchangeable。**  
   官方把 Usage 全网后果和切进共识就有完整历史路径分开——491 bundled 第二件事常与 323 混成「看见 unless state sync 就已经切进共识就有完整历史 interchangeable」，本页钉 not entered consensus has full history 单句。看见 all nodes remove，不是已经应用快照就已经从创世重放 interchangeable——38 钉创世重放，本页钉 caution 段里的全网后果。491 commitretaincaution vs kept bundled unbundling 在本页 item 2 续。

怎样填 retain_height、怎样删块、怎样开 state sync 是规范里的做法，本页不抄。Commit Usage retain_height caution 正式三事 bundled（491）、Use retain_height with caution（491 item 1 余量 / 692）、Historical blocks may also be required（491 item 3 余量 / 694）、切进共识就已经有完整历史（323）、从创世再装（38）是另外那套，本页不抄。

## 官方为什么这样拆

- **all nodes remove not bootstrap from genesis ≠ 366 / 323 / 38 interchangeable：** 官方把全网删历史的后果和还能从创世装路径分开。
- **all nodes remove not non-zero retain is pruning ≠ 回了非零高度就等于已经在剪 interchangeable：** 官方把 Usage 全网后果和字段回了高度就等于已经在剪路径分开。
- **all nodes remove not entered consensus has full history ≠ 323 interchangeable：** 官方把 Usage 全网后果和切进共识就有完整历史路径分开；491 commitretaincaution vs kept bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| all nodes remove → permanently lost | 不是已经能从创世再装（366 / 38） | 不是 caution 单句（692/491 item 1） |
| 看见 unless state sync | 不是非零 retain 就等于已经在剪 | 不是切进共识就已经有完整历史（323） |
| 看见 no new nodes bootstrap | 不是应用快照就已经从创世重放（38） | 不是 Historical blocks required（694/491 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage all nodes remove historical blocks not bootstrap from genesis / not non-zero retain is pruning / not entered consensus has full history 正式三事（491 余量），必须分开 all nodes remove 是不是已经能从创世再装 interchangeable / 366 / 38、是不是非零高度就等于已经在剪、是不是切进共识就有完整历史 interchangeable / 323。可以跳过「看见 caution 段落就已经能从创世再装」。不要另写怎样开 state sync。491 commitretaincaution vs kept bundled unbundling 在本页 item 2 续；完成 [`worked-example-commitretaincaution-nothistorical-vs-bundled.md`](worked-example-commitretaincaution-nothistorical-vs-bundled.md)（不变量 694 item 3）。

## 本页不抄

- 怎样填 retain_height、怎样删块、怎样开 state sync。
- Commit Usage retain_height caution 正式三事 bundled。那是不变量 491。
- Use retain_height with caution。那是不变量 491 item 1 余量 / 692。
- Historical blocks may also be required。那是不变量 491 item 3 余量 / 694。
- 切进共识就已经有完整历史。那是不变量 323。
- 应用快照就已经从创世重放。那是不变量 38。
