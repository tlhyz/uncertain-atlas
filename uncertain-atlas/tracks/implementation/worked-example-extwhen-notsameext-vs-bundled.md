# 例：看见回了 / 看见不解释 / 看见有字节 is not already already same-ext interchangeable / already canon-ve interchangeable / already settled interchangeable

**层次**：实现 / 回包字节不被共识算法解释不是已经是同一份扩展 not already same-ext / not already canon-ve / not already settled 正式三事（361 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「回包字节不被共识算法解释不是已经是同一份扩展 not already same-ext / not already canon-ve / not already settled 正式三事（361 余量）/ not 835 extwhen-notsameext interchangeable / not 361 extendwhen bundled interchangeable」，不是 ExtendVote 何时调用 bundled（361），也不是 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote（833 item 1 余量）或 ExtendVote 调用是同步的不是已经能在返回之后再改扩展（834 item 2 余量）。不要另写怎样写 ExtendVote 何时调用。

## 官方三件事

规范把 Methods 里应用回一份字节数组 `ExtendVoteResponse.extension`、共识算法不解释 和「已经是回了就已经是同一份扩展 interchangeable / 已经是不解释就已经包进 CanonicalVoteExtension interchangeable / 已经是有字节就已经交差 interchangeable / 已经是 extendwhen bundled interchangeable」分开写成三件独立的实现事，不是「看见回了就已经是同一份扩展 interchangeable / 就已经包进 CanonicalVoteExtension interchangeable / 就已经交差 interchangeable」一件事：

1. **看见回了 / 看见应用回了一串字节 `ExtendVoteResponse.extension` / 看见回了 extension is not already 已经是同一份扩展 interchangeable / 已经 same-ext interchangeable / 已经同一份扩展交差 interchangeable / 361 extendwhen bundled interchangeable / 338 preparenondet interchangeable / extendwhen-sold-as-locked interchangeable，也不是已经 ExtendVote 何时调用 bundled（361） interchangeable / 835 extwhen-notsameext interchangeable / 361 extendwhen item 3 interchangeable，也不是已经回包字节不被共识算法解释不是已经是同一份扩展 not already same-ext / not already canon-ve / not already settled 正式三事 bundled（361 item 3 余量） interchangeable / 361 extendwhen item 3 interchangeable，也不是已经会调 ExtendVote（833） interchangeable / 834 extwhen-notlaterrevise interchangeable / 358 nonrp interchangeable，也不是已经 ExtendVote 没有确定性要求就已经是同一份扩展（338） interchangeable。**  
   官方写：应用回一份字节数组 `ExtendVoteResponse.extension`，共识算法不解释。看见回了，不是已经同一份扩展。看见回了，不是已经 same-ext interchangeable——361 钉 bundled 三事，本页从 item 3 侧钉 not already same-ext 单句。看见应用回了一串字节，不是已经 ExtendVote 何时调用 bundled（361） interchangeable——361 钉 bundled，本页钉 item 3 第一件事。看见回了，不是已经会调 ExtendVote（833） interchangeable——833 另钉 item 1。看见回了，不是已经能稍后改扩展（834） interchangeable——834 另钉 item 2。361 extend-when vs locked bundled unbundling 在本页 item 3 完成。

2. **看见不解释 / 看见共识算法不解释 / 看见引擎不读这些字节 is not already 已经包进 CanonicalVoteExtension interchangeable / 已经 canon-ve interchangeable / 已经包进 CanonicalVoteExtension 交差 interchangeable / 361 extendwhen bundled interchangeable / 358 nonrp interchangeable，也不是已经 ExtendVote 何时调用 bundled（361） interchangeable / 835 extwhen-notsameext interchangeable / 361 extendwhen item 1 锁住再调 interchangeable / 361 extendwhen item 2 同步 interchangeable，也不是已经回包字节不被共识算法解释不是已经是同一份扩展 not already same-ext / not already canon-ve / not already settled 正式三事 bundled（361 item 3 余量） interchangeable / 361 extendwhen item 3 interchangeable，也不是已经是同一份扩展（本页第一件事） interchangeable。**  
   官方写：看见不解释，不是已经包进 `CanonicalVoteExtension`。看见共识算法不解释，不是已经 canon-ve interchangeable——本页钉 not already canon-ve 单句。看见引擎不读这些字节，不是已经是同一份扩展（本页第一件事） interchangeable——三件事分开钉。361 extend-when vs locked bundled unbundling 在本页 item 3 完成。

