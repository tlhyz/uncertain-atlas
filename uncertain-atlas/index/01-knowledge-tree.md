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
- 覆盖：课文 L1.1；BIP-340 tagged hash 公式在 `tracks/crypto/worked-example-tagged-hash.md`。txid ≠ wtxid：[`../tracks/implementation/worked-example-txid-vs-wtxid.md`](../tracks/implementation/worked-example-txid-vs-wtxid.md)（不变量 152）

### M1.2 数字签名 · 必学
- 签名、验签、公钥绑定
- 签名算法被攻破 = 授权体系被攻破
- domain separation：同一把钥匙签错域
- 覆盖：课文 L1.2；消息前缀精读 `tracks/crypto/worked-example-domain.md`；FIPS 第二层 `tracks/post-quantum/fips-context.md`（不变量 18 / 语料 C20）。子群过了 ≠ 点已经在曲线上：[`../tracks/failure-museum/cve-2025-30147.md`](../tracks/failure-museum/cve-2025-30147.md)（不变量 116）。JSON 里的 chainId ≠ 已经编进签名哈希；旧六字段签 ≠ 已经防跨链重放：[`../tracks/crypto/worked-example-chainid-vs-signed.md`](../tracks/crypto/worked-example-chainid-vs-signed.md)（不变量 161）。ECDSA 验得过 ≠ 已经是严格 DER：[`../tracks/implementation/worked-example-valid-vs-der.md`](../tracks/implementation/worked-example-valid-vs-der.md)（不变量 172）

### M1.3 Merkle 树 · 必学
- 包含证明、排除（先直觉）
- 轻节点为什么能少下数据
- 覆盖：课文 L1.3；奇数复制同根见博物馆 CVE-2012-2459

### M1.4 编码与规范化 · 重要
- canonical encoding
- 非规范编码如何变成共识分裂
- 覆盖：课文 L1.4；实现编码精读 `tracks/implementation/`。类型字节 ≠ 已经解开内层；旧式列表 ≠ 已经是信封：[`../tracks/implementation/worked-example-typed-vs-legacy.md`](../tracks/implementation/worked-example-typed-vs-legacy.md)（不变量 167）。ECDSA 验得过 ≠ 已经是严格 DER：[`../tracks/implementation/worked-example-valid-vs-der.md`](../tracks/implementation/worked-example-valid-vs-der.md)（不变量 172）。看见 Bech32 地址串 ≠ 链上已经有这笔输出：[`../tracks/implementation/worked-example-address-vs-utxo.md`](../tracks/implementation/worked-example-address-vs-utxo.md)（不变量 174）。看见部分签名包 ≠ 已经是网上能广播的完整交易：[`../tracks/implementation/worked-example-psbt-vs-broadcast.md`](../tracks/implementation/worked-example-psbt-vs-broadcast.md)（不变量 179）。后继校验过了 ≠ 已经是旧校验那套地址：[`../tracks/implementation/worked-example-bech32m-vs-bech32.md`](../tracks/implementation/worked-example-bech32m-vs-bech32.md)（不变量 181）。看见扩展公钥 ≠ 已经能花：[`../tracks/implementation/worked-example-xpub-vs-spendable.md`](../tracks/implementation/worked-example-xpub-vs-spendable.md)（不变量 182）。看见助记词 ≠ 已经是二进制种子：[`../tracks/implementation/worked-example-mnemonic-vs-seed.md`](../tracks/implementation/worked-example-mnemonic-vs-seed.md)（不变量 183）。看见私钥或助记词备份 ≠ 已经知道该看哪种输出脚本；看见描述符 ≠ 已经是地址：[`../tracks/implementation/worked-example-descriptor-vs-keys.md`](../tracks/implementation/worked-example-descriptor-vs-keys.md)（不变量 184）。看见后继版本工作包 ≠ 已经是旧版那份固定未签交易：[`../tracks/implementation/worked-example-psbtv2-vs-v0.md`](../tracks/implementation/worked-example-psbtv2-vs-v0.md)（不变量 186）

### M1.5 随机数与确定性 · 重要
- 签名随机数泄漏
- 共识里的超时不是「随便 sleep」
- 课程：[`../courses/level-01-crypto/L01-M06-randomness-and-determinism.md`](../courses/level-01-crypto/L01-M06-randomness-and-determinism.md)（课号 L1.6，避免与已占用的 L1.5 后量子预告撞号）。ValidateBasic 读本地钟 ≠ 已确定：Jackfruit / CVE-2021-41135（不变量 82）。合并后的 DIFFICULTY ≠ 工作量；PREVRANDAO ≠ 应用级无偏随机：[`../tracks/crypto/worked-example-prevrandao-vs-difficulty.md`](../tracks/crypto/worked-example-prevrandao-vs-difficulty.md)（不变量 157）。用户自造句子 ≠ 已经是本页那种助记词：[`../tracks/implementation/worked-example-mnemonic-vs-seed.md`](../tracks/implementation/worked-example-mnemonic-vs-seed.md)（不变量 183）

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
- 覆盖：课文 L2.1。谓词通过 ≠ 脚本已经跑完；只读重叠 ≠ 写冲突；并行验证 ≠ 已经不需要顺序 L：[`../tracks/parallelism/worked-example-utxo-access-list.md`](../tracks/parallelism/worked-example-utxo-access-list.md)（不变量 143）。进了块的 coinbase ≠ 已经能花：[`../tracks/economic/worked-example-coinbase-vs-mature.md`](../tracks/economic/worked-example-coinbase-vs-mature.md)（不变量 163）。脚本里的 CLTV ≠ 交易 nLockTime 已经把输出锁住：[`../tracks/state-models/worked-example-cltv-vs-nlocktime.md`](../tracks/state-models/worked-example-cltv-vs-nlocktime.md)（不变量 164）。脚本里的 CSV ≠ 绝对锁 / ≠ 部署名：[`../tracks/state-models/worked-example-csv-vs-cltv.md`](../tracks/state-models/worked-example-csv-vs-cltv.md)（不变量 165）。付给脚本哈希 ≠ 已经揭开赎回脚本：[`../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md`](../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md)（不变量 170）。看见 Bech32 地址串 ≠ 链上已经有这笔输出：[`../tracks/implementation/worked-example-address-vs-utxo.md`](../tracks/implementation/worked-example-address-vs-utxo.md)（不变量 174）

