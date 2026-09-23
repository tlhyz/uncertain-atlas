# 例：看见有第二份 / 看见能空 / 看见能用 is not already already same-as-ve interchangeable / already empty-verify interchangeable / already settled interchangeable

**层次**：实现 / 要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份 not already same-as-ve / not already empty-verify / not already settled 正式三事（358 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份 not already same-as-ve / not already empty-verify / not already settled 正式三事（358 余量）/ not 829 nonrp-notsame interchangeable / not 358 nonrp bundled interchangeable」，不是两份扩展两份签 bundled（358），也不是 vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签（827 item 1 余量）或 non_rp_extension 按原样签不是已经有重放保护（828 item 2 余量）。不要另写怎样编两份扩展。

## 官方三件事

规范把 Methods 里应用若要把原样扩展数据签出去、不要包装，可以用这份字段、`non_rp_vote_extension` 可选也可以空 和「已经是有第二份就已经和 vote_extension 同一份 interchangeable / 已经是能空就已经是空扩展仍验签 interchangeable / 已经是能用就已经交差 interchangeable / 已经是 nonrp bundled interchangeable」分开写成三件独立的实现事，不是「看见有第二份就已经和 vote_extension 同一份 interchangeable / 就已经是空扩展仍验签 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见有第二份 / 看见应用要签原样数据可以用 `non_rp` / 看见有第二份字段 is not already 已经和 vote_extension 同一份 interchangeable / 已经 same-as-ve interchangeable / 已经和第一份同一对象交差 interchangeable / 358 nonrp bundled interchangeable / 353 emptyverify interchangeable / nonrp-sold-as-protected interchangeable，也不是已经两份扩展两份签 bundled（358） interchangeable / 829 nonrp-notsame interchangeable / 358 nonrp item 3 interchangeable，也不是已经要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份 not already same-as-ve / not already empty-verify / not already settled 正式三事 bundled（358 item 3 余量） interchangeable / 358 nonrp item 3 interchangeable，也不是已经按原样签（827） interchangeable / 828 nonrp-notprotected interchangeable / 353 skip-verify interchangeable，也不是已经空扩展仍会调 Verify 就已经跳过 Verify（353） interchangeable。**  
   官方写：应用若要把原样扩展数据签出去、不要包装，可以用这份字段。看见有第二份，不是已经和第一份同一对象。看见有第二份，不是已经 same-as-ve interchangeable——358 钉 bundled 三事，本页从 item 3 侧钉 not already same-as-ve 单句。看见应用要签原样数据可以用 `non_rp`，不是已经两份扩展两份签 bundled（358） interchangeable——358 钉 bundled，本页钉 item 3 第一件事。看见有第二份，不是已经按原样签（827） interchangeable——827 另钉 item 1。看见有第二份，不是已经有重放保护（828） interchangeable——828 另钉 item 2。358 nonrp vs wrapped bundled unbundling 在本页 item 3 完成。

2. **看见能空 / 看见 `non_rp_vote_extension` 可选也可以空 / 看见能空着 is not already 已经是空扩展仍验签 interchangeable / 已经 empty-verify interchangeable / 已经是 34 那种空扩展仍验签交差 interchangeable / 358 nonrp bundled interchangeable / 353 emptyverify interchangeable，也不是已经两份扩展两份签 bundled（358） interchangeable / 829 nonrp-notsame interchangeable / 358 nonrp item 1 包装 interchangeable / 358 nonrp item 2 原样签 interchangeable，也不是已经要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份 not already same-as-ve / not already empty-verify / not already settled 正式三事 bundled（358 item 3 余量） interchangeable / 358 nonrp item 3 interchangeable，也不是已经和 vote_extension 同一份（本页第一件事） interchangeable。**  
   官方写：看见能空，不是已经是 34 那种空扩展仍验签。看见 `non_rp_vote_extension` 可选也可以空，不是已经 empty-verify interchangeable——本页钉 not already empty-verify 单句。看见能空着，不是已经和 vote_extension 同一份（本页第一件事） interchangeable——三件事分开钉。358 nonrp vs wrapped bundled unbundling 在本页 item 3 完成。

3. **看见能用 / 看见可以用这份字段 / 看见不要包装也能签 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 358 nonrp bundled interchangeable / 33 fourgates interchangeable，也不是已经两份扩展两份签 bundled（358） interchangeable / 829 nonrp-notsame interchangeable / 358 nonrp item 1 / 358 nonrp item 2，也不是已经要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份 not already same-as-ve / not already empty-verify / not already settled 正式三事 bundled（358 item 3 余量） interchangeable / 358 nonrp item 3 interchangeable，也不是已经和 vote_extension 同一份（本页第一件事） interchangeable / 已经是空扩展仍验签（本页第二件事） interchangeable。**  
   官方写：看见能用，不是已经交差。看见可以用这份字段，不是已经 settled interchangeable——本页钉 not already settled 单句。看见不要包装也能签，不是已经是空扩展仍验签（本页第二件事） interchangeable——三件事分开钉。358 nonrp vs wrapped bundled unbundling 在本页 item 3 完成。

怎样编两份扩展、怎样自防重放、怎样选空是规范里的做法，本页不抄。两份扩展两份签 bundled（358）、vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签（358 item 1 余量 / 827）、non_rp_extension 按原样签不是已经有重放保护（358 item 2 余量 / 828）、CanonicalVoteExtension 就已经是 CanonicalVote（34）、一轮只能交出一份扩展就已经是每一高度一份（350）、空扩展仍会调 Verify 就已经跳过 Verify（353）是另外那套，本页不抄。

## 官方为什么这样拆

- **有第二份 not already same-as-ve ≠ 358 / 353 interchangeable：** 官方把第二份字段和第一份分开。
- **能空 not already empty-verify ≠ 已经是空扩展仍验签 interchangeable：** 官方把能空和已经是空扩展仍验签分开。
- **能用 not already settled ≠ 已经交差 interchangeable：** 官方把能用和已经交差分开；358 nonrp vs wrapped bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 有第二份 | 不是 already same-as-ve | 不是空扩展仍会调 Verify 就已经跳过 Verify alone（353） |
| 能空 | 不是 already empty-verify | 不是包装侧 already raw-signed alone（827） |
| 能用 | 不是 already settled | 不是原样签 already replay-protected alone（828） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份 not already same-as-ve / not already empty-verify / not already settled 正式三事（358 余量），必须分开有第二份 是不是 already same-as-ve interchangeable / 358 nonrp bundled interchangeable / nonrp-sold-as-protected interchangeable、能空 是不是 already empty-verify interchangeable、能用 是不是 already settled interchangeable。可以跳过「看见有第二份就已经和 vote_extension 同一份 interchangeable / 就已经是空扩展仍验签 interchangeable / 就已经交差 interchangeable」。不要另写怎样编两份扩展。358 nonrp vs wrapped bundled unbundling 在本页 item 3 完成（827 + 828 + 829）。

## 本页不抄

- 怎样编两份扩展、怎样自防重放、怎样选空。
- 两份扩展两份签 bundled。那是不变量 358。
- vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签。那是不变量 358 item 1 余量 / 827。
- non_rp_extension 按原样签不是已经有重放保护。那是不变量 358 item 2 余量 / 828。
- CanonicalVoteExtension 就已经是 CanonicalVote。那是不变量 34。
- 一轮只能交出一份扩展就已经是每一高度一份。那是不变量 350。
- 空扩展仍会调 Verify 就已经跳过 Verify。那是不变量 353。
