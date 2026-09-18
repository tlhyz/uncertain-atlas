# L0.7 一笔转账的完整生命周期

优先级：必学  
先修：L0.3–L0.6

---

## A. 先修知识

你已经有：授权、交易、区块、共识问题。  
本课把它们串成一条不能跳步的路径。

---

## B. 核心问题

**用户点下「发送」之后，到「可以不可逆地认为钱到了」，中间到底经过哪些门？每扇门失败长什么样？**

---

## C. 直觉（ELI15）

把一次转账想成寄一封必须被全市档案馆收录的挂号信：

1. 你在家里写好并盖章（钱包构造、签名）
2. 交给街上的邮筒（RPC 节点）
3. 邮差口袋里还有别人的信（mempool）
4. 当天的档案员抽一批装订成册（出块）
5. 全市档案员按同一规则抄写（执行 / Apply）
6. 抄写结果落进他们的柜子（存储）
7. 过了该市规定的「不得再撕页」期限（最终性）

任何一步失败，用户都可能看见一种「没成功」，但原因完全不同。  
把它们说成同一种「失败」，以后你自己都修不了「不确定」。

---

## D. 正式定义：一笔支付的门

下面是一条**教学用**的通用路径。真实项目会改名字，但门还在。

```text
钱包构造
  → 本地预检查（可选，不可信）
  → 签名
  → 提交到某 RPC
  → 进入部分节点的 mempool（策略性）
  → 被某个出块者选入某块
  → 共识把该块变成当前历史的候选或已提交值
  → 执行 Apply，更新状态
  → 原子地写入存储
  → 对等节点同步、验证、复执行
  → 最终性规则满足
  → 收款方轻节点或全节点独立验证
```

协议工程师会把用户错觉钉死：

| 用户看见 | 实际最多只说明 |
|---|---|
| 「广播成功」 | 某个 RPC 收下了字节 |
| 「pending」 | 至少一处 mempool 记得它 |
| 「1 confirmation」 | 某条当前历史里有它；可能被重组掉 |
| 「final」 | 按该链规则，诚实节点不应再选冲突历史 |

**事实：** 收款安全取决于收款方自己的验证假设（全节点、轻节点、托管交易所），不是付款方截图。

---

## E. 最小案例

阿安向阿比转 4 个币。跟踪失败模式：

| 步骤 | 失败 | 链上状态变了吗 |
|---|---|---|
| 构造错地址 | 钱若仍被签出，可能转进黑洞 | 一旦入块，变了 |
| 签名错 | 各节点拒绝 | 没变 |
| RPC 撒谎「我已转发」 | 阿安以为发出去了 | 没变 |
| mempool 驱逐 / 费太低 | 一直 pending | 没变 |
| 进了块 A，重组到块 B | 曾经变过，又被扳回去 | 取决于你看到哪条历史 |
| 执行时余额不足 | 交易无效（或某些系统设计为失败交易仍占 nonce） | 看协议 |
| 节点写库写到一半断电 | 实现必须能恢复到「整块有或整块无」 | 不允许半块状态 |
| 阿比只看付款方截图 | 阿比被骗 | 与账本无关 |

最小三节点演示：

```text
Wallet --tx--> N1 mempool
N1 出 Block H=9 含该 tx
N2、N3 下载、验签、Apply
三份状态根一致  → 复制成功
若该协议在 H=9 收集到合法 commit → 最终
```

---

## F. 真实项目

- **Bitcoin（事实）**：确认数是重组风险的经验代理，不是数学上的 commit。交易所常等多个确认，是经济+概率判断。
- **CometBFT 应用链（事实）**：commit 后该高度不应再换。用户仍可能连到一个落后或作恶的 RPC。
- **Ethereum（事实）**：有 head、justified、finalized 等不同「看起来确定」的等级。钱包若只显示 head，语义偏乐观。
- **「不确定」（建议）**：产品文案必须把 pending / committed / finalized 分开。这是安全特性，不是 UI 细节。

---

## G. 源码

以后按门找，而不是从仓库根目录瞎逛：

1. 钱包：序列化 + 签名
2. RPC：提交接口
3. mempool：准入 / 替换 / 驱逐
4. 出块：如何选交易
5. 共识：如何提交块
6. 执行：Apply
7. 存储：原子提交
8. 同步：别人如何跟上

Level 0 只要求你能按这个清单提问。

---

