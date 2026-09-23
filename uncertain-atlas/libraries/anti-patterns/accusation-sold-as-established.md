# 反模式：accusation-sold-as-established

**层次**：实现 / 证据指控栏。  
**分类**：反模式（会把三件事写成一件）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) LightClientAttackEvidence 与 [Light Client Accountability](https://github.com/cometbft/cometbft/blob/main/spec/light-client/accountability/README.md)。  
**例**：[Byzantine Validators 是过错名单 ≠ 已经成立](../../tracks/implementation/worked-example-byzantine-vs-accusation.md)。

## 病症

把 `Byzantine Validators` 名单上有某个人写成此人作恶已经成立、已经能罚；或把校验栏里的 `Read Below` 当成「下文已给出定义」；或只按 `data_structures.md` 摘要的「三种攻击穷尽」就去写证据校验，而不去问责文逐条读。

## 为什么错

官方把该字段写成「acted maliciously 的验证者」——那是**主张**，成立与否看下文那套；同一张表里三个字段的说明或校验直接写 `Read Below`，那是指针不是内容；而 `data_structures.md` 摘要断言三类**穷尽**的同时，把详情指向问责文，问责文里却还有 **phantom validators**（不在当前集合、但仍在解绑期内仍可签名的人），并对是否单列留了一个 **Q** 开放问题。只看摘要会漏掉那一类。

## 正确写法

分开三句：Byzantine Validators 是过错名单不是已经成立；`Read Below` 不是已经给出了定义；摘要说三种穷尽不是已经验完。实现须读问责文，phantom validator 当待决问题。

## 边界

不是 [evidencefields-sold-as-selfcertified](evidencefields-sold-as-selfcertified.md)（那是证据里的票权与时间不是自带权威，不变量 443），不是 [lightblock-sold-as-both-present](lightblock-sold-as-both-present.md)（那是两件都在不是已经是同一高，不变量 445），不是 [evidence-equals-slash](evidence-equals-slash.md)（那是上链不是已经罚没，不变量 21），不是朝前 lunatic 形不成证据（不变量 66）。

## 本页不抄

- 怎样构造 `LightClientAttackEvidence`、怎样算 `CommonHeight`、怎样挑指控名单。
- 怎样写利用步骤。
