# 例：看见证据 MaxBytes / 看见填了数 / 看见有上限 is not already already block-maxbytes interchangeable / already minus-one interchangeable / already propose-sla interchangeable

**层次**：实现 / 证据 MaxBytes 不是已经是块 MaxBytes not already block-maxbytes / not already minus-one / not already propose-sla 正式三事（331 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / EvidenceParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「证据 MaxBytes 不是已经是块 MaxBytes not already block-maxbytes / not already minus-one / not already propose-sla 正式三事（331 余量）/ not 751 evidencemaxbytes-notblockmax interchangeable / not 331 evidencemaxbytes bundled interchangeable」，不是 EvidenceParams.MaxBytes bundled（331），也不是填了证据 MaxBytes 不是已经落在块上限下面（749 item 1 余量）或 > 0 不是已经盖住解绑（750 item 2 余量）。不要另写怎样设 EvidenceParams.MaxBytes 或怎样算块开销。

## 官方三件事

规范把 Requirements 里证据体积上限和块 MaxBytes 两把尺、填了数不等于 -1 无上限、有上限不等于活性 SLA 和「已经是证据 MaxBytes 就已经是块 MaxBytes interchangeable / 已经是填了数就已经是 -1 无上限 interchangeable / 已经是有上限就已经是活性 SLA interchangeable / 已经是 evidencemaxbytes bundled interchangeable」分开写成三件独立的实现事，不是「看见证据 MaxBytes 就已经是块 MaxBytes interchangeable / 就已经是 -1 无上限 interchangeable / 就已经是活性 SLA interchangeable」一件事：

1. **看见证据 MaxBytes / 看见证据这边有 MaxBytes / 看见证据体积上限 is not already 已经是块 MaxBytes interchangeable / 已经 block-maxbytes interchangeable / 已经块上限交差 interchangeable / 331 evidencemaxbytes bundled interchangeable / 33 four gates interchangeable / evidencemaxbytes-sold-as-blockmax interchangeable，也不是已经 EvidenceParams.MaxBytes bundled（331） interchangeable / 751 evidencemaxbytes-notblockmax interchangeable / 331 evidencemaxbytes item 3 interchangeable，也不是已经证据 MaxBytes 不是已经是块 MaxBytes not already block-maxbytes / not already minus-one / not already propose-sla 正式三事 bundled（331 item 3 余量） interchangeable / 331 evidencemaxbytes item 3 interchangeable，也不是已经填了证据 MaxBytes 不是已经落在块上限下面（749） interchangeable / 750 evidencemaxbytes-notunbonding interchangeable / 63 maxbytes-sla interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方把证据体积上限和块 `MaxBytes` 写成两把尺。看见证据这边有 MaxBytes，不是已经是块上限。看见证据 MaxBytes，不是已经 block-maxbytes interchangeable——331 钉 bundled 三事，本页从 item 3 侧钉 not already block-maxbytes 单句。看见证据体积上限，不是已经 EvidenceParams.MaxBytes bundled（331） interchangeable——331 钉 bundled，本页钉 item 3 第一件事。看见证据这边有 MaxBytes，不是已经 > 0 不是已经盖住解绑（750） interchangeable——750 另钉 item 2。331 evidencemaxbytes vs block bundled unbundling 在本页 item 3 完成。

2. **看见填了数 / 看见写成数 / 看见不是空白 is not already 已经是 -1 无上限 interchangeable / 已经 minus-one interchangeable / 已经无上限交差 interchangeable / 331 evidencemaxbytes bundled interchangeable / 299 evidence-full interchangeable，也不是已经 EvidenceParams.MaxBytes bundled（331） interchangeable / 751 evidencemaxbytes-notblockmax interchangeable / 331 evidencemaxbytes item 1 落在块上限 interchangeable / 331 evidencemaxbytes item 2 解绑 interchangeable，也不是已经证据 MaxBytes 不是已经是块 MaxBytes not already block-maxbytes / not already minus-one / not already propose-sla 正式三事 bundled（331 item 3 余量） interchangeable / 331 evidencemaxbytes item 3 interchangeable，也不是已经是块 MaxBytes（本页第一件事） interchangeable。**  
   官方写：看见填了数，不是已经是写成 -1 的那条。看见填了数，不是已经 minus-one interchangeable——本页钉 not already minus-one 单句。看见写成数，不是已经写成 -1 已经没有上限（299） interchangeable——299 另钉。看见不是空白，不是已经是块 MaxBytes（本页第一件事） interchangeable——三件事分开钉。331 evidencemaxbytes vs block bundled unbundling 在本页 item 3 完成。

