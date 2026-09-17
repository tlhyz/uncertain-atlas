# 例：看见 MaxBytes > 0 is not already covering unbonding interchangeable / not already enough to punish interchangeable / not already settled interchangeable

**层次**：实现 / MaxBytes > 0 not already covering unbonding / not already enough to punish / not already settled 正式三事（331 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / EvidenceParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、mempool。本页是「MaxBytes > 0 not already covering unbonding / not already enough to punish / not already settled 正式三事（331 余量）/ not 921 evidence-maxbytes-notunbond interchangeable / not 331 evidence-maxbytes-vs-block bundled interchangeable」，不是证据尺 bundled（331），也不是默认证据窗已经够罚（46），也不是仓库默认块 MaxBytes 已经是活性 SLA（63）。不要另写怎样设 EvidenceParams.MaxBytes 或怎样算块开销。

## 官方三件事

1. **看见 MaxBytes > 0 / 看见合法 这份下限 is not already 已经盖住解绑 interchangeable，也不是已经证据尺 bundled（331） interchangeable / 921 evidence-maxbytes-notunbond interchangeable / 920 evidence-maxbytes-notunder interchangeable / 331 evidence-maxbytes item 1 填了字段 interchangeable，也不是已经 MaxBytes > 0 not already covering unbonding / not already enough to punish / not already settled 正式三事 bundled（331 item 2 余量） interchangeable / 331 evidence-maxbytes item 2 interchangeable。**  
   官方写：必须 MaxBytes > 0。看见大于 0，不是已经盖住解绑期 interchangeable——本页从 331 item 2 侧钉 not already covering unbonding 单句。331 evidence-maxbytes vs block bundled unbundling 在本页 item 2 续。

2. **看见合法 / 看见大于 0 / 这份下限 is not already 已经够罚 interchangeable，也不是已经证据尺 bundled（331） interchangeable / 921 evidence-maxbytes-notunbond interchangeable / 331 evidence-maxbytes item 3 两把尺 interchangeable / 922 evidence-maxbytes-notblock interchangeable，也不是已经默认证据窗已经够罚 interchangeable / 46 evidence-window interchangeable。**  
   官方把合法下限和已经能罚到人走之前分开——331 bundled 第二件事常与 46 混成「看见 > 0 就已经盖住解绑或已经够罚 interchangeable」，本页钉 not already enough to punish 单句。

3. **看见大于 0 / 看见合法 / 这份下限 is not already 已经交差 interchangeable，也不是已经证据尺 bundled（331） interchangeable / 921 evidence-maxbytes-notunbond interchangeable / 920 evidence-maxbytes-notunder interchangeable，也不是已经仓库默认块 MaxBytes 已经是活性 SLA interchangeable / 63 maxbytes-sla interchangeable。**  
   官方把合法和已经交差分开。看见合法，不是已经交差 interchangeable。331 evidence-maxbytes vs block bundled unbundling 在本页 item 2 续。

怎样设 EvidenceParams.MaxBytes、默认取值、怎样算块开销是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **MaxBytes > 0 not already covering unbonding ≠ 已经盖住解绑 interchangeable：** 官方把合法下限和证据窗 / 解绑盖住分开。
- **看见合法 not already enough to punish ≠ 已经够罚 interchangeable：** 官方把合法下限和已经能罚到人走之前分开。
- **看见大于 0 not already settled ≠ 已经交差 interchangeable：** 官方把大于 0 和已经交差分开；331 evidence-maxbytes vs block bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| > 0 | 不是已经盖住解绑 | 不是默认证据窗已经够罚（46） |
| 看见合法 | 不是已经够罚 | 不是仓库默认块 MaxBytes 已经是活性 SLA（63） |
| 看见大于 0 | 不是已经交差 | 不是填了字段就已经落在块上限下面（920） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MaxBytes > 0 not already covering unbonding / not already enough to punish / not already settled 正式三事（331 余量），必须分开是不是已经盖住解绑、是不是已经够罚、是不是已经交差。可以跳过「看见 > 0 就已经盖住解绑」。不要另写怎样设 EvidenceParams.MaxBytes 或怎样算块开销。331 evidence-maxbytes vs block bundled unbundling 在本页 item 2 续；续 [`worked-example-evidence-maxbytes-notblock-vs-bundled.md`](worked-example-evidence-maxbytes-notblock-vs-bundled.md)（不变量 922 item 3）。

## 本页不抄

- 怎样设 EvidenceParams.MaxBytes、默认取值、怎样算块开销。
- 证据尺 bundled。那是不变量 331。
- 填了字段就已经落在块上限下面。那是不变量 331 item 1 余量 / 920。
- 默认证据窗已经够罚。那是不变量 46。
- 仓库默认块 MaxBytes 已经是活性 SLA。那是不变量 63。
