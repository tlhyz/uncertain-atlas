# Babylon · 过滤器页（19 节未写）

优先级：进阶候选。  
本页只做独特思想过滤器，**不**当 19 节档案。数字、委员会规模、奖励以现行模块为准，这里不抄。

## 过滤器

> 它提供了什么 Bitcoin / CometBFT / Ethereum / Polkadot / 乐观 rollup **很少同时具备**的思想？

**答得出（思想，不是营销）：** Bitcoin 上的 UTXO **继续留在 Bitcoin**。花费条件是 Taproot 脚本路径（时间锁取回 / 经契约委员会的提前解绑 / 惩罚路径），另一条链用**包含证明**登记这笔质押。官方模块说明写明：不是把 BTC wrap 到外链再质押。见 `babylonlabs-io/babylon` 的 `x/btcstaking/README.md` 与 `docs/staking-script.md`。

这与：

- Polkadot 共享安全（押的是中继自身的质押资产）  
- 桥接包装币再质押（资产已经离开 Bitcoin 脚本）  

不是同一对象。

## 代价（先写，再决定要不要 19 节）

1. **契约委员会（covenant）** 出现在解绑/惩罚路径里：这是额外的人集假设，不是「纯脚本自动罚」。  
2. Bitcoin 侧的「已包含」仍是 **Nakamoto 确认政策**（k-deep），不是 CometBFT commit。  
3. 惩罚依赖可提取的一次性签名等密码组件（EOTS，以规范/实现文档为准）。组件换代属于算法敏捷问题，本页不选型。  
4. 「给别的 PoS 链提供安全」是共享安全家族的新病：房东最终 ≠ 租户应用正确（L7.3）。

## 「不确定」四档（建议，本页即止）

| 档 | |
|---|---|
| 强烈研究 | 暂无。第一版结算机不靠外链 BTC 当质押。 |
| 可以参考 | 「抵押物仍是 Bitcoin UTXO + 包含证明」这句对象定义。 |
| 暂时不需要 | 契约委员会参数、多租户安全市场。 |
| 不建议 | 把「BTC 质押」写成「Bitcoin 共识保证了你的结算」。 |

精读：[`../../tracks/economic/worked-example-btc-lock-vs-commit.md`](../../tracks/economic/worked-example-btc-lock-vs-commit.md)（不变量 139）。k-deep 包含证明不是已经 commit。普通解绑是意图，不要求 k-deep。产品页「无需第三人」不是模块事实。

通过过滤器 ≠ 已经选型。要写 19 节时必须逐条对照 `staking-script.md` 三条路径，禁止用官网首页句填第 1 节。
