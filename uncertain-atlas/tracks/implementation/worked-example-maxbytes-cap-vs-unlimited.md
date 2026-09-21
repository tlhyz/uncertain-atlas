# 例：看见 -1 就按 100 MB 验不是已经没有上限；看见应用自己卡体积不是已经引擎不管了；看见必须 -1 或不超过 100 MB 不是已经是默认 21 MB

**层次**：实现 / BlockParams.MaxBytes。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「-1 就按 100 MB 验不是已经没有上限 / 应用自己卡体积不是已经引擎不管了 / 必须 -1 或不超过 100 MB 不是已经是默认 21 MB」，不是整池都给 Prepare 就已经没有上限，也不是仓库默认已经是活性 SLA。不要另写怎样设 MaxBytes 或怎样算块开销。 337 maxbytescap vs unlimited bundled unbundling 续（764 + 765）；精读 [`worked-example-maxbytes-notunlimited-vs-bundled.md`](worked-example-maxbytes-notunlimited-vs-bundled.md)；[`worked-example-maxbytes-notengineoff-vs-bundled.md`](worked-example-maxbytes-notengineoff-vs-bundled.md)（不变量 765 item 2）。

## 官方三件事

规范把块最大字节写成三件独立的实现事，不是「看见写成 -1 就已经没有上限、已经引擎不管了、已经是默认 21 MB」一件事：

1. **看见 `MaxBytes` 写成 -1 / 看见引擎按 100 MB 验 不是已经没有上限，也不是应用已经可以随便回。**  
   官方写：应用若写成 -1，共识会把**实际要验的值**当成 100 MB，并把内存池里所有交易交给 `PrepareProposal`。看见写成 -1，不是已经没有上限。看见按 100 MB 验，不是已经和「整池都给 Prepare、应用仍不得超过 MaxTxBytes」同一句。看见能打满，不是已经交差。
2. **看见应用自己卡体积 / 看见 MAY 写成 -1 不是已经引擎不管了，也不是已经只有应用这一把尺。**  
   官方写：应用若要自己管块大小，可在应用侧设字节上限，用 `PrepareProposal` 卡住回包、用 `ProcessProposal` 拒超限块，这时 **MAY** 把 `MaxBytes` 写成 -1。看见应用自己卡，不是引擎已经不管。看见 MAY 写成 -1，不是已经没有 100 MB 那把尺。看见 Process 会拒，不是已经只有应用在验。
3. **看见必须 `MaxBytes == -1` 或 `0 < MaxBytes <= 100 MB` / 看见默认能接到 21 MB 不是已经是默认 21 MB，也不是已经评估过带宽。**  
   官方写：合法取值只能是 -1，或大于 0 且不超过 100 MB。默认值把最大 21 MB 的块当成合法。若用例不需要这么大，或没评估过传播带宽和延迟，强烈建议把默认往下调。看见合法范围，不是已经是默认那档。看见默认能接到 21 MB，不是已经对照过 `timeout_propose`。看见建议下调，不是已经下调。

怎样设 `MaxBytes`、100 MB / 21 MB 取值、怎样算头和证据开销是规范里的取值或做法，本页不抄。整池都给 Prepare 仍不得超过 MaxTxBytes 是不变量 299，本页不抄。

## 官方为什么这样拆

- **-1 就按 100 MB 验 ≠ 已经没有上限：** 官方把 -1 和引擎仍按 100 MB 验分开。
- **应用自己卡体积 ≠ 已经引擎不管了：** 官方把应用侧上限和引擎那把 100 MB 尺分开。
- **必须 -1 或不超过 100 MB ≠ 已经是默认 21 MB：** 官方把合法范围、默认 21 MB、建议下调分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| -1 就按 100 MB 验 | 不是已经没有上限 | 不是整池都给 Prepare 就已经没有上限（299） |
| 应用自己卡体积 | 不是已经引擎不管了 | 不是仓库默认 MaxBytes 已经是活性 SLA（63） |
| 必须 -1 或不超过 100 MB | 不是已经是默认 21 MB | 不是证据 MaxBytes 已经是块 MaxBytes（331） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「写成 -1 就已经没有上限、已经引擎不管了、已经是默认 21 MB」，必须分开 -1 就按 100 MB 验是不是已经没有上限、应用自己卡体积是不是已经引擎不管了、必须 -1 或不超过 100 MB 是不是已经是默认 21 MB。可以跳过「看见写成 -1 就已经没有上限」。不要把 100 MB / 21 MB 当不确定常数。不要另写怎样设 MaxBytes 或怎样算块开销。 337 maxbytescap vs unlimited bundled unbundling 续（764 + 765 item 2）。

## 本页不抄

- 怎样设 `MaxBytes`、100 MB / 21 MB 取值、怎样算头和证据开销。
- 整池都给 Prepare 就已经没有上限。那是不变量 299。
- 仓库默认 MaxBytes 已经是活性 SLA。那是不变量 63。
- 证据 MaxBytes 已经是块 MaxBytes。那是不变量 331。
