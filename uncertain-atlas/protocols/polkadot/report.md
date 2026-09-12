# Polkadot · 19 节档案（第一版）

核心问题：一条小链为什么可以「借用」另一条链的安全？借的时候多出了什么可以被打的面？  
资料：Polkadot 指南 / 论文（可用性、backing、approval、GRANDPA/BABE）。细节随版本变，路径预告。

---

## 1. 一句话定义

Relay chain 的验证者对 parachain 的候选块做：**备份（backing）→ 数据可用 → 审批（approval checking）→ 最终**。平行链自己的 collator 出候选，不单独构成全网安全。

---

## 2. 它解决的问题

每条小链自养验证者：安全随市值变弱，易被租算力/租质押碾。  
共享安全：经济安全池在中继链，执行分片在平行链。

新病：中继与平行之间的协议本身会成为攻击面（不可用、错误备份、跨链消息伪造）。

---

## 3. 架构图

```text
用户 --tx--> 某条 parachain 的 collator
                    ↓
              候选块（PoV / 见证）
                    ↓
         中继验证者：backing
                    ↓
         可用性：分片/纠删，别人能重建
                    ↓
         approval checking（随机抽查执行）
                    ↓
         GRANDPA 等最终中继头
                    ↓
         XCM 跨链消息（可选）
```

---

## 4. 一笔交易完整生命周期

1. 用户对平行链签交易（该链自己的账户模型）。  
2. Collator 打进该链候选块，附带验证所需见证。  
3. 一组验证者 backing：声称「我们检查过」。  
4. 候选数据必须可用，否则无法独立复验。  
5. 其他验证者可能被抽中重新执行。失败则争议。  
6. 中继链最终后，该平行块才算在共享安全下敲定。  
7. 若只听 collator 的 RPC、不等中继最终：用户层假确认。

---

## 5. 状态模型

平行链自选（账户/UTXO/…）。  
中继链状态：验证者、质押、平行注册、可用性比特。  
XCM：跨共识消息，不是「同一 EVM 里转账」。

---

## 6. 共识

中继：出块（BABE 一类）+ 最终（GRANDPA 一类）。  
GRANDPA 可一次最终多块，与 Tendermint「每高一 commit」不同，不要混。  
平行候选有独立的可用性/审批子协议，挂在中继最终性之下。

---

## 7. 执行

平行链 runtime（常 WASM）在验证者/审批路径上被执行或抽查。  
Runtime 可升级：快，但升级治理是中心化风险（见反模式 admin-god-key）。

---

## 8. 网络

PoV 可能很大：可用性协议把数据分散。  
攻击：只让 backing 小组看见数据，其他人抽查失败或无法重建——这是 DA 问题在共享安全里的翻版。

---

## 9. 存储

中继存元数据与最终头。平行状态主要由该链节点存。  
归档谁负责「能复验旧平行块」，要单独设计。

---

## 10. 密码学

验证者签名、GRANDPA/BABE 用的签名与 VRF（抽签/随机），哈希，可用性编码。  
用户签名在平行链，可与中继不同。

---

## 11. 安全假设

| 假设 | 失效 |
|---|---|
| 中继验证者诚实阈值 | 错误平行块被最终 |
| 可用性成立 | 无法揭发错误执行 |
| 审批抽样够 | 错误执行漏网 |
| 平行 runtime 确定性 | 验证者算不同根 |
| XCM 配置与桥 | 跨链铸错/双花 |
| 用户等中继最终 | 假确认 |

「借用安全」不是免费：你借入的是**中继假设 + 子协议假设**。

---

## 12. 最大结构性优势

**小链的经济安全可以等于大池，而不是等于自己的市值。**  
执行仍分片，安全不随每条小链拆薄（在模型成立时）。

---

## 13. 最大具体缺陷

1. 子协议复杂，实现与参数都是新攻击面。  
2. 平行链仍可被自己的 runtime/升级伤害。共享的是共识安全，不是应用不错。  
3. 插槽/治理政治。  
4. 对「不确定」：你们若就是要做一条结算 L1，不必先当平行链；但要懂「共享安全 ≠ 无条件继承」。

---

## 14. Trade-off

| 得到 | 换 |
|---|---|
| 共享经济安全 | 复杂可用性/审批、延迟、治理 |
| 执行分片 | 跨链消息的新语义与桥风险 |
| WASM 可升级 | 升级钥匙 |

对照 restaking：也是「借安全」，攻击面同样转移到**如何证明被借用的工作做对了**。有名不是入选理由。

---

## 15. 历史事故

已归档官方七问：[`../../tracks/failure-museum/polkadot-2025-05-runtime-api-decode-depth.md`](../../tracks/failure-museum/polkadot-2025-05-runtime-api-decode-depth.md)（交易解码深度有界 ≠ runtime API 再解整块已安全）；[`../../tracks/failure-museum/kusama-2025-08-24-group-index-votes.md`](../../tracks/failure-museum/kusama-2025-08-24-group-index-votes.md)（组下标 ≠ 票向量下标）；[`../../tracks/failure-museum/kusama-2024-02-15-disabled-active-dispute.md`](../../tracks/failure-museum/kusama-2024-02-15-disabled-active-dispute.md)（Active ≠ Confirmed）；[`../../tracks/failure-museum/kusama-2025-05-09-offchain-disable.md`](../../tracks/failure-museum/kusama-2025-05-09-offchain-disable.md)（链下内存禁用 ≠ 已确认争议已经不参与）；[`../../tracks/failure-museum/polkadot-2026-06-election-score-floor.md`](../../tracks/failure-museum/polkadot-2026-06-election-score-floor.md)（改冻结门槛 ≠ 选举地板已经配对；出块还在 ≠ 纪元已经转）；[`../../tracks/failure-museum/polkadot-2026-03-xcm-preserve-origin.md`](../../tracks/failure-museum/polkadot-2026-03-xcm-preserve-origin.md)（preserve_origin 为真 ≠ 出站已经带了改 origin 的指令；静默跳过 ≠ BadOrigin）；[`../../tracks/failure-museum/polkadot-2026-03-deprecated-runtime-api-scale.md`](../../tracks/failure-museum/polkadot-2026-03-deprecated-runtime-api-scale.md)（废弃 runtime API 还在 ≠ 返回编码已经兼容；整理者还能写块 ≠ 中继已经收到）。其它（可用性、其它 XCM 回归）仍须官方出处且谓词独立，不编根因。

---

## 16. 源码入口（预告）

Polkadot SDK / 可用性与 approval 模块。

1. 候选 backing。  
2. 可用性比特与重建。  
3. approval 抽查。

不要从平行链 pallet 教程入门。

---

## 17. 关键函数（逻辑级）

**`ensure_available`**  
输入：候选、份额。输出：可重建或失败。  
invariant：最终前必须可用。

**`approve_or_dispute`**  
输入：随机抽中的复执行。输出：接受或争议。  
invariant：错误执行有被发现的路径。

---

## 18. 如何测试

扣留 PoV、错误执行应被审批抓住、XCM 重放。  
「不确定」若永不做平行链：仍要测「轻节点在无体时必须拒绝」。

---

## 19. 「不确定」适用性

| 档 | 内容 |
|---|---|
| 强烈建议研究 | 共享安全的新攻击面；可用性先于信任执行；最终性在哪一层 |
| 可以参考 | 执行与安全池分离 |
| 暂时不需要 | 成为平行链、XCM 全套 |
| 不建议采用 | 「我们挂在大链下所以自动安全」；升级万能钥匙 |
