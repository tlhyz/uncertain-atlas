# 模式：把 InitChain Usage app decide accept or different one not Response empty/not empty rule / not InitChain Usage remainder bundled / not genesis app_state already verified 正式三事（496 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**例**：[app decide not Response rule ≠ bundled（496）](../../tracks/implementation/worked-example-initchaindecide-notrule-vs-bundled.md)。

## 三个名字

1. **app decide 不是 Response empty/not empty 规则：** 看见 Methods Usage decide，不是已经 495 interchangeable / 698 initchaindecide-notrule interchangeable。
2. **看见 accept or different one 不是 InitChain Usage 余量 bundled：** 看见 decide，不是已经 412 bundled 第二件事 interchangeable。
3. **看见 Usage 这句 不是创世 app_state 就已经验过：** 看见 decide 单句，不是已经 303 interchangeable。

官方把 InitChain Usage 后三条核心句拆成三个名字。把它们叫成一个「看见 InitChain 了就已经 Response 规则 / 已经改了集合 / 已经没有集合」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage decide 正式三事（496 余量），先数清问的是 decide 是不是 495 response 规则、是不是 412 bundled、还是看见 Usage 是不是创世 app_state 就已经验过 / 303，再决定要不要同一次发布。496 initchaindecide vs emptyset bundled unbundling 在本页 item 1 启动。