### M2.2 Account · 必学
- 余额、nonce、storage
- 重放保护为什么常靠 nonce
- 热点账户
- 覆盖：课文 L2.2。空地址 ≠ 还没有账户类型：Barberry（不变量 83）。StateDB 可花 ≠ 归属锁定已经从同一笔写回排除：[`../tracks/failure-museum/cosmos-evm-2026-08-statedb-vesting.md`](../tracks/failure-museum/cosmos-evm-2026-08-statedb-vesting.md)（不变量 115）。预编译中途出错 ≠ SDK 已写入已经撤回：[`../tracks/failure-museum/isa-2025-004.md`](../tracks/failure-museum/isa-2025-004.md)（不变量 117）。内层改过 ≠ 外层已经看见：[`../tracks/failure-museum/asa-2026-002.md`](../tracks/failure-museum/asa-2026-002.md)（不变量 118）。瞬时存储 ≠ 账户持久存储；本笔结束丢掉 ≠ 本笔里从未存在：[`../tracks/state-models/worked-example-transient-vs-storage.md`](../tracks/state-models/worked-example-transient-vs-storage.md)（不变量 159）。后来的 SELFDESTRUCT ≠ 账户已经删掉：[`../tracks/state-models/worked-example-selfdestruct-vs-delete.md`](../tracks/state-models/worked-example-selfdestruct-vs-delete.md)（不变量 160）。JSON 里的 chainId ≠ 已经编进签名哈希：[`../tracks/crypto/worked-example-chainid-vs-signed.md`](../tracks/crypto/worked-example-chainid-vs-signed.md)（不变量 161）。发送者已有代码 ≠ 已经能当 EOA 发交易：[`../tracks/state-models/worked-example-code-sender-vs-eoa.md`](../tracks/state-models/worked-example-code-sender-vs-eoa.md)（不变量 162）。nonce 顶到规范上限 ≠ 已经还能加一：[`../tracks/state-models/worked-example-max-nonce-vs-next.md`](../tracks/state-models/worked-example-max-nonce-vs-next.md)（不变量 175）。空 ≠ 已经不存在；死 ≠ 已经一种对象：[`../tracks/state-models/worked-example-empty-vs-dead.md`](../tracks/state-models/worked-example-empty-vs-dead.md)（不变量 180）

### M2.3 Object / Resource · 重要
- 所有权、版本、能力
- 为什么 object 模型可能更好并行
- shared object 如何重新引入争用
- 覆盖：课文 L2.3。`store` ≠ 已经是顶层资源；声明了 `has copy` ≠ 这个实例能复制：[`../tracks/state-models/worked-example-ability-vs-resource.md`](../tracks/state-models/worked-example-ability-vs-resource.md)（不变量 151）

### M2.4 混合与证明复杂度 · 进阶
- 钱包体验 vs 证明大小 vs 存储
- statelessness 的真正含义
- 覆盖：课文 L2.5（eUTXO）+ L2.6（占用）；引用输入 ≠ 已经花费：[`../tracks/state-models/worked-example-refinput-vs-spent.md`](../tracks/state-models/worked-example-refinput-vs-spent.md)（不变量 150；看见 datum ≠ 已经过锁；同一枚不得既花又引用）。完整证明系统后置 L8

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
- 覆盖：课文 L3.1；块时间三把尺 `tracks/consensus/worked-example-mtp.md`（太早 / BIP113 locktime / 太新；不变量 41）。进了块的 coinbase ≠ 已经能花：[`../tracks/economic/worked-example-coinbase-vs-mature.md`](../tracks/economic/worked-example-coinbase-vs-mature.md)（不变量 163）。coinbase 第一项写了高度 ≠ 头上已经有高度字段：[`../tracks/implementation/worked-example-coinbase-height-vs-header.md`](../tracks/implementation/worked-example-coinbase-height-vs-header.md)（不变量 173）。脚本里的 CLTV ≠ 交易 nLockTime 已经把输出锁住：[`../tracks/state-models/worked-example-cltv-vs-nlocktime.md`](../tracks/state-models/worked-example-cltv-vs-nlocktime.md)（不变量 164）。脚本里的 CSV ≠ 绝对锁 / ≠ 部署名：[`../tracks/state-models/worked-example-csv-vs-cltv.md`](../tracks/state-models/worked-example-csv-vs-cltv.md)（不变量 165）

### M3.2 网络与传播 · 必学
- mempool、compact block、eclipse、带宽
- 覆盖：课文 L3.4；日蚀 `tracks/network/worked-example-eclipse.md`；调整钟 ≠ MTP `tracks/network/worked-example-adjusted-time.md`（CVE-2024-52912）；MTP 自己还要拆三把尺 `tracks/consensus/worked-example-mtp.md`。privatebroadcast 开关 ≠ IP 已经不暴露：[`../tracks/failure-museum/bitcoin-2026-06-privatebroadcast-v1-retry.md`](../tracks/failure-museum/bitcoin-2026-06-privatebroadcast-v1-retry.md)（不变量 112）

### M3.3 费用市场 · 重要
- 有限区块空间如何定价
- 不是「手续费越高越高级」
- 覆盖：课文 L3.2。策略拒绝 ≠ 共识非法；费率高 ≠ 更正确；策略不作用于块内交易：[`../tracks/mempool/worked-example-policy-vs-consensus.md`](../tracks/mempool/worked-example-policy-vs-consensus.md)（不变量 144）。选择加入替换信号 ≠ 已经换掉：[`../tracks/mempool/worked-example-rbf-signal-vs-replaced.md`](../tracks/mempool/worked-example-rbf-signal-vs-replaced.md)（不变量 166）

### M3.4 Script / SegWit / Taproot / Schnorr · 进阶
- 保守升级如何避免把旧节点踢出共识
- 覆盖：课文 L3.3 方向 + L3.7 见证结构。txid ≠ wtxid：[`../tracks/implementation/worked-example-txid-vs-wtxid.md`](../tracks/implementation/worked-example-txid-vs-wtxid.md)（不变量 152）。钥匙路径 ≠ 已经揭开脚本树；脚本路径 ≠ 已经揭开全部脚本：[`../tracks/implementation/worked-example-keypath-vs-scriptpath.md`](../tracks/implementation/worked-example-keypath-vs-scriptpath.md)（不变量 153）。付给脚本哈希 ≠ 已经揭开赎回脚本：[`../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md`](../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md)（不变量 170）。看见 Bech32 地址串 ≠ 链上已经有这笔输出：[`../tracks/implementation/worked-example-address-vs-utxo.md`](../tracks/implementation/worked-example-address-vs-utxo.md)（不变量 174）。后继校验过了 ≠ 已经是旧校验那套地址：[`../tracks/implementation/worked-example-bech32m-vs-bech32.md`](../tracks/implementation/worked-example-bech32m-vs-bech32.md)（不变量 181）。版本位被置上 ≠ 已经锁定；锁定 ≠ 已经激活：[`../tracks/implementation/worked-example-versionbit-vs-active.md`](../tracks/implementation/worked-example-versionbit-vs-active.md)（不变量 171）。Tapscript 操作码仍后置

### M3.5 全节点、剪枝、SPV · 必学
- 验证 vs 查看
- 轻客户端的安全假设
- 覆盖：课文 L3.5；assumevalid / assumeutxo ≠ 旧 checkpoint ≠ WS `tracks/implementation/worked-example-assumevalid.md`；头先够功 `tracks/implementation/worked-example-header-work.md`（CVE-2019-25220）

