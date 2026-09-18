# 反模式：把 BIP-30 same-txid not already unique / not already same-outputs / not already settled 正式三事（257 余量） 写成已经 已经唯一 / 已经不怕被覆盖 / 已经交差

**层次**：共识 / BIP-30 same-txid not already unique / not already same-outputs / not already settled 正式三事（257 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-30](https://github.com/bitcoin/bips/blob/master/bip-0030.mediawiki)（Deployed, Consensus soft fork）。  
**对应**：[`../tracks/consensus/worked-example-dup30-notuniq-vs-bundled.md`](../tracks/consensus/worked-example-dup30-notuniq-vs-bundled.md)。

把 BIP-30 same-txid not already unique / not already same-outputs / not already settled 正式三事（257 余量） 写成已经 已经唯一 / 已经不怕被覆盖 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同一交易标识 正式三事（257 余量），必须分开 not already unique、not already same-outputs、not already settled 三件事，不要和 257 / 152 / 163 / 1227 / 1228 糊成一句。

也不是：

- [pc47-notagain-sold-as-bundled](pc47-notagain-sold-as-bundled.md) 是第一次仍未免通知边界（273/1225），不是本页同一标识仍未唯一边界。
- [dup30-notlive-sold-as-bundled](dup30-notlive-sold-as-bundled.md) 是还没花光仍未合法单句边界（1227 item 2），不是本页同一标识仍未唯一边界。
- [duplicate-txid-sold-as-unique](duplicate-txid-sold-as-unique.md) 是父页 bundled 边界（257），不是本页余量单句。
