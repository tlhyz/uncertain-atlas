# 反模式：把 Policy higher-fee not already more-correct / not already 245 / not already 44 正式三事（144 余量） 写成已经 已经更正确 / 已经是不变量 245 / 已经是不变量 44

**层次**：实现 / Policy higher-fee not already more-correct / not already 245 / not already 44 正式三事（144 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin Core [Policy](https://github.com/bitcoin/bitcoin/blob/master/doc/policy/README.md)（Transaction Relay Policy；官方节点文档，不是冻结共识规范）。  
**对应**：[`../tracks/mempool/worked-example-polc-notfee-vs-bundled.md`](../tracks/mempool/worked-example-polc-notfee-vs-bundled.md)。

把 Policy higher-fee not already more-correct / not already 245 / not already 44 正式三事（144 余量） 写成已经 已经更正确 / 已经是不变量 245 / 已经是不变量 44，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Policy policy 正式三事（144 余量），必须分开 not already consensus-illegal、not already in-block、not already more-correct 三件事，不要和 144 / 245 / 44 / 1521 / 1522 糊成一句。

也不是：

- [polc-notill-sold-as-bundled](polc-notill-sold-as-bundled.md) 是 notill 单句边界（1521），不是本页边界。
- [polc-notblk-sold-as-bundled](polc-notblk-sold-as-bundled.md) 是 notblk 单句边界（1522），不是本页边界。
- [asv-notchk-sold-as-bundled](asv-notchk-sold-as-bundled.md) 是 assumevalid 边界（25/1518），不是本页策略门边界。
