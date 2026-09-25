# 例：看见有签 / 看见交给应用 / 看见签了空切片 is not already already raw interchangeable / already protected interchangeable / already must-fill interchangeable

**层次**：实现 / 把验过的签交给应用不是已经按原样签 not already raw / not already protected / not already must-fill 正式三事（369 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「把验过的签交给应用不是已经按原样签 not already raw / not already protected / not already must-fill 正式三事（369 余量）/ not 855 extvoteinfo-notraw interchangeable / not 369 extvoteinfo bundled interchangeable」，不是 extvoteinfo bundled（369），也不是 ExtendedVoteInfo 从本进程抽出不是已经从块里抽出（854 item 1 余量）或扩展关掉则字段全空不是已经到了启用高度（856 item 3 余量）。不要另写怎样写 ExtendedVoteInfo。

## 官方三件事

规范把 Methods 里 `extension_signature` 已由引擎验过、交给应用再处理；扩展启用时两份签都在；没给 `non_rp` 就签空切片 和「已经是有签就已经按原样签 interchangeable / 已经是交给应用就已经有重放保护 interchangeable / 已经是签了空切片就已经必须填 interchangeable / 已经是 extvoteinfo bundled interchangeable」分开写成三件独立的实现事，不是「看见有签就已经按原样签 interchangeable / 就已经有重放保护 interchangeable / 就已经必须填 interchangeable」一件事：

1. **看见有签 / 看见 `extension_signature` 已由引擎验过、交给应用再处理；扩展启用时两份签都在 / 看见有 extension_signature is not already 已经按原样签 interchangeable / 已经 raw interchangeable / 已经按原样签交差 interchangeable / 369 extvoteinfo bundled interchangeable / 358 nonrp interchangeable / extvoteinfo-sold-as-local interchangeable，也不是已经 extvoteinfo bundled（369） interchangeable / 855 extvoteinfo-notraw interchangeable / 369 extvoteinfo item 2 interchangeable，也不是已经把验过的签交给应用不是已经按原样签 not already raw / not already protected / not already must-fill 正式三事 bundled（369 item 2 余量） interchangeable / 369 extvoteinfo item 2 interchangeable，也不是已经从本进程抽出就已经从块里抽出（854） interchangeable / 856 extvoteinfo-notveheight interchangeable / 418 nonrp interchangeable，也不是已经 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358） interchangeable。**  
   官方写：`extension_signature` 是这份扩展的签，已经由 CometBFT 验过，这样才把签交给应用再处理或再验。扩展启用时两份签都会在。看见有签，不是已经按原样签。看见有签，不是已经 raw interchangeable——369 钉 bundled 三事，本页从 item 2 侧钉 not already raw 单句。看见 `extension_signature` 已由引擎验过、交给应用再处理，不是已经 extvoteinfo bundled（369） interchangeable——369 钉 bundled，本页钉 item 2 第一件事。看见有签，不是已经从本进程抽出就已经从块里抽出（854） interchangeable——854 另钉 item 1。看见有签，不是已经扩展关掉字段全空就已经到了启用高度（856） interchangeable——856 另钉 item 3。369 extvoteinfo-vs-local bundled unbundling 在本页 item 2 续。

2. **看见交给应用 / 看见把签交给应用再处理或再验 / 看见交给应用 is not already 已经有重放保护 interchangeable / 已经 protected interchangeable / 已经有重放保护交差 interchangeable / 369 extvoteinfo bundled interchangeable / 418 nonrp interchangeable，也不是已经 extvoteinfo bundled（369） interchangeable / 855 extvoteinfo-notraw interchangeable / 369 extvoteinfo item 1 抽出 interchangeable / 369 extvoteinfo item 3 关掉全空 interchangeable，也不是已经把验过的签交给应用不是已经按原样签 not already raw / not already protected / not already must-fill 正式三事 bundled（369 item 2 余量） interchangeable / 369 extvoteinfo item 2 interchangeable，也不是已经按原样签（本页第一件事） interchangeable。**  
   官方写：看见交给应用，不是已经有重放保护。看见把签交给应用再处理或再验，不是已经 protected interchangeable——本页钉 not already protected 单句。看见交给应用，不是已经按原样签（本页第一件事） interchangeable——三件事分开钉。369 extvoteinfo-vs-local bundled unbundling 在本页 item 2 续。

