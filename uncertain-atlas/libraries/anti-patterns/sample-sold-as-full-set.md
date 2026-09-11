# 反模式：抽样超多数被写成全集合超多数

> **事实 / 推断 / 建议** 已分开。
> 真值：[Altair 同步委员会工作实例](../../tracks/light-clients/worked-example-sync-committee.md)、[CometBFT skip](../../tracks/light-clients/worked-example-bft-skip.md)、[不变式 20](../invariants/README.md#20-bft-轻客户端重叠旧集合)、[不变式 22](../invariants/README.md#22-轻客户端必须点名信任对象)。

---

## 一句话

协议里的分母是 **512 人委员会**（或任意固定抽样），文案写成「全网 2/3 已最终确定」。

---

## 它看起来像什么

- 「以太坊轻客户端用和全节点一样的 2/3 安全」
- 「同步委员会签名 = Casper 最终确定」
- 把 `MIN_SYNC_COMMITTEE_PARTICIPANTS = 1` 解释成「有人签就安全」
- 把乐观头（`get_safety_threshold`）当成不可逆

---

## 为什么有人会这么写

「2/3」三个字在 BFT 课和以太坊课里都出现。Altair 同步协议的超多数公式也是 `participants * 3 >= committee * 2`。不看 **committee 是谁**，两句话会糊成一句。

---

## 事实（稳定规范）

- `SYNC_COMMITTEE_SIZE = 512`（Altair 引入；`altair/beacon-chain.md` 写 `Uint64(2**9)`）。
- 同步协议超多数的分母是 **该委员会长度**，不是 `validator_count`。
- Casper FFG 最终确定仍在 **全体验证者** 的证明上；同步委员会 **不替代** FFG。
- [EIP-8390](https://eips.ethereum.org/EIPS/eip-8390) 是 **Draft**，主张去掉这套抽样轻客户端，并写明抽样安全 ≠ 全集合安全。草案 **未激活**。

---

## 正确写法

| 对象 | 分母 | 能得出的句子 |
|------|------|----------------|
| Casper 证明 | 全体活跃验证者（有效余额加权） | 「信标最终确定」 |
| 同步委员会更新 | 512 抽样 | 「抽样委员会超多数签了这个信标头」 |
| CometBFT 提交 | 当时验证者集合 | 「该高度被该集合 2/3 提交」 |
| CometBFT 轻跳跃 | 受信任 `NextValidators` 与新提交的重叠 | 「跳跃仍钉在我信任的下一集合上」 |

---

## 对不确定的意义（建议）

文档和钱包必须把分母写进标题。禁止「我们的轻客户端有 2/3 安全」这种不写集合的句子。
