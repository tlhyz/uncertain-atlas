# 反模式：投票扩展被写成块规则，或本高度 Finalize 的输入

> **事实 / 推断 / 建议** 已分开。
> 真值：[扩展精读](../../tracks/consensus/worked-example-vote-extension.md)、[ABCI++ 应用要求 Req 6–10](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)、[不变式 34](../invariants/README.md#34-扩展验收失败丢掉整张-precommit且本高度状态不得依赖本高度收到的扩展)。亲戚：[extension-path-sold-as-checked](extension-path-sold-as-checked.md)（快路径跳过下标检查）。

---

## 一句话

看见 precommit 上挂了应用字节，就写成「又验了一次块」或「Finalize 按这些字节改余额」，不指出验失败丢掉的是那张票，且 `s_h` 不得依赖本高度收到的扩展。

---

## 它看起来像什么

- 「扩展没过所以共识判块无效」
- 「本高度 Apply 读 vote extension」
- 「扩展和 prevote 是同一份签」
- 「空扩展可以跳过 Verify」

---

## 事实

- `ExtendVote` 只挂非空 precommit；`CanonicalVoteExtension` 是另一套被签对象。
- `VerifyVoteExtension` REJECT 丢整张 Precommit，不是改块规则。
- Req 10：`s_h` 不依赖本高度收到的 *e*。扩展最早进 *h+1* 的 Prepare。
- 空扩展仍验签。诚实扩展必须被诚实 Verify 接受。

---

## 正确写法

| 路径 | 能说的句子 |
|------|------------|
| 扩展被拒 | 「这张 precommit 被丢掉；块规则没变」 |
| 用扩展 | 「下一高度提议者可在 Prepare 里看见上一高度的扩展」 |
| Finalize | 「本高度状态只依赖上一状态与已决定块」 |

---

## 对不确定的意义（建议）

第一版可以不启用扩展。启用则必须能背 Req 10。缺这句的「应用投票」，这条就红。