## H. 攻击者视角

1. 控制 RPC，对付款人显示假 pending，对收款人显示假到账。
2. 在最终性之前施压收款人发货。
3. 用替换交易（RBF）或更高费，把商家以为会确认的那笔挤掉。
4. 分区期间让两边看见不同 pending。

---

## I. Trade-off

确认快，通常意味着：

- 更弱的最终性，或
- 更小的去中心化集合，或
- 更强的同步假设，或
- 用户被教导接受「假最终」

没有「又全球无人值守、又 100ms 不可逆、又手机轻节点零假设」的组合。

---

## J. 对「不确定」的意义

后量子结算如果不能向收款人讲清「何时可以放货」，签名再现代也只是更贵的支票。

把生命周期画成你们自己的图，是 Level 0 结束后最值得做的一张图。

---

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | 钱包签名这一步；后面绿勾不证明签仍有效于最终块 |
| 协议 | 每扇门对应不同对象：有效 / 入池 / 入块 / 执行 / 最终 |
| 实现 | RPC / 钱包把「入池」画成「到了」是产品层撒谎 |
| 部署 | 你连的节点、日蚀、分区决定你看见哪条门 |
| 经济 | 费用与审查决定过门快慢，不把入池变成最终 |

**禁止假学习：** 「钱包绿勾指协议最终。」「进 mempool 就是上链。」「打开付款链接就是已验证。」「看见付款 URI 就是已经授权 / 已经付过。」「看见签过的消息就是已经能花 / 已经付过。」「看见资金证明清单就是已经齐 / 已经没花。」「看见静默付款地址就是已经有输出 / 已经付过。」「看见扫过就是已经收到。」「看见付款码就是已经是存款地址 / 已经付过。」「看见通知输出就是已经能花。」「看见可读名字就是已经该走 DNS / 已经能付。」「看见 TXT 就是已经合法。」  
**边界：** 各链细节在档案第 4 节。五列对照见 [`../../tracks/lifecycle/`](../../tracks/lifecycle/README.md)。付款 URI 远程取单 ≠ 验证：[`../../tracks/failure-museum/cve-2024-52918.md`](../../tracks/failure-museum/cve-2024-52918.md)。付款 URI 方案本身被写成已经授权是本页（不变量 255 / BIP-321），不是 55。看见签过的消息 ≠ 已经证明能控制资金；看见签过 ≠ 已经证明发过上一笔；看见资金证明清单 ≠ 已经齐 / ≠ 已经没花：[`../../tracks/lifecycle/worked-example-signed-message-vs-control.md`](../../tracks/lifecycle/worked-example-signed-message-vs-control.md)（不变量 258）。 BIP-322 signed-message not already control / not already will-sign-spend / not already settled 正式三事（258 余量）：[`../../tracks/lifecycle/worked-example-sig322-notctrl-vs-bundled.md`](../../tracks/lifecycle/worked-example-sig322-notctrl-vs-bundled.md)（不变量 1214）。 BIP-322 invoice-control not already previous-tx / not already paid / not already settled 正式三事（258 余量）：[`../../tracks/lifecycle/worked-example-sig322-notprev-vs-bundled.md`](../../tracks/lifecycle/worked-example-sig322-notprev-vs-bundled.md)（不变量 1215）。 BIP-322 proof-list not already complete / not already unspent / not already settled 正式三事（258 余量）：[`../../tracks/lifecycle/worked-example-sig322-notfund-vs-bundled.md`](../../tracks/lifecycle/worked-example-sig322-notfund-vs-bundled.md)（不变量 1216）。不要抄编码前缀或虚拟交易字段。不要写怎样拼能过验证器的签消息。看见静默付款地址 ≠ 已经有一笔链上输出；看见扫过 ≠ 已经收到；看见同一条码再用 ≠ 已经同一笔输出：[`../../tracks/lifecycle/worked-example-silent-payment-vs-output.md`](../../tracks/lifecycle/worked-example-silent-payment-vs-output.md)（不变量 260）。 BIP-352 silent-address not already output / not already paid / not already settled 正式三事（260 余量）：[`../../tracks/lifecycle/worked-example-sil352-notout-vs-bundled.md`](../../tracks/lifecycle/worked-example-sil352-notout-vs-bundled.md)（不变量 1217）。 BIP-352 scanned not already received / not already spendable / not already settled 正式三事（260 余量）：[`../../tracks/lifecycle/worked-example-sil352-notscan-vs-bundled.md`](../../tracks/lifecycle/worked-example-sil352-notscan-vs-bundled.md)（不变量 1218）。 BIP-352 reuse not already same-output / not already linked / not already settled 正式三事（260 余量）：[`../../tracks/lifecycle/worked-example-sil352-notreuse-vs-bundled.md`](../../tracks/lifecycle/worked-example-sil352-notreuse-vs-bundled.md)（不变量 1219）。不要抄派生公式或例地址。不要写怎样扫链或派生输出。看见付款码 ≠ 已经是存款地址；看见通知输出 ≠ 已经能花；看见第一次付款 ≠ 已经不必再通知：[`../../tracks/lifecycle/worked-example-payment-code-vs-notification.md`](../../tracks/lifecycle/worked-example-payment-code-vs-notification.md)（不变量 273）。不要抄用途号或编码版本字节。不要写怎样做 ECDH 或怎样拼通知。看见可读名字 ≠ 已经该走 DNS；看见 TXT ≠ 已经是合法付款指示；看见复制了名字 ≠ 已经是 URI：[`../../tracks/lifecycle/worked-example-dns-name-vs-instruction.md`](../../tracks/lifecycle/worked-example-dns-name-vs-instruction.md)（不变量 261）。 BIP-353 readable-name not already prefer-dns / not already better / not already settled 正式三事（261 余量）：[`../../tracks/lifecycle/worked-example-dns353-notpref-vs-bundled.md`](../../tracks/lifecycle/worked-example-dns353-notpref-vs-bundled.md)（不变量 1220）。 BIP-353 txt not already legal / not already remote-verified / not already settled 正式三事（261 余量）：[`../../tracks/lifecycle/worked-example-dns353-nottxt-vs-bundled.md`](../../tracks/lifecycle/worked-example-dns353-nottxt-vs-bundled.md)（不变量 1221）。 BIP-353 cache-copy not already current-uri / not already quote-live / not already settled 正式三事（261 余量）：[`../../tracks/lifecycle/worked-example-dns353-notcache-vs-bundled.md`](../../tracks/lifecycle/worked-example-dns353-notcache-vs-bundled.md)（不变量 1222）。不要抄 DNS 标签拼法或例名。不要另写 BIP-21 当现行用户方案。不要写怎样枚举用户。看见带 pj= 的付款 URI ≠ 已经是 payjoin 付款；看见原始包 ≠ 已经是提案；看见收款方加了输入 ≠ 已经另开一笔：[`../../tracks/lifecycle/worked-example-payjoin-vs-original.md`](../../tracks/lifecycle/worked-example-payjoin-vs-original.md)（不变量 290）。 BIP-78 pj-uri not already payjoin-payment / not already original / not already settled 正式三事（290 余量）：[`../../tracks/lifecycle/worked-example-pj78-noturi-vs-bundled.md`](../../tracks/lifecycle/worked-example-pj78-noturi-vs-bundled.md)（不变量 1184）。 BIP-78 original not already proposal / not already payjoin-tx / not already settled 正式三事（290 余量）：[`../../tracks/lifecycle/worked-example-pj78-notorig-vs-bundled.md`](../../tracks/lifecycle/worked-example-pj78-notorig-vs-bundled.md)（不变量 1185）。 BIP-78 added-input not already other-tx / not already network-private / not already settled 正式三事（290 余量）：[`../../tracks/lifecycle/worked-example-pj78-notmerge-vs-bundled.md`](../../tracks/lifecycle/worked-example-pj78-notmerge-vs-bundled.md)（不变量 1186）。不要抄 HTTP 配方或加费公式。不要写怎样构造提案或怎样加费。看见储备证明交易 ≠ 已经能花；看见其余输入签过 ≠ 已经控制资金；看见 POR 栏 ≠ 已经是普通花费：[`../../tracks/lifecycle/worked-example-reserves-vs-spend.md`](../../tracks/lifecycle/worked-example-reserves-vs-spend.md)（不变量 293）。 BIP-127 por-tx not already spendable / not already confirmable / not already settled 正式三事（293 余量）：[`../../tracks/lifecycle/worked-example-por127-notspend-vs-bundled.md`](../../tracks/lifecycle/worked-example-por127-notspend-vs-bundled.md)（不变量 1196）。 BIP-127 remaining-signed not already 258-control / not already paid / not already settled 正式三事（293 余量）：[`../../tracks/lifecycle/worked-example-por127-notctrl-vs-bundled.md`](../../tracks/lifecycle/worked-example-por127-notctrl-vs-bundled.md)（不变量 1197）。 BIP-127 por-field not already ordinary-spend / not already have-prev-utxo / not already settled 正式三事（293 余量）：[`../../tracks/lifecycle/worked-example-por127-notpor-vs-bundled.md`](../../tracks/lifecycle/worked-example-por127-notpor-vs-bundled.md)（不变量 1198）。不要抄哈希前缀或栏类型号。不要写怎样造承诺输入或怎样填 POR 栏。看见本页这种签消息 ≠ 已经是 322；看见头字节标了种类 ≠ 已经有地址；看见旧 P2PKH 习惯 ≠ 已经互操作：[`../../tracks/lifecycle/worked-example-legacy-sign-vs-322.md`](../../tracks/lifecycle/worked-example-legacy-sign-vs-322.md)（不变量 294）。 BIP-137 this-sign not already 322 / not already 258-control / not already settled 正式三事（294 余量）：[`../../tracks/lifecycle/worked-example-lsig137-not322-vs-bundled.md`](../../tracks/lifecycle/worked-example-lsig137-not322-vs-bundled.md)（不变量 1199）。 BIP-137 header-byte not already have-address / not already spendable-output / not already settled 正式三事（294 余量）：[`../../tracks/lifecycle/worked-example-lsig137-notaddr-vs-bundled.md`](../../tracks/lifecycle/worked-example-lsig137-notaddr-vs-bundled.md)（不变量 1200）。 BIP-137 old-habit not already interoperable / not already old-verifiers / not already settled 正式三事（294 余量）：[`../../tracks/lifecycle/worked-example-lsig137-nothabit-vs-bundled.md`](../../tracks/lifecycle/worked-example-lsig137-nothabit-vs-bundled.md)（不变量 1201）。不要抄头字节取值或示例代码。不要写怎样从头字节还原公钥。看见付款请求 ≠ 已经授权；看见付款报文 ≠ 已经是回执；看见回执 ≠ 已经最终：[`../../tracks/lifecycle/worked-example-request-vs-ack.md`](../../tracks/lifecycle/worked-example-request-vs-ack.md)（不变量 295）。 BIP-70 payment-request not already authorized / not already that-address / not already settled 正式三事（295 余量）：[`../../tracks/lifecycle/worked-example-pay70-notauth-vs-bundled.md`](../../tracks/lifecycle/worked-example-pay70-notauth-vs-bundled.md)（不变量 1202）。 BIP-70 payment-message not already ack / not already merchant-accepted / not already settled 正式三事（295 余量）：[`../../tracks/lifecycle/worked-example-pay70-notack-vs-bundled.md`](../../tracks/lifecycle/worked-example-pay70-notack-vs-bundled.md)（不变量 1203）。 BIP-70 ack not already final / not already confirmed / not already refunded 正式三事（295 余量）：[`../../tracks/lifecycle/worked-example-pay70-notfinal-vs-bundled.md`](../../tracks/lifecycle/worked-example-pay70-notfinal-vs-bundled.md)（不变量 1204）。 BIP-321 uri not already authorized / not already paid / not already settled 正式三事（255 余量）：[`../../tracks/lifecycle/worked-example-uri321-notauth-vs-bundled.md`](../../tracks/lifecycle/worked-example-uri321-notauth-vs-bundled.md)（不变量 1211）。 BIP-321 empty-path not already no-instruction / not already only-one / not already settled 正式三事（255 余量）：[`../../tracks/lifecycle/worked-example-uri321-notempty-vs-bundled.md`](../../tracks/lifecycle/worked-example-uri321-notempty-vs-bundled.md)（不变量 1212）。 BIP-321 required-param not already payable / not already confirmed / not already settled 正式三事（255 余量）：[`../../tracks/lifecycle/worked-example-uri321-notreq-vs-bundled.md`](../../tracks/lifecycle/worked-example-uri321-notreq-vs-bundled.md)（不变量 1213）。不要抄消息编码或传输头。不要写怎样拼付款请求或怎样验证书链。不要另写 BIP-71 / BIP-72。

---

试题已集中到 [`../../exams/level-00.md`](../../exams/level-00.md)。本课正文不再穿插出题。
