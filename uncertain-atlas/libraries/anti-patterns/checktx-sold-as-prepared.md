# 反模式：CheckTx 被写成已进提案 / 已执行，或 Process REJECT 被写成免费过滤

> **事实 / 推断 / 建议** 已分开。
> 真值：[Prepare / Process](../../tracks/consensus/worked-example-prepare-process.md)、[ABCI++ 基本概念](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_basic_concepts.md)、[不变式 33](../invariants/README.md#33-池预检提案改写提案验收提交执行必须分开)。

---

## 一句话

看见「CheckTx OK」或「应用验收了提案」，就写成「已经在块里 / 已经改余额 / 多验一次更安全」，不指出池、改写、验收、提交是四扇门。

---

## 它看起来像什么

- 「进池 = 本高度会出」
- 「Prepare 就是 PBS」
- 「Process 拒无效交易，没有坏处」
- 「Prepare 里执行过，状态已经换了」

---

## 事实

- `CheckTx` 只决定本节点池。从提案删掉一笔，池里可能还在。
- `PrepareProposal` 可以改序/增/删，且可以不确定；返回字节不得超过本次 `max_tx_bytes`。
- `ProcessProposal` 不能改列表；REJECT 走 prevote `nil`。诚实准备的提案，诚实 Process 必须 Accept。
- 立即执行只许候选状态；`FinalizeBlock` + `Commit` 才替换 `s_{h-1}`。

---

## 正确写法

| 路径 | 能说的句子 |
|------|------------|
| CheckTx OK | 「此刻这台节点的池愿意收」 |
| Prepare 改列表 | 「本轮提议者的应用写了（或改了）提案列表」 |
| Process REJECT | 「本验证者将对该提案 prevote nil；这伤活性」 |
| Finalize+Commit | 「该高度已决定，应用状态按列表更新」 |

---

## 对不确定的意义（建议）

产品「已发送」不得跳过四门直接写成结算。缺「哪一扇门」的 ABCI 口号，这条就红。
