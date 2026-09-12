# L1.4 规范编码

优先级：重要  
先修：L0.2，L1.1，L1.2

---

## A. 先修知识

复制状态机要求：同一输入字节，同一结果。  
签名和哈希吃的是字节，不是「我们心里的意思」。

---

## B. 核心问题

**为什么「意思一样、写法不一样」可以把一条链劈成两条？**

---

## C. 直觉（ELI15）

「一百」和「100」对人都一样。  
对哈希完全不一样。

如果节点 A 接受松散写法，节点 B 只接受一种写法：

- A 认为交易有效并打包
- B 验签或算根时对不上，拒绝这个块

两边都觉得自己在执行同一份协议。  
世界已经分裂。这不是密码被破，是**实现保证**先死。

规范编码的意思：每个抽象对象只允许一种字节表示进入共识。

---

## D. 正式定义（本科计算机）

**Canonical encoding**：协议规定的、唯一允许的序列化。

非规范的典型口子：

1. 同一整数的多种长度（前导零）
2. 同一公钥的压缩/非压缩
3. JSON / protobuf 字段顺序
4. 签名的 malleability（r,s 与 r,-s）
5. 交易多输入的排序是否强制
6. 错误字符串、非 UTF-8、未定义枚举进入状态

**事实：** Bitcoin 有 script 和 DER 签名的历史包袱；后来用更严的标准（如严格 DER、SegWit 后的新序列化）收口。  
**事实：** 多客户端链（Ethereum）必须把编码写到「两个实现算同一个根」。可执行规范存在的原因之一就是这个。
类型字节不是已经解开内层。旧式列表不是已经是信封。2718 不是 1559。精读：[`../../tracks/implementation/worked-example-typed-vs-legacy.md`](../../tracks/implementation/worked-example-typed-vs-legacy.md)（不变量 167）。

mempool 策略可以比共识更严。  
但「我本地解析失败」不能自动等于「全网共识非法」，除非规范就是这么写。这是反模式库会收的一条。

---

## E. 最小案例

对象：整数 1。

- 节点 A 接受 `0x01` 和 `0x0001`
- 节点 B 只接受 `0x01`

攻击者广播带 `0x0001` 的交易。A 出块，B 拒绝。分叉。

或者：同一 ECDSA 签名有两个合法 s。交易 ID 变了，但脚本仍能过。依赖 txid 的协议（旧式未确认找零、闪电网络早期）会被坑。这是 Bitcoin malleability 的工程故事。

---

## F. 真实项目

- **Bitcoin（事实）**：BIP-66 严格 DER。ECDSA 验得过不是已经是严格 DER。库接受某种变形不是共识已经接受。精读：[`../../tracks/implementation/worked-example-valid-vs-der.md`](../../tracks/implementation/worked-example-valid-vs-der.md)（不变量 172）。SegWit 把见证数据和 txid 计算分开。  
- **Ethereum（事实）**：RLP 必须规范；非规范 RLP 应拒绝。Yellow Paper / 客户端实现对此敏感。  
- **「不确定」（建议）**：选一种现成编码（例如规范的 protobuf / 明确的 length-prefix），写测试：随机加前导零、换字段序、复制签名，必须稳定拒绝。

---

## G. 源码入口（预告）

1. `decode` 是否拒绝非规范
2. 先哈希再解码，还是先解码再重编码再比
3. fuzz：任意字节进解码器，不得崩溃，也不得「修一修再当合法」

---

## H. 攻击者视角

1. 专门找「客户端 A 收、B 拒」的字节。
2. 用非规范编码做同一笔钱的两个 txid。
3. 把解析器当 DoS 武器（嵌套炸弹、超大整数）。
4. 把错误信息写进状态，让两个实现拼出不同字符串。

---

## I. Trade-off

| 选择 | 得到 | 失去 |
|---|---|---|
| 极严的唯一编码 | 难分裂 | 旧数据/旧钱包迁移痛 |
| 宽松解析 | 兼容烂实现 | 共识定时炸弹 |
| 共识宽、mempool 严 | 节点可自卫 | 用户会把「进不了池」当成「链拒绝」 |

---

## J. 对「不确定」的意义

