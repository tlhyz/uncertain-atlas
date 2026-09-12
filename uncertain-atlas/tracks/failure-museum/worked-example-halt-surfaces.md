# 实例：「停链」不是一种事故

目的 A + B。不是新馆藏，不新增未核验事故。  
先修：L0.8、L9.9、不变量 71 / 73 / 74 / 75 / 77 / 82 / 85 / 86 / 87 / 88 / 89 / 90 / 91 / 92 / 93 / 94 / 96 / 97 / 98 / 99 / 100 / 101 / 103 / 106 / 107 / 109 / 110 / 114 / 117 / 126 / 127 / 128 / 129 / 130 / 131 / 132 / 133。

产品句里的「我们会停链」如果只写三个字，下一辆车学不到。  
馆藏里至少有七种停，外加两种「看起来像停、其实不是」。必须点名是哪一种。

---

## 事实（只指向已归档页）

| 哪种停 | 可观察后果 | 谁能引入 | 馆藏 | 不变量 |
|---|---|---|---|---|
| 说明书停，交易内没停 | 发了停机消息，节点继续出块 | 能发 `MsgVerifyInvariant` 的人 | [x/crisis](x-crisis-no-halt.md) | 73 |
| EndBlocker 出错，高度停 | 可选模块结尾钩子返回错误，链停 | 能与该模块交互的用户 | [ISA-2025-002](isa-2025-002.md) | 71 |
| 溢出本该拒，却停了 | 入金溢出变成高度停 | 能向奖励池存款的验证者 | [ISA-2025-005](isa-2025-005.md) | 74 |
| Begin/EndBlock 碰到空户口 | `GetModuleAccount` 叫到未初始化被挡账户 | 能挂归属 / authz / feegrant 的人 | [ASA-2024-003](asa-2024-003.md) | 75 |
| 诚实节点两个世界 | 反序列化或入口校验不确定，对不上就停 | 能开 IBC 通道的人；或能发 Grant 的人 | [ISA-2025-001](isa-2025-001.md)、[Jackfruit](jackfruit.md) | 77、82 |
| 失败 durable nonce 当普通交易再重提 | 一边拒块、一边收块；超过 33% 接受、不够 66% 对齐 | 能发 durable nonce 的用户（本页不写怎样） | [2022-06-01](solana-2022-06-01-durable-nonce.md) | 85 |
| 已确认的重复槽赢家不能当父块 | 正确版本已确认，出块者无法往上建；票还在、根不前进，随后停 | 同一身份两台同时出块（热备双活）；边角在实现里 | [2022-09-30](solana-2022-09-30-duplicate-fork.md) | 86 |
| 回放无限再编译 | 旧加载器 JIT 主循环看不见刚编译的条目，无人投票 | 能部署旧加载器程序并让该交易进块的人（本页不写怎样） | [2024-02-06](solana-2024-02-06-legacy-loader-loop.md) | 88 |
| 票不够、分叉清不掉、OOM | 废弃分叉占满内存，重启后仍超能力 | 固定地板价热点上的经济灌包 | [2022-04-30](solana-2022-04-30-fork-cleanup-oom.md) | 89 |
| 拥塞控制估值 0 触发 assert | 全验证者崩溃循环，交易处理停 | 能送可变共享对象且 0 条 MoveCall 的交易（本页不写怎样） | [Sui 2024-11-21](sui-2024-11-21-zero-cost-assert.md) | 90 |
| 检查点隔离拒证 | 提交分叉后无法认证，停以求安全；无用户可见分叉 | 共识提交优化路径在特定 GC 下分叉 | [Sui 2026-01-14](sui-2026-01-14-commit-divergence.md) | 91 |
| 取消后仍砸气费、结算下溢 | 混合气费在取消路径砸币，负增量加到零余额，进程崩 | 两笔同时抢同一地址余额；另一种取消理由可盖住余额不足 | [Sui 2026-05 Part 1–2](sui-2026-05-gas-smash-cancel.md) | 92 |
| DKG 失败未落盘、换纪元排不空 | 按设计关掉随机性，重启后忘了，队列排不空，纪元关不了 | 为打另一补丁而重启；失败裁决只在内存 | [Sui 2026-05 Part 3](sui-2026-05-dkg-verdict-disk.md) | 93 |
| 同槽两块按槽号当同一对象 | 少数分区互修不了，新块确认停；乐观段可被丢掉 | 同槽两份不同块 + intake/repair 用槽号当身份 | [Solana 2020-12-04](solana-2020-12-04-slot-as-block-id.md) | 94 |
| Engine API 尺寸分裂、反复重组 | 多数拒、少数收，头来回跳；提议者丢奖励 | 出块通道沿用各家 HTTP RPC 上限；许多小交易可顶满低档 | [Sepolia 2024-03](ethereum-2024-03-sepolia-engine-rpc.md) | 96 |
| check_inherents 再解整块失败、出块者互踢 | 导入失败当非法，封禁邻居，循环重连 | 交易深度计数器套在 runtime API 整块参数上 | [Polkadot-SDK 2025-05](polkadot-2025-05-runtime-api-decode-depth.md) | 97 |
| 组下标当票下标、缺 inherent | 出块 finalize panic；create_inherent 回 None | 剔除已禁用者时用组座位号去票向量 | [Kusama 2025-08-24](kusama-2025-08-24-group-index-votes.md) | 98 |
| Active 未 Confirmed、GRANDPA 跳过 | 出块可仍在，最终性停 | 禁用后再发起的争议被标 Active | [Kusama 2024-02-15](kusama-2024-02-15-disabled-active-dispute.md) | 99 |
| 链下内存禁用挡不住已确认争议 | 最终性停；训练轮触发但 GRANDPA 已先停 | 版本差争议被确认后仍全员参与；重启清空名单 | [Kusama 2025-05-09](kusama-2025-05-09-offchain-disable.md) | 100 |
| gas 上限内的块执行拖到分钟级 | 出块变慢 / 可能错过槽；官方披露时尚未主网爆发 | 状态访问常数 gas、磁盘随树变深 | [Ethereum 2021-05](ethereum-2021-05-state-gas-not-time.md) | 101 |
| OOG 未回滚空账户删除 | 网络分叉；少数链被弃 | journaling 失败路径漏撤 | [Ethereum 2016-11](ethereum-2016-11-oog-empty-account.md) | 103 |
| 体可变拒绝先于授权承诺、诚实头被永久拉黑 | 诚实尖可能再也接不上同一头；体可换、头被写进非法表 | 授权数据由第二承诺根绑定，体检查抢跑 | [Zcash ZIP 256 体毒](zcash-2026-nu5-body-poison.md) | 106 |
| 身份 rk 转公开输入恐慌 | 两家节点验证明时进程退出 | 规范允许的零点，转换漏写 | [Zcash ZIP 256 身份 rk](zcash-2026-identity-rk-panic.md) | 107 |
| coinbase 正屏蔽余额、ConnectBlock 对不上 | 节点中止，重启再崩 | 链供给与池余额失同步，实现选退出 | [Zcash ZIP 256 coinbase](zcash-2026-coinbase-balance-crash.md) | 109 |
| 治理参数吃不了 | 启用高度提案让进程 panic | 能推治理参数的人 | [ASA-2024-001](asa-2024-001.md) | 58 |
| 解码 / 类型 panic | 深嵌套栈溢出，或 Dec 进 Int | 能送嵌套消息的人；或金额路径 | [ASA-2024-0012](asa-2024-0012.md)、[ASA-2024-010](asa-2024-010.md) | 70、76 |
| 先流言后处理 | 非法结构传出去，网络停 | 能发畸形 P2P 对象的人 | [ASA-2025-003](asa-2025-003.md) | 60 |
| 版本不一致 | 补丁覆盖率落在中间带，AppHash 或停 | 升级节奏，不是洞本身 | [Barberry](barberry.md) 论坛句；[Dragonberry](dragonberry.md) +⅓ 可见停 | 83 的运维句、79 的运维句 |

