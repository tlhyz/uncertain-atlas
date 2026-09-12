# 实例：「停链」不是一种事故

目的 A + B。不是新馆藏，不新增未核验事故。  
先修：L0.8、L9.9、不变量 71 / 73 / 74 / 75 / 77 / 82 / 85 / 86 / 87 / 88 / 89 / 90 / 91 / 92 / 93 / 94 / 96 / 97 / 98 / 99 / 100 / 101。

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

文案把「停链」写成一种事故必须红。把停链交易写成已停必须红。把 EndBlocker 出错写成可跳过必须红。把 +⅓ 打补丁写成不会停必须红。把 Barberry 锁钱写成高度停必须红。把失败 durable nonce 写成已消费 / Tower 已一致必须红。把「正确版本已确认」写成下一领导者必会往上建必须红。把 vote-only / 落到 Block Repair 写成高度已停必须红。把入站洪水写成已经停链必须红。把哨兵有效槽 0 写成已可见必须红。把估值为 0 写成已安全必须红。把隔离拒证写成已经分叉必须红。把因余额不足取消写成已经不再扣款必须红。把 DKG 按设计关掉写成重启后仍关必须红。把槽号写成块身份 / 乐观确认写成已 rooted 必须红。把单笔低于入池上限写成拼块已齐必须红。把交易深度有界写成 runtime API 再解已安全必须红。把组下标写成票下标必须红。把 Active 写成已 Confirmed 必须红。把链下内存禁用写成已确认已经不参与必须红。把训练轮触发写成最终性还在走必须红。把块 gas 上限写成墙钟已有界必须红。

对照：不变量 84–101；语料 C88–C105；反模式 [halt-sold-as-one-kind](../../libraries/anti-patterns/halt-sold-as-one-kind.md)、[durable-nonce-sold-as-consumed](../../libraries/anti-patterns/durable-nonce-sold-as-consumed.md)、[confirmed-dup-sold-as-parent](../../libraries/anti-patterns/confirmed-dup-sold-as-parent.md)、[recovery-shred-sold-as-filtered](../../libraries/anti-patterns/recovery-shred-sold-as-filtered.md)、[sentinel-slot-sold-as-visible](../../libraries/anti-patterns/sentinel-slot-sold-as-visible.md)、[flood-sold-as-halt](../../libraries/anti-patterns/flood-sold-as-halt.md)、[zero-cost-sold-as-safe](../../libraries/anti-patterns/zero-cost-sold-as-safe.md)、[quarantine-sold-as-fork](../../libraries/anti-patterns/quarantine-sold-as-fork.md)、[cancel-sold-as-no-debit](../../libraries/anti-patterns/cancel-sold-as-no-debit.md)、[dkg-disabled-sold-as-persisted](../../libraries/anti-patterns/dkg-disabled-sold-as-persisted.md)、[slot-sold-as-block-id](../../libraries/anti-patterns/slot-sold-as-block-id.md)、[fiat-shamir-sold-as-bound](../../libraries/anti-patterns/fiat-shamir-sold-as-bound.md)、[pertx-sold-as-block-rpc](../../libraries/anti-patterns/pertx-sold-as-block-rpc.md)、[tx-depth-sold-as-api-depth](../../libraries/anti-patterns/tx-depth-sold-as-api-depth.md)、[group-index-sold-as-vote-index](../../libraries/anti-patterns/group-index-sold-as-vote-index.md)、[active-dispute-sold-as-confirmed](../../libraries/anti-patterns/active-dispute-sold-as-confirmed.md)、[offchain-disable-sold-as-confirmed-ignore](../../libraries/anti-patterns/offchain-disable-sold-as-confirmed-ignore.md)、[gas-sold-as-wallclock](../../libraries/anti-patterns/gas-sold-as-wallclock.md)。
