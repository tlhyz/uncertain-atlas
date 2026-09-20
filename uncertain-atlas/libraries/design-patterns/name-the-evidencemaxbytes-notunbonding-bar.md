# 模式：把 > 0 不是已经盖住解绑 not already covers-unbonding / not already enough-to-slash / not already window-covers 正式三事（331 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / EvidenceParams.MaxBytes。  
**例**：[> 0 not already covers-unbonding ≠ bundled（331）](../../tracks/implementation/worked-example-evidencemaxbytes-notunbonding-vs-bundled.md)。

## 三个名字

1. **MaxBytes > 0 不是 already covers-unbonding：** 看见 MaxBytes > 0 / 大于 0 / 有正上限，不是已经盖住解绑 interchangeable / 已经盖住解绑交差 interchangeable，不是 331 evidencemaxbytes bundled interchangeable / 33 four gates interchangeable / evidencemaxbytes-sold-as-blockmax interchangeable。

2. **合法 不是 already enough-to-slash：** 看见合法 / 过了下限 / 字段合法，不是已经够罚 interchangeable / 已经够罚交差 interchangeable，不是 46 evidence-default interchangeable / 331 evidencemaxbytes item 1 interchangeable。

3. **盖住解绑期 不是 already window-covers：** 看见盖住解绑期 / 证据窗盖住 / 窗盖住，不是已经窗盖住交差 interchangeable / 已经窗盖住交差 interchangeable，不是 46 evidence-default interchangeable / 331 evidencemaxbytes item 3 interchangeable。

官方把 > 0 单句、already covers-unbonding、already enough-to-slash、already window-covers 写成三个名字。把它们叫成一个「看见 > 0 就已经盖住解绑 interchangeable / 就已经够罚 interchangeable / 就已经窗盖住 interchangeable」，会把 not already covers-unbonding、not already enough-to-slash、not already window-covers 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 > 0 不是已经盖住解绑 not already covers-unbonding / not already enough-to-slash / not already window-covers 正式三事（331 余量），先数清问的是 MaxBytes > 0 是不是 already covers-unbonding / 331 / evidencemaxbytes-sold-as-blockmax，是不是合法 是不是 already enough-to-slash，还是盖住解绑期 是不是 already window-covers，再决定要不要同一次发布。331 evidencemaxbytes vs block bundled unbundling 在本页 item 2 续。
