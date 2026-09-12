# 知识库修改日志

只记知识库结构与内容，不记交易回测。细节审核见 [`AUDIT_LOG.md`](AUDIT_LOG.md)。

## 2026-09-12（续 105–107）

- 博物馆 Zcash ZIP 256：重复块头可静默复位链价值池跟踪，ZIP 209 闸门名义上仍在、实现字段被清掉。初始化必须在去重之后；启动从块数据重算检查点之后的增量。跟踪复位不是闸门还在转。
- 不变量 104；语料 C108；反模式 dup-header-sold-as-turnstile；L10.3 第 100 条。
- 博物馆 Zcash ZIP 256：v4 无 Spend/Output 时，`valueBalanceSapling` 编码非零被反序列化改写成 0，共识「必须为 0」的检查从不开火。Zebra 按规范拒编码。归一化成零不是编码必须为零。
- 不变量 105；语料 C109；反模式 normalize-sold-as-encoded；L10.3 第 101 条。
- 博物馆 Zcash ZIP 256：NU5 起授权数据由 `hashBlockCommitments` 承诺，不由 Merkle 根。体可变拒绝若先开火，可把诚实头永久标非法。体拒绝不是头已经绑死。
- 不变量 106；语料 C110；反模式 body-reject-sold-as-header-bound；L10.3 第 102 条。
- 对照不变量 2 / 3 / 12 / 13 / 39 / 74 / 96 / 102。不写怎样送重复头、怎样拼非零余额栏、怎样改体。不抄版本 / 高度 / 规范金额上限。ZIP 256 其余独立谓词（身份 `rk`、`ephemeralKey`、coinbase 崩溃循环）有官方句且不与已归档条重复才另档。CVE-2024-52911 已在 Bitcoin 馆，不克隆。

## 2026-09-12（续 103–104）

- 博物馆 Zcash ZIP 257：Orchard Action 电路实现缺拷贝约束，陈述按规范是对的。先软分叉关 Orchard，再 NU6.2 换验证钥。旧钥过验不是新电路已安全。
- 不变量 102；语料 C106；反模式 circuit-impl-sold-as-statement；L10.3 第 98 条。
- 博物馆 Ethereum 2016-11-24：Geth journaling 在 OOG 时没撤回空账户删除，网络分叉。OOG 结束不是删除已回滚。
- 不变量 103；语料 C107；反模式 oog-sold-as-reverted；L10.3 第 99 条。
- 对照不变量 13 / 28 / 95 / 3 / 5 / 83 / 101。不写怎样欠约束或怎样踩 OOG 删户。不抄高度 / 证明长度 / 块号。

## 2026-09-12（续 102）

- 博物馆 Ethereum 2021-05：官方威胁披露（非已停机）。状态访问操作码 gas 是常数，磁盘查找随 trie 变密。gas 上限内的块仍可拖到分钟级。无条件涨价不够。未命中罚金须先查找，可被嵌套白嫖。Berlin 只涨本笔未访问对象；快照把读摊平，不是 gas 已经等于墙钟。
- 不变量 101；语料 C105；反模式 gas-sold-as-wallclock；L10.3 第 97 条。
- 对照不变量 44 / 89 / 90 / 96。不写怎样做随机查找。不转官方循环。不抄 gas / 秒数 / 层数 / 磁盘增量。Avalanche Native Asset Call 官方页被网关挡住，本批不写。

## 2026-09-12（续 101）

- 博物馆 Kusama 2025-05-09：官方预期旧节点会争议新收据，也预期链下禁用能挡垃圾。链下禁用只挡未确认；一旦确认，节点仍参与。名单在内存、只活一个 session，重启清空。训练轮触发了，但 GRANDPA 在它之前已停最终。
- 不变量 100；语料 C104；反模式 offchain-disable-sold-as-confirmed-ignore；L10.3 第 96 条。
- 对照不变量 80 / 93 / 98 / 99。不写怎样留下旧节点或怎样灌争议。不抄确认门槛 / 训练轮块数 / ⅓ / 版本号。

## 2026-09-12（续 99–100）

- 博物馆 Kusama 2025-08-24：剔除已禁用者的有效性票时用组下标当票向量下标。票比组少则删错签、后面错位。`create_inherent` 回 None，客户端当合法、不打错误；生产 runtime 关日志。`on_finalize` 缺 inherent 而 panic。空 InherentData 能出块是重启后内存空了；恢复靠候选过期。
- 不变量 98；语料 C102；反模式 group-index-sold-as-vote-index；L10.3 第 94 条。
- 博物馆 Kusama 2024-02-15：禁用后再发起的争议被导入并标 Active，无人参与，从未 Confirmed；GRANDPA 把 Active 当威胁并省略这些块。年龄安全网后来忽略更老争议，不是谓词。测试覆盖了当天情景，但没跑够久、没断言最终性。
- 不变量 99；语料 C103；反模式 active-dispute-sold-as-confirmed；L10.3 第 95 条。
- 对照不变量 21 / 59 / 86 / 97。不写怎样让票缺席或怎样再发起。不抄下标 / 块号 / 过期窗 / ⅓ / 落后块数。2025-05-09 争议风暴另页，谓词独立才写。

## 2026-09-12（续 97–98）

- 博物馆 Ethereum Sepolia 2024-03：Engine API 沿用各家 HTTP RPC 尺寸。单笔低于入池上限、gas 上限内，仍能拼出多数拒、少数收的块；把各家收到同一低值后，许多小交易仍能顶满。链反复重组。
- 不变量 96；语料 C100；反模式 pertx-sold-as-block-rpc；L10.3 第 92 条。
- 博物馆 Polkadot-SDK 2025-05：交易解码深度用满后仍能进块；`check_inherents` 再解整块失败；出块者互踢。深度应当只约束交易，却套在每个 runtime API 参数上。
- 不变量 97；语料 C101；反模式 tx-depth-sold-as-api-depth；L10.3 第 93 条。
- 对照不变量 3 / 45 / 48 / 50 / 63 / 70。不写怎样打磨或怎样套娃。不转官方停链脚本。不抄单笔 / 通道 / gas / 深度数字。

## 2026-09-12（续 95–96）

- 博物馆 Solana 2020-12-04：同槽两份不同块，intake 用槽号当身份，三分区互修不了。Turbine 对同一 (槽, shred 下标) 只传一次。重启丢掉乐观确认段。槽号 ≠ 块身份；乐观确认 ≠ 已 rooted。
- 不变量 94；语料 C98；反模式 slot-sold-as-block-id；L10.3 第 90 条。
- 博物馆 Solana 2025-05-02：ZK ElGamal Proof 程序 Fiat-Shamir transcript 漏哈希部分代数分量，可接受任意证明。只影响 Token-22 机密代币。Token-2022 不必改。无已知利用。
- 不变量 95；语料 C99；反模式 fiat-shamir-sold-as-bound；L10.3 第 91 条。
- 对照不变量 12 / 13 / 28 / 79 / 86 / 87。不写怎样配三分区，不写怎样伪造。不抄槽号 / 官网吞吐 / 客户端版本。

## 2026-09-12（续 93–94）

