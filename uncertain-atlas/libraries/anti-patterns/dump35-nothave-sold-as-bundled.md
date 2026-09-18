# 反模式：把 BIP-35 dump-inv not already have / not already accepted / not already empty-pool 正式三事（253 余量） 写成已经 已经有那些交易 / 已经收下 / 这个节点已经没有未确认池

**层次**：内存池 / BIP-35 dump-inv not already have / not already accepted / not already empty-pool 正式三事（253 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-35](https://github.com/bitcoin/bips/blob/master/bip-0035.mediawiki)（Deployed, Peer Services）。  
**对应**：[`../tracks/mempool/worked-example-dump35-nothave-vs-bundled.md`](../tracks/mempool/worked-example-dump35-nothave-vs-bundled.md)。

把 BIP-35 dump-inv not already have / not already accepted / not already empty-pool 正式三事（253 余量） 写成已经 已经有那些交易 / 已经收下 / 这个节点已经没有未确认池，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看未确认池查询 正式三事（253 余量），必须分开 not already have、not already downloaded、not already answering 三件事，不要和 253 / 245 / 248 / 1263 / 1264 糊成一句。

也不是：

- [dump35-notget-sold-as-bundled](dump35-notget-sold-as-bundled.md) 是 notget 单句边界（1263），不是本页边界。
- [dump35-notver-sold-as-bundled](dump35-notver-sold-as-bundled.md) 是 notver 单句边界（1264），不是本页边界。
- [blm111-notoff-sold-as-bundled](blm111-notoff-sold-as-bundled.md) 是 BIP-111 没开布隆仍未退役边界（252/1260），不是本页内存池查询边界。
