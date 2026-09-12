# 对抗语料目录（方法，不是考卷）

目的 B：把不变量和博物馆收成**命名用例**。  
不是 `exams/`。正文不穿插试题。实现仓库还不存在时，本目录只规定输入形状与期望，不写利用包。

覆盖知识树 M10.5。方法：L9.7。来源：博物馆 7 问第 7 条、不变量 1–37。

**允许 skip：** 仅当日志写明「没有第二实现」或「没有崩溃注入框架」。skip 不得当 PASS（反模式 test-skip-as-pass）。

**禁止：** 把绿条写成协议安全；为语料复现未公开漏洞。

| ID | 看守哪条 invariant | 输入形状 | 期望 | 层 | 出处 |
|---|---|---|---|---|---|
| C01 | 1 无双花 | 同一 prevout / 同一花费授权在 vin 中出现两次 | 共识拒绝 | 实现 | CVE-2018-17144 |
| C02 | 1 无双花 | 一块内两笔交易花同一授权 | 共识拒绝 | 实现 | 同上 |
| C03 | 2 供给 / 7 不回绕 | 两笔输出各自「看起来合法」，求和溢出 | 共识拒绝，不得模回绕 | 实现 | CVE-2010-5139 |
| C04 | 12 Merkle 唯一 | 奇数层复制叶子的变异块，与未复制的合法块同根 | 变异拒；先喂变异不得永久拉黑合法同哈希 | 协议+实现 | CVE-2012-2459 |
| C05 | 3 确定性 | 同一规范化块，`Apply` 读本地钟或 OS 随机数 | 两进程根必须同；读钟则设计失败 | 实现 | L1.6 / local-rng-in-apply |
| C06 | 3 确定性 | 错误字符串 / 无序 map 写进状态 | 两实现同根或都拒 | 实现 | L1.4 / L5.3 |
| C07 | 5 原子高度 | `Apply` 写到一半 SIGKILL | 重启 ∈ {pre_H, post_H_complete} | 实现 | L4.4 / L9.3 |
| C08 | 4 锁 | WAL 未记下 lock 即重启，同高改投冲突值 | 不得发出矛盾票 | 协议+实现 | L4.3 |
| C09 | 6 域分离 | `type=vote` 的字节拿到 `type=user-tx` 路径 | Verify 为假 | 协议 | domain 精读 |
| C10 | 8 `V(h)` 唯一 | 同高度两套验证者集合计票 | 只承认头/状态承诺的那一套 | 协议 | L4.5 |
| C11 | 11 算法标识 | 缺标签的签名，两实现各猜 ML-DSA / 旧曲线 | 必须拒或显式唯一标签 | 协议+实现 | L10.4 |
| C12 | 10 单旧签迁移 | 算法 A 已标危急，只带 A 的 σ 迁 pk | 拒绝 | 协议 | L10.4 |
| C13 | 14 升级不改供给 | UpgradeTx 改 `SupplyFormula` 或历史余额解释 | 拒绝（或必须走显式硬分叉对象） | 治理 | 升级精读 |
| C14 | 9 提交≠兑付 | 租户根已进房东头，挑战窗未过 | 不得显示可兑付 | 协议 | L7.4 |
| C15 | 15 占用 | 允许任意 data 时 `occupied > capacity` | 拒绝 | 协议 | L2.6 / Nervos RFC0022 形状 |
| C16 | 3 + BIP 50 亲戚 | 实现资源上限（锁、文件数）未写进规范 | 两实现一收一拒 ⇒ 规范或双方同拒 | 实现 | BIP 50 |
| C17 | 13 验证明≠供给 | （能测的模型里）错误公开输入仍过验 | 必须红；主网可靠性不能只靠诚实证明器 | 密码 | CVE-2019-7167；常不可单测 |
| C18 | 3 确定性 | 同一规范化交易；实现若把预编译返回值与可变内存别名 | 两 EVM / 规范向量必须同根；一家行为不得当规范 | 实现 | CVE-2021-39137 |
| C19 | 17 OTS 不复用 | 同一 pk 与同一 ots_index，两封不同消息的签 | 第二笔共识拒绝；不得 skip 当 PASS | 密码+协议 | RFC 8391 / SP 800-208；QRL 文档形状 |
| C20 | 18 FIPS ctx 按角色 | 同一 pk、同一应用消息 `M`；角色 A 的 `Verify(..., ctx_A)` 为真 | 角色 B 的 `Verify(..., ctx_B)` 必须为假；`ctx_A = ctx_B = ""` 不得当 PASS | 协议+实现 | FIPS 204 Alg. 2 / FIPS 205 Alg. 22 |
| C21 | 19 投票步类型 | 合法 prevote（或 attestation）的 σ 与同一块哈希 | `Verify` 走 precommit / proposer 路径必须为假；换 `chain_id` / genesis 根亦必须为假 | 协议 | CometBFT SignBytes；consensus-specs `compute_domain` |
| C22 | 20 BFT 轻客户端重叠 | 跳过中间高度；新 commit 只含 trusted `NextValidators` 中 ≤1/3 的权重（或信任期已过） | 必须 `NOT_ENOUGH_TRUST` / 拒绝，不得当 PASS；紧邻但 NextValidators 对不上亦拒 | 协议 | verification_001_published `LCV-FUNC-VALID.1` |
| C23 | 21 双签证据形状 | 同一验证者、同高同轮同 Type、两个不同 BlockID、本链 SignBytes 都真 | 必须能验为 DuplicateVoteEvidence；同 BlockID 或错 ChainID 必须拒。上链 ≠ 已 slash（应用侧另测） | 协议+经济 | CometBFT evidence.md |
| C24 | 22 轻客户端点名对象 | 文案/测试把「同步委员会超级多数」当成「全验证者 2/3 最终」 | 必须红；对象名写错不得当 PASS | 协议+文案 | Altair sync-protocol；对照 BFT 跳过 |
| C25 | 23 短时承诺≠永存 DA | 头已最终且含 versioned hash / `blob_kzg_commitments`，过了 4096 epoch 服务窗仍显示「L2 数据可重建」；或把 KZG 写成 Celestia DAS | 必须红；过窗无档案不得当 PASS | 协议+文案 | EIP-4844；deneb p2p；fulu/das-core；对照 Celestia |
| C26 | 24 检查点新鲜度 | 从检查点同步；`current_epoch > ws_epoch + ws_period`（或 CometBFT 信任期已过），仍显示「与从创世复算同一安全」；或检查点根不在路径上进程不退出 | 必须红；过期/错根不得当 PASS | 协议+部署 | phase0/weak-subjectivity.md；对照 trustingPeriod |
| C27 | 25 跳过须点名 | 开启 assumevalid / 已 load 快照，文案仍写「从创世验完所有脚本/UTXO」；或把默认哈希写成共识锁死的唯一历史 | 必须红；未点名跳过规则不得当 PASS | 实现+文案 | Bitcoin Core 0.14.0；assumeutxo 设计文档 |
| C28 | 26 可罚谓词 | 两张合法签但既非同 target epoch 不同 data、亦非 1 包住 2、亦非同 slot 双头，仍当 Casper slash；或 surround 顺序放反仍期望 process 成功；或把 DuplicateVoteEvidence 上链当已 slash | 必须红 | 协议+经济 | phase0 `is_slashable_attestation_data`；evidence.md |
| C29 | 27 排序须点名 | 文案把 Builder API / 盲头路径写成「共识已 PBS」或「提议者选过每一笔」；或把中继不揭示当成共识非法 | 必须红；文献等级写错不得当 PASS | 协议+文案 | builder-specs README；Bellatrix `builder.md` |
| C30 | 28 程序哈希与两层 accepted | 文案把 `ACCEPTED_ON_L2` 写成 L1 已更新 / 可提款；或把验 SNOS 证明写成与当前 `programHash` 无关的物理定律 | 必须红 | 协议+文案 | docs.starknet.io SNOS / Transactions |
| C31 | 29 调整钟上限 | 对等偏移算术可绕过「最大调整」；或节点因此拒收规范新块仍显示「与主网共识一致」 | 必须红 | 实现+部署 | CVE-2024-52912 |
| C32 | 30 索取不独占 | 一对等节点宣布未确认对象但不交付，超时后仍不能向其他已宣布对等节点索取；或文案把「本节点看不见」写成链拒绝 | 必须红 | 实现+网络 | CVE-2024-52913 |
| C33 | 31 头先够功 | 低工作量极长头序列可无界进块索引；或先入库再做检查点高度检查；或文案把「能跟头」写成「任意对等头都可常驻」 | 必须红 | 实现+部署 | CVE-2019-25220；CVE-2024-52916 |
| C34 | 32 孤儿可中断 | 接受一笔多输出交易后，孤儿解析数小时不让出；或文案把卡住写成「已同步」 | 必须红 | 实现 | CVE-2024-52914 |
| C35 | 33 四门分开 | 文案把 CheckTx OK 写成已进本块 / 已执行；或把 Process REJECT 当免费过滤；或 Prepare/Process 立即执行写入已提交状态；或把 Prepare 写成 PBS | 必须红 | 协议+文案 | ABCI++ basic concepts / app requirements / methods |
| C36 | 34 扩展≠块 | 文案把 Verify 拒扩展写成块非法；或 Finalize 按本高度收到的扩展改 `s_h`；或把扩展签写成 CanonicalVote | 必须红 | 协议+文案 | ABCI++ Req 6–10；CanonicalVoteExtension |
| C37 | 35 集合延迟 | 文案把 H 的 `validator_updates` 写成 H+1 按新集合计票；或把 `NextValidatorsHash` 更新写成新人已在投票；或把参数更新与集合更新写成同一拍 | 必须红 | 协议+文案 | ABCI++ FinalizeBlock；Validator Updates |
| C38 | 36 宣布≠收到 | 一对等节点宣布新块但不交付，超时前不能向其他已宣布对等节点索取；或文案把「本节点没拼出块」写成链非法 / 已跟上尖 | 必须红 | 实现+网络 | CVE-2024-52922 |
| C39 | 37 部分下载一次终结 | 第一次重建失败后同一实例再填一次导致进程断言退出；或文案把崩溃写成共识拒块 | 必须红 | 实现 | CVE-2024-35202 |

未编号、等第二实现才强制：差分 job 对 C01–C06、C11、C18 各跑一遍。  
未编号、等实测：验签配额（账本第 8 行）——无数字先写「超配额必拒」，配额本身空着。

对照：[`../invariants/README.md`](../invariants/README.md)、[`../../tracks/testing/worked-example.md`](../../tracks/testing/worked-example.md)、[`../../tracks/failure-museum/`](../../tracks/failure-museum/README.md)。