- 博物馆 Sui 2026-05 Part 1–2：地址余额 + 混合气费。因 `InsufficientFundsForWithdraw` 取消后仍砸币；崩溃在结算把负增量加到零余额上。周四只挡一种取消理由；周五另一种盖住它，同一下溢再崩。
- 不变量 92；语料 C96；反模式 cancel-sold-as-no-debit；L10.3 第 88 条。
- 博物馆 Sui 2026-05 Part 3：DKG 参与不够则本纪元关掉随机性（按设计）；失败裁决未写盘。为打气费补丁重启后忘了已失败；依赖随机性的交易既不执行也不取消；换纪元必须排空该队列 → 空等。一次强制关纪元不是常备能力。
- 不变量 93；语料 C97；反模式 dkg-disabled-sold-as-persisted；L10.3 第 89 条。
- 对照不变量 2 / 5 / 80 / 90 / 91。不写怎样竞态，不写怎样饿死 DKG。不抄 1.72 / 门槛。

## 2026-09-12（续 91–92）

- 博物馆 Sui 2024-11-21：拥塞控制 `assert!` 在估计执行代价为 0 时让全验证者崩溃循环。边角：`TotalGasBudgetWithCap` + 可变共享对象 + 0 条 MoveCall。
- 不变量 90；语料 C94；反模式 zero-cost-sold-as-safe；L10.3 第 86 条。
- 博物馆 Sui 2026-01-14：共识提交在特定 GC 优化路径下分叉；隔离区拒证，停以求安全。无用户可见分叉。RPC 仍读上一份已认证状态。与拥堵无关。
- 不变量 91；语料 C95；反模式 quarantine-sold-as-fork；L10.3 第 87 条。
- 知识树补 M8.1–M8.4 覆盖指针。Solana 2021-09 官方页是初报且与 2022-04-30 同族，不另立。
- 对照不变量 3 / 9 / 37 / 88 / 89。不写怎样拼 0 条 MoveCall，不写怎样踩 GC。不抄 ⅓ / 15 分钟。

## 2026-09-12（续 89–90）

- 博物馆 Solana 2024-02-06：旧加载器账户不保留部署槽，`LoadedPrograms` 用哨兵有效槽 0；驱逐后再编译插在卸载条目后面，回放无限再编译。v1.17 协作加载让触发交易进块；当时超过 95% 跑 1.17。止血是重启当下禁止 v2 再部署，不是缓存已修。
- 不变量 88；语料 C92；反模式 sentinel-slot-sold-as-visible；L10.3 第 84 条。
- 博物馆 Solana 2022-04-30：入站约每秒 600 万、个别节点超 100 Gbps。官方写没有 DoS 证据，指向固定地板价 NFT 竞速。停的具体原因是票不够最终更早的块，废弃分叉清不掉，节点 OOM；重启后分叉仍超能力。
- 不变量 89；语料 C93；反模式 flood-sold-as-halt；L10.3 第 85 条。
- 对照不变量 32 / 43 / 45 / 67 / 87。不写部署—驱逐—再引用，不写怎样灌包。不抄 95% / 600 万 / 100 Gbps / 2000 槽。不要把官网 TPS 当事实。

## 2026-09-12（续 88）

- 博物馆 Solana 2023-02-25 官方降级：恢复 shred 没有父槽元数据，不能像数据 shred 那样按旧父槽滤掉。转发服务坐在 Turbine 过滤前面，送回树里成环。落到 Block Repair；leader 进入 vote-only。
- 约 05:46 UTC 最终确认变慢；在线降级无效；02-26 约 01:28 UTC 手动重启后恢复。没有回滚已最终的经济交易。官方：单靠大块 / 单靠刚过 66% 的 v1.14.16 不够复现。
- 不变量 87；语料 C91；反模式 recovery-shred-sold-as-filtered；L10.3 第 83 条。停链面地图加「看起来像停」一行。
- 对照不变量 36 / 69 / 85 / 86。不写怎样造远父槽大块。不抄 400 / 160 秒 / 66%。

## 2026-09-12（续 87）

- 博物馆 Solana 2022-09-30 官方停机：热备与主节点同一身份同时出块；槽 221 正确版本已确认，fork selection 不让往上建。票还在、根不前进，随后停。不重启恢复失败。
- 约 22:41 UTC 停，次日约 06:57 UTC 协调重启后恢复。补丁回移 v1.10.40 / v1.13.2。无 CVE。
- 不变量 86；语料 C90；反模式 confirmed-dup-sold-as-parent；L10.3 第 82 条。停链面地图加一行。
- 对照不变量 4 / 12 / 36 / 69 / 85。不写怎样踩 221 边角。不抄 80/90。同一身份两台不是高可用。

## 2026-09-12（续 86）

- 博物馆 Solana 2022-06-01 官方停机：失败的 durable nonce 可被处理两次。运行时把它当普通 recent-blockhash 交易，nonce 未推进；用户重提后一边收一边拒。超过 33% 接受，不够 66% 对齐。
- 约 16:30 UTC 停出块，重启后 durable nonce 暂时关闭，约 21:00 UTC 恢复。与 1.10 / 1.11 无关。v1.9.28 / v1.10.23 关闭该功能。无 CVE。
- 不变量 85；语料 C89；反模式 durable-nonce-sold-as-consumed；L10.3 第 81 条。停链面地图加一行。
- 知识树补 M6.1–M6.5 覆盖指针。L6.1 / L6.4 / Solana 档案第 15 节互指本页。
- 对照不变量 3 / 4 / 69 / 77 / 82。不写怎样走双路径。不抄 33/66。第一版可以不提供不过期 nonce。

## 2026-09-12（续 85）

- 停链面地图：`tracks/failure-museum/worked-example-halt-surfaces.md`。不新增事故，只把已归档的停拆开。
- 「停链」不是一种事故。说明书停（73）≠ EndBlocker 错（71）≠ 溢出停（74）≠ 空户口（75）≠ 非确定（77/82）≠ 版本差（79/83 运维句）。锁钱不是停。
- 不变量 84；语料 C88；反模式 halt-sold-as-one-kind；L10.3 第 80 条。
- Huckleberry：ibc-go 官方 GHSA 404，不靠第三方 vuln DB 补写。cosmos/security ASA 表里能独立成句的均已归档。

## 2026-09-12（续 84）

- 博物馆 Barberry / GHSA-j2cr-jc39-wpx5（徽章 Moderate；论坛 high-severity）：攻击者可把受害者账户初始化成恶意定期归属，允许存款不允许取款，入金被永久锁住。
- 无绕过。回移了定期归属的更早线也受影响。论坛：33%+1 不受该洞影响；66%+1 才不会因版本不一致停。
- 不变量 83；语料 C87；反模式 empty-addr-sold-as-untyped；L10.3 第 79 条。
- 对照不变量 75 / 81 / 14。不写怎样初始化。不抄 33/66。第一版可以不装定期归属。

## 2026-09-12（续 82–83）

- 博物馆 Elderflower：Authz 管道漏掉一次 `ValidateBasic()`，可能造出无效状态转移，或可通胀或盗窃。官方 critical。补丁打在 Dragonberry 公开包里。
- 不变量 81；语料 C85；反模式 authz-sold-as-validated；L10.3 第 77 条。
- 博物馆 Jackfruit / CVE-2021-41135 / GHSA-2p6r-37p9-89p2（High）：`Grant.ValidateBasic()` 读节点本地钟，临近过期可停链。资金安全。修法是删掉这次检查。
- 不变量 82；语料 C86；反模式 local-clock-sold-as-validatebasic；L10.3 第 78 条。
- 两句都对照：漏检查 ≠ 检查读钟。不写怎样绕过，不写过期如何间隔。不抄 authz。第一版可以不装授权代发。

