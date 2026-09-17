# 例：看见从拟议块或已决块抽出 is not already has pubkey interchangeable / not already ValidatorUpdate interchangeable / not already changed set interchangeable

**层次**：实现 / 从块抽出 not already has pubkey / not already ValidatorUpdate / not already changed set 正式三事（365 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VoteInfo / CommitInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「从块抽出 not already has pubkey / not already ValidatorUpdate / not already changed set 正式三事（365 余量）/ not 831 voteinfo-notpubkey interchangeable / not 365 voteinfo-vs-reward bundled interchangeable」，不是 VoteInfo bundled（365），也不是 Validator 用 address 认人就已经带了公钥（364），也不是 ExtendedVoteInfo 本进程抽出就已经从块抽出（369/818），也不是必须回四列就已经改了集合（363）。不要另写怎样写 VoteInfo。

## 官方三件事

1. **看见这份信息通常从拟议块或已决块抽出 / 看见块里有票 / 这份抽出 is not already 已经带了公钥 interchangeable / 364 validator interchangeable，也不是已经 VoteInfo bundled（365） interchangeable / 831 voteinfo-notpubkey interchangeable / 830 voteinfo-notslashed interchangeable / 365 voteinfo item 1 定奖惩 interchangeable，也不是已经从块抽出 not already has pubkey / not already ValidatorUpdate / not already changed set 正式三事 bundled（365 item 2 余量） interchangeable / 365 voteinfo item 2 interchangeable。**  
   官方写：这份信息通常从拟议块或已决块抽出。看见从块里抽出，不是已经带了公钥 interchangeable——本页从 365 item 2 侧钉 not already has pubkey 单句。365 voteinfo vs reward bundled unbundling 在本页 item 2 续。

2. **看见块里有票 / 看见有 VoteInfo.validator / 这份抽出 is not already 已经是 ValidatorUpdate interchangeable / 364 validator interchangeable，也不是已经 VoteInfo bundled（365） interchangeable / 831 voteinfo-notpubkey interchangeable / 365 voteinfo item 3 降序 interchangeable / 832 voteinfo-notinblock interchangeable，也不是已经 Validator 用 address 认人就已经带了公钥 interchangeable / 364 validator interchangeable，也不是已经 ExtendedVoteInfo 本进程抽出就已经从块抽出 interchangeable / 369 extvoteinfo / 818 extvoteinfo-notblock interchangeable。**  
   官方把有 validator 和已经是 ValidatorUpdate 分开——365 bundled 第二件事常与 364 / 369 混成「看见块里有票就已经带了公钥或已经是 ValidatorUpdate interchangeable」，本页钉 not already ValidatorUpdate 单句。

3. **看见块里有票 / 看见从块里抽出 / 这份抽出 is not already 已经改了集合 interchangeable，也不是已经 VoteInfo bundled（365） interchangeable / 831 voteinfo-notpubkey interchangeable / 830 voteinfo-notslashed interchangeable，也不是已经必须回四列就已经改了集合 interchangeable / 363 finresp interchangeable。**  
   官方把从块里抽出和已经改了集合分开。看见从块里抽出，不是已经改了集合 interchangeable。365 voteinfo vs reward bundled unbundling 在本页 item 2 续。

怎样编 VoteInfo、怎样排 votes、怎样从 store 再装是规范里的做法，本页不抄。

## 官方为什么这样拆

- **从块抽出 not already has pubkey ≠ 364 interchangeable：** 官方把抽出票和更新集合的认人分开。
- **看见有 validator not already ValidatorUpdate ≠ 已经是 ValidatorUpdate interchangeable：** 官方把有 validator 和已经是 ValidatorUpdate 分开。
- **看见从块里抽出 not already changed set ≠ 已经改了集合 interchangeable：** 官方把从块里抽出和已经改了集合分开；365 voteinfo vs reward bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 从拟议块或已决块抽出 | 不是已经带了公钥（364） | 不是定奖惩（830/365 item 1） |
| 看见有 VoteInfo.validator | 不是已经是 ValidatorUpdate | 不是 ExtendedVoteInfo 本进程抽出（369/818） |
| 看见从块里抽出 | 不是已经改了集合 | 不是必须回四列就已经改了集合（363） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看从块抽出 not already has pubkey / not already ValidatorUpdate / not already changed set 正式三事（365 余量），必须分开是不是已经带了公钥 interchangeable / 364、是不是已经是 ValidatorUpdate、是不是已经改了集合。可以跳过「看见块里有票就已经带了公钥」。不要另写怎样写 VoteInfo。365 voteinfo vs reward bundled unbundling 在本页 item 2 续；续 [`worked-example-voteinfo-notinblock-vs-bundled.md`](worked-example-voteinfo-notinblock-vs-bundled.md)（不变量 832 item 3）。

## 本页不抄

- 怎样编 VoteInfo、怎样排 votes、怎样从 store 再装。
- VoteInfo bundled。那是不变量 365。
- VoteInfo 能按到场定奖惩。那是不变量 365 item 1 余量 / 830。
- Validator 用 address 认人就已经带了公钥。那是不变量 364。
- ExtendedVoteInfo 本进程抽出就已经从块抽出。那是不变量 369 / 818。
