# 反模式：把 h_e 必须高于当前不是已经能写成当前高度 not already writecurrent / not already height-H-prepare / not already settled 正式三事（346 余量）说成已经能写成当前高度 / 已经是到了 H 才 Prepare 带扩展 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[h_e 必须高于当前 not already writecurrent ≠ bundled（346）](../../tracks/implementation/worked-example-abci20-notwritecurrent-vs-bundled.md)。

## 卖法

把升级之后 *h<sub>u</sub>* 才能把 `VoteExtensionsEnableHeight` 写成 *h<sub>e</sub>* / *h<sub>e</sub>* 必须高于当前（最早 *h<sub>u</sub>*+1） / 必须比当前链高度高 写成已经能写成当前高度 interchangeable / 已经 writecurrent interchangeable / 已经写成当前交差 interchangeable / 346 abci20upgrade bundled interchangeable / abci20upgrade-sold-as-height interchangeable；把必须比当前高 / 最早 *h<sub>u</sub>*+1 写成已经是到了 H 才 Prepare 带扩展那种切换 interchangeable / 已经 height-H-prepare interchangeable / 已经 H Prepare 交差 interchangeable；把升级过了 / 协调升级已经发生在 *h<sub>u</sub>* 之后 写成已经交差 interchangeable / 已经 settled interchangeable / 已经写高度交差 interchangeable，或已经和 346 abci20upgrade bundled / abci20upgrade-sold-as-height interchangeable / 792 abci20-notwritecurrent interchangeable。

## 为什么错

官方把升级之后才能写高于当前的启用高度、不是已经是到了 H 才 Prepare 带扩展、不是已经交差写成三件独立的实现事。把它们卖成 already writecurrent interchangeable / already height-H-prepare interchangeable / already settled interchangeable，会把 not already writecurrent、not already height-H-prepare、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 h_e 必须高于当前不是已经能写成当前高度 not already writecurrent / not already height-H-prepare / not already settled 正式三事（346 余量），必须分开 not already writecurrent、not already height-H-prepare、not already settled 三件事，不要和 346 / 330 / 343 / 791 / 793 糊成一句。

## 和相邻反模式

- [abci20upgrade-sold-as-height](abci20upgrade-sold-as-height.md) 是 ABCI 2.0 协调升级 bundled 全段，不是本页 h_e 必须高于当前 item 2 单句边界。
- [abci20-notonlyveheight-sold-as-bundled](abci20-notonlyveheight-sold-as-bundled.md) 是必须协调升级 not already only-veheight（346 item 1），不是本页 not already writecurrent 边界。
- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是到了 H 不是已经 Prepare 带了扩展（330），不是本页必须比当前高 ≠ H Prepare 切换 边界。
