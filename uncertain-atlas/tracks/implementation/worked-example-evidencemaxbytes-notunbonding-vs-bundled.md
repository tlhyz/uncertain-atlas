# 例：看见 MaxBytes > 0 / 看见合法 / 看见盖住解绑期 is not already already covers-unbonding interchangeable / already enough-to-slash interchangeable / already window-covers interchangeable

**层次**：实现 / > 0 不是已经盖住解绑 not already covers-unbonding / not already enough-to-slash / not already window-covers 正式三事（331 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / EvidenceParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「> 0 不是已经盖住解绑 not already covers-unbonding / not already enough-to-slash / not already window-covers 正式三事（331 余量）/ not 750 evidencemaxbytes-notunbonding interchangeable / not 331 evidencemaxbytes bundled interchangeable」，不是 EvidenceParams.MaxBytes bundled（331），也不是填了证据 MaxBytes 不是已经落在块上限下面（749 item 1 余量）或证据 MaxBytes 不是已经是块 MaxBytes（751 item 3 余量）。不要另写怎样设 EvidenceParams.MaxBytes 或怎样算块开销。

## 官方三件事

规范把 Requirements 里必须 MaxBytes > 0、大于 0 不等于盖住解绑、合法不等于够罚 和「已经是 > 0 就已经盖住解绑 interchangeable / 已经是合法就已经够罚 interchangeable / 已经是盖住解绑期就已经窗盖住 interchangeable / 已经是 evidencemaxbytes bundled interchangeable」分开写成三件独立的实现事，不是「看见 > 0 就已经盖住解绑 interchangeable / 就已经够罚 interchangeable / 就已经窗盖住 interchangeable」一件事：

1. **看见 MaxBytes > 0 / 看见大于 0 / 看见有正上限 is not already 已经盖住解绑 interchangeable / 已经 covers-unbonding interchangeable / 已经盖住解绑交差 interchangeable / 331 evidencemaxbytes bundled interchangeable / 33 four gates interchangeable / evidencemaxbytes-sold-as-blockmax interchangeable，也不是已经 EvidenceParams.MaxBytes bundled（331） interchangeable / 750 evidencemaxbytes-notunbonding interchangeable / 331 evidencemaxbytes item 2 interchangeable，也不是已经 > 0 不是已经盖住解绑 not already covers-unbonding / not already enough-to-slash / not already window-covers 正式三事 bundled（331 item 2 余量） interchangeable / 331 evidencemaxbytes item 2 interchangeable，也不是已经填了证据 MaxBytes 不是已经落在块上限下面（749） interchangeable / 751 evidencemaxbytes-notblockmax interchangeable / 46 evidence-default interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：必须 `MaxBytes > 0`。看见大于 0，不是已经盖住解绑期。看见 MaxBytes > 0，不是已经 covers-unbonding interchangeable——331 钉 bundled 三事，本页从 item 2 侧钉 not already covers-unbonding 单句。看见有正上限，不是已经 EvidenceParams.MaxBytes bundled（331） interchangeable——331 钉 bundled，本页钉 item 2 第一件事。看见大于 0，不是已经填了证据 MaxBytes 不是已经落在块上限下面（749） interchangeable——749 另钉 item 1。331 evidencemaxbytes vs block bundled unbundling 在本页 item 2 续。

2. **看见合法 / 看见过了下限 / 看见字段合法 is not already 已经够罚 interchangeable / 已经 enough-to-slash interchangeable / 已经够罚交差 interchangeable / 331 evidencemaxbytes bundled interchangeable / 46 evidence-default interchangeable，也不是已经 EvidenceParams.MaxBytes bundled（331） interchangeable / 750 evidencemaxbytes-notunbonding interchangeable / 331 evidencemaxbytes item 1 落在块上限 interchangeable / 331 evidencemaxbytes item 3 块 MaxBytes interchangeable，也不是已经 > 0 不是已经盖住解绑 not already covers-unbonding / not already enough-to-slash / not already window-covers 正式三事 bundled（331 item 2 余量） interchangeable / 331 evidencemaxbytes item 2 interchangeable，也不是已经盖住解绑（本页第一件事） interchangeable。**  
   官方写：看见合法，不是已经能罚到人走之前。看见合法，不是已经 enough-to-slash interchangeable——本页钉 not already enough-to-slash 单句。看见过了下限，不是已经默认证据窗已经够罚（46） interchangeable——46 另钉。看见字段合法，不是已经盖住解绑（本页第一件事） interchangeable——三件事分开钉。331 evidencemaxbytes vs block bundled unbundling 在本页 item 2 续。