## 2026-09-12（续 81）

- 博物馆 ASA-2023-001 / GHSA-23px-mw2p-46qm（正文 Medium，徽章 Moderate）：Cosmovisor < v1.0.0 可 DoS；打开 `DAEMON_ALLOW_DOWNLOAD_BINARIES`（非默认）可走宿主机 RCE。
- 官方文档：该开关本意给全节点不是验证者；校验和默认不强制。分叉 SDK 在能升之前应停用 Cosmovisor。
- 不变量 80；语料 C84；反模式 download-sold-as-upgrade；L10.3 第 76 条。
- 对照 L9.4 / 不变量 14 / 79。不写怎样触发下载。不把管家写成共识。

## 2026-09-12（续 80）

- 博物馆 Dragonberry：ICS-23 描述语言缺 soundness，伪造缺席证明可让同一笔 ICS-20 既成功又失败，托管可被迭代抽空。官方标 critical。
- 升 SDK 还必须加 ics23 replace；最初公开的 replace 写错过。+⅓ 打补丁后利用变成可见停链，不是谓词已齐；100% 才算修完。无 CVE。
- 不变量 79；语料 C83；反模式 ics23-sold-as-sound；L10.3 第 75 条。
- 对照不变量 12 / 13 / 66 / 77 / 78。亲戚 Elderflower（Authz 漏 ValidateBasic）不另立。不写怎样伪造证明。不抄 ⅓。第一版可以不装 IBC。

## 2026-09-12（续 79）

- 博物馆 ASA-2024-007 / GHSA-j496-crgh-34mx（Critical）：ibc-hooks 的 `OnTimeout` 可能在包承诺删除前再执行同一 `MsgTimeout`，ICS-20 超时逻辑可能递归，托管可能丢资金或意外铸币。
- 须同时开 IBC、CosmWasm 上传、ibc-hooks 包裹 ICS-20。许可上传不是已安全。
- 不变量 78；语料 C82；反模式 timeout-hook-sold-as-atomic；L10.3 第 74 条。
- 对照不变量 77 / 9 / 2。不写怎样重入。不抄 CosmWasm。第一版可以不装挂钩。

## 2026-09-12（续 78）

- 博物馆 ISA-2025-001 / GHSA-4wf3-5qj9-368v 与 ASA-2025-004 / GHSA-jg6f-48ff-5xrw：IBC acknowledgement JSON 反序列化非确定可停链。
- 能开 IBC 通道的用户可引入。后一页把保护扩到 transfer 之外的所有应用。绕过是许可制开通道。
- 不变量 77；语料 C81；反模式 ack-json-sold-as-deterministic；L10.3 第 73 条。
- 对照不变量 3 / 70 / 71。不写怎样构造 ack。不抄中间件。第一版可以不装 IBC。

## 2026-09-12（续 77）

- 博物馆 ASA-2024-010 / GHSA-7225-m954-23v7（High）：`sdk.Int` 与 `sdk.Dec` 位宽不对齐，Dec 进 Int 可能 panic。
- 官方：1.3.0→1.4.0 可只改依赖、不必硬分叉；低于 1.3.0 升到 >=1.3.0 须先协调升级。
- 不变量 76；语料 C80；反模式 intdec-sold-as-aligned；L10.3 第 72 条。
- 对照不变量 7 / 51 / 74。不写位宽数字。不把 IBC-Go / tokenfactory 写成不确定已选。

## 2026-09-12（续 76）

- 博物馆 ASA-2024-003 / GHSA-4j93-fm92-rp4m（正文 Low，徽章 Moderate）：可在被挡地址上建定期归属账户，例如未初始化模块账户。
- 该账户若被 Begin/EndBlock 的 `GetModuleAccount` 叫到，可能停链。附录：authz / feegrant 变体。
- 不变量 75；语料 C79；反模式 blocked-sold-as-initialized；L10.3 第 71 条。
- 对照不变量 71 / 73 / 74。不写怎样挂归属。不把「并不常见」写成已安全。

## 2026-09-12（续 75）

- 博物馆 ISA-2025-005 / GHSA-p22h-3m2v-cmgh（High）：向 Validator Rewards pool 恶意存款可导致整数溢出并停链。
- 恶意验证者可与 `x/distribution` 交互引入该状态。无已知绕过。咨询未给 CVE。
- 不变量 74；语料 C78；反模式 pool-overflow-sold-as-amount-only；L10.3 第 70 条。
- 对照不变量 7 / 51 / 71 / 73。不写怎样存款。不抄版本号。

## 2026-09-12（续 74）

- 博物馆 x/crisis / GHSA-qfc5-6r3j-jj22（Low）：`MsgVerifyInvariant` 本应 panic 停链，但交易内 panic 被恢复，节点继续出块。
- EndBlock 周期检查才会停开了 `--inv-check-period` 的节点。官方不修，模块将弃用；需要真停则链下协调。
- 不变量 73；语料 C77；反模式 halt-msg-sold-as-halt；L10.3 第 69 条。
- 对照不变量 71。不抄检查周期。不写怎样触发不变量失败。

## 2026-09-12（续 73）

- 博物馆 ASA-2024-005 / GHSA-86h5-xcpx-cfqc（Low）：参与拜占庭行为的委托，在验证者尚未被罚没时，可能通过再委托躲开待执行惩罚。
- 不变量 72；语料 C76；反模式 redelegate-sold-as-wash；L10.3 第 68 条。
- 对照不变量 21 / 26 / 46。咨询未给 CVE。不写怎样再委托。不把 Low 写成可忽略。

## 2026-09-12（续 72）

- 博物馆 ISA-2025-002 / GHSA-47ww-ff84-4jrg（High）：群组模块恶意提案会在 end blocker 触发错误，可能导致整条链停摆。
- 能与 `x/group` 交互的用户集合可引入该状态。咨询写无已知绕过。未给 CVE。
- 不变量 71；语料 C75；反模式 endblocker-error-sold-as-skippable；L10.3 第 67 条。
- 亲戚 ASA-2025-003（除零停链）不另立不变量。对照不变量 58 / 60 / 70。不写提案怎么拼。不抄模块名。

## 2026-09-12（续 71）

- 博物馆 ASA-2024-0012 / ASA-2024-0013 / GHSA-8wcc-m6j2-qxvm（High）：深嵌套包解码可能栈溢出停网；嵌套消息在 `UnpackAny` 上可指数消耗 CPU/内存。
- `max_tx_bytes` 限制外层交易，不应用于 wasm 合约或恶意验证者块放出的内部消息。
- 不变量 70；语料 C74；反模式 maxtxbytes-sold-as-nested-bound；L10.3 第 66 条。
- 对照不变量 33 / 48 / 51 / 60 / 63。咨询未给 CVE。不写怎样嵌套。不抄递归深度。

## 2026-09-12（续 70）

- 博物馆 ASA-2024-002 / GHSA-2557-x9mg-76w8（Medium）：默认 `PrepareProposalHandler` 配默认 `SenderNonceMempool`，单一发送者在某些条件下放入多笔序号不连续的交易，可能提出非法块，出块减少。
- 官方定性 DoS。咨询未给 CVE。
- 不变量 69；语料 C73；反模式 nonce-gap-sold-as-proposal；L10.3 第 65 条。
- 对照不变量 33 / 63 / 68。不写怎样排不连续序号。不抄版本号。

