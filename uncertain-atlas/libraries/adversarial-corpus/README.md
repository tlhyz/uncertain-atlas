# 对抗语料目录（方法，不是考卷）

目的 B：把不变量和博物馆收成**命名用例**。  
不是 `exams/`。正文不穿插试题。实现仓库还不存在时，本目录只规定输入形状与期望，不写利用包。

覆盖知识树 M10.5。方法：L9.7。来源：博物馆 7 问第 7 条、不变量 1–84。

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
| C40 | 38 快照≠创世 | 文案把 state sync 写成从创世重放；或把 Snapshot.hash 对上写成轻验 AppHash；或把 assumeutxo 背景全验安到 ABCI 快照上 | 必须红 | 协议+文案+部署 | ABCI++ OfferSnapshot；state-sync P2P |
| C41 | 39 下载状态隔离 | 对等节点 A 送来未请求变异块后，对 B 的 compact 重建被清掉，随后 B 的诚实 blocktxn 用不上；或文案把变异写成共识已拒合法块 | 必须红 | 实现+网络 | CVE-2024-52921 |
| C42 | 40 块时间点名算法 | 文案把 PBTS 写成 MTP / BFT Time 中位数 / 墙上现在；或把不 timely 写成块非法 / 已 slash；或把调整钟拒块写成 PBTS 改了规则 | 必须红 | 协议+文案 | PBTS README；BFT Time；不变量 29 |
| C43 | 41 MTP 三把尺 | 文案把太早、BIP113 locktime、太新窗写成同一把 MTP；或把 locktime 写成创世就看 MTP；或把 time-too-new 写成 BLOCK_INVALID_HEADER | 必须红 | 协议+文案 | chain.h GetMedianTimePast；validation.cpp；BIP 113 |
| C44 | 42 拒绝仍占盘 | 同一类健全性失败或检查点前分叉被反复送达后，日志无上限增长；或文案把「已拒绝」写成磁盘安全 | 必须红 | 实现+部署 | CVE-2025-54605；同类 54604 |
| C45 | 43 后台验签寿命 | 另一项检查失败提前 return 后，后台脚本线程仍可能读已释放的预计算；或文案把崩溃写成共识已安全拒块 | 必须红 | 实现 | CVE-2024-52911 |
| C46 | 44 拒了仍能再烧 | 同一对等节点连续送会被拒的未确认对象，累计验时无上限且新块被挤；或文案把非标准拒绝写成已断开 / 免费 | 必须红 | 实现+网络 | CVE-2025-46598 |
| C47 | 45 入站 INV 回复风暴 | 一条大 INV 在一次处理里把发送缓冲推到无界，或对方拒收时缓冲不排空仍继续灌 | 必须红 | 实现+网络 | CVE-2024-52915 |
| C48 | 45 GETDATA 单连接空转 | 畸形 GETDATA 让该连接处理循环不前进；或文案把单连接转圈写成全节点已死 | 必须红 | 实现+网络 | CVE-2024-52920 |
| C49 | 45 出站待宣布排序 | 对方从不宣布、集合长过排空时，排序占满 P2P 线程导致新块/保活停；或测试只连会回 INV 的对等节点却标 PASS | 必须红 | 实现+网络 | 2023-05 inv-to-send 官方披露 |
| C50 | 46 默认窗≠解绑 | 文案把默认 EvidenceParams 写成已盖住解绑；或把过期写成高度或时间；或把「当场能收双签」标成窗已够 | 必须红 | 协议+部署+文案 | ASA-2024-004；evidence.md 合取 |
| C51 | 47 超时≠最终 | 文案把 timeout_commit 写成第三条最终性 / 锁 / PBTS；或把 skip_timeout_commit 写成另一种最终；或把文档示例秒数写成共识 | 必须红 | 协议+文案 | consensus.md；configuration.md；PR #2892 |
| C52 | 48 最大消息≠接收 RAM | 文案把「消息最大 N 字节」写成每连接接收已有界；或把 2015-3641 写成发送缓冲 / 日志盘 | 必须红 | 实现+网络+文案 | bitcoincore.org/en/2024/07/03/disclose_receive_buffer_oom |
| C53 | 49 限速≠宽度 | 文案把地址表插入限速写成递增 ID 不会回绕；或把 v22 限速写成 overflow 已消失 | 必须红 | 实现+网络+文案 | bitcoincore.org/en/2024/07/31/disclose-addrman-int-overflow ；part 2 2025-04-28 |
| C54 | 50 自动封禁≠有界 | 文案把「行为不好就 ban」写成惩罚表已有上限；或自动路径写入可枚举无界 map；或 GETADDR 对每条地址扫全表仍标 PASS | 必须红 | 实现+网络+文案 | bitcoincore.org/en/2024/07/03/disclose-unbounded-banlist |
| C55 | 51 旋钮≠固定宽度 | 文案把 32-bit 内存池上限写成尺寸检查不会溢出；或 32-bit 与 64-bit 对同一超大对象一崩一收仍标 PASS | 必须红 | 实现+文案 | bitcoincore.org/en/2025/10/24/disclose-cve-2025-46597 |
| C56 | 52 应用等待≠槽位 | 文案把 next_block_delay 写成全网槽位 / 第三条最终性 / 已复制的共识参数；或把 main 规范写成所有发布线都有该字段 | 必须红 | 协议+文案 | abci++_methods.md FinalizeBlock；ADR-115 |
| C57 | 53 打洞≠必开 | 文案把默认关 UPnP 写成节点没在验证；或把局域网假设备写成互联网 P2P；或把 2015-20111 写成 Bitcoin Core 上已发生的 RCE / 私钥已泄漏 | 必须红 | 实现+部署+文案 | bitcoincore.org 2015-20111 / 52917；0.11.1 发行说明 |
| C58 | 54 代理≠对等 | 文案把出站 SOCKS / HTTP 代理写成「只是多一个 P2P 对等节点」；或把 2017-18350 写成未配代理也能打；或把明文网上的任意代理写成已缩小攻击面 | 必须红 | 实现+部署+文案 | bitcoincore.org/en/2019/11/08/CVE-2017-18350 |
| C59 | 55 URI≠验证 | 文案把打开付款 URI / 远程取单写成全节点已验证；或把取单 OOM 写成共识拒绝；或把删掉 BIP70 写成共识倒退 | 必须红 | 实现+部署+文案 | bitcoincore.org/en/2024/07/03/disclose-bip70-crash |
| C60 | 56 AppHash≠日程 | 文案把轻验 AppHash 对上写成提议者选择已对齐；或两份 RPC 投票权相同、ProposerPriority 不同仍让 state sync 标 PASS | 必须红 | 协议+实现+部署+文案 | GHSA-g5xx-c4hv-9ccc |
| C61 | 57 扩展路径≠已检查 | 文案把扩展 Precommit 快路径写成旧票字段已验；或默认关扩展写成启用后不会 panic；或越界 ValidatorIndex 让接收进程退出仍标 PASS | 必须红 | 实现+文案 | GHSA-p7mv-53f2-4cwj |
| C62 | 58 治理改启用高度≠已能吃 | 文案把治理通过的 VoteExtensionsEnableHeight 写成所有节点已按新高度启用；或该键验证失败让进程退出仍标 PASS | 必须红 | 协议+实现+文案 | GHSA-qr8r-m495-7hc4 |
| C63 | 59 验根≠下标对齐 | 文案把「证明过根」写成外层下标已对齐；或 Part.Index ≠ Proof.Index 仍标已收到 / 再流言仍标 PASS | 必须红 | 实现+网络+文案 | GHSA-r3r4-g7hq-pq4f |
| C64 | 60 先验再传 | 文案把「稍后会处理」写成可以先转发非法 BitArray；或 Bits 与 Elems 对不上仍发出去仍标 PASS | 必须红 | 实现+网络+文案 | GHSA-hrhf-2vcr-ghch |
| C65 | 61 复算≠BFT保证 | 文案把「中位数复算通过」写成故障者不能抬高 Time；或 Verify(Commit) 与 MedianTime 输入集合不同仍标 PASS | 必须红 | 协议+实现+文案 | GHSA-c32p-wcqj-j677；bft-time.md |
| C66 | 62 邻居latest≠尖 | 文案把对等节点 latest 写成全网尖；或先高后低再断开后仍无限追无来源高度仍标 PASS | 必须红 | 实现+网络+文案 | GHSA-22qq-3xwm-r5x4 |
| C67 | 63 默认MaxBytes≠SLA | 文案把仓库默认 BlockParams.MaxBytes 写成第一轮总能过；或 timeout_propose 不对照块上限；或超限提案被接受仍标 PASS | 必须红 | 协议+部署+文案 | GHSA-hq58-p9mv-338c |
| C68 | 64 飞行中≠证据身份 | 文案把「看见双签立刻用本机当前块 last commit 打时间戳」写成已安全；或同一对票、两个时间戳、其余诚实节点被当非法提案者仍标 PASS | 必须红 | 协议+实现+文案 | GHSA-p658-8693-mhvg；CVE-2021-21271 |
| C69 | 65 +2/3≠其余已签 | 文案把「已有 +2/3，其余槽位随便」写成已安全；或错块签名进入 Commit 仍标 PASS；或应用按未验完的 LastCommitInfo 发奖仍标 PASS | 必须红 | 协议+实现+经济+文案 | GHSA-6jqj-f58p-mrw3；CVE-2020-15091 |
| C70 | 66 验过头≠能交证据 | 文案把 ValidAndVerified 写成已能提交 LightClientAttackEvidence；或只测同高两块、朝前高度形不成证据仍标 PASS；或把「安全模型外」写成免检 | 必须红 | 协议+经济+文案 | GHSA-f3w5-v9xx-rp8p |
| C71 | 67 邻居上限≠握手配额 | 文案把 max inbound peers 写成握手请求已有界；或 AddPeer 前失败、ID 不还、map 涨到顶仍标 PASS；或把公开 RPC 写成已随 P2P 有配额 | 必须红 | 实现+网络+部署+文案 | GHSA-v24h-pjjv-mcp6；CVE-2020-5303 |
| C72 | 68 注入扩展≠投票权 | 文案把 ValidateVoteExtensions 绿了写成权重已对齐状态机；或注入扩展里的权数与状态机不一致仍标 PASS | 必须红 | 协议+实现+文案 | GHSA-95rx-m9m5-m94v |
| C73 | 69 CheckTx绿≠整包可提案 | 文案把每笔 CheckTx 绿写成 Prepare 输出必被 Process 收下；或同一发送者序号不连续仍提出非法块仍标 PASS | 必须红 | 协议+实现+文案 | GHSA-2557-x9mg-76w8 |
| C74 | 70 外层上限≠内层已有界 | 文案把 max_tx_bytes 写成嵌套 UnpackAny 已有界；或深嵌套解码无递归上限仍标 PASS；或内部消息/恶意验证者块放出的消息不受外层上限仍标 PASS | 必须红 | 实现+协议+文案 | GHSA-8wcc-m6j2-qxvm |
| C75 | 71 EndBlocker错≠可跳过 | 文案把可选群组/治理模块写成局部失败；或能与该模块交互的用户引入 EndBlocker 错误仍标 PASS；或只用亲戚除零页代替本条仍标 PASS | 必须红 | 协议+实现+部署+文案 | GHSA-47ww-ff84-4jrg |
| C76 | 72 再委托≠洗白 | 文案把再委托写成待执行罚没已消失；或过错后、slash 前再委托、原份额仍标未罚仍标 PASS | 必须红 | 经济+协议+文案 | GHSA-86h5-xcpx-cfqc |
| C77 | 73 停链交易≠已停 | 文案把 MsgVerifyInvariant 写成链已停；或交易内 panic 被恢复、节点继续出块仍标「停机模块已安全」 | 必须红 | 协议+实现+部署+文案 | GHSA-qfc5-6r3j-jj22 |
| C78 | 74 池溢出≠只是金额 | 文案把奖励池入金溢出写成只拒金额；或能存款的验证者引入溢出、高度停仍标 PASS | 必须红 | 实现+协议+经济+文案 | GHSA-p22h-3m2v-cmgh |
| C79 | 75 被挡≠已开户 | 文案把 blocked 写成不能挂归属；或未初始化模块账户被 GetModuleAccount 叫到停链仍标 PASS；或 authz/feegrant 未扫仍标变体已修 | 必须红 | 协议+实现+部署+文案 | GHSA-4j93-fm92-rp4m |
| C80 | 76 Int/Dec≠已对齐 | 文案把 Int/Dec 写成位宽已齐、Dec 进 Int 仍 panic 仍标 PASS；或把 1.3.0→1.4.0 写成必须硬分叉 | 必须红 | 实现+协议+文案 | GHSA-7225-m954-23v7 |
| C81 | 77 ack JSON≠已确定 | 文案把 ack 意思对写成反序列化已确定；或能开通道的用户引入非确定 ack 仍标 PASS；或只测 transfer 标全覆盖 | 必须红 | 协议+实现+文案 | GHSA-4wf3-5qj9-368v；GHSA-jg6f-48ff-5xrw |
| C82 | 78 超时挂钩≠已原子 | 文案把 ibc-hooks 写成 ICS-20 超时已原子；或 OnTimeout 里再跑 MsgTimeout、承诺未删仍标 PASS；或只测许可上传标重入已安全 | 必须红 | 协议+实现+经济+文案 | GHSA-j496-crgh-34mx |
| C83 | 79 ICS-23验绿≠在树里 | 文案把 ICS-23 Verify 绿写成叶子已在原树 / 包真的没收到；或伪造超时仍标 ICS-20 已结算仍标 PASS；或只升 SDK、未换 ics23 仍标已补；或把 +⅓ 打补丁写成 soundness 已齐 | 必须红 | 密码+协议+经济+文案 | forum Dragonberry 7702；复盘 8735 |
| C84 | 80 自动下载≠已升级 | 文案把 Cosmovisor / 自动换二进制写成共识升级已完成；或打开 DAEMON_ALLOW_DOWNLOAD_BINARIES 仍标默认安全；或校验和默认 false 仍标已有强保证 | 必须红 | 部署+实现+文案 | GHSA-23px-mw2p-46qm |
| C85 | 81 授权代发≠已校验 | 文案把授权代发写成内层已过 ValidateBasic；或代发路径跳过基本校验仍标 PASS；或只测 ics23 replace 标 Elderflower 已修 | 必须红 | 协议+实现+经济+文案 | forum Elderflower 8584；复盘 8735 |
| C86 | 82 本地钟≠已确定 | 文案把 ValidateBasic 读 time.Now() 写成已确定；或过期比较用节点本地钟、两节点各执一词仍标 PASS；或把「资金安全」写成链不会停；或与 Elderflower 糊成一句 | 必须红 | 协议+实现+文案 | GHSA-2p6r-37p9-89p2；CVE-2021-41135 |
| C87 | 83 空地址≠无类型 | 文案把「地址还空」写成不能被外人写成归属账户；或他人初始化只进不出、随后入金取不出仍标 PASS；或把 33%+1 升完写成全网已齐 / 不会停；或与 ASA-2024-003 糊成一句 | 必须红 | 协议+实现+经济+文案 | GHSA-j2cr-jc39-wpx5 |
| C88 | 84 停链≠一种 | 文案把「停链」写成一种事故；或把停链交易写成已停；或把 EndBlocker 出错写成可跳过；或把 +⅓ 打补丁写成不会停；或把 Barberry 锁钱写成高度停 | 必须红 | 协议+实现+部署+文案 | 停链面地图；不变量 71/73/74/75/77/79/82/83 |

未编号、等第二实现才强制：差分 job 对 C01–C06、C11、C18 各跑一遍。  
未编号、等实测：验签配额（账本第 8 行）——无数字先写「超配额必拒」，配额本身空着。

对照：[`../invariants/README.md`](../invariants/README.md)、[`../../tracks/testing/worked-example.md`](../../tracks/testing/worked-example.md)、[`../../tracks/failure-museum/`](../../tracks/failure-museum/README.md)。
