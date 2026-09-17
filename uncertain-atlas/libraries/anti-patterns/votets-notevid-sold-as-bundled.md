# 反模式：把 冲突提案 not already evidence / not already object / not already exists 正式三事（304 余量） 写成已经 已经有提案证据 / 已经有对象 / 已经有

**层次**：共识 / 冲突提案 not already evidence / not already object / not already exists 正式三事（304 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Validator Signing](https://github.com/cometbft/cometbft/blob/main/spec/consensus/signing.md) validator signing / vote timestamp。  
**对应**：[`../tracks/consensus/worked-example-votets-notevid-vs-bundled.md`](../tracks/consensus/worked-example-votets-notevid-vs-bundled.md)。

把 冲突提案 not already evidence / not already object / not already exists 正式三事（304 余量） 写成已经 已经有提案证据 / 已经有对象 / 已经有，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看冲突提案 正式三事（304 余量），必须分开 not already evidence、not already object、not already exists 三件事，不要和 304 / 21 / 299 / 998 / 1000 糊成一句。

也不是：

- [votets-notcheck-sold-as-bundled](votets-notcheck-sold-as-bundled.md) 是时间戳仍未验过单句边界（998 item 1），不是本页冲突提案仍未有证据边界。
- 双签证据已经通知应用是不变量 21，不是本页两份提案仍未有对象边界。
