# 例：看见 ExtendedVoteInfo.vote_extension is not already extracted interchangeable / not already packed interchangeable / not already settled interchangeable

**层次**：实现 / ExtendedVoteInfo.vote_extension not already extracted / not already packed / not already settled 正式三事（421 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendedVoteInfo.vote_extension not already extracted / not already packed / not already settled 正式三事（421 余量）/ not 1043 extvicol-notextract interchangeable / not 421 extvitable-vs-usage bundled interchangeable」，不是 ExtendedVoteInfo 表栏 bundled（421），也不是 ExtendedVoteInfo 从本进程抽出就已经从块里抽出（369），也不是 ExtendVoteResponse.vote_extension 就已经会包进 CanonicalVoteExtension（418）。不要另写怎样写 ExtendedVoteInfo 表栏。

## 官方三件事

1. **看见 ExtendedVoteInfo.vote_extension 是发送验证者的应用给的非确定扩展 / 看见填了 vote_extension 这份栏 is not already 已经从本进程抽出 interchangeable，也不是已经 ExtendedVoteInfo 表栏 bundled（421） interchangeable / 1043 extvicol-notextract interchangeable / 1044 extvicol-notsign interchangeable / 421 extvitable item 2 non_rp interchangeable，也不是已经 ExtendedVoteInfo.vote_extension not already extracted / not already packed / not already settled 正式三事 bundled（421 item 1 余量） interchangeable / 421 extvitable item 1 interchangeable。**  
   官方写：vote_extension 是发送验证者的应用给的非确定扩展。看见填了 vote_extension，不是已经 ExtendedVoteInfo 从本进程的 CometBFT 数据结构抽出那种已经从块里抽出 interchangeable——本页从 421 item 1 侧钉 not already extracted 单句。421 extvitable vs usage bundled unbundling 在本页 item 1 启动。

2. **看见是应用给的 / 看见填了 vote_extension / 这份栏 is not already 已经会包进 CanonicalVoteExtension interchangeable，也不是已经 ExtendedVoteInfo 表栏 bundled（421） interchangeable / 1043 extvicol-notextract interchangeable / 421 extvitable item 3 signature interchangeable / 1045 extvicol-notgive interchangeable，也不是已经 ExtendVoteResponse.vote_extension 就已经会包进 CanonicalVoteExtension interchangeable / 418 extviresp interchangeable。**  
   官方把是应用给的和已经会包进 CanonicalVoteExtension 分开。看见是应用给的，不是已经会包进 CanonicalVoteExtension interchangeable。本页钉 not already packed 单句。

3. **看见能指扩展 / 看见填了 vote_extension / 这份栏 is not already 已经交差 interchangeable，也不是已经 ExtendedVoteInfo 表栏 bundled（421） interchangeable / 1043 extvicol-notextract interchangeable / 1044 extvicol-notsign interchangeable，也不是已经 ExtendedVoteInfo 从本进程抽出就已经从块里抽出 interchangeable / 369 extviout interchangeable。**  
   官方把能指扩展和已经交差分开。看见能指扩展，不是已经交差 interchangeable。421 extvitable vs usage bundled unbundling 在本页 item 1 启动。

怎样写 ExtendedVoteInfo 表栏、怎样填 vote_extension、怎样填 extension_signature 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ExtendedVoteInfo.vote_extension not already extracted ≠ 已经从本进程抽出 interchangeable：** 官方把发送验证者的应用给的非确定扩展和已经从本进程抽出分开。
- **看见是应用给的 not already packed ≠ 已经会包进 CanonicalVoteExtension interchangeable：** 官方把是应用给的和已经会包进 CanonicalVoteExtension 分开。
- **看见能指扩展 not already settled ≠ 已经交差 interchangeable：** 官方把能指扩展和已经交差分开；421 extvitable vs usage bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendedVoteInfo.vote_extension 是发送验证者的应用给的非确定扩展 | 不是已经从本进程抽出 | 不是 ExtendedVoteInfo 从本进程抽出就已经从块里抽出（369） |
| 看见是应用给的 | 不是已经会包进 CanonicalVoteExtension | 不是 ExtendVoteResponse.vote_extension 就已经会包进 CanonicalVoteExtension（418） |
| 看见能指扩展 | 不是已经交差 | 不是 non_rp_vote_extension 就已经按原样签（1044） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendedVoteInfo.vote_extension not already extracted / not already packed / not already settled 正式三事（421 余量），必须分开是不是已经从本进程抽出、是不是已经会包进 CanonicalVoteExtension、是不是已经交差。可以跳过「看见填了 ExtendedVoteInfo 表栏就已经从本进程抽出」。不要另写怎样写 ExtendedVoteInfo 表栏。421 extvitable vs usage bundled unbundling 在本页 item 1 启动；续 [`worked-example-extvicol-notsign-vs-bundled.md`](worked-example-extvicol-notsign-vs-bundled.md)（不变量 1044 item 2）。

## 本页不抄

- 怎样写 ExtendedVoteInfo 表栏、怎样填 vote_extension、怎样填 extension_signature。
- ExtendedVoteInfo 表栏 bundled。那是不变量 421。
- ExtendedVoteInfo 从本进程抽出就已经从块里抽出。那是不变量 369。
- ExtendVoteResponse.vote_extension 就已经会包进 CanonicalVoteExtension。那是不变量 418。
