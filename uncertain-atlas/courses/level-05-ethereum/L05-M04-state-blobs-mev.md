# L5.4 状态膨胀、blob 与「mempool 不再是队列」

优先级：重要  
先修：L5.2，L1.3，L7 可后读但会互相引用

---

## A. 先修知识

账户存储活在 Merkle-Patricia 树（现行结构；Verkle 是演进方向，**不要写成已经换完的事实**）。  
有头 ≠ 有数据（L7.2）。  
交易生命周期在 L0.7 是「进 mempool 再被选」。Ethereum 后来把「谁选、谁排序」市场化了。

---

## B. 核心问题

**通用计算成功之后，三个新病从哪来：状态为什么越来越贵、blob 解决的是哪一层、用户交易为何不再是简单排队？**

---

## C. 直觉（ELI15）

1. **状态：** 人人在公共黑板加格子。格子几乎不自动擦。后来的人要背整块板才能接着写。
2. **blob：** 有人把练习册附录贴在走廊，过几天撕掉。教务处只保证「当时能看得到附录」，不保证「十年后附录还在档案室」。
3. **MEV：** 班长不自己收作业，外包给最会排座位的人。排座位的人可以收插队费、可以不收某几本。

三件事都不是创世就设计好的优点，是成功之后的病与药。

---

## D. 正式定义

**状态膨胀（事实级描述）**

全节点必须维持可执行的最新状态。归档节点再加历史。成本差一个数量级（具体字节/价格不在本课填，填了也过期）。  
无状态/状态租赁是研究方向与提案族，不是「已经治好」。

**EIP-4844 blobs（事实：机制存在；细节以规范为准）**

blob 是给 rollup 一类租户用的短时大数据袋，用 KZG 承诺挂到信标块。  
它主要加强的是 **DA 通道**，不是 L1 EVM 吞吐本身。  
**不要**把 Celestia 纠删码抽样和 Ethereum KZG blob 写成同一种东西。Fulu PeerDAS 是后一层列抽样，仍不是 Celestia 二维 DAS。精读：[`../../tracks/light-clients/worked-example-blob-vs-das.md`](../../tracks/light-clients/worked-example-blob-vs-das.md)。blob gas 不是普通执行 gas；EVM 能读承诺不是已经读到袋里的字节：[`../../tracks/light-clients/worked-example-blob-fee-vs-gas.md`](../../tracks/light-clients/worked-example-blob-fee-vs-gas.md)（不变量 145）。看见 calldata 地板不是已经改了执行气，也不是已经是 blob 气：[`../../tracks/implementation/worked-example-calldata-floor-vs-execution.md`](../../tracks/implementation/worked-example-calldata-floor-vs-execution.md)（不变量 197）。看见非零 calldata 降价不是已经没有块大小上限，也不是已经是后来的地板或 blob。精读：[`../../tracks/implementation/worked-example-calldata-cut-vs-unlimited.md`](../../tracks/implementation/worked-example-calldata-cut-vs-unlimited.md)（不变量 226）。看见抬高 blob 目标/上限不是已经改了两套气的拆分，也不是已经 PeerDAS：[`../../tracks/light-clients/worked-example-blob-schedule-vs-4844.md`](../../tracks/light-clients/worked-example-blob-schedule-vs-4844.md)（不变量 200）。看见 blob 底价不是已经并成一套气，也不是已经改了日程：[`../../tracks/light-clients/worked-example-blob-reserve-vs-execution.md`](../../tracks/light-clients/worked-example-blob-reserve-vs-execution.md)（不变量 201）。看见 blob 基础费指令不是已经是执行层基础费指令，也不是已经并成一套气：[`../../tracks/implementation/worked-example-blobbasefee-vs-basefee.md`](../../tracks/implementation/worked-example-blobbasefee-vs-basefee.md)（不变量 219）。看见只改 blob 参数的专用分叉不是已经改了执行规则，也不是已经是常规抬日程或 PeerDAS：[`../../tracks/light-clients/worked-example-bpo-vs-hardfork.md`](../../tracks/light-clients/worked-example-bpo-vs-hardfork.md)（不变量 209）。

**MEV 与 PBS（描述，不写市值）**

同一块里交易顺序会改变谁赚钱。搜索者/构建者竞争出「更值钱的块」。  
PBS：构建者出执行载荷，提议者出块头。今天主网上常见的是 **域外 Builder API**（盲头 + 事后揭示），**不是**信标状态机里的协议内 PBS。精读：[`../../tracks/mempool/worked-example-who-orders.md`](../../tracks/mempool/worked-example-who-orders.md)。  
**事实：** 用户交易的生命周期不再是「全球一个公平队列」。  
**推断：** 审查与抽取会集中在构建者/中继，即使验证者集合看起来分散。

**Rollup 入口（架构，数学后置）**

L2 在自己的执行里跑，把数据/承诺丢回 L1（或 blob）。结算语义见 L7。  
本课只钉：L1 最终 ≠ rollup 提款已过挑战/证明。

---

## E. 最小案例