3. **看见有上限 / 看见对照第一轮超时 / 看见活性相关上限 is not already 已经是活性 SLA interchangeable / 已经 propose-sla interchangeable / 已经活性 SLA 交差 interchangeable / 331 evidencemaxbytes bundled interchangeable / 63 maxbytes-sla interchangeable，也不是已经 EvidenceParams.MaxBytes bundled（331） interchangeable / 751 evidencemaxbytes-notblockmax interchangeable / 331 evidencemaxbytes item 1 / 331 evidencemaxbytes item 2，也不是已经证据 MaxBytes 不是已经是块 MaxBytes not already block-maxbytes / not already minus-one / not already propose-sla 正式三事 bundled（331 item 3 余量） interchangeable / 331 evidencemaxbytes item 3 interchangeable，也不是已经是块 MaxBytes（本页第一件事） interchangeable / 已经是 -1 无上限（本页第二件事） interchangeable。**  
   官方写：看见有上限，不是已经对照过第一轮超时。看见有上限，不是已经 propose-sla interchangeable——本页钉 not already propose-sla 单句。看见对照第一轮超时，不是已经仓库默认块 MaxBytes 已经是活性 SLA（63） interchangeable——63 另钉。看见活性相关上限，不是已经是 -1 无上限（本页第二件事） interchangeable——三件事分开钉。331 evidencemaxbytes vs block bundled unbundling 在本页 item 3 完成。

怎样设 `EvidenceParams.MaxBytes`、默认取值、怎样算块开销是规范里的取值或做法，本页不抄。EvidenceParams.MaxBytes bundled（331）、填了证据 MaxBytes 不是已经落在块上限下面（331 item 1 余量 / 749）、> 0 不是已经盖住解绑（331 item 2 余量 / 750）、先装证据 / 写成 -1（299）、仓库默认块 MaxBytes 已经是活性 SLA（63）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **证据 MaxBytes not already block-maxbytes ≠ 331 / 33 interchangeable：** 官方把证据体积尺和块 MaxBytes 两把尺分开。
- **填了数 not already minus-one ≠ 已经是 -1 无上限 interchangeable：** 官方把填了数和写成 -1 那条分开。
- **有上限 not already propose-sla ≠ 已经是活性 SLA interchangeable：** 官方把有上限和已经对照第一轮超时分开；331 evidencemaxbytes vs block bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 证据 MaxBytes | 不是 already block-maxbytes | 不是盖住解绑 alone（750） |
| 填了数 | 不是 already minus-one | 不是写成 -1 无上限 alone（299） |
| 有上限 | 不是 already propose-sla | 不是块 MaxBytes SLA alone（63） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看证据 MaxBytes 不是已经是块 MaxBytes not already block-maxbytes / not already minus-one / not already propose-sla 正式三事（331 余量），必须分开证据 MaxBytes 是不是 already block-maxbytes interchangeable / 331 evidencemaxbytes bundled interchangeable / evidencemaxbytes-sold-as-blockmax interchangeable、填了数 是不是 already minus-one interchangeable、有上限 是不是 already propose-sla interchangeable。可以跳过「看见证据 MaxBytes 就已经是块 MaxBytes interchangeable / 就已经是 -1 无上限 interchangeable / 就已经是活性 SLA interchangeable」。不要另写怎样设 EvidenceParams.MaxBytes。331 evidencemaxbytes vs block bundled unbundling 在本页 item 3 完成（749 + 750 + 751）。

## 本页不抄

- 怎样设 `EvidenceParams.MaxBytes`、默认取值、怎样算块开销。
- EvidenceParams.MaxBytes bundled。那是不变量 331。
- 填了证据 MaxBytes 不是已经落在块上限下面。那是不变量 331 item 1 余量 / 749。
- > 0 不是已经盖住解绑。那是不变量 331 item 2 余量 / 750。
- 先装证据已经装满交易、写成 -1 已经没有上限。那是不变量 299。
- 仓库默认块 MaxBytes 已经是活性 SLA。那是不变量 63。
- 四门已经结算。那是不变量 33。
