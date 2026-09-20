# 例：看见填了证据 MaxBytes / 看见一块里证据有上限 / 看见取值有顶 is not already already under-block interchangeable / already overhead-deducted interchangeable / already fits-budget interchangeable

**层次**：实现 / 填了证据 MaxBytes 不是已经落在块上限下面 not already under-block / not already overhead-deducted / not already fits-budget 正式三事（331 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / EvidenceParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「填了证据 MaxBytes 不是已经落在块上限下面 not already under-block / not already overhead-deducted / not already fits-budget 正式三事（331 余量）/ not 749 evidencemaxbytes-notunder interchangeable / not 331 evidencemaxbytes bundled interchangeable」，不是 EvidenceParams.MaxBytes bundled（331），也不是 > 0 不是已经盖住解绑（750 item 2 余量）或证据 MaxBytes 不是已经是块 MaxBytes（751 item 3 余量）。不要另写怎样设 EvidenceParams.MaxBytes 或怎样算块开销。

## 官方三件事

规范把 Requirements 里单块证据总字节上限应当落在块最大字节下面、不得超过一块减去开销之后的体积 和「已经是填了证据 MaxBytes 就已经落在块上限下面 interchangeable / 已经是有上限就已经扣掉开销 interchangeable / 已经是取值有顶就已经装得下预算 interchangeable / 已经是 evidencemaxbytes bundled interchangeable」分开写成三件独立的实现事，不是「看见填了证据 MaxBytes 就已经落在块上限下面 interchangeable / 就已经扣掉开销 interchangeable / 就已经装得下预算 interchangeable」一件事：

1. **看见填了证据 MaxBytes / 看见填了这个字段 / 看见 EvidenceParams.MaxBytes 有值 is not already 已经落在块上限下面 interchangeable / 已经 under-block interchangeable / 已经落在下面交差 interchangeable / 331 evidencemaxbytes bundled interchangeable / 33 four gates interchangeable / evidencemaxbytes-sold-as-blockmax interchangeable，也不是已经 EvidenceParams.MaxBytes bundled（331） interchangeable / 749 evidencemaxbytes-notunder interchangeable / 331 evidencemaxbytes item 1 interchangeable，也不是已经填了证据 MaxBytes 不是已经落在块上限下面 not already under-block / not already overhead-deducted / not already fits-budget 正式三事 bundled（331 item 1 余量） interchangeable / 331 evidencemaxbytes item 1 interchangeable，也不是已经 > 0 不是已经盖住解绑（750） interchangeable / 751 evidencemaxbytes-notblockmax interchangeable / 299 evidence-full interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：这是**单块能交差的证据总字节**上限；它**应当**舒服地落在块最大字节下面。看见填了证据 MaxBytes，不是已经 under-block interchangeable——331 钉 bundled 三事，本页从 item 1 侧钉 not already under-block 单句。看见填了这个字段，不是已经 EvidenceParams.MaxBytes bundled（331） interchangeable——331 钉 bundled，本页钉 item 1 第一件事。看见 EvidenceParams.MaxBytes 有值，不是已经先装证据已经装满交易（299） interchangeable——299 另钉。331 evidencemaxbytes vs block bundled unbundling 在本页 item 1 启动。

2. **看见一块里证据有上限 / 看见有上限 / 看见证据体积有顶 is not already 已经扣掉开销 interchangeable / 已经 overhead-deducted interchangeable / 已经扣开销交差 interchangeable / 331 evidencemaxbytes bundled interchangeable / 63 maxbytes-sla interchangeable，也不是已经 EvidenceParams.MaxBytes bundled（331） interchangeable / 749 evidencemaxbytes-notunder interchangeable / 331 evidencemaxbytes item 2 解绑 interchangeable / 331 evidencemaxbytes item 3 块 MaxBytes interchangeable，也不是已经填了证据 MaxBytes 不是已经落在块上限下面 not already under-block / not already overhead-deducted / not already fits-budget 正式三事 bundled（331 item 1 余量） interchangeable / 331 evidencemaxbytes item 1 interchangeable，也不是已经落在块上限下面（本页第一件事） interchangeable。**  
   官方写：看见有上限，不是已经扣掉开销。看见一块里证据有上限，不是已经 overhead-deducted interchangeable——本页钉 not already overhead-deducted 单句。看见有上限，不是已经仓库默认块 MaxBytes 已经是活性 SLA（63） interchangeable——63 另钉。看见证据体积有顶，不是已经落在块上限下面（本页第一件事） interchangeable——三件事分开钉。331 evidencemaxbytes vs block bundled unbundling 在本页 item 1 启动。