## 2026-09-12（续 69）

- 博物馆 ASA-2024-006 / GHSA-95rx-m9m5-m94v（High）：默认 `ValidateVoteExtensions` 按提议者注入的扩展推断总投票权。
- 不诚实提议者可能改掉注入物里每人的权重，状态按假权重量写。修法是对照状态机核对。
- 不变量 68；语料 C72；反模式 extension-sold-as-voting-power；L10.3 第 64 条。
- 对照不变量 34 / 57 / 58 / 65。咨询未给 CVE。不写怎样改注入字段。不抄 CVSS。

## 2026-09-12（续 68）

- 博物馆 CVE-2020-5303 / Lavender / GHSA-v24h-pjjv-mcp6（High）：不限制 P2P 连接请求，每条分配内存，临时尖峰可 OOM。
- Mempool 在 Peer 诞生前失败时 RemovePeer 先于 AddPeer，`activeIDs` 只增不减，到顶 panic。DoS 2 独立于 DoS 1。
- 修法：请求数限制为 max inbound + unconditional；`InitPeer` 在连接启动前认领 ID。咨询当时不按 IP 限速握手，也不限速 HTTP(S)。
- 不变量 67；语料 C71；反模式 inbound-cap-sold-as-handshake；L10.3 第 63 条。
- 对照不变量 48 / 50 / 45 / 49。不抄 XXX 字节或 65535。不写怎样打满握手。

## 2026-09-12（续 67）

- 博物馆 Alderfly / GHSA-f3w5-v9xx-rp8p（Moderate）：官方 forward lunatic / FLA。⅓+ 拜占庭为尚未出现的高度签任意应用状态。
- 常见证据只在同高冲突块时形成；目标朝前可能来不及出冲突块。补丁前轻客户端可从 primary 收下坏头，secondary 全对也形不成证据。
- 成功 FLA 可能导致 IBC 丢资金；咨询写只在安全模型外才能成功，仍须检测惩罚。`FetchBlock` 加时间让停链后仍能上报。
- 不变量 66；语料 C70；反模式 verified-sold-as-evidence；L10.3 第 62 条。
- 对照不变量 20 / 21 / 64。不编 CVE。不写怎样签朝前高度。不抄 ⅓ 当门槛。

## 2026-09-12（续 66）

- 博物馆 CVE-2020-15091 / Syringa / GHSA-6jqj-f58p-mrw3（Moderate）：提议者可把错误块的签放进 Commit；复用 chainID 时诚实者也会误收，全网提案非法、可停。
- 执行块若凑齐 +2/3 就停验，其余槽位可填任意数据并声称「他们也签了」。应用信任引擎验 LastCommit，按 LastCommitInfo 发奖会看见假证人。
- 修法：创建 Commit 前确认所有签属于那块；执行时验完全部签。咨询脚注：轻客户端不验 nil 票，2/3+ 就退出。
- 不变量 65；语料 C69；反模式 quorum-sold-as-all-signed；L10.3 第 61 条。
- 对照锁（4）、证据身份（64）、块 Time 两条路径（61）。不写怎样塞错块签。不抄 Gaia 奖金。

## 2026-09-12（续 65）

- 博物馆 CVE-2021-21271 / Mulberry / GHSA-p658-8693-mhvg（High）：consensus reactor 在当前块仍飞行时用这块的 last commit 给 `DuplicateVoteEvidence` 打 `Timestamp`。
- 同一双签、两份身份；只有一份进块，其余诚实者继续提案非法证据、可能被断开。官方原文：双签变成 DoS 向量。
- 修法是把两张票交给 `EvidencePool` 再拼。无绕过。
- 不变量 64；语料 C68；反模式 inflight-sold-as-evidence-id；L10.3 第 60 条。
- 对照不变量 21（形状≠slash）、46（默认窗）、61（块 Time 两条路径）、sidecar 可改写。
- 不写怎样让 last commit 对不上。不抄版本号当常量。

## 2026-09-12（续 64）

- 博物馆 ASA-2023-002 / GHSA-hq58-p9mv-338c（Low）：仓库默认 `BlockParams.MaxBytes` 对常见用例偏大，顶满时增加带宽与延迟，可能减少第一轮参与、再开一轮。
- `timeout_propose` 必须对照该上限。官方确认超限提案不被接受。无代码补丁把默认改成「已安全」。
- 不变量 63；语料 C67；反模式 maxbytes-sold-as-sla；L10.3 第 59 条。
- 对照不变量 46（默认证据窗）、47（timeout_commit）、48（接收分配）、52（应用 delay）、证据体积 MaxBytes。
- 不抄示例兆字节。不编 CVE。不是直接丢资金的洞。

## 2026-09-12（续 63）

- 博物馆 ASA-2025-001 / GHSA-22qq-3xwm-r5x4：同一对等节点先报更高 `latest` 再报更低，同步者无限追那个高值；断开也不重算。
- 最初 Medium，2026-03-06 官方改口 Informational；页现 Low。须恶意代码。p2p ban 是部署止血。
- 不变量 62；语料 C66；反模式 peer-latest-sold-as-tip；L10.3 第 58 条。
- 亲戚 ASA-2024-008 不另立谓词。不抄示例高度。不编 CVE。

## 2026-09-12（续 62）

- 博物馆 CSA-2026-001 Tachyon / GHSA-c32p-wcqj-j677（Critical）：BFT Time 实现里验 commit 签名与推导 Time 不一致。
- 打破咨询原文：故障进程不能任意抬高 Time。无绕过。对照规范 bft-time.md 的 BFT 属性。
- 不变量 61；语料 C65；反模式 recompute-sold-as-bft-time；L10.3 第 57 条。
- 不发明两条路径差在哪一字段；不写怎样抬高；不编 CVE。

## 2026-09-12（续 61）

- 博物馆 ASA-2025-003 / GHSA-hrhf-2vcr-ghch（High）：`BitArray` 的 `Bits` 与 `Elems` 数量对不上时，以前验证不够。
- 官方最坏：先把非法状态流言给邻居，再自己处理 → 网络停，而不是只有接收者崩。
- 不变量 60；语料 C64；反模式 bitarray-sold-as-gossip-ok；L10.3 第 56 条。
- 对照不变量 59 / 57 / 45。咨询未给 CVE。iptables ban 是部署止血。
- 不写怎样拼对不上的位图。

## 2026-09-12（续 60）

- 博物馆 ASA-2025-002 / GHSA-r3r4-g7hq-pq4f（High）：以前不验 `Part.Index == Part.Proof.Index`。用另一片的证明仍接受。
- 官方后果：再流言无效片；标已收到并抑制正确片。修法是强制两下标相等。无绕过。
- 不变量 59；语料 C63；反模式 part-index-sold-as-proof-index；L10.3 第 55 条。
- 对照不变量 12 / 37 / 39 / 36。咨询未给 CVE。
- 不写对调证明；不抄分片字节大小。

## 2026-09-12（续 59）

