# 工作实例：单地址所有，不等于已经走快路径

> **事实 / 推断 / 建议** 已分开。
> 对照：[L6.2](../../courses/level-06-throughput/L06-M02-sui-ownership.md)、[L2.3](../../courses/level-02-state/README.md)、[Block-STM](worked-example-block-stm.md)、[Sui 档案](../../protocols/sui/report.md)、[停链面](../failure-museum/worked-example-halt-surfaces.md)。
> 主文献：Sui 官方 [Types of Object Ownership](https://docs.sui.io/concepts/object-ownership)、[Consensus](https://docs.sui.io/concepts/sui-architecture/consensus)。
> 本页钉 **owned ≠ fastpath**、**引用 shared ≠ 已授权**、**进了共识块 ≠ 已被接受**。不抄 epoch 小时、节点个数、Mysticeti 测试 TPS、轮数、秒数。

---

## 0. 先修

- [L2.3](../../courses/level-02-state/README.md) 对象与所有权
- [L6.2](../../courses/level-06-throughput/L06-M02-sui-ownership.md)
- [不变量 128](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比听见「Sui 的 owned 交易绕过共识」，或看见交易已经进某个验证者提出的共识块，以为已经结算，或以为点到 shared 对象就是自己有权改。

官方句（事实）：

- 每个对象都有所有者。所有权同时决定两件事：谁能在交易里用它，以及版本走 **fastpath** 还是走 **consensus**。
- 官方表把路径拆开。Address-owned：单个地址能用，版本走快路径，官方写无需共识。Shared：任何地址都能用，但要过 Move 检查，版本走共识。Immutable：只读，不再变版本。Wrapped：只能透过包装它的对象碰，路径跟包装走。
- 另有一行：**Consensus-address owned / party**。单个地址所有，但对象由共识排序。官方：想要单地址所有、又不要快路径锁、允许同一对象多笔在飞，就用 party。API 写成 `ConsensusAddressOwner`。
- 因此「属于一个地址」不是已经走快路径。Party 仍是一个人的东西，版本却走共识。
- Shared：任何人都能提交引用它的交易。运行时**不**按所有权挡。必须在 Move 里自己写授权（capability、`tx_context::sender()`、再验对象所有权）。**不要假定引用了 shared 就是调用者已授权。**
- 现行提交路径：客户端**不**自己拼证书，也**不**自己找法定人数说话。用户把签过的交易交给全节点；Transaction Driver 挑一个验证者送进去。该验证者验签、验输入存在且发送者能用、验气费够，然后放进自己下一份共识提案。邻居收到块再跑同一套检查。单独一个验证者收进双花，挡不住。
- 官方另写：**把带着某笔交易的块提交下来，单独不够让这笔生效。** 对等节点还要对块里的交易投票，协议只接受凑够接受票的交易。
- 执行要么成功并提交全部效果，要么 abort，除扣气费外无效果。
- Transaction Driver 再证明结算：从一个验证者拿到完整效果，再从其余人拿到同一效果摘要的法定人数确认。握着这些 certified effects 是结算最终的证明，此后不可逆。确认没到，就等交易出现在 certified checkpoint，那也是最终证明。

钱包绿勾、进了某验证者的提案块、owned、快路径、shared 引用、certified effects、certified checkpoint，是不同对象。

---

## 2. 直觉（ELI15）

书包里的笔通常是自己换、不用全班举手：快路径上的 address-owned。  
有人把笔登记成「还是我的，但全班按顺序发笔」：party。还是一个人的笔，已经要排队。  
黑板上的课表谁都能伸手去改：shared。伸手不是老师已经批准。  
课表草案钉在门口：进了某班长的提案块。全班还没点名接受。  
教务处盖了效果章，或等周报印发：两种官方承认的「已经归档」。

小朋友看见「这是我的笔」或「已经钉在门口」，以为全班已经举手，或以为谁碰到黑板都能改。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| Address-owned | 单个地址能用；表上版本走快路径 | 所有「一个人的东西」；已经最终 |
| Party / ConsensusAddressOwner | 单个地址所有，版本走共识 | 已经是快路径；已经是 shared |
| Shared | 谁都能引用，Move 自己做授权 | 引用者已经有权；已经快路径 |
| Immutable | 只读，不再变版本 | 可变 owned |
| Wrapped | 只能透过外层对象碰 | 自己有一条独立路径 |
| Fastpath | 官方写跳过共识的版本路径 | 所有 owned；现行提交仍由 Driver 代送 |
| 自己拼证书 / 自己找法定人数 | 旧叙述里的客户端动作 | 现行官方提交路径 |
| 共识块里带着这笔 | 某验证者提案被排序 | 这笔已经被接受；已经生效 |
| 接受票够 | 协议承认这笔 | 执行一定成功 |
| Abort | 除扣气外无效果 | 没花气费；没进过共识 |
| Certified effects | Driver 收集的效果摘要法定人数 | 已经等于 checkpoint；执行尚未 abort 过 |
| Certified checkpoint | 另一份官方最终证明 | 唯一一种最终 |

---

## 4. 最小案例

用户转一枚自己的硬币对象。

1. 对象若是 address-owned：官方表走快路径。若已被 party_transfer：仍是他的，但版本走共识。
2. 他把交易交给全节点。他自己不去收集验证者签名。
3. 某个验证者放进下一份共识块。邻居再验。块被提交，不等于这笔已被接受。
4. 接受票够了才执行。Move abort 则只扣气。
5. Driver 拿到效果 + 法定人数确认，或等到 certified checkpoint。这才是官方写的结算最终。

另一笔：用户引用一个 shared 池。谁都能送。没有 capability、没有 sender 检查，不是已经授权。

「Sui 所有交易都绕过共识」是假学习。「owned 所以已经快路径」也是。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | 对象能力不替代发送者签名 |
| 协议 | 所有权一行同时钉「谁能用」和「版本走哪条」；进块 ≠ 已接受；两种最终证明 |
| 实现 | Transaction Driver 代送；旧「客户端拼证书」不得写成现行必经 |
| 部署 | 全节点选哪个验证者送，是部署对象，不是已经法定人数 |
| 经济 | shared 热对象仍排队；Mysticeti 测试 TPS 不是生产事实 |

**推断：** 课文若只写 owned / shared 两行，读者会把 party 听成快路径，把「进块」听成已经结算。  
**建议：** 不确定第一版不要同时卖快路径、party、shared 三套「到了」。结算对象若是少数热账户，所有权广告帮不上。不要抄白皮书 TPS。

---

## 6. 和另外几句不是同一句

1. **STM 跑完 ≠ 已最终**（不变量 122）：Aptos 先有全序 L，再并行。本页是所有权决定要不要进那条序，以及进块还不够。
2. **估值 0 ≠ 已安全**（不变量 90）：shared 拥塞控制。本页是路径与授权，不是 assert。
3. **隔离拒证 ≠ 已分叉**（不变量 91）：检查点隔离。本页是 certified effects / checkpoint 两种最终证明，不是事故。
4. **取消 ≠ 已不扣款**（不变量 92）：abort 扣气的亲戚，对象是混合气费取消路径。
5. **head ≠ justified ≠ finalized**（不变量 127）：以太坊三等确认。本页是对象路径 + 接受票 + 两种最终证明。
6. **CheckTx ≠ 已进块**（不变量 33）：ABCI 四门。本页不是那四门。

不要把 epoch 小时、示例验证者个数、Mysticeti 测试 TPS / 秒数 / 轮数抄进不确定常量。官方自己写那些数字是受控测试，不是生产指标。也不要写怎样构造双花或怎样未授权改 shared。不编博物馆页。

---

## 7. 「不确定」测试句（建议）

```text
owned ≠ 已经走快路径
party / ConsensusAddressOwner ≠ 已经是快路径
引用 shared ≠ 已经授权
客户端自己拼证书 ≠ 现行官方提交
进了某验证者的共识块 ≠ 这笔已被接受
接受票够 ≠ 执行一定成功
abort ≠ 没扣气
certified effects ≠ 唯一最终证明
certified checkpoint 没到 ≠ 一定还没最终（可能 effects 已齐）
Mysticeti 测试 TPS ≠ 生产事实
Sui 所有交易绕过共识 ≠ 官方句
```

语料：[C132](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「Sui 所有交易都绕过共识。」「owned 就是快路径。」「引用 shared 就是有权。」「进共识块就是已经生效。」「客户端必须自己收齐验证者签。」「白皮书 TPS 就是主网。」  
**边界：** 不证 Mysticeti 论文、不填现行 epoch 秒数、不抄测试 TPS。Narwhal/Bullshark 旧名称只当历史。停机根因仍指博物馆四案，本页不重编。不写怎样未授权改 shared。
