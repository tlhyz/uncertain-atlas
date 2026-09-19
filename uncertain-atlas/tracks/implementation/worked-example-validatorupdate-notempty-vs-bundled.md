# 例：看见回了空 / 没回人 / 能设初始集合 is not already already no set interchangeable / already deleted genesis interchangeable / already app empty set interchangeable

**层次**：实现 / InitChain 空名单不是已经没有集合 not already no set / not already deleted genesis / not already app empty set 正式三事（318 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating the Validator Set。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)、[L4.5](../../courses/level-04-bft/L04-M05-validator-set.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5 mempool。本页是「InitChain 空名单不是已经没有集合 not already no set / not already deleted genesis / not already app empty set 正式三事（318 余量）/ not 713 validatorupdate-notempty interchangeable / not 318 validatorupdate bundled interchangeable」，不是 ValidatorUpdate vs set bundled（318），也不是同一批重复公钥不是已经能恢复（714 item 2 余量）或 power 0 不是已经删掉不在集合里的人（715 item 3 余量）。不要另写怎样编 `ValidatorUpdate` 或怎样算总权。

## 官方三件事

规范把 Requirements 里应用可在 `InitChain` 设集合、也可在 `FinalizeBlock` 更新、`InitChain` 回的名单若**空**则 CometBFT **用创世文件里的验证者**、若**不空**则用回包这份当集合 和「已经是回了空就已经没有集合 interchangeable / 已经是没回人就已经删掉创世名单 interchangeable / 已经是能设初始集合就已经用了应用自己的空集 interchangeable / 已经是 ValidatorUpdate vs set bundled interchangeable」分开写成三件独立的实现事，不是「看见 InitChain 回了空名单 就已经没有集合 interchangeable / 就已经删掉创世名单 interchangeable / 就已经和创世 validators 空同一句 interchangeable」一件事：

1. **看见回了空 / 看见 InitChain 回了空名单 / 看见名单空 is not already 已经没有集合 interchangeable / 已经 no set interchangeable / 已经空集交差 interchangeable / 318 validatorupdate bundled interchangeable / 33 four gates interchangeable / validatorupdate-sold-as-set interchangeable，也不是已经 ValidatorUpdate vs set bundled（318） interchangeable / 713 validatorupdate-notempty interchangeable / 318 validatorupdate item 1 interchangeable，也不是已经 InitChain 空名单不是已经没有集合 not already no set / not already deleted genesis / not already app empty set 正式三事 bundled（318 item 1 余量） interchangeable / 318 validatorupdate item 1 interchangeable，也不是已经同一批重复公钥不是已经能恢复（714） interchangeable / 715 validatorupdate-notpower0 interchangeable / 303 genesis validators interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：`InitChain` 回的名单若**空**，CometBFT **用创世文件里的验证者**。看见回了空，不是已经没有集合 interchangeable——318 钉 bundled 三事，本页从 item 1 侧钉 not already no set 单句。看见 InitChain 回了空名单，不是已经 ValidatorUpdate vs set bundled（318） interchangeable——318 钉 bundled，本页钉 item 1 第一件事。看见名单空，不是已经同一批重复公钥不是已经能恢复（714） interchangeable——714 另钉 item 2，本页钉 item 1 第一件事。318 validatorupdate vs set bundled unbundling 在本页 item 1 启动。

2. **看见没回人 / 看见没回验证者 / 看见回包没有验证者 is not already 已经删掉创世名单 interchangeable / 已经 deleted genesis interchangeable / 已经清掉创世集合 interchangeable / 318 validatorupdate bundled interchangeable / 303 genesis validators interchangeable，也不是已经 ValidatorUpdate vs set bundled（318） interchangeable / 713 validatorupdate-notempty interchangeable / 318 validatorupdate item 2 重复 interchangeable / 318 validatorupdate item 3 power0 interchangeable，也不是已经 InitChain 空名单不是已经没有集合 not already no set / not already deleted genesis / not already app empty set 正式三事 bundled（318 item 1 余量） interchangeable / 318 validatorupdate item 1 interchangeable，也不是已经没有集合（本页第一件事） interchangeable。**  
   官方把回空改用创世名单和已经删掉创世名单路径分开——没回人，不等于已经删掉创世名单。看见没回人，不是已经删掉创世名单 interchangeable——本页钉 not already deleted genesis 单句。看见没回验证者，不是已经 power 0 不是已经删掉不在集合里的人（715） interchangeable——715 另钉 item 3，本页钉 item 1 第二件事。看见回包没有验证者，不是已经创世 validators 空已经没有集合（303） interchangeable——303 另钉，本页钉 item 1 第二件事。318 validatorupdate vs set bundled unbundling 在本页 item 1 启动。

3. **看见能设初始集合 / 看见 InitChain 能设集合 / 看见应用可设集合 is not already 已经用了应用自己的空集 interchangeable / 已经 app empty set interchangeable / 已经和创世 validators 空同一句 interchangeable / 318 validatorupdate bundled interchangeable / 303 genesis validators interchangeable，也不是已经 ValidatorUpdate vs set bundled（318） interchangeable / 713 validatorupdate-notempty interchangeable / 318 validatorupdate item 2 / 318 validatorupdate item 3，也不是已经 InitChain 空名单不是已经没有集合 not already no set / not already deleted genesis / not already app empty set 正式三事 bundled（318 item 1 余量） interchangeable / 318 validatorupdate item 1 interchangeable，也不是已经没有集合（本页第一件事） interchangeable / 已经删掉创世名单（本页第二件事） interchangeable。**  
   官方把能设初始集合和已经用了应用自己的空集 / 已经和创世 validators 空同一句路径分开——能设，不等于已经空集交差。看见能设初始集合，不是已经 app empty set interchangeable——本页钉 not already app empty set 单句。看见 InitChain 能设集合，不是已经没有集合（本页第一件事） interchangeable——三件事分开钉。看见应用可设集合，不是已经创世 validators 空已经没有集合（303） interchangeable——303 另钉创世字段。318 validatorupdate vs set bundled unbundling 在本页 item 1 完成。

怎样编 `ValidatorUpdate`、怎样算总权、公钥类型表是规范里的取值或做法，本页不抄。ValidatorUpdate vs set bundled（318）、同一批重复公钥不是已经能恢复（318 item 2 余量 / 714）、power 0 不是已经删掉不在集合里的人（318 item 3 余量 / 715）、创世 validators 空（303）、H 更新生效（35）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **回了空 not already no set ≠ 318 / 33 interchangeable：** 官方把改用创世名单单句和已经没有集合路径分开。
- **没回人 not already deleted genesis ≠ 已经删掉创世名单 interchangeable：** 官方把回空改用创世单句和已经删掉创世路径分开。
- **能设初始集合 not already app empty set ≠ 已经和创世 validators 空同一句 interchangeable：** 官方把可设集合单句和已经空集交差路径分开；318 validatorupdate vs set bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回了空 | 不是 already no set | 不是重复公钥 alone（714） |
| 没回人 | 不是 already deleted genesis | 不是 power 0 alone（715） |
| 能设初始集合 | 不是 already app empty set | 不是创世 validators 空 alone（303） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 空名单不是已经没有集合 not already no set / not already deleted genesis / not already app empty set 正式三事（318 余量），必须分开回了空 是不是 already no set interchangeable / 318 validatorupdate bundled interchangeable / validatorupdate-sold-as-set interchangeable、没回人 是不是 already deleted genesis interchangeable、能设初始集合 是不是 already app empty set interchangeable。可以跳过「看见回了空就已经没有集合 interchangeable / 就已经删掉创世名单 interchangeable / 就已经和创世 validators 空同一句 interchangeable」。不要另写怎样编更新。318 validatorupdate vs set bundled unbundling 在本页 item 1 完成；续 [`worked-example-validatorupdate-notdup-vs-bundled.md`](worked-example-validatorupdate-notdup-vs-bundled.md)（不变量 714 item 2）。

## 本页不抄

- 怎样编 `ValidatorUpdate`、怎样算总权、公钥类型表。
- ValidatorUpdate vs set bundled。那是不变量 318。
- 同一批重复公钥不是已经能恢复。那是不变量 318 item 2 余量 / 714。
- power 0 不是已经删掉不在集合里的人。那是不变量 318 item 3 余量 / 715。
- 创世 validators 空已经没有集合。那是不变量 303。
- H+1 / H+2 / H+3。那是不变量 35。
- 四门已经结算。那是不变量 33。
