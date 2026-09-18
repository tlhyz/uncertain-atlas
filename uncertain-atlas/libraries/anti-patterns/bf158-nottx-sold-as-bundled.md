# 反模式：把 BIP-158 scripts not already have-tx / not already have-opreturn / not already spent 正式三事（244 余量） 写成已经 已经有那笔交易 / 已经有附言数据 / 已经花掉

**层次**：轻客户端 / BIP-158 scripts not already have-tx / not already have-opreturn / not already spent 正式三事（244 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-158](https://github.com/bitcoin/bips/blob/master/bip-0158.mediawiki)（Deployed, Peer Services；依赖 157）。  
**对应**：[`../tracks/light-clients/worked-example-bf158-nottx-vs-bundled.md`](../tracks/light-clients/worked-example-bf158-nottx-vs-bundled.md)。

把 BIP-158 scripts not already have-tx / not already have-opreturn / not already spent 正式三事（244 余量） 写成已经 已经有那笔交易 / 已经有附言数据 / 已经花掉，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看基本过滤器内容 / 假阳性 正式三事（244 余量），必须分开 not already have-tx、not already in-set、not already consensus 三件事，不要和 244 / 243 / 252 / 1281 / 1282 糊成一句。

也不是：

- [bf158-notrel-sold-as-bundled](bf158-notrel-sold-as-bundled.md) 是 notrel 单句边界（1281），不是本页边界。
- [bf158-notcomm-sold-as-bundled](bf158-notcomm-sold-as-bundled.md) 是 notcomm 单句边界（1282），不是本页边界。
- [cf157-notfull-sold-as-bundled](cf157-notfull-sold-as-bundled.md) 是 BIP-157 支持客户端侧过滤仍未全节点边界（243/1279），不是本页基本过滤器内容边界。
