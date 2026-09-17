# 反模式：任意两张签被写成可罚没

> **事实 / 推断 / 建议** 已分开。
> 真值：[Casper 罚没精读](../../tracks/economic/worked-example-casper-slashing.md)、[证据 ≠ 罚没](../../tracks/economic/worked-example-evidence.md)、[不变式 26](../invariants/README.md#26-可罚关系必须写成客观的两票谓词)。

---

## 一句话

看见两张验证者签名就写「双签、该罚」，不指出是同 epoch 两 data、包围、同 slot 两头，还是应用自己的公式。

---

## 它看起来像什么

- 「PoS 所以双签自动罚光」
- 把 CometBFT 证据上链写成已经 `slash_validator`
- 把 Altair 同步聚合签写成和 attestation 同一套 surround
- surround 两份证明放反，监视器报「协议不罚」

---

## 事实

- phase0：`is_slashable_attestation_data` 只有 double 与「1 包住 2」；`process_attester_slashing` 在信标状态里 `slash_validator`。
- 提议者：同 slot、同 index、不同 header。
- CometBFT：证据形状成立 ≠ 已罚没。
- 人还须 `activation_epoch <= now < withdrawable_epoch` 且尚未 slashed。

---

## 正确写法

| 关系 | 能说的句子 |
|------|------------|
| 同 target epoch，data 不同 | 「Casper double vote，信标应 slash 交集里仍可罚的人」 |
| attestation_1 包住 attestation_2 | 「Casper surround（注意顺序）」 |
| 同 slot 两头 | 「proposer slashing」 |
| 同高同轮同 Type 两 BlockID | 「DuplicateVoteEvidence 形状成立；罚不罚看应用」 |
| 同步委员会两张聚合 | 「不是 attestation 罚没条件」 |

---

## 对不确定的意义（建议）

先写谓词，再写执行人。缺谓词的「双签惩罚」四个字，这条就红。
