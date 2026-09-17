# 例：看见头上的 Merkle 根 is not already have-State interchangeable / not already gossiped-object interchangeable / not already settled interchangeable

**层次**：实现 / 头上的根 not already have-State / not already gossiped-object / not already settled 正式三事（300 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [State](https://github.com/cometbft/cometbft/blob/main/spec/core/state.md) Data Structures / local State object。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「头上的根 not already have-State / not already gossiped-object / not already settled 正式三事（300 余量）/ not 984 stategossip-notroot interchangeable / not 300 state-vs-gossip bundled interchangeable」，不是本地对象 bundled（300），也不是快照已经从创世重放（38），也不是 LastSignBytes 对上就已经换了高度（298/982）。不要另写怎样拼 State 字段或怎样算头上的根。

## 官方三件事

1. **看见头上的 Merkle 根 / 看见验证者根或结果根 这份根 is not already 已经有了 State 对象本身 interchangeable，也不是已经本地对象 bundled（300） interchangeable / 984 stategossip-notroot interchangeable / 983 stategossip-notblock interchangeable / 300 state item 1 本地 State interchangeable，也不是已经头上的根 not already have-State / not already gossiped-object / not already settled 正式三事 bundled（300 item 2 余量） interchangeable / 300 state item 2 interchangeable。**  
   官方写：State 里的类型属于规范，因为这些对象的 Merkle 根会进块，验证时也要用到里面的值。验证者集合和交易结果从不整份写进块，只进根。看见头上有根，不是已经有了本地那份 State interchangeable——本页从 300 item 2 侧钉 not already have-State 单句。300 state vs gossip bundled unbundling 在本页 item 2 续。

2. **看见根对上了 / 看见头上有根 / 这份根 is not already 已经流言过对象 interchangeable，也不是已经本地对象 bundled（300） interchangeable / 984 stategossip-notroot interchangeable / 300 state item 3 落盘接口 interchangeable / 985 stategossip-notspec interchangeable，也不是已经快照已经从创世重放 interchangeable / 38 snapshot interchangeable。**  
   官方把根对上了和 State 对象已经流言过分开。看见根对上了，不是已经流言过对象 interchangeable。本页钉 not already gossiped-object 单句。

3. **看见头上有根 / 看见根对上了 / 这份根 is not already 已经交差 interchangeable，也不是已经本地对象 bundled（300） interchangeable / 984 stategossip-notroot interchangeable / 983 stategossip-notblock interchangeable，也不是已经 LastSignBytes 对上就已经换了高度 interchangeable / 298/982 wal-notheight interchangeable。**  
   官方把进块的是根和对象本身分开。看见头上有根，不是已经交差 interchangeable。300 state vs gossip bundled unbundling 在本页 item 2 续。

验证者人数上限、字段表、创世高度取值是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **头上的根 not already have-State ≠ 已经有了 State 对象 interchangeable：** 官方把进块的是根、验证时用值，和对象本身分开。
- **看见根对上了 not already gossiped-object ≠ 已经流言过对象 interchangeable：** 官方把根对上了和对象已经流言过分开。
- **看见头上有根 not already settled ≠ 已经交差 interchangeable：** 官方把进块的是根和对象本身分开；300 state vs gossip bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 头上的根 | 不是已经有了 State 对象 | 不是快照已经从创世重放（38） |
| 看见根对上了 | 不是已经流言过对象 | 不是 LastSignBytes 对上就已经换了高度（298/982） |
| 看见头上有根 | 不是已经交差 | 不是落盘接口就已经进了规范（985） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头上的根 not already have-State / not already gossiped-object / not already settled 正式三事（300 余量），必须分开是不是已经有了 State、是不是已经流言过对象、是不是已经交差。可以跳过「看见本地 State 就已经在块里」。不要另写怎样拼 State 字段或怎样算头上的根。300 state vs gossip bundled unbundling 在本页 item 2 续；续 [`worked-example-stategossip-notspec-vs-bundled.md`](worked-example-stategossip-notspec-vs-bundled.md)（不变量 985 item 3）。

## 本页不抄

- 验证者人数上限、字段表、创世高度取值。
- 本地对象 bundled。那是不变量 300。
- 快照已经从创世重放。那是不变量 38。
- LastSignBytes 对上就已经换了高度。那是不变量 298/982。
