# 反模式：把 BIP-111 bloom-off not already retired / not already cfilter / not already consensus-illegal 正式三事（252 余量） 写成已经 全网布隆已经退役 / 已经改用客户端侧过滤 / 已经共识非法

**层次**：轻客户端 / BIP-111 bloom-off not already retired / not already cfilter / not already consensus-illegal 正式三事（252 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-111](https://github.com/bitcoin/bips/blob/master/bip-0111.mediawiki)（Deployed, Peer Services）。  
**对应**：[`../tracks/light-clients/worked-example-blm111-notoff-vs-bundled.md`](../tracks/light-clients/worked-example-blm111-notoff-vs-bundled.md)。

把 BIP-111 bloom-off not already retired / not already cfilter / not already consensus-illegal 正式三事（252 余量） 写成已经 全网布隆已经退役 / 已经改用客户端侧过滤 / 已经共识非法，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看布隆服务位 正式三事（252 余量），必须分开 not already private、not already retired、not already obeying 三件事，不要和 252 / 243 / 245 / 1259 / 1261 糊成一句。

也不是：

- [blm111-notpriv-sold-as-bundled](blm111-notpriv-sold-as-bundled.md) 是 notpriv 单句边界（1259），不是本页边界。
- [blm111-notver-sold-as-bundled](blm111-notver-sold-as-bundled.md) 是 notver 单句边界（1261），不是本页边界。
- [wit144-nothave-sold-as-bundled](wit144-nothave-sold-as-bundled.md) 是 BIP-144 带见证序列化仍未有见证边界（251/1256），不是本页布隆服务位边界。