### M3.6 工程哲学与测试 · 重要
- fuzzing、软分叉、Bitcoin Core 的保守主义
- 源码入口课
- 覆盖：课文 L3.6。迁移失败 ≠ 目录里其它钱包已经安全：[`../tracks/failure-museum/bitcoin-2026-01-wallet-migration-delete.md`](../tracks/failure-museum/bitcoin-2026-01-wallet-migration-delete.md)（不变量 120）。看见部分签名包 ≠ 已经是网上能广播的完整交易：[`../tracks/implementation/worked-example-psbt-vs-broadcast.md`](../tracks/implementation/worked-example-psbt-vs-broadcast.md)（不变量 179）。看见扩展公钥 ≠ 已经能花：[`../tracks/implementation/worked-example-xpub-vs-spendable.md`](../tracks/implementation/worked-example-xpub-vs-spendable.md)（不变量 182）。看见助记词 ≠ 已经是二进制种子：[`../tracks/implementation/worked-example-mnemonic-vs-seed.md`](../tracks/implementation/worked-example-mnemonic-vs-seed.md)（不变量 183）。看见私钥或助记词备份 ≠ 已经知道该看哪种输出脚本；看见描述符 ≠ 已经是地址：[`../tracks/implementation/worked-example-descriptor-vs-keys.md`](../tracks/implementation/worked-example-descriptor-vs-keys.md)（不变量 184）。看见后继版本工作包 ≠ 已经是旧版那份固定未签交易：[`../tracks/implementation/worked-example-psbtv2-vs-v0.md`](../tracks/implementation/worked-example-psbtv2-vs-v0.md)（不变量 186）

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
- 覆盖：课文 L4.2；被签字节 `tracks/consensus/worked-example-vote-signbytes.md`；块时间须点名算法 `tracks/consensus/worked-example-pbts.md`（PBTS timely ≠ BFT Time 中位数 ≠ MTP ≠ 调整钟；不变量 40）。复算中位数 ≠ 故障者不能抬高 Time：CSA-2026-001（不变量 61）。本地超时 ≠ 最终性：`tracks/consensus/worked-example-timeouts.md`（不变量 47）。应用回的等待 ≠ 槽位：`tracks/consensus/worked-example-next-block-delay.md`（不变量 52）。默认 MaxBytes ≠ 第一轮活性 SLA：ASA-2023-002（不变量 63；`timeout_propose` 必须对照块上限）。+2/3 ≠ 其余槽位已签：CVE-2020-15091 / Syringa（不变量 65）。本头 LastCommit ≠ 本高度已经 +2/3；本地 subjective ≠ 链上 canonical：[`../tracks/consensus/worked-example-lastcommit-vs-this-block.md`](../tracks/consensus/worked-example-lastcommit-vs-this-block.md)（不变量 148）

### M4.3 锁、解锁、超时 · 必学
- locking / unlock / round change
- 为了 safety 牺牲某一轮 liveness
- 覆盖：课文 L4.3；打破锁的链上对象是证据，见 `tracks/economic/worked-example-evidence.md`；Casper 两票谓词见 `tracks/economic/worked-example-casper-slashing.md`；不 timely → prevote nil 是活性代价不是解锁，见 `tracks/consensus/worked-example-pbts.md`。超时不是锁：`tracks/consensus/worked-example-timeouts.md`（不变量 47）。飞行中的 last commit 不是证据身份：CVE-2021-21271 / Mulberry（不变量 64）

### M4.4 验证者集合与投票权 · 必学
- validator set、voting power
- 集合变更何时生效
- 覆盖：课文 L4.5；生效延迟 `tracks/consensus/worked-example-validator-delay.md`（H 的更新：H+1 Next、H+2 计票、H+3 last_commit；不变量 35）。NPoS 当选 ≠ 共识已经按质押加权：[`../tracks/consensus/worked-example-npos-equal-weight.md`](../tracks/consensus/worked-example-npos-equal-weight.md)（不变量 129；⅔ 验证者 ≠ ⅔ 质押）

### M4.5 ABCI：应用与共识分离 · 必学
- 为什么这对「不确定」极有价值
- 共识不知道余额，应用不知道投票
- 覆盖：课文 L4.4；四门精读 `tracks/consensus/worked-example-prepare-process.md`（CheckTx ≠ Prepare ≠ Process ≠ Finalize；不变量 33）；扩展精读 `tracks/consensus/worked-example-vote-extension.md`（Verify 拒扩展 ≠ 块非法；不变量 34）。本头 AppHash ≠ 本高度交易已经交差；本块 DataHash 有这笔 ≠ 效果已经进本头：[`../tracks/consensus/worked-example-apphash-vs-this-block.md`](../tracks/consensus/worked-example-apphash-vs-this-block.md)（不变量 147）。扩展快路径不得跳过旧票字段：ASA-2024-011（不变量 57）。治理改启用高度必须先过转移谓词：ASA-2024-001（不变量 58）。提议者注入的扩展不是投票权：ASA-2024-006（不变量 68）。单笔 CheckTx 绿不是整包可提案：ASA-2024-002（不变量 69）。应用回的 post-commit 等待：`tracks/consensus/worked-example-next-block-delay.md`（非确定性；不变量 52）

### M4.6 崩溃恢复 · 重要
- WAL、超时、重启后如何不投矛盾票
- 覆盖：课文 L4.4；崩溃精读 `tracks/implementation/worked-example-crash.md`