3. **看见签了空切片 / 看见没给 `non_rp_vote_extension` 就签空切片 / 看见签空切片 is not already 已经必须填 interchangeable / 已经 must-fill interchangeable / 已经必须填交差 interchangeable / 369 extvoteinfo bundled interchangeable / 358 nonrp interchangeable，也不是已经 extvoteinfo bundled（369） interchangeable / 855 extvoteinfo-notraw interchangeable / 369 extvoteinfo item 1 / 369 extvoteinfo item 3，也不是已经把验过的签交给应用不是已经按原样签 not already raw / not already protected / not already must-fill 正式三事 bundled（369 item 2 余量） interchangeable / 369 extvoteinfo item 2 interchangeable，也不是已经按原样签（本页第一件事） interchangeable / 已经有重放保护（本页第二件事） interchangeable。**  
   官方写：若没给 `non_rp_vote_extension`，这份签签的是空切片。看见签了空切片，不是已经必须填。看见没给 `non_rp` 就签空切片，不是已经 must-fill interchangeable——本页钉 not already must-fill 单句。看见签空切片，不是已经有重放保护（本页第二件事） interchangeable——三件事分开钉。369 extvoteinfo-vs-local bundled unbundling 在本页 item 2 续。

怎样编 `ExtendedVoteInfo`、怎样验签、怎样开关扩展是规范里的做法，本页不抄。extvoteinfo bundled（369）、ExtendedVoteInfo 从本进程抽出不是已经从块里抽出（369 item 1 余量 / 854）、扩展关掉则字段全空不是已经到了启用高度（369 item 3 余量 / 856）、vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358）、从拟议块或已决块抽出就已经带了公钥（365）、到了 H 就已经 Prepare 带了扩展（330）是另外那套，本页不抄。

## 官方为什么这样拆

- **有签 not already raw ≠ 369 / 358 interchangeable：** 官方把有签和已经按原样签分开。
- **交给应用 not already protected ≠ 已经有重放保护 interchangeable：** 官方把交给应用和已经有重放保护分开。
- **签了空切片 not already must-fill ≠ 已经必须填 interchangeable：** 官方把签了空切片和已经必须填分开；369 extvoteinfo-vs-local bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 有签 | 不是 already raw | 不是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签 alone（358） |
| 交给应用 | 不是 already protected | 不是从本进程抽出 already from-block alone（854） |
| 签了空切片 | 不是 already must-fill | 不是扩展关掉字段全空 already ve-height alone（856） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看把验过的签交给应用不是已经按原样签 not already raw / not already protected / not already must-fill 正式三事（369 余量），必须分开有签 是不是 already raw interchangeable / 369 extvoteinfo bundled interchangeable / extvoteinfo-sold-as-local interchangeable、交给应用 是不是 already protected interchangeable、签了空切片 是不是 already must-fill interchangeable。可以跳过「看见有签就已经按原样签 interchangeable / 就已经有重放保护 interchangeable / 就已经必须填 interchangeable」。不要另写怎样写 ExtendedVoteInfo。369 extvoteinfo-vs-local bundled unbundling 在本页 item 2 续。

## 本页不抄

- 怎样编 `ExtendedVoteInfo`、怎样验签、怎样开关扩展。
- extvoteinfo bundled。那是不变量 369。
- ExtendedVoteInfo 从本进程抽出不是已经从块里抽出。那是不变量 369 item 1 余量 / 854。
- 扩展关掉则字段全空不是已经到了启用高度。那是不变量 369 item 3 余量 / 856。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。那是不变量 358。
- 从拟议块或已决块抽出就已经带了公钥。那是不变量 365。
- 到了 H 就已经 Prepare 带了扩展。那是不变量 330。