3. **看见盖住解绑期 / 看见证据窗盖住 / 看见窗盖住 is not already 已经窗盖住交差 interchangeable / 已经 window-covers interchangeable / 已经窗盖住交差 interchangeable / 331 evidencemaxbytes bundled interchangeable / 46 evidence-default interchangeable，也不是已经 EvidenceParams.MaxBytes bundled（331） interchangeable / 750 evidencemaxbytes-notunbonding interchangeable / 331 evidencemaxbytes item 1 / 331 evidencemaxbytes item 3，也不是已经 > 0 不是已经盖住解绑 not already covers-unbonding / not already enough-to-slash / not already window-covers 正式三事 bundled（331 item 2 余量） interchangeable / 331 evidencemaxbytes item 2 interchangeable，也不是已经盖住解绑（本页第一件事） interchangeable / 已经够罚（本页第二件事） interchangeable。**  
   官方写：看见大于 0，不是已经盖住解绑期。看见盖住解绑期，不是已经 window-covers interchangeable——本页钉 not already window-covers 单句。看见证据窗盖住，不是已经默认证据窗已经够罚（46） interchangeable——46 另钉证据窗。看见窗盖住，不是已经够罚（本页第二件事） interchangeable——三件事分开钉。331 evidencemaxbytes vs block bundled unbundling 在本页 item 2 完成。

怎样设 `EvidenceParams.MaxBytes`、默认取值、怎样算块开销是规范里的取值或做法，本页不抄。EvidenceParams.MaxBytes bundled（331）、填了证据 MaxBytes 不是已经落在块上限下面（331 item 1 余量 / 749）、证据 MaxBytes 不是已经是块 MaxBytes（331 item 3 余量 / 751）、默认证据窗已经够罚（46）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **> 0 not already covers-unbonding ≠ 331 / 33 interchangeable：** 官方把合法下限和已经盖住解绑分开。
- **合法 not already enough-to-slash ≠ 已经够罚 interchangeable：** 官方把字段合法和已经能罚到人走之前分开。
- **盖住解绑期 not already window-covers ≠ 已经窗盖住 interchangeable：** 官方把盖住解绑期和证据窗已经盖住分开；331 evidencemaxbytes vs block bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| MaxBytes > 0 | 不是 already covers-unbonding | 不是落在块上限 alone（749） |
| 合法 | 不是 already enough-to-slash | 不是默认证据窗 alone（46） |
| 盖住解绑期 | 不是 already window-covers | 不是默认证据窗够罚 alone（46） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 > 0 不是已经盖住解绑 not already covers-unbonding / not already enough-to-slash / not already window-covers 正式三事（331 余量），必须分开 MaxBytes > 0 是不是 already covers-unbonding interchangeable / 331 evidencemaxbytes bundled interchangeable / evidencemaxbytes-sold-as-blockmax interchangeable、合法 是不是 already enough-to-slash interchangeable、盖住解绑期 是不是 already window-covers interchangeable。可以跳过「看见 > 0 就已经盖住解绑 interchangeable / 就已经够罚 interchangeable / 就已经窗盖住 interchangeable」。不要另写怎样设 EvidenceParams.MaxBytes。331 evidencemaxbytes vs block bundled unbundling 在本页 item 2 续（749 + 750）；续 [`worked-example-evidencemaxbytes-notblockmax-vs-bundled.md`](worked-example-evidencemaxbytes-notblockmax-vs-bundled.md)（不变量 751 item 3）。

## 本页不抄

- 怎样设 `EvidenceParams.MaxBytes`、默认取值、怎样算块开销。
- EvidenceParams.MaxBytes bundled。那是不变量 331。
- 填了证据 MaxBytes 不是已经落在块上限下面。那是不变量 331 item 1 余量 / 749。
- 证据 MaxBytes 不是已经是块 MaxBytes。那是不变量 331 item 3 余量 / 751。
- 默认证据窗已经盖住解绑 / 已经够罚。那是不变量 46。
- 四门已经结算。那是不变量 33。
