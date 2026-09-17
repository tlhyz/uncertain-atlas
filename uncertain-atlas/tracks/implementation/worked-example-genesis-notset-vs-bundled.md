# 例：看见创世 validators 空 is not already no-set interchangeable / not already no-root interchangeable / not already settled interchangeable

**层次**：实现 / 空名单 / 空根 not already no-set / not already no-root / not already settled 正式三事（303 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Genesis](https://github.com/cometbft/cometbft/blob/main/spec/core/genesis.md) genesis file / app_state。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「空名单 / 空根 not already no-set / not already no-root / not already settled 正式三事（303 余量）/ not 988 genesis-notset interchangeable / not 303 genesis-vs-app bundled interchangeable」，不是创世 bundled（303），也不是 InitChain 空名单就已经没有集合（318），也不是落盘接口就已经进了规范（300/985）。不要另写怎样填创世字段或怎样调 InitChain。

## 官方三件事

1. **看见创世 validators 空 / 看见 app_hash 空 这份空 is not already 已经没有验证者 interchangeable，也不是已经创世 bundled（303） interchangeable / 988 genesis-notset interchangeable / 986 genesis-notapp interchangeable / 987 genesis-nottime interchangeable / 303 genesis item 1 app_state interchangeable，也不是已经空名单 / 空根 not already no-set / not already no-root / not already settled 正式三事 bundled（303 item 3 余量） interchangeable / 303 genesis item 3 interchangeable。**  
   官方写：validators 可以空，若应用在 InitChain 给出集合。app_hash 起步不必填，应用也可经 InitChain 给出。看见名单空，不是已经没有验证者 interchangeable——本页从 303 item 3 侧钉 not already no-set 单句。303 genesis vs app bundled unbundling 在本页 item 3 完成。

2. **看见根空 / 看见名单空 / 这份空 is not already 已经没有状态根 interchangeable，也不是已经创世 bundled（303） interchangeable / 988 genesis-notset interchangeable / 303 genesis item 2 进程起来 interchangeable / 987 genesis-nottime interchangeable，也不是已经 InitChain 空名单就已经没有集合 interchangeable / 318 validatorupdate interchangeable。**  
   官方把根空和已经没有状态根分开。看见根空，不是已经没有状态根 interchangeable。本页钉 not already no-root 单句。

3. **看见 InitChain 被叫了 / 看见名单空 / 这份空 is not already 已经交差 interchangeable，也不是已经创世 bundled（303） interchangeable / 988 genesis-notset interchangeable / 986 genesis-notapp interchangeable，也不是已经落盘接口就已经进了规范 interchangeable / 300/985 stategossip-notspec interchangeable。**  
   官方把 InitChain 被叫了和已经过了四门分开。看见 InitChain 被叫了，不是已经交差 interchangeable。303 genesis vs app bundled unbundling 在本页 item 3 完成。

`time_iota_ms`、曲线名单、字段表是规范里的取值或过期项，本页不抄。

## 官方为什么这样拆

- **空名单 not already no-set ≠ 已经没有集合 interchangeable：** 官方把起步可以空，和 InitChain 再给分开。
- **看见根空 not already no-root ≠ 已经没有状态根 interchangeable：** 官方把根空和已经没有状态根分开。
- **看见 InitChain 被叫了 not already settled ≠ 已经交差 interchangeable：** 官方把 InitChain 被叫了和已经过了四门分开；303 genesis vs app bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 空 validators / 空 app_hash | 不是已经没有集合或根 | 不是 InitChain 空名单就已经没有集合（318） |
| 看见根空 | 不是已经没有状态根 | 不是落盘接口就已经进了规范（300/985） |
| 看见 InitChain 被叫了 | 不是已经交差 | 不是创世 app_state 就已经验过（986） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看空名单 / 空根 not already no-set / not already no-root / not already settled 正式三事（303 余量），必须分开是不是已经没有集合、是不是已经没有状态根、是不是已经交差。可以跳过「看见创世文件就已经验过应用」。不要另写怎样填创世字段或怎样调 InitChain。303 genesis vs app bundled unbundling 在本页 item 3 完成。

## 本页不抄

- time_iota_ms、曲线名单、字段表、例 JSON。
- 创世 bundled。那是不变量 303。
- InitChain 空名单就已经没有集合。那是不变量 318。
- 落盘接口就已经进了规范。那是不变量 300/985。
