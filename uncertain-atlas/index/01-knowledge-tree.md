# Level 0–10 知识树

这不是浏览目录。箭头表示**硬依赖**：左边不会，右边只会变成背词。

标记：

- 必学
- 重要
- 进阶
- 研究级

---

## 总依赖骨架

```text
L0 机器直觉
 └─ L1 工程密码学
     ├─ L2 状态模型
     │    ├─ L3 Bitcoin 完整系统
     │    └─ L5 Ethereum 可编程
     ├─ L4 BFT / CometBFT  ←「不确定」主骨架
     └─ L8 隐私/ZK 的密码前置
          │
          L2 + L3 + L4 + L5
               ├─ L6 高吞吐（Solana / Sui / Aptos）
               ├─ L7 模块化 / DA / 共享安全
               └─ L9 横向系统与失败博物馆
                    └─ L10 「不确定」设计工作室
                         └─ 轨道 C：后量子手册（研究级）
```

读法：先往下，再往右。不要从 L6 或 L8 抄近路。

---

## Level 0 · 区块链作为一台机器 · 必学

毕业：能不看笔记，把一笔转账从「我想转」讲到「全网按同一顺序写入」。

### M0.1 账本问题 · 必学
- L0.1.1 为什么不能各自记一本互不承认的账
- L0.1.2 双花：同一笔钱花两次
- L0.1.3 「我看见了」和「大家承认了」不是一回事
- 知识点：共享账本、双花、承认、本地记录

### M0.2 复制状态机 · 必学
- L0.2.1 状态是什么
- L0.2.2 状态转移函数
- L0.2.3 复制：很多机器跑同一个函数
- 知识点：`S + T → S'`、确定性、副本、分歧

### M0.3 身份与授权 · 必学
- L0.3.1 链上没有「姓名」，只有「谁能证明自己被授权」
- L0.3.2 公钥、私钥、地址的职责分工（先直觉，公式在 L1）
- L0.3.3 丢失私钥 = 丢失授权，不是「忘记密码可以找回」
- 知识点：授权、密钥、地址、不可恢复

### M0.4 交易 · 必学
- L0.4.1 交易是「签名过的状态变更请求」
- L0.4.2 有效交易 vs 已确认交易 vs 最终交易
- L0.4.3 重放：同一张请求被执行两次
- 知识点：签名请求、有效性、确认、最终性、重放保护

### M0.5 区块与顺序 · 必学
- L0.5.1 为什么要打包：顺序、传播、证明
- L0.5.2 区块头与区块体
- L0.5.3 同一高度出现两个块意味着什么
- 知识点：全序、批次、区块头、分叉

### M0.6 一致性问题 · 必学
- L0.6.1 为什么「大家投票，过半数就行」不够
- L0.6.2 诚实节点、掉线节点、说谎节点
- L0.6.3 安全（不做错）与活性（最终能做完）
- 知识点：共识、拜占庭、crash、safety、liveness

### M0.7 一笔转账完整生命周期 · 必学
- L0.7.1 钱包 → RPC → mempool → 出块 → 执行 → 落盘 → 确认
- L0.7.2 每一步失败会长什么样
- 知识点：生命周期、可见、不可逆、用户错觉

### M0.8 五种保证 · 必学
- L0.8.1 密码 / 协议 / 实现 / 部署 / 经济
- L0.8.2 一层失效时，哪一层救不了你
- 知识点：保证分层、假设失效传播

### M0.9 常见假学习 · 必学
- L0.9.1 TPS 不是总成绩
- L0.9.2 去中心化不是开关
- L0.9.3 有浏览器能查到 ≠ 你验证过
- 知识点：指标滥用、验证 vs 查看、全节点

### M0.10 「不确定」的镜头 · 重要
- L0.10.1 现在还不能选共识，但已经能列出以后必须回答的问题
- L0.10.2 结算链与通用计算链的差别（先定性）
- 知识点：设计问题清单、过早优化

**本 Level 完整课程已写。** 见 `courses/level-00-machine/`。  
L1 见 `courses/level-01-crypto/`。L2 见 `courses/level-02-state/`。  
L3–L10 见 `courses/README.md`（每个必学/重要节点有课文或覆盖声明）。

