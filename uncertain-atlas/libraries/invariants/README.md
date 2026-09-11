# Invariant Library

只收能写成测试的句子。

已收：

1. **无双花：** 同一花费授权在 canonical 历史上不得被接受两次。  
2. **供给守恒：** 除协议允许的发行规则外，不得凭空多出可花费余额。  
3. **确定性：** 同一已排序输入，两实现状态哈希相同。  
4. **锁：** 诚实节点不得在同一高度对两个冲突值发出违反锁规则的承诺。  
5. **原子高度：** 崩溃恢复后，应用高度与引擎高度一致，无半块状态。  
6. **域分离：** 验证者投票字节不得被当成用户交易。  
7. **金额不回绕：** 任何余额/输出求和溢出必须拒绝，不得模回绕后当作合法。  
8. **集合版本：** 同一高度的计票只使用唯一的 `V(h)`，且该哈希被状态/头承诺。  
9. **提交≠兑付：** 租户状态根被包含到房东头，不等于桥可兑付。  
10. **迁移不可单旧签：** 算法 A 危急后，不得只凭 A 的签名把账户迁到新 pk。  
11. **算法标识：** 共识验签必须先读明确的算法标签，禁止隐式默认两种实现各猜各的。  
12. **Merkle 叶列表唯一：** 规范允许的填充不得让两个不同叶列表承诺到同一根；变异块必须拒绝，且不得把同哈希的合法块永久拉黑（CVE-2012-2459）。  
13. **验证明 ≠ 供给：** `VerifyProof=接受` 不得单独充当供给守恒（CVE-2019-7167）。  
14. **升级不得改供给解释：** 升级交易可增加算法标识，不得静默改 `SupplyFormula` 或历史余额含义。  
15. **状态占用有界：** 若协议允许任意 `data` 进活状态，必须有占用不等式或等价回收；禁止只收一次执行费而要求全节点永存。  
16. **投票流量先算：** 宣称 PQ-BFT 可上主网之前，必须写出 `每高度票数 × |σ_vote|`（参数集 + FIPS 版本）；未写不得用「已后量子」当结算文案。  
17. **OTS 叶子不复用：** 若路径使用有状态哈希签名（XMSS/LMS 等），canonical 历史上同一 `(pk, ots_index)` 不得再授权另一笔不同消息；实现必须先持久化 index 再输出 σ（RFC 8391；SP 800-208）。  
18. **FIPS ctx 按角色：** 使用 FIPS 204/205 外部 API 时，`Verify` 必须传入规范写明的 `ctx`（≤255 B）。同一把钥上的用户签与投票签不得都用空 `ctx`；pure 与 pre-hash 必须由算法标签区分（FIPS 204 Alg. 2；FIPS 205 Alg. 22）。  
19. **投票步类型进被签字节：** Prevote 的 SignBytes（或 attestation 的 domain）不得使 Precommit / proposer 路径 Verify 为真。同一高度两步不是「再签一次同一哈希」（CometBFT signing.md；consensus-specs `compute_domain`）。  
20. **BFT 轻客户端重叠旧集合：** 跳过中间高度时，新 commit 必须含 trusted `NextValidators` 中 **> max(1/3, trustThreshold)** 的投票权，且 trusted 仍在 `trustingPeriod` 内；紧邻后继必须集合哈希相接且旧集合 +2/3。只数新委员会自己的 2/3 不得接受（verification_001_published `LCV-FUNC-VALID.1`）。  
21. **双签证据形状成立 ≠ 已罚没：** 同一 `(addr, height, round, type)`、不同 `BlockID`、本链 `ChainID` 上两张合法签，必须能被验为 `DuplicateVoteEvidence`；同 BlockID 或错链必须拒。引擎提交 `Misbehavior`，应用决定 slash。过期按规范的年龄参数忽略（CometBFT evidence.md）。  
22. **轻客户端必须点名信任对象：** 产品句须写清是「已信任全集的重叠」（CometBFT 跳过）、「同步委员会样本」（Altair）还是证明系统。样本的 2/3 不得写成全验证者集合的 2/3（altair/light-client/sync-protocol.md）。  
23. **短时承诺不是永存 DA，且 KZG 不是纠删 DAS：** 头或 versioned hash 被最终确定，不得单独充当「数据永远可重建」。4844 sidecar 的服务窗是 `MIN_EPOCHS_FOR_BLOB_SIDECARS_REQUESTS`（4096 epoch）。PeerDAS 抽到列不得写成执行正确，也不得写成与 Celestia 二维 DAS 同一对象（EIP-4844；deneb/p2p-interface.md；fulu/das-core.md）。  
24. **检查点同步必须落在弱主观或信任期内：** 从检查点起步时，检查点必须在同步路径上，且对当前时间仍 `is_within_weak_subjectivity_period`（或 CometBFT `trusted.Time > now - trustingPeriod`）。过期或对不上不得当「和从创世复算同一安全」；对不上路径按规范应致命退出。检查点从哪来是部署对象（phase0/weak-subjectivity.md；verification_001_published）。  

来源：L0–L10 课 + 档案 + 博物馆。每条应对 L9.7 的自动测试。用例目录：[`../adversarial-corpus/README.md`](../adversarial-corpus/README.md)。

**对不确定（建议，不是选型）：** 第 16 条在选定 PQ 算法之前就算一遍。第 17 条：投票与热钱包不要用有状态 HBS。第 18 条：每个签名角色一个 `ctx` 常量（或一把钥只服务一个角色）；不要只靠「消息里已经写了 domain」。空 `ctx` 是 FIPS 默认，不是已分离。第 19 条：步类型进 `M`；签名器记住上次 `(height, round, type)`。第 20 条：轻客户端默认不是结算角色；若启用，跳过必须重叠旧集合，信任期必须短于解绑期。第 21 条：证据上链只通知应用；罚没公式写在 ABCI 一侧。第 22 条：轻客户端文案点名样本还是全集；不要抄 Altair 当第一版默认。第 23 条：短时 DA 必须写服务窗；不要抄 KZG blob 当后量子默认 DA。第 24 条：检查点同步必须写新鲜度；不要把 finalized 写成「从创世一样安全」。
