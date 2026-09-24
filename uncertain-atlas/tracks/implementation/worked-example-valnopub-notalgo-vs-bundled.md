# 例：看见省了字段 / 看见提到后量子公钥 / 看见 ABCI 不传公钥 is not already already algo interchangeable / already no-pq interchangeable / already settled interchangeable

**层次**：实现 / 不带 PubKey 不是已经选型 not already algo / not already no-pq / not already settled 正式三事（364 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator / ValidatorUpdate。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「不带 PubKey 不是已经选型 not already algo / not already no-pq / not already settled 正式三事（364 余量）/ not 840 valnopub-notalgo interchangeable / not 364 validator bundled interchangeable」，不是 Validator 类型 bundled（364），也不是 Validator 用 address 认人不是已经带了公钥（839 item 1 余量）或 ValidatorUpdate 用公钥认人不是已经改了集合（841 item 3 余量）。不要另写怎样写 Validator 类型。

## 官方三件事

规范把 Methods 里不带 PubKey、是为了避免在 ABCI 上传送可能很大的后量子公钥 和「已经是省了字段就已经选型 interchangeable / 已经是提到后量子公钥就已经没有后量子钥 interchangeable / 已经是 ABCI 不传公钥就已经交差 interchangeable / 已经是 validator bundled interchangeable」分开写成三件独立的实现事，不是「看见省了字段就已经选型 interchangeable / 就已经没有后量子钥 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见省了字段 / 看见不带 PubKey 是为了不在 ABCI 上传大后量子公钥 / 看见省了 PubKey 字段 is not already 已经选型 interchangeable / 已经 algo interchangeable / 已经选型交差 interchangeable / 364 validator bundled interchangeable / 318 emptyset interchangeable / validator-sold-as-update interchangeable，也不是已经 Validator 类型 bundled（364） interchangeable / 840 valnopub-notalgo interchangeable / 364 validator item 2 interchangeable，也不是已经不带 PubKey 不是已经选型 not already algo / not already no-pq / not already settled 正式三事 bundled（364 item 2 余量） interchangeable / 364 validator item 2 interchangeable，也不是已经带了公钥（839） interchangeable / 841 valupdate-notset interchangeable / 35 valupdate interchangeable，也不是已经 InitChain 空名单就已经没有集合（318） interchangeable。**  
   官方写：不带 PubKey，是为了避免在 ABCI 上传送可能很大的后量子公钥。看见省了字段，不是已经选定算法。看见省了字段，不是已经 algo interchangeable——364 钉 bundled 三事，本页从 item 2 侧钉 not already algo 单句。看见不带 PubKey 是为了不在 ABCI 上传大后量子公钥，不是已经 Validator 类型 bundled（364） interchangeable——364 钉 bundled，本页钉 item 2 第一件事。看见省了字段，不是已经带了公钥（839） interchangeable——839 另钉 item 1。看见省了字段，不是已经 ValidatorUpdate 改了集合（841） interchangeable——841 另钉 item 3。364 validator-vs-update bundled unbundling 在本页 item 2 续。

2. **看见提到后量子公钥 / 看见可能很大的后量子公钥 / 看见提到后量子钥 is not already 已经没有后量子钥 interchangeable / 已经 no-pq interchangeable / 已经没有后量子钥交差 interchangeable / 364 validator bundled interchangeable / 318 emptyset interchangeable，也不是已经 Validator 类型 bundled（364） interchangeable / 840 valnopub-notalgo interchangeable / 364 validator item 1 address interchangeable / 364 validator item 3 更新 interchangeable，也不是已经不带 PubKey 不是已经选型 not already algo / not already no-pq / not already settled 正式三事 bundled（364 item 2 余量） interchangeable / 364 validator item 2 interchangeable，也不是已经选型（本页第一件事） interchangeable。**  
   官方写：看见提到后量子公钥，不是已经没有后量子钥。看见可能很大的后量子公钥，不是已经 no-pq interchangeable——本页钉 not already no-pq 单句。看见提到后量子钥，不是已经选型（本页第一件事） interchangeable——三件事分开钉。364 validator-vs-update bundled unbundling 在本页 item 2 续。

3. **看见 ABCI 不传公钥 / 看见 ABCI 上不传送公钥 / 看见不在 ABCI 上传公钥 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 364 validator bundled interchangeable / 33 fourgates interchangeable，也不是已经 Validator 类型 bundled（364） interchangeable / 840 valnopub-notalgo interchangeable / 364 validator item 1 / 364 validator item 3，也不是已经不带 PubKey 不是已经选型 not already algo / not already no-pq / not already settled 正式三事 bundled（364 item 2 余量） interchangeable / 364 validator item 2 interchangeable，也不是已经选型（本页第一件事） interchangeable / 已经没有后量子钥（本页第二件事） interchangeable。**  
   官方写：看见 ABCI 不传公钥，不是已经交差。看见 ABCI 上不传送公钥，不是已经 settled interchangeable——本页钉 not already settled 单句。看见不在 ABCI 上传公钥，不是已经没有后量子钥（本页第二件事） interchangeable——三件事分开钉。364 validator-vs-update bundled unbundling 在本页 item 2 续。

怎样编 `Validator`、怎样编 `ValidatorUpdate`、怎样在 ABCI 上传钥是规范里的做法，本页不抄。Validator 类型 bundled（364）、Validator 用 address 认人不是已经带了公钥（364 item 1 余量 / 839）、ValidatorUpdate 用公钥认人不是已经改了集合（364 item 3 余量 / 841）、H 的更新已经在 H+1 计票（35）、InitChain 空名单就已经没有集合（318）、必须回四列就已经改了集合（363）是另外那套，本页不抄。

## 官方为什么这样拆

- **省了字段 not already algo ≠ 364 / 318 interchangeable：** 官方把省了字段和已经选型分开。
- **提到后量子公钥 not already no-pq ≠ 已经没有后量子钥 interchangeable：** 官方把提到后量子公钥和已经没有后量子钥分开。
- **ABCI 不传公钥 not already settled ≠ 已经交差 interchangeable：** 官方把 ABCI 不传公钥和已经交差分开；364 validator-vs-update bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 省了字段 | 不是 already algo | 不是 InitChain 空名单就已经没有集合 alone（318） |
| 提到后量子公钥 | 不是 already no-pq | 不是有结构 already pubkey alone（839） |
| ABCI 不传公钥 | 不是 already settled | 不是 ValidatorUpdate already changed-set alone（841） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看不带 PubKey 不是已经选型 not already algo / not already no-pq / not already settled 正式三事（364 余量），必须分开省了字段 是不是 already algo interchangeable / 364 validator bundled interchangeable / validator-sold-as-update interchangeable、提到后量子公钥 是不是 already no-pq interchangeable、ABCI 不传公钥 是不是 already settled interchangeable。可以跳过「看见省了字段就已经选型 interchangeable / 就已经没有后量子钥 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Validator 类型。364 validator-vs-update bundled unbundling 在本页 item 2 续（839 + 840）。

## 本页不抄

- 怎样编 `Validator`、怎样编 `ValidatorUpdate`、怎样在 ABCI 上传钥。
- Validator 类型 bundled。那是不变量 364。
- Validator 用 address 认人不是已经带了公钥。那是不变量 364 item 1 余量 / 839。
- ValidatorUpdate 用公钥认人不是已经改了集合。那是不变量 364 item 3 余量 / 841。
- H 的更新已经在 H+1 计票。那是不变量 35。
- InitChain 空名单就已经没有集合。那是不变量 318。
- 必须回四列就已经改了集合。那是不变量 363。
