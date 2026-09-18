# 模式：点名 bf158-nottx 杠

**层次**：轻客户端 / BIP-158 scripts not already have-tx / not already have-opreturn / not already spent 正式三事（244 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-158](https://github.com/bitcoin/bips/blob/master/bip-0158.mediawiki)（Deployed, Peer Services；依赖 157）。  
**对应**：[`../tracks/light-clients/worked-example-bf158-nottx-vs-bundled.md`](../tracks/light-clients/worked-example-bf158-nottx-vs-bundled.md)。

- **装了花费脚本和收款脚本 不是已经有那笔交易：看见装了花费脚本和收款脚本，不是已经有那笔交易 interchangeable / 1280 bf158-nottx interchangeable。**
- **对上了一个脚本 不是已经有附言数据：看见对上了一个脚本，不是已经有附言数据 interchangeable / 1280 bf158-nottx interchangeable。**
- **装了花费脚本和收款脚本 不是已经花掉：看见装了花费脚本和收款脚本，不是已经花掉 interchangeable / 1280 bf158-nottx interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看基本过滤器内容 / 假阳性 正式三事（244 余量），必须分开 not already have-tx、not already in-set、not already consensus 三件事。
