# 例：看见必须回四列 is not already changed set interchangeable / not already settled interchangeable / not already header AppHash interchangeable

**层次**：实现 / 必须回四列 not already changed set / not already settled / not already header AppHash 正式三事（363 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「必须回四列 not already changed set / not already settled / not already header AppHash 正式三事（363 余量）/ not 838 finalize-equiv-notchanged interchangeable / not 363 finalize-equiv-vs-gates bundled interchangeable」，不是 Finalize 回包义务 bundled（363），也不是 ValidatorUpdate 就已经改了集合（364/835），也不是本头 AppHash 就已经是本高度交差（147），也不是 InitChain 空名单就已经没有集合（318）。不要另写怎样写 Finalize 回包。

## 官方三件事

1. **看见必须回 `app_hash` / `tx_results` / `validator_updates` / `consensus_param_updates` / 看见回了四列 这份必须回 is not already 已经改了集合 interchangeable / 364 validator / 835 validator-notchanged interchangeable，也不是已经 Finalize 回包义务 bundled（363） interchangeable / 838 finalize-equiv-notchanged interchangeable / 836 finalize-equiv-notgates interchangeable / 363 finalize-equiv item 1 等价 interchangeable，也不是已经必须回四列 not already changed set / not already settled / not already header AppHash 正式三事 bundled（363 item 3 余量） interchangeable / 363 finalize-equiv item 3 interchangeable。**  
   官方写：执行完这块，应用必须给 `FinalizeBlockResponse.app_hash`、`tx_results`、`validator_updates`、`consensus_param_updates` 提供值。看见回了四列，不是已经改了集合 interchangeable——本页从 363 item 3 侧钉 not already changed set 单句。363 finalize-equiv vs gates bundled unbundling 在本页 item 3 完成。

2. **看见回了四列 / 看见有 `validator_updates` / 这份必须回 is not already 已经交差 interchangeable，也不是已经 Finalize 回包义务 bundled（363） interchangeable / 838 finalize-equiv-notchanged interchangeable / 363 finalize-equiv item 2 定奖惩 interchangeable / 837 finalize-equiv-notslashed interchangeable，也不是已经 InitChain 空名单就已经没有集合 interchangeable / 318 initempty interchangeable，也不是已经 ValidatorUpdate 就已经改了集合 interchangeable / 364 validator / 835 validator-notchanged interchangeable。**  
   官方把有 validator_updates 和已经交差分开——363 bundled 第三件事常与 364 / 147 混成「看见回了四列就已经改了集合或已经印进本头 interchangeable」，本页钉 not already settled 单句。

3. **看见回了四列 / 看见必须回 / 这份必须回 is not already 已经印进本头 interchangeable / 147 header AppHash interchangeable，也不是已经 Finalize 回包义务 bundled（363） interchangeable / 838 finalize-equiv-notchanged interchangeable / 836 finalize-equiv-notgates interchangeable，也不是已经 finresp-notsettled 那条别前缀 interchangeable。**  
   官方把必须回和已经印进本头分开。看见必须回，不是已经印进本头 interchangeable。363 finalize-equiv vs gates bundled unbundling 在本页 item 3 完成。

怎样写 Finalize 回包、怎样算奖惩、怎样填四列是规范里的做法，本页不抄。

## 官方为什么这样拆

- **必须回四列 not already changed set ≠ 364/835 interchangeable：** 官方把必须回和已经改完分开。
- **看见有 validator_updates not already settled ≠ 已经交差 interchangeable：** 官方把有 validator_updates 和已经交差分开。
- **看见必须回 not already header AppHash ≠ 147 interchangeable：** 官方把必须回和已经印进本头分开；363 finalize-equiv vs gates bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 必须回四列 | 不是已经改了集合 | 不是 ValidatorUpdate 就已经改了集合（364/835） |
| 看见有 validator_updates | 不是已经交差 | 不是 InitChain 空名单就已经没有集合（318） |
| 看见必须回 | 不是已经印进本头 | 不是本头 AppHash 就已经是本高度交差（147） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看必须回四列 not already changed set / not already settled / not already header AppHash 正式三事（363 余量），必须分开是不是已经改了集合 interchangeable / 364 / 835、是不是已经交差、是不是已经印进本头 interchangeable / 147。可以跳过「看见回了四列就已经改了集合」。不要另写怎样写 Finalize 回包。363 finalize-equiv vs gates bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Finalize 回包、怎样算奖惩、怎样填四列。
- Finalize 回包义务 bundled。那是不变量 363。
- Finalize 等价于 ABCI 1.0 那三步。那是不变量 363 item 1 余量 / 836。
- ValidatorUpdate 就已经改了集合。那是不变量 364 / 835。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
- InitChain 空名单就已经没有集合。那是不变量 318。
