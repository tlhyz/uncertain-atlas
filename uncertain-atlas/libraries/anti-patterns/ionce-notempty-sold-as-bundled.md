# 反模式：把 InitChain may-choose-set not already no-set / not already genesis-used / not already app-checked 正式三事（412 余量） 写成已经 已经没有集合 / 已经用了创世文件里的验证者 / 已经验过应用状态

**层次**：实现 / InitChain may-choose-set not already no-set / not already genesis-used / not already app-checked 正式三事（412 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**对应**：[`../tracks/implementation/worked-example-ionce-notempty-vs-bundled.md`](../tracks/implementation/worked-example-ionce-notempty-vs-bundled.md)。

把 InitChain may-choose-set not already no-set / not already genesis-used / not already app-checked 正式三事（412 余量） 写成已经 已经没有集合 / 已经用了创世文件里的验证者 / 已经验过应用状态，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 may-choose-set 正式三事（412 余量），必须分开 not already no-set、not already genesis-used、not already app-checked 三件事，不要和 412 / 318 / 364 / 1091 / 1093 糊成一句。

也不是：

- [ionce-notcrash-sold-as-bundled](ionce-notcrash-sold-as-bundled.md) 是创世只调一次仍未是崩溃后再调单句边界（1091 item 1），不是本页能决定仍未没有集合边界。
- InitChain 回了空名单就已经没有集合是不变量 318，不是本页能算另一套仍未用了创世文件边界。
