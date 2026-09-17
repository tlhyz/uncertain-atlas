# 实例：三种「域」编码，不要混成一种

目的 A/B。不是考试。  
先修：L1.1、L1.2、[`worked-example-domain.md`](worked-example-domain.md)、[`../post-quantum/fips-context.md`](../post-quantum/fips-context.md)。

规范原文：

- [BIP-340](https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki) Tagged Hashes  
- [EIP-712](https://eips.ethereum.org/EIPS/eip-712) `domainSeparator`  
- FIPS 204 Algorithm 2 / FIPS 205 Algorithm 22（外部 `ctx`）

---

## 故事

阿安以为「我们用了 Schnorr / 用了 EIP-712 / 用了 ML-DSA，所以签不会串台」。  
三套编码钉的是**三层不同的钉子**。少一层，另外两层的实现一改就会穿。

---

## 事实：BIP-340 把标签焊进哈希

BIP-340 规定：

```text
hash_name(x) = SHA256( SHA256(tag) ‖ SHA256(tag) ‖ x )
tag = name 的 UTF-8
```

规范里用到的名字包括 `BIP0340/challenge`、`BIP0340/nonce`、`BIP0340/aux`。  
前缀是 **64 字节**（两个 SHA256 块），正好一块，实现可以改初始状态做同一哈希。

BIP 原文要挡的两件事：

1. 只把哈希参数换序的「另一个 Schnorr」，可能把 BIP-340 的签当成自己的签。  
2. 更糟：另一套方案抄了 nonce 派生却没用独特标签 → **nonce 复用 → 漏 sk**。这是密码/实现层，不是「跨链重放」那句话。

**挡不住：** `m` 本身如果只是块哈希、没有 `type=vote`，tagged hash 仍然只是「这是 BIP-340 的 challenge」，不是「这是投票不是转账」。

---

## 事实：EIP-712 把 dapp 域焊进钱包签

EIP-712 把可签对象从「交易 ∪ 字节串」扩成再加结构化数据 `𝕊`。三种编码**首字节不同**，所以单射：

| 对象 | 编码（规范原文形状） | 首字节 |
|---|---|---|
| 交易 | `RLP_encode(tx)` | 不是 `0x19` |
| 普通字节 | `"\x19Ethereum Signed Message:\n" ‖ 十进制长度 ‖ message` | `0x19` |
| 结构化 | `"\x19\x01" ‖ domainSeparator ‖ hashStruct(message)` | `0x19` 后接 `0x01` |

`domainSeparator = hashStruct(eip712Domain)`。规范列出可选用的域字段：`name`、`version`、`chainId`、`verifyingContract`、`salt`。只用其中有意义的字段。

规范自己写的边界（事实，不是贬损）：

- 同一条已签结构化消息出现两次，应用必须拒或做成幂等；**怎样做不在本标准范围**。  
- 广播与抢跑也不在本标准范围。

**不是事实：** 「用了 EIP-712 所以结算链不会重放。」它管的是钱包/合约的 typed data，不是 BFT 投票路径。

---

## 事实：FIPS `ctx` 是算法包装，不是哈希标签

FIPS 204/205 外部 API 在把 `M` 交给内部签之前，先拼 `0x00 ‖ |ctx| ‖ ctx`。  
这与 BIP-340 的 `SHA256(tag)‖SHA256(tag)`、EIP-712 的 `\x19\x01` **不是同一个函数**。  
空 `ctx` 是标准默认。见 [`../post-quantum/fips-context.md`](../post-quantum/fips-context.md)。

---

## 三层对照（不要合并成一句「域分离」）

| 编码 | 钉在哪一层 | 典型挡住 | 典型挡不住 |
|---|---|---|---|
| BIP-340 `hash_name` | 密码构造（challenge / nonce / aux） | 跨方案哈希重解释；nonce 派生撞车漏钥 | `m` 里没写角色 |
| EIP-191 / EIP-712 | 钱包与合约的 typed data | 聊天签变成 RLP 交易；跨 dapp（若域字段填全） | 共识投票；同一 typed 消息被执行两次（规范声明范围外） |
| 消息前缀 `chain‖type‖version` | 协议 | 投票字节当用户 tx | 库走 FIPS **internal** API，跳过 `ctx` |
| BFT SignBytes / CL `DomainType` | 协议（步类型） | Prevote 当 Precommit；attestation 当 proposer | `timestamp` 也在票里；σ 不是票身份 |
| FIPS 外部 `ctx` | 算法包装 | 同一 `M` 在另一角色 Verify 为假 | 两个角色都用空默认 |

**建议：** 「不确定」四层都写进规范：BIP 风格的构造标签（若沿用哈希构造）、协议消息前缀、FIPS `ctx`、钱包若签结构化数据再单独用 712 形状。缺一层就在审核里写「未钉」。

---

## 精密检查

**禁止假学习：** 「Schnorr 自带域分离。」「EIP-712 等于共识域分离。」「NIST 算法自带角色。」  
**边界：** 不抄 BIP-340 的曲线公式当本课作业；不把 712 的 JSON-RPC 示例当共识测试向量；不填 PQ CPU。