**事实：** 「停链」在上表里不是同一谓词。  
**事实：** 交易内 panic 被恢复，不是已经停（73）。EndBlocker 出错，不是局部失败（71）。  
**事实：** +⅓ 打上 Dragonberry 补丁之后，再利用会变成**可见停链**；那是止血，不是 ICS-23 已齐（79）。Barberry：33%+1 不受**该洞**影响，66%+1 才不会因**版本差**停——两句都不要抄进不确定法定人数。

---

## 看起来像停、其实不是

| 现象 | 不是 | 馆藏 | 不变量 |
|---|---|---|---|
| 出块变少 | 不是高度已经停 | [ASA-2024-002](asa-2024-002.md) 非法提案 | 69 |
| 最终确认变慢 / 只打包投票 | 不是高度已经停，也不是已最终经济交易被回滚 | [2023-02-25](solana-2023-02-25-turbine-recovery.md) vote-only | 87 |
| 入站数字很大 / 官网 TPS | 不是已经停链 | [2022-04-30](solana-2022-04-30-fork-cleanup-oom.md) 洪水 | 89 |
| RPC 仍能读上一份已认证状态 | 不是链还在结算 | [Sui 2026-01-14](sui-2026-01-14-commit-divergence.md) 隔离 | 91 |
| 本节点崩溃 / OOM | 不是共识已拒绝合法块 | [Lavender](cve-2020-5303.md)、Bitcoin 各崩溃案 | 67 等 |
| `timeout_commit` 在等 | 不是最终性，也不是锁 | 超时精读 | 47 |
| 资金被锁、链还在出块 | 不是停链 | [Barberry](barberry.md) 只进不出 | 83 |
| 出块与最终性继续、选举 / 纪元冻住 | 不是高度已经停，也不是解绑已前进 | [Polkadot 2026-06](polkadot-2026-06-election-score-floor.md) 地板 | 110 |
| 中继还在最终、平行链块送不出去 | 不是平行链已经出块，也不是整理者本地写块已经交给中继 | [Polkadot 2026-03](polkadot-2026-03-deprecated-runtime-api-scale.md) 废弃 API | 114 |
| BABE 还在出块、GRANDPA 没盖章 | 不是已经最终，也不是高度已经停 | [BABE ≠ GRANDPA](../consensus/worked-example-babe-vs-grandpa.md) 精读，不是新馆藏 | 126 |
| 头还在走、justified / finalized 没升 | 不是已经最终，也不是高度已经停 | [head ≠ justified ≠ finalized](../finality/worked-example-head-vs-justified-vs-finalized.md) 精读，不是新馆藏 | 127 |
| 交易进了共识块、接受票还没够 | 不是这笔已经生效，也不是高度已经停 | [owned ≠ 快路径](../parallelism/worked-example-owned-vs-fastpath.md) 精读，不是新馆藏 | 128 |
| 大户质押已经过半 / explorer 总质押绿了 | 不是官方超多数已经到，也不是高度已经停 | [NPoS 等权](../consensus/worked-example-npos-equal-weight.md) 精读，不是新馆藏 | 129 |
| 好久没 finalized / leak 在抽 | 不是高度已经停，也不是已经 slash | [leak ≠ slash](../finality/worked-example-inactivity-leak.md) 精读，不是新馆藏 | 130 |
| Preference 还在走 / 出块窗空着 | 不是已经接受，也不是已经有一张 QC | [抽样 α ≠ QC](../consensus/worked-example-snow-sample-vs-qc.md) 精读，不是新馆藏 | 131 |
| 批次已传开 / 已认证、还没排进 L | 不是已经排序，也不是已经落盘 | [批次 ≠ 已排序](../consensus/worked-example-quorum-store-vs-order.md) 精读，不是新馆藏 | 132 |
| 槽还在走 / 只有 processed 或 confirmed | 不是已经 finalized / 已经 root，也不是高度已经停 | [PoH ≠ Tower](../consensus/worked-example-poh-vs-tower.md) 精读，不是新馆藏 | 133 |