### M4.7 HotStuff / Casper 对照预习 · 进阶
- QC、view change
- 先建立对照表，不深挖所有变体
- 覆盖：课文 L4.6；Casper 两票谓词 `tracks/economic/worked-example-casper-slashing.md`。BABE 出块 ≠ GRANDPA 最终：[`../tracks/consensus/worked-example-babe-vs-grandpa.md`](../tracks/consensus/worked-example-babe-vs-grandpa.md)（不变量 126；对照每高度 commit，不要混进本课变体表）。抽样 α 多数 ≠ 全集 +2/3 证书：[`../tracks/consensus/worked-example-snow-sample-vs-qc.md`](../tracks/consensus/worked-example-snow-sample-vs-qc.md)（不变量 131；「也是 BFT」不是已经有 QC）

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
- 覆盖：课文 L5.1。blob gas ≠ 普通执行 gas：[`../tracks/light-clients/worked-example-blob-fee-vs-gas.md`](../tracks/light-clients/worked-example-blob-fee-vs-gas.md)（不变量 145）。基础费 ≠ 小费；烧掉 ≠ 已经给了出块者；弹性块大小 ≠ 整套费用市场已经齐：[`../tracks/mempool/worked-example-basefee-vs-tip.md`](../tracks/mempool/worked-example-basefee-vs-tip.md)（不变量 158）。瞬时存储 ≠ 账户持久存储：[`../tracks/state-models/worked-example-transient-vs-storage.md`](../tracks/state-models/worked-example-transient-vs-storage.md)（不变量 159）。后来的 SELFDESTRUCT ≠ 账户已经删掉：[`../tracks/state-models/worked-example-selfdestruct-vs-delete.md`](../tracks/state-models/worked-example-selfdestruct-vs-delete.md)（不变量 160）。块 gas 上限 ≠ 墙钟已有界：[`../tracks/failure-museum/ethereum-2021-05-state-gas-not-time.md`](../tracks/failure-museum/ethereum-2021-05-state-gas-not-time.md)（不变量 101）。OOG 结束 ≠ 空账户删除已回滚：[`../tracks/failure-museum/ethereum-2016-11-oog-empty-account.md`](../tracks/failure-museum/ethereum-2016-11-oog-empty-account.md)（不变量 103）。预编译中途出错 ≠ SDK 已写入已经撤回：[`../tracks/failure-museum/isa-2025-004.md`](../tracks/failure-museum/isa-2025-004.md)（不变量 117）。内层改过 ≠ 外层已经看见：[`../tracks/failure-museum/asa-2026-002.md`](../tracks/failure-museum/asa-2026-002.md)（不变量 118）。正确兑现委托语义 ≠ 预编译信任已经改过：[`../tracks/failure-museum/avalanche-2025-delegatecall-precompile.md`](../tracks/failure-museum/avalanche-2025-delegatecall-precompile.md)（不变量 119）。类型字节 ≠ 已经解开内层；旧式列表 ≠ 已经是信封：[`../tracks/implementation/worked-example-typed-vs-legacy.md`](../tracks/implementation/worked-example-typed-vs-legacy.md)（不变量 167）。列出地址或槽 ≠ 已经访问过：[`../tracks/implementation/worked-example-listed-vs-accessed.md`](../tracks/implementation/worked-example-listed-vs-accessed.md)（不变量 168）。本笔第一次碰 ≠ 已经热：[`../tracks/implementation/worked-example-cold-vs-warm.md`](../tracks/implementation/worked-example-cold-vs-warm.md)（不变量 169）。nonce 顶到规范上限 ≠ 已经还能加一：[`../tracks/state-models/worked-example-max-nonce-vs-next.md`](../tracks/state-models/worked-example-max-nonce-vs-next.md)（不变量 175）。initcode 超界 ≠ 已经是部署代码超界：[`../tracks/implementation/worked-example-initcode-vs-runtime.md`](../tracks/implementation/worked-example-initcode-vs-runtime.md)（不变量 176）。带回剩余气的回滚 ≠ 已经像非法指令那样把剩余气烧光：[`../tracks/implementation/worked-example-revert-vs-invalid.md`](../tracks/implementation/worked-example-revert-vs-invalid.md)（不变量 177）。静态帧 ≠ 已经是高级语言的只读函数：[`../tracks/implementation/worked-example-static-vs-view.md`](../tracks/implementation/worked-example-static-vs-view.md)（不变量 178）。空 ≠ 已经不存在：[`../tracks/state-models/worked-example-empty-vs-dead.md`](../tracks/state-models/worked-example-empty-vs-dead.md)（不变量 180）。创建结束返回的运行时代码超界 ≠ 已经是 initcode 超界：[`../tracks/implementation/worked-example-returned-vs-initcode.md`](../tracks/implementation/worked-example-returned-vs-initcode.md)（不变量 185）。出块者地址开跑时已在热集合 ≠ 已经访问过；开跑已热 ≠ 169 那几个预填已经覆盖出块者：[`../tracks/implementation/worked-example-coinbase-vs-prefill.md`](../tracks/implementation/worked-example-coinbase-vs-prefill.md)（不变量 187）。新创建要存上链的代码以保留首字节开头 ≠ 已经是对象格式已经部署；链上已有以该字节开头的代码 ≠ 已经被本页改语义：[`../tracks/implementation/worked-example-reserved-prefix-vs-eof.md`](../tracks/implementation/worked-example-reserved-prefix-vs-eof.md)（不变量 188）

### M5.2 状态树与状态膨胀 · 重要
- trie、存档节点、无状态方向
- 覆盖：课文 L5.4。状态访问的常数 gas ≠ 磁盘已是 O(1)：[`../tracks/failure-museum/ethereum-2021-05-state-gas-not-time.md`](../tracks/failure-museum/ethereum-2021-05-state-gas-not-time.md)（不变量 101）

### M5.3 执行层 / 共识层 · 必学
- validator、attestation、finality、fork choice
- 覆盖：课文 L5.2；CL `DomainType` 见投票 SignBytes 精读；弱主观性 `tracks/finality/worked-example-weak-subjectivity.md`。head ≠ justified ≠ finalized：[`../tracks/finality/worked-example-head-vs-justified-vs-finalized.md`](../tracks/finality/worked-example-head-vs-justified-vs-finalized.md)（不变量 127；`safe` 不是官方已经写成 justified）。终局推迟 ≠ 停链，leak ≠ slash：[`../tracks/finality/worked-example-inactivity-leak.md`](../tracks/finality/worked-example-inactivity-leak.md)（不变量 130）。处理完一块 ≠ 已经改规范头：[`../tracks/finality/worked-example-processed-vs-forkchoice.md`](../tracks/finality/worked-example-processed-vs-forkchoice.md)（不变量 149；Engine API `VALID` 不是已经改头，也不是已经 finalized）。提款操作 ≠ 用户交易；信标链出队 ≠ 执行账户已经加钱：[`../tracks/economic/worked-example-withdrawal-vs-tx.md`](../tracks/economic/worked-example-withdrawal-vs-tx.md)（不变量 154）。头里的父信标根 ≠ 当前信标头；合约读到的根 ≠ 已经 finalized：[`../tracks/light-clients/worked-example-parent-root-vs-head.md`](../tracks/light-clients/worked-example-parent-root-vs-head.md)（不变量 156）。合并后的 DIFFICULTY ≠ 工作量；PREVRANDAO ≠ 应用级无偏随机：[`../tracks/crypto/worked-example-prevrandao-vs-difficulty.md`](../tracks/crypto/worked-example-prevrandao-vs-difficulty.md)（不变量 157）

### M5.4 多客户端与可执行规范 · 必学
- 为什么故意允许多个实现
- 差异性测试如何抓住「实现保证」漏洞
- 覆盖：课文 L5.3。单笔低于入池上限 ≠ 拼块已被所有客户端接受：[`../tracks/failure-museum/ethereum-2024-03-sepolia-engine-rpc.md`](../tracks/failure-museum/ethereum-2024-03-sepolia-engine-rpc.md)（不变量 96）。子群过了 ≠ 点已经在曲线上：[`../tracks/failure-museum/cve-2025-30147.md`](../tracks/failure-museum/cve-2025-30147.md)（不变量 116）。Engine API `VALID` ≠ 已经改规范头：[`../tracks/finality/worked-example-processed-vs-forkchoice.md`](../tracks/finality/worked-example-processed-vs-forkchoice.md)（不变量 149；通道尺寸是 96，哪一次调用才改头是 149）

### M5.5 EIP、交易类型、blobs、rollup 入口 · 重要
- 协议如何演化
- 覆盖：课文 L5.4；blob sidecar / PeerDAS / Celestia 三维对照 `tracks/light-clients/worked-example-blob-vs-das.md`（不变量 23）。blob gas ≠ 普通执行 gas：[`../tracks/light-clients/worked-example-blob-fee-vs-gas.md`](../tracks/light-clients/worked-example-blob-fee-vs-gas.md)（不变量 145）

### M5.6 MEV 与 PBS · 进阶
- mempool 不再是简单队列
- 覆盖：课文 L5.4；谁写列表 vs 谁签头 `tracks/mempool/worked-example-who-orders.md`（Builder API ≠ consensus-specs；不变量 27）。烧掉基础费 ≠ MEV 已经解决：[`../tracks/mempool/worked-example-basefee-vs-tip.md`](../tracks/mempool/worked-example-basefee-vs-tip.md)（不变量 158）

