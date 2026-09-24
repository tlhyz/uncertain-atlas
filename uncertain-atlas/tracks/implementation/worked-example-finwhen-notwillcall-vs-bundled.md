# 例：看见到了这一高 / 看见有提案 / 看见规范写了 When is not already already will-call interchangeable / already decided interchangeable / already settled interchangeable

**层次**：实现 / +2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize not already will-call / not already decided / not already settled 正式三事（362 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「+2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize not already will-call / not already decided / not already settled 正式三事（362 余量）/ not 836 finwhen-notwillcall interchangeable / not 362 finwhen bundled interchangeable」，不是 Finalize 何时调用 bundled（362），也不是先把 v 落成这一高的决定再同步调 Finalize 不是已经交差（837 item 2 余量）或应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 不是已经印进本头（838 item 3 余量）。不要另写怎样写 Finalize 何时调用。

## 官方三件事

规范把 Methods 里节点处在高度 *h*、收到提案和全部块片、并且同一 `id(v)` 的 +2/3 precommit 才决定再调 `FinalizeBlock` 和「已经是到了这一高就已经会调 Finalize interchangeable / 已经是有提案就已经决定 interchangeable / 已经是规范写了 When 就已经交差 interchangeable / 已经是 finwhen bundled interchangeable」分开写成三件独立的实现事，不是「看见到了这一高就已经会调 Finalize interchangeable / 就已经决定 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见到了这一高 / 看见收到提案和全部块片、并且 +2/3 precommit 同一 `id(v)` 才决定再调 Finalize / 看见到了这一高 is not already 已经会调 Finalize interchangeable / 已经 will-call interchangeable / 已经会调交差 interchangeable / 362 finwhen bundled interchangeable / 361 extendwhen interchangeable / finalizewhen-sold-as-decided interchangeable，也不是已经 Finalize 何时调用 bundled（362） interchangeable / 836 finwhen-notwillcall interchangeable / 362 finwhen item 1 interchangeable，也不是已经 +2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize not already will-call / not already decided / not already settled 正式三事 bundled（362 item 1 余量） interchangeable / 362 finwhen item 1 interchangeable，也不是已经落成决定（837） interchangeable / 838 finwhen-notprinted interchangeable / 361 prevote interchangeable，也不是已经 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote（361） interchangeable。**  
   官方写：节点 *p* 处在高度 *h*，收到提议者 *q* 的提案 *v* 和全部块片，并且收到同一 `id(v)` 的 +2/3 precommit，才决定 *v*，再调 `FinalizeBlock`。看见到了这一高，不是已经会调。看见到了这一高，不是已经 will-call interchangeable——362 钉 bundled 三事，本页从 item 1 侧钉 not already will-call 单句。看见收到提案和全部块片才决定再调，不是已经 Finalize 何时调用 bundled（362） interchangeable——362 钉 bundled，本页钉 item 1 第一件事。看见到了这一高，不是已经落成决定（837） interchangeable——837 另钉 item 2。看见到了这一高，不是已经 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote（361） interchangeable——361 另钉。362 finalize-when vs decided bundled unbundling 在本页 item 1 启动。

2. **看见有提案 / 看见有提案 *v* 和全部块片 / 看见同一 `id(v)` 的 +2/3 precommit is not already 已经决定 interchangeable / 已经 decided interchangeable / 已经决定 *v* 交差 interchangeable / 362 finwhen bundled interchangeable / 361 extendwhen interchangeable，也不是已经 Finalize 何时调用 bundled（362） interchangeable / 836 finwhen-notwillcall interchangeable / 362 finwhen item 2 落决定 interchangeable / 362 finwhen item 3 ResultHash interchangeable，也不是已经 +2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize not already will-call / not already decided / not already settled 正式三事 bundled（362 item 1 余量） interchangeable / 362 finwhen item 1 interchangeable，也不是已经会调 Finalize（本页第一件事） interchangeable。**  
   官方写：看见有提案，不是已经决定。看见有提案 *v* 和全部块片，不是已经 decided interchangeable——本页钉 not already decided 单句。看见同一 `id(v)` 的 +2/3 precommit，不是已经会调 Finalize（本页第一件事） interchangeable——三件事分开钉。362 finalize-when vs decided bundled unbundling 在本页 item 1 启动。

