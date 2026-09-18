# L3.7 SegWit：把新数据放进旧节点仍能验证的缝

优先级：进阶（知识树 M3.4；不讲脚本语言）  
先修：L3.3，L3.5，L1.3

---

## A. 先修知识

软分叉：新规则更严，旧全节点仍跟同一历史（理想情况）。  
txid 一旦被后续输入引用，若能被第三方改掉交易字节却仍有效，依赖链会断——这是**延展性**问题，不是「签名数学废了」。

---

## B. 核心问题

**怎样在不把旧节点踢出共识的前提下，把见证（签名）移出 txid，并让新节点执行更严的规则？**

---

## C. 直觉（ELI15）

旧成绩册只看「题目编号」。  
新老师把「答题过程」另订一本附件。旧老师仍认为这道题交了（看到一个他能接受的占位）。新老师会去附件里核对笔迹。

附件不进「题目编号」（txid）。别人就不能靠改附件笔迹来改题目编号，从而拆掉后面依赖这道题的作业。

---

## D. 正式定义

**SegWit（BIP 141 家族，细节以 BIP 为准）**

- 见证数据（签名等）放到交易的 witness，**不进入旧式 txid 的哈希承诺**。  
- 对旧节点：某些输出看起来像他们能接受的脚本形态（他们验证变薄）。  
- 对新节点：必须检查 witness 满足新规则，否则拒块。  
- 这是软分叉：旧节点不升级仍跟链，但**少验证了一截**。

**延展性（事实级）**

旧式把脚本/签名放进 txid。第三方改签名编码可能改 txid 而交易仍有效。  
依赖未确认 txid 的子交易会悬挂。闪电等二层因此难做。SegWit 的结构目标之一是把签名移出 txid。

**不是**

- 不是「区块变大所以 TPS 事实上升」（广告）。容量与折扣是政策/规则对象，本课不把数字当成绩。  
- 不是硬分叉换哈希函数。  
- 不是教你写 Taproot 脚本。

**事实：** 旧节点安全假设变弱（他们不再查见证）。全网安全依赖足够多的新节点与矿工执行新规则。  
**建议：** 把「谁还在做完整验证」写成升级文档的第一句。

---

## E. 最小案例

交易 T 的旧式 txid 含签名。攻击者改签名 DER 编码，得到 T'，txid 不同，仍能花同一输入。  
阿比已用 T 的 txid 做子支付。T' 上链，子支付失效。  
SegWit 后：改 witness 不改 txid，子支付仍指同一对象（在新规则下）。

旧节点看见 SegWit 花费：可能当「脚本过了」而不看 witness。新节点看 witness。两边仍在同一最重链上——若矿工执行新规则、不挖旧节点会当无效而新节点当有效的块。

---

## F. 真实项目

Bitcoin SegWit 激活史（版本位/矿工信号，细节后置）。  
Taproot 是后续软分叉，本课不展开脚本语言。走脚本路径不是已经是 tapscript 语义：[`../../tracks/implementation/worked-example-tapscript-vs-scriptpath.md`](../../tracks/implementation/worked-example-tapscript-vs-scriptpath.md)（不变量 189）。看见 Miniscript 不是已经是链上脚本：[`../../tracks/implementation/worked-example-miniscript-vs-script.md`](../../tracks/implementation/worked-example-miniscript-vs-script.md)（不变量 191）。  
对照：Ethereum 硬分叉改操作码更常把旧客户端直接踢走。

---

## G. 源码入口