### M5.7 事故：共识分裂、客户端差异、状态问题 · 重要
- 覆盖：L9.9 方法 + 博物馆 CVE-2021-39137 + Sepolia 2024-03 Engine API 尺寸（不变量 96）+ 2021-05 状态问题 / gas≠墙钟（不变量 101）+ 2016-11 OOG≠空账户删除已回滚（不变量 103）+ CVE-2025-30147 子群≠在曲线上（不变量 116）

---

## Level 6 · 高吞吐架构 · 重要

依赖：L2 全部 + L4 或 L5 其一 + L3 的网络直觉。

毕业：能拆开「高 TPS」的五个来源，而不是说「硬件好」。

### M6.1 Solana · 重要
- 账户列表、锁定、Sealevel
- PoH、Tower BFT、Gulf Stream、Turbine
- 本地费用市场、状态争用、硬件门槛
- 覆盖：课文 L6.1。PoH ≠ 单独的 BFT；`processed` ≠ `confirmed` ≠ `finalized`：[`../tracks/consensus/worked-example-poh-vs-tower.md`](../tracks/consensus/worked-example-poh-vs-tower.md)（不变量 133）。停机/降级根因：[`../tracks/failure-museum/solana-2022-06-01-durable-nonce.md`](../tracks/failure-museum/solana-2022-06-01-durable-nonce.md)（失败的 durable nonce ≠ 已不能再播；不变量 85）；[`../tracks/failure-museum/solana-2022-09-30-duplicate-fork.md`](../tracks/failure-museum/solana-2022-09-30-duplicate-fork.md)（已确认的重复槽赢家 ≠ 可当父块；不变量 86）；[`../tracks/failure-museum/solana-2023-02-25-turbine-recovery.md`](../tracks/failure-museum/solana-2023-02-25-turbine-recovery.md)（恢复 shred ≠ 已按父槽滤掉；vote-only ≠ 已停链；不变量 87）；[`../tracks/failure-museum/solana-2024-02-06-legacy-loader-loop.md`](../tracks/failure-museum/solana-2024-02-06-legacy-loader-loop.md)（哨兵有效槽 0 ≠ 已可见；不变量 88）；[`../tracks/failure-museum/solana-2022-04-30-fork-cleanup-oom.md`](../tracks/failure-museum/solana-2022-04-30-fork-cleanup-oom.md)（入站洪水 ≠ 已停链；票不够、分叉不回收才 OOM；不变量 89）；[`../tracks/failure-museum/solana-2020-12-04-slot-as-block-id.md`](../tracks/failure-museum/solana-2020-12-04-slot-as-block-id.md)（槽号 ≠ 块身份；乐观确认 ≠ 已 rooted；不变量 94）；[`../tracks/failure-museum/solana-2025-05-02-elgamal-fiat-shamir.md`](../tracks/failure-museum/solana-2025-05-02-elgamal-fiat-shamir.md)（验绿 ≠ Fiat-Shamir 已绑完；不变量 95）

### M6.2 Sui · 重要
- object ownership、owned vs shared
- 依赖图、fast path / 共识旁路思想
- 覆盖：课文 L6.2。owned ≠ 已经走快路径；引用 shared ≠ 已经授权；进共识块 ≠ 已被接受：[`../tracks/parallelism/worked-example-owned-vs-fastpath.md`](../tracks/parallelism/worked-example-owned-vs-fastpath.md)（不变量 128）。禁止「所有交易都绕过共识」。共享对象拥塞控制估值 0 ≠ 已安全：[`../tracks/failure-museum/sui-2024-11-21-zero-cost-assert.md`](../tracks/failure-museum/sui-2024-11-21-zero-cost-assert.md)（不变量 90）。检查点隔离拒证 ≠ 已分叉：[`../tracks/failure-museum/sui-2026-01-14-commit-divergence.md`](../tracks/failure-museum/sui-2026-01-14-commit-divergence.md)（不变量 91）。因余额不足取消 ≠ 已不扣款：[`../tracks/failure-museum/sui-2026-05-gas-smash-cancel.md`](../tracks/failure-museum/sui-2026-05-gas-smash-cancel.md)（不变量 92）。DKG 按设计关掉 ≠ 已落盘：[`../tracks/failure-museum/sui-2026-05-dkg-verdict-disk.md`](../tracks/failure-museum/sui-2026-05-dkg-verdict-disk.md)（不变量 93）

### M6.3 Aptos · 重要
- Move resource
- Block-STM：未完全定序时为何敢并行
- 冲突、回滚、确定性提交
- 覆盖：课文 L6.3；工作实例 [`../tracks/parallelism/worked-example-block-stm.md`](../tracks/parallelism/worked-example-block-stm.md)（不变量 122）。并行结果 ≡ 已共识的串行序 L；STM 跑完 ≠ 已经最终；未声明写集 ≠ 已经不需要 L。Quorum Store 批次传播 ≠ 已经写出 L：[`../tracks/consensus/worked-example-quorum-store-vs-order.md`](../tracks/consensus/worked-example-quorum-store-vs-order.md)（不变量 132）。`store` ≠ 已经是顶层资源：[`../tracks/state-models/worked-example-ability-vs-resource.md`](../tracks/state-models/worked-example-ability-vs-resource.md)（不变量 151）

### M6.4 对照：并行的三种世界观 · 必学
- 预先声明依赖（Solana）
- 所有权依赖（Sui）
- 乐观执行再检测（Aptos）
- 覆盖：课文 L6.4。Sui 停机对照见 M6.2 四案（估值 0、隔离拒证、取消后仍砸气费、DKG 未落盘）。顺序已定 ≠ 本块根已交差：[`../tracks/consensus/worked-example-order-vs-state.md`](../tracks/consensus/worked-example-order-vs-state.md)（不变量 136）。谓词通过 ≠ 脚本已经跑完；只读重叠 ≠ 写冲突：[`../tracks/parallelism/worked-example-utxo-access-list.md`](../tracks/parallelism/worked-example-utxo-access-list.md)（不变量 143）

### M6.5 对「不确定」 · 重要
- 结算链是否需要这种吞吐
- 不建议第一版照搬的部分
- 覆盖：课文 L6.4 的 J 节（矩阵列仍空；三种世界观当储备，不当默认发动机）。先定序再 Apply 是问题不是默认发动机：[`../tracks/consensus/worked-example-order-vs-state.md`](../tracks/consensus/worked-example-order-vs-state.md)（不变量 136）。短槽 + 声明调度也不是默认发动机：[`../tracks/parallelism/worked-example-utxo-access-list.md`](../tracks/parallelism/worked-example-utxo-access-list.md)（不变量 143）

---

课程：`courses/level-07-modular/`。档案：`protocols/celestia/`、`protocols/polkadot/`。

## Level 7 · 模块化、数据可用、共享安全 · 重要

依赖：L3 轻节点 + L5 rollup 入口 + L1 Merkle。

毕业：能用自己的话解释 Data Availability。

