# 例：看见创世 app_state is not already app-verified interchangeable / not already understood interchangeable / not already settled interchangeable

**层次**：实现 / 创世 app_state not already app-verified / not already understood / not already settled 正式三事（303 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Genesis](https://github.com/cometbft/cometbft/blob/main/spec/core/genesis.md) genesis file / app_state。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「创世 app_state not already app-verified / not already understood / not already settled 正式三事（303 余量）/ not 986 genesis-notapp interchangeable / not 303 genesis-vs-app bundled interchangeable」，不是创世 bundled（303），也不是快照已经从创世重放（38），也不是本地 State 就已经进了块（300/983）。不要另写怎样填创世字段或怎样调 InitChain。

## 官方三件事

1. **看见创世里的 app_state / 看见引擎收下这份创世 这份文件 is not already 已经验过应用状态 interchangeable，也不是已经创世 bundled（303） interchangeable / 986 genesis-notapp interchangeable / 987 genesis-nottime interchangeable / 303 genesis item 2 进程起来 interchangeable，也不是已经创世 app_state not already app-verified / not already understood / not already settled 正式三事 bundled（303 item 1 余量） interchangeable / 303 genesis item 1 interchangeable。**  
   官方写：应用往创世的 app_state 填自己要的字段。CometBFT 验不了这一段，因为它不知道应用状态由什么组成。看见创世文件齐了，不是应用段已经验过 interchangeable——本页从 303 item 1 侧钉 not already app-verified 单句。303 genesis vs app bundled unbundling 在本页 item 1 启动。

2. **看见引擎收下了 / 看见文件齐了 / 这份文件 is not already 已经懂余额 interchangeable，也不是已经创世 bundled（303） interchangeable / 986 genesis-notapp interchangeable / 303 genesis item 3 空名单 interchangeable / 988 genesis-notset interchangeable，也不是已经快照已经从创世重放 interchangeable / 38 snapshot interchangeable。**  
   官方把引擎收下了和已经懂余额分开。看见引擎收下了，不是已经懂余额 interchangeable。本页钉 not already understood 单句。

3. **看见有 app_state / 看见文件齐了 / 这份文件 is not already 已经交差 interchangeable，也不是已经创世 bundled（303） interchangeable / 986 genesis-notapp interchangeable / 987 genesis-nottime interchangeable，也不是已经本地 State 就已经进了块 interchangeable / 300/983 stategossip-notblock interchangeable。**  
   官方把有 app_state 和已经交差分开。看见有 app_state，不是已经交差 interchangeable。303 genesis vs app bundled unbundling 在本页 item 1 启动。

`time_iota_ms`、曲线名单、字段表是规范里的取值或过期项，本页不抄。

## 官方为什么这样拆

- **创世 app_state not already app-verified ≠ 已经验过应用状态 interchangeable：** 官方把引擎不认识应用状态，和文件已经收下分开。
- **看见引擎收下了 not already understood ≠ 已经懂余额 interchangeable：** 官方把引擎收下了和已经懂余额分开。
- **看见有 app_state not already settled ≠ 已经交差 interchangeable：** 官方把有 app_state 和已经交差分开；303 genesis vs app bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 创世 app_state | 不是已经验过应用状态 | 不是快照已经从创世重放（38） |
| 看见引擎收下了 | 不是已经懂余额 | 不是本地 State 就已经进了块（300/983） |
| 看见有 app_state | 不是已经交差 | 不是进程起来就已经开出块（987） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看创世 app_state not already app-verified / not already understood / not already settled 正式三事（303 余量），必须分开是不是已经验过、是不是已经懂余额、是不是已经交差。可以跳过「看见创世文件就已经验过应用」。不要另写怎样填创世字段或怎样调 InitChain。303 genesis vs app bundled unbundling 在本页 item 1 启动；续 [`worked-example-genesis-nottime-vs-bundled.md`](worked-example-genesis-nottime-vs-bundled.md)（不变量 987 item 2）。

## 本页不抄

- time_iota_ms、曲线名单、字段表、例 JSON。
- 创世 bundled。那是不变量 303。
- 快照已经从创世重放。那是不变量 38。
- 本地 State 就已经进了块。那是不变量 300/983。
