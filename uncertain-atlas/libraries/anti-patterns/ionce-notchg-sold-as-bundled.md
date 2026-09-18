# 反模式：把 InitChain Validators-as-update not already set-changed / not already has-key / not already no-set 正式三事（412 余量） 写成已经 已经改了集合 / 已经带了公钥 / 已经没有集合

**层次**：实现 / InitChain Validators-as-update not already set-changed / not already has-key / not already no-set 正式三事（412 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**对应**：[`../tracks/implementation/worked-example-ionce-notchg-vs-bundled.md`](../tracks/implementation/worked-example-ionce-notchg-vs-bundled.md)。

把 InitChain Validators-as-update not already set-changed / not already has-key / not already no-set 正式三事（412 余量） 写成已经 已经改了集合 / 已经带了公钥 / 已经没有集合，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Validators-as-update 正式三事（412 余量），必须分开 not already set-changed、not already has-key、not already no-set 三件事，不要和 412 / 364 / 318 / 1091 / 1092 糊成一句。

也不是：

- [ionce-notempty-sold-as-bundled](ionce-notempty-sold-as-bundled.md) 是能决定仍未没有集合单句边界（1092 item 2），不是本页两边都是 ValidatorUpdate 仍未改了集合边界。
- ValidatorUpdate 用公钥认人就已经改了集合是不变量 364，不是本页从空集合更新仍未带了公钥边界。