---

## Level 1 · 工程密码学入门 · 必学

依赖：L0 全部。  
先修：能说出「授权」和「状态」是两件事。

毕业：看到一个密码组件，先问「它挡住谁」，再问「公式是什么」。

### M1.1 哈希 · 必学
- 抗碰撞、抗原像、承诺、内容寻址
- 哈希撞了会发生什么
- 覆盖：课文 L1.1；BIP-340 tagged hash 公式在 `tracks/crypto/worked-example-tagged-hash.md`

### M1.2 数字签名 · 必学
- 签名、验签、公钥绑定
- 签名算法被攻破 = 授权体系被攻破
- domain separation：同一把钥匙签错域
- 覆盖：课文 L1.2；消息前缀精读 `tracks/crypto/worked-example-domain.md`；FIPS 第二层 `tracks/post-quantum/fips-context.md`（不变量 18 / 语料 C20）

### M1.3 Merkle 树 · 必学
- 包含证明、排除（先直觉）
- 轻节点为什么能少下数据
- 覆盖：课文 L1.3；奇数复制同根见博物馆 CVE-2012-2459

### M1.4 编码与规范化 · 重要
- canonical encoding
- 非规范编码如何变成共识分裂
- 覆盖：课文 L1.4；实现编码精读 `tracks/implementation/`

### M1.5 随机数与确定性 · 重要
- 签名随机数泄漏
- 共识里的超时不是「随便 sleep」
- 课程：[`../courses/level-01-crypto/L01-M06-randomness-and-determinism.md`](../courses/level-01-crypto/L01-M06-randomness-and-determinism.md)（课号 L1.6，避免与已占用的 L1.5 后量子预告撞号）

### M1.6 后量子预告 · 进阶
- 经典椭圆曲线怕什么
- 体积、验签、网络：工程代价先于数学
- 现在只建立问题清单，不选算法
- 课程：L1.5（`L01-M05-pq-preview.md`）

---

## Level 2 · 状态模型 · 必学

依赖：L0 + M1.1 + M1.2。

毕业：能解释「并行性不是执行器变快，而是冲突变少」。

### M2.1 UTXO · 必学
- 未花费输出、花费、找零
- 天然并行的来源
- 可编程性代价
- 覆盖：课文 L2.1

### M2.2 Account · 必学
- 余额、nonce、storage
- 重放保护为什么常靠 nonce
- 热点账户
- 覆盖：课文 L2.2

### M2.3 Object / Resource · 重要
- 所有权、版本、能力
- 为什么 object 模型可能更好并行
- shared object 如何重新引入争用
- 覆盖：课文 L2.3

### M2.4 混合与证明复杂度 · 进阶
- 钱包体验 vs 证明大小 vs 存储
- statelessness 的真正含义
- 覆盖：课文 L2.5（eUTXO）+ L2.6（占用）；完整证明系统后置 L8

### M2.5 《状态模型设计地图》初稿 · 重要
- 对比表：并行、冲突、隐私、存储、可编程、后量子成本
- 覆盖：课文 L2.4；决策矩阵 `libraries/decision-matrix/` 状态表（不确定列空）

输出资产：`04 状态模型图谱` 的第一版骨架。

---

课程：`courses/level-03-bitcoin/`。档案：`protocols/bitcoin/`。

## Level 3 · Bitcoin 作为完整系统 · 必学

依赖：L2 的 UTXO + L1 哈希/签名/Merkle。

毕业：能回答「Bitcoin 为什么能稳定运行十几年」。

### M3.1 Nakamoto Consensus · 必学
- PoW、最重链、概率最终性、reorg
- 覆盖：课文 L3.1；块时间三把尺 `tracks/consensus/worked-example-mtp.md`（太早 / BIP113 locktime / 太新；不变量 41）

### M3.2 网络与传播 · 必学
- mempool、compact block、eclipse、带宽
- 覆盖：课文 L3.4；日蚀 `tracks/network/worked-example-eclipse.md`；调整钟 ≠ MTP `tracks/network/worked-example-adjusted-time.md`（CVE-2024-52912）；MTP 自己还要拆三把尺 `tracks/consensus/worked-example-mtp.md`

