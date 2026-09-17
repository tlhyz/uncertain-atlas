# 例：看见 Use CommitResponse.retain_height with caution 不是已经 retain_height 默认 0 就等于已经在剪；看见 all nodes remove historical blocks → permanently lost / no bootstrap unless state sync 不是已经能从创世再装；看见 Historical blocks may also be required for auditing / replay / light client verification 不是已经 persist signal bundled interchangeable

**层次**：实现 / Commit Usage retain_height caution 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Use retain_height with caution 不是已经 retain_height 默认 0 就等于已经在剪 / all nodes remove historical blocks 不是已经能从创世再装 / Historical blocks required for auditing replay light client 不是已经 persist signal bundled interchangeable」，不是 Commit 保留高度 bundled 三事（366），也不是 Commit Usage persist signal bundled 第三件事（481）。不要另写怎样填 retain_height、怎样删块、怎样开 state sync。

## 官方三件事

规范把 Commit Usage 里 Use `CommitResponse.retain_height` with caution! … If all nodes remove historical blocks … Historical blocks may also be required … 写成三件独立的实现事，不是「看见 caution 段落就已经在剪、已经能从创世再装、已经 persist signal 交差」一件事：

1. **看见 Use `CommitResponse.retain_height` with caution! / 看见要慎用 retain_height 不是已经 retain_height defaults to 0 (retain all)（366） interchangeable，也不是已经 blocks below this height may be removed 那种回了高度就等于已经在剪 interchangeable，也不是已经 Commit Usage persist signal（481） bundled 第三件事 interchangeable。**  
   官方 Usage 写：Use `CommitResponse.retain_height` with caution! 看见 with caution，不是已经默认 0 全留（366）那种没填就等于已经在剪 interchangeable。看见慎用 retain_height，不是已经 Signal persist application state（481） bundled 就代表 caution 已经验完 interchangeable。看见 caution 这句，不是已经低于这个高度的块可以被删（366）第二件事 interchangeable——366 钉字段语义，本页钉 caution 语气。
2. **看见 If all nodes in the network remove historical blocks then this data is permanently lost, and no new nodes will be able to join the network and bootstrap, unless state sync is enabled on the chain / 看见全网都删历史块会永久丢、除非开了 state sync 否则新节点加不进来 不是已经能从创世再装（366 / 323 / 38） interchangeable，也不是已经 retain_height 回了非零高度就等于已经在剪 interchangeable，也不是已经切进共识就已经有完整历史（323）。**  
   官方 Usage 写：If all nodes in the network remove historical blocks then this data is permanently lost, and no new nodes will be able to join the network and bootstrap, unless state sync is enabled on the chain。看见 all nodes remove，不是已经单节点删完就代表全网已经剪 interchangeable。看见 permanently lost / no bootstrap unless state sync，不是已经能从创世再装（366 第三件事） interchangeable——366 钉能剪 vs 从创世装，本页钉 caution 段里的全网后果。看见 unless state sync，不是已经开了 state sync 就等于已经能给轻客户端验 interchangeable。
3. **看见 Historical blocks may also be required for other purposes, e.g. auditing, replay of non-persisted heights, light client verification, and so on / 看见历史块还可能要用于审计、回放没落盘高度、轻客户端验 不是已经 Commit Usage persist signal（481） bundled 第三件事 interchangeable，也不是已经 retain_height 默认 0 就等于已经在剪（366） interchangeable，也不是已经 Historical blocks required 就代表 persist signal 已经交差 interchangeable。**  
   官方把 Historical blocks may also be required 和 caution / all nodes remove 分开写。看见 auditing / replay / light client，不是已经 persist signal 段里那句 Historical blocks 就等于已经 persist 已经交差 interchangeable——481 钉 persist signal 语境，本页钉 caution 语境。看见 may also be required，不是已经能剪就等于已经没有历史。看见 other purposes，不是已经切进共识就已经有完整历史（323） interchangeable。

怎样填 retain_height、怎样删块、怎样开 state sync 是规范里的做法，本页不抄。Commit 保留高度（366）、Commit Usage persist signal（481）、切进共识就已经有完整历史（323）、应用快照就已经从创世重放（38）是另外那套，本页不抄。

## 官方为什么这样拆

- **Use retain_height with caution ≠ retain_height 默认 0 就等于已经在剪：** 官方把 caution 语气和字段默认全留分开。
- **all nodes remove historical blocks → permanently lost / no bootstrap unless state sync ≠ 已经能从创世再装：** 官方把全网删历史的后果和还能从创世装分开。
- **Historical blocks required for auditing / replay / light client ≠ persist signal bundled interchangeable：** 官方把 caution 段里的 other purposes 和 persist signal 段里的 Historical blocks 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Use retain_height with caution | 不是 retain_height 默认 0 就等于已经在剪 | 不是 Commit 保留高度（366） |
| all nodes remove → permanently lost / no bootstrap unless state sync | 不是已经能从创世再装 | 不是切进共识就已经有完整历史（323） |
| Historical blocks for auditing / replay / light client | 不是 persist signal bundled | 不是 Commit Usage persist signal（481） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage retain_height caution，必须分开 Use retain_height with caution 是不是 retain_height 默认 0 就等于已经在剪、all nodes remove historical blocks 是不是已经能从创世再装 / 已经开了 state sync 就交差、Historical blocks required for auditing / replay / light client 是不是已经 persist signal bundled interchangeable。可以跳过「看见 caution 段落就已经在剪」。不要另写怎样填 retain_height。491 commitretaincaution vs kept bundled unbundling 续（677 item 1 / 678 item 2）；精读 [`worked-example-commitretaincaution-notbootstrap-vs-bundled.md`](worked-example-commitretaincaution-notbootstrap-vs-bundled.md)（不变量 678 item 2）。

## 本页不抄

- 怎样填 retain_height、怎样删块、怎样开 state sync。
- Commit 保留高度。那是不变量 366。
- Commit Usage persist signal。那是不变量 481。
- 切进共识就已经有完整历史。那是不变量 323。
- 应用快照就已经从创世重放。那是不变量 38。
- 崩溃恢复三步就已经 Commit。那是不变量 320。
