# 模式：点名 pong31-notmatch 杠

**层次**：网络 / BIP-31 pong not already matched / not already this-ping / not already rtt 正式三事（262 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-31](https://github.com/bitcoin/bips/blob/master/bip-0031.mediawiki)（Deployed, Peer Services）。  
**对应**：[`../tracks/network/worked-example-pong31-notmatch-vs-bundled.md`](../tracks/network/worked-example-pong31-notmatch-vs-bundled.md)。

- **一条 pong 不是已经对上那一次 ping：看见一条 pong，不是已经对上那一次 ping interchangeable / 1269 pong31-notmatch interchangeable。**
- **回显了 nonce 不是已经对上你刚发的那一次：看见回显了 nonce，不是已经对上你刚发的那一次 interchangeable / 1269 pong31-notmatch interchangeable。**
- **nonce 是零 不是已经测过往返：看见 nonce 是零，不是已经测过往返 interchangeable / 1269 pong31-notmatch interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看带 nonce 的 ping / pong 正式三事（262 余量），必须分开 not already nonce-ping、not already matched、not already alive 三件事。
