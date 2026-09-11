# 工作实例：签了头，不等于自己排了序

> **事实 / 推断 / 建议** 已分开。
> 对照：[内存池筐](worked-example.md)、[投票 SignBytes](../consensus/worked-example-vote-signbytes.md)、[Casper 罚没](../economic/worked-example-casper-slashing.md)、[Monad 先定序](../../protocols/monad/README.md)。
> 主文献：[ethereum/builder-specs README](https://github.com/ethereum/builder-specs/blob/main/README.md)、[Bellatrix `builder.md`](https://github.com/ethereum/builder-specs/blob/main/specs/bellatrix/builder.md)。
> 本页钉 **谁出有序列表** 与 **谁签共识对象**。Builder API **不是** beacon 状态转换。不抄 MEV 金额、不抄经由中继的块占比。

---

## 0. 先修

- [L5.4](../../courses/level-05-ethereum/L05-M04-state-blobs-mev.md)
- [L9.2](../../courses/level-09-systems/L09-M02-mempool.md)
- [L0.7 生命周期](../../tracks/lifecycle/README.md)
- [不变式 26](../../libraries/invariants/README.md#26-可罚关系必须写成客观的两票谓词)

---

## 1. 核心问题

阿比看见「本 slot 的提议者签了块」，以为是这位验证者自己从内存池挑了每一笔交易。

可能是三件不同的事：

1. 提议者本地选交易，签带完整 `ExecutionPayload` 的信标块（共识对象）。
2. 提议者只看见 `ExecutionPayloadHeader`，签 `SignedBlindedBeaconBlock`，别人再揭示交易列表（Builder API）。
3. 协议内把「出块」和「排序」拆成两个共识角色（builder-specs 称为 PBS；**当时合并做不到**，要改信标链）。

「PBS」三个字母不够。必须能指出：列表谁写、头谁签、揭示失败时谁被信任。

---

## 2. 直觉（ELI15）

班长这节课盖章。以前班长自己排座位。后来有人先把「座位表封面」给班长盖章，座位名单事后才拆开。班长盖了章就不能再盖另一张，否则按双头罚。名单谁写的、拆不开怎么办，盖章规则本身没写。

---

## 3. 正式对象（builder-specs，事实）

### 3.1 两套文献不要糊

| 文献 | 它规定什么 | 它不是 |
|------|------------|--------|
| `consensus-specs` 信标状态机 | 全网对 `SignedBeaconBlock`（含完整执行载荷）做状态转换 | 构建者市场、中继、盲头议价 |
| `builder-specs` Builder API | 共识客户端如何向**外部实体**要块 | beacon `process_block` 的一部分 |

README 原文形状：Builder API 是共识客户端向外部实体要块的接口；协议内 PBS 要改信标链，合并时做不到；本 API 是**临时方案**，信任假设**高于**协议内 PBS，且**不改基础协议**。

**事实：** 把 Builder API 写成「以太坊共识已经 enshrine 了 PBS」，文献等级错了。

### 3.2 盲头与出价

`BuilderBid`：`ExecutionPayloadHeader` + `value` + 构建者 `pubkey`。  
`BlindedBeaconBlockBody` 带 `execution_payload_header`，**不**带交易列表。  
`get_bid` 把 `transactions_root = hash_tree_root(payload.transactions)` 写进 header——提议者签的是**根**，不是逐笔看见。

出价与验证者登记的签名走 `compute_domain(DOMAIN_APPLICATION_BUILDER)`（应用域；与 `DOMAIN_APPLICATION_MASK` 同族，见 SignBytes 精读）。  
盲块本身仍走 `DOMAIN_BEACON_PROPOSER`：`verify_blinded_block_signature` 用提议者钥验 `SignedBlindedBeaconBlock`。

**事实：** 同一把提议者钥、同一个 proposer 域，签的可以是「自己看见过载荷的块」，也可以是「只承诺了 header 的盲块」。域分不出「谁排的序」。

### 3.3 签完就绑住

README：一旦提议者签了带该 header 的块，选择被绑住，再签另一份就要承担 **equivocation / proposer slashing**（同 slot 两头，见 [casper-slashing](../economic/worked-example-casper-slashing.md)）。构建者这才揭示被盲掉的交易。

**事实：** 揭示发生在提议者已经无法无罚地改选之后。揭示失败（中继不回、载荷对不上 header）不是「共识判定该块非法」的新规则，是**部署/信任**：本 slot 可能空过。

**推断：** 审查与抽取会集中在写出列表的人，即使验证者集合看起来分散。这不是规范定理。

### 3.4 协议内 PBS

README 把「协议内拆 proposer / builder」叫 PBS，并写明当时要改信标链。后续 enshrined-PBS 提案族（研究/草案）**不是**本页对象。不要把某份 EIP 草稿写成已激活共识。

---

## 4. 对照表

| | 本地出块 | Builder API（域外） | 协议内 PBS（规范若将来写） | Bitcoin / 默认 CometBFT |
|--|----------|---------------------|---------------------------|-------------------------|
| 谁写交易列表 | 本 slot 提议者 | 外部 builder | 规范定义的 builder 角色 | 矿工 / proposer |
| 提议者签什么 | 完整载荷的信标块 | 先签盲头 | 以将来规范为准 | 整块 |
| 列表何时可见 | 签之前 | 签之后揭示 | 以将来规范为准 | 签之前 |
| 揭示失败 | 无此步 | 信任/活性；可能空 slot | 应有协议对象 | — |
| 文献 | consensus-specs | builder-specs | 当时不存在于合并时的信标规范 | 各自共识规范 |

Monad 的「先最终顺序、后出状态根」是**另一根钉子**（定序 ≠ 交差根），见过滤器页。不要和「谁写顺序」糊成一词。

---

## 5. 攻击者

| 攻击 | 机制 | 文献挡的 | 文献挡不住的 |
|------|------|----------|--------------|
| 把域外 API 当共识 | 文案 | README 写明不改基础协议、更高信任 | 用户以为「有 PBS 所以无需信任排序者」 |
| 签盲头后再改选 | 同 slot 另一头 | proposer slashing | 构建者已审查的那一份仍可能上链 |
| 中继不揭示 | 签后扣列表 | — | 本 slot 活性；不是新的 fork choice |
| 构建者稳定不收某类地址 | 列表权 | — | 验证者人数看起来分散 |
| 抄 MEV 金额 / 中继占比 | 官网仪表 | — | 数字过期；本页不填 |

---

## 6. 五层

| 层 | 本页能说的 | 不能说的 |
|----|------------|----------|
| 密码学 | 盲块走 proposer 域；出价走 application builder 域 | 「BLS 让提议者看见了每一笔」 |
| 协议 | 信标状态机仍吃完整载荷；Builder API 不在 `process_block` 里 | 「共识已经强制 PBS」 |
| 实现 | CL 经 Builder API 向外部要 header / 揭示 | 某客户端默认连哪家中继 |
| 部署 | 中继 / 多路复用器是信任对象 | 某年经由 MEV-Boost 的块比例 |
| 经济 | 排序权可被出价买走；`value` 是出价字段 | 累计提取的 MEV |

---

## 7. 对不确定的意义（建议）

- 结算机文档必须有一句：**谁写出块里的交易顺序**。默认「本高度提议者本地选」可以；若拆角色，必须写签什么、何时揭示、揭示失败怎么办。
- 不要抄域外 Builder API 当 v1 模块。那是更高信任，不是更少信任。
- 不要写「PBS 解决了 MEV」。拆角色改变的是**谁持有排序权**，不是消灭抽取。
- 提议者双头仍按不变量 26；盲头也是头。
- 后量子：盲块仍是一份 proposer σ；另加 builder 出价 σ。账本先加一行「每高度额外 builder 签」，数字仍空。

---

## 8. 禁句

- 「PBS 所以验证者不再审查」
- 「Builder API = 信标共识」
- 「签了头 = 提议者选过每一笔」
- 「协议内 PBS 已在合并时上线」
- 未标注日期的 MEV 金额、中继市场份额、经由 builder 的块占比
