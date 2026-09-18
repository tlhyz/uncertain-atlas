# 反模式：把 EIP-868 request not already parsed / not already signed-ok / not already verified 正式三事（241 余量） 写成已经 已经解析完 / 已经核过签名 / 已经验过是那个节点签的

**层次**：网络 / EIP-868 request not already parsed / not already signed-ok / not already verified 正式三事（241 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-868](https://eips.ethereum.org/EIPS/eip-868)（Final, Networking；依赖 8、778）。  
**对应**：[`../tracks/network/worked-example-enreq-notreq-vs-bundled.md`](../tracks/network/worked-example-enreq-notreq-vs-bundled.md)。

把 EIP-868 request not already parsed / not already signed-ok / not already verified 正式三事（241 余量） 写成已经 已经解析完 / 已经核过签名 / 已经验过是那个节点签的，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看发现要记录 / 交叉核对 正式三事（241 余量），必须分开 not already have、not already parsed、not already no-amp 三件事，不要和 241 / 240 / 235 / 1292 / 1294 糊成一句。

也不是：

- [enreq-notping-sold-as-bundled](enreq-notping-sold-as-bundled.md) 是 notping 单句边界（1292），不是本页边界。
- [enreq-notfind-sold-as-bundled](enreq-notfind-sold-as-bundled.md) 是 notfind 单句边界（1294），不是本页边界。
- [enr-notid-sold-as-bundled](enr-notid-sold-as-bundled.md) 是 EIP-778 默认方案仍未换发现协议边界（240/1291），不是本页发现要记录边界。
