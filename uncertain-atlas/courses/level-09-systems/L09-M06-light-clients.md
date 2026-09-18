# L9.6 轻节点专题

优先级：重要（知识树 M9.6）  
先修：L3.5，L7.2，L8.3，L5.3

---

## A. 先修知识

四种少下数据的办法已经散落在课里。本课把假设叠成一张表，避免串词。  
精读：[`../../tracks/light-clients/worked-example.md`](../../tracks/light-clients/worked-example.md)。

---

## B. 核心问题

**SPV、状态证明、DAS、递归证明，各自少下了什么、多信了什么？**

---

## C. 直觉（ELI15）

四种「我不背整本练习册」：

1. **SPV：** 只看目录 + 一题的页码条。信多数劳动力。  
2. **状态证明：** 你问「阿安现在多少钱」，对方给一条通向树根的路径。你信根来自你已接受的头。  
3. **DAS：** 你抽查几格擦除码，推断整页大概能拼回来。信编码与抽样参数。  
4. **递归证明：** 你只验一枚「从创世到现在都合法」的章。信电路与证明系统。还要另想办法拿到自己的那一页。

---

## D. 正式定义

| 方案 | 你下载 | 你假设 | 你仍然没有 |
|---|---|---|---|
| 全节点 | 规则所需历史/状态 | 实现正确、网络连通 | — |
| SPV | 头 + 含路径 | 多数算力/工作 | 完整规则、他人交易合法性 |
| 状态证明 | 头/根 + 账户路径 | 根是 canonical | 未证明的槽、历史体 |
| DAS | 头 + 若干份额 | 纠删码、抽样诚实足够 | 单独份额≠执行正确 |
| 递归 SNARK | 小证明 + 现根 | 证明系统 + 电路 | 自动的账户内容、DA、最新 staged（Mina：SNARKed ≠ staged） |
| BFT 轻客户端 | 头 + commit + 集合 | 信任期、init 头、旧集合重叠 | `Apply` / 余额；检测要第二全节点 |
| Altair 同步委员会 | 信标头 + 512 抽样聚合签 | 当期委员会超多数、独立域 | 全验证者 2/3、执行层余额、Casper 罚没 |
| 4844 blob / PeerDAS | 袋里的字节 | versioned hash 或抽到的列 + 服务窗 | 永存档案、执行正确、Celestia 二维 DAS |

**事实：** 上表可以组合（例如：递归证明 + 状态证明 + 外部 DA）。组合是假设相加，不是假设相消。  
**事实：** Mina 的区块链 SNARK 点名 SNARKed ledger，不保证最新 staged。Pickles 不是 Kimchi。精读：[`../../tracks/light-clients/worked-example-snarked-vs-staged.md`](../../tracks/light-clients/worked-example-snarked-vs-staged.md)。  
**事实：** Celestia 的 NMT 证明命名空间齐了，不是扩展方阵已经可用。DAS 抽样过关不是编码已经诚实，也不是历史已经有人存。精读：[`../../tracks/light-clients/worked-example-nmt-vs-das.md`](../../tracks/light-clients/worked-example-nmt-vs-das.md)。  
**事实：** BFT 轻客户端不是 SPV。跳过中间块时，重叠的是**已信任的** `NextValidators`，不是新委员会自嗨的 2/3。精读：[`../../tracks/light-clients/worked-example-bft-skip.md`](../../tracks/light-clients/worked-example-bft-skip.md)。  
**事实：** Ethereum Altair 轻客户端跟的是 **512 人样本**，不是全验证者集合。精读：[`../../tracks/light-clients/worked-example-sync-committee.md`](../../tracks/light-clients/worked-example-sync-committee.md)。EIP-8390 是草案，不是已激活删除。  
**事实：** 轻客户端安全 ≠ 手机 App 安全。App 默认仍可能是 RPC。

---

## E. 最小案例

钱包宣称「ZK 轻客户端」。实际：RPC 给余额，本地验了一下 TLS。  
没有状态路径，没有证明，没有 DAS。词是 L8 的，保证是 L0.9 的假学习。

真组合：验 π（历史合法）+ 对根的账户路径 + 自己保存的查看密钥。缺任何一段，故事断。

---

## F. 真实项目

Bitcoin SPV；Ethereum 轻客户端 / 同步委员会路线（细节以规范为准，勿抄过期博客）；Celestia DAS；Mina 递归；rollup 的「对 L1 根的路径」。

---

## G. 源码入口

先画产品声称的验证集合，再对表找入口。找不到代码的声称当 RPC。

---

## H. 攻击者模型

- 用正确的词包装 RPC。  
- 给路径对一个非 canonical 根。  
- DAS 份额不够仍显示绿勾。  
- 证明验证跳过（test-skip-as-pass）。  
- 把同步委员会抽样 2/3 写成「全网已最终确定」。

---

## I. 代价

越少下载，假设越尖。  
后量子：路径与证明与签名都可能变大，轻客户端的「轻」会反弹。

---

## J. 对「不确定」的意义

第一版建议默认全节点验证结算。轻客户端当明确的第二配置文件，假设写在用户能看见的地方。  
决策矩阵应增「默认验证角色」一行。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | 路径 / 证明 / 抽样各有自己的假设 |
| 协议 | 轻客户端减规则；头 ≠ 结算 |
| 实现 | 证明验证器必须忠实规范 |
| 部署 | 连谁、是否真抽样 |
| 经济 | 默认 RPC 则「无需信任」是假句 |

