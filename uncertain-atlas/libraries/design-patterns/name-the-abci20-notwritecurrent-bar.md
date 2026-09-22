# 模式：把 h_e 必须高于当前不是已经能写成当前高度 not already writecurrent / not already height-H-prepare / not already settled 正式三事（346 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Application configuration required to switch to ABCI 2.0。  
**例**：[h_e 必须高于当前 not already writecurrent ≠ bundled（346）](../../tracks/implementation/worked-example-abci20-notwritecurrent-vs-bundled.md)。

## 三个名字

1. **h_e 必须高于当前 不是 already writecurrent：** 看见升级之后 *h<sub>u</sub>* 才能把 `VoteExtensionsEnableHeight` 写成 *h<sub>e</sub>* / *h<sub>e</sub>* 必须高于当前（最早 *h<sub>u</sub>*+1） / 必须比当前链高度高，不是已经能写成当前高度 interchangeable / 已经 writecurrent interchangeable / 已经写成当前交差 interchangeable，不是 346 abci20upgrade bundled interchangeable / abci20upgrade-sold-as-height interchangeable。

2. **必须比当前高 不是 already height-H-prepare：** 看见必须比当前高 / 最早 *h<sub>u</sub>*+1 / 启用高度要晚于当前，不是已经是到了 H 才 Prepare 带扩展那种切换 interchangeable / 已经 height-H-prepare interchangeable / 已经 H Prepare 交差 interchangeable，不是 330 veheight-sold-as-prepared interchangeable / 343 pbtsheight interchangeable。

3. **升级过了 不是 already settled：** 看见升级过了 / 协调升级已经发生在 *h<sub>u</sub>* 之后 / 可以开始写 *h<sub>e</sub>*，不是已经交差 interchangeable / 已经 settled interchangeable / 已经写高度交差 interchangeable，不是 791 abci20-notonlyveheight interchangeable / 793 abci20-notgenesiscfg interchangeable。

官方把升级之后才能写高于当前的启用高度、不是已经是到了 H 才 Prepare 带扩展、不是已经交差写成三个名字。把它们叫成一个「看见必须比当前高就已经能写成当前 interchangeable / 就已经是到了 H 才 Prepare 带扩展 interchangeable / 就已经交差 interchangeable」，会把 not already writecurrent、not already height-H-prepare、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 h_e 必须高于当前不是已经能写成当前高度 not already writecurrent / not already height-H-prepare / not already settled 正式三事（346 余量），先数清问的是 h_e 必须高于当前 是不是 already writecurrent / 346 / abci20upgrade-sold-as-height，是不是必须比当前高 是不是 already height-H-prepare，还是升级过了 是不是 already settled，再决定要不要同一次发布。346 abci20 vs height bundled unbundling 在本页 item 2 续。
