# 反模式：H 的 validator_updates 被写成 H+1 立刻计票

> **事实 / 推断 / 建议** 已分开。
> 真值：[集合延迟](../../tracks/consensus/worked-example-validator-delay.md)、[ABCI++ FinalizeBlock](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md)、[不变式 35](../invariants/README.md#35-集合更新必须写出哪一高度改哪一个哈希)。

---

## 一句话

看见应用在高度 H 返回了验证者更新，就写成「下一高度按新集合投票」，不指出 H+1 只更新 `NextValidatorsHash`，H+2 才改 `ValidatorsHash`。

---

## 它看起来像什么

- 「EndBlock 换人，马上用新人凑 2/3」
- 「头里已经有新 Next，所以新人在投」
- 「参数更新和集合更新一起生效」

---

## 事实

- 处理 H 返回的 `validator_updates` 在块 **H+2** 生效。
- H+1：`NextValidatorsHash`；H+2：新集合计票；H+3：`*_last_commit` 带新集合。
- `consensus_param_updates` 是 H→H+1，另一条。

---

## 正确写法

| 高度 | 能说的句子 |
|------|------------|
| H | 「应用决定了以后的集合更新」 |
| H+1 | 「头承诺了下一集合哈希；本高仍按旧表投」 |
| H+2 | 「新集合开始计票」 |

---

## 对不确定的意义（建议）

轮换后量子验证者钥必须能指出这三格。缺「哪一高计票」的「换钥」，这条就红。