**禁止假学习：** 「有 Merkle 就是全节点。」「有 ZK 就是无需信任。」「验了递归 π 就是最新余额。」「过滤器对上 = 已经有块。」「过滤器头链对上 = 已经写进共识。」「过滤器对上 = 已经在集合里。」「排除了 OP_RETURN = 已经写进共识。」「没开布隆服务位 = 已经退役。」「开了布隆服务位 = 已经私人。」「协议版本够了 = 已经在遵守。」  
**边界：** 同步委员会常数只引用稳定规范（512 / 256 epoch / `MIN_SYNC_COMMITTEE_PARTICIPANTS = 1`）；EIP-8390 是草案，不是已激活删除。不抄草案里的验证者人数与发行量。不把某一手机钱包当规范。精读：[`../../tracks/light-clients/worked-example.md`](../../tracks/light-clients/worked-example.md)、[`../../tracks/light-clients/worked-example-bft-skip.md`](../../tracks/light-clients/worked-example-bft-skip.md)、[`../../tracks/light-clients/worked-example-sync-committee.md`](../../tracks/light-clients/worked-example-sync-committee.md)、[`../../tracks/light-clients/worked-example-blob-vs-das.md`](../../tracks/light-clients/worked-example-blob-vs-das.md)、[`../../tracks/light-clients/worked-example-snarked-vs-staged.md`](../../tracks/light-clients/worked-example-snarked-vs-staged.md)、[`../../tracks/light-clients/worked-example-nmt-vs-das.md`](../../tracks/light-clients/worked-example-nmt-vs-das.md)。不抄某一链的解绑秒数，不抄现行每块 blob 个数，不抄 22kB / 方阵边长 / FAQ 百分比。验过头 ≠ 已经能交证据：朝前 lunatic 不得只等同高再出一块，见 [Alderfly](../../tracks/failure-museum/alderfly.md)。客户端侧过滤器对上 ≠ 已经有块；过滤器头链对上 ≠ 已经写进共识：[`../../tracks/light-clients/worked-example-cfilter-vs-have.md`](../../tracks/light-clients/worked-example-cfilter-vs-have.md) BIP-157 match not already have-block / not already have-tx / not already bip37 正式三事（243 余量）：[`../../tracks/light-clients/worked-example-cf157-nothave-vs-bundled.md`](../../tracks/light-clients/worked-example-cf157-nothave-vs-bundled.md)（不变量 1277）。 BIP-157 header-chain not already consensus / not already valid-block / not already no-honest-peer 正式三事（243 余量）：[`../../tracks/light-clients/worked-example-cf157-notcons-vs-bundled.md`](../../tracks/light-clients/worked-example-cf157-notcons-vs-bundled.md)（不变量 1278）。 BIP-157 cfilter not already full-node / not already scripts-checked / not already bloom-retired 正式三事（243 余量）：[`../../tracks/light-clients/worked-example-cf157-notfull-vs-bundled.md`](../../tracks/light-clients/worked-example-cf157-notfull-vs-bundled.md)（不变量 1279）。（不变量 243）。基本过滤器对上 ≠ 已经在集合里；排除了 OP_RETURN ≠ 已经写进共识：[`../../tracks/light-clients/worked-example-basic-filter-vs-relevant.md`](../../tracks/light-clients/worked-example-basic-filter-vs-relevant.md) BIP-158 scripts not already have-tx / not already have-opreturn / not already spent 正式三事（244 余量）：[`../../tracks/light-clients/worked-example-bf158-nottx-vs-bundled.md`](../../tracks/light-clients/worked-example-bf158-nottx-vs-bundled.md)（不变量 1280）。 BIP-158 match not already in-set / not already relevant / not already no-false-positive 正式三事（244 余量）：[`../../tracks/light-clients/worked-example-bf158-notrel-vs-bundled.md`](../../tracks/light-clients/worked-example-bf158-notrel-vs-bundled.md)（不变量 1281）。 BIP-158 exclude-opreturn not already consensus / not already other-type / not already header-chain 正式三事（244 余量）：[`../../tracks/light-clients/worked-example-bf158-notcomm-vs-bundled.md`](../../tracks/light-clients/worked-example-bf158-notcomm-vs-bundled.md)（不变量 1282）。（不变量 244）。不抄过滤器构造 / 检查点间隔。不要写怎样造假过滤器。不抄假阳性参数。不要写怎样调假阳性。没开布隆服务位 ≠ 已经退役；开了这一位 ≠ 已经私人；协议版本够了 ≠ 已经在遵守：[`../../tracks/light-clients/worked-example-bloom-bit-vs-retired.md`](../../tracks/light-clients/worked-example-bloom-bit-vs-retired.md) BIP-111 bloom-bit not already private / not already no-dos / not already everyone-serves 正式三事（252 余量）：[`../../tracks/light-clients/worked-example-blm111-notpriv-vs-bundled.md`](../../tracks/light-clients/worked-example-blm111-notpriv-vs-bundled.md)（不变量 1259）。 BIP-111 bloom-off not already retired / not already cfilter / not already consensus-illegal 正式三事（252 余量）：[`../../tracks/light-clients/worked-example-blm111-notoff-vs-bundled.md`](../../tracks/light-clients/worked-example-blm111-notoff-vs-bundled.md)（不变量 1260）。 BIP-111 version-enough not already obeying / not already full-history / not already archive 正式三事（252 余量）：[`../../tracks/light-clients/worked-example-blm111-notver-vs-bundled.md`](../../tracks/light-clients/worked-example-blm111-notver-vs-bundled.md)（不变量 1261）。（不变量 252）。不要抄位编号 / 协议版本号 / 过滤器命令字段。不要写怎样用布隆做拒绝服务或交集分析。不要另写 BIP-37 构造页。
