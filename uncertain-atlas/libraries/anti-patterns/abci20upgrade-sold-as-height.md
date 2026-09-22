# 反模式：看见必须协调升级就当成已经只改 VoteExtensionsEnableHeight / 看见 h_e 必须高于当前就当成已经能写成当前高度 / 看见引擎按当前高度决定存什么要什么就当成已经按创世配好了

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Application configuration required to switch to ABCI 2.0。  
**例**：[必须协调升级 ≠ 已经只改 VoteExtensionsEnableHeight](../../tracks/implementation/worked-example-abci20-upgrade-vs-height.md)。

## 塌法

1. 看见必须协调升级 / 看见切到带扩展的 CometBFT，就当成已经只改 `VoteExtensionsEnableHeight`，或当成已经是单节点能切。
2. 看见升级之后 *h<sub>u</sub>* 才能写成 *h<sub>e</sub>* / 看见 *h<sub>e</sub>* 必须高于当前（最早 *h<sub>u</sub>*+1），就当成已经能写成当前高度，或当成已经是到了 H 才 Prepare 带扩展那种切换。
3. 看见引擎按当前高度决定存什么、要什么 / 看见成功运转看当前高度，就当成已经按创世配好了，或当成已经是应用自己决定存什么。

## 为什么会出事

官方写：切到带投票扩展的版本必须协调升级。升级发生在 *h<sub>u</sub>* 之后，`VoteExtensionsEnableHeight` 可以写成 *h<sub>e</sub>*，但必须高于当前链高度，最早是 *h<sub>u</sub>*+1。CometBFT 按当前高度决定存哪些数据、运转要哪些数据。

## 和相邻反模式

- [abci20-notonlyveheight-sold-as-bundled](abci20-notonlyveheight-sold-as-bundled.md) 是必须协调升级 not already only-veheight / not already single-node / not already field-filled 正式三事（346 item 1），不是本页 bundled 全段 alone。
- [abci20-notwritecurrent-sold-as-bundled](abci20-notwritecurrent-sold-as-bundled.md) 是 h_e 必须高于当前 not already writecurrent / not already height-H-prepare / not already settled 正式三事（346 item 2），不是本页 bundled 全段 alone。
- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是到了 H 不是已经 Prepare 带了扩展，不是本页这种必须协调升级不是已经只改 VoteExtensionsEnableHeight。
- [enable-height-sold-as-safe](enable-height-sold-as-safe.md) 是治理改 enable-height 会让未升级节点 panic，不是本页这种 h_e 必须高于当前不是已经能写成当前高度。
- [pbtsheight-sold-as-enabled](pbtsheight-sold-as-enabled.md) 是写成 0 不是已经启用 PBTS，不是本页这种引擎按当前高度决定存什么要什么不是已经按创世配好了。
