# L9.2 Mempool：准入、替换、驱逐、抢跑

优先级：必学  
先修：L0.7，L5.4，L3.2 费用直觉

---

## A. 先修知识

交易先进入「尚未 canonical」的池。池不是账本。  
Ethereum 的 PBS 说明：池还可以被市场吃掉。Bitcoin 有标准性：共识允许但池拒绝。

---

## B. 核心问题

**谁有资格进池、谁能替换谁、池满了踢谁、对手如何用池做垃圾或抢跑？**

---

## C. 直觉（ELI15）

邮局门口的筐：

- 信封不合格（没邮票、地址乱）——不进筐（准入）。
- 同一寄件人同一序号，后到的邮票更多——换掉前一封（替换）。
- 筐满了——扔最不值钱的（驱逐）。
- 有人偷看筐里的汇款单，自己先寄一封把钱转走（抢跑）。

筐里有信 ≠ 总局长已盖章。

---

## D. 正式定义

| 政策 | 作用 | 若缺失 |
|---|---|---|
| 准入 | 签名、费、大小、标准性 | DoS、垃圾占内存 |
| 替换 | 同身份更高费替换 | 卡死的低费交易 |
| 驱逐 | 池有界 | 内存爆、节点倒 |
| 广播 | 传给邻居 | 审查、日蚀 |
| 加密池 / 隐私订单（演进） | 减少抢跑 | 新的延迟与信任点 |

**事实：** mempool 政策常常是**本地的**。两节点池内容可以不同。共识只对块负责。  
**事实：** 「标准性 ≠ 共识有效性」（Bitcoin L3.2）。  
**推断：** 把 mempool 写成「全球公平队列」的文档，在 MEV 之后过期。

后量子：验签更贵，准入必须有配额，见反模式 unbounded-verify。

---

## E. 最小案例

攻击者发 10 万笔验签很贵、费刚好过线的交易。  
节点若先验后拒、且无字节/CPU 配额，部署层先于协议层倒下。  
另一场景：看到池里的清算交易，插入更高费的抢跑。协议可完全「正确」，用户仍亏。这是经济/排序，不是签名伪造。

---

## F. 真实项目

Bitcoin mempool + 标准性；Ethereum 本地池 + 构建者市场；Solana Gulf Stream（压力前移到 leader）。  
加密内存池是研究/产品线，本课不选品牌。

---

## G. 源码入口

预告：准入函数、替换规则、驱逐堆、向 leader/构建者的提交路径。

---

## H. 攻击者模型

- 廉价验签炸弹（PQ 后更毒）。
- 替换规则漏洞：免费取消别人的交易或永不替换。
- 审查：池收了但不转发。
- 用户以为「已进池」=「已结算」。

---

## I. 代价

严准入：抗 DoS，伤复杂合法交易。  
宽准入：钱包好用，节点危险。  
公开池：简单、可抢跑。隐藏池：少抢跑、多信任中继。

---

## J. 对「不确定」的意义

第一版结算必须有：**验签配额、池大小、替换是否允许、分区时池怎么丢。**  
不要抄「公共 mempool 是公平的」。把排序权写进威胁模型。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | 入池前验签配额（后量子预备） |
| 协议 | 准入 / 替换 / 驱逐规则；入池 ≠ 结算 |
| 实现 | 池索引、解析 DoS |
| 部署 | 每节点一池，没有全球公平队列 |
| 经济 | 排序权、抢跑、审查 |