- 博物馆 ASA-2024-001 / GHSA-qr8r-m495-7hc4（High）：ABCI2 链上治理改 `VoteExtensionsEnableHeight`，当时验证处理不了这次提案，节点可能 panic，网络停。
- 修法是改进该参数在治理路径上的验证。软补丁超过 66.7% 投票权只缓解本条利用。
- 不变量 58；语料 C62；反模式 enable-height-sold-as-safe；L10.3 第 54 条。
- 对照不变量 34（拒扩展丢票）、57（快路径下标）、35（集合延迟）。咨询未给 CVE。
- 不写提案怎么拼；不发明具体漏检行；不抄 66.7% 当法定人数。

## 2026-09-12（续 58）

- 博物馆 ASA-2024-011 / GHSA-p7mv-53f2-4cwj（High）：启用扩展时，Precommit 非空的扩展处理插在普通 Vote 验证之前，不复查 `ValidatorIndex`，接收节点 panic。
- 官方：须发送端恶意代码；上游发不出不存在的下标；默认关扩展则不受影响。绕过是 p2p ban，不是谓词。
- 不变量 57；语料 C61；反模式 extension-path-sold-as-checked；L10.3 第 53 条。
- 对照不变量 34（拒扩展丢票）、37（断言）、43（提前 return）。咨询未给 CVE。
- 不写下标怎么造；不抄版本号或 CWE。

## 2026-09-12（续 57）

- 博物馆 ASA-2024-009 / GHSA-g5xx-c4hv-9ccc（Medium）：state sync 用轻客户端算共识 `State` 时，当时不比 `ProposerPriority`。
- 无效提议者状态 → 认错「该谁出块」；多人如此则网络停。补丁：priority 不同则同步失败。
- 不变量 56；语料 C60；反模式 apphash-sold-as-proposer；L10.3 第 52 条。
- 对照不变量 38（AppHash）、20（跳过重叠）、46（证据窗）。咨询未给 CVE。
- 不写怎样改本地库；不抄版本号或 CVSS。

## 2026-09-12（续 56）

- 博物馆 CVE-2024-52918（Medium）：Bitcoin-Qt 打开 BIP72 URI 按 `r` 远程取 payment request；大文件分配到崩溃。受害人须打开该 URI。
- 官方修法是整段去掉 BIP70（#17165，0.20.0），不是加下载配额。
- 不变量 55；语料 C59；反模式 uri-fetch-sold-as-verify；L10.3 第 51 条。
- 对照 P2P 接收（48）、SOCKS 跳（54）、UPnP（53）、RPC 绿勾。
- 不写 URI 怎么拼；不复现 PoC。

## 2026-09-12（续 55）

- 博物馆 CVE-2017-18350：恶意 SOCKS 可在 signed `char` 平台覆写栈。须先配置代理才脆弱。官方另写：不安全网络上的任意代理本身就可被截获。
- 隐蔽修复进 v0.15.1（#11397）：哑缓冲改成显式无符号类型。公告未标严重度。
- 不变量 54；语料 C58；反模式 proxy-sold-as-peer；L10.3 第 50 条。
- 对照 UPnP（53）、P2P 接收分配（48）、写盘前平台宽度（51）。
- 不写握手回复怎么拼；不抄缓冲长度或高位区间；不把栈覆写写成已发生主网 RCE。

## 2026-09-12（续 54）

- 博物馆 CVE-2015-20111（Medium）：miniupnpc 溢出可泄数据；与 6031 合在一起**可能** RCE。公告：未直接泄漏私钥；演示手法不能直接搬到 Bitcoin Core。
- 0.11.1 官方：默认关 UPnP，以免以后的库洞变成全网结构风险。CVE-2024-52917（Low）：只有打开 `-miniupnp` 才受局域网 OOM。
- 不变量 53；语料 C57；反模式 upnp-sold-as-must；L10.3 第 49 条。
- 不写利用步骤；不把 RCE 写成已在 Bitcoin Core 发生。

## 2026-09-12（续 53）

- `next_block_delay` 精读：现行 `main` FinalizeBlock 回包字段 6，规范标 Deterministic = No。语义仍是 Commit 之后再等，以前是本地 `timeout_commit`。
- ADR-115 Accepted：恒定出块间隔做不到；不要做成 ConsensusParams。不是所有发布线都有该字段。
- 不变量 52；语料 C56；反模式 app-delay-sold-as-slot；L10.3 第 48 条。
- 不抄规范 1s / ADR 示例秒数。不把 ADR 里的应用链名字写成那些链的规范保证。

## 2026-09-12（续 52）

- 博物馆 CVE-2025-46597：32-bit 写盘前尺寸检查对超大块溢出。Low。不能走 BLOCK；理论上 compact + 非默认超大内存池。
- 落地修法是间接卡住 32-bit `-maxmempool`。卡住旋钮 ≠ 溢出谓词已改成固定宽度。
- 对照 2015-3641（接收分配）、35202（部分块断言）、52919（递增 ID）。
- 不变量 51；语料 C55；反模式 mempool-cap-sold-as-width；L10.3 第 47 条。
- 不抄 GB / GiB / `-maxmempool` 数字。不写拼块步骤。不把后续 `size_t` 讨论写成公告原文。

## 2026-09-12（续 51）

- 博物馆 CVE-2020-14198：封禁 IP 表无上限，对手可灌（IPv6 便宜）；GETADDR 对每条待返回地址扫全表。High。
- 后来拆成手动 ban 与自动 discourage（有界、不可枚举）。对照 52919（递增 ID）、52915（发送缓冲）、2015-3641（接收）、25220（头索引）。
- 不变量 50；语料 C54；反模式 autoban-sold-as-bound；L10.3 第 46 条。
- 不抄 GETADDR 返回 2500。不写如何灌 IPv6。

## 2026-09-12（续 50）

- 博物馆 CVE-2024-52919：地址表递增 `nIdCount` 回绕触发断言。同一 CVE 两份披露：v22.0 限速（High）≠ v29.0 改 64-bit 宽度（Low / part 2）。
- 限速只改代价，不是回绕谓词。对照 2015-3641（接收）、52915（发送）、14198（封禁表，另页）、35202（部分块断言）。
- 不变量 49；语料 C53；反模式 rate-limit-sold-as-width；L10.3 第 45 条。
- 不抄「每 10 秒 1 条」「1000 个对等节点」「一年以上」。不写灌 `addr` 步骤。

## 2026-09-12（续 49）

- 超时精读：规范里超时是本地等待。成功一轮里「必须等」的只有 `timeout_commit`，且它是 **Commit 之后**再收迟到 precommit。Commit 步等的是块到齐，不是 timeout_commit。
- `skip_timeout_commit=true` 官方语义 = 像 TimeoutCommit=0。PR #2892 在较新的线上删该键；现行 `main` 的 `config.go` 仍可能保留（Deprecated）。不把「键还在 / 已删」写成另一套共识。
- 博物馆 CVE-2015-3641：最大序列化长度被当成接收分配上限。Medium。修法是读完载荷前收紧。后来 BIP144 调大该上限 ≠ 洞又开了。
- 对照 52915（发送缓冲）、54605（日志盘）、25220（头索引）。
- 不变量 47–48；语料 C51–C52；反模式 timeout-commit-sold-as-finality / max-msg-sold-as-recv-quota；L10.3 第 43–44 条。
- 已修：L4.2 曾把「超时数字」写成协议参数。
- 不抄文档秒数、Alice/Bob 玩具、「大约每秒一个空块」、32/2/4 MiB。

## 2026-09-12（续 48）