---

## 推断

若文案只写「不变量失败则停」，读者会把 73 的假停和 71 的真停听成一句。  
若运维把「已经有 ⅓ 打了补丁」写成「不会停」，会把 Dragonberry 的可见停与 Barberry 的版本差停听成已经安全。

---

## 建议（不是选型）

1. 产品句若出现「停」，必须从本表点名一行，并链到那一页。  
2. 真要停：写在交易恢复笼外（73），或写链下协调。  
3. 出错若发生在 EndBlocker：按会停审，能交互的用户是活性对手（71）。  
4. 溢出、类型转换、解码失败：拒，不得 panic 成停（74、76、70）。  
5. 第一版可以不装 IBC、授权代发、定期归属、可选治理模块——少一行，就少一种停。  
6. 不要把 ⅓ / 33% / 66% / 66.7% 抄进不确定法定人数。

---

## 回归测试形状

文案把「停链」写成一种事故必须红。把停链交易写成已停必须红。把 EndBlocker 出错写成可跳过必须红。把 +⅓ 打补丁写成不会停必须红。把 Barberry 锁钱写成高度停必须红。把失败 durable nonce 写成已消费 / Tower 已一致必须红。把「正确版本已确认」写成下一领导者必会往上建必须红。把 vote-only / 落到 Block Repair 写成高度已停必须红。把入站洪水写成已经停链必须红。把哨兵有效槽 0 写成已可见必须红。把估值为 0 写成已安全必须红。把隔离拒证写成已经分叉必须红。把因余额不足取消写成已经不再扣款必须红。把 DKG 按设计关掉写成重启后仍关必须红。把槽号写成块身份 / 乐观确认写成已 rooted 必须红。把单笔低于入池上限写成拼块已齐必须红。把交易深度有界写成 runtime API 再解已安全必须红。把组下标写成票下标必须红。把 Active 写成已 Confirmed 必须红。把链下内存禁用写成已确认已经不参与必须红。把训练轮触发写成最终性还在走必须红。把块 gas 上限写成墙钟已有界必须红。把 OOG 结束写成空账户删除已回滚必须红。把体可变拒绝先于授权承诺写成头已经绑死必须红。把诚实头写进永久非法表写成块已经非法必须红。把规范允许身份 rk 写成验证明已经能吃必须红。把 ConnectBlock 对不上写成重启能起来必须红。把出块还在写成纪元已经转必须红。把改冻结门槛写成选举地板已经配对必须红。把废弃 API 还在写成返回编码已经兼容必须红。把整理者还能写块写成中继已经收到必须红。把预编译中途出错写成 SDK 已写入已经撤回必须红。把更低 gas 写成已经更安全必须红。把 BABE 出块写成已经 GRANDPA 必须红。把最长链写成 hybrid 最终头之后的尺子必须红。把出块 / justified / `safe` 写成已经 finalized 必须红。把 owned 写成已经快路径必须红。把进共识块写成这笔已被接受必须红。把 NPoS 当选 / ⅔ 质押写成官方链投票已经过必须红。把 BABE 按质押抽槽写成 GRANDPA 也按质押必须红。把终局推迟写成高度已经停必须红。把 inactivity leak 写成已经 slash 必须红。把两边都 finalized 写成协议已经选出唯一链必须红。把抽样 α 多数写成全集 +2/3 证书必须红。把连续 β 轮写成可转发 QC 必须红。把 Preference 写成已经接受必须红。把出块窗写成已经决定必须红。把「也是 BFT」写成已经和 CometBFT 同一把尺子必须红。把 Quorum Store 传开写成已经写出 L 必须红。把已认证批次写成已经排序或已经 commit 必须红。把去掉领袖瓶颈写成已经没有领袖必须红。把进了提议块写成已经落盘必须红。把 PoH / 槽钟写成已经投票或已经 BFT 必须红。把 `processed` 写成已经不可逆必须红。把 `confirmed` 写成已经 `finalized` / 已经 root 必须红。把 Alpenglow 计划写成现行已经切完必须红。