预告：txid vs wtxid 的哈希域；区块里 witness 的提交（coinbase / 承诺）。先读 BIP 141 目录，再打开实现。精读：[`../../tracks/implementation/worked-example-txid-vs-wtxid.md`](../../tracks/implementation/worked-example-txid-vs-wtxid.md)（不变量 152）。txid 不是 wtxid。改见证不是已经改交易身份。头上的 txid Merkle 不是已经承诺 wtxid。按 wtxid 通告不是已经有那笔交易：[`../../tracks/network/worked-example-wtxidrelay-vs-have.md`](../../tracks/network/worked-example-wtxidrelay-vs-have.md) BIP-339 wtxid-ann not already have / not already accepted / not already never-again 正式三事（248 余量）：[`../../tracks/network/worked-example-wtx339-nothave-vs-bundled.md`](../../tracks/network/worked-example-wtx339-nothave-vs-bundled.md)（不变量 1247）。 BIP-339 wtxidrelay not already switched / not already negotiated / not already using 正式三事（248 余量）：[`../../tracks/network/worked-example-wtx339-notswitch-vs-bundled.md`](../../tracks/network/worked-example-wtx339-notswitch-vs-bundled.md)（不变量 1248）。 BIP-339 old-getdata not already retired / not already have-wit / not already net-wide 正式三事（248 余量）：[`../../tracks/network/worked-example-wtx339-notold-vs-bundled.md`](../../tracks/network/worked-example-wtx339-notold-vs-bundled.md)（不变量 1249）。（不变量 248）。带见证的线上序列化不是已经有见证：[`../../tracks/network/worked-example-witness-wire-vs-have.md`](../../tracks/network/worked-example-witness-wire-vs-have.md) BIP-144 witness-ser not already have / not already accepted / not already no-capability 正式三事（251 余量）：[`../../tracks/network/worked-example-wit144-nothave-vs-bundled.md`](../../tracks/network/worked-example-wit144-nothave-vs-bundled.md)（不变量 1256）。 BIP-144 service-bit not already sending / not already have / not already old-retired 正式三事（251 余量）：[`../../tracks/network/worked-example-wit144-notsend-vs-bundled.md`](../../tracks/network/worked-example-wit144-notsend-vs-bundled.md)（不变量 1257）。 BIP-144 old-inv not already no-wit / not already wtxid-ann / not already verified 正式三事（251 余量）：[`../../tracks/network/worked-example-wit144-notold-vs-bundled.md`](../../tracks/network/worked-example-wit144-notold-vs-bundled.md)（不变量 1258）。（不变量 251）。看见 Bech32 地址串不是链上已经有这笔输出：[`../../tracks/implementation/worked-example-address-vs-utxo.md`](../../tracks/implementation/worked-example-address-vs-utxo.md)（不变量 174）。后继校验过了不是已经是旧校验那套地址：[`../../tracks/implementation/worked-example-bech32m-vs-bech32.md`](../../tracks/implementation/worked-example-bech32m-vs-bech32.md)（不变量 181）。

---

## H. 攻击者模型

- 在激活窗口挖「旧节点收、新节点拒」或相反的块，制造社会分裂。  
- 骗用户「旧节点也完整验证了 SegWit」。  
- 用「扩容数字」把结构课讲成营销课。

---

## I. 代价

得到：延展性修复、软分叉兼容、见证可单独传播。  
换：两套哈希（txid/wtxid）、旧节点验证变薄、钱包与手续费估计变复杂。

---

## J. 对「不确定」的意义

后量子签名更大。若要把大签放进「旧节点不理解的附件」：

1. 必须写清旧节点少验了什么；  
2. 必须有新节点法定的完整验证；  
3. 算法敏捷更干净的做法往往是**版本化字段**，而不是永远靠「看起来像旧脚本」。

**建议：** 偷软分叉的纪律（不踢旧验证者出历史），不要偷「用任何人可花的外壳骗过旧节点」当通用技巧——那是 Bitcoin 脚本模型下的特例。

---

## 精密检查

| 层 | 本课 |
|---|---|
| 密码学 | 签名仍要验；改的是签在哪一段哈希里 |
| 协议 | 软分叉：新严旧松 |
| 实现 | txid/wtxid 算错即分裂 |
| 部署 | 谁升级谁做完整验证 |
| 经济 | 矿工/节点激励是否执行新规则 |

