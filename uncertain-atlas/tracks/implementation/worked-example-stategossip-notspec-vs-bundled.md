# 例：看见 State 的落盘或查询接口 is not already in-spec interchangeable / not already network-aligned interchangeable / not already settled interchangeable

**层次**：实现 / 落盘或查询接口 not already in-spec / not already network-aligned / not already settled 正式三事（300 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [State](https://github.com/cometbft/cometbft/blob/main/spec/core/state.md) Data Structures / local State object。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「落盘或查询接口 not already in-spec / not already network-aligned / not already settled 正式三事（300 余量）/ not 985 stategossip-notspec interchangeable / not 300 state-vs-gossip bundled interchangeable」，不是本地对象 bundled（300），也不是提议者选择已经对齐（56），也不是本头 LastCommit 已经是本高 +2/3（148）。不要另写怎样拼 State 字段或怎样算头上的根。

## 官方三件事

1. **看见 State 的落盘或查询接口 / 看见能读本地 State 这份接口 is not already 已经进了规范 interchangeable，也不是已经本地对象 bundled（300） interchangeable / 985 stategossip-notspec interchangeable / 983 stategossip-notblock interchangeable / 984 stategossip-notroot interchangeable / 300 state item 1 本地 State interchangeable，也不是已经落盘或查询接口 not already in-spec / not already network-aligned / not already settled 正式三事 bundled（300 item 3 余量） interchangeable / 300 state item 3 interchangeable。**  
   官方写：State 怎么落盘、怎么查询，是实现细节，不写进规范。看见能读本地 State，不是这份接口已经是规范对象 interchangeable——本页从 300 item 3 侧钉 not already in-spec 单句。300 state vs gossip bundled unbundling 在本页 item 3 完成。

2. **看见落盘了 / 看见能读本地 State / 这份接口 is not already 已经能在网上对上 interchangeable，也不是已经本地对象 bundled（300） interchangeable / 985 stategossip-notspec interchangeable / 300 state item 2 头上的根 interchangeable / 984 stategossip-notroot interchangeable，也不是已经提议者选择已经对齐 interchangeable / 56 proposer interchangeable。**  
   官方把落盘了和已经能在网上对上分开。看见落盘了，不是已经能在网上对上 interchangeable。本页钉 not already network-aligned 单句。

3. **看见查询回了字段 / 看见能读本地 State / 这份接口 is not already 已经交差 interchangeable，也不是已经本地对象 bundled（300） interchangeable / 985 stategossip-notspec interchangeable / 983 stategossip-notblock interchangeable，也不是已经本头 LastCommit 已经是本高 +2/3 interchangeable / 148 LastCommit interchangeable。**  
   官方把查询回了字段和这些字段已经进了块分开。看见查询回了字段，不是已经交差 interchangeable。300 state vs gossip bundled unbundling 在本页 item 3 完成。

验证者人数上限、字段表、创世高度取值是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **落盘或查询接口 not already in-spec ≠ 已经进了规范 interchangeable：** 官方把怎么存、怎么查写成不进规范。
- **看见落盘了 not already network-aligned ≠ 已经能在网上对上 interchangeable：** 官方把落盘了和已经能在网上对上分开。
- **看见查询回了字段 not already settled ≠ 已经交差 interchangeable：** 官方把查询回了字段和这些字段已经进了块分开；300 state vs gossip bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 落盘或查询接口 | 不是已经进了规范 | 不是提议者选择已经对齐（56） |
| 看见落盘了 | 不是已经能在网上对上 | 不是本头 LastCommit 已经是本高 +2/3（148） |
| 看见查询回了字段 | 不是已经交差 | 不是本地 State 就已经进了块（983） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看落盘或查询接口 not already in-spec / not already network-aligned / not already settled 正式三事（300 余量），必须分开是不是已经进了规范、是不是已经能在网上对上、是不是已经交差。可以跳过「看见本地 State 就已经在块里」。不要另写怎样拼 State 字段或怎样算头上的根。300 state vs gossip bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 验证者人数上限、字段表、创世高度取值。
- 本地对象 bundled。那是不变量 300。
- 提议者选择已经对齐。那是不变量 56。
- 本头 LastCommit 已经是本高 +2/3。那是不变量 148。
