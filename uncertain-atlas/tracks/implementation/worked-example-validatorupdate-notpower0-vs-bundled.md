# 例：看见写成 0 / 看见总权 / 看见四种钥型 is not already already delete outsider interchangeable / already no max interchangeable / already key-type chosen interchangeable

**层次**：实现 / power 0 不是已经删掉不在集合里的人 not already delete outsider / not already no max / not already key-type chosen 正式三事（318 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating the Validator Set。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)、[L4.5](../../courses/level-04-bft/L04-M05-validator-set.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5 mempool。本页是「power 0 不是已经删掉不在集合里的人 not already delete outsider / not already no max / not already key-type chosen 正式三事（318 余量）/ not 715 validatorupdate-notpower0 interchangeable / not 318 validatorupdate bundled interchangeable」，不是 ValidatorUpdate vs set bundled（318），也不是 InitChain 空名单不是已经没有集合（713 item 1 余量）或同一批重复公钥不是已经能恢复（714 item 2 余量）。不要另写怎样编 `ValidatorUpdate` 或怎样算总权。

## 官方三件事

规范把 Requirements 里投票权必须非负、写成 0 时这个人**必须已经在集合里**才会被删掉、大于 0 则不在就加入在就改权、新集合总投票权不得超过 `MaxTotalVotingPower`、四种钥型表 和「已经是写成 0 就已经能删不在名单里的人 interchangeable / 已经是看见总权就已经没有上限 interchangeable / 已经是看见四种钥型就已经选型 interchangeable / 已经是 ValidatorUpdate vs set bundled interchangeable」分开写成三件独立的实现事，不是「看见 power 写成 0 就已经删掉 interchangeable / 就已经能对不在集合里的人写 0 interchangeable / 就已经没有总权上限 interchangeable」一件事：

1. **看见写成 0 / 看见 power 写成 0 / 看见名单里没有这个人 is not already 已经能删一个不在名单里的人 interchangeable / 已经 delete outsider interchangeable / 已经对不在集合里的人写 0 interchangeable / 318 validatorupdate bundled interchangeable / 33 four gates interchangeable / validatorupdate-sold-as-set interchangeable，也不是已经 ValidatorUpdate vs set bundled（318） interchangeable / 715 validatorupdate-notpower0 interchangeable / 318 validatorupdate item 3 interchangeable，也不是已经 power 0 不是已经删掉不在集合里的人 not already delete outsider / not already no max / not already key-type chosen 正式三事 bundled（318 item 3 余量） interchangeable / 318 validatorupdate item 3 interchangeable，也不是已经 InitChain 空名单不是已经没有集合（713） interchangeable / 714 validatorupdate-notdup interchangeable / 35 validator delay interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：写成 0 时，这个人**必须已经在集合里**，才会被删掉。看见写成 0，不是已经能删一个不在名单里的人 interchangeable——318 钉 bundled 三事，本页从 item 3 侧钉 not already delete outsider 单句。看见 power 写成 0，不是已经 ValidatorUpdate vs set bundled（318） interchangeable——318 钉 bundled，本页钉 item 3 第一件事。看见名单里没有这个人，不是已经 InitChain 空名单不是已经没有集合（713） interchangeable——713 另钉 item 1，本页钉 item 3 第一件事。318 validatorupdate vs set bundled unbundling 在本页 item 3 启动。

2. **看见总权 / 看见新集合总投票权 / 看见 MaxTotalVotingPower is not already 已经没有上限 interchangeable / 已经 no max interchangeable / 已经无限总权 interchangeable / 318 validatorupdate bundled interchangeable / 315 maxgas interchangeable，也不是已经 ValidatorUpdate vs set bundled（318） interchangeable / 715 validatorupdate-notpower0 interchangeable / 318 validatorupdate item 1 空名单 interchangeable / 318 validatorupdate item 2 重复 interchangeable，也不是已经 power 0 不是已经删掉不在集合里的人 not already delete outsider / not already no max / not already key-type chosen 正式三事 bundled（318 item 3 余量） interchangeable / 318 validatorupdate item 3 interchangeable，也不是已经能删不在名单里的人（本页第一件事） interchangeable。**  
   官方写：新集合总投票权不得超过 `MaxTotalVotingPower`。看见总权，不是已经没有上限 interchangeable——本页钉 not already no max 单句。看见新集合总投票权，不是已经同一批重复公钥不是已经能恢复（714） interchangeable——714 另钉 item 2，本页钉 item 3 第二件事。看见 MaxTotalVotingPower，不是已经 MaxGas 已经在执行（315） interchangeable——315 另钉，本页钉 item 3 第二件事。318 validatorupdate vs set bundled unbundling 在本页 item 3 启动。

3. **看见四种钥型 / 看见公钥类型表 / 看见钥型列表 is not already 已经选型 interchangeable / 已经 key-type chosen interchangeable / 已经选定钥型 interchangeable / 318 validatorupdate bundled interchangeable / 35 validator delay interchangeable，也不是已经 ValidatorUpdate vs set bundled（318） interchangeable / 715 validatorupdate-notpower0 interchangeable / 318 validatorupdate item 1 / 318 validatorupdate item 2，也不是已经 power 0 不是已经删掉不在集合里的人 not already delete outsider / not already no max / not already key-type chosen 正式三事 bundled（318 item 3 余量） interchangeable / 318 validatorupdate item 3 interchangeable，也不是已经能删不在名单里的人（本页第一件事） interchangeable / 已经没有上限（本页第二件事） interchangeable。**  
   官方把四种钥型表和已经选型路径分开——看见四种钥型，不等于已经选型。看见四种钥型，不是已经选型 interchangeable——本页钉 not already key-type chosen 单句。看见公钥类型表，不是已经能删不在名单里的人（本页第一件事） interchangeable——三件事分开钉。看见钥型列表，不是已经 H 的更新已经在 H+1 计票（35） interchangeable——35 另钉。318 validatorupdate vs set bundled unbundling 在本页 item 3 完成。

怎样编 `ValidatorUpdate`、怎样算总权、公钥类型表是规范里的取值或做法，本页不抄。ValidatorUpdate vs set bundled（318）、InitChain 空名单不是已经没有集合（318 item 1 余量 / 713）、同一批重复公钥不是已经能恢复（318 item 2 余量 / 714）、H 更新生效（35）、MaxGas（315）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **写成 0 not already delete outsider ≠ 318 / 33 interchangeable：** 官方把必须已在集合里才删单句和已经能删不在名单里的人路径分开。
- **看见总权 not already no max ≠ 已经没有上限 interchangeable：** 官方把 MaxTotalVotingPower 单句和已经无限总权路径分开。
- **看见四种钥型 not already key-type chosen ≠ 已经选型 interchangeable：** 官方把钥型表单句和已经选型路径分开；318 validatorupdate vs set bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 写成 0 | 不是 already delete outsider | 不是空名单 alone（713） |
| 看见总权 | 不是 already no max | 不是重复公钥 alone（714） |
| 看见四种钥型 | 不是 already key-type chosen | 不是 H+1 计票 alone（35） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 power 0 不是已经删掉不在集合里的人 not already delete outsider / not already no max / not already key-type chosen 正式三事（318 余量），必须分开写成 0 是不是 already delete outsider interchangeable / 318 validatorupdate bundled interchangeable / validatorupdate-sold-as-set interchangeable、看见总权 是不是 already no max interchangeable、看见四种钥型 是不是 already key-type chosen interchangeable。可以跳过「看见写成 0 就已经能删不在名单里的人 interchangeable / 就已经没有总权上限 interchangeable / 就已经选型 interchangeable」。不要另写怎样编更新。不要把 `MaxTotalVotingPower` 当不确定默认。318 validatorupdate vs set bundled unbundling 在本页 item 3 完成（713 + 714 + 715）。

## 本页不抄

- 怎样编 `ValidatorUpdate`、怎样算总权、公钥类型表。
- ValidatorUpdate vs set bundled。那是不变量 318。
- InitChain 空名单不是已经没有集合。那是不变量 318 item 1 余量 / 713。
- 同一批重复公钥不是已经能恢复。那是不变量 318 item 2 余量 / 714。
- H+1 / H+2 / H+3。那是不变量 35。
- MaxGas 已经在执行。那是不变量 315。
- 四门已经结算。那是不变量 33。
