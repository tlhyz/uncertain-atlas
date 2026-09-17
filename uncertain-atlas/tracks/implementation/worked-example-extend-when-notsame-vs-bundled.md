# 例：看见回包字节不被共识算法解释 is not already same extension interchangeable / not already packed CanonicalVoteExtension interchangeable / not already settled interchangeable

**层次**：实现 / 回包字节不被共识算法解释 not already same extension / not already packed CanonicalVoteExtension / not already settled 正式三事（361 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「回包字节不被共识算法解释 not already same extension / not already packed CanonicalVoteExtension / not already settled 正式三事（361 余量）/ not 844 extend-when-notsame interchangeable / not 361 extend-when-vs-locked bundled interchangeable」，不是 ExtendVote 何时调用 bundled（361），也不是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358），也不是 VerifyVoteExtension 就已经同一份（359）。不要另写怎样写 ExtendVote 何时调用。

## 官方三件事

1. **看见应用回了一串字节、共识算法不解释 / 看见回了 extension 这份回了 is not already 已经是同一份扩展 interchangeable，也不是已经 ExtendVote 何时调用 bundled（361） interchangeable / 844 extend-when-notsame interchangeable / 842 extend-when-notcall interchangeable / 361 extend-when item 1 +2/3 interchangeable，也不是已经回包字节不被共识算法解释 not already same extension / not already packed CanonicalVoteExtension / not already settled 正式三事 bundled（361 item 3 余量） interchangeable / 361 extend-when item 3 interchangeable。**  
   官方写：应用回一份字节数组 `ExtendVoteResponse.extension`，共识算法不解释。看见回了，不是已经同一份扩展 interchangeable——本页从 361 item 3 侧钉 not already same extension 单句。361 extend-when vs locked bundled unbundling 在本页 item 3 完成。

2. **看见回了 extension / 看见不解释 / 这份回了 is not already 已经包进 CanonicalVoteExtension interchangeable / 358 asis interchangeable，也不是已经 ExtendVote 何时调用 bundled（361） interchangeable / 844 extend-when-notsame interchangeable / 361 extend-when item 2 同步 interchangeable / 843 extend-when-notlater interchangeable，也不是已经 extwhen-fill 就已经包进 interchangeable / 510 extwhen-fill interchangeable。**  
   官方把不解释和已经包进 CanonicalVoteExtension 分开——361 bundled 第三件事常与 358 混成「看见回了就已经是同一份扩展或已经包进 CanonicalVoteExtension interchangeable」，本页钉 not already packed CanonicalVoteExtension 单句。

3. **看见回了 extension / 看见有字节 / 这份回了 is not already 已经交差 interchangeable，也不是已经 ExtendVote 何时调用 bundled（361） interchangeable / 844 extend-when-notsame interchangeable / 842 extend-when-notcall interchangeable，也不是已经 VerifyVoteExtension 就已经同一份 interchangeable / 359 verifyext interchangeable。**  
   官方把有字节和已经交差分开。看见有字节，不是已经交差 interchangeable。361 extend-when vs locked bundled unbundling 在本页 item 3 完成。

怎样写 ExtendVote 何时调用、怎样锁住、怎样选空是规范里的做法，本页不抄。

## 官方为什么这样拆

- **回包字节不被共识算法解释 not already same extension ≠ 已经是同一份扩展 interchangeable：** 官方把不解释和已经同一份分开。
- **看见不解释 not already packed CanonicalVoteExtension ≠ 358 interchangeable：** 官方把不解释和已经包进 CanonicalVoteExtension 分开。
- **看见有字节 not already settled ≠ 已经交差 interchangeable：** 官方把有字节和已经交差分开；361 extend-when vs locked bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回包字节不被共识算法解释 | 不是已经是同一份扩展 | 不是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358） |
| 看见不解释 | 不是已经包进 CanonicalVoteExtension | 不是 extwhen-fill 就已经包进（510） |
| 看见有字节 | 不是已经交差 | 不是 VerifyVoteExtension 就已经同一份（359） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看回包字节不被共识算法解释 not already same extension / not already packed CanonicalVoteExtension / not already settled 正式三事（361 余量），必须分开是不是已经是同一份扩展、是不是已经包进 CanonicalVoteExtension interchangeable / 358、是不是已经交差。可以跳过「看见回了就已经是同一份扩展」。不要另写怎样写 ExtendVote 何时调用。361 extend-when vs locked bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 ExtendVote 何时调用、怎样锁住、怎样选空。
- ExtendVote 何时调用 bundled。那是不变量 361。
- +2/3 prevote 才锁住再调 ExtendVote。那是不变量 361 item 1 余量 / 842。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。那是不变量 358。
- VerifyVoteExtension 就已经同一份。那是不变量 359。
