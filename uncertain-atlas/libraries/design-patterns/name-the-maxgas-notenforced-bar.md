# 模式：把 MaxGas 不是已经在执行 not already enforcing / not already MaxBytes synonym / not already fee market 正式三事（315 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Gas。  
**例**：[字段在 not already enforcing ≠ bundled（315）](../../tracks/implementation/worked-example-maxgas-notenforced-vs-bundled.md)。

## 三个名字

1. **字段在 不是 already enforcing：** 看见 MaxGas / 回包里有气字段，不是已经在执行 interchangeable / 已经在卡 interchangeable，不是 315 maxgas bundled interchangeable / 299 maxbytes interchangeable / maxgas-sold-as-enforced interchangeable。

2. **写成 -1 不是 already MaxBytes synonym：** 看见默认 -1 / MaxGas = -1，不是已经和 MaxBytes 写成 -1 同一句 interchangeable / 已经没有上限同一句 interchangeable，不是 315 maxgas item 2 interchangeable / 705 maxgas-notgasused interchangeable。

3. **学了以太坊 不是 already fee market：** 看见官方说学了类似抽象 / 类似以太坊气，不是已经有费用市场 interchangeable / 已经以太坊费用市场 interchangeable，不是 315 maxgas item 3 interchangeable / 706 maxgas-notcommitted interchangeable。

官方把字段在单句、already enforcing、already MaxBytes synonym、already fee market 写成三个名字。把它们叫成一个「看见有 MaxGas 就已经在卡 interchangeable / 就已经和 MaxBytes -1 同一句 interchangeable / 就已经有费用市场 interchangeable」，会把 not already enforcing、not already MaxBytes synonym、not already fee market 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MaxGas 不是已经在执行 not already enforcing / not already MaxBytes synonym / not already fee market 正式三事（315 余量），先数清问的是字段在 是不是 already enforcing / 315 / maxgas-sold-as-enforced，是不是写成 -1 是不是 already MaxBytes synonym，还是学了以太坊 是不是 already fee market，再决定要不要同一次发布。315 maxgas vs enforced bundled unbundling 在本页 item 1 完成。
