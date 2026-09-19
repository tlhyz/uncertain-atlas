# 例：看见重复 / 看见失败 / 看见同一把钥 is not already already last-wins interchangeable / already recoverable interchangeable / already two rows interchangeable

**层次**：实现 / 同一批重复公钥不是已经能恢复 not already last-wins / not already recoverable / not already two rows 正式三事（318 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating the Validator Set。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)、[L4.5](../../courses/level-04-bft/L04-M05-validator-set.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5 mempool。本页是「同一批重复公钥不是已经能恢复 not already last-wins / not already recoverable / not already two rows 正式三事（318 余量）/ not 714 validatorupdate-notdup interchangeable / not 318 validatorupdate bundled interchangeable」，不是 ValidatorUpdate vs set bundled（318），也不是 InitChain 空名单不是已经没有集合（713 item 1 余量）或 power 0 不是已经删掉不在集合里的人（715 item 3 余量）。不要另写怎样编 `ValidatorUpdate` 或怎样算总权。

## 官方三件事

规范把 Requirements 里应用必须保证**同一批**更新里没有重复、一把公钥在这一次更新里只能出现一次、若带了重复则**块执行会不可恢复地失败** 和「已经是看见重复就已经按后一条改权 interchangeable / 已经是看见失败就已经能重放修好 interchangeable / 已经是看见同一把钥就已经能写两行 interchangeable / 已经是 ValidatorUpdate vs set bundled interchangeable」分开写成三件独立的实现事，不是「看见一次更新里同一把公钥出现两次 就已经按后一条改权 interchangeable / 就已经能恢复 interchangeable / 就已经能写两行 interchangeable」一件事：

1. **看见重复 / 看见一次更新里同一把公钥出现两次 / 看见同一批重复 is not already 已经按后一条改权 interchangeable / 已经 last-wins interchangeable / 已经按后一条算 interchangeable / 318 validatorupdate bundled interchangeable / 33 four gates interchangeable / validatorupdate-sold-as-set interchangeable，也不是已经 ValidatorUpdate vs set bundled（318） interchangeable / 714 validatorupdate-notdup interchangeable / 318 validatorupdate item 2 interchangeable，也不是已经同一批重复公钥不是已经能恢复 not already last-wins / not already recoverable / not already two rows 正式三事 bundled（318 item 2 余量） interchangeable / 318 validatorupdate item 2 interchangeable，也不是已经 InitChain 空名单不是已经没有集合（713） interchangeable / 715 validatorupdate-notpower0 interchangeable / 35 validator delay interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：应用必须保证**同一批**更新里没有重复，一把公钥在这一次更新里只能出现一次。看见重复，不是已经按后一条改权 interchangeable——318 钉 bundled 三事，本页从 item 2 侧钉 not already last-wins 单句。看见一次更新里同一把公钥出现两次，不是已经 ValidatorUpdate vs set bundled（318） interchangeable——318 钉 bundled，本页钉 item 2 第一件事。看见同一批重复，不是已经 InitChain 空名单不是已经没有集合（713） interchangeable——713 另钉 item 1，本页钉 item 2 第一件事。318 validatorupdate vs set bundled unbundling 在本页 item 2 续。

2. **看见失败 / 看见块执行失败 / 看见不可恢复失败 is not already 已经能重放修好 interchangeable / 已经 recoverable interchangeable / 已经能恢复 interchangeable / 318 validatorupdate bundled interchangeable / 320 crash recovery interchangeable，也不是已经 ValidatorUpdate vs set bundled（318） interchangeable / 714 validatorupdate-notdup interchangeable / 318 validatorupdate item 1 空名单 interchangeable / 318 validatorupdate item 3 power0 interchangeable，也不是已经同一批重复公钥不是已经能恢复 not already last-wins / not already recoverable / not already two rows 正式三事 bundled（318 item 2 余量） interchangeable / 318 validatorupdate item 2 interchangeable，也不是已经按后一条改权（本页第一件事） interchangeable。**  
   官方写：若带了重复，**块执行会不可恢复地失败**。看见失败，不是已经能重放修好 interchangeable——本页钉 not already recoverable 单句。看见块执行失败，不是已经 power 0 不是已经删掉不在集合里的人（715） interchangeable——715 另钉 item 3，本页钉 item 2 第二件事。看见不可恢复失败，不是已经 Crash Recovery 能修好（320） interchangeable——320 另钉，本页钉 item 2 第二件事。318 validatorupdate vs set bundled unbundling 在本页 item 2 续。

3. **看见同一把钥 / 看见同一把公钥 / 看见一把公钥出现两次 is not already 已经能写两行 interchangeable / 已经 two rows interchangeable / 已经能写两份更新 interchangeable / 318 validatorupdate bundled interchangeable / 33 four gates interchangeable，也不是已经 ValidatorUpdate vs set bundled（318） interchangeable / 714 validatorupdate-notdup interchangeable / 318 validatorupdate item 1 / 318 validatorupdate item 3，也不是已经同一批重复公钥不是已经能恢复 not already last-wins / not already recoverable / not already two rows 正式三事 bundled（318 item 2 余量） interchangeable / 318 validatorupdate item 2 interchangeable，也不是已经按后一条改权（本页第一件事） interchangeable / 已经能恢复（本页第二件事） interchangeable。**  
   官方把一把公钥只能出现一次和已经能写两行路径分开——看见同一把钥，不等于已经能写两行。看见同一把钥，不是已经能写两行 interchangeable——本页钉 not already two rows 单句。看见同一把公钥，不是已经按后一条改权（本页第一件事） interchangeable——三件事分开钉。看见一把公钥出现两次，不是已经四门已经结算（33） interchangeable——33 另钉。318 validatorupdate vs set bundled unbundling 在本页 item 2 完成。

怎样编 `ValidatorUpdate`、怎样算总权、公钥类型表是规范里的取值或做法，本页不抄。ValidatorUpdate vs set bundled（318）、InitChain 空名单不是已经没有集合（318 item 1 余量 / 713）、power 0 不是已经删掉不在集合里的人（318 item 3 余量 / 715）、H 更新生效（35）、Crash Recovery（320）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **看见重复 not already last-wins ≠ 318 / 33 interchangeable：** 官方把同一批不得重复单句和已经按后一条改权路径分开。
- **看见失败 not already recoverable ≠ 已经能重放修好 interchangeable：** 官方把不可恢复失败单句和已经能恢复路径分开。
- **看见同一把钥 not already two rows ≠ 已经能写两行 interchangeable：** 官方把只能出现一次单句和已经能写两行路径分开；318 validatorupdate vs set bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 看见重复 | 不是 already last-wins | 不是空名单 alone（713） |
| 看见失败 | 不是 already recoverable | 不是 power 0 alone（715） |
| 看见同一把钥 | 不是 already two rows | 不是 Crash Recovery alone（320） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同一批重复公钥不是已经能恢复 not already last-wins / not already recoverable / not already two rows 正式三事（318 余量），必须分开看见重复 是不是 already last-wins interchangeable / 318 validatorupdate bundled interchangeable / validatorupdate-sold-as-set interchangeable、看见失败 是不是 already recoverable interchangeable、看见同一把钥 是不是 already two rows interchangeable。可以跳过「看见重复就已经按后一条改权 interchangeable / 就已经能恢复 interchangeable / 就已经能写两行 interchangeable」。不要另写怎样编更新。318 validatorupdate vs set bundled unbundling 在本页 item 2 完成；续 [`worked-example-validatorupdate-notpower0-vs-bundled.md`](worked-example-validatorupdate-notpower0-vs-bundled.md)（不变量 715 item 3）。

## 本页不抄

- 怎样编 `ValidatorUpdate`、怎样算总权、公钥类型表。
- ValidatorUpdate vs set bundled。那是不变量 318。
- InitChain 空名单不是已经没有集合。那是不变量 318 item 1 余量 / 713。
- power 0 不是已经删掉不在集合里的人。那是不变量 318 item 3 余量 / 715。
- H+1 / H+2 / H+3。那是不变量 35。
- Crash Recovery。那是不变量 320。
- 四门已经结算。那是不变量 33。
