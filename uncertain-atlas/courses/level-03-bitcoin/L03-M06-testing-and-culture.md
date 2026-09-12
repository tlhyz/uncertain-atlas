# L3.6 保守工程与测试文化

优先级：重要（知识树 M3.6 / M3.7 的方法部分）  
先修：L3.3，L9.7，失败博物馆两案

---

## A. 先修知识

L3.3：慢升级本身是安全特性。  
博物馆：2010 溢出、2018 重复输入——都是实现没守住「供给守恒」。

---

## B. 核心问题

**Bitcoin 能跑十几年，是因为「没人攻击」，还是因为规则小、全节点可验证、变更慢、事故会回流成规则？**

---

## C. 直觉（ELI15）

一间只做加减法的厨房，菜单十年加一道菜。  
菜谱公开，谁都可以在自己灶上复做同一道菜。  
有一次油锅溢了（溢出），他们把「倒油前先看刻度」写进每道菜，而不是发明新灶具品牌。

稳定来自：**可复做 + 菜单短 + 溢过油就改刻度**。不是来自「厨房从未失火」的神话。

---

## D. 正式定义

**可验证性（事实）**

任意人可跑全节点，按同一规则重放。这把实现保证放到用户能执行的位置，而不只在发行方实验室。

**规则表面积**

脚本有意弱。表面积小，测试与审计的句子少。这是产品选择，换来的是少合约表达力。

**事故回流**

CVE-2010-5139：输出和溢出 → 必须检查和不溢出且不超过上限。  
CVE-2018-17144：重复输入 → 必须检查唯一花费。  
两案都没有让「PoW 数学」失效。

**事实：** 「看起来没崩」不是证据。崩过、修过、节点升上去，才是历史。  
**推断：** 文化（全节点、慢变）降低了「静默改供给」的频率；它不保证下一次实现洞不存在。

---

## E. 最小案例

对比：通用世界计算机，菜单每天加菜，两家餐厅做同一道菜口味不同（多客户端税）。  
Bitcoin：少菜、单主实现文化更重。单实现灭绝风险换来的是「少一套分歧」。Ethereum 走另一条（L5.3）。  
「不确定」要同时偷：小规则 + 预留第二实现位置。两者有张力，必须写明。

---

## F. 真实项目

Bitcoin Core 的 fuzz 与回归；软分叉评审。  
源码入口预告：共识检查函数、测试向量。先读博物馆再读 diff。

---

## G. 源码入口

预告：`CheckTransaction` / 连接块时的输入唯一性。路径以当前仓库为准。

---

## H. 攻击者模型

- 专找「从未有人构造过的交易形状」。  
- 社会层：用「十年没出大事」推销不升级。  
- 把应用层事故（交易所）算成协议胜利或失败。

---

## I. 代价

保守：新能力极慢。  
激进：活得像产品公司，假设失效传播更快。

---

## J. 对「不确定」的意义

后量子结算第一版更该像这间厨房，而不是每日新菜。  
算法敏捷是「允许以后加菜谱编号」，不是「每天换灶」。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | 测试绿不证明曲线安全 |
| 协议 | 回归必须钉共识不变量 |
| 实现 | fuzz / 差分抓实现洞（CVE-2018-17144 一类） |
| 部署 | 测试网 ≠ 主网拓扑；signet ≠ 已经是 testnet / regtest / 已经签过 |
| 经济 | 「从未出事」不是证明；通胀事故曾经发生（CVE-2010-5139） |