- 证据窗精读：过期是高度**且**时间。`> 0` 不是盖住解绑。
- 博物馆 ASA-2024-004 / GHSA-555p-m4v6-cqxv：默认 MaxAge 可能短于解绑；Low；affected all；无代码补丁。
- 对照不变量 21（谁执行 slash）与 20（信任期必须短于解绑）。证据窗必须长于解绑。
- 不变量 46；语料 C50；反模式 evidence-default-sold-as-unbonding；L10.3 第 42 条。
- 不抄默认块数 / 纳秒 / Cosmos 罚金百分比。

## 2026-09-12（续 47）

- 库存三方向精读：入站 INV（CVE-2024-52915 Medium，回复风暴灌发送缓冲）、入站 GETDATA（CVE-2024-52920 Low，单连接空转）、出站待宣布（2023-05 官方披露 Medium，排序卡住 P2P；spy 节点放大）。
- 三案都不是 52913 / 52922 / 52921。inv-to-send 无 CVE 号，有官方披露即收。
- 不变量 45；语料 C47–C49；反模式 inv-sold-as-free；L10.3 第 41 条。
- 不抄 50000 / 50 MB / 7 笔每秒当不确定常数。不写畸形包构造。

## 2026-09-12（续 46）

- 博物馆 CVE-2024-52911：非法块提前 return，后台脚本检查读已释放的 PrecomputedTransactionData。High。合法路径会 Wait()。修复是去掉提前 return。
- 博物馆 CVE-2025-46598：未确认非标准交易拒了但不踢人，可重复烧 CPU，拖延块传播。Low。对照 52914（已进池才扫孤儿）。
- 不变量 43–44；语料 C45–C46；反模式 early-return-sold-as-joined / reject-without-ban-sold-as-free；L10.3 第 39–40 条。
- 不写块构造或二次哈希脚本；不把「几秒」抄成不确定常数；不把 RCE 写成已发生。

## 2026-09-12（续 45）

- 博物馆 CVE-2025-54605：健全性失败或检查点前分叉被拒后，无条件日志仍可灌满磁盘。Low。修复是全库日志限速，不是改共识。
- 亲戚 CVE-2025-54604：伪造自连接打同一类无条件日志，同一 PR #32604。
- 对照 25220（头索引）、35202（断言崩）、52921（清别人下载）。拒绝 ≠ 不占磁盘。
- 不变量 42；语料 C44；反模式 reject-sold-as-no-disk；L10.3 第 38 条。
- 知识树补一批覆盖指针（课文已在、树节点只剩标题的必学/重要项）。
- 不抄每源每小时字节当不确定常数。不写造块步骤。

## 2026-09-12（续 44）

- Bitcoin MTP 精读：太早看父块 GetMedianTimePast（time-too-old / INVALID_HEADER）。BIP 113 之后 locktime 也看父 MTP，不看本块 nTime。太新看本节点钟 + 命名宽限（time-too-new / TIME_FUTURE）。
- 三把尺都不是 PBTS / BFT Time / 调整钟公式。调整钟打的是太新那条实现路径。
- 不变量 41；语料 C43；反模式 mtp-sold-as-one-clock；L10.3 第 37 条。树 M3.1 补覆盖指针。
- 不抄 nMedianTimeSpan / MAX_FUTURE_BLOCK_TIME 当不确定常数。

## 2026-09-12（续 43）

- PBTS 精读：块时间是提议者本地钟；timely 相对本节点收到 Proposal 的窗子；不 timely → prevote nil。已在更早轮拿到 +2/3 prevote 再提议的块不再验 timely。启用后不能关。
- 对照 BFT Time（LastCommit 加权中位数，可复算）、Bitcoin MTP、实现对等调整钟（CVE-2024-52912）。四把尺不是「墙上现在」。
- 不变量 40；语料 C42；反模式 pbts-sold-as-mtp；L10.3 第 36 条。
- 不抄 PRECISION / MSGDELAY 默认毫秒，不抄 BFT Time 的 1 ms 当不确定常数。规范仍开放「乱填时间能否罚」。

## 2026-09-12（续 42）

- 博物馆 CVE-2024-52921：未请求的变异块可清掉其他对等节点的 compact 重建状态。Medium。
- 对照 2012-2459（同根共识）、52922（卡住）、35202（断言崩）。下载状态必须按 (对等节点, 对象) 隔离。
- 不变量 39；语料 C41；反模式 mutated-clears-others-download；L10.3 第 35 条。
- 不写变异构造。

## 2026-09-12（续 41）

- ABCI state sync 精读：装应用快照、不重放历史块。OfferSnapshot 只有轻验 AppHash 可信；Snapshot.hash / metadata 可伪造。
- 对照 assumeutxo（背景全验）、assumevalid、弱主观、BFT 轻跳过。
- 不变量 38；语料 C40；反模式 statesync-sold-as-genesis；L10.3 第 34 条。
- 不抄分块上限、最近快照条数。

## 2026-09-12（续 40）

- 博物馆 CVE-2024-35202：部分块重建失败后实例未清，第二次 `blocktxn` 断言崩节点。High。碰撞不得罚对等节点。
- compact 精读：拼出一块 ≠ 共识验块。对照 52922（卡住）与 2012-2459（同根）。
- 不变量 37；语料 C39；反模式 assert-sold-as-peer-filter；L10.3 第 33 条。
- 不写触发字节；不把短 ID 长度当共识。树 M9.3 补覆盖指针。

## 2026-09-12（续 39）

- 集合生效延迟：H 的 `validator_updates` 在 H+2 才计票；H+1 只更新 `NextValidatorsHash`；H+3 才带进 last_commit。参数更新是另一条（H→H+1）。
- 博物馆 CVE-2024-52922：宣布新块后单一对等节点可卡住传播。宣布 ≠ 已收到；对象是块，不是未确认交易。
- 不变量 35–36；语料 C37–C38；反模式 validator-update-sold-as-immediate / announce-sold-as-received；L10.3 第 31–32 条。
- 不抄解绑天、等待秒数、并行路数当共识。

## 2026-09-12（续 38）

- Vote extension 精读：非空 precommit 才扩展；`CanonicalVoteExtension` 是另一份签；Verify REJECT 丢掉整张票，不是块非法。
- Req 10：`s_h` 不得依赖本高度收到的扩展；最早 *h+1* Prepare 才用。
- 不变量 34；语料 C36；反模式 vote-extension-sold-as-block；L10.3 第 30 条。
- 不抄启用高度、SDK 预言机产品。第一版建议可不启用。

## 2026-09-12（续 37）

- ABCI++ 四门精读：CheckTx（池）≠ PrepareProposal（可改列表，可不确定）≠ ProcessProposal（不可改，必须确定，REJECT = prevote nil）≠ FinalizeBlock+Commit。
- 对照 Builder API：Prepare 是本验证者应用回调，不是域外 PBS。
- 不变量 33；语料 C35；反模式 checktx-sold-as-prepared；L10.3 第 29 条。
- 不展开 vote extension 全文。不抄默认 max_tx_bytes、propose 超时、SDK 版本。

## 2026-09-12（续 36）

- 博物馆 CVE-2024-52914：进池后二次扫描孤儿，可卡住数小时。修复是匹配一次就让出。
- 对照 52913（看不见）与头垃圾（内存）。不变量 32；语料 C34。
- 不写昂贵无效孤儿构造；不把缓存上限当共识。

