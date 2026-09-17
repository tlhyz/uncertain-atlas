# 反模式：把 TrySend 回假 not already stopped / not already same-scale / not already delivered 正式三事（309 余量） 写成已经 已经停掉这个人 / 已经和 Send 同一把尺 / 已经送到

**层次**：网络 / TrySend 回假 not already stopped / not already same-scale / not already delivered 正式三事（309 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / send vs enqueued。  
**对应**：[`../tracks/network/worked-example-sendq-notsame-vs-bundled.md`](../tracks/network/worked-example-sendq-notsame-vs-bundled.md)。

把 TrySend 回假 not already stopped / not already same-scale / not already delivered 正式三事（309 余量） 写成已经 已经停掉这个人 / 已经和 Send 同一把尺 / 已经送到，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 TrySend 回假 正式三事（309 余量），必须分开 not already stopped、not already same-scale、not already delivered 三件事，不要和 309 / 67 / 1010 / 1011 糊成一句。

也不是：

- [sendq-notdisc-sold-as-bundled](sendq-notdisc-sold-as-bundled.md) 是 Send 回假仍未断开单句边界（1011 item 2），不是本页 TrySend 仍未和 Send 同一把尺边界。
- 入站配额已经认领 ID 是不变量 67，不是本页立刻回假仍未和 Send 等过同一段时间边界。