后量子签名字节更长、结构更怪，解析器更容易被灌爆。  
**建议：** 编码规范与验签限额（每笔、每块、每连接）一起写，不要等主网上了再补。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | 编码本身不是签；签的是规范化后的字节 |
| 协议 | 同一语义只允许一种字节串 |
| 实现 | 接受非规范 = 分裂或可变哈希 |
| 部署 | 解析器被灌爆是 DoS，不是「JSON 更方便」 |
| 经济 | 裂链后跟错根放货 |

**禁止假学习：** 「JSON 也能当共识编码。」「带了类型号 = 已经解开内层。」「旧式列表 = 已经是信封。」「2718 = 1559。」「库验过 = 共识已收。」「策略已经要 DER = 共识已经要。」「66 = 62。」「看见地址 = 已经有 UTXO。」「校验过 = 程序已经上链。」「173 = 141。」「看见 PSBT = 已经能广播。」「有签 = 已经凑齐。」「174 = 173。」「后继校验过了 = 已经是 173。」「更高版本过了旧校验 = 已经合法。」「350 = 173。」「看见 xpub = 已经能花。」「能推子钥 = 已经是地址。」「32 = 174。」「看见词 = 已经是种子。」「39 = 32。」「口令错 = 已经非法。」「有钥 = 已经知道脚本。」「看见描述符 = 已经是地址。」「380 = 39。」「看见 v2 = 已经是旧包。」「能加栏 = 已经能广播。」「370 = 174。」「dummy 不是空 = 已经合法。」「隔离见证开了 = 已经没有 dummy 延展。」「策略已经要空 dummy = 共识已经要。」「147 = 66。」「看见 BIP32 compatible = 已经能互操作。」「看见自称 BIPxx compatible = 已经是那份结构。」「看见同一套扩展钥前缀 = 已经是比特币专用。」「看见同一份种子 = 已经是同一条币。」「看见下一个账户号 = 已经有过往。」「看见余额为零 = 已经发现完。」「看见同一套 BIP44 账户 = 已经能找回嵌套隔离见证。」「看见专用账户 = 已经向后兼容。」「看见账户出现了 = 已经不用核余额。」「看见现有多签派生习惯 = 已经要搬家。」「看见脚本类型层 = 已经是账户层。」「看见本页多签 = 已经不排序。」  
**边界：** 具体编解码以各链规范为准。见反模式 noncanonical-accepted。精读：[`../../tracks/implementation/worked-example-encoding.md`](../../tracks/implementation/worked-example-encoding.md)。类型信封 ≠ 已经解开内层：[`../../tracks/implementation/worked-example-typed-vs-legacy.md`](../../tracks/implementation/worked-example-typed-vs-legacy.md)（不变量 167）。ECDSA 验得过 ≠ 已经是严格 DER：[`../../tracks/implementation/worked-example-valid-vs-der.md`](../../tracks/implementation/worked-example-valid-vs-der.md)（不变量 172）。看见 Bech32 地址串 ≠ 链上已经有这笔输出：[`../../tracks/implementation/worked-example-address-vs-utxo.md`](../../tracks/implementation/worked-example-address-vs-utxo.md)（不变量 174）。看见部分签名包 ≠ 已经是网上能广播的完整交易：[`../../tracks/implementation/worked-example-psbt-vs-broadcast.md`](../../tracks/implementation/worked-example-psbt-vs-broadcast.md)（不变量 179）。后继校验过了 ≠ 已经是旧校验那套地址：[`../../tracks/implementation/worked-example-bech32m-vs-bech32.md`](../../tracks/implementation/worked-example-bech32m-vs-bech32.md)（不变量 181）。看见扩展公钥 ≠ 已经能花：[`../../tracks/implementation/worked-example-xpub-vs-spendable.md`](../../tracks/implementation/worked-example-xpub-vs-spendable.md)（不变量 182）。看见助记词 ≠ 已经是二进制种子：[`../../tracks/implementation/worked-example-mnemonic-vs-seed.md`](../../tracks/implementation/worked-example-mnemonic-vs-seed.md)（不变量 183）。看见私钥或助记词备份 ≠ 已经知道该看哪种输出脚本：[`../../tracks/implementation/worked-example-descriptor-vs-keys.md`](../../tracks/implementation/worked-example-descriptor-vs-keys.md)（不变量 184）。看见后继版本工作包 ≠ 已经是旧版那份固定未签交易：[`../../tracks/implementation/worked-example-psbtv2-vs-v0.md`](../../tracks/implementation/worked-example-psbtv2-vs-v0.md)（不变量 186）。外层交易上限不是内层解码已有界：[`../../tracks/failure-museum/asa-2024-0012.md`](../../tracks/failure-museum/asa-2024-0012.md)。Int/Dec 位宽对不齐不是已对齐：[`../../tracks/failure-museum/asa-2024-010.md`](../../tracks/failure-museum/asa-2024-010.md)。跨链 ack JSON 不是已经确定：[`../../tracks/failure-museum/isa-2025-001.md`](../../tracks/failure-museum/isa-2025-001.md)。不抄类型取值范围。不写怎样跨类型复用签名。不抄 DER 长度。不写怎样改编码。不抄字符表 / 例地址。不写怎样增删字符撞合法地址。看见多余栈元素 ≠ 已经随便填；看见隔离见证 ≠ 已经没有这条延展；看见转发策略已经要空 dummy ≠ 已经是共识：[`../../tracks/implementation/worked-example-dummy-vs-empty.md`](../../tracks/implementation/worked-example-dummy-vs-empty.md)（不变量 264）。不要抄激活时间。不要写怎样改 dummy 撞身份。看见 BIP32 compatible ≠ 已经能互操作；看见自称 BIPxx compatible ≠ 已经是那份结构：[`../../tracks/implementation/worked-example-purpose-vs-compatible.md`](../../tracks/implementation/worked-example-purpose-vs-compatible.md)（不变量 266）。不要抄用途号取值或例路径。不要写怎样选用途号或从种子扫账户。看见同一份种子 ≠ 已经是同一条币；看见余额为零 ≠ 已经发现完：[`../../tracks/implementation/worked-example-account-vs-discovered.md`](../../tracks/implementation/worked-example-account-vs-discovered.md)（不变量 267）。不要抄用途号或间隙条数。不要写怎样扫间隙或枚举账户。看见同一套 BIP44 账户 ≠ 已经能找回嵌套隔离见证；看见账户出现了 ≠ 已经不用核余额：[`../../tracks/implementation/worked-example-nested-vs-same-account.md`](../../tracks/implementation/worked-example-nested-vs-same-account.md)（不变量 268）。不要抄用途号或脚本套法。不要写怎样套脚本或从种子扫嵌套地址。看见现有多签派生习惯 ≠ 已经要搬家；看见脚本类型层 ≠ 已经是账户层：[`../../tracks/implementation/worked-example-script-type-vs-account.md`](../../tracks/implementation/worked-example-script-type-vs-account.md)（不变量 269）。不要抄脚本类型取值或例路径。不要写怎样排序公钥或从种子扫多签。看见同一套钥 ≠ 已经是同一条 P2SH 地址；看见未压缩钥 ≠ 已经是本页：[`../../tracks/implementation/worked-example-sorted-vs-one-address.md`](../../tracks/implementation/worked-example-sorted-vs-one-address.md)（不变量 270）。不要抄压缩钥例、地址例、脚本十六进制。不要写怎样按字节字典序排公钥。看见共享主公钥 ≠ 已经是本页；看见前面分支没有交易 ≠ 已经发现完：[`../../tracks/implementation/worked-example-cosigner-vs-discovered.md`](../../tracks/implementation/worked-example-cosigner-vs-discovered.md)（不变量 271）。不要抄用途号或间隙条数。不要写怎样按用途公钥排下标或从种子扫每一支。看见派生钥 ≠ 已经是输出钥；看见不需要脚本路径 ≠ 已经不承诺：[`../../tracks/implementation/worked-example-derived-vs-output-key.md`](../../tracks/implementation/worked-example-derived-vs-output-key.md)（不变量 272）。不要抄用途号或地址例。不要写怎样算标签微调。看见付款码 ≠ 已经是存款地址；看见通知输出 ≠ 已经能花：[`../../tracks/lifecycle/worked-example-payment-code-vs-notification.md`](../../tracks/lifecycle/worked-example-payment-code-vs-notification.md)（不变量 273）。不要抄用途号或编码版本字节。不要写怎样做 ECDH 或怎样拼通知。看见 multi ≠ 已经按字典序排；看见门限和钥数 ≠ 已经同一套上限：[`../../tracks/implementation/worked-example-multi-vs-sortedmulti.md`](../../tracks/implementation/worked-example-multi-vs-sortedmulti.md)（不变量 274）。不要抄函数名单或脚本模板。不要写怎样按字节排公钥。看见 tr 没有树 ≠ 已经有脚本路径；看见树表达式 ≠ 已经是旧脚本套法：[`../../tracks/implementation/worked-example-tr-vs-tree.md`](../../tracks/implementation/worked-example-tr-vs-tree.md)（不变量 275）。不要抄树花括号或微调公式。不要写怎样把压缩钥抬成 x-only。看见 pk ≠ 已经和 pkh / sh 同一套放置；看见 sh 产出 ≠ 已经有赎回脚本：[`../../tracks/implementation/worked-example-pk-vs-toplevel.md`](../../tracks/implementation/worked-example-pk-vs-toplevel.md)（不变量 276）。不要抄脚本模板或测试向量。不要写怎样拼 P2PK。看见 wpkh / wsh ≠ 已经只能顶层；看见未压缩钥 ≠ 已经允许：[`../../tracks/implementation/worked-example-wpkh-vs-compressed.md`](../../tracks/implementation/worked-example-wpkh-vs-compressed.md)（不变量 277）。不要抄脚本模板或测试向量。不要写怎样拼见证程序。看见 multi_a ≠ 已经是 383 那种 multi；看见门限 ≠ 已经同一套编码：[`../../tracks/implementation/worked-example-multia-vs-tr.md`](../../tracks/implementation/worked-example-multia-vs-tr.md)（不变量 278）。不要抄脚本模板或测试向量。不要写怎样按 x-only 排公钥。看见旧 PSBT 栏 ≠ 已经能装 Taproot；看见输出脚本里的钥 ≠ 已经是内部钥：[`../../tracks/implementation/worked-example-tap-psbt-vs-old.md`](../../tracks/implementation/worked-example-tap-psbt-vs-old.md)（不变量 279）。不要抄类型号或测试向量。不要写怎样拼控制块。看见钱包策略 ≠ 已经是一条描述符；看见钥占位 ≠ 已经是那把精确公钥：[`../../tracks/implementation/worked-example-policy-vs-descriptor.md`](../../tracks/implementation/worked-example-policy-vs-descriptor.md)（不变量 280）。看见 combo ≠ 已经只能产出一种脚本；看见未压缩钥 ≠ 已经带齐见证对：[`../../tracks/implementation/worked-example-combo-vs-one-script.md`](../../tracks/implementation/worked-example-combo-vs-one-script.md)（不变量 281）。看见 raw ≠ 已经能套进具名表达式；看见 addr ≠ 已经是那份输出脚本：[`../../tracks/implementation/worked-example-raw-vs-named.md`](../../tracks/implementation/worked-example-raw-vs-named.md)（不变量 282）。看见 MuSig2 聚合钥 ≠ 已经是扩展公钥；看见合成扩展公钥 ≠ 已经能硬化派生：[`../../tracks/implementation/worked-example-musig-xpub-vs-aggregate.md`](../../tracks/implementation/worked-example-musig-xpub-vs-aggregate.md)（不变量 283）。看见旧 PSBT 栏 ≠ 已经能装 MuSig2；看见聚合钥栏 ≠ 已经是输出钥：[`../../tracks/implementation/worked-example-musig-psbt-vs-tap.md`](../../tracks/implementation/worked-example-musig-psbt-vs-tap.md)（不变量 284）。不要抄占位写法或测试向量。不要写怎样编译占位。不要写怎样拼那几份输出脚本。不要写怎样把地址解成脚本。不要写怎样算派生微调。不要写怎样造 nonce 或部分签。
