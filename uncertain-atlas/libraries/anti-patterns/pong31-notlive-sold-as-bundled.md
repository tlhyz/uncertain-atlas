# 反模式：把 BIP-31 pong not already alive / not already unstuck / not already forever 正式三事（262 余量） 写成已经 已经还活着 / 已经不卡 / 已经永远响应

**层次**：网络 / BIP-31 pong not already alive / not already unstuck / not already forever 正式三事（262 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-31](https://github.com/bitcoin/bips/blob/master/bip-0031.mediawiki)（Deployed, Peer Services）。  
**对应**：[`../tracks/network/worked-example-pong31-notlive-vs-bundled.md`](../tracks/network/worked-example-pong31-notlive-vs-bundled.md)。

把 BIP-31 pong not already alive / not already unstuck / not already forever 正式三事（262 余量） 写成已经 已经还活着 / 已经不卡 / 已经永远响应，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看带 nonce 的 ping / pong 正式三事（262 余量），必须分开 not already nonce-ping、not already matched、not already alive 三件事，不要和 262 / 256 / 259 / 1268 / 1269 糊成一句。

也不是：

- [pong31-notver-sold-as-bundled](pong31-notver-sold-as-bundled.md) 是 notver 单句边界（1268），不是本页边界。
- [pong31-notmatch-sold-as-bundled](pong31-notmatch-sold-as-bundled.md) 是 notmatch 单句边界（1269），不是本页边界。
- [rej61-notill-sold-as-bundled](rej61-notill-sold-as-bundled.md) 是 BIP-61 拒收仍未共识非法边界（254/1265），不是本页 pong 探活边界。
