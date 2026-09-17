# 例：看见 State 对象 is not already in-block interchangeable / not already gossiped interchangeable / not already settled interchangeable

**层次**：实现 / 本地 State not already in-block / not already gossiped / not already settled 正式三事（300 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [State](https://github.com/cometbft/cometbft/blob/main/spec/core/state.md) Data Structures / local State object。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「本地 State not already in-block / not already gossiped / not already settled 正式三事（300 余量）/ not 983 stategossip-notblock interchangeable / not 300 state-vs-gossip bundled interchangeable」，不是本地对象 bundled（300），也不是本头 AppHash 已经交差（147），也不是写下就已经刷盘（298/980）。不要另写怎样拼 State 字段或怎样算头上的根。

## 官方三件事

1. **看见 State 对象 / 看见本地 State 这份对象 is not already 已经写进块 interchangeable，也不是已经本地对象 bundled（300） interchangeable / 983 stategossip-notblock interchangeable / 984 stategossip-notroot interchangeable / 300 state item 2 头上的根 interchangeable，也不是已经本地 State not already in-block / not already gossiped / not already settled 正式三事 bundled（300 item 1 余量） interchangeable / 300 state item 1 interchangeable。**  
   官方写：State 对象本身是实现细节。它从不写进块，也不在网上流言，也不给它算哈希。看见本机有一份 State，不是这份已经进了某块 interchangeable——本页从 300 item 1 侧钉 not already in-block 单句。300 state vs gossip bundled unbundling 在本页 item 1 启动。

2. **看见能读到它 / 看见字段齐了 / 这份对象 is not already 已经流言 interchangeable，也不是已经本地对象 bundled（300） interchangeable / 983 stategossip-notblock interchangeable / 300 state item 3 落盘接口 interchangeable / 985 stategossip-notspec interchangeable，也不是已经本头 AppHash 已经交差 interchangeable / 147 AppHash interchangeable。**  
   官方把能读到它和邻居已经收到同一份分开。看见能读到它，不是已经流言 interchangeable。本页钉 not already gossiped 单句。

3. **看见字段齐了 / 看见本地 State / 这份对象 is not already 已经交差 interchangeable，也不是已经本地对象 bundled（300） interchangeable / 983 stategossip-notblock interchangeable / 984 stategossip-notroot interchangeable，也不是已经写下就已经刷盘 interchangeable / 298/980 wal-notfsync interchangeable。**  
   官方把字段齐了和已经有一个 State 哈希可以对分开。看见字段齐了，不是已经交差 interchangeable。300 state vs gossip bundled unbundling 在本页 item 1 启动。

验证者人数上限、字段表、创世高度取值是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **本地 State not already in-block ≠ 已经写进块 interchangeable：** 官方把本地这份对象写成实现细节，从不进块、不流言、不算哈希。
- **看见能读到它 not already gossiped ≠ 已经流言 interchangeable：** 官方把能读到它和邻居已经收到同一份分开。
- **看见字段齐了 not already settled ≠ 已经交差 interchangeable：** 官方把字段齐了和已经有一个 State 哈希可以对分开；300 state vs gossip bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 本地 State | 不是已经进了块，也不是已经流言 | 不是本头 AppHash 已经交差（147） |
| 看见能读到它 | 不是已经流言 | 不是写下就已经刷盘（298/980） |
| 看见字段齐了 | 不是已经交差 | 不是头上的根就已经有了 State（984） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看本地 State not already in-block / not already gossiped / not already settled 正式三事（300 余量），必须分开是不是已经进了块、是不是已经流言、是不是已经交差。可以跳过「看见本地 State 就已经在块里」。不要另写怎样拼 State 字段或怎样算头上的根。300 state vs gossip bundled unbundling 在本页 item 1 启动；续 [`worked-example-stategossip-notroot-vs-bundled.md`](worked-example-stategossip-notroot-vs-bundled.md)（不变量 984 item 2）。

## 本页不抄

- 验证者人数上限、字段表、创世高度取值。
- 本地对象 bundled。那是不变量 300。
- 本头 AppHash 已经交差。那是不变量 147。
- 写下就已经刷盘。那是不变量 298/980。
