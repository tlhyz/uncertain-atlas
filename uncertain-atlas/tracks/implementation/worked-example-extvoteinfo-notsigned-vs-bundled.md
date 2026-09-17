# 例：看见把验过的签交给应用 is not already signed as-is interchangeable / not already replay protected interchangeable / not already must-fill interchangeable

**层次**：实现 / 验过的签交给应用 not already signed as-is / not already replay protected / not already must-fill 正式三事（369 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「验过的签交给应用 not already signed as-is / not already replay protected / not already must-fill 正式三事（369 余量）/ not 819 extvoteinfo-notsigned interchangeable / not 369 extvoteinfo-vs-local bundled interchangeable」，不是 ExtendedVoteInfo bundled（369），也不是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358），也不是 ExtendedVoteInfo 余栏签就已经交给应用（425），也不是 ExtendVote 何时调用就已经按原样签（361）。不要另写怎样写 ExtendedVoteInfo。

## 官方三件事

1. **看见 `extension_signature` 已由引擎验过、交给应用再处理 / 看见有签 / 这份签 is not already 已经按原样签 interchangeable / 358 canonical interchangeable，也不是已经 ExtendedVoteInfo bundled（369） interchangeable / 819 extvoteinfo-notsigned interchangeable / 818 extvoteinfo-notblock interchangeable / 369 extvoteinfo item 1 抽出 interchangeable，也不是已经验过的签交给应用 not already signed as-is / not already replay protected / not already must-fill 正式三事 bundled（369 item 2 余量） interchangeable / 369 extvoteinfo item 2 interchangeable。**  
   官方写：`extension_signature` 已经由 CometBFT 验过，这样才把签交给应用再处理或再验。看见有签，不是已经按原样签 interchangeable——本页从 369 item 2 侧钉 not already signed as-is 单句。369 extvoteinfo vs local bundled unbundling 在本页 item 2 续。

2. **看见有签 / 看见交给应用 / 这份签 is not already 已经有重放保护 interchangeable / 358 canonical interchangeable，也不是已经 ExtendedVoteInfo bundled（369） interchangeable / 819 extvoteinfo-notsigned interchangeable / 369 extvoteinfo item 3 关掉全空 interchangeable / 820 extvoteinfo-notenabled interchangeable，也不是已经 ExtendedVoteInfo 余栏签就已经交给应用 interchangeable / 425 extvirest interchangeable，也不是已经 ExtendVote 何时调用就已经按原样签 interchangeable / 361 extwhen interchangeable。**  
   官方把交给应用和已经有重放保护分开——369 bundled 第二件事常与 358 / 425 / 361 混成「看见有签就已经按原样签或已经有重放保护 interchangeable」，本页钉 not already replay protected 单句。

3. **看见有签 / 看见签了空切片 / 这份签 is not already 已经必须填 interchangeable，也不是已经 ExtendedVoteInfo bundled（369） interchangeable / 819 extvoteinfo-notsigned interchangeable / 818 extvoteinfo-notblock interchangeable。**  
   官方把签了空切片和已经必须填分开。看见签了空切片，不是已经必须填 interchangeable。369 extvoteinfo vs local bundled unbundling 在本页 item 2 续。

怎样编 ExtendedVoteInfo、怎样验签、怎样开关扩展是规范里的做法，本页不抄。

## 官方为什么这样拆

- **验过的签交给应用 not already signed as-is ≠ 358 interchangeable：** 官方把交给应用和包装方式分开。
- **看见交给应用 not already replay protected ≠ 已经有重放保护 interchangeable：** 官方把交给应用和已经有重放保护分开。
- **看见签了空切片 not already must-fill ≠ 已经必须填 interchangeable：** 官方把签了空切片和已经必须填分开；369 extvoteinfo vs local bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 把验过的签交给应用 | 不是已经按原样签（358） | 不是从本进程抽出（818/369 item 1） |
| 看见交给应用 | 不是已经有重放保护 | 不是 ExtendedVoteInfo 余栏签（425） |
| 看见签了空切片 | 不是已经必须填 | 不是 ExtendVote 何时调用（361） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看验过的签交给应用 not already signed as-is / not already replay protected / not already must-fill 正式三事（369 余量），必须分开是不是已经按原样签 interchangeable / 358、是不是已经有重放保护、是不是已经必须填。可以跳过「看见有签就已经按原样签」。不要另写怎样写 ExtendedVoteInfo。369 extvoteinfo vs local bundled unbundling 在本页 item 2 续；续 [`worked-example-extvoteinfo-notenabled-vs-bundled.md`](worked-example-extvoteinfo-notenabled-vs-bundled.md)（不变量 820 item 3）。

## 本页不抄

- 怎样编 ExtendedVoteInfo、怎样验签、怎样开关扩展。
- ExtendedVoteInfo bundled。那是不变量 369。
- 从本进程抽出。那是不变量 369 item 1 余量 / 818。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。那是不变量 358。
- ExtendedVoteInfo 余栏签就已经交给应用。那是不变量 425。
