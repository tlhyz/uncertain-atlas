# FIPS 外部 API 的 context string（不是选型）

目的 B。数字与编码只来自正式 FIPS。  
对照：消息前缀域分离见 [`../crypto/worked-example-domain.md`](../crypto/worked-example-domain.md)。两层都要，缺一层就假。

---

## 事实：算法自己带一层域

**FIPS 204**（2024-08）Algorithm 2 `ML-DSA.Sign(sk, M, ctx)`：

- `ctx` 是最多 **255** 字节的字节串。默认空串。超过 255 返回 ⊥。  
- 内部先构造  
  `M' ← BytesToBits( IntegerToBytes(0, 1) ∥ IntegerToBytes(|ctx|, 1) ∥ ctx ) ∥ M`  
  再交给 `Sign_internal`。即：一字节 `0x00` + 一字节长度 + `ctx` + 消息。  
- `Verify` 必须带**同一** `ctx`。

同文件还定义 **HashML-DSA**（先哈希再签）。FIPS 写：一般更推荐 **pure ML-DSA**；标识（如 OID）应标明是 pure 还是 pre-hash；同一密钥对虽可两用，**建议一把钥只用一种**。

**FIPS 205**（2024-08）§10.2 / Algorithm 22 `slh_sign(M, ctx, SK)`：

- `ctx` 同样最多 255 字节，默认空。  
- pure：`M' ← toByte(0, 1) ∥ toByte(|ctx|, 1) ∥ ctx ∥ M`。  
- 空 `ctx` 时，就是在消息前加两个 `0x00`。  
- 域分隔字节 `0` 的作用（原文）：防止 pre-hash 签被当成 pure 验证，反之亦然。  
- pre-hash（`hash_slh_sign`）用分隔字节 `1`，并拼 OID 与 `PH(M)`。同样建议一把钥只用一种版本。一般更推荐 pure。

**不是事实：** 「空 ctx 所以已经域分离。」空 ctx 只是标准默认，不是协议完成。

---

## 事实：同一 `(sk, M, ctx)` 可以有两个都真的 σ

FIPS 204 Algorithm 2 默认走 **hedged** 签：内部取随机 `rnd`。把 `rnd` 固定成全零才是确定性变体。标准更推荐 hedged。  
FIPS 205 的 `slh_sign` 同样允许 `opt_rand`（随机或改用公钥种子做确定性）。  
因此：同一私钥、同一 `M`、同一 `ctx`，两次 `Sign` 可以吐出**不同**的 σ，两次 `Verify` 都可以为真。

这不是「算法坏了」。协议若把「σ 字节必须唯一」写成授权唯一性，会把合法的第二次 hedged 签当成双花或 malleability 攻击。  
授权对象是 `(pk, M, ctx)`，不是 σ 的十六进制。Bitcoin 的 scriptSig malleability 是另一条历史（见 L3.7）；这里只钉 FIPS 默认就允许两份合法 σ。

**建议：** 共识去重看花费授权 / nonce / 高度，不看「这串 σ 以前见过没」。txid 不要把可变 σ 编进去当身份。

---

## 两层域，不要混成一层

| 层 | 钉在哪 | 挡不住什么 |
|---|---|---|
| 算法 `ctx` | FIPS 外部 API 的 255 字节槽 | 你自己规定的 `type=vote` 若从没写进 `ctx` 或 `M` |
| 消息前缀 | chain / type / version 进 `M` | 库若走 **internal** API，会跳过 `0x00‖len‖ctx` |

实现若调用 `Sign_internal` / `slh_sign_internal`，FIPS 的外部包装（含 `ctx`）不会自动发生。测试向量分 external / internal 正是这个缝。  
**建议：** 共识路径只走外部 API；`ctx` 写成规范常量，不让应用层「有时传、有时忘」。

---

## 对「不确定」（建议，不是选型）

1. 用户签与投票签：要么两把钥，要么同一把钥配**两个非空、互不相同的 `ctx`**（再加 `M` 里的 type）。两个角色都用空 `ctx` = 反模式。  
2. `ctx` 进规范，进不变量 18，进语料 C20。不要只写在钱包 README。  
3. 算法标签（不变量 11）还要能区分 ML-DSA / HashML-DSA、SLH-DSA / HashSLH-DSA。FIPS 自己要求 OID 标明版本。  
4. 不填 CPU，不选 44/65/87。

精读：[`worked-example-fips-ctx.md`](worked-example-fips-ctx.md)。
