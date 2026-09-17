# 工作实例：证据窗是合取，默认值不是解绑

> **事实 / 推断 / 建议** 已分开。
> 对照：[证据 ≠ slash](worked-example-evidence.md)、[信任期 < 解绑](../light-clients/worked-example-bft-skip.md)、[ASA-2024-004](../failure-museum/asa-2024-004.md)。
> 主文献：[evidence.md](https://github.com/cometbft/cometbft/blob/main/spec/consensus/evidence.md)、[ABCI++ EvidenceParams](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)、[GHSA-555p-m4v6-cqxv](https://github.com/cometbft/cometbft/security/advisories/GHSA-555p-m4v6-cqxv)。
> 本页钉 **过期公式与默认窗**。不抄默认块数 / 纳秒。

---

## 0. 先修

- [L4.3](../../courses/level-04-bft/L04-M03-locks.md)
- [不变量 21](../../libraries/invariants/README.md)（证据通知应用）
- [不变量 20](../../libraries/invariants/README.md)（信任期 < 解绑）

---

## 1. 核心问题

阿比看见 `EvidenceParams`，以为「有默认所以能罚到解绑前的双签」。

规范写的是另一句：两条尺子**都**超过才过期。咨询写的是第三句：出厂默认可能比解绑短。

---

## 2. 直觉（ELI15）

班规：检举必须在「过了这么多节课」**并且**「过了这么多天」之后才作废。只过其中一条，检举还算数。

学校发的空白表格上填的数字，可能比「毕业离校手续」短。表格有数字 ≠ 还能罚到已经办完离校的人。

---

## 3. 正式对象（规范 + 咨询，事实）

过期（evidence.md）：

`CurrentHeight - MaxAgeNumBlocks > EvidenceHeight` **且** `CurrentTime - MaxAgeDuration > EvidenceTime` → 忽略。

高度用 `DuplicateVoteEvidence` 里票的高度，或 `LightClientAttackEvidence` 的 `CommonHeight`，再取对应头的时间。

ABCI++：块若带过期证据（上述合取成立），验证者不应投票。`MaxAgeDuration > 0`、`MaxAgeNumBlocks > 0`。

ASA-2024-004：默认两参数对常见用例可能盖不住 `UnbondingTime`。两条都超 → 证据过期 → 窗外发现的拜占庭行为可能罚不到。无代码补丁。建议：`MaxAgeDuration` 超过解绑时长；`MaxAgeNumBlocks` 超过解绑期内估计块数。

`data_structures.md` 建议：`max_age_duration` 应对应用的解绑（或同类 nothing-at-stake 机制）；`max_age_num_blocks` 可用 `max_age_duration / 平均出块时间`。平均出块时间是部署估计，不是共识常数。

| 钉子 | 不等式 | 断了会怎样 |
|------|--------|------------|
| 证据窗 | 窗 ≥ 解绑（两参数都要够） | 晚到的证据合法过期，罚不到 |
| 轻客户端信任期 | 信任期 < 解绑 | 过期检查点仍被当成从创世一样安全 |
| 谁执行 slash | 引擎通知，应用写公式 | 上链被写成已经罚光 |

**事实：** 把「或」写成过期条件，是实现分叉。  
**事实：** 默认有值 ≠ 已盖住解绑。  
**建议：** 第一版把两参数当空位，测过再填；不要抄仓库默认。

---

## 4. 攻击者

| 攻击 | 机制 | 文献挡的 | 文献挡不住的 |
|------|------|----------|--------------|
| 拖到窗外再曝光双签 | 分区 / 藏证据 | 窗 ≥ 解绑则人还在 | 默认太短；≥1/3 审查证据 |
| 把默认写成已安全 | 文案 | ASA-2024-004 | 运营者不改参数 |
| 把合取改成析取 | 实现 | 规范写且 | 两实现各判各的过期 |

---

## 5. 五层

| 层 | 本页能说的 | 不能说的 |
|----|------------|----------|
| 密码学 | 过期不验证伪签 | 「窗已经后量子」 |
| 协议 | 合取公式；>0 是下限不是解绑 | 某 SDK 默认秒数 |
| 实现 | 用证据高度取头时间 | 默认块数当永恒 |
| 部署 | 参数必须按解绑重算 | 某链出块间隔 SLA |
| 经济 | 窗短于解绑 = 晚发现罚不到 | Cosmos 罚金百分比 |

---

## 6. 对不确定的意义（建议）

- 写进同一页：上链 ≠ slash；窗是合取；窗 ≥ 解绑；默认不是第三句。
- 与不变量 20 对照着写，不要只抄「信任期短于解绑」忘了证据窗要长于解绑。
- 不填具体天、块、纳秒，直到有自己的出块估计。

---

## 7. 禁句

- 「有 EvidenceParams 所以能罚到解绑前的人」
- 「默认窗已经按规范够用」
- 「过期是高度或时间」（规范是且）
- 「ASA-2024-004 已经有补丁版本」