### M3.3 费用市场 · 重要
- 有限区块空间如何定价
- 不是「手续费越高越高级」
- 覆盖：课文 L3.2

### M3.4 Script / SegWit / Taproot / Schnorr · 进阶
- 保守升级如何避免把旧节点踢出共识
- 覆盖：课文 L3.3 方向 + L3.7 见证结构；Taproot 语言细节仍后置

### M3.5 全节点、剪枝、SPV · 必学
- 验证 vs 查看
- 轻客户端的安全假设
- 覆盖：课文 L3.5；assumevalid / assumeutxo ≠ 旧 checkpoint ≠ WS `tracks/implementation/worked-example-assumevalid.md`；头先够功 `tracks/implementation/worked-example-header-work.md`（CVE-2019-25220）

### M3.6 工程哲学与测试 · 重要
- fuzzing、软分叉、Bitcoin Core 的保守主义
- 源码入口课
- 覆盖：课文 L3.6

### M3.7 事故与「看起来没崩」的原因 · 重要
- 通胀漏洞、分叉事件
- 稳定来自可验证性 + 慢变更 + 全节点文化
- 覆盖：课文 L3.6 方法；博物馆 BIP 50 / CVE-2018-17144 / CVE-2010-5139

---

课程：`courses/level-04-bft/`。档案：`protocols/cometbft/`。

## Level 4 · BFT 与 Cosmos / CometBFT · 必学

依赖：L0.6 + L1.2 + L2 任意一种状态模型。  
这是「不确定」最需要认真对待的一层。

毕业：能画出 round/step 状态机，并解释每一把锁为什么存在。

### M4.1 为什么「投票过 2/3」不够 · 必学
- 两个合法值同时过门槛
- 法定人数相交（quorum intersection）
- 覆盖：课文 L4.1。+2/3 ≠ 其余 Commit 槽位已签：CVE-2020-15091 / Syringa（不变量 65）

### M4.2 高度、轮次、步骤 · 必学
- propose / prevote / precommit / commit
- 覆盖：课文 L4.2；被签字节 `tracks/consensus/worked-example-vote-signbytes.md`；块时间须点名算法 `tracks/consensus/worked-example-pbts.md`（PBTS timely ≠ BFT Time 中位数 ≠ MTP ≠ 调整钟；不变量 40）。复算中位数 ≠ 故障者不能抬高 Time：CSA-2026-001（不变量 61）。本地超时 ≠ 最终性：`tracks/consensus/worked-example-timeouts.md`（不变量 47）。应用回的等待 ≠ 槽位：`tracks/consensus/worked-example-next-block-delay.md`（不变量 52）。默认 MaxBytes ≠ 第一轮活性 SLA：ASA-2023-002（不变量 63；`timeout_propose` 必须对照块上限）。+2/3 ≠ 其余槽位已签：CVE-2020-15091 / Syringa（不变量 65）

### M4.3 锁、解锁、超时 · 必学
- locking / unlock / round change
- 为了 safety 牺牲某一轮 liveness
- 覆盖：课文 L4.3；打破锁的链上对象是证据，见 `tracks/economic/worked-example-evidence.md`；Casper 两票谓词见 `tracks/economic/worked-example-casper-slashing.md`；不 timely → prevote nil 是活性代价不是解锁，见 `tracks/consensus/worked-example-pbts.md`。超时不是锁：`tracks/consensus/worked-example-timeouts.md`（不变量 47）。飞行中的 last commit 不是证据身份：CVE-2021-21271 / Mulberry（不变量 64）

### M4.4 验证者集合与投票权 · 必学
- validator set、voting power
- 集合变更何时生效
- 覆盖：课文 L4.5；生效延迟 `tracks/consensus/worked-example-validator-delay.md`（H 的更新：H+1 Next、H+2 计票、H+3 last_commit；不变量 35）

