# 例：看见节点已经启动 is not already past-genesis-time interchangeable / not already handshake-ready interchangeable / not already settled interchangeable

**层次**：实现 / 进程起来 not already past-genesis-time / not already handshake-ready / not already settled 正式三事（303 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Genesis](https://github.com/cometbft/cometbft/blob/main/spec/core/genesis.md) genesis file / app_state。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「进程起来 not already past-genesis-time / not already handshake-ready / not already settled 正式三事（303 余量）/ not 987 genesis-nottime interchangeable / not 303 genesis-vs-app bundled interchangeable」，不是创世 bundled（303），也不是本头 AppHash 已经交差（147），也不是头上的根就已经有了 State（300/984）。不要另写怎样填创世字段或怎样调 InitChain。

## 官方三件事

1. **看见节点已经启动 / 看见进程起来了 这份起步 is not already 已经过了 genesis_time 开始出块 interchangeable，也不是已经创世 bundled（303） interchangeable / 987 genesis-nottime interchangeable / 986 genesis-notapp interchangeable / 303 genesis item 1 app_state interchangeable，也不是已经进程起来 not already past-genesis-time / not already handshake-ready / not already settled 正式三事 bundled（303 item 2 余量） interchangeable / 303 genesis item 2 interchangeable。**  
   官方写：genesis_time 是链开始或将要开始的时间。节点若在这个时间之前起来，会空坐到指定时刻。看见进程起来了，不是已经开出块 interchangeable——本页从 303 item 2 侧钉 not already past-genesis-time 单句。303 genesis vs app bundled unbundling 在本页 item 2 续。

2. **看见握手过了 / 看见进程起来了 / 这份起步 is not already 已经过了创世时间 interchangeable，也不是已经创世 bundled（303） interchangeable / 987 genesis-nottime interchangeable / 303 genesis item 3 空名单 interchangeable / 988 genesis-notset interchangeable，也不是已经本头 AppHash 已经交差 interchangeable / 147 AppHash interchangeable。**  
   官方把握手过了和已经过了创世时间分开。看见握手过了，不是已经过了创世时间 interchangeable。本页钉 not already handshake-ready 的镜像：握手过了 not already past-genesis-time。

3. **看见本机钟到了 / 看见进程起来了 / 这份起步 is not already 已经交差 interchangeable，也不是已经创世 bundled（303） interchangeable / 987 genesis-nottime interchangeable / 986 genesis-notapp interchangeable，也不是已经头上的根就已经有了 State interchangeable / 300/984 stategossip-notroot interchangeable。**  
   官方把本机钟到了和邻居已经一起动分开。看见本机钟到了，不是已经交差 interchangeable。303 genesis vs app bundled unbundling 在本页 item 2 续。

`time_iota_ms`、曲线名单、字段表是规范里的取值或过期项，本页不抄。

## 官方为什么这样拆

- **进程起来 not already past-genesis-time ≠ 已经开出块 interchangeable：** 官方把空坐等到指定时刻，和节点已经启动分开。
- **看见握手过了 not already handshake-ready ≠ 已经过了创世时间 interchangeable：** 官方把握手过了和已经过了创世时间分开。
- **看见本机钟到了 not already settled ≠ 已经交差 interchangeable：** 官方把本机钟到了和邻居已经一起动分开；303 genesis vs app bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 空坐等到 genesis_time | 不是已经开出块 | 不是本头 AppHash 已经交差（147） |
| 看见握手过了 | 不是已经过了创世时间 | 不是头上的根就已经有了 State（300/984） |
| 看见本机钟到了 | 不是已经交差 | 不是空名单就已经没有集合（988） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看进程起来 not already past-genesis-time / not already handshake-ready / not already settled 正式三事（303 余量），必须分开是不是已经开出块、是不是已经过了创世时间、是不是已经交差。可以跳过「看见创世文件就已经验过应用」。不要另写怎样填创世字段或怎样调 InitChain。303 genesis vs app bundled unbundling 在本页 item 2 续；续 [`worked-example-genesis-notset-vs-bundled.md`](worked-example-genesis-notset-vs-bundled.md)（不变量 988 item 3）。

## 本页不抄

- time_iota_ms、曲线名单、字段表、例 JSON。
- 创世 bundled。那是不变量 303。
- 本头 AppHash 已经交差。那是不变量 147。
- 头上的根就已经有了 State。那是不变量 300/984。
