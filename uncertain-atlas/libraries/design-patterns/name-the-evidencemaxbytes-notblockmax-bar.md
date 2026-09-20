# 模式：把证据 MaxBytes 不是已经是块 MaxBytes not already block-maxbytes / not already minus-one / not already propose-sla 正式三事（331 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / EvidenceParams.MaxBytes。  
**例**：[证据 MaxBytes not already block-maxbytes ≠ bundled（331）](../../tracks/implementation/worked-example-evidencemaxbytes-notblockmax-vs-bundled.md)。

## 三个名字

1. **证据 MaxBytes 不是 already block-maxbytes：** 看见证据 MaxBytes / 证据这边有 MaxBytes / 证据体积上限，不是已经是块 MaxBytes interchangeable / 已经块上限交差 interchangeable，不是 331 evidencemaxbytes bundled interchangeable / 33 four gates interchangeable / evidencemaxbytes-sold-as-blockmax interchangeable。

2. **填了数 不是 already minus-one：** 看见填了数 / 写成数 / 不是空白，不是已经是 -1 无上限 interchangeable / 已经无上限交差 interchangeable，不是 299 evidence-full interchangeable / 331 evidencemaxbytes item 1 interchangeable。

3. **有上限 不是 already propose-sla：** 看见有上限 / 对照第一轮超时 / 活性相关上限，不是已经是活性 SLA interchangeable / 已经活性 SLA 交差 interchangeable，不是 63 maxbytes-sla interchangeable / 331 evidencemaxbytes item 2 interchangeable。

官方把证据 MaxBytes 单句、already block-maxbytes、already minus-one、already propose-sla 写成三个名字。把它们叫成一个「看见证据 MaxBytes 就已经是块 MaxBytes interchangeable / 就已经是 -1 无上限 interchangeable / 就已经是活性 SLA interchangeable」，会把 not already block-maxbytes、not already minus-one、not already propose-sla 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看证据 MaxBytes 不是已经是块 MaxBytes not already block-maxbytes / not already minus-one / not already propose-sla 正式三事（331 余量），先数清问的是证据 MaxBytes 是不是 already block-maxbytes / 331 / evidencemaxbytes-sold-as-blockmax，是不是填了数 是不是 already minus-one，还是有上限 是不是 already propose-sla，再决定要不要同一次发布。331 evidencemaxbytes vs block bundled unbundling 在本页 item 3 完成。