### M4.5 ABCI：应用与共识分离 · 必学
- 为什么这对「不确定」极有价值
- 共识不知道余额，应用不知道投票
- 覆盖：课文 L4.4；四门精读 `tracks/consensus/worked-example-prepare-process.md`（CheckTx ≠ Prepare ≠ Process ≠ Finalize；不变量 33）；扩展精读 `tracks/consensus/worked-example-vote-extension.md`（Verify 拒扩展 ≠ 块非法；不变量 34）。扩展快路径不得跳过旧票字段：ASA-2024-011（不变量 57）。治理改启用高度必须先过转移谓词：ASA-2024-001（不变量 58）。提议者注入的扩展不是投票权：ASA-2024-006（不变量 68）。单笔 CheckTx 绿不是整包可提案：ASA-2024-002（不变量 69）。应用回的 post-commit 等待：`tracks/consensus/worked-example-next-block-delay.md`（非确定性；不变量 52）

### M4.6 崩溃恢复 · 重要
- WAL、超时、重启后如何不投矛盾票
- 覆盖：课文 L4.4；崩溃精读 `tracks/implementation/worked-example-crash.md`

### M4.7 HotStuff / Casper 对照预习 · 进阶
- QC、view change
- 先建立对照表，不深挖所有变体
- 覆盖：课文 L4.6；Casper 两票谓词 `tracks/economic/worked-example-casper-slashing.md`

### M4.8 源码与测试 · 重要
- CometBFT 状态机入口
- 对「不确定」：强烈建议研究的部分
- 覆盖：课文 L4.4 入口；档案第 16–18 节

---

## Level 5 · Ethereum：可编程与多客户端 · 重要

依赖：L2 Account + L1 + L4 的最终性直觉。

毕业：能解释「多个独立客户端如何仍对同一交易得到同一结果」。

### M5.1 账户、nonce、EVM、gas · 必学
- 状态转移、收据、日志
- 覆盖：课文 L5.1

### M5.2 状态树与状态膨胀 · 重要
- trie、存档节点、无状态方向
- 覆盖：课文 L5.4

### M5.3 执行层 / 共识层 · 必学
- validator、attestation、finality、fork choice
- 覆盖：课文 L5.2；CL `DomainType` 见投票 SignBytes 精读；弱主观性 `tracks/finality/worked-example-weak-subjectivity.md`

### M5.4 多客户端与可执行规范 · 必学
- 为什么故意允许多个实现
- 差异性测试如何抓住「实现保证」漏洞
- 覆盖：课文 L5.3

### M5.5 EIP、交易类型、blobs、rollup 入口 · 重要
- 协议如何演化
- 覆盖：课文 L5.4；blob sidecar / PeerDAS / Celestia 三维对照 `tracks/light-clients/worked-example-blob-vs-das.md`（不变量 23）

### M5.6 MEV 与 PBS · 进阶
- mempool 不再是简单队列
- 覆盖：课文 L5.4；谁写列表 vs 谁签头 `tracks/mempool/worked-example-who-orders.md`（Builder API ≠ consensus-specs；不变量 27）

### M5.7 事故：共识分裂、客户端差异、状态问题 · 重要
- 覆盖：L9.9 方法 + 博物馆 CVE-2021-39137

---

## Level 6 · 高吞吐架构 · 重要

依赖：L2 全部 + L4 或 L5 其一 + L3 的网络直觉。

毕业：能拆开「高 TPS」的五个来源，而不是说「硬件好」。

### M6.1 Solana · 重要
- 账户列表、锁定、Sealevel
- PoH、Tower BFT、Gulf Stream、Turbine
- 本地费用市场、状态争用、硬件门槛

### M6.2 Sui · 重要
- object ownership、owned vs shared
- 依赖图、fast path / 共识旁路思想

### M6.3 Aptos · 重要
- Move resource
- Block-STM：未完全定序时为何敢并行
- 冲突、回滚、确定性提交

### M6.4 对照：并行的三种世界观 · 必学
- 预先声明依赖（Solana）
- 所有权依赖（Sui）
- 乐观执行再检测（Aptos）

### M6.5 对「不确定」 · 重要
- 结算链是否需要这种吞吐
- 不建议第一版照搬的部分

