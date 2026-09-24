# 例：看见决定了 / 看见先落了决定 / 看见是同步的 is not already already settled interchangeable / already app-persist interchangeable / already sync-settled interchangeable

**层次**：实现 / 先把 v 落成这一高的决定再同步调 Finalize 不是已经交差 not already settled / not already app-persist / not already sync-settled 正式三事（362 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「先把 v 落成这一高的决定再同步调 Finalize 不是已经交差 not already settled / not already app-persist / not already sync-settled 正式三事（362 余量）/ not 837 finwhen-notpersist interchangeable / not 362 finwhen bundled interchangeable」，不是 Finalize 何时调用 bundled（362），也不是 +2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize（836 item 1 余量）或应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 不是已经印进本头（838 item 3 余量）。不要另写怎样写 Finalize 何时调用。

## 官方三件事

规范把 Methods 里 *p* 先把 *v* 落成高度 *h* 的决定、再由 CometBFT 同步调 `FinalizeBlock` 和「已经是决定了就已经交差 interchangeable / 已经是先落了决定就已经落盘应用状态 interchangeable / 已经是同步的就已经交差 interchangeable / 已经是 finwhen bundled interchangeable」分开写成三件独立的实现事，不是「看见决定了就已经交差 interchangeable / 就已经落盘应用状态 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见决定了 / 看见先把 *v* 落成这一高的决定再同步调 Finalize / 看见决定了 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 362 finwhen bundled interchangeable / 335 finpersist interchangeable / finalizewhen-sold-as-decided interchangeable，也不是已经 Finalize 何时调用 bundled（362） interchangeable / 837 finwhen-notpersist interchangeable / 362 finwhen item 2 interchangeable，也不是已经先把 v 落成这一高的决定再同步调 Finalize 不是已经交差 not already settled / not already app-persist / not already sync-settled 正式三事 bundled（362 item 2 余量） interchangeable / 362 finwhen item 2 interchangeable，也不是已经会调 Finalize（836） interchangeable / 838 finwhen-notprinted interchangeable / 335 committed interchangeable，也不是已经 Finalize 改了就已经落盘（335） interchangeable。**  
   官方写：*p* 先把 *v* 落成高度 *h* 的决定，再由 CometBFT 同步调 `FinalizeBlock`。看见决定了，不是已经交差。看见决定了，不是已经 settled interchangeable——362 钉 bundled 三事，本页从 item 2 侧钉 not already settled 单句。看见先把 *v* 落成这一高的决定再同步调，不是已经 Finalize 何时调用 bundled（362） interchangeable——362 钉 bundled，本页钉 item 2 第一件事。看见决定了，不是已经会调 Finalize（836） interchangeable——836 另钉 item 1。看见决定了，不是已经 Finalize 改了就已经落盘（335） interchangeable——335 另钉。362 finalize-when vs decided bundled unbundling 在本页 item 2 续。

2. **看见先落了决定 / 看见先把 *v* 落成高度 *h* 的决定 / 看见决定落了 is not already 已经落盘应用状态 interchangeable / 已经 app-persist interchangeable / 已经落盘应用状态交差 interchangeable / 362 finwhen bundled interchangeable / 335 finpersist interchangeable，也不是已经 Finalize 何时调用 bundled（362） interchangeable / 837 finwhen-notpersist interchangeable / 362 finwhen item 1 决定再调 interchangeable / 362 finwhen item 3 ResultHash interchangeable，也不是已经先把 v 落成这一高的决定再同步调 Finalize 不是已经交差 not already settled / not already app-persist / not already sync-settled 正式三事 bundled（362 item 2 余量） interchangeable / 362 finwhen item 2 interchangeable，也不是已经交差（本页第一件事） interchangeable。**  
   官方写：看见先落了决定，不是已经落盘应用状态。看见先把 *v* 落成高度 *h* 的决定，不是已经 app-persist interchangeable——本页钉 not already app-persist 单句。看见决定落了，不是已经交差（本页第一件事） interchangeable——三件事分开钉。362 finalize-when vs decided bundled unbundling 在本页 item 2 续。

3. **看见是同步的 / 看见再同步调 Finalize / 看见 CometBFT 同步调用 is not already 已经交差 interchangeable / 已经 sync-settled interchangeable / 已经同步交差交差 interchangeable / 362 finwhen bundled interchangeable / 33 fourgates interchangeable，也不是已经 Finalize 何时调用 bundled（362） interchangeable / 837 finwhen-notpersist interchangeable / 362 finwhen item 1 / 362 finwhen item 3，也不是已经先把 v 落成这一高的决定再同步调 Finalize 不是已经交差 not already settled / not already app-persist / not already sync-settled 正式三事 bundled（362 item 2 余量） interchangeable / 362 finwhen item 2 interchangeable，也不是已经交差（本页第一件事） interchangeable / 已经落盘应用状态（本页第二件事） interchangeable。**  
   官方写：看见是同步的，不是已经交差。看见再同步调 Finalize，不是已经 sync-settled interchangeable——本页钉 not already sync-settled 单句。看见 CometBFT 同步调用，不是已经落盘应用状态（本页第二件事） interchangeable——三件事分开钉。362 finalize-when vs decided bundled unbundling 在本页 item 2 续。

怎样写 Finalize 何时调用、怎样落决定、怎样算 ResultHash 是规范里的做法，本页不抄。Finalize 何时调用 bundled（362）、+2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize（362 item 1 余量 / 836）、应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 不是已经印进本头（362 item 3 余量 / 838）、+2/3 prevote 同一 id(v) 才锁住再调 ExtendVote（361）、Finalize 改了就已经落盘（335）、本头 AppHash 就已经是本高度交差（147）是另外那套，本页不抄。

## 官方为什么这样拆

- **决定了 not already settled ≠ 362 / 335 interchangeable：** 官方把决定了和已经交差分开。
- **先落了决定 not already app-persist ≠ 已经落盘应用状态 interchangeable：** 官方把先落了决定和已经落盘应用状态分开。
- **是同步的 not already sync-settled ≠ 已经交差 interchangeable：** 官方把同步调用和已经交差分开；362 finalize-when vs decided bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 决定了 | 不是 already settled | 不是 Finalize 改了就已经落盘 alone（335） |
| 先落了决定 | 不是 already app-persist | 不是决定再调 already will-call alone（836） |
| 是同步的 | 不是 already sync-settled | 不是 ResultHash already printed alone（838） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看先把 v 落成这一高的决定再同步调 Finalize 不是已经交差 not already settled / not already app-persist / not already sync-settled 正式三事（362 余量），必须分开决定了 是不是 already settled interchangeable / 362 finwhen bundled interchangeable / finalizewhen-sold-as-decided interchangeable、先落了决定 是不是 already app-persist interchangeable、是同步的 是不是 already sync-settled interchangeable。可以跳过「看见决定了就已经交差 interchangeable / 就已经落盘应用状态 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Finalize 何时调用。362 finalize-when vs decided bundled unbundling 在本页 item 2 续（836 + 837）。

## 本页不抄

- 怎样写 Finalize 何时调用、怎样落决定、怎样算 ResultHash。
- Finalize 何时调用 bundled。那是不变量 362。
- +2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize。那是不变量 362 item 1 余量 / 836。
- 应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 不是已经印进本头。那是不变量 362 item 3 余量 / 838。
- +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote。那是不变量 361。
- Finalize 改了就已经落盘。那是不变量 335。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
