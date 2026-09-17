# 反模式：把 应用比引擎高 not already allowed / not already recover-alone / not already same-as-atomic 正式三事（320 余量） 写成已经 已经允许 / 已经能各醒各的 / 已经和半写已经原子同一句

**层次**：实现 / 应用比引擎高 not already allowed / not already recover-alone / not already same-as-atomic 正式三事（320 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Crash Recovery。  
**对应**：[`../tracks/implementation/worked-example-crashrec-notahead-vs-bundled.md`](../tracks/implementation/worked-example-crashrec-notahead-vs-bundled.md)。

把 应用比引擎高 not already allowed / not already recover-alone / not already same-as-atomic 正式三事（320 余量） 写成已经 已经允许 / 已经能各醒各的 / 已经和半写已经原子同一句，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看应用比引擎高 正式三事（320 余量），必须分开 not already allowed、not already recover-alone、not already same-as-atomic 三件事，不要和 320 / 5 / 298 / 1020 / 1021 糊成一句。

也不是：

- [chktxresp-notprio-sold-as-bundled](chktxresp-notprio-sold-as-bundled.md) 是 Priority 仍未共识顺序边界（317/1018），不是本页应用比引擎高仍未允许边界。
- 半写已经原子是不变量 5，不是本页两边高度不一样仍未各醒各的边界。