---

课程：`courses/level-07-modular/`。档案：`protocols/celestia/`、`protocols/polkadot/`。

## Level 7 · 模块化、数据可用、共享安全 · 重要

依赖：L3 轻节点 + L5 rollup 入口 + L1 Merkle。

毕业：能用自己的话解释 Data Availability。

### M7.1 模块化四件套 · 必学
- execution / settlement / consensus / DA
- 覆盖：课文 L7.1

### M7.2 Celestia · 必学
- DAS、纠删码、NMT
- 数据扣留攻击
- 「有区块头 ≠ 有验证状态所需的数据」
- 覆盖：课文 L7.2；与 4844 / PeerDAS 分列 `tracks/light-clients/worked-example-blob-vs-das.md`

### M7.3 Rollup 作为执行租户 · 重要
- 乐观 vs ZK（先架构，后数学）
- 覆盖：课文 L7.4；乐观品类 `protocols/optimistic-rollup/`；有效性租户仅过滤器 `protocols/starknet/`（点名 SNOS 程序哈希 + `ACCEPTED_ON_L2` ≠ `ACCEPTED_ON_L1`；无 19 节）

### M7.4 Polkadot · 重要
- Relay / Parachain、collator / validator
- backing、availability、approval
- 小链如何借用安全，以及新的攻击面
- 覆盖：课文 L7.3 入口；档案 `protocols/polkadot/`

### M7.5 共享安全对照 · 进阶
- restaking 等后到项目：只收「独特思想」，不因有名而学
- 覆盖：课文 L7.3；EigenLayer 仅过滤器 `protocols/eigenlayer/`（已质押 ETH/LST 再声明 + AVS 自定罚没）；Babylon 仅过滤器 `protocols/babylon/`（BTC UTXO 仍在比特币）；不要开 19 节

---

## Level 8 · 隐私与简洁证明 · 进阶

依赖：L1 全部 + L2 + L3 的承诺树直觉。  
研究级内容标出，可先读架构再读数学。

### M8.1 Zcash · 进阶 / 对「不确定」重要
- note、commitment、nullifier
- 链知道什么、不知道什么、为何仍能防双花
- trusted setup 演化、Orchard、Halo 2

### M8.2 Monero · 进阶
- stealth address、ring、key image、RingCT
- 与 ZK 隐私是两个世界

### M8.3 Mina · 研究级
- 递归证明、简洁链
- 「从创世到现在合法」如何被一个小证明表达

### M8.4 ZK 课程轨道 · 研究级
- 电路、witness、多项式、PCS
- 教学顺序：直觉 → 例子 → 数学 → 电路 → 源码 → 性能 → 假设

---

## Level 9 · 横向系统与失败博物馆 · 重要

依赖：至少完成 L3 + L4 + L5。L6–L8 可并行补。

毕业：能把别人的事故写成「不确定」的 invariant 和回归测试。

### M9.1 P2P · 必学
- 发现、gossip、eclipse、Sybil、分区、NAT
- 很多链的瓶颈在网络不在执行
- 覆盖：课文 L9.1；日蚀精读；调整钟 CVE-2024-52912；索取独占 CVE-2024-52913。新块宣布 ≠ 已收到：CVE-2024-52922。部分重建断言崩：CVE-2024-35202。变异清别人下载：CVE-2024-52921。拒绝仍灌日志盘：CVE-2025-54605。非法块打崩并行验签：CVE-2024-52911。库存三方向：`tracks/network/worked-example-inventory-quotas.md`（52915 / 52920 / inv-to-send）。最大消息 ≠ 接收分配：CVE-2015-3641。地址表递增 ID 回绕：CVE-2024-52919（限速 ≠ 宽度）。无界封禁表：CVE-2020-14198（自动 ban ≠ 有界）。平台宽度尺寸检查：CVE-2025-46597。局域网打洞辅助 ≠ P2P：CVE-2015-20111 / CVE-2024-52917。出站代理 ≠ 对等节点：CVE-2017-18350。分片外层下标 ≠ 证明下标：ASA-2025-002。结构必须先验再传：ASA-2025-003。blocksync 目标必须可归因：ASA-2025-001。握手请求 ≠ 已接受邻居：CVE-2020-5303 / Lavender。compact 精读 `tracks/network/worked-example-compact-block.md`。加密内存池尚无冻结规范级独特对象，不写页

