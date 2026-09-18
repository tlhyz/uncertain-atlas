# 反模式：把 BIP-30 unspent-collide not already legal / not already all-coinbase-unique / not already settled 正式三事（257 余量） 写成已经 已经合法 / 已经保证所有 coinbase 标识都唯一 / 已经交差

**层次**：共识 / BIP-30 unspent-collide not already legal / not already all-coinbase-unique / not already settled 正式三事（257 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-30](https://github.com/bitcoin/bips/blob/master/bip-0030.mediawiki)（Deployed, Consensus soft fork）。  
**对应**：[`../tracks/consensus/worked-example-dup30-notlive-vs-bundled.md`](../tracks/consensus/worked-example-dup30-notlive-vs-bundled.md)。

把 BIP-30 unspent-collide not already legal / not already all-coinbase-unique / not already settled 正式三事（257 余量） 写成已经 已经合法 / 已经保证所有 coinbase 标识都唯一 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看还没花光的旧标识 正式三事（257 余量），必须分开 not already legal、not already all-coinbase-unique、not already settled 三件事，不要和 257 / 173 / 1226 / 1228 糊成一句。

也不是：

- [dup30-notuniq-sold-as-bundled](dup30-notuniq-sold-as-bundled.md) 是同一标识仍未唯一单句边界（1226 item 1），不是本页还没花光仍未合法边界。
- [dup30-notspent-sold-as-bundled](dup30-notspent-sold-as-bundled.md) 是花光后再出现仍未非法单句边界（1228 item 3），不是本页还没花光仍未合法边界。
