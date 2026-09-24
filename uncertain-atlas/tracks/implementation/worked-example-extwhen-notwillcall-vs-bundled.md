# 例：看见到了 prevote 步 / 看见有提案 / 看见规范写了 When is not already already will-call interchangeable / already locked-value interchangeable / already settled interchangeable

**层次**：实现 / +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote not already will-call / not already locked-value / not already settled 正式三事（361 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「+2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote not already will-call / not already locked-value / not already settled 正式三事（361 余量）/ not 833 extwhen-notwillcall interchangeable / not 361 extendwhen bundled interchangeable」，不是 ExtendVote 何时调用 bundled（361），也不是 ExtendVote 调用是同步的不是已经能在返回之后再改扩展（834 item 2 余量）或回包字节不被共识算法解释不是已经是同一份扩展（835 item 3 余量）。不要另写怎样写 ExtendVote 何时调用。

## 官方三件事

规范把 Methods 里验证者处在 prevote 步、收到提案和全部块片、并且同一 `id(v)` 的 +2/3 prevote 才锁住再调 `ExtendVote` 和「已经是到了 prevote 步就已经会调 ExtendVote interchangeable / 已经是有提案就已经锁住 interchangeable / 已经是规范写了 When 就已经交差 interchangeable / 已经是 extendwhen bundled interchangeable」分开写成三件独立的实现事，不是「看见到了 prevote 步就已经会调 ExtendVote interchangeable / 就已经锁住 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见到了 prevote 步 / 看见收到提案和全部块片、并且 +2/3 prevote 同一 `id(v)` 才锁住再调 ExtendVote / 看见到了 prevote 步 is not already 已经会调 ExtendVote interchangeable / 已经 will-call interchangeable / 已经会调交差 interchangeable / 361 extendwhen bundled interchangeable / 350 extendonce interchangeable / extendwhen-sold-as-locked interchangeable，也不是已经 ExtendVote 何时调用 bundled（361） interchangeable / 833 extwhen-notwillcall interchangeable / 361 extendwhen item 1 interchangeable，也不是已经 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote not already will-call / not already locked-value / not already settled 正式三事 bundled（361 item 1 余量） interchangeable / 361 extendwhen item 1 interchangeable，也不是已经能稍后改扩展（834） interchangeable / 835 extwhen-notsameext interchangeable / 350 per-height interchangeable，也不是已经一轮只能交出一份扩展就已经是每一高度一份（350） interchangeable。**  
   官方写：验证者 *p* 处在一轮 *r*、高度 *h* 的 prevote 步，收到提议者 *q* 的提案 *v* 和全部块片，并且收到同一 `id(v)` 的 +2/3 prevote，才锁住 *v*，再调 `ExtendVote`。看见到了 prevote 步，不是已经会调。看见到了 prevote 步，不是已经 will-call interchangeable——361 钉 bundled 三事，本页从 item 1 侧钉 not already will-call 单句。看见收到提案和全部块片才锁住再调，不是已经 ExtendVote 何时调用 bundled（361） interchangeable——361 钉 bundled，本页钉 item 1 第一件事。看见到了 prevote 步，不是已经能稍后改扩展（834） interchangeable——834 另钉 item 2。看见到了 prevote 步，不是已经一轮只能交出一份扩展就已经是每一高度一份（350） interchangeable——350 另钉。361 extend-when vs locked bundled unbundling 在本页 item 1 启动。

2. **看见有提案 / 看见有提案 *v* 和全部块片 / 看见同一 `id(v)` 的 +2/3 prevote is not already 已经锁住 interchangeable / 已经 locked-value interchangeable / 已经锁住 *v* 交差 interchangeable / 361 extendwhen bundled interchangeable / 350 extendonce interchangeable，也不是已经 ExtendVote 何时调用 bundled（361） interchangeable / 833 extwhen-notwillcall interchangeable / 361 extendwhen item 2 同步 interchangeable / 361 extendwhen item 3 不解释 interchangeable，也不是已经 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote not already will-call / not already locked-value / not already settled 正式三事 bundled（361 item 1 余量） interchangeable / 361 extendwhen item 1 interchangeable，也不是已经会调 ExtendVote（本页第一件事） interchangeable。**  
   官方写：看见有提案，不是已经锁住。看见有提案 *v* 和全部块片，不是已经 locked-value interchangeable——本页钉 not already locked-value 单句。看见同一 `id(v)` 的 +2/3 prevote，不是已经会调 ExtendVote（本页第一件事） interchangeable——三件事分开钉。361 extend-when vs locked bundled unbundling 在本页 item 1 启动。

