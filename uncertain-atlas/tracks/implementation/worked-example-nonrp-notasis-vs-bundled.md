# 例：看见 vote_extension 会包进 CanonicalVoteExtension is not already signed as-is interchangeable / not already CanonicalVote interchangeable / not already settled interchangeable

**层次**：实现 / vote_extension 会包进 CanonicalVoteExtension not already signed as-is / not already CanonicalVote / not already settled 正式三事（358 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「vote_extension 会包进 CanonicalVoteExtension not already signed as-is / not already CanonicalVote / not already settled 正式三事（358 余量）/ not 848 nonrp-notasis interchangeable / not 358 nonrp-vs-wrapped bundled interchangeable」，不是两份扩展两份签 bundled（358），也不是 CanonicalVoteExtension 就已经是 CanonicalVote（34），也不是回包字节不解释就已经包进 CanonicalVoteExtension（361/844）。不要另写怎样编两份扩展。

## 官方三件事

1. **看见 `vote_extension` 会包进 `CanonicalVoteExtension` / 看见绑了 Height Round ChainID 这份包装 is not already 已经按原样签 interchangeable，也不是已经两份扩展两份签 bundled（358） interchangeable / 848 nonrp-notasis interchangeable / 849 nonrp-notrp interchangeable / 358 nonrp item 2 原样签 interchangeable，也不是已经 vote_extension 会包进 CanonicalVoteExtension not already signed as-is / not already CanonicalVote / not already settled 正式三事 bundled（358 item 1 余量） interchangeable / 358 nonrp item 1 interchangeable。**  
   官方写：`ExtendVoteResponse.vote_extension` 会进 `CanonicalVoteExtension`，再填 Height、Round、ChainID 后签名。看见绑了这些字段，不是已经按应用给的字节原样签 interchangeable——本页从 358 item 1 侧钉 not already signed as-is 单句。358 nonrp vs wrapped bundled unbundling 在本页 item 1 启动。

2. **看见绑了这些字段 / 看见有包装 / 这份包装 is not already 已经是票上那份 CanonicalVote interchangeable / 34 canvote interchangeable，也不是已经两份扩展两份签 bundled（358） interchangeable / 848 nonrp-notasis interchangeable / 358 nonrp item 3 第二份 interchangeable / 850 nonrp-notsame interchangeable，也不是已经回包字节不解释就已经包进 CanonicalVoteExtension interchangeable / 361 extend-when / 844 extend-when-notsame interchangeable。**  
   官方把有包装和已经是 CanonicalVote 分开——358 bundled 第一件事常与 34 / 361 混成「看见绑了 Height Round ChainID 就已经按原样签或已经是 CanonicalVote interchangeable」，本页钉 not already CanonicalVote 单句。

3. **看见绑了这些字段 / 看见签了 / 这份包装 is not already 已经交差 interchangeable，也不是已经两份扩展两份签 bundled（358） interchangeable / 848 nonrp-notasis interchangeable / 849 nonrp-notrp interchangeable，也不是已经一轮只能交出一份扩展 interchangeable / 350 oneext interchangeable。**  
   官方把签了和已经交差分开。看见签了，不是已经交差 interchangeable。358 nonrp vs wrapped bundled unbundling 在本页 item 1 启动。

怎样编两份扩展、怎样自防重放、怎样选空是规范里的做法，本页不抄。

## 官方为什么这样拆

- **vote_extension 会包进 CanonicalVoteExtension not already signed as-is ≠ 已经按原样签 interchangeable：** 官方把包装和原样签分开。
- **看见有包装 not already CanonicalVote ≠ 34 interchangeable：** 官方把有包装和已经是 CanonicalVote 分开。
- **看见签了 not already settled ≠ 已经交差 interchangeable：** 官方把签了和已经交差分开；358 nonrp vs wrapped bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| vote_extension 会包进 CanonicalVoteExtension | 不是已经按原样签 | 不是 CanonicalVoteExtension 就已经是 CanonicalVote（34） |
| 看见有包装 | 不是已经是 CanonicalVote | 不是回包字节不解释就已经包进（361/844） |
| 看见签了 | 不是已经交差 | 不是一轮只能交出一份扩展（350） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 vote_extension 会包进 CanonicalVoteExtension not already signed as-is / not already CanonicalVote / not already settled 正式三事（358 余量），必须分开是不是已经按原样签、是不是已经是 CanonicalVote、是不是已经交差。可以跳过「看见有扩展就已经按原样签」。不要另写怎样编两份扩展。358 nonrp vs wrapped bundled unbundling 在本页 item 1 启动；续 [`worked-example-nonrp-notrp-vs-bundled.md`](worked-example-nonrp-notrp-vs-bundled.md)（不变量 849 item 2）。

## 本页不抄

- 怎样编两份扩展、怎样自防重放、怎样选空。
- 两份扩展两份签 bundled。那是不变量 358。
- non_rp_extension 按原样签。那是不变量 358 item 2 余量 / 849。
- CanonicalVoteExtension 就已经是 CanonicalVote。那是不变量 34。
- 回包字节不解释就已经包进 CanonicalVoteExtension。那是不变量 361 / 844。
