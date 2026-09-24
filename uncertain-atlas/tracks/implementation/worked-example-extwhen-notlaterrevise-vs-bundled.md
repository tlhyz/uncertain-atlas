# 例：看见是同步的 / 看见引擎在等 / 看见回了 is not already already later-revise interchangeable / already left-critical interchangeable / already settled interchangeable

**层次**：实现 / ExtendVote 调用是同步的不是已经能在返回之后再改扩展 not already later-revise / not already left-critical / not already settled 正式三事（361 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVote 调用是同步的不是已经能在返回之后再改扩展 not already later-revise / not already left-critical / not already settled 正式三事（361 余量）/ not 834 extwhen-notlaterrevise interchangeable / not 361 extendwhen bundled interchangeable」，不是 ExtendVote 何时调用 bundled（361），也不是 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote（833 item 1 余量）或回包字节不被共识算法解释不是已经是同一份扩展（835 item 3 余量）。不要另写怎样写 ExtendVote 何时调用。

## 官方三件事

规范把 Methods 里 CometBFT 调 `ExtendVote` 是同步的 和「已经是同步的就已经能在返回之后再改扩展 interchangeable / 已经是引擎在等就已经离开关键路径 interchangeable / 已经是回了就已经交差 interchangeable / 已经是 extendwhen bundled interchangeable」分开写成三件独立的实现事，不是「看见是同步的就已经能稍后改扩展 interchangeable / 就已经离开关键路径 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见是同步的 / 看见 CometBFT 调 `ExtendVote` 是同步的 / 看见引擎同步等回包 is not already 已经能在返回之后再改扩展 interchangeable / 已经 later-revise interchangeable / 已经能稍后改扩展交差 interchangeable / 361 extendwhen bundled interchangeable / 354 processwhen interchangeable / extendwhen-sold-as-locked interchangeable，也不是已经 ExtendVote 何时调用 bundled（361） interchangeable / 834 extwhen-notlaterrevise interchangeable / 361 extendwhen item 2 interchangeable，也不是已经 ExtendVote 调用是同步的不是已经能在返回之后再改扩展 not already later-revise / not already left-critical / not already settled 正式三事 bundled（361 item 2 余量） interchangeable / 361 extendwhen item 2 interchangeable，也不是已经会调 ExtendVote（833） interchangeable / 835 extwhen-notsameext interchangeable / 354 later-revise interchangeable，也不是已经 Process 调用是同步的就已经能稍后改裁决（354） interchangeable。**  
   官方写：CometBFT 调 `ExtendVote` 是同步的。看见是同步的，不是已经能稍后改扩展。看见是同步的，不是已经 later-revise interchangeable——361 钉 bundled 三事，本页从 item 2 侧钉 not already later-revise 单句。看见 CometBFT 调 `ExtendVote` 是同步的，不是已经 ExtendVote 何时调用 bundled（361） interchangeable——361 钉 bundled，本页钉 item 2 第一件事。看见是同步的，不是已经会调 ExtendVote（833） interchangeable——833 另钉 item 1。看见是同步的，不是已经 Process 调用是同步的就已经能稍后改裁决（354） interchangeable——354 另钉。361 extend-when vs locked bundled unbundling 在本页 item 2 续。

2. **看见引擎在等 / 看见引擎在等回包 / 看见同步阻塞 is not already 已经离开关键路径 interchangeable / 已经 left-critical interchangeable / 已经离开关键路径交差 interchangeable / 361 extendwhen bundled interchangeable / 354 processwhen interchangeable，也不是已经 ExtendVote 何时调用 bundled（361） interchangeable / 834 extwhen-notlaterrevise interchangeable / 361 extendwhen item 1 锁住再调 interchangeable / 361 extendwhen item 3 不解释 interchangeable，也不是已经 ExtendVote 调用是同步的不是已经能在返回之后再改扩展 not already later-revise / not already left-critical / not already settled 正式三事 bundled（361 item 2 余量） interchangeable / 361 extendwhen item 2 interchangeable，也不是已经能稍后改扩展（本页第一件事） interchangeable。**  
   官方写：看见引擎在等，不是已经离开关键路径。看见引擎在等回包，不是已经 left-critical interchangeable——本页钉 not already left-critical 单句。看见同步阻塞，不是已经能稍后改扩展（本页第一件事） interchangeable——三件事分开钉。361 extend-when vs locked bundled unbundling 在本页 item 2 续。

