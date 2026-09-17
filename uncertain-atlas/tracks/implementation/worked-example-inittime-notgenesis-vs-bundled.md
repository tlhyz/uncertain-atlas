# 例：看见 InitChain 请求 time 是创世时间 is not already past genesis_time interchangeable / not already producing blocks interchangeable / not already settled interchangeable

**层次**：实现 / InitChain 请求 time not already past genesis_time / not already producing blocks / not already settled 正式三事（387 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「InitChain 请求 time not already past genesis_time / not already producing blocks / not already settled 正式三事（387 余量）/ not 767 inittime-notgenesis interchangeable / not 387 inittime-vs-genesis bundled interchangeable」，不是 InitChain 请求 bundled（387），也不是进程起来就已经过了 genesis_time（303），也不是 InitChain 请求余栏 app_state_bytes 就已经验过（388/766）。不要另写怎样写 InitChain 请求。

## 官方三件事

1. **看见 InitChain 请求 `time` 是创世时间 / 看见填了 time / InitChain 这份创世时间 is not already 已经过了创世文件里的 `genesis_time` interchangeable / 303 genesis interchangeable，也不是已经 InitChain 请求 bundled（387） interchangeable / 767 inittime-notgenesis interchangeable / 768 inittime-notchainid interchangeable / 387 inittime item 2 chain_id interchangeable，也不是已经 time not already past genesis_time / not already producing blocks / not already settled 正式三事 bundled（387 item 1 余量） interchangeable / 387 inittime item 1 interchangeable。**  
   官方写：`time` 是创世时间。看见填了 time，不是已经过了创世文件里的 `genesis_time` interchangeable——本页从 387 item 1 侧钉 not already past genesis_time 单句。387 inittime vs genesis bundled unbundling 在本页 item 1 启动。

2. **看见填了 time / 看见有时间 / InitChain 这份创世时间 is not already 已经开出块 interchangeable / 303 genesis interchangeable，也不是已经 InitChain 请求 bundled（387） interchangeable / 767 inittime-notgenesis interchangeable / 387 inittime item 3 initial_height interchangeable / 769 inittime-notskip interchangeable。**  
   官方把请求里的创世时间和已经开出块分开——387 bundled 第一件事常与 303 混成「看见填了 time 就已经过了 genesis_time 或已经开出块 interchangeable」，本页钉 not already producing blocks 单句。

3. **看见填了 time / 看见能填 / InitChain 这份创世时间 is not already 已经交差 interchangeable，也不是已经 InitChain 请求 bundled（387） interchangeable / 767 inittime-notgenesis interchangeable / 768 inittime-notchainid interchangeable。**  
   官方把能填 InitChain 请求 time 和已经交差分开。看见能填，不是已经交差 interchangeable。387 inittime vs genesis bundled unbundling 在本页 item 1 启动。

怎样写 InitChain 请求、怎样填时间、怎样选起步高是规范里的做法，本页不抄。

## 官方为什么这样拆

- **time not already past genesis_time ≠ 303 interchangeable：** 官方把请求里的创世时间和创世文件里的 genesis_time 分开。
- **time not already producing blocks ≠ 303 interchangeable：** 官方把有时间和已经开出块分开。
- **time not already settled ≠ 已经交差 interchangeable：** 官方把能填 time 和已经交差分开；387 inittime vs genesis bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| InitChain 请求 time 是创世时间 | 不是已经过了 genesis_time（303） | 不是 InitChain 请求 chain_id（768/387 item 2） |
| 看见填了 time | 不是已经开出块（303） | 不是 InitChain 请求 bundled（387） |
| 看见能填 | 不是已经交差 | 不是 InitChain 请求 initial_height（769/387 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 请求 time not already past genesis_time / not already producing blocks / not already settled 正式三事（387 余量），必须分开 time 是不是已经过了 genesis_time interchangeable / 303、是不是已经开出块、是不是已经交差。可以跳过「看见填了 time 就已经过了 genesis_time」。不要另写怎样写 InitChain 请求。387 inittime vs genesis bundled unbundling 在本页 item 1 启动；续 [`worked-example-inittime-notchainid-vs-bundled.md`](worked-example-inittime-notchainid-vs-bundled.md)（不变量 768 item 2）。

## 本页不抄

- 怎样写 InitChain 请求、怎样填时间、怎样选起步高。
- InitChain 请求 bundled。那是不变量 387。
- InitChain 请求 chain_id。那是不变量 387 item 2 余量 / 768。
- InitChain 请求 initial_height。那是不变量 387 item 3 余量 / 769。
- 进程起来就已经过了 genesis_time。那是不变量 303。
- InitChain 请求余栏 app_state_bytes 就已经验过。那是不变量 388 / 766。