3. **看见规范写了 When / 看见 When 条款在 / 看见决定再调写进了规范 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 362 finwhen bundled interchangeable / 33 fourgates interchangeable，也不是已经 Finalize 何时调用 bundled（362） interchangeable / 836 finwhen-notwillcall interchangeable / 362 finwhen item 2 / 362 finwhen item 3，也不是已经 +2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize not already will-call / not already decided / not already settled 正式三事 bundled（362 item 1 余量） interchangeable / 362 finwhen item 1 interchangeable，也不是已经会调 Finalize（本页第一件事） interchangeable / 已经决定（本页第二件事） interchangeable。**  
   官方写：看见规范写了 When，不是已经交差。看见 When 条款在，不是已经 settled interchangeable——本页钉 not already settled 单句。看见决定再调写进了规范，不是已经决定（本页第二件事） interchangeable——三件事分开钉。362 finalize-when vs decided bundled unbundling 在本页 item 1 启动。

怎样写 Finalize 何时调用、怎样落决定、怎样算 ResultHash 是规范里的做法，本页不抄。Finalize 何时调用 bundled（362）、先把 v 落成这一高的决定再同步调 Finalize 不是已经交差（362 item 2 余量 / 837）、应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 不是已经印进本头（362 item 3 余量 / 838）、+2/3 prevote 同一 id(v) 才锁住再调 ExtendVote（361）、Finalize 改了就已经落盘（335）、本头 AppHash 就已经是本高度交差（147）是另外那套，本页不抄。

## 官方为什么这样拆

- **到了这一高 not already will-call ≠ 362 / 361 interchangeable：** 官方把到了这一高和已经会调 Finalize 分开。
- **有提案 not already decided ≠ 已经决定 interchangeable：** 官方把有提案和已经决定分开。
- **规范写了 When not already settled ≠ 已经交差 interchangeable：** 官方把 When 条款和已经交差分开；362 finalize-when vs decided bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 到了这一高 | 不是 already will-call | 不是 +2/3 prevote 才锁住再调 ExtendVote alone（361） |
| 有提案 | 不是 already decided | 不是落决定 already settled alone（837） |
| 规范写了 When | 不是 already settled | 不是 ResultHash already printed alone（838） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 +2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize not already will-call / not already decided / not already settled 正式三事（362 余量），必须分开到了这一高 是不是 already will-call interchangeable / 362 finwhen bundled interchangeable / finalizewhen-sold-as-decided interchangeable、有提案 是不是 already decided interchangeable、规范写了 When 是不是 already settled interchangeable。可以跳过「看见到了这一高就已经会调 Finalize interchangeable / 就已经决定 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Finalize 何时调用。362 finalize-when vs decided bundled unbundling 在本页 item 1 启动；完成 [`worked-example-finwhen-notpersist-vs-bundled.md`](worked-example-finwhen-notpersist-vs-bundled.md)（不变量 837 item 2）；完成 [`worked-example-finwhen-notprinted-vs-bundled.md`](worked-example-finwhen-notprinted-vs-bundled.md)（不变量 838 item 3）。

## 本页不抄

- 怎样写 Finalize 何时调用、怎样落决定、怎样算 ResultHash。
- Finalize 何时调用 bundled。那是不变量 362。
- 先把 v 落成这一高的决定再同步调 Finalize 不是已经交差。那是不变量 362 item 2 余量 / 837。
- 应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 不是已经印进本头。那是不变量 362 item 3 余量 / 838。
- +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote。那是不变量 361。
- Finalize 改了就已经落盘。那是不变量 335。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
