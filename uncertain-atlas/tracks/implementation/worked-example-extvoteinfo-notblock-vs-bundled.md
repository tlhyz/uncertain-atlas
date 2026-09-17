# 例：看见 ExtendedVoteInfo 从本进程抽出 is not already extracted from block interchangeable / not already has pubkey interchangeable / not already settled interchangeable

**层次**：实现 / ExtendedVoteInfo 抽出 not already from block / not already has pubkey / not already settled 正式三事（369 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendedVoteInfo 抽出 not already from block / not already has pubkey / not already settled 正式三事（369 余量）/ not 818 extvoteinfo-notblock interchangeable / not 369 extvoteinfo-vs-local bundled interchangeable」，不是 ExtendedVoteInfo bundled（369），也不是 VoteInfo 从拟议块或已决块抽出就已经带了公钥（365），也不是 ExtendedVoteInfo 余栏就已经从本进程抽出（421），也不是 ExtendedCommitInfo 轮就已经从本进程抽出（394/749）。不要另写怎样写 ExtendedVoteInfo。

## 官方三件事

1. **看见 ExtendedVoteInfo 从本进程的 CometBFT 数据结构抽出 / 看见 Prepare 里有这份 / 这份抽出 is not already 已经从拟议块或已决块抽出 interchangeable / 365 voteinfo interchangeable，也不是已经 ExtendedVoteInfo bundled（369） interchangeable / 818 extvoteinfo-notblock interchangeable / 819 extvoteinfo-notsigned interchangeable / 369 extvoteinfo item 2 交给应用 interchangeable，也不是已经 ExtendedVoteInfo 抽出 not already from block / not already has pubkey / not already settled 正式三事 bundled（369 item 1 余量） interchangeable / 369 extvoteinfo item 1 interchangeable。**  
   官方写：这份信息从本进程里 CometBFT 的数据结构抽出。看见 Prepare 里有这份，不是已经从拟议块或已决块抽出 interchangeable——本页从 369 item 1 侧钉 not already from block 单句。369 extvoteinfo vs local bundled unbundling 在本页 item 1 启动。

2. **看见 Prepare 里有这份 / 看见有 validator / 这份抽出 is not already 已经带了公钥 interchangeable / 365 voteinfo interchangeable，也不是已经 ExtendedVoteInfo bundled（369） interchangeable / 818 extvoteinfo-notblock interchangeable / 369 extvoteinfo item 3 关掉全空 interchangeable / 820 extvoteinfo-notenabled interchangeable，也不是已经 ExtendedVoteInfo 余栏就已经从本进程抽出 interchangeable / 421 extvitable interchangeable，也不是已经 ExtendedCommitInfo 轮就已经从本进程抽出 interchangeable / 394 extcommitround / 749 extcommitround-notcommitinfo interchangeable。**  
   官方把有 validator 和已经带了公钥分开——369 bundled 第一件事常与 365 / 421 / 394 混成「看见 Prepare 里有扩展就已经从块里抽出或已经带了公钥 interchangeable」，本页钉 not already has pubkey 单句。

3. **看见 Prepare 里有这份 / 看见能抽 / 这份抽出 is not already 已经交差 interchangeable，也不是已经 ExtendedVoteInfo bundled（369） interchangeable / 818 extvoteinfo-notblock interchangeable / 819 extvoteinfo-notsigned interchangeable。**  
   官方把能抽和已经交差分开。看见能抽，不是已经交差 interchangeable。369 extvoteinfo vs local bundled unbundling 在本页 item 1 启动。

怎样编 ExtendedVoteInfo、怎样验签、怎样开关扩展是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ExtendedVoteInfo 抽出 not already from block ≠ 365 interchangeable：** 官方把本进程抽出和从块里抽出分开。
- **看见有 validator not already has pubkey ≠ 已经带了公钥 interchangeable：** 官方把有 validator 和已经带了公钥分开。
- **看见能抽 not already settled ≠ 已经交差 interchangeable：** 官方把能抽和已经交差分开；369 extvoteinfo vs local bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendedVoteInfo 从本进程抽出 | 不是已经从块里抽出（365） | 不是交给应用（819/369 item 2） |
| 看见有 validator | 不是已经带了公钥 | 不是 ExtendedVoteInfo 余栏（421） |
| 看见能抽 | 不是已经交差 | 不是 ExtendedCommitInfo 轮（394/749） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendedVoteInfo 抽出 not already from block / not already has pubkey / not already settled 正式三事（369 余量），必须分开是不是已经从块里抽出 interchangeable / 365、是不是已经带了公钥、是不是已经交差。可以跳过「看见 Prepare 里有扩展就已经从块里抽出」。不要另写怎样写 ExtendedVoteInfo。369 extvoteinfo vs local bundled unbundling 在本页 item 1 启动；续 [`worked-example-extvoteinfo-notsigned-vs-bundled.md`](worked-example-extvoteinfo-notsigned-vs-bundled.md)（不变量 819 item 2）。

## 本页不抄

- 怎样编 ExtendedVoteInfo、怎样验签、怎样开关扩展。
- ExtendedVoteInfo bundled。那是不变量 369。
- 把验过的签交给应用。那是不变量 369 item 2 余量 / 819。
- VoteInfo 从拟议块或已决块抽出就已经带了公钥。那是不变量 365。
- ExtendedVoteInfo 余栏就已经从本进程抽出。那是不变量 421。