**禁止假学习：** 「Bitcoin 从未出过通胀事故。」「因为去中心所以不会有实现洞。」「看见 xpub = 已经能花。」「能推子钥 = 已经是地址。」「32 = 174。」「看见词 = 已经是种子。」「39 = 32。」「有钥 = 已经知道脚本。」「看见描述符 = 已经是地址。」「380 = 39。」「看见 v2 = 已经是旧包。」「能加栏 = 已经能广播。」「370 = 174。」「看见 Miniscript = 已经是链上脚本。」「379 = 380。」「看见付款 URI = 已经授权。」「看见路径没有链上地址 = 已经没有指示。」「看见不认识的必选参数 = 已经能付。」「看见打开了回执 = 已经确认。」「看见签过 = 已经能花。」「看见资金证明清单 = 已经齐。」「看见静默付款地址 = 已经有输出。」「看见扫过 = 已经收到。」「看见可读名字 = 已经该走 DNS。」「看见 TXT = 已经合法。」「看见 signet = 已经是 testnet。」「看见 signet = 已经是 regtest。」「看见头上有合法工作量 = 已经签过。」「看见 BIP32 compatible = 已经能互操作。」「看见自称 BIPxx compatible = 已经是那份结构。」「看见同一份种子 = 已经是同一条币。」「看见余额为零 = 已经发现完。」「看见同一套 BIP44 账户 = 已经能找回嵌套隔离见证。」「看见账户出现了 = 已经不用核余额。」「看见现有多签派生习惯 = 已经要搬家。」「看见脚本类型层 = 已经是账户层。」  
**边界：** 不写闪电网络；不把 Core 开发过程神化。迁移失败 ≠ 目录里其它钱包已经安全：[`../../tracks/failure-museum/bitcoin-2026-01-wallet-migration-delete.md`](../../tracks/failure-museum/bitcoin-2026-01-wallet-migration-delete.md)（不变量 120）。privatebroadcast 开关 ≠ IP 已经不暴露：[`../../tracks/failure-museum/bitcoin-2026-06-privatebroadcast-v1-retry.md`](../../tracks/failure-museum/bitcoin-2026-06-privatebroadcast-v1-retry.md)（不变量 112）。看见部分签名包 ≠ 已经是网上能广播的完整交易：[`../../tracks/implementation/worked-example-psbt-vs-broadcast.md`](../../tracks/implementation/worked-example-psbt-vs-broadcast.md)（不变量 179）。看见扩展公钥 ≠ 已经能花：[`../../tracks/implementation/worked-example-xpub-vs-spendable.md`](../../tracks/implementation/worked-example-xpub-vs-spendable.md)（不变量 182）。看见助记词 ≠ 已经是二进制种子：[`../../tracks/implementation/worked-example-mnemonic-vs-seed.md`](../../tracks/implementation/worked-example-mnemonic-vs-seed.md)（不变量 183）。看见私钥或助记词备份 ≠ 已经知道该看哪种输出脚本：[`../../tracks/implementation/worked-example-descriptor-vs-keys.md`](../../tracks/implementation/worked-example-descriptor-vs-keys.md)（不变量 184）。看见后继版本工作包 ≠ 已经是旧版那份固定未签交易：[`../../tracks/implementation/worked-example-psbtv2-vs-v0.md`](../../tracks/implementation/worked-example-psbtv2-vs-v0.md)（不变量 186）。不要写怎样踩迁移失败。不要写怎样拼未签包去冒充已签。不要写怎样从扩展公钥推子钥。不要写怎样从助记词推种子。看见 Miniscript ≠ 已经是链上脚本：[`../../tracks/implementation/worked-example-miniscript-vs-script.md`](../../tracks/implementation/worked-example-miniscript-vs-script.md)（不变量 191）。不要写怎样拼描述符。不要写怎样把后继包改回旧包。不要写怎样拼片段。看见付款 URI ≠ 已经授权；路径没有链上地址 ≠ 已经没有指示；不认识的必选参数 ≠ 已经能付：[`../../tracks/lifecycle/worked-example-uri-vs-authorized.md`](../../tracks/lifecycle/worked-example-uri-vs-authorized.md)（不变量 255）。不要抄例地址 / 语法细则 / 金额写法。不要另写 BIP-21 当现行方案。不要写怎样造能骗过旧钱包的必选参数。看见签过的消息 ≠ 已经证明能控制资金；看见资金证明清单 ≠ 已经齐：[`../../tracks/lifecycle/worked-example-signed-message-vs-control.md`](../../tracks/lifecycle/worked-example-signed-message-vs-control.md)（不变量 258）。不要抄编码前缀或虚拟交易字段。不要写怎样拼能过验证器的签消息。看见静默付款地址 ≠ 已经有一笔链上输出；看见扫过 ≠ 已经收到：[`../../tracks/lifecycle/worked-example-silent-payment-vs-output.md`](../../tracks/lifecycle/worked-example-silent-payment-vs-output.md)（不变量 260）。不要抄派生公式或例地址。不要写怎样扫链或派生输出。看见可读名字 ≠ 已经该走 DNS；看见 TXT ≠ 已经是合法付款指示：[`../../tracks/lifecycle/worked-example-dns-name-vs-instruction.md`](../../tracks/lifecycle/worked-example-dns-name-vs-instruction.md)（不变量 261）。不要抄 DNS 标签拼法或例名。不要另写 BIP-21 当现行用户方案。不要写怎样枚举用户。看见 signet ≠ 已经是 testnet；看见 signet ≠ 已经是 regtest；看见头上有合法工作量 ≠ 已经签过：[`../../tracks/implementation/worked-example-signet-vs-testnet.md`](../../tracks/implementation/worked-example-signet-vs-testnet.md)（不变量 265）。不要抄挑战头字节 / 最低难度 / 创世哈希。不要写怎样拼挑战或造假签块。看见 BIP32 compatible ≠ 已经能互操作；看见自称 BIPxx compatible ≠ 已经是那份结构：[`../../tracks/implementation/worked-example-purpose-vs-compatible.md`](../../tracks/implementation/worked-example-purpose-vs-compatible.md)（不变量 266）。不要抄用途号取值或例路径。不要写怎样选用途号或从种子扫账户。看见同一份种子 ≠ 已经是同一条币；看见余额为零 ≠ 已经发现完：[`../../tracks/implementation/worked-example-account-vs-discovered.md`](../../tracks/implementation/worked-example-account-vs-discovered.md)（不变量 267）。不要抄用途号或间隙条数。不要写怎样扫间隙或枚举账户。看见同一套 BIP44 账户 ≠ 已经能找回嵌套隔离见证；看见账户出现了 ≠ 已经不用核余额：[`../../tracks/implementation/worked-example-nested-vs-same-account.md`](../../tracks/implementation/worked-example-nested-vs-same-account.md)（不变量 268）。不要抄用途号或脚本套法。不要写怎样套脚本或从种子扫嵌套地址。看见现有多签派生习惯 ≠ 已经要搬家；看见脚本类型层 ≠ 已经是账户层：[`../../tracks/implementation/worked-example-script-type-vs-account.md`](../../tracks/implementation/worked-example-script-type-vs-account.md)（不变量 269）。不要抄脚本类型取值或例路径。不要写怎样排序公钥或从种子扫多签。
