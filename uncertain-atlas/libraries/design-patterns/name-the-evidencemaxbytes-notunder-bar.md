# 模式：把填了证据 MaxBytes 不是已经落在块上限下面 not already under-block / not already overhead-deducted / not already fits-budget 正式三事（331 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / EvidenceParams.MaxBytes。  
**例**：[填了证据 MaxBytes not already under-block ≠ bundled（331）](../../tracks/implementation/worked-example-evidencemaxbytes-notunder-vs-bundled.md)。

## 三个名字

1. **填了证据 MaxBytes 不是 already under-block：** 看见填了证据 MaxBytes / 填了这个字段 / EvidenceParams.MaxBytes 有值，不是已经落在块上限下面 interchangeable / 已经落在下面交差 interchangeable，不是 331 evidencemaxbytes bundled interchangeable / 33 four gates interchangeable / evidencemaxbytes-sold-as-blockmax interchangeable。

2. **有上限 不是 already overhead-deducted：** 看见一块里证据有上限 / 有上限 / 证据体积有顶，不是已经扣掉开销 interchangeable / 已经扣开销交差 interchangeable，不是 63 maxbytes-sla interchangeable / 331 evidencemaxbytes item 2 interchangeable。

3. **取值有顶 不是 already fits-budget：** 看见取值有顶 / 不得超过一块减去开销 / 约 BlockParams.MaxBytes 那条，不是已经装得下预算 interchangeable / 已经装得下交差 interchangeable，不是 299 evidence-full interchangeable / 331 evidencemaxbytes item 3 interchangeable。

官方把填了证据 MaxBytes 单句、already under-block、already overhead-deducted、already fits-budget 写成三个名字。把它们叫成一个「看见填了证据 MaxBytes 就已经落在块上限下面 interchangeable / 就已经扣掉开销 interchangeable / 就已经装得下预算 interchangeable」，会把 not already under-block、not already overhead-deducted、not already fits-budget 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了证据 MaxBytes 不是已经落在块上限下面 not already under-block / not already overhead-deducted / not already fits-budget 正式三事（331 余量），先数清问的是填了证据 MaxBytes 是不是 already under-block / 331 / evidencemaxbytes-sold-as-blockmax，是不是有上限 是不是 already overhead-deducted，还是取值有顶 是不是 already fits-budget，再决定要不要同一次发布。331 evidencemaxbytes vs block bundled unbundling 在本页 item 1 启动。
