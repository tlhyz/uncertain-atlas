# 反模式：把 BIP-35 dump-get not already downloaded / not already full-query / not already gone 正式三事（253 余量） 写成已经 已经下载那些交易 / 已经支持整池查询 / 那些交易已经不在池里

**层次**：内存池 / BIP-35 dump-get not already downloaded / not already full-query / not already gone 正式三事（253 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-35](https://github.com/bitcoin/bips/blob/master/bip-0035.mediawiki)（Deployed, Peer Services）。  
**对应**：[`../tracks/mempool/worked-example-dump35-notget-vs-bundled.md`](../tracks/mempool/worked-example-dump35-notget-vs-bundled.md)。

把 BIP-35 dump-get not already downloaded / not already full-query / not already gone 正式三事（253 余量） 写成已经 已经下载那些交易 / 已经支持整池查询 / 那些交易已经不在池里，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看未确认池查询 正式三事（253 余量），必须分开 not already have、not already downloaded、not already answering 三件事，不要和 253 / 249 / 245 / 1262 / 1264 糊成一句。

也不是：

- [dump35-nothave-sold-as-bundled](dump35-nothave-sold-as-bundled.md) 是 nothave 单句边界（1262），不是本页边界。
- [dump35-notver-sold-as-bundled](dump35-notver-sold-as-bundled.md) 是 notver 单句边界（1264），不是本页边界。
- [blm111-notoff-sold-as-bundled](blm111-notoff-sold-as-bundled.md) 是 BIP-111 没开布隆仍未退役边界（252/1260），不是本页内存池查询边界。