3. **看见回了 / 看见回包回来了 / 看见同步调用返回了 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 361 extendwhen bundled interchangeable / 33 fourgates interchangeable，也不是已经 ExtendVote 何时调用 bundled（361） interchangeable / 834 extwhen-notlaterrevise interchangeable / 361 extendwhen item 1 / 361 extendwhen item 3，也不是已经 ExtendVote 调用是同步的不是已经能在返回之后再改扩展 not already later-revise / not already left-critical / not already settled 正式三事 bundled（361 item 2 余量） interchangeable / 361 extendwhen item 2 interchangeable，也不是已经能稍后改扩展（本页第一件事） interchangeable / 已经离开关键路径（本页第二件事） interchangeable。**  
   官方写：看见回了，不是已经交差。看见回包回来了，不是已经 settled interchangeable——本页钉 not already settled 单句。看见同步调用返回了，不是已经离开关键路径（本页第二件事） interchangeable——三件事分开钉。361 extend-when vs locked bundled unbundling 在本页 item 2 续。

怎样写 ExtendVote 何时调用、怎样锁住、怎样选空是规范里的做法，本页不抄。ExtendVote 何时调用 bundled（361）、+2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote（361 item 1 余量 / 833）、回包字节不被共识算法解释不是已经是同一份扩展（361 item 3 余量 / 835）、一轮只能交出一份扩展就已经是每一高度一份（350）、Process 调用是同步的就已经能稍后改裁决（354）、vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358）是另外那套，本页不抄。

## 官方为什么这样拆

- **是同步的 not already later-revise ≠ 361 / 354 interchangeable：** 官方把同步和已经能稍后改扩展分开。
- **引擎在等 not already left-critical ≠ 已经离开关键路径 interchangeable：** 官方把引擎在等和已经离开关键路径分开。
- **回了 not already settled ≠ 已经交差 interchangeable：** 官方把回了和已经交差分开；361 extend-when vs locked bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 是同步的 | 不是 already later-revise | 不是 Process 调用是同步的就已经能稍后改裁决 alone（354） |
| 引擎在等 | 不是 already left-critical | 不是锁住再调 already will-call alone（833） |
| 回了 | 不是 already settled | 不是不解释 already same-ext alone（835） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote 调用是同步的不是已经能在返回之后再改扩展 not already later-revise / not already left-critical / not already settled 正式三事（361 余量），必须分开是同步的 是不是 already later-revise interchangeable / 361 extendwhen bundled interchangeable / extendwhen-sold-as-locked interchangeable、引擎在等 是不是 already left-critical interchangeable、回了 是不是 already settled interchangeable。可以跳过「看见是同步的就已经能稍后改扩展 interchangeable / 就已经离开关键路径 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 ExtendVote 何时调用。361 extend-when vs locked bundled unbundling 在本页 item 2 续（833 + 834）。

## 本页不抄

- 怎样写 ExtendVote 何时调用、怎样锁住、怎样选空。
- ExtendVote 何时调用 bundled。那是不变量 361。
- +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote。那是不变量 361 item 1 余量 / 833。
- 回包字节不被共识算法解释不是已经是同一份扩展。那是不变量 361 item 3 余量 / 835。
- 一轮只能交出一份扩展就已经是每一高度一份。那是不变量 350。
- Process 调用是同步的就已经能稍后改裁决。那是不变量 354。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。那是不变量 358。
