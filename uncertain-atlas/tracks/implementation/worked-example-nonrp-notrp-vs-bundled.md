# 例：看见 non_rp_extension 按原样签 is not already has replay protection interchangeable / not already must-fill interchangeable / not already settled interchangeable

**层次**：实现 / non_rp_extension 按原样签 not already has replay protection / not already must-fill / not already settled 正式三事（358 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「non_rp_extension 按原样签 not already has replay protection / not already must-fill / not already settled 正式三事（358 余量）/ not 849 nonrp-notrp interchangeable / not 358 nonrp-vs-wrapped bundled interchangeable」，不是两份扩展两份签 bundled（358），也不是一轮只能交出一份扩展（350），也不是空扩展仍验签就已经必须填（353）。不要另写怎样编两份扩展。

## 官方三件事

1. **看见 `non_rp_extension` 按应用给的字节原样签 / 看见没有包装 这份原样 is not already 已经有重放保护 interchangeable，也不是已经两份扩展两份签 bundled（358） interchangeable / 849 nonrp-notrp interchangeable / 848 nonrp-notasis interchangeable / 358 nonrp item 1 包装 interchangeable，也不是已经 non_rp_extension 按原样签 not already has replay protection / not already must-fill / not already settled 正式三事 bundled（358 item 2 余量） interchangeable / 358 nonrp item 2 interchangeable。**  
   官方写：`non_rp_extension` 由 CometBFT 签名并挂上 Precommit，不再套一层重放保护，和 `vote_extension` 不同。看见按原样签了，不是已经有 Height / Round / ChainID interchangeable——本页从 358 item 2 侧钉 not already has replay protection 单句。358 nonrp vs wrapped bundled unbundling 在本页 item 2 续。

2. **看见没有包装 / 看见字段在 / 这份原样 is not already 已经必须填 interchangeable，也不是已经两份扩展两份签 bundled（358） interchangeable / 849 nonrp-notrp interchangeable / 358 nonrp item 3 第二份 interchangeable / 850 nonrp-notsame interchangeable，也不是已经空扩展仍验签就已经必须填 interchangeable / 353 emptyverify interchangeable。**  
   官方把字段在和已经必须填分开——358 bundled 第二件事常与 350 / 353 混成「看见按原样签了就已经有重放保护或已经必须填 interchangeable」，本页钉 not already must-fill 单句。

3. **看见没有包装 / 看见没有包装 / 这份原样 is not already 已经交差 interchangeable，也不是已经两份扩展两份签 bundled（358） interchangeable / 849 nonrp-notrp interchangeable / 848 nonrp-notasis interchangeable，也不是已经一轮只能交出一份扩展 interchangeable / 350 oneext interchangeable。**  
   官方把没有包装和已经交差分开。看见没有包装，不是已经交差 interchangeable。358 nonrp vs wrapped bundled unbundling 在本页 item 2 续。

怎样编两份扩展、怎样自防重放、怎样选空是规范里的做法，本页不抄。

## 官方为什么这样拆

- **non_rp_extension 按原样签 not already has replay protection ≠ 已经有重放保护 interchangeable：** 官方把没有包装和已经有保护分开。
- **看见字段在 not already must-fill ≠ 已经必须填 interchangeable：** 官方把字段在和已经必须填分开。
- **看见没有包装 not already settled ≠ 已经交差 interchangeable：** 官方把没有包装和已经交差分开；358 nonrp vs wrapped bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| non_rp_extension 按原样签 | 不是已经有重放保护 | 不是一轮只能交出一份扩展（350） |
| 看见字段在 | 不是已经必须填 | 不是空扩展仍验签就已经必须填（353） |
| 看见没有包装 | 不是已经交差 | 不是 vote_extension 包装就已经有保护（848） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 non_rp_extension 按原样签 not already has replay protection / not already must-fill / not already settled 正式三事（358 余量），必须分开是不是已经有重放保护、是不是已经必须填、是不是已经交差。可以跳过「看见按原样签了就已经有重放保护」。不要另写怎样编两份扩展。358 nonrp vs wrapped bundled unbundling 在本页 item 2 续；续 [`worked-example-nonrp-notsame-vs-bundled.md`](worked-example-nonrp-notsame-vs-bundled.md)（不变量 850 item 3）。

## 本页不抄

- 怎样编两份扩展、怎样自防重放、怎样选空。
- 两份扩展两份签 bundled。那是不变量 358。
- vote_extension 会包进 CanonicalVoteExtension。那是不变量 358 item 1 余量 / 848。
- 一轮只能交出一份扩展。那是不变量 350。
- 空扩展仍验签就已经必须填。那是不变量 353。
