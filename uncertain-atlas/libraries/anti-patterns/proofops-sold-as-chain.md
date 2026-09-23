# 反模式：proofops-sold-as-chain

**层次**：实现 / ProofOps 链。  
**分类**：反模式（会把三件事写成一件）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ProofOps。  
**例**：[ProofOps.ops 是多条证明 ≠ 已经串上了](../../tracks/implementation/worked-example-proofops-vs-chain.md)。

## 病症

把「`ProofOps.ops` 里有多条证明」写成这几条已经按前一条的根接上了下一条，或写成各条 `type` 相同就等于同一棵树、同一套编码，或写成中间某一条的根对上就等于整链已经对上、可以停。

## 为什么错

规范写的是：`ops` 是一串**成链**的默克尔证明，可能类型不同；一条 op 的默克尔根是**下一条** op 里正在被证明的值；**最后一条** op 的默克尔根才该等于正在核对的最终根哈希。列出多条、名字相同、前几条绿，都不是整链对上。

## 正确写法

分开三句：ProofOps.ops 是多条证明不是已经串上了；各条的 type 可以不同不是已经是同一棵树；最后一条的根才该对上待验根不是已经对了中间某一条。

## 边界

不是 [queryproof-sold-as-apphash](queryproof-sold-as-apphash.md)（那是 Query 回了 Proof 就已经对上 AppHash，不变量 325），不是 [proofop-sold-as-key](proofop-sold-as-key.md)（那是 `ProofOp.key` 不是 Query 回包键、`ProofOp.data` 不是 proof_ops，不变量 390），不是 [proof-ok-equals-no-inflation](proof-ok-equals-no-inflation.md)（那是验证明 ≠ 供给，不变量 13）。看见写了自描述 `type` 不是已经是 `ProofOp` 类型，那是不变量 405。

## 本页不抄

- 怎样编 `ProofOps` 链、怎样种多层树、怎样挑 `type`。
- 怎样写利用步骤。
