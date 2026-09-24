# 例：看见有这列 / 看见能定奖惩 / 看见有 block_id_flag is not already already slashed interchangeable / already decided-commit interchangeable / already settled interchangeable

**层次**：实现 / VoteInfo 能按到场定奖惩不是已经罚没 not already slashed / not already decided-commit / not already settled 正式三事（365 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VoteInfo / CommitInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VoteInfo 能按到场定奖惩不是已经罚没 not already slashed / not already decided-commit / not already settled 正式三事（365 余量）/ not 842 voteinfo-notslashed interchangeable / not 365 voteinfo bundled interchangeable」，不是 VoteInfo bundled（365），也不是从拟议块或已决块抽出不是已经带了公钥（843 item 2 余量）或按投票权降序排不是已经进了块（844 item 3 余量）。不要另写怎样写 VoteInfo。

## 官方三件事

规范把 Methods 里 `VoteInfo` 标明验证者有没有签上一块、好按到场定奖惩 和「已经是有这列就已经罚没 interchangeable / 已经是能定奖惩就已经用 decided_last_commit 算完 interchangeable / 已经是有 block_id_flag 就已经交差 interchangeable / 已经是 voteinfo bundled interchangeable」分开写成三件独立的实现事，不是「看见有这列就已经罚没 interchangeable / 就已经用 decided_last_commit 算完 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见有这列 / 看见 VoteInfo 标明上一块有没有签、能按到场定奖惩 / 看见有 `block_id_flag` 列 is not already 已经罚没 interchangeable / 已经 slashed interchangeable / 已经罚没交差 interchangeable / 365 voteinfo bundled interchangeable / 21 evidence interchangeable / voteinfo-sold-as-rewarded interchangeable，也不是已经 VoteInfo bundled（365） interchangeable / 842 voteinfo-notslashed interchangeable / 365 voteinfo item 1 interchangeable，也不是已经 VoteInfo 能按到场定奖惩不是已经罚没 not already slashed / not already decided-commit / not already settled 正式三事 bundled（365 item 1 余量） interchangeable / 365 voteinfo item 1 interchangeable，也不是已经从块抽出带了公钥（843） interchangeable / 844 voteinfo-notinblock interchangeable / 463 finreward interchangeable，也不是已经证据上链就已经罚没（21） interchangeable。**  
   官方写：`VoteInfo` 标明验证者有没有签上一块，好按到场定奖惩。看见有这列，不是已经罚没。看见有这列，不是已经 slashed interchangeable——365 钉 bundled 三事，本页从 item 1 侧钉 not already slashed 单句。看见 VoteInfo 标明上一块有没有签、能按到场定奖惩，不是已经 VoteInfo bundled（365） interchangeable——365 钉 bundled，本页钉 item 1 第一件事。看见有这列，不是已经从块抽出带了公钥（843） interchangeable——843 另钉 item 2。看见有这列，不是已经按权排序进了块（844） interchangeable——844 另钉 item 3。365 voteinfo-vs-reward bundled unbundling 在本页 item 1 启动。

2. **看见能定奖惩 / 看见好按到场定奖惩 / 看见能按到场定 is not already 已经是应用已经用 `decided_last_commit` 算完 interchangeable / 已经 decided-commit interchangeable / 已经算完交差 interchangeable / 365 voteinfo bundled interchangeable / 463 finreward interchangeable，也不是已经 VoteInfo bundled（365） interchangeable / 842 voteinfo-notslashed interchangeable / 365 voteinfo item 2 抽出 interchangeable / 365 voteinfo item 3 排序 interchangeable，也不是已经 VoteInfo 能按到场定奖惩不是已经罚没 not already slashed / not already decided-commit / not already settled 正式三事 bundled（365 item 1 余量） interchangeable / 365 voteinfo item 1 interchangeable，也不是已经罚没（本页第一件事） interchangeable。**  
   官方写：看见能定奖惩，不是已经是应用已经用 `decided_last_commit` 算完。看见好按到场定奖惩，不是已经 decided-commit interchangeable——本页钉 not already decided-commit 单句。看见能按到场定，不是已经罚没（本页第一件事） interchangeable——三件事分开钉。365 voteinfo-vs-reward bundled unbundling 在本页 item 1 启动。

