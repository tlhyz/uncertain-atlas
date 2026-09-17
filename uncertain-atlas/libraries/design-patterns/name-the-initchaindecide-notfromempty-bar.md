# 模式：把 InitChain Usage updating from empty set not empty list means no set / not Response empty/not empty rule / not app decide already used genesis validators 正式三事（496 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**例**：[updating from empty set not no-set ≠ bundled（496）](../../tracks/implementation/worked-example-initchaindecide-notfromempty-vs-bundled.md)。

## 三个名字

1. **updating from empty set 不是空名单就没有集合：** 看见从空集合更新，不是已经 318 interchangeable / 700 initchaindecide-notfromempty interchangeable。
2. **看见 technically both are updating 不是 Response empty/not empty 规则：** 看见 from the empty set，不是已经 495 interchangeable。
3. **看见 Usage 这句 不是 app decide 就已经用了创世验证者：** 看见 from the empty set，不是已经 412 bundled 第三件事 interchangeable。

官方把 InitChain Usage 后三条核心句拆成三个名字。把它们叫成一个「看见 InitChain 了就已经 Response 规则 / 已经改了集合 / 已经没有集合」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage updating from empty set 正式三事（496 余量），先数清问的是 updating from empty set 是不是空名单就没有集合 / 318、是不是 495 response 规则、还是看见 Usage 是不是 app decide 就已经用了创世验证者，再决定要不要同一次发布。496 initchaindecide vs emptyset bundled unbundling 在本页 item 3 完成。