**禁止假学习：** 「mempool 是全球公平队列。」「进池 = 结算。」「策略拒绝 = 共识非法。」「跳过库存通告 = 已经拒进池。」「发了费率过滤器 = 对等节点已经照做。」「对账素描 = 已经有交易。」「对账失败退回洪水 = 库存通告已经退役。」「内存池查询回了一串库存 = 已经有那些交易。」「只肯给最近转发过的 = 已经支持整池查询。」「协议版本够了 = 已经在答内存池查询。」「拒收消息 = 已经共识非法。」「调试理由 = 已经该给用户看。」「没拒收 = 已经是当前最好链。」「看见先装证据 = 已经装满交易。」「看见两条收交易上限 = 已经同一条。」「看见 MaxBytes 写成 -1 = 已经没有上限。」「看见提案收了交易 = 已经从池里删掉。」「看见本块已 commit = 已经不用再验剩下的。」「看见 CheckTx 过了 = 已经永远有效。」
**边界：** PBS 细节在 L5.4。ABCI 四门在 L4.4 / [`../../tracks/consensus/worked-example-prepare-process.md`](../../tracks/consensus/worked-example-prepare-process.md)。精读：[`../../tracks/mempool/worked-example.md`](../../tracks/mempool/worked-example.md)、[`../../tracks/mempool/worked-example-who-orders.md`](../../tracks/mempool/worked-example-who-orders.md)、[`../../tracks/mempool/worked-example-orphan-resolution.md`](../../tracks/mempool/worked-example-orphan-resolution.md)、[`../../tracks/mempool/worked-example-policy-vs-consensus.md`](../../tracks/mempool/worked-example-policy-vs-consensus.md)（不变量 144）。跳过库存通告 ≠ 已经拒进池；发了费率过滤器 ≠ 对等节点已经照做；布隆过了 ≠ 已经过了费率门：[`../../tracks/mempool/worked-example-feefilter-vs-rejected.md`](../../tracks/mempool/worked-example-feefilter-vs-rejected.md) BIP-133 skip-inv not already rejected / not already illegal / not already filtered-net 正式三事（245 余量）：[`../../tracks/mempool/worked-example-fee133-notpool-vs-bundled.md`](../../tracks/mempool/worked-example-fee133-notpool-vs-bundled.md)（不变量 1238）。 BIP-133 permission not already must / not already sending / not already obeying 正式三事（245 余量）：[`../../tracks/mempool/worked-example-fee133-notmust-vs-bundled.md`](../../tracks/mempool/worked-example-fee133-notmust-vs-bundled.md)（不变量 1239）。 BIP-133 bloom-and not already fee-pass / not already exact-min / not already policy-off 正式三事（245 余量）：[`../../tracks/mempool/worked-example-fee133-notbloom-vs-bundled.md`](../../tracks/mempool/worked-example-fee133-notbloom-vs-bundled.md)（不变量 1240）。（不变量 245）。对账素描 ≠ 已经有那些交易；发了 sendtxrcncl ≠ 已经在对账；对账失败退回洪水 ≠ 库存通告已经退役：[`../../tracks/network/worked-example-erlay-vs-have.md`](../../tracks/network/worked-example-erlay-vs-have.md) BIP-330 recon not already have / not already flood-retired / not already net-wide 正式三事（249 余量）：[`../../tracks/network/worked-example-erl330-nothave-vs-bundled.md`](../../tracks/network/worked-example-erl330-nothave-vs-bundled.md)（不变量 1250）。 BIP-330 sendtxrcncl not already reconciling / not already opened / not already aligned 正式三事（249 余量）：[`../../tracks/network/worked-example-erl330-notsig-vs-bundled.md`](../../tracks/network/worked-example-erl330-notsig-vs-bundled.md)（不变量 1251）。 BIP-330 sketch not already have / not already illegal / not already wtxid 正式三事（249 余量）：[`../../tracks/network/worked-example-erl330-notflood-vs-bundled.md`](../../tracks/network/worked-example-erl330-notflood-vs-bundled.md)（不变量 1252）。（不变量 249）。内存池查询回了一串库存 ≠ 已经有那些交易；只肯给最近转发过的 ≠ 已经支持整池查询；协议版本够了 ≠ 已经在答：[`../../tracks/mempool/worked-example-mempool-dump-vs-have.md`](../../tracks/mempool/worked-example-mempool-dump-vs-have.md)（不变量 253）。不要抄协议版本号 / 库存条数上限。不要写怎样把别人的内存池整包拉走。拒收消息 ≠ 已经共识非法；调试理由 ≠ 已经该给用户看；没拒收 ≠ 已经是当前最好链：[`../../tracks/network/worked-example-reject-vs-consensus.md`](../../tracks/network/worked-example-reject-vs-consensus.md)（不变量 254）。不要抄拒收码取值 / 协议版本号。不要写怎样对合法对象乱发拒收。签了头 ≠ 自己排了序。CheckTx ≠ 已进提案。单笔 CheckTx 绿 ≠ 整包可提案：ASA-2024-002。外层交易上限 ≠ 内层解码已有界：ASA-2024-0012 / 0013。看不见 ≠ 非法：CVE-2024-52913。孤儿扫描必须可中断：CVE-2024-52914。拒了但不踢人仍能烧 CPU：CVE-2025-46598。策略拒绝 ≠ 共识非法。加密内存池尚无冻结规范，不写页。不抄协议版本号。不写怎样按费率认出节点。先装证据 ≠ 已经装满交易；两条收交易上限 ≠ 已经同一条：[`../../tracks/consensus/worked-example-evidence-vs-reap.md`](../../tracks/consensus/worked-example-evidence-vs-reap.md)（不变量 299）。不要抄扣减公式。不要写怎样从池里收割。提案收了 ≠ 已经从池里删掉；本块已 commit ≠ 已经不用再验剩下的：[`../../tracks/mempool/worked-example-proposed-vs-removed.md`](../../tracks/mempool/worked-example-proposed-vs-removed.md)（不变量 301）。不要抄加锁做法。不要写怎样再验。
