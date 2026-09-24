# 例：看见从块里抽出 / 看见有 VoteInfo.validator / 看见块里有票 is not already already pubkey interchangeable / already update interchangeable / already changed-set interchangeable

**层次**：实现 / 从拟议块或已决块抽出不是已经带了公钥 not already pubkey / not already update / not already changed-set 正式三事（365 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VoteInfo / CommitInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「从拟议块或已决块抽出不是已经带了公钥 not already pubkey / not already update / not already changed-set 正式三事（365 余量）/ not 843 voteinfo-notpubkey interchangeable / not 365 voteinfo bundled interchangeable」，不是 VoteInfo bundled（365），也不是 VoteInfo 能按到场定奖惩不是已经罚没（842 item 1 余量）或按投票权降序排不是已经进了块（844 item 3 余量）。不要另写怎样写 VoteInfo。

## 官方三件事

规范把 Methods 里这份信息通常从拟议块或已决块抽出 和「已经是从块里抽出就已经带了公钥 interchangeable / 已经是有 VoteInfo.validator 就已经是 ValidatorUpdate interchangeable / 已经是块里有票就已经改了集合 interchangeable / 已经是 voteinfo bundled interchangeable」分开写成三件独立的实现事，不是「看见从块里抽出就已经带了公钥 interchangeable / 就已经是 ValidatorUpdate interchangeable / 就已经改了集合 interchangeable」一件事：

1. **看见从块里抽出 / 看见这份信息通常从拟议块或已决块抽出 / 看见从块抽出 is not already 已经带了公钥 interchangeable / 已经 pubkey interchangeable / 已经带了公钥交差 interchangeable / 365 voteinfo bundled interchangeable / 364 validator interchangeable / voteinfo-sold-as-rewarded interchangeable，也不是已经 VoteInfo bundled（365） interchangeable / 843 voteinfo-notpubkey interchangeable / 365 voteinfo item 2 interchangeable，也不是已经从拟议块或已决块抽出不是已经带了公钥 not already pubkey / not already update / not already changed-set 正式三事 bundled（365 item 2 余量） interchangeable / 365 voteinfo item 2 interchangeable，也不是已经罚没（842） interchangeable / 844 voteinfo-notinblock interchangeable / 841 valupdate interchangeable，也不是已经 Validator 用 address 认人就已经带了公钥（364） interchangeable。**  
   官方写：这份信息通常从拟议块或已决块抽出。看见从块里抽出，不是已经带了公钥。看见从块里抽出，不是已经 pubkey interchangeable——365 钉 bundled 三事，本页从 item 2 侧钉 not already pubkey 单句。看见这份信息通常从拟议块或已决块抽出，不是已经 VoteInfo bundled（365） interchangeable——365 钉 bundled，本页钉 item 2 第一件事。看见从块里抽出，不是已经罚没（842） interchangeable——842 另钉 item 1。看见从块里抽出，不是已经按权排序进了块（844） interchangeable——844 另钉 item 3。365 voteinfo-vs-reward bundled unbundling 在本页 item 2 续。

2. **看见有 `VoteInfo.validator` / 看见有 validator 字段 / 看见票里有 Validator is not already 已经是 ValidatorUpdate interchangeable / 已经 update interchangeable / 已经是 ValidatorUpdate 交差 interchangeable / 365 voteinfo bundled interchangeable / 364 validator interchangeable，也不是已经 VoteInfo bundled（365） interchangeable / 843 voteinfo-notpubkey interchangeable / 365 voteinfo item 1 到场 interchangeable / 365 voteinfo item 3 排序 interchangeable，也不是已经从拟议块或已决块抽出不是已经带了公钥 not already pubkey / not already update / not already changed-set 正式三事 bundled（365 item 2 余量） interchangeable / 365 voteinfo item 2 interchangeable，也不是已经带了公钥（本页第一件事） interchangeable。**  
   官方写：看见有 `VoteInfo.validator`，不是已经是 `ValidatorUpdate`。看见有 validator 字段，不是已经 update interchangeable——本页钉 not already update 单句。看见票里有 Validator，不是已经带了公钥（本页第一件事） interchangeable——三件事分开钉。365 voteinfo-vs-reward bundled unbundling 在本页 item 2 续。