### M9.2 Mempool · 必学
- 准入、替换、驱逐、垃圾、抢跑、加密内存池
- 覆盖：课文 L9.2；筐精读；谁排序 `tracks/mempool/worked-example-who-orders.md`。ABCI 四门：`tracks/consensus/worked-example-prepare-process.md`。看不见 ≠ 非法：CVE-2024-52913。孤儿扫描必须可中断：CVE-2024-52914。拒了但不踢人仍能烧 CPU：CVE-2025-46598。单笔 CheckTx 绿 ≠ 整包可提案：ASA-2024-002。加密内存池：无规范级对象，先不过滤器

### M9.3 存储 · 必学
- WAL、原子提交、断电、剪枝、状态同步
- 「写到一半断电怎么办」
- 覆盖：课文 L9.3；崩溃精读 `tracks/implementation/worked-example-crash.md`。ABCI 快照 ≠ 创世重放：`tracks/implementation/worked-example-statesync.md`（只有轻验 AppHash 可信；不变量 38）。轻验集合 ≠ 提议者选择：ASA-2024-009（不变量 56）。写盘前尺寸检查固定宽度：CVE-2025-46597（不变量 51）

### M9.4 升级 · 重要
- 软/硬分叉、runtime upgrade、紧急升级
- 升级密钥如何变成中心化后门
- 覆盖：课文 L9.4；升级精读 `tracks/upgrades/worked-example.md`

### M9.5 经济安全 · 重要
- 发行、质押、罚没、MEV、审查、卡特尔
- 密码学安全 ≠ 经济安全
- 覆盖：课文 L9.5；桥资本精读；证据 ≠ slash `tracks/economic/worked-example-evidence.md`；默认窗 ≠ 解绑 `tracks/economic/worked-example-evidence-window.md`（ASA-2024-004）；飞行中 last commit ≠ 证据身份 `tracks/failure-museum/cve-2021-21271.md`（Mulberry；不变量 64）；Casper double / surround `tracks/economic/worked-example-casper-slashing.md`

### M9.6 轻节点专题 · 重要
- SPV、状态证明、DAS、简洁证明
- 覆盖：课文 L9.6；阿比放货精读；BFT 跳过 `tracks/light-clients/worked-example-bft-skip.md`；Altair 抽样 `tracks/light-clients/worked-example-sync-committee.md`。验过头 ≠ 能交证据：Alderfly（不变量 66；朝前 lunatic 不得只等同高再出一块）

### M9.7 协议测试 · 必学
- unit / property / fuzz / differential / chaos / mutation
- 覆盖：课文 L9.7；语料目录 `libraries/adversarial-corpus/`（runner 未建）

### M9.8 形式化验证入口 · 进阶
- invariant、safety/liveness、TLA+、模型检测
- 选一个简化 BFT 做状态模型（研究级作业）
- 覆盖：课文 L9.8；缝精读 `tracks/formal-methods/worked-example.md`

### M9.9 Blockchain Failure Museum · 必学
- 共识停机、通胀、签名、重放、桥、客户端分歧、治理
- 覆盖：课文 L9.9；目录 `tracks/failure-museum/`（四十六案；含 ISA-2025-005、x/crisis 不停链、ASA-2024-005、ISA-2025-002、ASA-2024-0012、ASA-2024-002、ASA-2024-006、CVE-2020-5303、Alderfly、CVE-2020-15091、CVE-2021-21271、CSA-2026-001、ASA-2025-001、ASA-2023-002、ASA-2025-002、ASA-2025-003、ASA-2024-001、ASA-2024-004、ASA-2024-009、ASA-2024-011、CVE-2015-3641、CVE-2024-52919、CVE-2020-14198、CVE-2025-46597、CVE-2015-20111、CVE-2017-18350、CVE-2024-52918）
- 每案 7 问（见总任务第五节）

