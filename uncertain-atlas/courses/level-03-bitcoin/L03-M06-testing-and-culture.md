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

**禁止假学习：** 「Bitcoin 从未出过通胀事故。」「因为去中心所以不会有实现洞。」「看见 xpub = 已经能花。」「能推子钥 = 已经是地址。」「32 = 174。」「看见词 = 已经是种子。」「39 = 32。」「有钥 = 已经知道脚本。」「看见描述符 = 已经是地址。」「380 = 39。」「看见 v2 = 已经是旧包。」「能加栏 = 已经能广播。」「370 = 174。」「看见 Miniscript = 已经是链上脚本。」「379 = 380。」「看见付款 URI = 已经授权。」「看见路径没有链上地址 = 已经没有指示。」「看见不认识的必选参数 = 已经能付。」「看见打开了回执 = 已经确认。」「看见签过 = 已经能花。」「看见资金证明清单 = 已经齐。」「看见静默付款地址 = 已经有输出。」「看见扫过 = 已经收到。」「看见可读名字 = 已经该走 DNS。」「看见 TXT = 已经合法。」「看见 signet = 已经是 testnet。」「看见 signet = 已经是 regtest。」「看见头上有合法工作量 = 已经签过。」「看见 BIP32 compatible = 已经能互操作。」「看见自称 BIPxx compatible = 已经是那份结构。」「看见同一份种子 = 已经是同一条币。」「看见余额为零 = 已经发现完。」「看见同一套 BIP44 账户 = 已经能找回嵌套隔离见证。」「看见账户出现了 = 已经不用核余额。」「看见现有多签派生习惯 = 已经要搬家。」「看见脚本类型层 = 已经是账户层。」「看见同一套钥 = 已经是同一条 P2SH 地址。」「看见前面分支没有交易 = 已经发现完。」「看见派生钥 = 已经是输出钥。」「看见付款码 = 已经是存款地址。」「看见 multi = 已经按字典序排。」「看见 tr 没有树 = 已经有脚本路径。」「看见 pk = 已经和 pkh / sh 同一套放置。」「看见 wpkh / wsh = 已经只能顶层。」「看见 multi_a = 已经是 383 那种 multi。」「看见旧 PSBT 栏 = 已经能装 Taproot。」「看见钱包策略 = 已经是一条描述符。」「看见 combo = 已经只能产出一种脚本。」「看见 raw = 已经具名脚本。」「看见聚合钥 = 已经是扩展公钥。」「看见旧 PSBT 栏 = 已经能装 MuSig2。」「看见脚本各走各的路径 = 已经是多签该有的树。」「看见一份助记词 = 已经能备齐所有钱包。」「看见签流程 = 已经是跨厂安全多签开户。」「看见一条派生路径 = 已经是一份路径模板。」「看见共享了扩展公钥 = 已经是链码委托。」「看见带 pj= 的付款 URI = 已经是 payjoin 付款。」「看见原始包 = 已经是提案。」「看见收款方加了输入 = 已经另开一笔。」「看见自家习惯的输入输出顺序 = 已经是字典序标准。」「看见按字典序排了 = 已经是共识。」「看见按字典序排了 = 已经私人。」「看见 Testnet 4 = 已经是 Testnet 3。」「看见 20 分钟例外 = 已经没有块风暴。」「看见会 Testnet 3 = 已经能安全跟 Testnet 4。」「看见储备证明交易 = 已经能花。」「看见其余输入签过 = 已经控制资金。」「看见 POR 栏 = 已经是普通花费。」「看见本页这种签消息 = 已经是 322。」「看见头字节标了种类 = 已经有地址。」「看见旧 P2PKH 习惯 = 已经互操作。」「看见付款请求 = 已经授权。」「看见付款报文 = 已经是回执。」「看见回执 = 已经最终。」  
**边界：** 不写闪电网络；不把 Core 开发过程神化。迁移失败 ≠ 目录里其它钱包已经安全：[`../../tracks/failure-museum/bitcoin-2026-01-wallet-migration-delete.md`](../../tracks/failure-museum/bitcoin-2026-01-wallet-migration-delete.md)（不变量 120）。privatebroadcast 开关 ≠ IP 已经不暴露：[`../../tracks/failure-museum/bitcoin-2026-06-privatebroadcast-v1-retry.md`](../../tracks/failure-museum/bitcoin-2026-06-privatebroadcast-v1-retry.md)（不变量 112）。看见部分签名包 ≠ 已经是网上能广播的完整交易：[`../../tracks/implementation/worked-example-psbt-vs-broadcast.md`](../../tracks/implementation/worked-example-psbt-vs-broadcast.md)（不变量 179）。看见扩展公钥 ≠ 已经能花：[`../../tracks/implementation/worked-example-xpub-vs-spendable.md`](../../tracks/implementation/worked-example-xpub-vs-spendable.md)（不变量 182）。看见助记词 ≠ 已经是二进制种子：[`../../tracks/implementation/worked-example-mnemonic-vs-seed.md`](../../tracks/implementation/worked-example-mnemonic-vs-seed.md)（不变量 183）。看见私钥或助记词备份 ≠ 已经知道该看哪种输出脚本：[`../../tracks/implementation/worked-example-descriptor-vs-keys.md`](../../tracks/implementation/worked-example-descriptor-vs-keys.md)（不变量 184）。看见后继版本工作包 ≠ 已经是旧版那份固定未签交易：[`../../tracks/implementation/worked-example-psbtv2-vs-v0.md`](../../tracks/implementation/worked-example-psbtv2-vs-v0.md)（不变量 186）。不要写怎样踩迁移失败。不要写怎样拼未签包去冒充已签。不要写怎样从扩展公钥推子钥。不要写怎样从助记词推种子。看见 Miniscript ≠ 已经是链上脚本：[`../../tracks/implementation/worked-example-miniscript-vs-script.md`](../../tracks/implementation/worked-example-miniscript-vs-script.md)（不变量 191）。不要写怎样拼描述符。不要写怎样把后继包改回旧包。不要写怎样拼片段。看见付款 URI ≠ 已经授权；路径没有链上地址 ≠ 已经没有指示；不认识的必选参数 ≠ 已经能付：[`../../tracks/lifecycle/worked-example-uri-vs-authorized.md`](../../tracks/lifecycle/worked-example-uri-vs-authorized.md)（不变量 255）。不要抄例地址 / 语法细则 / 金额写法。不要另写 BIP-21 当现行方案。不要写怎样造能骗过旧钱包的必选参数。看见签过的消息 ≠ 已经证明能控制资金；看见资金证明清单 ≠ 已经齐：[`../../tracks/lifecycle/worked-example-signed-message-vs-control.md`](../../tracks/lifecycle/worked-example-signed-message-vs-control.md)（不变量 258）。不要抄编码前缀或虚拟交易字段。不要写怎样拼能过验证器的签消息。看见静默付款地址 ≠ 已经有一笔链上输出；看见扫过 ≠ 已经收到：[`../../tracks/lifecycle/worked-example-silent-payment-vs-output.md`](../../tracks/lifecycle/worked-example-silent-payment-vs-output.md)（不变量 260）。不要抄派生公式或例地址。不要写怎样扫链或派生输出。看见可读名字 ≠ 已经该走 DNS；看见 TXT ≠ 已经是合法付款指示：[`../../tracks/lifecycle/worked-example-dns-name-vs-instruction.md`](../../tracks/lifecycle/worked-example-dns-name-vs-instruction.md)（不变量 261）。不要抄 DNS 标签拼法或例名。不要另写 BIP-21 当现行用户方案。不要写怎样枚举用户。看见 signet ≠ 已经是 testnet；看见 signet ≠ 已经是 regtest；看见头上有合法工作量 ≠ 已经签过：[`../../tracks/implementation/worked-example-signet-vs-testnet.md`](../../tracks/implementation/worked-example-signet-vs-testnet.md)（不变量 265）。不要抄挑战头字节 / 最低难度 / 创世哈希。不要写怎样拼挑战或造假签块。看见 BIP32 compatible ≠ 已经能互操作；看见自称 BIPxx compatible ≠ 已经是那份结构：[`../../tracks/implementation/worked-example-purpose-vs-compatible.md`](../../tracks/implementation/worked-example-purpose-vs-compatible.md)（不变量 266）。不要抄用途号取值或例路径。不要写怎样选用途号或从种子扫账户。看见同一份种子 ≠ 已经是同一条币；看见余额为零 ≠ 已经发现完：[`../../tracks/implementation/worked-example-account-vs-discovered.md`](../../tracks/implementation/worked-example-account-vs-discovered.md)（不变量 267）。不要抄用途号或间隙条数。不要写怎样扫间隙或枚举账户。看见同一套 BIP44 账户 ≠ 已经能找回嵌套隔离见证；看见账户出现了 ≠ 已经不用核余额：[`../../tracks/implementation/worked-example-nested-vs-same-account.md`](../../tracks/implementation/worked-example-nested-vs-same-account.md)（不变量 268）。不要抄用途号或脚本套法。不要写怎样套脚本或从种子扫嵌套地址。看见现有多签派生习惯 ≠ 已经要搬家；看见脚本类型层 ≠ 已经是账户层：[`../../tracks/implementation/worked-example-script-type-vs-account.md`](../../tracks/implementation/worked-example-script-type-vs-account.md)（不变量 269）。不要抄脚本类型取值或例路径。不要写怎样排序公钥或从种子扫多签。看见同一套钥 ≠ 已经是同一条 P2SH 地址；看见未压缩钥 ≠ 已经是本页：[`../../tracks/implementation/worked-example-sorted-vs-one-address.md`](../../tracks/implementation/worked-example-sorted-vs-one-address.md)（不变量 270）。不要抄压缩钥例、地址例、脚本十六进制。不要写怎样按字节字典序排公钥。看见共享主公钥 ≠ 已经是本页；看见前面分支没有交易 ≠ 已经发现完：[`../../tracks/implementation/worked-example-cosigner-vs-discovered.md`](../../tracks/implementation/worked-example-cosigner-vs-discovered.md)（不变量 271）。不要抄用途号或间隙条数。不要写怎样按用途公钥排下标或从种子扫每一支。看见派生钥 ≠ 已经是输出钥；看见不需要脚本路径 ≠ 已经不承诺：[`../../tracks/implementation/worked-example-derived-vs-output-key.md`](../../tracks/implementation/worked-example-derived-vs-output-key.md)（不变量 272）。不要抄用途号或地址例。不要写怎样算标签微调。看见付款码 ≠ 已经是存款地址；看见通知输出 ≠ 已经能花：[`../../tracks/lifecycle/worked-example-payment-code-vs-notification.md`](../../tracks/lifecycle/worked-example-payment-code-vs-notification.md)（不变量 273）。不要抄用途号或编码版本字节。不要写怎样做 ECDH 或怎样拼通知。看见 multi ≠ 已经按字典序排；看见门限和钥数 ≠ 已经同一套上限：[`../../tracks/implementation/worked-example-multi-vs-sortedmulti.md`](../../tracks/implementation/worked-example-multi-vs-sortedmulti.md)（不变量 274）。不要抄函数名单或脚本模板。不要写怎样按字节排公钥。看见 tr 没有树 ≠ 已经有脚本路径；看见树表达式 ≠ 已经是旧脚本套法：[`../../tracks/implementation/worked-example-tr-vs-tree.md`](../../tracks/implementation/worked-example-tr-vs-tree.md)（不变量 275）。不要抄树花括号或微调公式。不要写怎样把压缩钥抬成 x-only。看见 pk ≠ 已经和 pkh / sh 同一套放置；看见 sh 产出 ≠ 已经有赎回脚本：[`../../tracks/implementation/worked-example-pk-vs-toplevel.md`](../../tracks/implementation/worked-example-pk-vs-toplevel.md)（不变量 276）。不要抄脚本模板或测试向量。不要写怎样拼 P2PK。看见 wpkh / wsh ≠ 已经只能顶层；看见未压缩钥 ≠ 已经允许：[`../../tracks/implementation/worked-example-wpkh-vs-compressed.md`](../../tracks/implementation/worked-example-wpkh-vs-compressed.md)（不变量 277）。不要抄脚本模板或测试向量。不要写怎样拼见证程序。看见 multi_a ≠ 已经是 383 那种 multi；看见门限 ≠ 已经同一套编码：[`../../tracks/implementation/worked-example-multia-vs-tr.md`](../../tracks/implementation/worked-example-multia-vs-tr.md)（不变量 278）。不要抄脚本模板或测试向量。不要写怎样按 x-only 排公钥。看见旧 PSBT 栏 ≠ 已经能装 Taproot；看见输出脚本里的钥 ≠ 已经是内部钥：[`../../tracks/implementation/worked-example-tap-psbt-vs-old.md`](../../tracks/implementation/worked-example-tap-psbt-vs-old.md)（不变量 279）。不要抄类型号或测试向量。不要写怎样拼控制块。看见钱包策略 ≠ 已经是一条描述符；看见钥占位 ≠ 已经是那把精确公钥：[`../../tracks/implementation/worked-example-policy-vs-descriptor.md`](../../tracks/implementation/worked-example-policy-vs-descriptor.md)（不变量 280）。看见 combo ≠ 已经只能产出一种脚本；看见未压缩钥 ≠ 已经带齐见证对：[`../../tracks/implementation/worked-example-combo-vs-one-script.md`](../../tracks/implementation/worked-example-combo-vs-one-script.md)（不变量 281）。看见 raw ≠ 已经能套进具名表达式；看见 addr ≠ 已经是那份输出脚本：[`../../tracks/implementation/worked-example-raw-vs-named.md`](../../tracks/implementation/worked-example-raw-vs-named.md)（不变量 282）。看见 MuSig2 聚合钥 ≠ 已经是扩展公钥；看见合成扩展公钥 ≠ 已经能硬化派生：[`../../tracks/implementation/worked-example-musig-xpub-vs-aggregate.md`](../../tracks/implementation/worked-example-musig-xpub-vs-aggregate.md)（不变量 283）。看见旧 PSBT 栏 ≠ 已经能装 MuSig2；看见聚合钥栏 ≠ 已经是输出钥：[`../../tracks/implementation/worked-example-musig-psbt-vs-tap.md`](../../tracks/implementation/worked-example-musig-psbt-vs-tap.md)（不变量 284）。看见脚本各走各的路径 ≠ 已经是多签该有的树；看见路径里的脚本类型 ≠ 已经必要：[`../../tracks/implementation/worked-example-multisig-path-vs-script.md`](../../tracks/implementation/worked-example-multisig-path-vs-script.md)（不变量 285）。看见一份助记词 ≠ 已经能备齐所有钱包；看见扩展根钥 ≠ 已经能倒回助记词：[`../../tracks/implementation/worked-example-entropy-vs-seed.md`](../../tracks/implementation/worked-example-entropy-vs-seed.md)（不变量 286）。不要抄占位写法或测试向量。不要写怎样编译占位。不要写怎样拼那几份输出脚本。不要写怎样把地址解成脚本。不要写怎样算派生微调。不要写怎样造 nonce 或部分签。不要写怎样加账户号。不要写怎样从子钥算出熵。看见部分签名包 ≠ 已经是跨厂安全多签开户；看见指纹对上 ≠ 已经核过 KEY：[`../../tracks/implementation/worked-example-setup-vs-psbt.md`](../../tracks/implementation/worked-example-setup-vs-psbt.md)（不变量 287）。不要抄记录行格式或测试向量。不要写怎样核对钥或怎样加密会话。看见一条派生路径 ≠ 已经是一份路径模板；看见写死了熟路径检查 ≠ 已经能互操作：[`../../tracks/implementation/worked-example-template-vs-path.md`](../../tracks/implementation/worked-example-template-vs-path.md)（不变量 288）。不要抄语法取值或模板例句。不要写怎样解析或匹配模板。看见共享了扩展公钥 ≠ 已经是链码委托；看见委托方那把非扩展钥 ≠ 已经能推出整棵钱包：[`../../tracks/implementation/worked-example-delegation-vs-xpub.md`](../../tracks/implementation/worked-example-delegation-vs-xpub.md)（不变量 289）。不要抄微调算法或测试向量。不要写怎样做委托微调或盲签。看见带 pj= 的付款 URI ≠ 已经是 payjoin 付款；看见原始包 ≠ 已经是提案；看见收款方加了输入 ≠ 已经另开一笔：[`../../tracks/lifecycle/worked-example-payjoin-vs-original.md`](../../tracks/lifecycle/worked-example-payjoin-vs-original.md)（不变量 290）。不要抄 HTTP 配方或加费公式。不要写怎样构造提案或怎样加费。看见自家习惯的输入输出顺序 ≠ 已经是字典序标准；看见按字典序排了 ≠ 已经是共识 / ≠ 已经私人：[`../../tracks/implementation/worked-example-order-vs-lex.md`](../../tracks/implementation/worked-example-order-vs-lex.md)（不变量 291）。不要抄比较算法或例交易。不要写怎样按前交易哈希排输入。看见 Testnet 4 ≠ 已经是 Testnet 3；看见 20 分钟例外 ≠ 已经没有块风暴；看见会 Testnet 3 ≠ 已经能安全跟：[`../../tracks/implementation/worked-example-testnet4-vs-testnet3.md`](../../tracks/implementation/worked-example-testnet4-vs-testnet3.md)（不变量 292）。不要抄创世哈希或端口。不要写怎样挖最低难度或怎样造块风暴。看见储备证明交易 ≠ 已经能花；看见其余输入签过 ≠ 已经控制资金；看见 POR 栏 ≠ 已经是普通花费：[`../../tracks/lifecycle/worked-example-reserves-vs-spend.md`](../../tracks/lifecycle/worked-example-reserves-vs-spend.md)（不变量 293）。不要抄哈希前缀或栏类型号。不要写怎样造承诺输入或怎样填 POR 栏。看见本页这种签消息 ≠ 已经是 322；看见头字节标了种类 ≠ 已经有地址；看见旧 P2PKH 习惯 ≠ 已经互操作：[`../../tracks/lifecycle/worked-example-legacy-sign-vs-322.md`](../../tracks/lifecycle/worked-example-legacy-sign-vs-322.md)（不变量 294）。不要抄头字节取值或示例代码。不要写怎样从头字节还原公钥。看见付款请求 ≠ 已经授权；看见付款报文 ≠ 已经是回执；看见回执 ≠ 已经最终：[`../../tracks/lifecycle/worked-example-request-vs-ack.md`](../../tracks/lifecycle/worked-example-request-vs-ack.md)（不变量 295）。不要抄消息编码或传输头。不要写怎样拼付款请求或怎样验证书链。不要另写 BIP-71 / BIP-72。