3. **看见块里有票 / 看见拟议块或已决块里有票 / 看见块里抽出了票 is not already 已经改了集合 interchangeable / 已经 changed-set interchangeable / 已经改了集合交差 interchangeable / 365 voteinfo bundled interchangeable / 33 fourgates interchangeable，也不是已经 VoteInfo bundled（365） interchangeable / 843 voteinfo-notpubkey interchangeable / 365 voteinfo item 1 / 365 voteinfo item 3，也不是已经从拟议块或已决块抽出不是已经带了公钥 not already pubkey / not already update / not already changed-set 正式三事 bundled（365 item 2 余量） interchangeable / 365 voteinfo item 2 interchangeable，也不是已经带了公钥（本页第一件事） interchangeable / 已经是 ValidatorUpdate（本页第二件事） interchangeable。**  
   官方写：看见块里有票，不是已经改了集合。看见拟议块或已决块里有票，不是已经 changed-set interchangeable——本页钉 not already changed-set 单句。看见块里抽出了票，不是已经是 ValidatorUpdate（本页第二件事） interchangeable——三件事分开钉。365 voteinfo-vs-reward bundled unbundling 在本页 item 2 续。

怎样编 `VoteInfo`、怎样排 `votes`、怎样从 store 再装是规范里的做法，本页不抄。VoteInfo bundled（365）、VoteInfo 能按到场定奖惩不是已经罚没（365 item 1 余量 / 842）、按投票权降序排不是已经进了块（365 item 3 余量 / 844）、必须回四列就已经改了集合（363）、Validator 用 address 认人就已经带了公钥（364）、证据上链就已经罚没（21）是另外那套，本页不抄。

## 官方为什么这样拆

- **从块里抽出 not already pubkey ≠ 365 / 364 interchangeable：** 官方把从块里抽出和已经带了公钥分开。
- **有 VoteInfo.validator not already update ≠ 已经是 ValidatorUpdate interchangeable：** 官方把有 VoteInfo.validator 和已经是 ValidatorUpdate 分开。
- **块里有票 not already changed-set ≠ 已经改了集合 interchangeable：** 官方把块里有票和已经改了集合分开；365 voteinfo-vs-reward bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 从块里抽出 | 不是 already pubkey | 不是 Validator 用 address 认人就已经带了公钥 alone（364） |
| 有 VoteInfo.validator | 不是 already update | 不是有这列 already slashed alone（842） |
| 块里有票 | 不是 already changed-set | 不是按权排序 already in-block alone（844） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看从拟议块或已决块抽出不是已经带了公钥 not already pubkey / not already update / not already changed-set 正式三事（365 余量），必须分开从块里抽出 是不是 already pubkey interchangeable / 365 voteinfo bundled interchangeable / voteinfo-sold-as-rewarded interchangeable、有 VoteInfo.validator 是不是 already update interchangeable、块里有票 是不是 already changed-set interchangeable。可以跳过「看见从块里抽出就已经带了公钥 interchangeable / 就已经是 ValidatorUpdate interchangeable / 就已经改了集合 interchangeable」。不要另写怎样写 VoteInfo。365 voteinfo-vs-reward bundled unbundling 在本页 item 2 续（842 + 843）。

## 本页不抄

- 怎样编 `VoteInfo`、怎样排 `votes`、怎样从 store 再装。
- VoteInfo bundled。那是不变量 365。
- VoteInfo 能按到场定奖惩不是已经罚没。那是不变量 365 item 1 余量 / 842。
- 按投票权降序排不是已经进了块。那是不变量 365 item 3 余量 / 844。
- 必须回四列就已经改了集合。那是不变量 363。
- Validator 用 address 认人就已经带了公钥。那是不变量 364。
- 证据上链就已经罚没。那是不变量 21。