### M7.1 模块化四件套 · 必学
- execution / settlement / consensus / DA
- 覆盖：课文 L7.1。执行费 ≠ DA 费；blob gas ≠ 普通执行 gas；EVM 能读承诺 ≠ 已经读到袋里的字节：[`../tracks/light-clients/worked-example-blob-fee-vs-gas.md`](../tracks/light-clients/worked-example-blob-fee-vs-gas.md)（不变量 145）

### M7.2 Celestia · 必学
- DAS、纠删码、NMT
- 数据扣留攻击
- 「有区块头 ≠ 有验证状态所需的数据」
- 覆盖：课文 L7.2；与 4844 / PeerDAS 分列 `tracks/light-clients/worked-example-blob-vs-das.md`。NMT 命名空间齐了 ≠ 扩展方阵已经可用：[`../tracks/light-clients/worked-example-nmt-vs-das.md`](../tracks/light-clients/worked-example-nmt-vs-das.md)（不变量 124）。DACert ≠ 全文已经贴上父链：[`../tracks/light-clients/worked-example-dacert-vs-posted.md`](../tracks/light-clients/worked-example-dacert-vs-posted.md)（不变量 142）

### M7.3 Rollup 作为执行租户 · 重要
- 乐观 vs ZK（先架构，后数学）
- 覆盖：课文 L7.4；乐观品类 `protocols/optimistic-rollup/`。`unsafe` / `latest` ≠ 已经从 L1 推导；OP `safe` ≠ Gasper justified；L2 `finalized` ≠ 桥已兑付：[`../tracks/finality/worked-example-unsafe-vs-derived.md`](../tracks/finality/worked-example-unsafe-vs-derived.md)（不变量 141）。DACert ≠ 全文已经贴上父链：[`../tracks/light-clients/worked-example-dacert-vs-posted.md`](../tracks/light-clients/worked-example-dacert-vs-posted.md)（不变量 142）。有效性租户仅过滤器 `protocols/starknet/`（点名 SNOS 程序哈希 + `CANDIDATE` / `PRE_CONFIRMED` ≠ `ACCEPTED_ON_L2` ≠ `ACCEPTED_ON_L1`；无 19 节）。精读 [`../tracks/finality/worked-example-l2-status-vs-l1.md`](../tracks/finality/worked-example-l2-status-vs-l1.md)（不变量 138）

### M7.4 Polkadot · 重要
- Relay / Parachain、collator / validator
- backing、availability、approval
- 小链如何借用安全，以及新的攻击面
- 覆盖：课文 L7.3 入口；档案 `protocols/polkadot/`。BABE 出块 ≠ GRANDPA 最终：[`../tracks/consensus/worked-example-babe-vs-grandpa.md`](../tracks/consensus/worked-example-babe-vs-grandpa.md)（不变量 126）。backed ≠ 已可用 ≠ 已批准 ≠ GRANDPA：[`../tracks/finality/worked-example-backed-vs-available.md`](../tracks/finality/worked-example-backed-vs-available.md)（不变量 125）。交易解码深度有界 ≠ runtime API 再解整块已安全：[`../tracks/failure-museum/polkadot-2025-05-runtime-api-decode-depth.md`](../tracks/failure-museum/polkadot-2025-05-runtime-api-decode-depth.md)（不变量 97）。组下标 ≠ 票向量下标：[`../tracks/failure-museum/kusama-2025-08-24-group-index-votes.md`](../tracks/failure-museum/kusama-2025-08-24-group-index-votes.md)（不变量 98）。Active ≠ Confirmed：[`../tracks/failure-museum/kusama-2024-02-15-disabled-active-dispute.md`](../tracks/failure-museum/kusama-2024-02-15-disabled-active-dispute.md)（不变量 99）。链下内存禁用 ≠ 已确认争议已经不参与：[`../tracks/failure-museum/kusama-2025-05-09-offchain-disable.md`](../tracks/failure-museum/kusama-2025-05-09-offchain-disable.md)（不变量 100）。改冻结门槛 ≠ 选举地板已经配对：[`../tracks/failure-museum/polkadot-2026-06-election-score-floor.md`](../tracks/failure-museum/polkadot-2026-06-election-score-floor.md)（不变量 110）。preserve_origin 为真 ≠ 出站已经带了改 origin 的指令：[`../tracks/failure-museum/polkadot-2026-03-xcm-preserve-origin.md`](../tracks/failure-museum/polkadot-2026-03-xcm-preserve-origin.md)（不变量 113）。废弃 runtime API 还在 ≠ 返回编码已经兼容：[`../tracks/failure-museum/polkadot-2026-03-deprecated-runtime-api-scale.md`](../tracks/failure-museum/polkadot-2026-03-deprecated-runtime-api-scale.md)（不变量 114）

### M7.5 共享安全对照 · 进阶
- restaking 等后到项目：只收「独特思想」，不因有名而学
- 覆盖：课文 L7.3；EigenLayer 仅过滤器 `protocols/eigenlayer/`（已质押 ETH/LST 再声明 + AVS 自定罚没）。AVS 罚没 ≠ Casper：[`../tracks/economic/worked-example-avs-slash-vs-casper.md`](../tracks/economic/worked-example-avs-slash-vs-casper.md)（不变量 140）。Babylon 仅过滤器 `protocols/babylon/`（BTC UTXO 仍在比特币）。k-deep 包含证明 ≠ 已经 commit；解绑意图 ≠ 已经 k-deep：[`../tracks/economic/worked-example-btc-lock-vs-commit.md`](../tracks/economic/worked-example-btc-lock-vs-commit.md)（不变量 139）。IBC 客户端 ≠ 连接 ≠ 通道 ≠ 数据包已送达：[`../tracks/economic/worked-example-ibc-client-vs-packet.md`](../tracks/economic/worked-example-ibc-client-vs-packet.md)（不变量 146）。源链托管 ≠ 对岸已经铸出原币；对岸券 ≠ 源链已解锁的原币：[`../tracks/economic/worked-example-escrow-vs-voucher.md`](../tracks/economic/worked-example-escrow-vs-voucher.md)（不变量 155）。不要开 19 节

---

## Level 8 · 隐私与简洁证明 · 进阶

依赖：L1 全部 + L2 + L3 的承诺树直觉。  
研究级内容标出，可先读架构再读数学。

