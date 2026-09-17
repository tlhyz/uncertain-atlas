# 例：看见 Historical blocks may also be required is not already persist signal bundled interchangeable / not already default 0 is pruning interchangeable / not already required means persist already done interchangeable

**层次**：实现 / Commit Usage Historical blocks required not persist signal bundled / not default 0 is pruning / not required means persist already done 正式三事（491 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Commit Usage Historical blocks required not persist signal bundled / not default 0 is pruning / not required means persist already done 正式三事（491 余量）/ not 694 commitretaincaution-nothistorical interchangeable / not 491 commitretaincaution-vs-kept bundled interchangeable」，不是 Commit Usage retain_height caution 正式三事 bundled（491），也不是 persist signal（481）或 Commit 保留高度（366）。不要另写怎样填 retain_height、怎样删块、怎样开 state sync。

## 官方三件事

规范把 Commit Usage 里 Historical blocks may also be required for other purposes, e.g. auditing, replay of non-persisted heights, light client verification 和「已经 Commit Usage persist signal（481） bundled 第三件事 interchangeable / 已经 retain_height 默认 0 就等于已经在剪（366） interchangeable / 已经 Historical blocks required 就代表 persist signal 已经交差 interchangeable」分开写成三件独立的实现事，不是「看见 auditing / replay / light client 就已经 persist signal bundled interchangeable / 就已经默认 0 就等于已经在剪 interchangeable / 就已经 caution 已经验完 interchangeable」一件事：

1. **看见 Historical blocks may also be required for other purposes, e.g. auditing, replay of non-persisted heights, light client verification, and so on / 看见历史块还可能要用于审计、回放没落盘高度、轻客户端验 / Historical blocks is not already 已经 Commit Usage persist signal（481） bundled 第三件事 interchangeable / 481 commitpersist interchangeable / 已经 persist signal 段里那句 Historical blocks 就等于已经 persist 已经交差 interchangeable，也不是已经 Commit Usage retain_height caution 正式三事 bundled（491） interchangeable / 694 commitretaincaution-nothistorical interchangeable / 692 commitretaincaution-notdefault interchangeable / 491 commitretaincaution item 1 caution interchangeable，也不是已经 Historical blocks required not persist signal bundled / not default 0 is pruning / not required means persist already done 正式三事 bundled（491 item 3 余量） interchangeable / 491 commitretaincaution item 3 interchangeable。**  
   官方把 Historical blocks may also be required 和 persist signal 段里的 Historical blocks 分开写。看见 auditing / replay / light client，不是已经 persist signal bundled interchangeable——481 钉 persist signal 语境，本页从 491 item 3 侧钉 not persist signal bundled 单句。491 commitretaincaution vs kept bundled unbundling 在本页 item 3 完成。

2. **看见 Historical blocks may also be required / 看见 other purposes / 看见 auditing replay light client is not already 已经 retain_height 默认 0 就等于已经在剪（366） interchangeable / 366 retain interchangeable / 已经能剪就等于已经没有历史 interchangeable，也不是已经 Commit Usage retain_height caution 正式三事 bundled（491） interchangeable / 694 commitretaincaution-nothistorical interchangeable / 491 commitretaincaution item 2 all nodes interchangeable / 693 commitretaincaution-notgenesis interchangeable。**  
   官方把 Usage other purposes 和「默认 0 就等于已经在剪」路径分开——491 bundled 第三件事常与 366 混成「看见 may also be required 就已经默认 0 就等于已经在剪 interchangeable」，本页钉 not default 0 is pruning 单句。看见 may also be required，不是已经能剪就等于已经没有历史 interchangeable。

3. **看见 Historical blocks may also be required / 看见 caution 语境下的 other purposes / 看见 Usage 这句 is not already 已经 Historical blocks required 就代表 persist signal 已经交差 interchangeable / 已经 caution 已经验完 interchangeable / 已经切进共识就已经有完整历史（323） interchangeable / 323 snaptransition interchangeable，也不是已经 Commit Usage retain_height caution 正式三事 bundled（491） interchangeable / 694 commitretaincaution-nothistorical interchangeable / 692 commitretaincaution-notdefault interchangeable。**  
   官方把 Usage other purposes 和「required 就代表 persist 已经交差」路径分开——491 bundled 第三件事常与 481 混成「看见 Historical blocks required 就已经 persist signal 交差 interchangeable」，本页钉 not required means persist already done 单句。看见 other purposes，不是已经切进共识就已经有完整历史 interchangeable——323 钉切进共识，本页钉 caution 语境。491 commitretaincaution vs kept bundled unbundling 在本页 item 3 完成。

怎样填 retain_height、怎样删块、怎样开 state sync 是规范里的做法，本页不抄。Commit Usage retain_height caution 正式三事 bundled（491）、Use retain_height with caution（491 item 1 余量 / 692）、all nodes remove historical blocks（491 item 2 余量 / 693）、persist signal（481）、Commit 保留高度（366）是另外那套，本页不抄。

## 官方为什么这样拆

- **Historical blocks required not persist signal bundled ≠ 481 interchangeable：** 官方把 caution 段里的 other purposes 和 persist signal 段里 Historical blocks 分开。
- **Historical blocks required not default 0 is pruning ≠ 366 interchangeable：** 官方把 Usage other purposes 和默认 0 就等于已经在剪路径分开。
- **Historical blocks required not required means persist already done ≠ persist 已经交差 interchangeable：** 官方把 Usage other purposes 和 required 就代表 persist 交差路径分开；491 commitretaincaution vs kept bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Historical blocks for auditing / replay / light client | 不是 persist signal bundled（481） | 不是 caution 单句（692/491 item 1） |
| 看见 may also be required | 不是默认 0 就等于已经在剪（366） | 不是 all nodes remove（693/491 item 2） |
| 看见 Usage 这句 | 不是 required 就代表 persist 已经交差 | 不是切进共识就已经有完整历史（323） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage Historical blocks required not persist signal bundled / not default 0 is pruning / not required means persist already done 正式三事（491 余量），必须分开 Historical blocks required 是不是 persist signal bundled interchangeable / 481、是不是默认 0 就等于已经在剪 interchangeable / 366、是不是 required 就代表 persist 已经交差。可以跳过「看见 caution 段落就已经 persist signal 交差」。不要另写怎样填 retain_height。491 commitretaincaution vs kept bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样填 retain_height、怎样删块、怎样开 state sync。
- Commit Usage retain_height caution 正式三事 bundled。那是不变量 491。
- Use retain_height with caution。那是不变量 491 item 1 余量 / 692。
- all nodes remove historical blocks。那是不变量 491 item 2 余量 / 693。
- Commit Usage persist signal。那是不变量 481。
- Commit 保留高度。那是不变量 366。
