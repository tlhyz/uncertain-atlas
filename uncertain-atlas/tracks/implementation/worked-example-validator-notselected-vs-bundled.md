# 例：看见不带 PubKey is not already selected interchangeable / not already no PQ key interchangeable / not already settled interchangeable

**层次**：实现 / 不带 PubKey not already selected / not already no PQ key / not already settled 正式三事（364 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator / ValidatorUpdate。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「不带 PubKey not already selected / not already no PQ key / not already settled 正式三事（364 余量）/ not 834 validator-notselected interchangeable / not 364 validator-vs-update bundled interchangeable」，不是 Validator 类型 bundled（364），也不是 InitChain 空名单就已经没有集合（318），也不是 ConsensusParams.validator 就已经选型（385/774）。不要另写怎样写 Validator 类型。

## 官方三件事

1. **看见不带 PubKey 是为了不在 ABCI 上传大后量子公钥 / 看见省了字段 / 这份省字段 is not already 已经选型 interchangeable，也不是已经 Validator 类型 bundled（364） interchangeable / 834 validator-notselected interchangeable / 833 validator-notpubkey interchangeable / 364 validator item 1 address interchangeable，也不是已经不带 PubKey not already selected / not already no PQ key / not already settled 正式三事 bundled（364 item 2 余量） interchangeable / 364 validator item 2 interchangeable。**  
   官方写：不带 PubKey，是为了避免在 ABCI 上传送可能很大的后量子公钥。看见省了字段，不是已经选定算法 interchangeable——本页从 364 item 2 侧钉 not already selected 单句。364 validator vs update bundled unbundling 在本页 item 2 续。

2. **看见省了字段 / 看见提到后量子公钥 / 这份省字段 is not already 已经没有后量子钥 interchangeable，也不是已经 Validator 类型 bundled（364） interchangeable / 834 validator-notselected interchangeable / 364 validator item 3 ValidatorUpdate interchangeable / 835 validator-notchanged interchangeable，也不是已经 InitChain 空名单就已经没有集合 interchangeable / 318 initempty / 765 initparams-notnoset interchangeable。**  
   官方把提到后量子公钥和已经没有后量子钥分开——364 bundled 第二件事常与 318 混成「看见省了字段就已经选型或已经没有后量子钥 interchangeable」，本页钉 not already no PQ key 单句。

3. **看见省了字段 / 看见 ABCI 不传公钥 / 这份省字段 is not already 已经交差 interchangeable，也不是已经 Validator 类型 bundled（364） interchangeable / 834 validator-notselected interchangeable / 833 validator-notpubkey interchangeable，也不是已经 ConsensusParams.validator 就已经选型 interchangeable / 385 paramsblock / 774 paramsblock-notpubkey interchangeable。**  
   官方把 ABCI 不传公钥和已经交差分开。看见 ABCI 不传公钥，不是已经交差 interchangeable。364 validator vs update bundled unbundling 在本页 item 2 续。

怎样编 Validator、怎样编 ValidatorUpdate、怎样在 ABCI 上传钥是规范里的做法，本页不抄。

## 官方为什么这样拆

- **不带 PubKey not already selected ≠ 已经选型 interchangeable：** 官方把省字段和已经选定算法分开。
- **看见提到后量子公钥 not already no PQ key ≠ 已经没有后量子钥 interchangeable：** 官方把提到后量子公钥和已经没有后量子钥分开。
- **看见 ABCI 不传公钥 not already settled ≠ 已经交差 interchangeable：** 官方把 ABCI 不传公钥和已经交差分开；364 validator vs update bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 不带 PubKey | 不是已经选型 | 不是 address 认人（833/364 item 1） |
| 看见提到后量子公钥 | 不是已经没有后量子钥 | 不是 InitChain 空名单（318） |
| 看见 ABCI 不传公钥 | 不是已经交差 | 不是 ConsensusParams.validator（385/774） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看不带 PubKey not already selected / not already no PQ key / not already settled 正式三事（364 余量），必须分开是不是已经选型、是不是已经没有后量子钥、是不是已经交差。可以跳过「看见省了字段就已经选型」。不要另写怎样写 Validator 类型。364 validator vs update bundled unbundling 在本页 item 2 续；续 [`worked-example-validator-notchanged-vs-bundled.md`](worked-example-validator-notchanged-vs-bundled.md)（不变量 835 item 3）。

## 本页不抄

- 怎样编 Validator、怎样编 ValidatorUpdate、怎样在 ABCI 上传钥。
- Validator 类型 bundled。那是不变量 364。
- Validator 用 address 认人。那是不变量 364 item 1 余量 / 833。
- InitChain 空名单就已经没有集合。那是不变量 318。
- ConsensusParams.validator 就已经选型。那是不变量 385 / 774。