3. **看见取值有顶 / 看见不得超过一块减去开销 / 看见约 BlockParams.MaxBytes 那条 is not already 已经装得下预算 interchangeable / 已经 fits-budget interchangeable / 已经装得下交差 interchangeable / 331 evidencemaxbytes bundled interchangeable / 299 evidence-full interchangeable，也不是已经 EvidenceParams.MaxBytes bundled（331） interchangeable / 749 evidencemaxbytes-notunder interchangeable / 331 evidencemaxbytes item 2 / 331 evidencemaxbytes item 3，也不是已经填了证据 MaxBytes 不是已经落在块上限下面 not already under-block / not already overhead-deducted / not already fits-budget 正式三事 bundled（331 item 1 余量） interchangeable / 331 evidencemaxbytes item 1 interchangeable，也不是已经落在块上限下面（本页第一件事） interchangeable / 已经扣掉开销（本页第二件事） interchangeable。**  
   官方写：取值**不得超过**一块减去开销之后的体积（约 `BlockParams.MaxBytes`）。看见取值有顶，不是已经 fits-budget interchangeable——本页钉 not already fits-budget 单句。看见不得超过一块减去开销，不是已经先装证据已经装满交易（299） interchangeable——299 另钉。看见约 BlockParams.MaxBytes 那条，不是已经扣掉开销（本页第二件事） interchangeable——三件事分开钉。331 evidencemaxbytes vs block bundled unbundling 在本页 item 1 完成。

怎样设 `EvidenceParams.MaxBytes`、默认取值、怎样算块开销是规范里的取值或做法，本页不抄。EvidenceParams.MaxBytes bundled（331）、> 0 不是已经盖住解绑（331 item 2 余量 / 750）、证据 MaxBytes 不是已经是块 MaxBytes（331 item 3 余量 / 751）、先装证据已经装满交易（299）、仓库默认块 MaxBytes 已经是活性 SLA（63）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **填了证据 MaxBytes not already under-block ≠ 331 / 33 interchangeable：** 官方把填了字段和已经落在块上限下面分开。
- **有上限 not already overhead-deducted ≠ 已经扣掉开销 interchangeable：** 官方把有上限和已经扣掉开销分开。
- **取值有顶 not already fits-budget ≠ 已经装得下预算 interchangeable：** 官方把不得超过减去开销之后的体积和已经装得下分开；331 evidencemaxbytes vs block bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 填了证据 MaxBytes | 不是 already under-block | 不是先装证据 alone（299） |
| 有上限 | 不是 already overhead-deducted | 不是块 MaxBytes SLA alone（63） |
| 取值有顶 | 不是 already fits-budget | 不是写成 -1 无上限 alone（299） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了证据 MaxBytes 不是已经落在块上限下面 not already under-block / not already overhead-deducted / not already fits-budget 正式三事（331 余量），必须分开填了证据 MaxBytes 是不是 already under-block interchangeable / 331 evidencemaxbytes bundled interchangeable / evidencemaxbytes-sold-as-blockmax interchangeable、有上限 是不是 already overhead-deducted interchangeable、取值有顶 是不是 already fits-budget interchangeable。可以跳过「看见填了证据 MaxBytes 就已经落在块上限下面 interchangeable / 就已经扣掉开销 interchangeable / 就已经装得下预算 interchangeable」。不要另写怎样设 EvidenceParams.MaxBytes。331 evidencemaxbytes vs block bundled unbundling 在本页 item 1 启动；续 [`worked-example-evidencemaxbytes-notunbonding-vs-bundled.md`](worked-example-evidencemaxbytes-notunbonding-vs-bundled.md)（不变量 750 item 2）。

## 本页不抄

- 怎样设 `EvidenceParams.MaxBytes`、默认取值、怎样算块开销。
- EvidenceParams.MaxBytes bundled。那是不变量 331。
- > 0 不是已经盖住解绑。那是不变量 331 item 2 余量 / 750。
- 证据 MaxBytes 不是已经是块 MaxBytes。那是不变量 331 item 3 余量 / 751。
- 先装证据已经装满交易、写成 -1 已经没有上限。那是不变量 299。
- 仓库默认块 MaxBytes 已经是活性 SLA。那是不变量 63。
- 四门已经结算。那是不变量 33。
