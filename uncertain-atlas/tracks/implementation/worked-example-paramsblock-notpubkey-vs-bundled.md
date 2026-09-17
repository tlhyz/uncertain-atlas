# 例：看见 ConsensusParams.validator 限制验证者公钥类型 is not already has pubkey interchangeable / not already selected type interchangeable / not already settled interchangeable

**层次**：实现 / ConsensusParams.validator not already has pubkey / not already selected type / not already settled 正式三事（385 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ConsensusParams。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ConsensusParams.validator not already has pubkey / not already selected type / not already settled 正式三事（385 余量）/ not 774 paramsblock-notpubkey interchangeable / not 385 paramsblock-vs-maxbytes bundled interchangeable」，不是 ConsensusParams 字段 bundled（385），也不是 Validator 用 address 认人就已经带了公钥（364）。不要另写怎样写 ConsensusParams 字段。

## 官方三件事

1. **看见 ConsensusParams.`validator` 限制验证者公钥类型 / 看见填了 validator / ConsensusParams 这份钥型栏 is not already 已经带了公钥 interchangeable / 364 addrkey interchangeable，也不是已经 ConsensusParams 字段 bundled（385） interchangeable / 774 paramsblock-notpubkey interchangeable / 773 paramsblock-notmaxbytes interchangeable / 385 paramsblock item 1 block interchangeable，也不是已经 validator not already has pubkey / not already selected type / not already settled 正式三事 bundled（385 item 2 余量） interchangeable / 385 paramsblock item 2 interchangeable。**  
   官方写：`validator` 限制验证者能用的公钥类型。看见填了 validator，不是已经带了公钥 interchangeable——本页从 385 item 2 侧钉 not already has pubkey 单句。385 paramsblock vs maxbytes bundled unbundling 在本页 item 2 续。

2. **看见填了 validator / 看见限了类型 / ConsensusParams 这份钥型栏 is not already 已经选型 interchangeable / 364 addrkey interchangeable，也不是已经 ConsensusParams 字段 bundled（385） interchangeable / 774 paramsblock-notpubkey interchangeable / 385 paramsblock item 3 version interchangeable / 775 paramsblock-notappver interchangeable。**  
   官方把限钥型和已经选型分开——385 bundled 第二件事常与 364 混成「看见填了 validator 就已经带了公钥或已经选型 interchangeable」，本页钉 not already selected type 单句。

3. **看见填了 validator / 看见能填 / ConsensusParams 这份钥型栏 is not already 已经改了集合 interchangeable，也不是已经 ConsensusParams 字段 bundled（385） interchangeable / 774 paramsblock-notpubkey interchangeable / 773 paramsblock-notmaxbytes interchangeable。**  
   官方把能填 ConsensusParams.validator 和已经改了集合分开。看见能填，不是已经改了集合 interchangeable。385 paramsblock vs maxbytes bundled unbundling 在本页 item 2 续。

怎样写 ConsensusParams、怎样选 MaxBytes、怎样限钥型是规范里的做法，本页不抄。

## 官方为什么这样拆

- **validator not already has pubkey ≠ 364 interchangeable：** 官方把限钥型和已经带了公钥分开。
- **validator not already selected type ≠ 364 interchangeable：** 官方把限了类型和已经选型分开。
- **validator not already settled ≠ 已经改了集合 interchangeable：** 官方把能填 validator 和已经改了集合分开；385 paramsblock vs maxbytes bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ConsensusParams.validator 限制验证者公钥类型 | 不是已经带了公钥（364） | 不是 ConsensusParams.block（773/385 item 1） |
| 看见填了 validator | 不是已经选型（364） | 不是 ConsensusParams 字段 bundled（385） |
| 看见能填 | 不是已经改了集合 | 不是 ConsensusParams.version（775/385 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ConsensusParams.validator not already has pubkey / not already selected type / not already settled 正式三事（385 余量），必须分开 validator 是不是已经带了公钥 interchangeable / 364、是不是已经选型、是不是已经改了集合。可以跳过「看见填了 validator 就已经带了公钥」。不要另写怎样写 ConsensusParams 字段。385 paramsblock vs maxbytes bundled unbundling 在本页 item 2 续；完成 [`worked-example-paramsblock-notappver-vs-bundled.md`](worked-example-paramsblock-notappver-vs-bundled.md)（不变量 775 item 3）。

## 本页不抄

- 怎样写 ConsensusParams、怎样选 MaxBytes、怎样限钥型。
- ConsensusParams 字段 bundled。那是不变量 385。
- ConsensusParams.block。那是不变量 385 item 1 余量 / 773。
- ConsensusParams.version。那是不变量 385 item 3 余量 / 775。
- Validator 用 address 认人就已经带了公钥。那是不变量 364。
