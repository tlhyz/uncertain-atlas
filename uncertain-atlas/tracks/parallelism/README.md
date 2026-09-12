# 横向地图：并行

并行首先来自冲突变少（L2.4），不是品牌名。

| 世界观 | 冲突何时可见 | 没有全局顺序时 | 热点形状 | 课 |
|---|---|---|---|---|
| 默认账户/EVM | 执行时 | 不能安全并行 | 热合约单行道 | L2.2 L5.1 |
| 声明锁 | 调度前 | 不调度漏列交易 | 本地费/本地队 | L6.1 |
| 对象所有权 | 类型/对象图 | address-owned 可走快路径；party 仍排队（须单独论证） | shared 回全序 | L6.2 / [精读](worked-example-owned-vs-fastpath.md) |
| 乐观 STM | 执行后校验 | **禁止**：必须有序列 L | 回滚风暴 | L6.3；[工作实例](worked-example-block-stm.md) |
| UTXO | 输入不交则可 | 仍要 canonical 历史 | 热输出少见、热合约仍难 | L2.1 |
| eUTXO | 整笔校验；共享 datum 输出仍抢 | 同 UTXO | 共享脚本 UTXO 单行道 | L2.5 |
| UTXO+声明调度 | 调度前 | 必须有序 L | 合约 UTXO 热点 | Fuel 档案 / [精读](worked-example-utxo-access-list.md) |
| Cell + deps | 输入花费 / deps 只读 | 仍要 canonical 历史 | 热 Cell 单行道 | Nervos / L2.6 |
| 分片账户（Nightshade） | 分片内执行时 | 跨分片靠收据，不是无序 | 热账户挤在同一分片则单行道 | `protocols/near/` |

五笔账（任何高吞吐声称都要拆）：状态 / 执行 / 网络 / 协议 / 硬件。占用压的是存储账，不是并行账。

Block-STM 精读：[`worked-example-block-stm.md`](worked-example-block-stm.md)（不变量 122）。提交 ≡ 串行 L。STM 跑完不是已经最终。不抄加速比。  
Quorum Store 精读：[`../consensus/worked-example-quorum-store-vs-order.md`](../consensus/worked-example-quorum-store-vs-order.md)（不变量 132）。批次传播不是已经写出 L。已认证批次不是已经排序。  
所有权路径精读：[`worked-example-owned-vs-fastpath.md`](worked-example-owned-vs-fastpath.md)（不变量 128）。owned 不是已经快路径。引用 shared 不是已经授权。进共识块不是已被接受。不抄测试 TPS。  
Fuel 访问集精读：[`worked-example-utxo-access-list.md`](worked-example-utxo-access-list.md)（不变量 143）。谓词通过不是脚本已经跑完。只读重叠不是写冲突。写集相交不是可以并行。并行验证不是已经不需要顺序 L。不抄上限或官网 TPS。
