# 反模式：把 Policy policy-pass not already in-block / not already 25 / not already 166 正式三事（144 余量） 写成已经 已经进块 / 已经是不变量 25 / 已经是不变量 166

**层次**：实现 / Policy policy-pass not already in-block / not already 25 / not already 166 正式三事（144 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin Core [Policy](https://github.com/bitcoin/bitcoin/blob/master/doc/policy/README.md)（Transaction Relay Policy；官方节点文档，不是冻结共识规范）。  
**对应**：[`../tracks/mempool/worked-example-polc-notblk-vs-bundled.md`](../tracks/mempool/worked-example-polc-notblk-vs-bundled.md)。

把 Policy policy-pass not already in-block / not already 25 / not already 166 正式三事（144 余量） 写成已经 已经进块 / 已经是不变量 25 / 已经是不变量 166，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Policy policy 正式三事（144 余量），必须分开 not already consensus-illegal、not already in-block、not already more-correct 三件事，不要和 144 / 25 / 166 / 1521 / 1523 糊成一句。

也不是：

- [polc-notill-sold-as-bundled](polc-notill-sold-as-bundled.md) 是 notill 单句边界（1521），不是本页边界。
- [polc-notfee-sold-as-bundled](polc-notfee-sold-as-bundled.md) 是 notfee 单句边界（1523），不是本页边界。
- [asv-notchk-sold-as-bundled](asv-notchk-sold-as-bundled.md) 是 assumevalid 边界（25/1518），不是本页策略门边界。
