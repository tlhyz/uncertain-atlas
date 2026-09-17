# 例：看见扩展关掉则字段全空 is not already enable height interchangeable / not already settled interchangeable / not already from block interchangeable

**层次**：实现 / 扩展关掉全空 not already enable height / not already settled / not already from block 正式三事（369 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「扩展关掉全空 not already enable height / not already settled / not already from block 正式三事（369 余量）/ not 820 extvoteinfo-notenabled interchangeable / not 369 extvoteinfo-vs-local bundled interchangeable」，不是 ExtendedVoteInfo bundled（369），也不是到了 H 就已经 Prepare 带了扩展（330），也不是 ExtendVote 何时调用就已经到了启用高度（361），也不是 VoteInfo 从块抽出（365）。不要另写怎样写 ExtendedVoteInfo。

## 官方三件事

1. **看见扩展关掉则 `vote_extension` / `non_rp_vote_extension` 和对应的签都空 / 看见空着 / 这份空 is not already 已经到了启用高度 interchangeable / 330 prepareext interchangeable，也不是已经 ExtendedVoteInfo bundled（369） interchangeable / 820 extvoteinfo-notenabled interchangeable / 818 extvoteinfo-notblock interchangeable / 369 extvoteinfo item 1 抽出 interchangeable，也不是已经扩展关掉全空 not already enable height / not already settled / not already from block 正式三事 bundled（369 item 3 余量） interchangeable / 369 extvoteinfo item 3 interchangeable。**  
   官方写：若投票扩展关掉，`vote_extension`、`non_rp_vote_extension` 和对应的签都空。看见空着，不是已经到了启用高度 interchangeable——本页从 369 item 3 侧钉 not already enable height 单句。369 extvoteinfo vs local bundled unbundling 在本页 item 3 完成。

2. **看见空着 / 看见关掉了 / 这份空 is not already 已经交差 interchangeable / 330 prepareext interchangeable，也不是已经 ExtendedVoteInfo bundled（369） interchangeable / 820 extvoteinfo-notenabled interchangeable / 369 extvoteinfo item 2 交给应用 interchangeable / 819 extvoteinfo-notsigned interchangeable，也不是已经 ExtendVote 何时调用就已经到了启用高度 interchangeable / 361 extwhen interchangeable。**  
   官方把关掉了和已经交差分开——369 bundled 第三件事常与 330 / 361 混成「看见空着就已经到了启用高度或已经交差 interchangeable」，本页钉 not already settled 单句。

3. **看见空着 / 看见字段在 / 这份空 is not already 已经从块里抽出 interchangeable，也不是已经 ExtendedVoteInfo bundled（369） interchangeable / 820 extvoteinfo-notenabled interchangeable / 818 extvoteinfo-notblock interchangeable，也不是已经 VoteInfo 从块抽出 interchangeable / 365 voteinfo interchangeable。**  
   官方把字段在和已经从块里抽出分开。看见字段在，不是已经从块里抽出 interchangeable。369 extvoteinfo vs local bundled unbundling 在本页 item 3 完成。

怎样编 ExtendedVoteInfo、怎样验签、怎样开关扩展是规范里的做法，本页不抄。

## 官方为什么这样拆

- **扩展关掉全空 not already enable height ≠ 330 interchangeable：** 官方把关掉全空和启用高度分开。
- **看见关掉了 not already settled ≠ 已经交差 interchangeable：** 官方把关掉了和已经交差分开。
- **看见字段在 not already from block ≠ 已经从块里抽出 interchangeable：** 官方把字段在和已经从块里抽出分开；369 extvoteinfo vs local bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 扩展关掉则字段全空 | 不是已经到了启用高度（330） | 不是从本进程抽出（818/369 item 1） |
| 看见关掉了 | 不是已经交差 | 不是 ExtendVote 何时调用（361） |
| 看见字段在 | 不是已经从块里抽出 | 不是 VoteInfo 从块抽出（365） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看扩展关掉全空 not already enable height / not already settled / not already from block 正式三事（369 余量），必须分开是不是已经到了启用高度 interchangeable / 330、是不是已经交差、是不是已经从块里抽出。可以跳过「看见空着就已经到了启用高度」。不要另写怎样写 ExtendedVoteInfo。369 extvoteinfo vs local bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样编 ExtendedVoteInfo、怎样验签、怎样开关扩展。
- ExtendedVoteInfo bundled。那是不变量 369。
- 从本进程抽出。那是不变量 369 item 1 余量 / 818。
- 到了 H 就已经 Prepare 带了扩展。那是不变量 330。
- VoteInfo 从拟议块或已决块抽出就已经带了公钥。那是不变量 365。