**禁止假学习：** 「SegWit 是硬分叉扩容。」「旧节点和以前一样安全。」「见证折扣 = 官方 TPS。」「交易哈希 = 已经含签名。」「块头 Merkle 绿 = 见证已进头。」「txid = wtxid。」「付给哈希 = 赎回已经揭开。」「旧节点 EQUAL 通过 = 新节点已经再跑。」「16 = Taproot。」「看见地址 = 已经有 UTXO。」「校验过 = 程序已经上链。」「173 = 141。」「173 = 350。」「后继校验过了 = 已经是 173。」「更高版本过了旧校验 = 已经合法。」「350 = 141。」「走了脚本路径 = 已经是 342。」「成功操作码 = 已经执行完。」「342 = 341。」「看见 Miniscript = 已经是链上脚本。」「共识健全 = 已经策略完备。」「379 = 380。」「按 wtxid 通告 = 已经有交易。」「发了 wtxidrelay = 已经改口。」「仍用旧类型要父交易 = 旧库存已经退役。」「339 = 152。」「带见证的线上序列化 = 已经有见证。」「能提供见证 = 已经在传。」「库存通告仍用旧类型 = 线上已经没有见证。」「144 = 141。」「dummy 不是空 = 已经合法。」「隔离见证开了 = 已经没有 dummy 延展。」「策略已经要空 dummy = 共识已经要。」「147 = 66。」  
**边界：** 不抄 Tapscript 操作码号、不讲闪电路由、不背激活日期表。走脚本路径 ≠ 已经是 tapscript 语义见 **C193** / 不变量 **189**：[`../../tracks/implementation/worked-example-tapscript-vs-scriptpath.md`](../../tracks/implementation/worked-example-tapscript-vs-scriptpath.md)。不抄承诺魔数 / 重量公式 / 版本 0 程序长度。`txid` ≠ `wtxid` 见 **C156** / 不变量 **152**。政策门 ≠ 共识门见 **C148**。钥匙路径 ≠ 揭树见 **C157** / 不变量 **153**：[`../../tracks/implementation/worked-example-keypath-vs-scriptpath.md`](../../tracks/implementation/worked-example-keypath-vs-scriptpath.md)。付给脚本哈希 ≠ 已经揭开赎回脚本见 **C174** / 不变量 **170**：[`../../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md`](../../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md)。看见 Bech32 地址串 ≠ 链上已经有这笔输出见 **C178** / 不变量 **174**：[`../../tracks/implementation/worked-example-address-vs-utxo.md`](../../tracks/implementation/worked-example-address-vs-utxo.md)。后继校验过了 ≠ 已经是旧校验那套地址见 **C185** / 不变量 **181**：[`../../tracks/implementation/worked-example-bech32m-vs-bech32.md`](../../tracks/implementation/worked-example-bech32m-vs-bech32.md)。Taproot 路径用 BIP-340；tagged hash 公式在 [`../../tracks/crypto/worked-example-tagged-hash.md`](../../tracks/crypto/worked-example-tagged-hash.md)，本课不展开曲线。不抄激活票数。不抄字符表 / 例地址。不写怎样构造旧合法新非法的赎回。看见 Miniscript ≠ 已经是链上脚本见 **C195** / 不变量 **191**：[`../../tracks/implementation/worked-example-miniscript-vs-script.md`](../../tracks/implementation/worked-example-miniscript-vs-script.md)。按 wtxid 通告 ≠ 已经有交易；发了 wtxidrelay ≠ 已经改口；仍用旧类型要父交易 ≠ 旧库存已经退役：[`../../tracks/network/worked-example-wtxidrelay-vs-have.md`](../../tracks/network/worked-example-wtxidrelay-vs-have.md)（不变量 248）。带见证的线上序列化 ≠ 已经有见证；能提供见证 ≠ 已经在传；库存通告仍用旧类型 ≠ 线上已经没有见证：[`../../tracks/network/worked-example-witness-wire-vs-have.md`](../../tracks/network/worked-example-witness-wire-vs-have.md)（不变量 251）。不写怎样增删字符撞合法地址。不写怎样拼片段。不要写怎样改见证挡住转发。不要抄协议版本号 / 库存类型取值。不要抄标记 / 旗标。不要写怎样拼能骗过旧解析器的字节。看见多余栈元素 ≠ 已经随便填；看见隔离见证 ≠ 已经没有这条延展；看见转发策略已经要空 dummy ≠ 已经是共识：[`../../tracks/implementation/worked-example-dummy-vs-empty.md`](../../tracks/implementation/worked-example-dummy-vs-empty.md)（不变量 264）。 BIP-147 dummy not already arbitrary / not already legal / not already settled 正式三事（264 余量）：[`../../tracks/implementation/worked-example-dum147-notany-vs-bundled.md`](../../tracks/implementation/worked-example-dum147-notany-vs-bundled.md)（不变量 1229）。 BIP-147 segwit not already no-dummy-malleation / not already wtxid-fixed / not already settled 正式三事（264 余量）：[`../../tracks/implementation/worked-example-dum147-notwit-vs-bundled.md`](../../tracks/implementation/worked-example-dum147-notwit-vs-bundled.md)（不变量 1230）。 BIP-147 policy not already consensus / not already bip62 / not already settled 正式三事（264 余量）：[`../../tracks/implementation/worked-example-dum147-notpol-vs-bundled.md`](../../tracks/implementation/worked-example-dum147-notpol-vs-bundled.md)（不变量 1231）。不要抄激活时间。不要写怎样改 dummy 撞身份。
