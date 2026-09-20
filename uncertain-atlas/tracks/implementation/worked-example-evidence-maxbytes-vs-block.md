# 例：看见填了证据 MaxBytes 不是已经落在块上限下面；看见 > 0 不是已经盖住解绑；看见证据 MaxBytes 不是已经是块 MaxBytes

**层次**：实现 / EvidenceParams.MaxBytes。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / EvidenceParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「填了证据 MaxBytes 不是已经落在块上限下面 / > 0 不是已经盖住解绑 / 证据 MaxBytes 不是已经是块 MaxBytes」，不是先装证据已经装满交易，也不是默认证据窗已经够罚。不要另写怎样设 EvidenceParams.MaxBytes 或怎样算块开销。 331 evidencemaxbytes vs block bundled unbundling 启动（749）；精读 [`worked-example-evidencemaxbytes-notunder-vs-bundled.md`](worked-example-evidencemaxbytes-notunder-vs-bundled.md)。

## 官方三件事

规范把 `EvidenceParams.MaxBytes` 写成三件独立的实现事，不是「看见填了证据体积上限就已经落在块上限下面、已经盖住解绑、已经是块 MaxBytes」一件事：

1. **看见填了证据 MaxBytes / 看见一块里证据有上限 不是已经落在块 MaxBytes 下面，也不是已经扣掉开销。**  
   官方写：这是**单块能交差的证据总字节**上限。它**应当**舒服地落在块最大字节下面。取值**不得超过**一块减去开销之后的体积（约 `BlockParams.MaxBytes`）。看见填了这个字段，不是已经落在块上限下面。看见有上限，不是已经扣掉开销。
2. **看见 MaxBytes > 0 / 看见合法 不是已经盖住解绑，也不是已经够罚。**  
   官方写：必须 `MaxBytes > 0`。看见大于 0，不是已经盖住解绑期。看见合法，不是已经能罚到人走之前。
3. **看见证据 MaxBytes 不是已经是块 MaxBytes，也不是已经是 -1 无上限，也不是已经是活性 SLA。**  
   官方把证据体积上限和块 `MaxBytes` 写成两把尺。看见证据这边有 MaxBytes，不是已经是块上限。看见填了数，不是已经是写成 -1 的那条。看见有上限，不是已经对照过第一轮超时。

怎样设 `EvidenceParams.MaxBytes`、默认取值、怎样算块开销是规范里的取值或做法，本页不抄。先装证据不是已经装满交易是不变量 299，本页不抄。

## 官方为什么这样拆

- **填了证据 MaxBytes ≠ 已经落在块上限下面：** 官方把「应当落在下面」和「已经填了字段」分开。
- **> 0 ≠ 已经盖住解绑：** 官方把合法下限和证据窗 / 解绑盖住分开。
- **证据 MaxBytes ≠ 已经是块 MaxBytes：** 官方把单块证据体积和整块上限写成两把尺。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 填了证据 MaxBytes | 不是已经落在块上限下面 | 不是先装证据已经装满交易（299） |
| > 0 | 不是已经盖住解绑 | 不是默认证据窗已经够罚（46） |
| 证据 MaxBytes | 不是已经是块 MaxBytes | 不是仓库默认块 MaxBytes 已经是活性 SLA（63） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「填了证据体积上限就已经落在块上限下面、已经盖住解绑、已经是块 MaxBytes」，必须分开填了证据 MaxBytes 是不是已经落在块上限下面、> 0 是不是已经盖住解绑、证据 MaxBytes 是不是已经是块 MaxBytes。可以跳过「看见填了证据体积就已经和块上限同一把尺」。不要另写怎样设 EvidenceParams.MaxBytes 或怎样算块开销。 331 evidencemaxbytes vs block bundled unbundling 启动（749 item 1）。

## 本页不抄

- 怎样设 `EvidenceParams.MaxBytes`、默认取值、怎样算块开销。
- 先装证据已经装满交易、两条上限已经同一条、写成 -1 已经没有上限。那是不变量 299。
- 默认证据窗已经盖住解绑。那是不变量 46。
- 仓库默认块 MaxBytes 已经是活性 SLA。那是不变量 63。
