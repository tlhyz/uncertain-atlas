# 例：看见要签原样数据可以用 non_rp is not already same as vote_extension interchangeable / not already empty still verify interchangeable / not already settled interchangeable

**层次**：实现 / 要签原样数据可以用 non_rp not already same as vote_extension / not already empty still verify / not already settled 正式三事（358 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「要签原样数据可以用 non_rp not already same as vote_extension / not already empty still verify / not already settled 正式三事（358 余量）/ not 850 nonrp-notsame interchangeable / not 358 nonrp-vs-wrapped bundled interchangeable」，不是两份扩展两份签 bundled（358），也不是空扩展仍会调 Verify 就已经跳过 Verify（353），也不是回包字节不解释就已经是同一份扩展（361/844）。不要另写怎样编两份扩展。

## 官方三件事

1. **看见应用要签原样数据可以用 `non_rp` / 看见有第二份字段 这份第二份 is not already 已经和 vote_extension 同一份 interchangeable，也不是已经两份扩展两份签 bundled（358） interchangeable / 850 nonrp-notsame interchangeable / 848 nonrp-notasis interchangeable / 358 nonrp item 1 包装 interchangeable，也不是已经要签原样数据可以用 non_rp not already same as vote_extension / not already empty still verify / not already settled 正式三事 bundled（358 item 3 余量） interchangeable / 358 nonrp item 3 interchangeable。**  
   官方写：应用若要把原样扩展数据签出去、不要包装，可以用这份字段。`non_rp_vote_extension` 可选，也可以空。看见有第二份，不是已经和第一份同一对象 interchangeable——本页从 358 item 3 侧钉 not already same as vote_extension 单句。358 nonrp vs wrapped bundled unbundling 在本页 item 3 完成。

2. **看见有第二份字段 / 看见能空 / 这份第二份 is not already 已经是空扩展仍验签 interchangeable / 353 emptyverify / 34 canvote interchangeable，也不是已经两份扩展两份签 bundled（358） interchangeable / 850 nonrp-notsame interchangeable / 358 nonrp item 2 原样签 interchangeable / 849 nonrp-notrp interchangeable，也不是已经回包字节不解释就已经是同一份扩展 interchangeable / 361 extend-when / 844 extend-when-notsame interchangeable。**  
   官方把能空和已经是空扩展仍验签分开——358 bundled 第三件事常与 353 / 361 混成「看见有第二份就已经和 vote_extension 同一份或已经是空扩展仍验签 interchangeable」，本页钉 not already empty still verify 单句。

3. **看见有第二份字段 / 看见能用 / 这份第二份 is not already 已经交差 interchangeable，也不是已经两份扩展两份签 bundled（358） interchangeable / 850 nonrp-notsame interchangeable / 848 nonrp-notasis interchangeable，也不是已经一轮只能交出一份扩展 interchangeable / 350 oneext interchangeable。**  
   官方把能用和已经交差分开。看见能用，不是已经交差 interchangeable。358 nonrp vs wrapped bundled unbundling 在本页 item 3 完成。

怎样编两份扩展、怎样自防重放、怎样选空是规范里的做法，本页不抄。

## 官方为什么这样拆

- **要签原样数据可以用 non_rp not already same as vote_extension ≠ 已经和 vote_extension 同一份 interchangeable：** 官方把第二份字段和第一份分开。
- **看见能空 not already empty still verify ≠ 353 interchangeable：** 官方把能空和已经是空扩展仍验签分开。
- **看见能用 not already settled ≠ 已经交差 interchangeable：** 官方把能用和已经交差分开；358 nonrp vs wrapped bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 要签原样数据可以用 non_rp | 不是已经和 vote_extension 同一份 | 不是空扩展仍会调 Verify 就已经跳过 Verify（353） |
| 看见能空 | 不是已经是空扩展仍验签 | 不是回包字节不解释就已经是同一份（361/844） |
| 看见能用 | 不是已经交差 | 不是一轮只能交出一份扩展（350） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看要签原样数据可以用 non_rp not already same as vote_extension / not already empty still verify / not already settled 正式三事（358 余量），必须分开是不是已经和 vote_extension 同一份、是不是已经是空扩展仍验签 interchangeable / 353、是不是已经交差。可以跳过「看见有第二份就已经和 vote_extension 同一份」。不要另写怎样编两份扩展。358 nonrp vs wrapped bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样编两份扩展、怎样自防重放、怎样选空。
- 两份扩展两份签 bundled。那是不变量 358。
- vote_extension 会包进 CanonicalVoteExtension。那是不变量 358 item 1 余量 / 848。
- 空扩展仍会调 Verify 就已经跳过 Verify。那是不变量 353。
- 回包字节不解释就已经是同一份扩展。那是不变量 361 / 844。
