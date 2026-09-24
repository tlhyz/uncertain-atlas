# 例：看见回了 / 看见有 ResultHash / 看见哈希了 is not already already printed interchangeable / already header interchangeable / already settled interchangeable

**层次**：实现 / 应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 不是已经印进本头 not already printed / not already header / not already settled 正式三事（362 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 不是已经印进本头 not already printed / not already header / not already settled 正式三事（362 余量）/ not 838 finwhen-notprinted interchangeable / not 362 finwhen bundled interchangeable」，不是 Finalize 何时调用 bundled（362），也不是 +2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize（836 item 1 余量）或先把 v 落成这一高的决定再同步调 Finalize 不是已经交差（837 item 2 余量）。不要另写怎样写 Finalize 何时调用。

## 官方三件事

规范把 Methods 里应用算出并回 `_AppHash_` 以及各笔执行输出、CometBFT 把这些输出哈希进 `_ResultHash_` 和「已经是回了就已经印进本头 interchangeable / 已经是有 ResultHash 就已经是本头 AppHash interchangeable / 已经是哈希了就已经交差 interchangeable / 已经是 finwhen bundled interchangeable」分开写成三件独立的实现事，不是「看见回了就已经印进本头 interchangeable / 就已经是本头 AppHash interchangeable / 就已经交差 interchangeable」一件事：

1. **看见回了 / 看见应用回了 AppHash 和各笔输出 / 看见回了 AppHash 与各笔输出 is not already 已经印进本头 interchangeable / 已经 printed interchangeable / 已经印进本头交差 interchangeable / 362 finwhen bundled interchangeable / 147 apphash interchangeable / finalizewhen-sold-as-decided interchangeable，也不是已经 Finalize 何时调用 bundled（362） interchangeable / 838 finwhen-notprinted interchangeable / 362 finwhen item 3 interchangeable，也不是已经应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 不是已经印进本头 not already printed / not already header / not already settled 正式三事 bundled（362 item 3 余量） interchangeable / 362 finwhen item 3 interchangeable，也不是已经会调 Finalize（836） interchangeable / 837 finwhen-notpersist interchangeable / 335 committed interchangeable，也不是已经本头 AppHash 就已经是本高度交差（147） interchangeable。**  
   官方写：应用算出并回 `_AppHash_`，以及各笔执行输出；CometBFT 把这些输出哈希进 `_ResultHash_`。看见回了，不是已经印进本头。看见回了，不是已经 printed interchangeable——362 钉 bundled 三事，本页从 item 3 侧钉 not already printed 单句。看见应用回了 AppHash 和各笔输出，不是已经 Finalize 何时调用 bundled（362） interchangeable——362 钉 bundled，本页钉 item 3 第一件事。看见回了，不是已经会调 Finalize（836） interchangeable——836 另钉 item 1。看见回了，不是已经落成决定（837） interchangeable——837 另钉 item 2。362 finalize-when vs decided bundled unbundling 在本页 item 3 完成。

2. **看见有 ResultHash / 看见引擎把输出哈希进 ResultHash / 看见有 ResultHash is not already 已经是本头 AppHash interchangeable / 已经 header interchangeable / 已经是本头 AppHash 交差 interchangeable / 362 finwhen bundled interchangeable / 147 apphash interchangeable，也不是已经 Finalize 何时调用 bundled（362） interchangeable / 838 finwhen-notprinted interchangeable / 362 finwhen item 1 决定再调 interchangeable / 362 finwhen item 2 落决定 interchangeable，也不是已经应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 不是已经印进本头 not already printed / not already header / not already settled 正式三事 bundled（362 item 3 余量） interchangeable / 362 finwhen item 3 interchangeable，也不是已经印进本头（本页第一件事） interchangeable。**  
   官方写：看见有 ResultHash，不是已经是本头 AppHash。看见引擎把输出哈希进 ResultHash，不是已经 header interchangeable——本页钉 not already header 单句。看见有 ResultHash，不是已经印进本头（本页第一件事） interchangeable——三件事分开钉。362 finalize-when vs decided bundled unbundling 在本页 item 3 完成。

3. **看见哈希了 / 看见把输出哈希进了 / 看见引擎哈希了 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 362 finwhen bundled interchangeable / 33 fourgates interchangeable，也不是已经 Finalize 何时调用 bundled（362） interchangeable / 838 finwhen-notprinted interchangeable / 362 finwhen item 1 / 362 finwhen item 2，也不是已经应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 不是已经印进本头 not already printed / not already header / not already settled 正式三事 bundled（362 item 3 余量） interchangeable / 362 finwhen item 3 interchangeable，也不是已经印进本头（本页第一件事） interchangeable / 已经是本头 AppHash（本页第二件事） interchangeable。**  
   官方写：看见哈希了，不是已经交差。看见把输出哈希进了，不是已经 settled interchangeable——本页钉 not already settled 单句。看见引擎哈希了，不是已经是本头 AppHash（本页第二件事） interchangeable——三件事分开钉。362 finalize-when vs decided bundled unbundling 在本页 item 3 完成。

怎样写 Finalize 何时调用、怎样落决定、怎样算 ResultHash 是规范里的做法，本页不抄。Finalize 何时调用 bundled（362）、+2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize（362 item 1 余量 / 836）、先把 v 落成这一高的决定再同步调 Finalize 不是已经交差（362 item 2 余量 / 837）、+2/3 prevote 同一 id(v) 才锁住再调 ExtendVote（361）、Finalize 改了就已经落盘（335）、本头 AppHash 就已经是本高度交差（147）是另外那套，本页不抄。

## 官方为什么这样拆

- **回了 not already printed ≠ 362 / 147 interchangeable：** 官方把回了和已经印进本头分开。
- **有 ResultHash not already header ≠ 已经是本头 AppHash interchangeable：** 官方把有 ResultHash 和已经是本头 AppHash 分开。
- **哈希了 not already settled ≠ 已经交差 interchangeable：** 官方把哈希了和已经交差分开；362 finalize-when vs decided bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回了 | 不是 already printed | 不是本头 AppHash 就已经是本高度交差 alone（147） |
| 有 ResultHash | 不是 already header | 不是决定再调 already will-call alone（836） |
| 哈希了 | 不是 already settled | 不是落决定 already settled alone（837） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 不是已经印进本头 not already printed / not already header / not already settled 正式三事（362 余量），必须分开回了 是不是 already printed interchangeable / 362 finwhen bundled interchangeable / finalizewhen-sold-as-decided interchangeable、有 ResultHash 是不是 already header interchangeable、哈希了 是不是 already settled interchangeable。可以跳过「看见回了就已经印进本头 interchangeable / 就已经是本头 AppHash interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Finalize 何时调用。362 finalize-when vs decided bundled unbundling 在本页 item 3 完成（836 + 837 + 838）。

## 本页不抄

- 怎样写 Finalize 何时调用、怎样落决定、怎样算 ResultHash。
- Finalize 何时调用 bundled。那是不变量 362。
- +2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize。那是不变量 362 item 1 余量 / 836。
- 先把 v 落成这一高的决定再同步调 Finalize 不是已经交差。那是不变量 362 item 2 余量 / 837。
- +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote。那是不变量 361。
- Finalize 改了就已经落盘。那是不变量 335。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
