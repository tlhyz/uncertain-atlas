# 反模式：把 断开 not already slashed / not already on-chain / not already doublesign 正式三事（304 余量） 写成已经 已经罚了 / 已经上链 / 已经是双签

**层次**：共识 / 断开 not already slashed / not already on-chain / not already doublesign 正式三事（304 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Validator Signing](https://github.com/cometbft/cometbft/blob/main/spec/consensus/signing.md) validator signing / vote timestamp。  
**对应**：[`../tracks/consensus/worked-example-votets-notslash-vs-bundled.md`](../tracks/consensus/worked-example-votets-notslash-vs-bundled.md)。

把 断开 not already slashed / not already on-chain / not already doublesign 正式三事（304 余量） 写成已经 已经罚了 / 已经上链 / 已经是双签，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看断开 正式三事（304 余量），必须分开 not already slashed、not already on-chain、not already doublesign 三件事，不要和 304 / 19 / 46 / 998 / 999 糊成一句。

也不是：

- [votets-notevid-sold-as-bundled](votets-notevid-sold-as-bundled.md) 是冲突提案仍未有证据单句边界（999 item 2），不是本页断开仍未罚边界。
- 签名器已经记住上次高度轮类型是不变量 19，不是本页非法仍未上链边界。