---

## Level 10 · 「不确定」设计工作室 · 研究级

依赖：L9 的测试与失败课 + L4 主骨架 + L1 后量子预告。

毕业：能写决策，而不是能写愿望。

### M10.1 设计决策矩阵 · 必学
- 状态模型、共识、执行、最终性、升级
- 覆盖：课文 L10.1；表在 `libraries/decision-matrix/`（不确定列空）

### M10.2 后量子工程手册 · 研究级
- 用户签名、验证者投票、体积、CPU、传播、区块大小
- mempool DoS、批量验签、地址、算法敏捷
- 密钥轮换、紧急迁移、冷账户、多算法共存
- domain separation、PQ+ZK、轻节点、BFT 投票流量
- 覆盖：L10.2 + L10.4；尺寸卡 / 投票字节 / 有状态 HBS / FIPS `ctx` 在 `tracks/post-quantum/`；CPU 与决策列仍空

### M10.3 威胁模型 · 必学
- 对手能力、分区、量子、升级密钥、实现分歧
- 覆盖：[`../libraries/threat-model/README.md`](../libraries/threat-model/README.md)

### M10.4 Invariant Library · 必学
- 从失败博物馆提取、写成可测试断言
- 目录：[`../libraries/invariants/README.md`](../libraries/invariants/README.md)（1–74）

### M10.5 Adversarial Test Corpus · 重要
- fuzz、差分、崩溃注入、拜占庭仿真
- 目录：[`../libraries/adversarial-corpus/README.md`](../libraries/adversarial-corpus/README.md)（C01–C78；runner 未建）

### M10.6 长期技术路线 · 重要
- 第一版最小结算机
- 什么以后再发明
- 什么永远不要发明
- 覆盖：课文 L10.3

---

## 额外项目插入规则

下列项目**不自动进入主线**。只有当它提供其他项目很少有的思想时，才插入：

| 候选 | 可能的独特思想 | 建议插入点 | 优先级 |
|---|---|---|---|
| Cardano | eUTXO（L2.5 已写；不写全生态 19 节） | L2 | 进阶 |
| Near | Nightshade 一条链+chunk（`protocols/near` 思想级）；Doomslug ≠ BFT 标记 | L7 | 进阶 |
| Algorand | 密码抽签（`protocols/algorand` 已写） | L4 对照 | 进阶 |
| Kaspa | 区块 DAG（`protocols/kaspa` + L3.8） | L3 | 进阶 |
| Fuel | UTXO + 声明调度（思想级档案） | L2 + L6 | 进阶 |
| Monad / Sei | Monad：共识先定序、根延迟 `D` 块（`protocols/monad` 仅过滤器）。Sei 仍待独特思想，不写页 | L5 + L6 | 进阶 |
| Starknet / zkSync | 有效性租户：点名程序哈希 + 两层 accepted（`protocols/starknet` 仅过滤器）。zkSync 仍无独立对象，不写页 | L7 + L8 | 研究级 |
| Arbitrum / Optimism | 乐观滚动（`protocols/optimistic-rollup` 已写） | L7 | 重要 |
| EigenLayer / Babylon | 再质押：`protocols/eigenlayer` 仅过滤器（AVS 罚没不必客观可归属）。BTC UTXO 仍留在 Bitcoin：`protocols/babylon` 仅过滤器。都无 19 节 | L7 共享安全对照 | 进阶 |
| Filecoin / Arweave | 存储证明、永久数据 | 仅当「不确定」要做存储 | 按需 |
| Nervos | 状态占用 / 链下生成（`protocols/nervos` + L2.6） | L2 + L9 经济 | 进阶 |
| ICP | 容器、子网、链密钥 | 仅当独特思想被确认 | 研究级 |
| 后量子实验链 | 有状态 XMSS：QRL 过滤器页 + RFC 8391 / SP 800-208 思想卡 | L10 轨道 C | 研究级 |

插入前必须先回答：

> 它提供了什么其他项目很少有的技术思想？

答不出来，就降级，不写完整 19 节报告。
