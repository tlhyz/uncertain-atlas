# 模式：点名 bf158-notcomm 杠

**层次**：轻客户端 / BIP-158 exclude-opreturn not already consensus / not already other-type / not already header-chain 正式三事（244 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-158](https://github.com/bitcoin/bips/blob/master/bip-0158.mediawiki)（Deployed, Peer Services；依赖 157）。  
**对应**：[`../tracks/light-clients/worked-example-bf158-notcomm-vs-bundled.md`](../tracks/light-clients/worked-example-bf158-notcomm-vs-bundled.md)。

- **排除了 OP_RETURN 不是已经有共识承诺：看见排除了 OP_RETURN，不是已经有共识承诺 interchangeable / 1282 bf158-notcomm interchangeable。**
- **服务位 不是已经在答别的过滤器类型：看见服务位，不是已经在答别的过滤器类型 interchangeable / 1282 bf158-notcomm interchangeable。**
- **排除了 OP_RETURN 不是已经写了 157 那套头链：看见排除了 OP_RETURN，不是已经写了 157 那套头链 interchangeable / 1282 bf158-notcomm interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看基本过滤器内容 / 假阳性 正式三事（244 余量），必须分开 not already have-tx、not already in-set、not already consensus 三件事。
