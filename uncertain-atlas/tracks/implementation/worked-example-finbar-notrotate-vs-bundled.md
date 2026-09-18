# 例：看见 FinalizeBlockResponse.validator_updates is not already h1-rotate interchangeable / not already set-changed interchangeable / not already four-col interchangeable

**层次**：实现 / FinalizeBlockResponse.validator_updates not already h1-rotate / not already set-changed / not already four-col 正式三事（431 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockResponse.validator_updates not already h1-rotate / not already set-changed / not already four-col 正式三事（431 余量）/ not 1072 finbar-notrotate interchangeable / not 431 finrespbar-vs-header bundled interchangeable」，不是 Finalize 回包栏 bundled（431），也不是高度 H 的 validator_updates 已经在 H+1 计票（35），也不是 Validator 用 address 认人就已经改了集合。不要另写怎样写 Finalize 回包栏。

## 官方三件事

1. **看见 FinalizeBlockResponse.validator_updates 是对验证者集合的改动 / 看见回了 validator_updates 这份栏 is not already 已经在 H+1 换人 interchangeable，也不是已经 Finalize 回包栏 bundled（431） interchangeable / 1072 finbar-notrotate interchangeable / 1070 finbar-notheader interchangeable / 431 finrespbar item 1 events interchangeable，也不是已经 FinalizeBlockResponse.validator_updates not already h1-rotate / not already set-changed / not already four-col 正式三事 bundled（431 item 3 余量） interchangeable / 431 finrespbar item 3 interchangeable。**  
   官方写：validator_updates 是 Changes to validator set (set voting power to 0 to remove)。Deterministic 列是 Yes。看见回了更新，不是已经在 H+1 换人 interchangeable——本页从 431 item 3 侧钉 not already h1-rotate 单句。431 finrespbar vs header bundled unbundling 在本页 item 3 完成。

2. **看见有 ValidatorUpdate / 看见回了 validator_updates / 这份栏 is not already 已经改了集合 interchangeable，也不是已经 Finalize 回包栏 bundled（431） interchangeable / 1072 finbar-notrotate interchangeable / 431 finrespbar item 2 tx_results interchangeable / 1071 finbar-notchktx interchangeable，也不是已经高度 H 的 validator_updates 已经在 H+1 计票 interchangeable / 35 validatorupdate interchangeable。**  
   官方把有 ValidatorUpdate 和已经改了集合分开。看见有 ValidatorUpdate，不是已经改了集合 interchangeable。本页钉 not already set-changed 单句。

3. **看见能指下一份集合 / 看见回了 validator_updates / 这份栏 is not already 已经必须回四列那种已经交差 interchangeable，也不是已经 Finalize 回包栏 bundled（431） interchangeable / 1072 finbar-notrotate interchangeable / 1070 finbar-notheader interchangeable，也不是已经 Validator 用 address 认人就已经改了集合 interchangeable。**  
   官方把能指下一份集合和已经必须回四列那种已经交差分开。看见能指下一份集合，不是已经必须回四列那种已经交差 interchangeable。431 finrespbar vs header bundled unbundling 在本页 item 3 完成。

怎样写 Finalize 回包栏、怎样编 events、怎样编 ValidatorUpdate 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockResponse.validator_updates not already h1-rotate ≠ 已经在 H+1 换人 interchangeable：** 官方把对验证者集合的改动和已经在 H+1 换人分开。
- **看见有 ValidatorUpdate not already set-changed ≠ 已经改了集合 interchangeable：** 官方把有 ValidatorUpdate 和已经改了集合分开。
- **看见能指下一份集合 not already four-col ≠ 已经必须回四列那种已经交差 interchangeable：** 官方把能指下一份集合和已经必须回四列那种已经交差分开；431 finrespbar vs header bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockResponse.validator_updates 是对验证者集合的改动 | 不是已经在 H+1 换人 | 不是高度 H 的 validator_updates 已经在 H+1 计票（35） |
| 看见有 ValidatorUpdate | 不是已经改了集合 | 不是 Validator 用 address 认人就已经改了集合 |
| 看见能指下一份集合 | 不是已经必须回四列那种已经交差 | 不是 events 就已经印进本头（1070） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse.validator_updates not already h1-rotate / not already set-changed / not already four-col 正式三事（431 余量），必须分开是不是已经在 H+1 换人、是不是已经改了集合、是不是已经必须回四列那种已经交差。可以跳过「看见回了 Finalize 回包栏就已经印进本头」。不要另写怎样写 Finalize 回包栏。431 finrespbar vs header bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Finalize 回包栏、怎样编 events、怎样编 ValidatorUpdate。
- Finalize 回包栏 bundled。那是不变量 431。
- 高度 H 的 validator_updates 已经在 H+1 计票。那是不变量 35。
- Validator 用 address 认人就已经改了集合。那是相邻 Validator 页，不是本页。
