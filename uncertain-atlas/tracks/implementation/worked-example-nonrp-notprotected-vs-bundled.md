# 例：看见按原样签了 / 看见字段在 / 看见没有包装 is not already already replay-protected interchangeable / already must-fill interchangeable / already settled interchangeable

**层次**：实现 / non_rp_extension 按原样签不是已经有重放保护 not already replay-protected / not already must-fill / not already settled 正式三事（358 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「non_rp_extension 按原样签不是已经有重放保护 not already replay-protected / not already must-fill / not already settled 正式三事（358 余量）/ not 828 nonrp-notprotected interchangeable / not 358 nonrp bundled interchangeable」，不是两份扩展两份签 bundled（358），也不是 vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签（827 item 1 余量）或要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份（829 item 3 余量）。不要另写怎样编两份扩展。

## 官方三件事

规范把 Methods 里 `non_rp_extension` 由 CometBFT 签名并挂上 Precommit、**不**再套一层重放保护、和 `vote_extension` 不同 和「已经是按原样签了就已经有重放保护 interchangeable / 已经是字段在就已经必须填 interchangeable / 已经是没有包装就已经交差 interchangeable / 已经是 nonrp bundled interchangeable」分开写成三件独立的实现事，不是「看见按原样签了就已经有重放保护 interchangeable / 就已经必须填 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见按原样签了 / 看见 `non_rp_extension` 按应用给的字节原样签 / 看见没有再套一层重放保护 is not already 已经有重放保护 interchangeable / 已经 replay-protected interchangeable / 已经有 Height Round ChainID 交差 interchangeable / 358 nonrp bundled interchangeable / 350 extendonce interchangeable / nonrp-sold-as-protected interchangeable，也不是已经两份扩展两份签 bundled（358） interchangeable / 828 nonrp-notprotected interchangeable / 358 nonrp item 2 interchangeable，也不是已经 non_rp_extension 按原样签不是已经有重放保护 not already replay-protected / not already must-fill / not already settled 正式三事 bundled（358 item 2 余量） interchangeable / 358 nonrp item 2 interchangeable，也不是已经按原样签（827） interchangeable / 829 nonrp-notsame interchangeable / 350 per-height interchangeable，也不是已经一轮只能交出一份扩展就已经是每一高度一份（350） interchangeable。**  
   官方写：`non_rp_extension` 由 CometBFT 签名并挂上 Precommit，**不**再套一层重放保护，和 `vote_extension` 不同。看见按原样签了，不是已经有 Height / Round / ChainID。看见按原样签了，不是已经 replay-protected interchangeable——358 钉 bundled 三事，本页从 item 2 侧钉 not already replay-protected 单句。看见 `non_rp_extension` 按原样签，不是已经两份扩展两份签 bundled（358） interchangeable——358 钉 bundled，本页钉 item 2 第一件事。看见按原样签了，不是已经按原样签（827） interchangeable——827 另钉 item 1 的包装侧。看见按原样签了，不是已经一轮只能交出一份扩展就已经是每一高度一份（350） interchangeable——350 另钉。358 nonrp vs wrapped bundled unbundling 在本页 item 2 续。

2. **看见字段在 / 看见 non_rp_extension 字段存在 / 看见挂上 Precommit is not already 已经必须填 interchangeable / 已经 must-fill interchangeable / 已经必须填交差 interchangeable / 358 nonrp bundled interchangeable / 353 emptyverify interchangeable，也不是已经两份扩展两份签 bundled（358） interchangeable / 828 nonrp-notprotected interchangeable / 358 nonrp item 1 包装 interchangeable / 358 nonrp item 3 第二份 interchangeable，也不是已经 non_rp_extension 按原样签不是已经有重放保护 not already replay-protected / not already must-fill / not already settled 正式三事 bundled（358 item 2 余量） interchangeable / 358 nonrp item 2 interchangeable，也不是已经有重放保护（本页第一件事） interchangeable。**  
   官方写：看见字段在，不是已经必须填。看见 non_rp_extension 字段存在，不是已经 must-fill interchangeable——本页钉 not already must-fill 单句。看见挂上 Precommit，不是已经有重放保护（本页第一件事） interchangeable——三件事分开钉。358 nonrp vs wrapped bundled unbundling 在本页 item 2 续。

3. **看见没有包装 / 看见不套一层重放保护 / 看见和 vote_extension 不同 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 358 nonrp bundled interchangeable / 33 fourgates interchangeable，也不是已经两份扩展两份签 bundled（358） interchangeable / 828 nonrp-notprotected interchangeable / 358 nonrp item 1 / 358 nonrp item 3，也不是已经 non_rp_extension 按原样签不是已经有重放保护 not already replay-protected / not already must-fill / not already settled 正式三事 bundled（358 item 2 余量） interchangeable / 358 nonrp item 2 interchangeable，也不是已经有重放保护（本页第一件事） interchangeable / 已经必须填（本页第二件事） interchangeable。**  
   官方写：看见没有包装，不是已经交差。看见不套一层重放保护，不是已经 settled interchangeable——本页钉 not already settled 单句。看见和 vote_extension 不同，不是已经必须填（本页第二件事） interchangeable——三件事分开钉。358 nonrp vs wrapped bundled unbundling 在本页 item 2 续。

怎样编两份扩展、怎样自防重放、怎样选空是规范里的做法，本页不抄。两份扩展两份签 bundled（358）、vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签（358 item 1 余量 / 827）、要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份（358 item 3 余量 / 829）、CanonicalVoteExtension 就已经是 CanonicalVote（34）、一轮只能交出一份扩展就已经是每一高度一份（350）、空扩展仍会调 Verify 就已经跳过 Verify（353）是另外那套，本页不抄。

## 官方为什么这样拆

- **按原样签了 not already replay-protected ≠ 358 / 350 interchangeable：** 官方把没有包装和已经有重放保护分开。
- **字段在 not already must-fill ≠ 已经必须填 interchangeable：** 官方把字段在和已经必须填分开。
- **没有包装 not already settled ≠ 已经交差 interchangeable：** 官方把没有包装和已经交差分开；358 nonrp vs wrapped bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 按原样签了 | 不是 already replay-protected | 不是一轮只能交出一份扩展就已经是每一高度一份 alone（350） |
| 字段在 | 不是 already must-fill | 不是包装侧 already raw-signed alone（827） |
| 没有包装 | 不是 already settled | 不是第二份字段 already same-as-ve alone（829） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 non_rp_extension 按原样签不是已经有重放保护 not already replay-protected / not already must-fill / not already settled 正式三事（358 余量），必须分开按原样签了 是不是 already replay-protected interchangeable / 358 nonrp bundled interchangeable / nonrp-sold-as-protected interchangeable、字段在 是不是 already must-fill interchangeable、没有包装 是不是 already settled interchangeable。可以跳过「看见按原样签了就已经有重放保护 interchangeable / 就已经必须填 interchangeable / 就已经交差 interchangeable」。不要另写怎样编两份扩展。358 nonrp vs wrapped bundled unbundling 在本页 item 2 续（827 + 828）。

## 本页不抄

- 怎样编两份扩展、怎样自防重放、怎样选空。
- 两份扩展两份签 bundled。那是不变量 358。
- vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签。那是不变量 358 item 1 余量 / 827。
- 要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份。那是不变量 358 item 3 余量 / 829。
- CanonicalVoteExtension 就已经是 CanonicalVote。那是不变量 34。
- 一轮只能交出一份扩展就已经是每一高度一份。那是不变量 350。
- 空扩展仍会调 Verify 就已经跳过 Verify。那是不变量 353。