### M8.1 Zcash · 进阶 / 对「不确定」重要
- note、commitment、nullifier
- 链知道什么、不知道什么、为何仍能防双花
- trusted setup 演化、Orchard、Halo 2
- 覆盖：课文 L8.1。验证明 ≠ 供给：博物馆 CVE-2019-7167（不变量 13）。Fiat-Shamir 漏哈希 ≠ 已绑定：[`../tracks/failure-museum/solana-2025-05-02-elgamal-fiat-shamir.md`](../tracks/failure-museum/solana-2025-05-02-elgamal-fiat-shamir.md)（不变量 95）。电路实现 ≠ 已写明的陈述：[`../tracks/failure-museum/zcash-2026-orchard-circuit-not-statement.md`](../tracks/failure-museum/zcash-2026-orchard-circuit-not-statement.md)（不变量 102）。重复头复位跟踪 ≠ 闸门还在转：[`../tracks/failure-museum/zcash-2026-zip209-header-reset.md`](../tracks/failure-museum/zcash-2026-zip209-header-reset.md)（不变量 104）。归一化成零 ≠ 编码必须为零：[`../tracks/failure-museum/zcash-2026-valuebalance-normalized.md`](../tracks/failure-museum/zcash-2026-valuebalance-normalized.md)（不变量 105）。体可变拒绝 ≠ 头已经绑死：[`../tracks/failure-museum/zcash-2026-nu5-body-poison.md`](../tracks/failure-museum/zcash-2026-nu5-body-poison.md)（不变量 106）。规范允许身份 rk ≠ 验证明已经能吃：[`../tracks/failure-museum/zcash-2026-identity-rk-panic.md`](../tracks/failure-museum/zcash-2026-identity-rk-panic.md)（不变量 107）。无效 ephemeralKey ≠ 规范已经允许：[`../tracks/failure-museum/zcash-2026-ephemeralkey-split.md`](../tracks/failure-museum/zcash-2026-ephemeralkey-split.md)（不变量 108）。coinbase 正屏蔽余额 ≠ 重启能起来：[`../tracks/failure-museum/zcash-2026-coinbase-balance-crash.md`](../tracks/failure-museum/zcash-2026-coinbase-balance-crash.md)（不变量 109）

### M8.2 Monero · 进阶
- stealth address、ring、key image、RingCT
- 与 ZK 隐私是两个世界
- 覆盖：课文 L8.2。环世界 ≠ 电路世界。从文件加载 ≠ 出站 TXID 已经不泄漏：[`../tracks/failure-museum/monero-2025-08-find-and-save-rings.md`](../tracks/failure-museum/monero-2025-08-find-and-save-rings.md)（不变量 111）

### M8.3 Mina · 研究级
- 递归证明、简洁链
- 「从创世到现在合法」如何被一个小证明表达
- 覆盖：课文 L8.3。小证明 ≠ 数据还在；「22kB」是证明尺寸不是整条链。区块链 SNARK 验绿 ≠ 最新 staged 已被证明；Pickles ≠ Kimchi：[`../tracks/light-clients/worked-example-snarked-vs-staged.md`](../tracks/light-clients/worked-example-snarked-vs-staged.md)（不变量 123）

### M8.4 ZK 课程轨道 · 研究级
- 电路、witness、多项式、PCS
- 教学顺序：直觉 → 例子 → 数学 → 电路 → 源码 → 性能 → 假设
- 覆盖：课文 L8.4（架构层；多项式数学后置）

---

## Level 9 · 横向系统与失败博物馆 · 重要

依赖：至少完成 L3 + L4 + L5。L6–L8 可并行补。

毕业：能把别人的事故写成「不确定」的 invariant 和回归测试。

### M9.1 P2P · 必学
- 发现、gossip、eclipse、Sybil、分区、NAT
- 很多链的瓶颈在网络不在执行
- 覆盖：课文 L9.1；日蚀精读；调整钟 CVE-2024-52912；索取独占 CVE-2024-52913。新块宣布 ≠ 已收到：CVE-2024-52922。部分重建断言崩：CVE-2024-35202。变异清别人下载：CVE-2024-52921。拒绝仍灌日志盘：CVE-2025-54605。非法块打崩并行验签：CVE-2024-52911。库存三方向：`tracks/network/worked-example-inventory-quotas.md`（52915 / 52920 / inv-to-send）。最大消息 ≠ 接收分配：CVE-2015-3641。地址表递增 ID 回绕：CVE-2024-52919（限速 ≠ 宽度）。无界封禁表：CVE-2020-14198（自动 ban ≠ 有界）。平台宽度尺寸检查：CVE-2025-46597。局域网打洞辅助 ≠ P2P：CVE-2015-20111 / CVE-2024-52917。出站代理 ≠ 对等节点：CVE-2017-18350。分片外层下标 ≠ 证明下标：ASA-2025-002。结构必须先验再传：ASA-2025-003。blocksync 目标必须可归因：ASA-2025-001。握手请求 ≠ 已接受邻居：CVE-2020-5303 / Lavender。插入检查加法 ≠ 心跳加余量已经安全：CVE-2026-34219（不变量 121）。compact 精读 `tracks/network/worked-example-compact-block.md`。加密内存池尚无冻结规范级独特对象，不写页

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
- 覆盖：课文 L9.5；桥资本精读；证据 ≠ slash `tracks/economic/worked-example-evidence.md`；默认窗 ≠ 解绑 `tracks/economic/worked-example-evidence-window.md`（ASA-2024-004）；飞行中 last commit ≠ 证据身份 `tracks/failure-museum/cve-2021-21271.md`（Mulberry；不变量 64）；Casper double / surround `tracks/economic/worked-example-casper-slashing.md`。Inactivity leak ≠ slash：[`../tracks/finality/worked-example-inactivity-leak.md`](../tracks/finality/worked-example-inactivity-leak.md)（不变量 130）。提款操作 ≠ 用户交易：[`../tracks/economic/worked-example-withdrawal-vs-tx.md`](../tracks/economic/worked-example-withdrawal-vs-tx.md)（不变量 154）。源链托管 ≠ 对岸已经铸出原币：[`../tracks/economic/worked-example-escrow-vs-voucher.md`](../tracks/economic/worked-example-escrow-vs-voucher.md)（不变量 155）

### M9.6 轻节点专题 · 重要
- SPV、状态证明、DAS、简洁证明
- 覆盖：课文 L9.6；阿比放货精读；BFT 跳过 `tracks/light-clients/worked-example-bft-skip.md`；Altair 抽样 `tracks/light-clients/worked-example-sync-committee.md`；Mina SNARKed ≠ staged `tracks/light-clients/worked-example-snarked-vs-staged.md`（不变量 123）；Celestia NMT 齐 ≠ 方阵可用 `tracks/light-clients/worked-example-nmt-vs-das.md`（不变量 124）。验过头 ≠ 能交证据：Alderfly（不变量 66；朝前 lunatic 不得只等同高再出一块）。头里的父信标根 ≠ 当前信标头：[`../tracks/light-clients/worked-example-parent-root-vs-head.md`](../tracks/light-clients/worked-example-parent-root-vs-head.md)（不变量 156）

### M9.7 协议测试 · 必学
- unit / property / fuzz / differential / chaos / mutation
- 覆盖：课文 L9.7；语料目录 `libraries/adversarial-corpus/`（runner 未建）

### M9.8 形式化验证入口 · 进阶
- invariant、safety/liveness、TLA+、模型检测
- 选一个简化 BFT 做状态模型（研究级作业）
- 覆盖：课文 L9.8；缝精读 `tracks/formal-methods/worked-example.md`

