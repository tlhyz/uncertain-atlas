# 实例：Prevote 的印，不能当 Precommit

目的 A/B。不是考试。  
先修：L4.2、L1.2、[`../crypto/worked-example-domain.md`](../crypto/worked-example-domain.md)、[`../crypto/worked-example-tagged-hash.md`](../crypto/worked-example-tagged-hash.md)。

规范原文：

- [CometBFT `spec/consensus/signing.md`](https://github.com/cometbft/cometbft/blob/main/spec/consensus/signing.md)  
- [CometBFT `spec/core/encoding.md`](https://github.com/cometbft/cometbft/blob/main/spec/core/encoding.md)（`CanonicalVote`）  
- [Ethereum consensus-specs phase0 · Domains / `compute_domain` / `compute_signing_root`](https://github.com/ethereum/consensus-specs/blob/master/specs/phase0/beacon-chain.md)

---

## 故事

阿安已经对高度 50、轮 0 的块哈希签了 **prevote**。实现若把同一串哈希再送进 **precommit** 的 Verify，或者把 Ethereum 的 attestation 域拿去验 proposer，验签为真就假了。  
两步不是「再盖一次同一枚印」。被签字节里必须有**角色**。

这与用户交易域分离是亲戚，但钉子更细：同一把验证者钥、同一高度，两步仍必须是两封信。

---

## 事实：CometBFT 把 type 和 chain_id 焊进 SignBytes

签名规范写明 `SignedMsgType`：

| 常量 | 值 |
|---|---|
| Prevote | `0x01` |
| Precommit | `0x02` |
| Proposal | `0x20` |

（数据结构文档的 protobuf 枚举是 1 / 2 / 32，同一组数。）

`SignBytes` 不是块里那条 Vote 的普通编码。编码规范：先重排字段，固定宽度的 type / height / round 在前，**chain_id 在末尾**，方便 HSM 按固定偏移读。形状：

```text
CanonicalVote {
  type, height, round, block_id, timestamp, chain_id
}
```

全体 canonical 消息还要 **length-prefix**。  
Verify 必须用**调用方提供的** `chain_id` 重算 `VoteSignBytes`，再对验证者公钥验。换一条链的 id，同一 σ 应为假。

投票有效当且仅当：type 是 prevote 或 precommit、height > 0、round ≥ 0、BlockID 要么空要么完整。  
Proposal 的 type 必须是 `0x20`，且 BlockID 必须完整。

**双签纪律（同一规范）：** 签名器要记住上次签过的 `(height, round, type)`。同一高度同一轮：签过 prevote 之后，只允许再签 precommit；签过 precommit 之后，**不得再签任何消息**（包括把 nil 改成完整 BlockID）。这是协议/部署层，不是「Ed25519 自己会记住」。

**挡不住：** `timestamp` 也在 SignBytes 里。同一 type / height / round / block 的两张票，时钟不同就是两封信。不要把 σ 字节当成「这一票的身份」。后量子 hedged 签会让同一封信也能吐出两个 σ（见 FIPS ctx 卡）。

---

## 事实：Ethereum CL 把 DomainType 焊进 signing root

phase0 规范表（后续分叉文件会**再加**类型；引用时写文件名，不要把本表当成永恒全集）：

| 名字 | `DomainType` |
|---|---|
| `DOMAIN_BEACON_PROPOSER` | `0x00000000` |
| `DOMAIN_BEACON_ATTESTER` | `0x01000000` |
| `DOMAIN_RANDAO` | `0x02000000` |
| `DOMAIN_DEPOSIT` | `0x03000000` |
| `DOMAIN_VOLUNTARY_EXIT` | `0x04000000` |
| `DOMAIN_SELECTION_PROOF` | `0x05000000` |
| `DOMAIN_AGGREGATE_AND_PROOF` | `0x06000000` |

Altair 另加（本表仍不是全集）：`DOMAIN_SYNC_COMMITTEE = 0x07000000`。同步委员会消息走这个域，不是 attester / proposer。见 [Altair 轻客户端精读](../light-clients/worked-example-sync-committee.md)。

`DOMAIN_APPLICATION_MASK = 0x00000001`：应用自用的域，与 mask 按位与必须非零；共识层已列的类型与 mask 按位与必须为零。

`compute_domain`：`DomainType ‖ fork_data_root` 的前 28 字节。`fork_data_root` 来自 `fork_version` 与 `genesis_validators_root`。  
`compute_signing_root`：对 `SigningData{ object_root, domain }` 再做 `hash_tree_root`。  
验 attestation 走 `DOMAIN_BEACON_ATTESTER`；验信标块走 `DOMAIN_BEACON_PROPOSER`。域不同，同一对象根不得在另一条 Verify 上为真。

**挡不住：** 这是共识层投票/操作的域，不是用户 EOA 转账（那是 secp256k1 + chainId）。EIP-712 更不是 attestation。

---

## 和另外几层不要混名

| 编码 | 本页的亲戚关系 |
|---|---|
| 消息前缀 `type‖chain` | CometBFT SignBytes **就是**这层的一种实现 |
| Ethereum CL `DomainType` | 同一层的另一种实现，还焊了 fork / genesis |
| FIPS 外部 `ctx` | 算法包装；投票家族建议一个 `ctx`，步类型仍要进 `M` |
| BIP-340 tagged hash | 哈希构造标签，不是 BFT 步 |
| EIP-712 | 钱包 typed data，不是 prevote |

---

## 对「不确定」（建议）

1. 规范写死：`Sign(prevote)` 的字节在 `Verify(precommit)` 上必须为假。语料 C21。  
2. `chain_id` / genesis 根进被签字节，不要只靠进程配置「我们只连这一条」。  
3. 签名器状态（上次 height/round/type）是部署不变量；崩溃后读 WAL，不能靠内存。  
4. 后量子：不变量 16 的「每高度票数」先数 prevote+precommit（再加 proposal）；`ctx` 按**消息家族**分，步类型仍在 `M` 里。  
5. 不填 CPU，不选 Ed25519 / BLS / ML-DSA。

---

## 精密检查

**禁止假学习：** 「验证者钥签的都是共识。」「BLS 聚合了所以不用域。」「同一块哈希签两次只是确认更强。」  
**边界：** 不写 vote extension 的另签细节；不抄当前 Ethereum 的 slot 秒数；不把 phase0 域表当成后续分叉的全集。Altair 的 `DOMAIN_SYNC_COMMITTEE` 已点名；后续文件仍可能再加类型。
