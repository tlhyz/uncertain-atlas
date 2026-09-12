# 工作实例：策略拒绝不是共识非法，费率高不是更正确，策略不作用于块内交易

> **事实 / 推断 / 建议** 已分开。
> 对照：[L3.2](../../courses/level-03-bitcoin/L03-M02-fees-and-standardness.md)、[Bitcoin 档案](../../protocols/bitcoin/README.md)、[入池拒绝代价](../failure-museum/cve-2025-46598.md)、[筐里有信](worked-example.md)、[谓词 ≠ 脚本](../parallelism/worked-example-utxo-access-list.md)。
> 主文献：Bitcoin Core [Transaction Relay Policy](https://github.com/bitcoin/bitcoin/blob/master/doc/policy/README.md)；[Fee and Size Terminology](https://github.com/bitcoin/bitcoin/blob/master/doc/policy/mempool-terminology.md) 只钉 base fee = 输入和 − 输出和。资料层级是官方节点文档，不是冻结共识规范。不另写 19 节。
> 本页钉 **策略拒绝 ≠ 共识非法**、**策略通过 ≠ 已经进块**、**费率高 ≠ 更正确**、**策略不作用于块内交易**。不抄费率、灰尘、祖先条数、簇上限。

---

## 0. 先修

- [L3.2](../../courses/level-03-bitcoin/L03-M02-fees-and-standardness.md) 费用与标准性
- [L9.2](../../courses/level-09-systems/L09-M02-mempool.md) 内存池
- [不变量 44](../../libraries/invariants/README.md) 入池拒绝不是免费
- [不变量 144](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见邻居不转发，或看见钱包写「失败」，以为链已经判死刑；或看见费率高，以为交易更正确；或看见进了自己的 mempool，以为已经进块。

官方句（事实）：

- Bitcoin Core `doc/policy/README.md`：**Policy**（Mempool 或 Transaction Relay Policy）是节点在**共识之外**、对**未确认**交易进 mempool **之前**再执行的验证规则。
- 这些规则是**本地的**、**可配置的**（见 `-help` 的 Node relay options）。
- 策略可限制：交易本身、交易相对当前 tip、交易相对本节点 mempool 内容。
- **Policy is not applied to transactions in blocks.** 策略不作用于块内交易。
- 该文档声明：这不是穷尽清单。
- terminology 页：一笔交易的 **base fee** 是输入值与输出值之差。**modified fee** 是 base fee 加上 `prioritisetransaction` 的 fee delta；那是本节点出块用的本地增量，不是共识正确性。
- 官方页**没有**把策略拒绝写成共识非法，也没有把费率写成正确性，也没有把策略写成已经检查过块内交易。

策略门、共识门、费率、本节点 mempool，是不同对象。

---

## 2. 直觉（ELI15）

门口保安有一本自己的手册：今天哪些货不进院子。  
法官只看法律：格式对、没双花、脚本过，就能进合法块。  
保安拒你，不是法官已经判刑。保安放行，不是货已经装上车。  
多付钱买的是卡车位子，不是「这箱货更合法」。

小朋友看见「没广播出去」，以为链拒绝了。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| 策略 / policy | 未确认交易进本节点 mempool 之前、共识之外的本地规则 | 共识非法；已经作用于块内交易 |
| 共识规则 | 验块时全节点必须一致 | 本节点肯不肯转发 |
| base fee | 输入和 − 输出和 | 正确性；已经进块 |
| modified fee | base fee + 本节点 `prioritisetransaction` 增量 | 全网同一把尺；共识正确性 |
| 本节点 mempool | 本地未确认筐 | 全网共享池；已经 canonical |
| 费率 | 块空间拍卖 | 脚本更对；更最终 |

---

## 4. 最小案例

一笔共识合法、本节点策略嫌费低或不标准的交易。

1. 邻居按本地策略不进池、不转发。官方：策略是本地的。不是共识已经非法。
2. 另一台节点策略更松，或矿工直接看见，打进下一块。官方：策略不作用于块内交易。进块之后全节点只跑共识。
3. 钱包先显示「失败」，块出来又显示「成功」。三种故事：策略、共识、用户层。
4. 有人把高费率听成「更正确」。terminology：fee 是输入减输出。正确性在脚本与无双花，不在费率。
5. 有人把「进了我的 mempool」听成已经进块。官方：策略只管未确认、进池之前。
6. 这和入池拒绝必须记代价（不变量 44）不是同一句：那句管 DoS 配额，本页管两扇门。

「邻居不转发所以链拒绝了」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | 策略不验更多数学，只过滤继电器 |
| 协议 | 必须点名问的是策略、共识、费率还是本节点筐 |
| 实现 | 各节点一份可配置手册；policy 分叉不裂共识 |
| 部署 | `-help` 的 Node relay options 是部署旋钮，不是规范常量 |
| 经济 | 费率买空间，不是正确性 |

**推断：** 产品句若只写「交易被拒绝」，读者会把保安手册听成法官。  
**建议：** 不确定第一版必须把本地错 / 池拒绝 / 共识非法三套文案分开。不要抄默认费率。不要写怎样把非标准塞进块或怎样 RBF 钉死。

---

## 6. 和另外几句不是同一句

1. **入池拒绝不是免费**（不变量 44）：非标准 / CheckTx 拒了仍连着，必须记验代价。本页是门的种类，不是配额。
2. **IBD 跳脚本**（不变量 25）：同步加速跳过的是哪条规则。本页不是 assumevalid。
3. **洪水 ≠ 停链**（不变量 89）：入站数字不是停链谓词。本页是策略门。
4. **谓词 ≠ 脚本**（不变量 143）：Fuel 生命周期。本页是 Bitcoin 策略/共识两扇门。
5. **筐里有信 ≠ 局长盖章**（mempool 精读）：未确认 ≠ 已出块。本页再钉策略不作用于块。

不要把默认费率、灰尘、祖先条数、簇上限抄进不确定常量。不要写怎样绕策略或怎样 RBF。不编博物馆页。不另写 19 节。RBF 细则见 [`worked-example-rbf-signal-vs-replaced.md`](worked-example-rbf-signal-vs-replaced.md)（不变量 166）。package relay、cluster 线性化标成另一对象。

---

## 7. 「不确定」测试句（建议）

```text
策略拒绝 ≠ 共识非法
策略通过 ≠ 已经进块
费率高 ≠ 更正确
策略不作用于块内交易
本节点 mempool ≠ 全网共享池
modified fee ≠ 共识正确性
```

语料：[C148](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「标准性 = 共识规则。」「邻居不转发 = 链拒绝。」「费率高所以更正确。」「进了 mempool = 已经进块。」  
**边界：** 不讲某一版 Bitcoin Core 的默认费率表。不填簇上限。不把 cluster mempool 设计笔记当共识规范。不另写 19 节。不写怎样绕策略。RBF / package / cluster 线性化另标。