Rollup 排序者发布状态根 R，数据放进 blob。  
信标头已 finalized。一周后 blob 按规则过期。  
新验证者仍能跟 L1 共识；想重放当年那条 L2 的人，必须另有 DA 档案。  
若某桥在「看到 R 进了 L1 头」的瞬间放行，它用的是 head/包含，不是自己的欺诈/有效性条件——见反模式 header-equals-settlement。

---

## F. 真实项目

Ethereum L1 + 各类 rollup。具体 rollup 19 节只在通过独特思想过滤器后写。  
对照：Celestia 把 DA 当主业；Bitcoin 几乎不提供通用 DA 出租。

---

## G. 源码入口

预告：状态树更新与根；blob sidecar 校验；构建者/中继接口（产品，不是核心结算必读）。

---

## H. 攻击者模型

- 廉价写状态，把全节点磁盘当公共物品垃圾场。
- 扣留 blob：头在、数据临时不在（DA）。
- 构建者卡特尔：稳定审查某类地址。
- 钱包把「L2 已出块」画成「L1 已最终」。

---

## I. 代价

| 药 | 新病 |
|---|---|
| 通用合约 | 状态与规范复杂度 |
| blob 扩容 | DA 时效、桥语义更绕 |
| PBS | 审查与 MEV 机构化 |

---

## J. 对「不确定」的意义

**暂时不需要** EVM、blob、PBS。  
**必须提前会说：** 状态谁付费、历史谁存、排序谁做、用户看见的确认指哪一层。  
结算链若把 mempool 当「公平队列」写进文档，Ethereum 的演化说明这句会过期。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | blob 承诺（KZG）≠ Celestia 纠删码 |
| 协议 | L2 头在 L1 ≠ L2 最终；状态谁付费 |
| 实现 | 状态树 / 剪枝切点必须两客户端相同 |
| 部署 | 历史谁存、blob 过期后谁能复原 |
| 经济 | MEV / PBS：排序权被卖；mempool 不是公平队列 |

**禁止假学习：** 「有 blob 所以和 Celestia 一种 DA。」「L2 出块 = L1 最终。」「PBS 解决了 MEV。」「烧掉基础费 = MEV 已解决。」「都叫 gas = 同一本账。」「`BLOBHASH` = 已经读到附录。」「抬高了目标/上限 = 已经改了两套气 / 已经是 PeerDAS。」「看见 blob 底价 = 已经并成一套气 / 已经改了日程。」「看见只改 blob 参数 = 已经改了执行。」「配置里有日程 = 已经不用分叉。」「摘要掺进上限 = 版本号已换。」「7892 = 7691。」「2028 = 已经没有块上限。」「2028 = 7623。」「2028 = 4844。」  
**边界：** 不写 Verkle 已完成；不写构建者名单；不抄 MEV 金额与中继占比。不把 Deneb 的 6 个 blob 或后来的上限当永恒。精读：[`../../tracks/light-clients/worked-example-blob-vs-das.md`](../../tracks/light-clients/worked-example-blob-vs-das.md)、[`../../tracks/light-clients/worked-example-blob-fee-vs-gas.md`](../../tracks/light-clients/worked-example-blob-fee-vs-gas.md)（不变量 145）、[`../../tracks/mempool/worked-example-who-orders.md`](../../tracks/mempool/worked-example-who-orders.md)、[`../../tracks/mempool/worked-example-basefee-vs-tip.md`](../../tracks/mempool/worked-example-basefee-vs-tip.md)（不变量 158）。看见 calldata 地板 ≠ 已经改了执行气：[`../../tracks/implementation/worked-example-calldata-floor-vs-execution.md`](../../tracks/implementation/worked-example-calldata-floor-vs-execution.md)（不变量 197）。看见非零 calldata 降价 ≠ 已经没有块大小上限：[`../../tracks/implementation/worked-example-calldata-cut-vs-unlimited.md`](../../tracks/implementation/worked-example-calldata-cut-vs-unlimited.md)（不变量 226）。看见抬高 blob 目标/上限 ≠ 已经改了两套气的拆分，也不是已经 PeerDAS：[`../../tracks/light-clients/worked-example-blob-schedule-vs-4844.md`](../../tracks/light-clients/worked-example-blob-schedule-vs-4844.md)（不变量 200）。看见 blob 底价 ≠ 已经并成一套气，也不是已经改了日程：[`../../tracks/light-clients/worked-example-blob-reserve-vs-execution.md`](../../tracks/light-clients/worked-example-blob-reserve-vs-execution.md)（不变量 201）。看见 blob 基础费指令 ≠ 已经是执行层基础费指令：[`../../tracks/implementation/worked-example-blobbasefee-vs-basefee.md`](../../tracks/implementation/worked-example-blobbasefee-vs-basefee.md)（不变量 219）。看见只改 blob 参数的专用分叉 ≠ 已经改了执行规则：[`../../tracks/light-clients/worked-example-bpo-vs-hardfork.md`](../../tracks/light-clients/worked-example-bpo-vs-hardfork.md)（不变量 209）。KZG 不是后量子。Builder API 不是 consensus-specs。状态访问的常数 gas ≠ 磁盘已是 O(1)：[`../../tracks/failure-museum/ethereum-2021-05-state-gas-not-time.md`](../../tracks/failure-museum/ethereum-2021-05-state-gas-not-time.md)（不变量 101）。
