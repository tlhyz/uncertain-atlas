# 例：看见空着 / 看见没回人 / 看见能空 is not already already empty interchangeable / already changed interchangeable / already genesis interchangeable

**层次**：实现 / validator_updates 空则引擎保持当前集合不是已经没有集合 not already empty / not already changed / not already genesis 正式三事（382 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「validator_updates 空则引擎保持当前集合不是已经没有集合 not already empty / not already changed / not already genesis 正式三事（382 余量）/ not 894 syncingheight-notempty interchangeable / not 382 syncingheight bundled interchangeable」，不是 syncingheight bundled（382），也不是 syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史（382 item 1 / 893）或 Finalize 回包 events 标成非确定不是已经必须确定（382 item 3 余量）。不要另写怎样写 Finalize 请求回包。

## 官方三件事

规范把 Methods 里 validator_updates 空则引擎保持当前集合 和「已经是空着就已经没有集合 interchangeable / 已经是没回人就已经改了集合 interchangeable / 已经是能空就已经是 InitChain 空名单 interchangeable / 已经是 syncingheight bundled interchangeable」分开写成三件独立的实现事，不是「看见空着就已经没有集合 interchangeable / 就已经改了集合 interchangeable / 就已经是 InitChain 空名单 interchangeable」一件事：

1. **看见空着 / 看见 validator_updates 空则引擎保持当前集合 / 看见 validator_updates 或 consensus_param_updates 可以空 is not already 已经没有集合 interchangeable / 已经 empty interchangeable / 已经没有集合交差 interchangeable / 382 syncingheight bundled interchangeable / 318 validatorupdate interchangeable / syncingheight-sold-as-history interchangeable，也不是已经 syncingheight bundled（382） interchangeable / 894 syncingheight-notempty interchangeable / 382 syncingheight item 2 interchangeable，也不是已经 validator_updates 空则引擎保持当前集合不是已经没有集合 not already empty / not already changed / not already genesis 正式三事 bundled（382 item 2 余量） interchangeable / 382 syncingheight item 2 interchangeable，也不是已经填了目标就已经有完整历史（382 item 1 / 893） interchangeable / 回了事件就已经必须确定（382 item 3） interchangeable / 318 validatorupdate interchangeable，也不是已经 InitChain 空名单就已经没有集合（318） interchangeable。**  
   官方写：`validator_updates` 或 `consensus_param_updates` 可以空。空着时，CometBFT 保持当前值。看见空着，不是已经没有集合。看见空着，不是已经 empty interchangeable——382 钉 bundled 三事，本页从 item 2 侧钉 not already empty 单句。看见 validator_updates 空则引擎保持当前集合，不是已经 syncingheight bundled（382） interchangeable——382 钉 bundled，本页钉 item 2 第一件事。看见可以空，不是已经 InitChain 空名单就已经没有集合（318） interchangeable——318 另钉。382 syncingheight-vs-history bundled unbundling 在本页 item 2 续。

2. **看见没回人 / 看见没回 validator_updates / 看见保持当前值 is not already 已经改了集合 interchangeable / 已经 changed interchangeable / 已经改了集合交差 interchangeable / 382 syncingheight bundled interchangeable / 318 validatorupdate interchangeable，也不是已经 syncingheight bundled（382） interchangeable / 894 syncingheight-notempty interchangeable / 382 syncingheight item 1 填了目标 interchangeable / 382 syncingheight item 3 回了事件 interchangeable，也不是已经 validator_updates 空则引擎保持当前集合不是已经没有集合 not already empty / not already changed / not already genesis 正式三事 bundled（382 item 2 余量） interchangeable / 382 syncingheight item 2 interchangeable，也不是已经没有集合（本页第一件事） interchangeable。**  
   官方写：看见没回人，不是已经改了集合。看见没回 validator_updates，不是已经 changed interchangeable——本页钉 not already changed 单句。看见保持当前值，不是已经没有集合（本页第一件事） interchangeable——三件事分开钉。382 syncingheight-vs-history bundled unbundling 在本页 item 2 续。

3. **看见能空 / 看见 Finalize 回包可以空着更新 / 看见空着不是 InitChain 那种空名单 is not already 已经是 InitChain 空名单 interchangeable / 已经 genesis interchangeable / 已经是创世空名单交差 interchangeable / 382 syncingheight bundled interchangeable / 318 validatorupdate interchangeable，也不是已经 syncingheight bundled（382） interchangeable / 894 syncingheight-notempty interchangeable / 382 syncingheight item 1 / 382 syncingheight item 3，也不是已经 validator_updates 空则引擎保持当前集合不是已经没有集合 not already empty / not already changed / not already genesis 正式三事 bundled（382 item 2 余量） interchangeable / 382 syncingheight item 2 interchangeable，也不是已经没有集合（本页第一件事） interchangeable / 已经改了集合（本页第二件事） interchangeable。**  
   官方写：看见能空，不是已经是 InitChain 那种空名单。看见 Finalize 回包可以空着更新，不是已经 genesis interchangeable——本页钉 not already genesis 单句。看见空着不是 InitChain 那种空名单，不是已经改了集合（本页第二件事） interchangeable——三件事分开钉。382 syncingheight-vs-history bundled unbundling 在本页 item 2 续。

怎样写 Finalize 请求、怎样空着更新、怎样编事件是规范里的做法，本页不抄。syncingheight bundled（382）、syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史（382 item 1 / 893）、Finalize 回包 events 标成非确定不是已经必须确定（382 item 3 余量）、InitChain 空名单就已经没有集合（318）、切进共识就已经有从创世的完整历史（323）、结果列表就已经同一顺序（316）是另外那套，本页不抄。

## 官方为什么这样拆

- **空着 not already empty ≠ 382 / 318 interchangeable：** 官方把 Finalize 空更新和已经没有集合分开。
- **没回人 not already changed ≠ 已经改了集合 interchangeable：** 官方把保持当前值和已经改了集合分开。
- **能空 not already genesis ≠ 已经是 InitChain 空名单 interchangeable：** 官方把 Finalize 能空和 InitChain 空名单分开；382 syncingheight-vs-history bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 空着 | 不是 already empty | 不是 InitChain 空名单就已经没有集合 alone（318） |
| 没回人 | 不是 already changed | 不是填了目标 already history alone（893） |
| 能空 | 不是 already genesis | 不是回了事件 already deterministic alone（382 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 validator_updates 空则引擎保持当前集合不是已经没有集合 not already empty / not already changed / not already genesis 正式三事（382 余量），必须分开空着 是不是 already empty interchangeable / 382 syncingheight bundled interchangeable / syncingheight-sold-as-history interchangeable、没回人 是不是 already changed interchangeable、能空 是不是 already genesis interchangeable。可以跳过「看见空着就已经没有集合 interchangeable / 就已经改了集合 interchangeable / 就已经是 InitChain 空名单 interchangeable」。不要另写怎样写 Finalize 请求回包。382 syncingheight-vs-history bundled unbundling 在本页 item 2 续（894）。

## 本页不抄

- 怎样写 Finalize 请求、怎样空着更新、怎样编事件。
- syncingheight bundled。那是不变量 382。
- syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史。那是不变量 382 item 1 / 893。
- Finalize 回包 events 标成非确定不是已经必须确定。那是不变量 382 item 3 余量。
- InitChain 空名单就已经没有集合。那是不变量 318。
- 切进共识就已经有从创世的完整历史。那是不变量 323。
- 结果列表就已经同一顺序。那是不变量 316。
