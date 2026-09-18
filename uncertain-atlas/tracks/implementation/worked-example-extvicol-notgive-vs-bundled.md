# 例：看见 ExtendedVoteInfo.extension_signature is not already given-to-app interchangeable / not already replay-protected interchangeable / not already settled interchangeable

**层次**：实现 / ExtendedVoteInfo.extension_signature not already given-to-app / not already replay-protected / not already settled 正式三事（421 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendedVoteInfo.extension_signature not already given-to-app / not already replay-protected / not already settled 正式三事（421 余量）/ not 1045 extvicol-notgive interchangeable / not 421 extvitable-vs-usage bundled interchangeable」，不是 ExtendedVoteInfo 表栏 bundled（421），也不是 extension_signature 已由引擎验过、交给应用再处理就已经按原样签，也不是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358）。不要另写怎样写 ExtendedVoteInfo 表栏。

## 官方三件事

1. **看见 ExtendedVoteInfo.extension_signature 是发送验证者造、CometBFT 验过的扩展签 / 看见填了 extension_signature 这份栏 is not already 已经把验过的签交给应用 interchangeable，也不是已经 ExtendedVoteInfo 表栏 bundled（421） interchangeable / 1045 extvicol-notgive interchangeable / 1043 extvicol-notextract interchangeable / 421 extvitable item 1 vote_extension interchangeable，也不是已经 ExtendedVoteInfo.extension_signature not already given-to-app / not already replay-protected / not already settled 正式三事 bundled（421 item 3 余量） interchangeable / 421 extvitable item 3 interchangeable。**  
   官方写：extension_signature 是发送验证者造、CometBFT 验过的扩展签。看见填了 extension_signature，不是已经 extension_signature 已由引擎验过、交给应用再处理那种已经按原样签 interchangeable——本页从 421 item 3 侧钉 not already given-to-app 单句。421 extvitable vs usage bundled unbundling 在本页 item 3 完成。

2. **看见验过了 / 看见填了 extension_signature / 这份栏 is not already 已经有重放保护 interchangeable，也不是已经 ExtendedVoteInfo 表栏 bundled（421） interchangeable / 1045 extvicol-notgive interchangeable / 421 extvitable item 2 non_rp interchangeable / 1044 extvicol-notsign interchangeable，也不是已经 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签 interchangeable / 358 extcanon interchangeable。**  
   官方把验过了和已经有重放保护分开。看见验过了，不是已经有重放保护 interchangeable。本页钉 not already replay-protected 单句。

3. **看见能指签 / 看见填了 extension_signature / 这份栏 is not already 已经交差 interchangeable，也不是已经 ExtendedVoteInfo 表栏 bundled（421） interchangeable / 1045 extvicol-notgive interchangeable / 1043 extvicol-notextract interchangeable，也不是已经 ExtendedVoteInfo 从本进程抽出就已经从块里抽出 interchangeable / 369 extviout interchangeable。**  
   官方把能指签和已经交差分开。看见能指签，不是已经交差 interchangeable。421 extvitable vs usage bundled unbundling 在本页 item 3 完成。

怎样写 ExtendedVoteInfo 表栏、怎样填 vote_extension、怎样填 extension_signature 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ExtendedVoteInfo.extension_signature not already given-to-app ≠ 已经把验过的签交给应用 interchangeable：** 官方把发送验证者造、CometBFT 验过的扩展签和已经把验过的签交给应用分开。
- **看见验过了 not already replay-protected ≠ 已经有重放保护 interchangeable：** 官方把验过了和已经有重放保护分开。
- **看见能指签 not already settled ≠ 已经交差 interchangeable：** 官方把能指签和已经交差分开；421 extvitable vs usage bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendedVoteInfo.extension_signature 是发送验证者造、CometBFT 验过的扩展签 | 不是已经把验过的签交给应用 | 不是 extension_signature 已由引擎验过、交给应用再处理就已经按原样签 |
| 看见验过了 | 不是已经有重放保护 | 不是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358） |
| 看见能指签 | 不是已经交差 | 不是 vote_extension 就已经从本进程抽出（1043） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendedVoteInfo.extension_signature not already given-to-app / not already replay-protected / not already settled 正式三事（421 余量），必须分开是不是已经把验过的签交给应用、是不是已经有重放保护、是不是已经交差。可以跳过「看见填了 ExtendedVoteInfo 表栏就已经从本进程抽出」。不要另写怎样写 ExtendedVoteInfo 表栏。421 extvitable vs usage bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 ExtendedVoteInfo 表栏、怎样填 vote_extension、怎样填 extension_signature。
- ExtendedVoteInfo 表栏 bundled。那是不变量 421。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。那是不变量 358。
- ExtendedVoteInfo 从本进程抽出就已经从块里抽出。那是不变量 369。
