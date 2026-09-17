# 例：看见 InitChain 请求 initial_height 是起步块高度 is not already can skip interchangeable / not already past crash steps interchangeable / not already settled interchangeable

**层次**：实现 / InitChain 请求 initial_height not already can skip / not already past crash steps / not already settled 正式三事（387 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「InitChain 请求 initial_height not already can skip / not already past crash steps / not already settled 正式三事（387 余量）/ not 769 inittime-notskip interchangeable / not 387 inittime-vs-genesis bundled interchangeable」，不是 InitChain 请求 bundled（387），也不是启动 Info 对上就已经能跳步（320）。不要另写怎样写 InitChain 请求。

## 官方三件事

1. **看见 InitChain 请求 `initial_height` 是起步块高度 / 看见填了起步高 / InitChain 这份起步高 is not already 已经能从半截高度接着走 interchangeable / 320 infoskip interchangeable，也不是已经 InitChain 请求 bundled（387） interchangeable / 769 inittime-notskip interchangeable / 767 inittime-notgenesis interchangeable / 387 inittime item 1 time interchangeable，也不是已经 initial_height not already can skip / not already past crash steps / not already settled 正式三事 bundled（387 item 3 余量） interchangeable / 387 inittime item 3 interchangeable。**  
   官方写：`initial_height` 是起步块的高度，通常是 1。看见填了起步高，不是已经能从半截高度接着走 interchangeable——本页从 387 item 3 侧钉 not already can skip 单句。387 inittime vs genesis bundled unbundling 在本页 item 3 完成。

2. **看见填了起步高 / 看见写成 1 / InitChain 这份起步高 is not already 已经过了崩溃三步 interchangeable / 320 infoskip interchangeable，也不是已经 InitChain 请求 bundled（387） interchangeable / 769 inittime-notskip interchangeable / 387 inittime item 2 chain_id interchangeable / 768 inittime-notchainid interchangeable。**  
   官方把起步高度和已经过了崩溃三步分开——387 bundled 第三件事常与 320 混成「看见填了起步高就已经能跳步或已经过了崩溃三步 interchangeable」，本页钉 not already past crash steps 单句。

3. **看见填了起步高 / 看见有高度 / InitChain 这份起步高 is not already 已经交差 interchangeable，也不是已经 InitChain 请求 bundled（387） interchangeable / 769 inittime-notskip interchangeable / 767 inittime-notgenesis interchangeable。**  
   官方把能填 InitChain 请求 initial_height 和已经交差分开。看见有高度，不是已经交差 interchangeable。387 inittime vs genesis bundled unbundling 在本页 item 3 完成。

怎样写 InitChain 请求、怎样填时间、怎样选起步高是规范里的做法，本页不抄。

## 官方为什么这样拆

- **initial_height not already can skip ≠ 320 interchangeable：** 官方把起步高度和崩溃恢复已经能跳步分开。
- **initial_height not already past crash steps ≠ 320 interchangeable：** 官方把写成 1 和已经过了崩溃三步分开。
- **initial_height not already settled ≠ 已经交差 interchangeable：** 官方把有高度和已经交差分开；387 inittime vs genesis bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| InitChain 请求 initial_height 是起步块高度 | 不是已经能跳步（320） | 不是 InitChain 请求 time（767/387 item 1） |
| 看见填了起步高 | 不是已经过了崩溃三步（320） | 不是 InitChain 请求 bundled（387） |
| 看见有高度 | 不是已经交差 | 不是 InitChain 请求 chain_id（768/387 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 请求 initial_height not already can skip / not already past crash steps / not already settled 正式三事（387 余量），必须分开 initial_height 是不是已经能跳步 interchangeable / 320、是不是已经过了崩溃三步、是不是已经交差。可以跳过「看见填了起步高就已经能跳步」。不要另写怎样写 InitChain 请求。387 inittime vs genesis bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 InitChain 请求、怎样填时间、怎样选起步高。
- InitChain 请求 bundled。那是不变量 387。
- InitChain 请求 time。那是不变量 387 item 1 余量 / 767。
- InitChain 请求 chain_id。那是不变量 387 item 2 余量 / 768。
- 启动 Info 对上就已经能跳步。那是不变量 320。
