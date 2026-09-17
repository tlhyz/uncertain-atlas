# 例：看见 power 写成 0 is not already deleted outsider interchangeable / not already no cap interchangeable / not already settled interchangeable

**层次**：实现 / power 写成 0 not already deleted outsider / not already no cap / not already settled 正式三事（318 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating the Validator Set。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)、[L4.5](../../courses/level-04-bft/L04-M05-validator-set.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、mempool。本页是「power 写成 0 not already deleted outsider / not already no cap / not already settled 正式三事（318 余量）/ not 907 validatorupdate-notzero interchangeable / not 318 validatorupdate-vs-set bundled interchangeable」，不是 ValidatorUpdate bundled（318），也不是同一高度换轮已经换了集合（302），也不是 Validator 就已经改了集合（364/835）。不要另写怎样编更新或怎样算总权。

## 官方三件事

1. **看见 power 写成 0 / 看见名单里没有这个人 这份 0 is not already 已经删掉 interchangeable，也不是已经 ValidatorUpdate bundled（318） interchangeable / 907 validatorupdate-notzero interchangeable / 905 validatorupdate-notempty interchangeable / 318 validatorupdate item 1 空名单 interchangeable，也不是已经 power 写成 0 not already deleted outsider / not already no cap / not already settled 正式三事 bundled（318 item 3 余量） interchangeable / 318 validatorupdate item 3 interchangeable。**  
   官方写：投票权必须非负。写成 0 时，这个人必须已经在集合里，才会被删掉。看见写成 0，不是已经能删一个不在名单里的人 interchangeable——本页从 318 item 3 侧钉 not already deleted outsider 单句。318 validatorupdate vs set bundled unbundling 在本页 item 3 完成。

2. **看见总权 / 看见写成 0 / 这份 0 is not already 已经没有上限 interchangeable，也不是已经 ValidatorUpdate bundled（318） interchangeable / 907 validatorupdate-notzero interchangeable / 318 validatorupdate item 2 重复 interchangeable / 906 validatorupdate-notdup interchangeable，也不是已经同一高度换轮已经换了集合 interchangeable / 302 round-set interchangeable。**  
   官方把总权和已经没有上限分开——318 bundled 第三件事常与 302 混成「看见写成 0 就已经删掉或不已经有上限 interchangeable」，本页钉 not already no cap 单句。

3. **看见四种钥型 / 看见总权 / 这份 0 is not already 已经交差 interchangeable，也不是已经 ValidatorUpdate bundled（318） interchangeable / 907 validatorupdate-notzero interchangeable / 905 validatorupdate-notempty interchangeable，也不是已经选型 interchangeable。**  
   官方把四种钥型和已经选型 / 已经交差分开。看见四种钥型，不是已经交差 interchangeable。318 validatorupdate vs set bundled unbundling 在本页 item 3 完成。

怎样编 `ValidatorUpdate`、怎样算总权、公钥类型表是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **power 写成 0 not already deleted outsider ≠ 已经删掉不在集合里的人 interchangeable：** 官方把必须已在集合里才删分开。
- **看见总权 not already no cap ≠ 已经没有上限 interchangeable：** 官方把总权不得超过 MaxTotalVotingPower 和已经没有上限分开。
- **看见四种钥型 not already settled ≠ 已经交差 interchangeable：** 官方把四种钥型和已经交差分开；318 validatorupdate vs set bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| power 写成 0 | 不是已经删掉不在集合里的人 | 不是同一高度换轮已经换了集合（302） |
| 看见总权 | 不是已经没有上限 | 不是 Validator 就已经改了集合（364/835） |
| 看见四种钥型 | 不是已经交差 | 不是 InitChain 空名单就已经没有集合（905） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 power 写成 0 not already deleted outsider / not already no cap / not already settled 正式三事（318 余量），必须分开是不是已经删掉不在集合里的人、是不是已经没有上限、是不是已经交差。可以跳过「看见写成 0 就已经删掉」。不要把 MaxTotalVotingPower 当不确定默认。不要另写怎样编更新或怎样算总权。318 validatorupdate vs set bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样编 `ValidatorUpdate`、怎样算总权、公钥类型表。
- ValidatorUpdate bundled。那是不变量 318。
- InitChain 空名单就已经没有集合。那是不变量 318 item 1 余量 / 905。
- 同一高度换轮已经换了集合。那是不变量 302。
- Validator 就已经改了集合。那是不变量 364 / 835。
