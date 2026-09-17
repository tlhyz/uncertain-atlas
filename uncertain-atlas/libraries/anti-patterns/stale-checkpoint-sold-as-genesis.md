# 反模式：过期检查点被写成「和从创世一样」

> **事实 / 推断 / 建议** 已分开。
> 真值：[弱主观性精读](../../tracks/finality/worked-example-weak-subjectivity.md)、[CometBFT 信任期](../../tracks/light-clients/worked-example-bft-skip.md)、[不变式 24](../invariants/README.md#24-检查点同步必须落在弱主观或信任期内)。

---

## 一句话

节点 / 钱包从一份检查点起步，文案写成「全节点级安全」或「PoS 已最终所以和从创世重放一样」，却不检查这份检查点对新不新。

---

## 它看起来像什么

- 「这是质押链，没有弱主观性」
- 内置六个月前的 checkpoint，启动不跑 `is_within_weak_subjectivity_period`
- 检查点对不上 canonical 只弹黄条，进程继续
- 把规范参考表的人数当成「今天的以太坊」

---

## 为什么有人会这么写

`finalized` 三个字听起来像 Bitcoin 确认加到无穷。弱主观性讲的是**集合换血之后旧钥匙还在**，不是「最终确定会自己撤销」。

---

## 事实

- Ethereum：任何 `Checkpoint` 都能当 WS 检查点；周期由 `compute_weak_subjectivity_period` 算出，下限含 `MIN_VALIDATOR_WITHDRAWABILITY_DELAY = 256` epoch；对不上路径则应致命退出。分发节规范写未完成。
- CometBFT：`trustingPeriod < unbondingPeriod`；信任期外不得把旧集合当轻客户端信任锚。
- 两套都是经济牙 + 时间窗，不是「签名算法自己会过期」。

---

## 正确写法

| 你做了什么 | 能说的句子 |
|------------|------------|
| 从创世按规则复算到现在 | 「我复算了这段历史」（仍有实现/日蚀假设） |
| 从**未过期**检查点同步且路径命中 | 「我接受了这份检查点，并验证它仍在期内、在链上」 |
| 检查点过期或对不上 | 不得显示「已验证」；Ethereum 规范要退出 |

---

## 对不确定的意义（建议）

提供检查点同步就把新鲜度写进产品句。缺时间窗还写「和全节点一样」，这条就红。