对照：不变量 84–133；语料 C88–C137；反模式 [halt-sold-as-one-kind](../../libraries/anti-patterns/halt-sold-as-one-kind.md)、[durable-nonce-sold-as-consumed](../../libraries/anti-patterns/durable-nonce-sold-as-consumed.md)、[confirmed-dup-sold-as-parent](../../libraries/anti-patterns/confirmed-dup-sold-as-parent.md)、[recovery-shred-sold-as-filtered](../../libraries/anti-patterns/recovery-shred-sold-as-filtered.md)、[sentinel-slot-sold-as-visible](../../libraries/anti-patterns/sentinel-slot-sold-as-visible.md)、[flood-sold-as-halt](../../libraries/anti-patterns/flood-sold-as-halt.md)、[zero-cost-sold-as-safe](../../libraries/anti-patterns/zero-cost-sold-as-safe.md)、[quarantine-sold-as-fork](../../libraries/anti-patterns/quarantine-sold-as-fork.md)、[cancel-sold-as-no-debit](../../libraries/anti-patterns/cancel-sold-as-no-debit.md)、[dkg-disabled-sold-as-persisted](../../libraries/anti-patterns/dkg-disabled-sold-as-persisted.md)、[slot-sold-as-block-id](../../libraries/anti-patterns/slot-sold-as-block-id.md)、[fiat-shamir-sold-as-bound](../../libraries/anti-patterns/fiat-shamir-sold-as-bound.md)、[pertx-sold-as-block-rpc](../../libraries/anti-patterns/pertx-sold-as-block-rpc.md)、[tx-depth-sold-as-api-depth](../../libraries/anti-patterns/tx-depth-sold-as-api-depth.md)、[group-index-sold-as-vote-index](../../libraries/anti-patterns/group-index-sold-as-vote-index.md)、[active-dispute-sold-as-confirmed](../../libraries/anti-patterns/active-dispute-sold-as-confirmed.md)、[offchain-disable-sold-as-confirmed-ignore](../../libraries/anti-patterns/offchain-disable-sold-as-confirmed-ignore.md)、[gas-sold-as-wallclock](../../libraries/anti-patterns/gas-sold-as-wallclock.md)、[circuit-impl-sold-as-statement](../../libraries/anti-patterns/circuit-impl-sold-as-statement.md)、[oog-sold-as-reverted](../../libraries/anti-patterns/oog-sold-as-reverted.md)、[dup-header-sold-as-turnstile](../../libraries/anti-patterns/dup-header-sold-as-turnstile.md)、[normalize-sold-as-encoded](../../libraries/anti-patterns/normalize-sold-as-encoded.md)、[body-reject-sold-as-header-bound](../../libraries/anti-patterns/body-reject-sold-as-header-bound.md)、[identity-rk-sold-as-handled](../../libraries/anti-patterns/identity-rk-sold-as-handled.md)、[ephemeralkey-sold-as-valid](../../libraries/anti-patterns/ephemeralkey-sold-as-valid.md)、[coinbase-balance-sold-as-restart-safe](../../libraries/anti-patterns/coinbase-balance-sold-as-restart-safe.md)、[chill-sold-as-score-paired](../../libraries/anti-patterns/chill-sold-as-score-paired.md)、[wallet-load-sold-as-no-txid](../../libraries/anti-patterns/wallet-load-sold-as-no-txid.md)、[privatebroadcast-sold-as-hidden](../../libraries/anti-patterns/privatebroadcast-sold-as-hidden.md)、[preserve-origin-sold-as-bound](../../libraries/anti-patterns/preserve-origin-sold-as-bound.md)、[deprecated-api-sold-as-compat](../../libraries/anti-patterns/deprecated-api-sold-as-compat.md)、[statedb-spendable-sold-as-bank](../../libraries/anti-patterns/statedb-spendable-sold-as-bank.md)、[subgroup-sold-as-on-curve](../../libraries/anti-patterns/subgroup-sold-as-on-curve.md)、[precompile-oog-sold-as-reverted](../../libraries/anti-patterns/precompile-oog-sold-as-reverted.md)、[nested-ics20-sold-as-outer-state](../../libraries/anti-patterns/nested-ics20-sold-as-outer-state.md)、[owned-sold-as-fastpath](../../libraries/anti-patterns/owned-sold-as-fastpath.md)、[stake-sold-as-validator-quorum](../../libraries/anti-patterns/stake-sold-as-validator-quorum.md)、[leak-sold-as-slash](../../libraries/anti-patterns/leak-sold-as-slash.md)、[snow-sold-as-qc](../../libraries/anti-patterns/snow-sold-as-qc.md)、[batch-sold-as-ordered](../../libraries/anti-patterns/batch-sold-as-ordered.md)、[poh-sold-as-tower](../../libraries/anti-patterns/poh-sold-as-tower.md)。