3. **看见规范写了 When / 看见 When 条款在 / 看见锁住再调写进了规范 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 361 extendwhen bundled interchangeable / 33 fourgates interchangeable，也不是已经 ExtendVote 何时调用 bundled（361） interchangeable / 833 extwhen-notwillcall interchangeable / 361 extendwhen item 2 / 361 extendwhen item 3，也不是已经 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote not already will-call / not already locked-value / not already settled 正式三事 bundled（361 item 1 余量） interchangeable / 361 extendwhen item 1 interchangeable，也不是已经会调 ExtendVote（本页第一件事） interchangeable / 已经锁住（本页第二件事） interchangeable。**  
   官方写：看见规范写了 When，不是已经交差。看见 When 条款在，不是已经 settled interchangeable——本页钉 not already settled 单句。看见锁住再调写进了规范，不是已经锁住（本页第二件事） interchangeable——三件事分开钉。361 extend-when vs locked bundled unbundling 在本页 item 1 启动。

怎样写 ExtendVote 何时调用、怎样锁住、怎样选空是规范里的做法，本页不抄。ExtendVote 何时调用 bundled（361）、ExtendVote 调用是同步的不是已经能在返回之后再改扩展（361 item 2 余量 / 834）、回包字节不被共识算法解释不是已经是同一份扩展（361 item 3 余量 / 835）、一轮只能交出一份扩展就已经是每一高度一份（350）、Process 调用是同步的就已经能稍后改裁决（354）、vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358）是另外那套，本页不抄。

## 官方为什么这样拆

- **到了 prevote 步 not already will-call ≠ 361 / 350 interchangeable：** 官方把到了 prevote 步和已经会调 ExtendVote 分开。
- **有提案 not already locked-value ≠ 已经锁住 interchangeable：** 官方把有提案和已经锁住分开。
- **规范写了 When not already settled ≠ 已经交差 interchangeable：** 官方把 When 条款和已经交差分开；361 extend-when vs locked bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 到了 prevote 步 | 不是 already will-call | 不是一轮只能交出一份扩展就已经是每一高度一份 alone（350） |
| 有提案 | 不是 already locked-value | 不是同步 already later-revise alone（834） |
| 规范写了 When | 不是 already settled | 不是不解释 already same-ext alone（835） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote not already will-call / not already locked-value / not already settled 正式三事（361 余量），必须分开到了 prevote 步 是不是 already will-call interchangeable / 361 extendwhen bundled interchangeable / extendwhen-sold-as-locked interchangeable、有提案 是不是 already locked-value interchangeable、规范写了 When 是不是 already settled interchangeable。可以跳过「看见到了 prevote 步就已经会调 ExtendVote interchangeable / 就已经锁住 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 ExtendVote 何时调用。361 extend-when vs locked bundled unbundling 在本页 item 1 启动；完成 [`worked-example-extwhen-notlaterrevise-vs-bundled.md`](worked-example-extwhen-notlaterrevise-vs-bundled.md)（不变量 834 item 2）；完成 [`worked-example-extwhen-notsameext-vs-bundled.md`](worked-example-extwhen-notsameext-vs-bundled.md)（不变量 835 item 3）。

## 本页不抄

- 怎样写 ExtendVote 何时调用、怎样锁住、怎样选空。
- ExtendVote 何时调用 bundled。那是不变量 361。
- ExtendVote 调用是同步的不是已经能在返回之后再改扩展。那是不变量 361 item 2 余量 / 834。
- 回包字节不被共识算法解释不是已经是同一份扩展。那是不变量 361 item 3 余量 / 835。
- 一轮只能交出一份扩展就已经是每一高度一份。那是不变量 350。
- Process 调用是同步的就已经能稍后改裁决。那是不变量 354。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。那是不变量 358。
