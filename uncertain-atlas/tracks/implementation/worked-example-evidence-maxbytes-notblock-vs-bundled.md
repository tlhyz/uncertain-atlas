# 例：看见证据 MaxBytes is not already block MaxBytes interchangeable / not already unlimited-minus-one interchangeable / not already settled interchangeable

**层次**：实现 / 证据 MaxBytes not already block MaxBytes / not already unlimited-minus-one / not already settled 正式三事（331 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / EvidenceParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、mempool。本页是「证据 MaxBytes not already block MaxBytes / not already unlimited-minus-one / not already settled 正式三事（331 余量）/ not 922 evidence-maxbytes-notblock interchangeable / not 331 evidence-maxbytes-vs-block bundled interchangeable」，不是证据尺 bundled（331），也不是仓库默认块 MaxBytes 已经是活性 SLA（63），也不是合法范围就已经是默认 21 MB（337/919）。不要另写怎样设 EvidenceParams.MaxBytes 或怎样算块开销。

## 官方三件事

1. **看见证据 MaxBytes / 看见证据这边有 MaxBytes 这份尺 is not already 已经是块 MaxBytes interchangeable，也不是已经证据尺 bundled（331） interchangeable / 922 evidence-maxbytes-notblock interchangeable / 920 evidence-maxbytes-notunder interchangeable / 331 evidence-maxbytes item 1 填了字段 interchangeable，也不是已经证据 MaxBytes not already block MaxBytes / not already unlimited-minus-one / not already settled 正式三事 bundled（331 item 3 余量） interchangeable / 331 evidence-maxbytes item 3 interchangeable。**  
   官方把证据体积上限和块 MaxBytes 写成两把尺。看见证据这边有 MaxBytes，不是已经是块上限 interchangeable——本页从 331 item 3 侧钉 not already block MaxBytes 单句。331 evidence-maxbytes vs block bundled unbundling 在本页 item 3 完成。

2. **看见填了数 / 看见有上限 / 这份尺 is not already 已经是写成 -1 的那条 interchangeable，也不是已经证据尺 bundled（331） interchangeable / 922 evidence-maxbytes-notblock interchangeable / 331 evidence-maxbytes item 2 > 0 interchangeable / 921 evidence-maxbytes-notunbond interchangeable，也不是已经 -1 就已经没有块上限 interchangeable / 337/917 maxbytes-cap-notunlim interchangeable。**  
   官方把填了数和已经是写成 -1 的那条分开——331 bundled 第三件事常与 337 混成「看见证据 MaxBytes 就已经是块上限或已经是 -1 无上限 interchangeable」，本页钉 not already unlimited-minus-one 单句。

3. **看见有上限 / 看见证据这边有 MaxBytes / 这份尺 is not already 已经交差 interchangeable，也不是已经证据尺 bundled（331） interchangeable / 922 evidence-maxbytes-notblock interchangeable / 920 evidence-maxbytes-notunder interchangeable，也不是已经仓库默认块 MaxBytes 已经是活性 SLA interchangeable / 63 maxbytes-sla interchangeable。**  
   官方把有上限和已经对照过第一轮超时 / 已经交差分开。看见有上限，不是已经交差 interchangeable。331 evidence-maxbytes vs block bundled unbundling 在本页 item 3 完成。

怎样设 EvidenceParams.MaxBytes、默认取值、怎样算块开销是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **证据 MaxBytes not already block MaxBytes ≠ 已经是块 MaxBytes interchangeable：** 官方把单块证据体积和整块上限写成两把尺。
- **看见填了数 not already unlimited-minus-one ≠ 已经是写成 -1 的那条 interchangeable：** 官方把证据这边填了数和块 MaxBytes 写成 -1 分开。
- **看见有上限 not already settled ≠ 已经交差 interchangeable：** 官方把有上限和已经对照过第一轮超时 / 已经交差分开；331 evidence-maxbytes vs block bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 证据 MaxBytes | 不是已经是块 MaxBytes | 不是仓库默认块 MaxBytes 已经是活性 SLA（63） |
| 看见填了数 | 不是已经是写成 -1 的那条 | 不是合法范围就已经是默认 21 MB（337/919） |
| 看见有上限 | 不是已经交差 | 不是填了字段就已经落在块上限下面（920） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看证据 MaxBytes not already block MaxBytes / not already unlimited-minus-one / not already settled 正式三事（331 余量），必须分开是不是已经是块 MaxBytes、是不是已经是写成 -1 的那条、是不是已经交差。可以跳过「看见证据这边有 MaxBytes 就已经是块上限」。不要另写怎样设 EvidenceParams.MaxBytes 或怎样算块开销。331 evidence-maxbytes vs block bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样设 EvidenceParams.MaxBytes、默认取值、怎样算块开销。
- 证据尺 bundled。那是不变量 331。
- 填了字段就已经落在块上限下面。那是不变量 331 item 1 余量 / 920。
- 仓库默认块 MaxBytes 已经是活性 SLA。那是不变量 63。
- 合法范围就已经是默认 21 MB。那是不变量 337/919。
