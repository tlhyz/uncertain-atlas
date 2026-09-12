# 工作实例：AVS 罚没不是已经 Casper 罚没，也不必链上可证

> **事实 / 推断 / 建议** 已分开。
> 对照：[EigenLayer 滤网](../../protocols/eigenlayer/README.md)、[Babylon BTC 锁](worked-example-btc-lock-vs-commit.md)、[L7.3](../../courses/level-07-modular/L07-M03-shared-security.md)、[Casper 谓词](worked-example-casper-slashing.md)、[证据 ≠ slash](worked-example-evidence.md)、[leak ≠ slash](../finality/worked-example-inactivity-leak.md)。
> 主文献：[ELIP-002](https://github.com/eigenfoundation/ELIPs/blob/main/ELIPs/ELIP-002.md)、官方 [Slashing 概念页](https://docs.eigencloud.xyz/eigenlayer/concepts/slashing/slashing-concept)。资料层级是产品改进提案 + 官方文档，不是信标规范。不写 19 节。
> 本页钉 **restake ≠ 已经变成另一个信标最终**、**AVS 罚没 ≠ Casper / CometBFT 协议罚没**、**任何理由 ≠ 必须客观可归属**、**协议不提供否决**、**Unique Stake ≠ 已经被所有 AVS 同时可罚**。不抄 TVL、AVS 个数、延迟秒数、比例示例。

---

## 0. 先修

- [L7.3](../../courses/level-07-modular/L07-M03-shared-security.md) 共享安全
- [不变量 21](../../libraries/invariants/README.md) 证据形状 ≠ 已 slash
- [不变量 26](../../libraries/invariants/README.md) Casper 两票谓词
- [不变量 140](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见「restake」或看见「也被罚了」，以为这份 ETH 已经变成另一条信标链的最终性，或以为 AVS 罚没和 Casper surround / CometBFT 双签证据是同一把尺子，或以为协议会替你否决乱罚。

官方句（事实）：

- 滤网已钉：restake 把**已经**为以太坊质押的 ETH 或 LST，再声明为 AVS 的可罚没抵押。不是在 EigenLayer 里另铸一份与信标无关的「以太坊质押」。
- 文档**没有**声称 restake 让你变成另一个信标最终确定，也没有声称轻客户端可以只看 restake 状态就验证信标头。以太坊共识仍由信标链验证者跑。
- ELIP-002：协议提供「最大灵活」的罚没函数。AVS 可对其任一 Operator Set 里的 Operator **以任何理由**罚没。罚没**不必**客观可归属（官方括注：链上可证）。
- 官方概念页重复同一句：AVS 可按任何理由设计罚没；不必链上可证。Operator 必须先自己看懂该 AVS 的条件；一旦委托，资金可按该 AVS 的条件被罚。
- ELIP-002：AVS 自己可以加延迟或否决窗，用来挡实现 bug / 误罚 / 欺诈。**EigenLayer 协议不提供否决。**
- Unique Stake：某一时刻，一份可罚抵押只能分给**一个** AVS。一个 AVS 罚了，不碰其他 AVS 的 Unique Stake。第一版模型曾让 Operator 选中的全部 AVS 都能罚同一份委托——那是旧对象，不是本页现行 Unique Stake。
- 只有 Unique Stake 可被 AVS 罚。它是 Operator 从 Staker 那里拿到的委托的比例，按 Operator Set 记账。
- Operator Set 是协议里的 `(avs, operatorSetId)`。AVS 可按自己的理由切分 Operator，并给集合派「任务」。任务可以是计算、验证明、聚合签名、活性探测，或完全自创。本页不把任务清单写成结算语义。
- 新存款 / 新委托立刻按同一比例可罚。官方写没有 activation delay。取出与解除委托在排队期内仍可罚——延迟数字不抄。
- 后到的 Redistributable Slashing、Slash Resolution Delay 是另几份 ELIP。本页不把它们写成已经解释了 002。

restake 声明、Unique Stake 分配、AVS 自定罚没、Casper 两票谓词、信标最终，是不同对象。

---

## 2. 直觉（ELI15）

你已经把押金放在学校总务处：以太坊质押。  
课外班再让你写一张「这份押金也给我当保证金」：restake。  
课外班自己定什么叫犯规，不必拿出全校都能验的监控录像：不必客观可归属。  
总务处**不会**替你否决课外班乱扣：协议不提供否决。  
这一张保证金一次只给一个课外班：Unique Stake。  
这不是你已经当上另一所学校的校长，也不是总务处那套「两张冲突的出席签」罚则。

小朋友看见「也被罚了」，以为和 Casper 是同一句话。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| Restake | 已有以太坊质押上的第二份可罚声明 | 新铸的信标质押；另一个信标最终 |
| AVS | 自己定义任务和罚没条件 | 自动继承 Casper surround / double |
| 最大灵活罚没 | 对集合内 Operator 可以任何理由罚 | 必须链上可证；协议会否决 |
| Unique Stake | 某一时刻只分给一个 AVS 的可罚比例 | 所有已选 AVS 同时能罚同一份 |
| Operator Set | `(avs, id)` 记账与罚没单位 | 信标验证者集合；CometBFT 投票权 |
| 协议否决 | **没有** | AVS 自己加的窗 = 协议已提供 |
| Casper 罚没 | 规范写明的两票关系 + 谁执行 | AVS 产品函数 |
| Babylon 锁 | Bitcoin 上的 UTXO + 脚本路径 | 本页的 ETH/LST 再声明 |

---

## 4. 最小案例

用户把已质押的 ETH 再声明给某个 AVS。

1. 信标最终性仍走 Gasper。不是已经多了一条信标。
2. Operator 把 Unique Stake 分给该 AVS 的一个 Operator Set。不是所有 AVS 都能罚这一份。
3. AVS 按自己的理由调用协议罚没函数。官方写不必链上可证。不是已经 Casper surround。
4. 用户等协议来否决。官方写协议不提供否决。
5. 另一个 AVS 的 Unique Stake 按官方句不被这次罚碰到。不是「一份 restake 被全世界一起罚」。
6. 有人把「共享安全」写成 Polkadot：那边押的是中继自己的 DOT，检查职责写在中继协议里。
7. 有人把「BTC 质押」写成同一句：Babylon 的锁还在 Bitcoin 脚本里（不变量 139）。

「restake 所以和以太坊罚没是同一把尺子」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | 信标签与 AVS 任务签不是同一域。本页不证配对或提取 |
| 协议 | 必须点名问的是 restake 声明、Unique Stake、AVS 自定罚，还是 Casper / 证据形状 |
| 实现 | ELIP 不是信标规范；合约接口会变 |
| 部署 | 谁当 AVS、有没有自己的否决窗，是部署事实 |
| 经济 | 同一份底层质押被第二份声明盯着；TVL 不是安全证明 |

**推断：** 产品句若只写「以太坊共享安全」，读者会把 AVS 任意理由听成 Casper 两票，或把 restake 听成轻客户端更硬。  
**建议：** 不确定第一版不要把「同一 ETH 同时服务任意 AVS」当默认模块。若对照，罚没必须点名证据形状和谁执行；不要抄「不必客观」当优点。不要抄 TVL。不要写 19 节。不要写怎样调用罚没函数。

---

## 6. 和另外几句不是同一句

1. **证据形状 ≠ 已 slash**（不变量 21）：CometBFT 双签证据上链，应用再决定罚不罚。本页是 AVS 产品函数，官方写不必链上可证。
2. **Casper 两票谓词**（不变量 26）：double / surround。本页没有这两条规范关系。
3. **leak ≠ slash**（不变量 130）：抽不跟多数走的质押。本页不是 inactivity leak。
4. **平行链共享安全**（不变量 125）：中继 DOT + 批准/可用性。本页押的是已有以太坊质押的再声明。
5. **BTC 锁 ≠ commit**（不变量 139）：UTXO 仍在 Bitcoin。本页不是那条锁。
6. **NPoS 等权**（不变量 129）：当选后共识等权。本页没有 Phragmén。

不要把 TVL、AVS 个数、取出延迟、比例 wad、官网收益抄进不确定常量。不要写怎样点名 Operator 去罚。不编博物馆页。不写 19 节。Redistributable / Resolution Delay 标成另一对象。

---

## 7. 「不确定」测试句（建议）

```text
restake ≠ 已经变成另一个信标最终
AVS 罚没 ≠ Casper / CometBFT 协议罚没
任何理由 ≠ 必须客观可归属 / 链上可证
AVS 自己的否决窗 ≠ 协议已经提供否决
Unique Stake ≠ 已被所有已选 AVS 同时可罚
一个 AVS 罚了 ≠ 其他 AVS 的 Unique Stake 已被碰
轻客户端只看 restake ≠ 已经能验信标头
```

语料：[C144](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「EigenLayer = 以太坊共享安全。」「AVS 罚没 = Casper 罚没。」「restake 之后轻客户端更安全。」「协议会否决乱罚。」「一份 restake 被所有 AVS 同时盯。」  
**边界：** 不讲合约调用、不填 TVL / 延迟数字。不把 ELIP 写成信标规范。不写 19 节。不写怎样罚。后到 ELIP 另标。