3. **看见有 `block_id_flag` / 看见有 flag / 看见标明有没有签 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 365 voteinfo bundled interchangeable / 33 fourgates interchangeable，也不是已经 VoteInfo bundled（365） interchangeable / 842 voteinfo-notslashed interchangeable / 365 voteinfo item 2 / 365 voteinfo item 3，也不是已经 VoteInfo 能按到场定奖惩不是已经罚没 not already slashed / not already decided-commit / not already settled 正式三事 bundled（365 item 1 余量） interchangeable / 365 voteinfo item 1 interchangeable，也不是已经罚没（本页第一件事） interchangeable / 已经用 decided_last_commit 算完（本页第二件事） interchangeable。**  
   官方写：看见有 `block_id_flag`，不是已经交差。看见有 flag，不是已经 settled interchangeable——本页钉 not already settled 单句。看见标明有没有签，不是已经用 decided_last_commit 算完（本页第二件事） interchangeable——三件事分开钉。365 voteinfo-vs-reward bundled unbundling 在本页 item 1 启动。

怎样编 `VoteInfo`、怎样排 `votes`、怎样从 store 再装是规范里的做法，本页不抄。VoteInfo bundled（365）、从拟议块或已决块抽出不是已经带了公钥（365 item 2 余量 / 843）、按投票权降序排不是已经进了块（365 item 3 余量 / 844）、必须回四列就已经改了集合（363）、Validator 用 address 认人就已经带了公钥（364）、证据上链就已经罚没（21）是另外那套，本页不抄。

## 官方为什么这样拆

- **有这列 not already slashed ≠ 365 / 21 interchangeable：** 官方把有这列和已经罚没分开。
- **能定奖惩 not already decided-commit ≠ 已经用 decided_last_commit 算完 interchangeable：** 官方把能定奖惩和已经算完分开。
- **有 block_id_flag not already settled ≠ 已经交差 interchangeable：** 官方把有 block_id_flag 和已经交差分开；365 voteinfo-vs-reward bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 有这列 | 不是 already slashed | 不是证据上链就已经罚没 alone（21） |
| 能定奖惩 | 不是 already decided-commit | 不是从块抽出 already pubkey alone（843） |
| 有 block_id_flag | 不是 already settled | 不是按权排序 already in-block alone（844） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VoteInfo 能按到场定奖惩不是已经罚没 not already slashed / not already decided-commit / not already settled 正式三事（365 余量），必须分开有这列 是不是 already slashed interchangeable / 365 voteinfo bundled interchangeable / voteinfo-sold-as-rewarded interchangeable、能定奖惩 是不是 already decided-commit interchangeable、有 block_id_flag 是不是 already settled interchangeable。可以跳过「看见有这列就已经罚没 interchangeable / 就已经用 decided_last_commit 算完 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 VoteInfo。365 voteinfo-vs-reward bundled unbundling 在本页 item 1 启动；完成 [`worked-example-voteinfo-notpubkey-vs-bundled.md`](worked-example-voteinfo-notpubkey-vs-bundled.md)（不变量 843 item 2）；完成 [`worked-example-voteinfo-notinblock-vs-bundled.md`](worked-example-voteinfo-notinblock-vs-bundled.md)（不变量 844 item 3）。

## 本页不抄

- 怎样编 `VoteInfo`、怎样排 `votes`、怎样从 store 再装。
- VoteInfo bundled。那是不变量 365。
- 从拟议块或已决块抽出不是已经带了公钥。那是不变量 365 item 2 余量 / 843。
- 按投票权降序排不是已经进了块。那是不变量 365 item 3 余量 / 844。
- 必须回四列就已经改了集合。那是不变量 363。
- Validator 用 address 认人就已经带了公钥。那是不变量 364。
- 证据上链就已经罚没。那是不变量 21。
