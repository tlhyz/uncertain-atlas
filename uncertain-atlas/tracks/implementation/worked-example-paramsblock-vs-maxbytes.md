# 例：看见 ConsensusParams.block 限制块大小和块间隔不是已经是 MaxBytes 上限；看见 ConsensusParams.validator 限制验证者公钥类型不是已经带了公钥；看见 ConsensusParams.version 是 ABCI 应用版本不是已经是 app_version 进了头

**层次**：实现 / ConsensusParams 字段。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ConsensusParams。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「ConsensusParams.block 限制块大小和块间隔不是已经是 MaxBytes 上限 / ConsensusParams.validator 限制验证者公钥类型不是已经带了公钥 / ConsensusParams.version 是 ABCI 应用版本不是已经是 app_version 进了头」，不是 -1 就按 100 MB 验就已经没有上限，也不是 Validator 用 address 认人就已经带了公钥。不要另写怎样写 ConsensusParams 字段。

## 官方三件事

规范把 `block` 限制块大小和块间隔、`validator` 限制验证者公钥类型、`version` 是 ABCI 应用版本写成三件独立的实现事，不是「看见填了 ConsensusParams 就已经是 MaxBytes 上限、已经带了公钥、已经是 app_version 进了头」一件事：

1. **看见 ConsensusParams.`block` 限制块大小和块间隔 / 看见填了 block 不是已经是 MaxBytes 上限，也不是已经是 next_block_delay。**  
   官方写：`block` 限制一块的大小和两块之间的时间。看见填了 block，不是已经是 MaxBytes 写成 -1 那种上限。看见能卡间隔，不是已经是应用回的 `next_block_delay`。看见有字段，不是已经交差。
2. **看见 ConsensusParams.`validator` 限制验证者公钥类型 / 看见填了 validator 不是已经带了公钥，也不是已经选型。**  
   官方写：`validator` 限制验证者能用的公钥类型。看见填了 validator，不是已经带了公钥。看见限了类型，不是已经选型。看见能填，不是已经改了集合。
3. **看见 ConsensusParams.`version` 是 ABCI 应用版本 / 看见填了 version 不是已经是 app_version 进了头，也不是已经印进本头 AppHash。**  
   官方写：`version` 是 ABCI 应用版本。看见填了 version，不是已经是 Info 回包 `app_version` 进了每块头。看见有应用版本，不是已经印进本头 AppHash。看见能回，不是已经是握手对齐。

怎样写 ConsensusParams、怎样选 MaxBytes、怎样限钥型是规范里的做法，本页不抄。-1 就按 100 MB 验就已经没有上限是不变量 337，本页不抄。

## 官方为什么这样拆

- **ConsensusParams.block 限制块大小和块间隔 ≠ 已经是 MaxBytes 上限：** 官方把这一栏和 MaxBytes 写成 -1 那种上限分开。
- **ConsensusParams.validator 限制验证者公钥类型 ≠ 已经带了公钥：** 官方把限钥型和已经带了公钥分开。
- **ConsensusParams.version 是 ABCI 应用版本 ≠ 已经是 app_version 进了头：** 官方把这一栏和 Info 回的 app_version 进头分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ConsensusParams.block 限制块大小和块间隔 | 不是已经是 MaxBytes 上限 | 不是 -1 就按 100 MB 验就已经没有上限（337） |
| ConsensusParams.validator 限制验证者公钥类型 | 不是已经带了公钥 | 不是 Validator 用 address 认人就已经带了公钥（364） |
| ConsensusParams.version 是 ABCI 应用版本 | 不是已经是 app_version 进了头 | 不是 app_version 进每块头就已经印进本头 AppHash（370） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ConsensusParams 就已经是 MaxBytes 上限、已经带了公钥、已经是 app_version 进了头」，必须分开 ConsensusParams.block 限制块大小和块间隔是不是已经是 MaxBytes 上限、ConsensusParams.validator 限制验证者公钥类型是不是已经带了公钥、ConsensusParams.version 是 ABCI 应用版本是不是已经是 app_version 进了头。可以跳过「看见填了 ConsensusParams 就已经是 MaxBytes 上限」。不要另写怎样写 ConsensusParams 字段。385 paramsblock vs maxbytes bundled unbundling 完成（773 item 1 / 774 item 2 / 775 item 3）；精读 [`worked-example-paramsblock-notmaxbytes-vs-bundled.md`](worked-example-paramsblock-notmaxbytes-vs-bundled.md)（不变量 773 item 1）。

## 本页不抄

- 怎样写 ConsensusParams、怎样选 MaxBytes、怎样限钥型。
- -1 就按 100 MB 验就已经没有上限。那是不变量 337。
- Validator 用 address 认人就已经带了公钥。那是不变量 364。
- app_version 进每块头就已经印进本头 AppHash。那是不变量 370。
