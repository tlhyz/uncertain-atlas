# 实例：空 ctx 的投票签，被用户路径当真

目的 B。不是考试。  
先修：L1.2、域分离精读、[`fips-context.md`](fips-context.md)。

---

## 故事

规范写了「用户交易和 prevote 都用 ML-DSA-65」。实现调用库的默认外部 API，`ctx = ""`。  
阿安作为验证者，对高度 50 的块哈希签了 prevote。消息 `M` 若也只是「这块的哈希」、没有 `type`，则：

`M' = 0x00 ∥ 0x00 ∥ <块哈希>`

用户转账路径若接受「把块哈希当金额承诺」或另一条路径把同一 `M` 送进 `Verify(pk, M, σ, ctx="")`，验签为真。  
FIPS 的空默认帮了倒忙：算法层没有反对，协议层没写角色。

若投票 `ctx = "uncertain/vote/v1"`，用户 `ctx = "uncertain/tx/v1"`，同一 `M` 也不会在另一条 `Verify` 上为真。

**层：** 协议（角色没进 `ctx`/`M`）+ 实现（走了默认空串或 internal API）。密码学假设可以仍然成立。

---

## 和隔壁精读的关系

| 页 | 钉子 |
|---|---|
| `tracks/crypto/worked-example-domain.md` | `M` 里要有 chain / type |
| 本页 | 即使 `M` 暂时含糊，FIPS `ctx` 也必须按角色非空且不同 |
| `stateful-hbs.md` | 有状态方案没有这套 255 字节外部 `ctx`；别混 |

两层都做。只做一层，另一层的实现一改（internal、pre-hash、剥前缀）就会穿。

---

## 对「不确定」

C20：同一 pk、同一 `M`、两个角色的 `Verify`，必须一对真一对假。  
空 `ctx` + 空 `type` 不得当 PASS。
