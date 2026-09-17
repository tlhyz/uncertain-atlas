# QRL · 过滤器页（19 节未写）

优先级：进阶候选（后量子主线）。  
本页只做独特思想过滤器。不写官网 TPS，不写 Zond / EVM 测试网营销。

## 过滤器

> 它提供了什么 Bitcoin / CometBFT / Ethereum / 已有档案 **很少同时具备**的思想？

**答得出：** 用户授权用 **XMSS（有状态哈希签名）**，地址是一棵高度在创建时选定的树；默认高度 10 ⇒ 1024 个出站 OTS index；**入账不消耗** index；官方文档写明：**节点拒绝重复 OTS index**。见 [QRL Docs · One Time Signature Keys](https://docs.theqrl.org/build/fundamentals/ots-keys)。

这与「以后再迁到 PQ」「白皮书写量子安全但仍用 secp256k1」不是同一对象。  
规范底本是 [RFC 8391](https://www.rfc-editor.org/rfc/rfc8391.html)，轮廓见 [SP 800-208](https://csrc.nist.gov/pubs/sp/800/208/final)。QRL 选用的哈希/参数集**不必**等于 SP 800-208 批准子集；引用实现时要写清，禁止写成「NIST 认证了这条链」。

## 不是独特思想的部分

- 共识家族：公开材料按 PoW / 最重链教学，没有新的锁规则。不因此写 19 节。  
- 首页「工业级首次」：营销，不进档案第 1 节。  
- Zond / EVM：另一条产品线，过不了「很少同时具备」；本页忽略。

## 代价（先写）

1. 一地址出站次数封顶；用尽必须换地址并先把钱转走（官方文档原句结构）。  
2. 钱包崩溃若先漏出 σ 再丢掉 index，就是 OTS 复用（反模式 ots-index-reuse）。  
3. SP 800-208：有状态方案不适合通用使用；热钱包默认违反「高度受控的签名环境」。  
4. 树高越大，造钥/打开钱包越贵（官方文档承认）；这是实现/部署税，不是 TPS。

## 「不确定」四档（建议）

| 档 | |
|---|---|
| 强烈研究 | 协议层拒绝 `(pk, idx)` 复用；RFC「先更新再输出」。 |
| 可以参考 | 入账不耗 index；树高在创建时冻结。 |
| 暂时不需要 | 抄 QRL 地址编码、挖矿、生态。 |
| 不建议 | 把有状态 XMSS 当验证者投票签；把「QRL 还在跑」写成 PQ 已完成。 |

19 节未写。思想卡：[`../../tracks/post-quantum/stateful-hbs.md`](../../tracks/post-quantum/stateful-hbs.md)。