## 2026-09-12（续 35）

- 博物馆 CVE-2019-25220 + 亲戚 CVE-2024-52916：低难度头可填爆索引。24.0.1 先验工作量再入库。
- 检查点历史三职：强迫块在链上、跳脚本（0.14 拆给 assumevalid）、挡头垃圾。
- 不变量 31；语料 C33；反模式 cheap-header-sold-as-free。不抄攻击成本 BTC。

## 2026-09-11（续 34）

- 博物馆 CVE-2024-52912：`version` 时间偏移溢出 + `abs64(INT64_MIN)` 绕过上限，拒收规范新块。不是日蚀，不是分区。
- 博物馆 CVE-2024-52913：有界 already-asked 表让 `GETDATA` 被单一对等节点独占。看不见未确认 ≠ 共识非法。
- 不变量 29–30；语料 C31–C32；反模式 adjusted-clock-sold-as-consensus / unseen-mempool-sold-as-invalid。
- 加密内存池：无冻结规范，明确不写页。不附利用构造。

## 2026-09-11（续 33）

- Starknet 仅过滤器：SNOS 把「块有效」写成点名 Cairo 程序；Core 登记 `programHash`。v0.13.2 起还要 applicative bootloader。
- `ACCEPTED_ON_L2` ≠ `ACCEPTED_ON_L1`。状态差 DA ≠ 「有证明就不用数据」。
- 不变量 28；语料 C30；反模式 l2-accepted-sold-as-l1；L10.3 第 24 条。
- 不抄吞吐口号、TVL、现行 hash。zkSync 仍无独立对象。

## 2026-09-11（续 32）

- 谁排序精读：ethereum/builder-specs。提议者可只签 `ExecutionPayloadHeader`，交易列表事后揭示。Builder API 不是 `process_block`。
- 对照本地出块 / 协议内 PBS（合并时不存在）/ Monad「定序 ≠ 交差根」。
- 不变量 27；语料 C29；反模式 builder-sold-as-consensus；L10.3 第 23 条。
- 不抄 MEV 金额、中继占比；不把 enshrined-PBS 草案当已激活。

## 2026-09-12（续 31）

- Casper 罚没精读：phase0 `is_slashable_attestation_data` 的 double / surround（容器顺序不对称）；同 slot 双头的 proposer slashing；信标状态执行 `slash_validator`。
- 对照 CometBFT 证据≠罚没、Altair 同步委员会无同一套 slash、EigenLayer AVS 可主观。
- 不变量 26；语料 C28；反模式 two-votes-sold-as-slash；L10.3 第 22 条。
- 不抄罚金商、现网验证者人数、罚没总额。

## 2026-09-12（续 30）

- assumevalid 精读：Bitcoin Core 0.14.0。跳祖先脚本/签名，不强迫那条链；`-assumevalid=0` 全验。旧 checkpoint 才要求块在链上。
- assumeutxo：UTXO 快照 + 背景 chainstate 验到基块并核编译哈希。不是弱主观周期。
- 不变量 25；语料 C27；反模式 skip-sold-as-full-verify；L10.3 第 21 条。
- 不抄 IBD 耗时与发行默认哈希。

## 2026-09-12（续 29）

- 弱主观性精读：phase0 `weak-subjectivity.md`。检查点是任意 `Checkpoint`；周期由 churn 算出，下限 256 epoch；对不上路径应退出。分发节未写完。
- 对照 CometBFT `trustingPeriod`。不变量 24；语料 C26；反模式 stale-checkpoint-sold-as-genesis。
- L10.3 第 20 条。不抄参考表人数，不把周期换成「多少天」。

## 2026-09-12（续 28）

- blob / DAS 精读：EIP-4844 sidecar + versioned hash + 4096 epoch 服务窗；Fulu PeerDAS 一维 128 列；Celestia 二维纠删另列。
- 不变量 23；语料 C25；反模式 kzg-sold-as-das。
- L10.3 建议清单第 19 条。L5.4 / L7.2 / L9.6 / Ethereum / Celestia 档案互指。
- 不抄现行每块 blob 个数；不以 EIP 动机段的「1/8」覆盖规范常量。KZG 不是后量子。

## 2026-09-12（续 27）

- Altair 同步委员会轻客户端精读：512 抽样的 2/3 ≠ 全验证者 2/3；`MIN_SYNC_COMMITTEE_PARTICIPANTS = 1` 是处理下限；EIP-8390 仅草案。
- 反模式 sample-sold-as-full-set；不变量 22；语料 C24。
- EigenLayer 仅过滤器页：restake + AVS 自定、不必客观可归属的罚没。对照 Polkadot / Babylon。无 19 节、不抄 TVL。
- L10.3 建议清单第 17、18 条。通读第 19 步、最终性表、Ethereum 档案互指。

## 2026-09-12（续 26）

- 证据精读：CometBFT `DuplicateVoteEvidence` / `LightClientAttackEvidence`。引擎发现并通知应用，不自动 slash。
- 三种轻客户端攻击分型（lunatic / equivocation / amnesia）只作分类。
- 不变量 21；语料 C23；反模式 evidence-equals-slash。账本第 18 行证据字节公式，数字空。

## 2026-09-12（续 25）

- BFT 轻客户端跳过精读：CometBFT `verification_001_published`。紧邻后继用旧集合 +2/3；跳过用旧 `NextValidators` 的 1/3+。
- 反模式：新委员会自己的 2/3 当成轻客户端信任。
- 不变量 20；语料 C22。L9.6 / L4.5 / CometBFT 档案互指。不抄解绑秒数。

## 2026-09-12（续 24）

- BFT 投票被签字节精读：CometBFT `CanonicalVote`（type / chain_id / 固定宽度）+ 签名器双签纪律；Ethereum phase0 `DomainType` 与 `compute_signing_root`。
- 不变量 19；语料 C21。Prevote 的印不得验成 Precommit。
- L4.2 / L5.2 / 两份档案 / 通读第 10 步互指。phase0 表不是后续分叉全集。

## 2026-09-12（续 23）

- Monad 仅过滤器页：共识先对顺序投票，本块可以没有状态根；延迟 `D` 块根是有效性条件。
- 反模式：顺序最终卖成状态最终。
- 最终性 / 共识表加行。Sei 仍不写页。不抄官网吞吐与执行预算对照。

## 2026-09-12（续 22）

- 域分离三层编码精读：BIP-340 tagged hash（规范公式 + nonce 漏钥警告）、EIP-712 `domainSeparator`（范围不含应用重放）、FIPS 外部 `ctx`。
- 模式 domain-separation、L1.1/L1.2、L3.7、Bitcoin/Ethereum 档案互指。
- 禁止把三种编码说成一句话。

## 2026-09-12（续 21）

- FIPS 204/205 外部 `ctx` 卡：算法层域分离；空默认不是完成；共识只走外部 API。
- hedged 签：同一 `(sk, M, ctx)` 可有两个都真的 σ；授权对象不是 σ 字节。
- 精读空 ctx 双角色；反模式 empty-ctx-two-roles；不变量 18；语料 C20。
- L10.3 建议清单第 13 条；通读第 24 步互指。
- RFC 8554 Table 1 标明为 LM-OTS 叶子，不是 LMS 整签。
- CPU / 决策列仍空。

## 2026-09-12（续 20）

