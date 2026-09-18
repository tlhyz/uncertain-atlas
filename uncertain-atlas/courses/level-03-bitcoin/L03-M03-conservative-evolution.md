# L3.3 保守演化

优先级：重要  
先修：Bitcoin 档案第 12、15 节，L0.8

---

## A. 先修知识

软分叉 / 硬分叉：旧节点是否仍能验证新历史而不违反自己的规则。

---

## B. 核心问题

**为什么「十年还能跑」和「功能加得慢」是同一设计，而不是开发者懒？**

---

## C. 直觉

桥梁每天有人走。你要换钢，最好让昨天的检查员用旧尺子量，仍然认为桥合法。  
否则一半检查员走旧桥，一半走新桥，桥裂了。

Bitcoin 偏爱：新功能看起来像旧节点已经允许的某种「总是真」的条件（软分叉），而不是宣布旧尺子作废。

慢，是为了：全节点文化、多实现/多版本共存、少制造「升级钥匙」。

---

## D. 正式定义

**软分叉：** 收紧有效集。旧节点仍接受新块（可能看不见新语义）。  
**硬分叉：** 放宽或改变，旧节点会拒绝新块。

**事实：** SegWit、Taproot 以软分叉部署。它们改变了见证与脚本，但走兼容路径。  
**事实：** CVE-2018-17144 是实现没守住早已存在的供给规则，不是「功能加太慢所以安全」。慢升级救不了漏测的 invariant。

保守演化 ≠ 不修 bug。它 = 不把共识当产品迭代。

---

## E. 最小案例

旧节点：某脚本形态「永远可花」或「永远不可花」的旧解释。  
软分叉：新节点对那种形态赋予更严含义。旧节点看见的仍是合法块。  
若你硬分叉改哈希算法或块规则，旧节点立刻分家。

---

## F. 真实项目

Bitcoin 的 BIP 过程、长时间讨论、激活机制（细节各次不同）。  
对照：部分链的 runtime upgrade 快，但升级钥匙可能变成治理后门。

---

## G. 源码

看一次软分叉的脚本标志位 / 版本位，比看十篇新闻有用。版本位被置上不是已经锁定。锁定不是已经激活。精读：[`../../tracks/implementation/worked-example-versionbit-vs-active.md`](../../tracks/implementation/worked-example-versionbit-vs-active.md)（不变量 171）。

---

## H. 攻击者视角

1. 催「紧急硬分叉」塞进后门。  
2. 利用旧节点看不见的新语义做社会分裂。  
3. 在激活窗口制造两套规则的块。

---

## I. Trade-off

得到：可复验、少意外分裂、少万能钥匙。  
失去：新密码算法（后量子）上主网会极慢——这正是「不确定」要提前做算法敏捷的原因，而不是嘲笑 Bitcoin 慢。

---

## J. 对「不确定」的意义

**建议：** 偷「规则少 + 变更要兼容旧验证」，不要偷「我们永远不加字段」。  
后量子必须换签名时，应走版本化账户，而不是突然硬分叉让旧全节点全部非法却无迁移。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | 升级不得静默改哈希 / 签名的含义 |
| 协议 | 软分叉新严旧松；旧节点仍在同一历史上 |
| 实现 | 不同软件版本必须仍能汇合 |
| 部署 | 激活窗口、谁先升级 |
| 经济 | 变更慢是为了全节点跟得上，不是没有升级 |

**禁止假学习：** 「慢 = 没有升级。」「软分叉不改变任何人的安全假设。」「旧节点 EQUAL 通过 = 新节点已经再跑赎回。」「置位 = 已经锁定。」「LOCKED_IN = 已经强制新规则。」「9 = 34。」「库验过 = 共识已收。」「看见头 = 高度已在头上。」「34 = 9。」「走了脚本路径 = 已经是 342。」「342 = 341。」「看见 Miniscript = 已经是链上脚本。」「379 = 16。」「dummy 不是空 = 已经合法。」「隔离见证开了 = 已经没有 dummy 延展。」「策略已经要空 dummy = 共识已经要。」「147 = 66。」
**边界：** SegWit 结构案例在 L3.7。txid ≠ wtxid 见 [`../../tracks/implementation/worked-example-txid-vs-wtxid.md`](../../tracks/implementation/worked-example-txid-vs-wtxid.md)（不变量 152）。钥匙路径 ≠ 已经揭开脚本树见 [`../../tracks/implementation/worked-example-keypath-vs-scriptpath.md`](../../tracks/implementation/worked-example-keypath-vs-scriptpath.md)（不变量 153）。走脚本路径 ≠ 已经是 tapscript 语义见 [`../../tracks/implementation/worked-example-tapscript-vs-scriptpath.md`](../../tracks/implementation/worked-example-tapscript-vs-scriptpath.md)（不变量 189）。付给脚本哈希 ≠ 已经揭开赎回脚本见 [`../../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md`](../../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md)（不变量 170）。版本位被置上 ≠ 已经锁定；锁定 ≠ 已经激活见 [`../../tracks/implementation/worked-example-versionbit-vs-active.md`](../../tracks/implementation/worked-example-versionbit-vs-active.md)（不变量 171）。ECDSA 验得过 ≠ 已经是严格 DER 见 [`../../tracks/implementation/worked-example-valid-vs-der.md`](../../tracks/implementation/worked-example-valid-vs-der.md)（不变量 172）。coinbase 第一项写了高度 ≠ 头上已经有高度字段见 [`../../tracks/implementation/worked-example-coinbase-height-vs-header.md`](../../tracks/implementation/worked-example-coinbase-height-vs-header.md)（不变量 173）。看见 Miniscript ≠ 已经是链上脚本见 [`../../tracks/implementation/worked-example-miniscript-vs-script.md`](../../tracks/implementation/worked-example-miniscript-vs-script.md)（不变量 191）。不抄阈值。不写怎样假示意。不抄 DER 长度。不写怎样改编码。不写怎样拼片段。看见多余栈元素 ≠ 已经随便填；看见隔离见证 ≠ 已经没有这条延展；看见转发策略已经要空 dummy ≠ 已经是共识：[`../../tracks/implementation/worked-example-dummy-vs-empty.md`](../../tracks/implementation/worked-example-dummy-vs-empty.md)（不变量 264）。 BIP-147 dummy not already arbitrary / not already legal / not already settled 正式三事（264 余量）：[`../../tracks/implementation/worked-example-dum147-notany-vs-bundled.md`](../../tracks/implementation/worked-example-dum147-notany-vs-bundled.md)（不变量 1229）。 BIP-147 segwit not already no-dummy-malleation / not already wtxid-fixed / not already settled 正式三事（264 余量）：[`../../tracks/implementation/worked-example-dum147-notwit-vs-bundled.md`](../../tracks/implementation/worked-example-dum147-notwit-vs-bundled.md)（不变量 1230）。 BIP-147 policy not already consensus / not already bip62 / not already settled 正式三事（264 余量）：[`../../tracks/implementation/worked-example-dum147-notpol-vs-bundled.md`](../../tracks/implementation/worked-example-dum147-notpol-vs-bundled.md)（不变量 1231）。不要抄激活时间。不要写怎样改 dummy 撞身份。