3. **看见有字节 / 看见回包有 extension 字段 / 看见字节数组在 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 361 extendwhen bundled interchangeable / 33 fourgates interchangeable，也不是已经 ExtendVote 何时调用 bundled（361） interchangeable / 835 extwhen-notsameext interchangeable / 361 extendwhen item 1 / 361 extendwhen item 2，也不是已经回包字节不被共识算法解释不是已经是同一份扩展 not already same-ext / not already canon-ve / not already settled 正式三事 bundled（361 item 3 余量） interchangeable / 361 extendwhen item 3 interchangeable，也不是已经是同一份扩展（本页第一件事） interchangeable / 已经包进 CanonicalVoteExtension（本页第二件事） interchangeable。**  
   官方写：看见有字节，不是已经交差。看见回包有 extension 字段，不是已经 settled interchangeable——本页钉 not already settled 单句。看见字节数组在，不是已经包进 CanonicalVoteExtension（本页第二件事） interchangeable——三件事分开钉。361 extend-when vs locked bundled unbundling 在本页 item 3 完成。

怎样写 ExtendVote 何时调用、怎样锁住、怎样选空是规范里的做法，本页不抄。ExtendVote 何时调用 bundled（361）、+2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote（361 item 1 余量 / 833）、ExtendVote 调用是同步的不是已经能在返回之后再改扩展（361 item 2 余量 / 834）、一轮只能交出一份扩展就已经是每一高度一份（350）、Process 调用是同步的就已经能稍后改裁决（354）、vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358）是另外那套，本页不抄。

## 官方为什么这样拆

- **回了 not already same-ext ≠ 361 / 338 interchangeable：** 官方把回了和已经是同一份扩展分开。
- **不解释 not already canon-ve ≠ 已经包进 CanonicalVoteExtension interchangeable：** 官方把不解释和已经包进 CanonicalVoteExtension 分开。
- **有字节 not already settled ≠ 已经交差 interchangeable：** 官方把有字节和已经交差分开；361 extend-when vs locked bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回了 | 不是 already same-ext | 不是 ExtendVote 没有确定性要求就已经是同一份扩展 alone（338） |
| 不解释 | 不是 already canon-ve | 不是锁住再调 already will-call alone（833） |
| 有字节 | 不是 already settled | 不是同步 already later-revise alone（834） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看回包字节不被共识算法解释不是已经是同一份扩展 not already same-ext / not already canon-ve / not already settled 正式三事（361 余量），必须分开回了 是不是 already same-ext interchangeable / 361 extendwhen bundled interchangeable / extendwhen-sold-as-locked interchangeable、不解释 是不是 already canon-ve interchangeable、有字节 是不是 already settled interchangeable。可以跳过「看见回了就已经是同一份扩展 interchangeable / 就已经包进 CanonicalVoteExtension interchangeable / 就已经交差 interchangeable」。不要另写怎样写 ExtendVote 何时调用。361 extend-when vs locked bundled unbundling 在本页 item 3 完成（833 + 834 + 835）。

## 本页不抄

- 怎样写 ExtendVote 何时调用、怎样锁住、怎样选空。
- ExtendVote 何时调用 bundled。那是不变量 361。
- +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote。那是不变量 361 item 1 余量 / 833。
- ExtendVote 调用是同步的不是已经能在返回之后再改扩展。那是不变量 361 item 2 余量 / 834。
- 一轮只能交出一份扩展就已经是每一高度一份。那是不变量 350。
- Process 调用是同步的就已经能稍后改裁决。那是不变量 354。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。那是不变量 358。