- 有状态哈希签名卡：RFC 8391（先更新再输出、Table 3 名义 \|Sig\|）+ SP 800-208（不适合通用、禁止导出私钥）。
- OTS 复用精读；不变量 17；语料 C19。
- 模式 stateful-hash-signature；反模式 ots-index-reuse。
- QRL 仅过滤器页：节点拒重复 OTS；不写 19 节、不抄 Zond。
- 建议：验证者投票签不要用有状态方案。CPU 仍空。

## 2026-09-12（续 19）

- 博物馆：CVE-2021-39137（Geth RETURNDATA 错根 / 少数分叉；GHSA + 官方 postmortem；不附利用构造）。
- 语料 C18；威胁模型第 9 行（多数客户端同一实现洞）。
- NEAR Nightshade 思想级 19 节：一条链 + chunk；Doomslug 标记 ≠ BFT 谓词。
- 模式 single-chain-chunks；反模式 two-finality-sold-as-one。
- Babylon 仅过滤器页：BTC UTXO 留在 Bitcoin；契约委员会是代价；无 19 节。

## 2026-09-12（续 18）

- L0–L10 每课精密检查补齐五层表（密码学 / 协议 / 实现 / 部署 / 经济）。
- 博物馆精读：同一 CVE-2018-17144，五层各说什么（不新编事故）。

## 2026-09-12（续 17）

- 对抗语料目录 C01–C17（覆盖 M10.5；不是 exams）。
- 不变量 16：PQ-BFT 上主网前必须写出每高度投票字节公式。

## 2026-09-12（续 16）

- PQ 尺寸卡：FIPS 204 / 205 名义公钥与签名长度（非本机实测、非选型）。
- 投票字节精读：64 B → 3309 B → 49856 B 对同一轮票的结构算术。
- 轻节点表补 Nervos 概述中的 light 假设。

## 2026-09-12（续 15）

- 最终性 / 共识 / 并行 / 升级横表随第 8 波回填。
- 分区精读：帘子两边停还是各「到了」。
- 形式化缝：模型有锁，Apply 仍裂根；反模式 model-equals-implementation。
- L10.3 补占用白名单与域分离。

## 2026-09-11（续 14）

- L2.6 状态占用；Nervos CKB 思想级 19 节（容量绑定存储、生成/验证分离、VM 不硬编码密码）。
- 模式 capacity-binds-storage；反模式 one-fee-eternal-state。
- 不变量 12–15（Merkle 唯一、验证明≠供给、升级不改供给、占用有界）。
- 精读：绿测试、日蚀、内存池、域分离。

## 2026-09-11（续 13）

- 博物馆：CVE-2012-2459（Merkle 变异）、CVE-2019-7167（Sprout 伪造币）。
- 反模式：验证明通过所以不能通胀。
- 升级精读：升级钥把 1 改成 2。
- 经济精读：桥里的钱比能罚的多。
- Bitcoin / Zcash 档案第 15 节与通读第 14、22 步互指。

## 2026-09-11（续 12）

- 实现保证横向：编码 / 崩溃精读挂进第四通与相关课。
- L1.6：三种「随机」与 `Apply` 禁骰（补知识树 M1.5）。
- 反模式：`Apply` 里掷骰子。
- 轻节点精读：阿比只看头就放货。
- 覆盖声明：L1 课号映射、L5/L10、L3 八课 / L8 四课计数。

## 2026-09-11（续 11）

- PQ 迁移精读：危急后单旧签、双签自愿、无标签裂链、投票/用户不同步。

## 2026-09-11（续 10）

- 五层失效表补全五列，不再把 Ethereum / 屏蔽挤进「同左」。

## 2026-09-11（续 9）

- 精读实例补完乐观 L2 与屏蔽列，并加同一笔钱的五层失效表。

## 2026-09-11（续 8）

- 生命周期精读：阿安付 1 走 Bitcoin / CometBFT / Ethereum。
- 结算文案纪律：允许句型必须填协议对象 Y。

## 2026-09-11（续 7）

- 通读顺序 `index/04-study-path.md`；新链接待 19 问。
- PQ 迁移状态机 + L10.4；修正「GOAL 21 项」过期句。
- 不变量补迁移与算法标识。

## 2026-09-11（续 6）

- 生命周期五列对照（目的 A）：BTC / BFT / ETH / 乐观 L2 / 屏蔽支付。
- L2.5 eUTXO；L3.8 孤块与 DAG。
- Kaspa、Fuel 19 节（思想/对照）；威胁模型按对手×层展开。
- 反模式：实现上限当共识。

## 2026-09-11（续 5）

- L0–L2 及缺件课文统一补「精密检查」（A41）。
- L3.7 SegWit 软分叉结构；L8.4 电路作为机器（多项式后置）。
- 博物馆 BIP 50（2013 意外分叉）。
- Algorand 19 节（VRF 抽签对照）；模式 vrf-sortition；升级横向表；状态决策表补定性格。

## 2026-09-11（续 4 · 细致 / 精密 / 全面）

- GOAL 追加门禁：必学节点必须有课文、每课精密检查、对照表随波更新。
- 课程：L3 补网络/SPV/文化；L4 补集合变更与 HotStuff/Casper 对照；L5 四课；L6 四课；L7 补 rollup 租户；L8 三课；L9 九课；L10 三课（决策列空）。
- 档案：Zcash / Monero / Mina / 乐观 rollup 品类。
- 横向：最终性、并行、轻节点、密码地图；博物馆 CVE-2010-5139。
- 模式 +2、反模式 +2、不变量 +3；共识决策表加入 Gasper 列。

## 2026-09-11（续 3）

- Celestia / Polkadot 19 节。
- L7 三课：四层、DA、共享安全。
- 模式 DAS；反模式「有头就是结算」。

## 2026-09-11（续 2）

- Sui / Aptos 19 节：三种并行世界观对照写进 Aptos 第 14 节。
- L4 四课：quorum 相交、round/step、锁、ABCI+WAL。
- 锁课强调崩溃后丢失 lock 是安全事故。

## 2026-09-11（续）

- 协议档案：Avalanche（对照）、Solana（五笔账拆吞吐）。
- 课程 L3：Nakamoto 最终性、费用/标准性、保守演化。
- 事故细节仍只在有原文时写；Snow/Solana 停机七问留空。

## 2026-09-11

- 建立 `uncertain-atlas/`，与 `qtb/` 隔离。根 README 仅一行指针。
- 立 GOAL、路线图、知识树、研究顺序、资产目录。
- 写完 Level 0 十课；复审修正 L0.2/L0.6 例子、Turbine 笔误、五层保证提前出题、伪造/偷钥匙混淆。
- 用户改门禁：不出题、先写全知识、架构清晰、不与交易混。
- 目录改为五条轨：`index/` `courses/` `protocols/` `tracks/` `libraries/` `exams/`。
- Level 0 试题迁到 `exams/level-00.md`，正文去掉 K 节。
- 写完 Level 1（哈希/签名/Merkle/规范编码/PQ 工程预告）、Level 2（UTXO/账户/对象/设计地图）。
- 写完 Bitcoin、CometBFT、Ethereum 19 节第一版。
- 模式 8 条、反模式 10 条、决策矩阵空表、威胁模型草稿、6 条 invariant。
- 失败博物馆收 CVE-2018-17144；PQ 工程账本不填未测数字。
