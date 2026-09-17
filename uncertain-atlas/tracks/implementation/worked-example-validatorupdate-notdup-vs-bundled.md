# 例：看见一次更新里重复公钥 is not already last wins interchangeable / not already recoverable interchangeable / not already settled interchangeable

**层次**：实现 / 同一批重复公钥 not already last wins / not already recoverable / not already settled 正式三事（318 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating the Validator Set。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)、[L4.5](../../courses/level-04-bft/L04-M05-validator-set.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、mempool。本页是「同一批重复公钥 not already last wins / not already recoverable / not already settled 正式三事（318 余量）/ not 906 validatorupdate-notdup interchangeable / not 318 validatorupdate-vs-set bundled interchangeable」，不是 ValidatorUpdate bundled（318），也不是 H 的更新已经在 H+1 计票（35），也不是同一高度换轮已经换了集合（302）。不要另写怎样编更新或怎样算总权。

## 官方三件事

1. **看见一次更新里同一把公钥出现两次 / 看见重复 这份重复 is not already 已经按后一条改权 interchangeable，也不是已经 ValidatorUpdate bundled（318） interchangeable / 906 validatorupdate-notdup interchangeable / 905 validatorupdate-notempty interchangeable / 318 validatorupdate item 1 空名单 interchangeable，也不是已经同一批重复公钥 not already last wins / not already recoverable / not already settled 正式三事 bundled（318 item 2 余量） interchangeable / 318 validatorupdate item 2 interchangeable。**  
   官方写：应用必须保证同一批更新里没有重复，一把公钥在这一次更新里只能出现一次。看见重复，不是已经按后一条算 interchangeable——本页从 318 item 2 侧钉 not already last wins 单句。318 validatorupdate vs set bundled unbundling 在本页 item 2 续。

2. **看见失败 / 看见重复 / 这份重复 is not already 已经能恢复 interchangeable，也不是已经 ValidatorUpdate bundled（318） interchangeable / 906 validatorupdate-notdup interchangeable / 318 validatorupdate item 3 power 0 interchangeable / 907 validatorupdate-notzero interchangeable，也不是已经 H 的更新已经在 H+1 计票 interchangeable / 35 height-effect interchangeable。**  
   官方把失败和已经能重放修好分开——318 bundled 第二件事常与 35 混成「看见重复就已经能恢复或已经是哪一高度生效 interchangeable」，本页钉 not already recoverable 单句。

3. **看见同一把钥 / 看见失败 / 这份重复 is not already 已经交差 interchangeable，也不是已经 ValidatorUpdate bundled（318） interchangeable / 906 validatorupdate-notdup interchangeable / 905 validatorupdate-notempty interchangeable，也不是已经能写两行 interchangeable。**  
   官方把同一把钥和已经能写两行 / 已经交差分开。看见同一把钥，不是已经交差 interchangeable。318 validatorupdate vs set bundled unbundling 在本页 item 2 续。

怎样编 `ValidatorUpdate`、怎样算总权、公钥类型表是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **同一批重复公钥 not already last wins ≠ 已经按后一条改权 interchangeable：** 官方把同一批不得重复和按后一条算分开。
- **看见失败 not already recoverable ≠ 已经能恢复 interchangeable：** 官方把不可恢复失败和已经能重放修好分开。
- **看见同一把钥 not already settled ≠ 已经交差 interchangeable：** 官方把同一把钥和已经交差分开；318 validatorupdate vs set bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 同一批重复公钥 | 不是已经按后一条改权 | 不是 H 的更新已经在 H+1 计票（35） |
| 看见失败 | 不是已经能恢复 | 不是同一高度换轮已经换了集合（302） |
| 看见同一把钥 | 不是已经交差 | 不是 InitChain 空名单就已经没有集合（905） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同一批重复公钥 not already last wins / not already recoverable / not already settled 正式三事（318 余量），必须分开是不是已经按后一条改权、是不是已经能恢复、是不是已经交差。可以跳过「看见重复就已经能恢复」。不要把 MaxTotalVotingPower 当不确定默认。不要另写怎样编更新或怎样算总权。318 validatorupdate vs set bundled unbundling 在本页 item 2 续；续 [`worked-example-validatorupdate-notzero-vs-bundled.md`](worked-example-validatorupdate-notzero-vs-bundled.md)（不变量 907 item 3）。

## 本页不抄

- 怎样编 `ValidatorUpdate`、怎样算总权、公钥类型表。
- ValidatorUpdate bundled。那是不变量 318。
- InitChain 空名单就已经没有集合。那是不变量 318 item 1 余量 / 905。
- H 的更新已经在 H+1 计票。那是不变量 35。
- 同一高度换轮已经换了集合。那是不变量 302。