### M9.9 Blockchain Failure Museum · 必学
- 共识停机、通胀、签名、重放、桥、客户端分歧、治理
- 覆盖：课文 L9.9；目录 `tracks/failure-museum/`（九十二案；含 CVE-2026-34219 插入检查≠心跳已安全、Bitcoin 2026-01 迁移失败≠邻居已安全、Avalanche 2025 正确语义≠预编译信任、CVE-2025-30147 子群≠在曲线上、ISA-2025-004 预编译失败≠已撤、ASA-2026-002 内层≠外层已见、Cosmos EVM 2026-08 可花≠银行对齐、Polkadot 2026-03 废弃 API≠编码兼容、Polkadot 2026-03 preserve_origin≠出站已绑、Polkadot 2026-06 选举地板≠已配对、Monero 2025-08 加载≠TXID不泄、Bitcoin 2026-06 privatebroadcast≠IP已藏、Zcash ZIP 256 身份 rk≠已能吃 / 无效 ephemeralKey≠已允许 / coinbase 正余额≠能重启 / 跟踪复位≠闸门 / 归一化≠编码 / 体拒绝≠头已绑、Zcash ZIP 257 电路≠陈述、Ethereum 2016-11 OOG≠删除已回滚、Ethereum 2021-05 gas≠墙钟、Kusama 2025-05 链下禁用≠已确认不参与、Kusama 2025-08 组下标≠票下标、Kusama 2024-02 Active≠Confirmed、Sepolia 2024-03 Engine API 尺寸、Polkadot-SDK 2025-05 交易深度套错对象、Solana 2025-05 Fiat-Shamir 漏哈希、Solana 2020-12 槽号当块身份、Sui 2026-05 取消后仍砸气费、Sui 2026-05 DKG 失败未落盘、Sui 2026-01-14 检查点隔离、Sui 2024-11-21 估值 0 assert、Solana 2024-02-06 旧加载器死循环、Solana 2022-04-30 分叉清理 OOM、Solana 2023-02-25 Turbine 恢复 shred、Solana 2022-09-30 重复槽分叉、Solana 2022-06-01 durable nonce、Barberry、Jackfruit、Elderflower、ASA-2023-001、Dragonberry、ASA-2024-007、ISA-2025-001、ASA-2024-010、ASA-2024-003、ISA-2025-005、x/crisis 不停链、ASA-2024-005、ISA-2025-002、ASA-2024-0012、ASA-2024-002、ASA-2024-006、CVE-2020-5303、Alderfly、CVE-2020-15091、CVE-2021-21271、CSA-2026-001、ASA-2025-001、ASA-2023-002、ASA-2025-002、ASA-2025-003、ASA-2024-001、ASA-2024-004、ASA-2024-009、ASA-2024-011、CVE-2015-3641、CVE-2024-52919、CVE-2020-14198、CVE-2025-46597、CVE-2015-20111、CVE-2017-18350、CVE-2024-52918）。停链面地图：`tracks/failure-museum/worked-example-halt-surfaces.md`（不变量 84）
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
- 目录：[`../libraries/invariants/README.md`](../libraries/invariants/README.md)（1–188）

### M10.5 Adversarial Test Corpus · 重要
- fuzz、差分、崩溃注入、拜占庭仿真
- 目录：[`../libraries/adversarial-corpus/README.md`](../libraries/adversarial-corpus/README.md)（C01–C192；runner 未建）

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
| Cardano | eUTXO（L2.5 已写；不写全生态 19 节）。引用输入 ≠ 已经花费：[`../tracks/state-models/worked-example-refinput-vs-spent.md`](../tracks/state-models/worked-example-refinput-vs-spent.md)（不变量 150） | L2 | 进阶 |
| Near | Nightshade 一条链+chunk（`protocols/near` 思想级）。Doomslug / `near-final` ≠ BFT 谓词 / `final`：[`../tracks/finality/worked-example-doomslug-vs-bft.md`](../tracks/finality/worked-example-doomslug-vs-bft.md)（不变量 135） | L7 | 进阶 |
| Algorand | 密码抽签（`protocols/algorand` 已写）。VRF 抽中 ≠ 已经认证：[`../tracks/consensus/worked-example-vrf-sortition-vs-certified.md`](../tracks/consensus/worked-example-vrf-sortition-vs-certified.md)（不变量 134） | L4 对照 | 进阶 |
| Kaspa | 区块 DAG（`protocols/kaspa` + L3.8）。进了某个块 ≠ 已经在 selected chain：[`../tracks/consensus/worked-example-dag-vs-selected-chain.md`](../tracks/consensus/worked-example-dag-vs-selected-chain.md)（不变量 137） | L3 | 进阶 |
| Fuel | UTXO + 声明调度（思想级档案）。谓词通过 ≠ 脚本已经跑完；只读重叠 ≠ 写冲突；并行验证 ≠ 已经不需要顺序 L：[`../tracks/parallelism/worked-example-utxo-access-list.md`](../tracks/parallelism/worked-example-utxo-access-list.md)（不变量 143） | L2 + L6 | 进阶 |
| Monad / Sei | Monad：共识先定序、根延迟 `D` 块（`protocols/monad` 仅过滤器）。顺序已定 ≠ 本块根已交差：[`../tracks/consensus/worked-example-order-vs-state.md`](../tracks/consensus/worked-example-order-vs-state.md)（不变量 136）。Sei 仍待独特思想，不写页 | L5 + L6 | 进阶 |
| Starknet / zkSync | 有效性租户：点名程序哈希 + 两层 accepted（`protocols/starknet` 仅过滤器）。`CANDIDATE` / `PRE_CONFIRMED` ≠ `ACCEPTED_ON_L2` ≠ `ACCEPTED_ON_L1`：[`../tracks/finality/worked-example-l2-status-vs-l1.md`](../tracks/finality/worked-example-l2-status-vs-l1.md)（不变量 138）。zkSync 仍无独立对象，不写页 | L7 + L8 | 研究级 |
| Arbitrum / Optimism | 乐观滚动（`protocols/optimistic-rollup` 已写）。`unsafe` ≠ 已从 L1 推导；OP `safe` ≠ Gasper justified：[`../tracks/finality/worked-example-unsafe-vs-derived.md`](../tracks/finality/worked-example-unsafe-vs-derived.md)（不变量 141）。DACert ≠ 全文已贴父链：[`../tracks/light-clients/worked-example-dacert-vs-posted.md`](../tracks/light-clients/worked-example-dacert-vs-posted.md)（不变量 142） | L7 | 重要 |
| EigenLayer / Babylon | 再质押：`protocols/eigenlayer` 仅过滤器。AVS 罚没 ≠ Casper：[`../tracks/economic/worked-example-avs-slash-vs-casper.md`](../tracks/economic/worked-example-avs-slash-vs-casper.md)（不变量 140）。BTC UTXO 仍留在 Bitcoin：`protocols/babylon` 仅过滤器。k-deep ≠ commit：[`../tracks/economic/worked-example-btc-lock-vs-commit.md`](../tracks/economic/worked-example-btc-lock-vs-commit.md)（不变量 139）。都无 19 节 | L7 共享安全对照 | 进阶 |
| Filecoin / Arweave | 存储证明、永久数据 | 仅当「不确定」要做存储 | 按需 |
| Nervos | 状态占用 / 链下生成（`protocols/nervos` + L2.6） | L2 + L9 经济 | 进阶 |
| ICP | 容器、子网、链密钥 | 仅当独特思想被确认 | 研究级 |
| 后量子实验链 | 有状态 XMSS：QRL 过滤器页 + RFC 8391 / SP 800-208 思想卡 | L10 轨道 C | 研究级 |

插入前必须先回答：

> 它提供了什么其他项目很少有的技术思想？

答不出来，就降级，不写完整 19 节报告。
