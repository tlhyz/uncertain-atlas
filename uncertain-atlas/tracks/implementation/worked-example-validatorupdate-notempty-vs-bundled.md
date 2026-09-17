# 例：看见 InitChain 回了空名单 is not already no set interchangeable / not already app empty set interchangeable / not already settled interchangeable

**层次**：实现 / InitChain 空名单 not already no set / not already app empty set / not already settled 正式三事（318 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating the Validator Set。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)、[L4.5](../../courses/level-04-bft/L04-M05-validator-set.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、mempool。本页是「InitChain 空名单 not already no set / not already app empty set / not already settled 正式三事（318 余量）/ not 905 validatorupdate-notempty interchangeable / not 318 validatorupdate-vs-set bundled interchangeable」，不是 ValidatorUpdate bundled（318），也不是创世 validators 空已经没有集合（303），也不是 Validator 用公钥认人就已经改了集合（364/835）。不要另写怎样编更新或怎样算总权。

## 官方三件事

1. **看见 InitChain 回了空名单 / 看见没回验证者 这份空名单 is not already 已经没有集合 interchangeable，也不是已经 ValidatorUpdate bundled（318） interchangeable / 905 validatorupdate-notempty interchangeable / 906 validatorupdate-notdup interchangeable / 318 validatorupdate item 2 重复 interchangeable，也不是已经 InitChain 空名单 not already no set / not already app empty set / not already settled 正式三事 bundled（318 item 1 余量） interchangeable / 318 validatorupdate item 1 interchangeable。**  
   官方写：应用可在 `InitChain` 设集合，也可在 `FinalizeBlock` 更新。`InitChain` 回的名单若空，CometBFT 用创世文件里的验证者。看见回了空，不是已经没有集合 interchangeable——本页从 318 item 1 侧钉 not already no set 单句。318 validatorupdate vs set bundled unbundling 在本页 item 1 启动。

2. **看见没回人 / 看见能设初始集合 / 这份空名单 is not already 已经用了应用自己的空集 interchangeable，也不是已经 ValidatorUpdate bundled（318） interchangeable / 905 validatorupdate-notempty interchangeable / 318 validatorupdate item 3 power 0 interchangeable / 907 validatorupdate-notzero interchangeable，也不是已经创世 validators 空已经没有集合 interchangeable / 303 genesis-empty interchangeable。**  
   官方把没回人和已经删掉创世名单 / 已经用了应用自己的空集分开——318 bundled 第一件事常与 303 混成「看见回了空就已经没有集合或已经和创世空同一句 interchangeable」，本页钉 not already app empty set 单句。

3. **看见能设初始集合 / 看见回了空 / 这份空名单 is not already 已经交差 interchangeable，也不是已经 ValidatorUpdate bundled（318） interchangeable / 905 validatorupdate-notempty interchangeable / 906 validatorupdate-notdup interchangeable，也不是已经 ValidatorUpdate 就已经改了集合 interchangeable / 364 / 835 validator-notchanged interchangeable。**  
   官方把能设初始集合和已经和创世 validators 空同一句 / 已经交差分开。看见能设初始集合，不是已经交差 interchangeable。318 validatorupdate vs set bundled unbundling 在本页 item 1 启动。

怎样编 `ValidatorUpdate`、怎样算总权、公钥类型表是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **InitChain 空名单 not already no set ≠ 已经没有集合 interchangeable：** 官方把回空和改用创世名单分开。
- **看见没回人 not already app empty set ≠ 已经用了应用自己的空集 interchangeable：** 官方把没回人和已经删掉创世名单分开。
- **看见能设初始集合 not already settled ≠ 已经交差 interchangeable：** 官方把能设初始集合和已经交差分开；318 validatorupdate vs set bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| InitChain 回空 | 不是已经没有集合 | 不是创世 validators 空已经没有集合（303） |
| 看见没回人 | 不是已经用了应用自己的空集 | 不是 ValidatorUpdate 就已经改了集合（364/835） |
| 看见能设初始集合 | 不是已经交差 | 不是同一批重复就已经能恢复（906） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 空名单 not already no set / not already app empty set / not already settled 正式三事（318 余量），必须分开是不是已经没有集合、是不是已经用了应用自己的空集、是不是已经交差。可以跳过「看见回了就已经定了」。不要把 MaxTotalVotingPower 当不确定默认。不要另写怎样编更新或怎样算总权。318 validatorupdate vs set bundled unbundling 在本页 item 1 启动；续 [`worked-example-validatorupdate-notdup-vs-bundled.md`](worked-example-validatorupdate-notdup-vs-bundled.md)（不变量 906 item 2）。

## 本页不抄

- 怎样编 `ValidatorUpdate`、怎样算总权、公钥类型表。
- ValidatorUpdate bundled。那是不变量 318。
- 同一批重复就已经能恢复。那是不变量 318 item 2 余量 / 906。
- 创世 validators 空已经没有集合。那是不变量 303。
- ValidatorUpdate 就已经改了集合。那是不变量 364 / 835。
