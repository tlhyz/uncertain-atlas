# Bitcoin · 19 节档案（第一版）

资料优先级提醒：白皮书、BIPs、Bitcoin Core、CVE/postmortem 高于任何交易所博客。  
未核对到当前文件名的源码路径标「预告，Level 3 深挖时对照仓库」。

---

## 1. 一句话定义

用 **UTXO 状态** 和 **PoW 最重链规则**，让不认识的节点对「哪些输出已花」达成可独立复验的历史。最终性是概率的，不是委员会 commit。

禁止的句子：「数字黄金」「最快最安全」。

---

## 2. 它解决的问题

上一代电子现金的病：必须有柜员防双花，柜员可以审查、停机、造币。

Bitcoin 的问题陈述（事实，白皮书 2008）：点对点电子现金，用时间戳服务器 + 工作量证明，不靠单一柜员决定花费顺序。

它故意不解决：通用合约平台、秒级确定最终性、隐私默认、低能耗。

---

## 3. 架构图

```text
钱包  →  P2P 广播
           ↓
        mempool（各节点本地策略）
           ↓
        矿工组装候选块 + PoW
           ↓
        块在 P2P 传播（可 compact block）
           ↓
        全节点：验头、验 Merkle、验脚本、更新 UTXO
           ↓
        最重链选择  →  概率最终
           ↓
        磁盘：区块文件 + UTXO 集（chainstate）
```

没有独立的「共识客户端 / 执行客户端」拆分。一台 Bitcoin Core 默认全做。

---

## 4. 一笔交易完整生命周期

1. 钱包选币（哪些 UTXO）、构造输出（收款+找零）、算费、签名。看见部分签名包不是已经是网上能广播的完整交易；里面有几张签不是这一输入已经凑齐：[`../../tracks/implementation/worked-example-psbt-vs-broadcast.md`](../../tracks/implementation/worked-example-psbt-vs-broadcast.md)（不变量 179）。看见扩展公钥不是已经能花；能推子钥不是已经是地址：[`../../tracks/implementation/worked-example-xpub-vs-spendable.md`](../../tracks/implementation/worked-example-xpub-vs-spendable.md)（不变量 182）。看见 BIP32 compatible 不是已经能互操作；看见自称 BIPxx compatible 不是已经是那份结构：[`../../tracks/implementation/worked-example-purpose-vs-compatible.md`](../../tracks/implementation/worked-example-purpose-vs-compatible.md)（不变量 266）。看见同一份种子不是已经是同一条币；看见余额为零不是已经发现完：[`../../tracks/implementation/worked-example-account-vs-discovered.md`](../../tracks/implementation/worked-example-account-vs-discovered.md)（不变量 267）。看见同一套 BIP44 账户不是已经能找回嵌套隔离见证；看见账户出现了不是已经不用核余额：[`../../tracks/implementation/worked-example-nested-vs-same-account.md`](../../tracks/implementation/worked-example-nested-vs-same-account.md)（不变量 268）。看见现有多签派生习惯不是已经要搬家；看见脚本类型层不是已经是账户层：[`../../tracks/implementation/worked-example-script-type-vs-account.md`](../../tracks/implementation/worked-example-script-type-vs-account.md)（不变量 269）。看见同一套钥不是已经是同一条 P2SH 地址；看见未压缩钥不是已经是本页：[`../../tracks/implementation/worked-example-sorted-vs-one-address.md`](../../tracks/implementation/worked-example-sorted-vs-one-address.md)（不变量 270）。看见共享主公钥不是已经是本页；看见前面分支没有交易不是已经发现完：[`../../tracks/implementation/worked-example-cosigner-vs-discovered.md`](../../tracks/implementation/worked-example-cosigner-vs-discovered.md)（不变量 271）。看见派生钥不是已经是输出钥；看见不需要脚本路径不是已经不承诺：[`../../tracks/implementation/worked-example-derived-vs-output-key.md`](../../tracks/implementation/worked-example-derived-vs-output-key.md)（不变量 272）。看见付款码不是已经是存款地址；看见通知输出不是已经能花：[`../../tracks/lifecycle/worked-example-payment-code-vs-notification.md`](../../tracks/lifecycle/worked-example-payment-code-vs-notification.md)（不变量 273）。看见 multi 不是已经按字典序排；看见门限和钥数不是已经同一套上限：[`../../tracks/implementation/worked-example-multi-vs-sortedmulti.md`](../../tracks/implementation/worked-example-multi-vs-sortedmulti.md)（不变量 274）。看见 tr 没有树不是已经有脚本路径；看见树表达式不是已经是旧脚本套法；看见压缩钥不是已经是 x-only：[`../../tracks/implementation/worked-example-tr-vs-tree.md`](../../tracks/implementation/worked-example-tr-vs-tree.md)（不变量 275）。看见 pk 不是已经和 pkh / sh 同一套放置；看见 sh 产出不是已经有赎回脚本；看见熟悉的标准脚本不是已经能互操作：[`../../tracks/implementation/worked-example-pk-vs-toplevel.md`](../../tracks/implementation/worked-example-pk-vs-toplevel.md)（不变量 276）。看见 wpkh / wsh 不是已经只能顶层；看见未压缩钥不是已经允许；看见 wsh 产出不是已经有见证脚本：[`../../tracks/implementation/worked-example-wpkh-vs-compressed.md`](../../tracks/implementation/worked-example-wpkh-vs-compressed.md)（不变量 277）。看见 multi_a 不是已经是 383 那种 multi；看见门限不是已经同一套编码；看见 sortedmulti_a 不是已经是 383 那种排序：[`../../tracks/implementation/worked-example-multia-vs-tr.md`](../../tracks/implementation/worked-example-multia-vs-tr.md)（不变量 278）。看见旧 PSBT 栏不是已经能装 Taproot；看见输出脚本里的钥不是已经是内部钥；看见 Taproot 输入不是已经必须带整笔前交易：[`../../tracks/implementation/worked-example-tap-psbt-vs-old.md`](../../tracks/implementation/worked-example-tap-psbt-vs-old.md)（不变量 279）。看见钱包策略不是已经是一条描述符；看见钥占位不是已经是那把精确公钥；看见登记过不是已经批准这笔花：[`../../tracks/implementation/worked-example-policy-vs-descriptor.md`](../../tracks/implementation/worked-example-policy-vs-descriptor.md)（不变量 280）。看见 combo 不是已经只能产出一种脚本；看见未压缩钥不是已经带齐见证对：[`../../tracks/implementation/worked-example-combo-vs-one-script.md`](../../tracks/implementation/worked-example-combo-vs-one-script.md)（不变量 281）。看见 raw 不是已经能套进具名表达式；看见 addr 不是已经是那份输出脚本：[`../../tracks/implementation/worked-example-raw-vs-named.md`](../../tracks/implementation/worked-example-raw-vs-named.md)（不变量 282）。看见 MuSig2 聚合钥不是已经是扩展公钥；看见合成扩展公钥不是已经能硬化派生：[`../../tracks/implementation/worked-example-musig-xpub-vs-aggregate.md`](../../tracks/implementation/worked-example-musig-xpub-vs-aggregate.md)（不变量 283）。看见旧 PSBT 栏不是已经能装 MuSig2；看见聚合钥栏不是已经是输出钥：[`../../tracks/implementation/worked-example-musig-psbt-vs-tap.md`](../../tracks/implementation/worked-example-musig-psbt-vs-tap.md)（不变量 284）。看见脚本各走各的路径不是已经是多签该有的树；看见路径里的脚本类型不是已经必要：[`../../tracks/implementation/worked-example-multisig-path-vs-script.md`](../../tracks/implementation/worked-example-multisig-path-vs-script.md)（不变量 285）。看见一份助记词不是已经能备齐所有钱包；看见扩展根钥不是已经能倒回助记词：[`../../tracks/implementation/worked-example-entropy-vs-seed.md`](../../tracks/implementation/worked-example-entropy-vs-seed.md)（不变量 286）。看见部分签名包不是已经是跨厂安全多签开户；看见指纹对上不是已经核过 KEY；看见 TOKEN 不是已经是钱包种子：[`../../tracks/implementation/worked-example-setup-vs-psbt.md`](../../tracks/implementation/worked-example-setup-vs-psbt.md)（不变量 287）。看见一条派生路径不是已经是一份路径模板；看见写死了熟路径检查不是已经能互操作；看见完整模板不是已经是半截模板：[`../../tracks/implementation/worked-example-template-vs-path.md`](../../tracks/implementation/worked-example-template-vs-path.md)（不变量 288）。看见共享了扩展公钥不是已经是链码委托；看见委托方那把非扩展钥不是已经能推出整棵钱包；看见这一输入的微调不是已经是盲签：[`../../tracks/implementation/worked-example-delegation-vs-xpub.md`](../../tracks/implementation/worked-example-delegation-vs-xpub.md)（不变量 289）。看见带 pj= 的付款 URI 不是已经是 payjoin 付款；看见原始包不是已经是提案；看见收款方加了输入不是已经另开一笔：[`../../tracks/lifecycle/worked-example-payjoin-vs-original.md`](../../tracks/lifecycle/worked-example-payjoin-vs-original.md)（不变量 290）。看见自家习惯的输入输出顺序不是已经是字典序标准；看见按字典序排了不是已经是共识；看见按字典序排了不是已经私人：[`../../tracks/implementation/worked-example-order-vs-lex.md`](../../tracks/implementation/worked-example-order-vs-lex.md)（不变量 291）。看见助记词不是已经是二进制种子；用户自造句子不是已经是本页那种助记词：[`../../tracks/implementation/worked-example-mnemonic-vs-seed.md`](../../tracks/implementation/worked-example-mnemonic-vs-seed.md)（不变量 183）。看见私钥或助记词备份不是已经知道该看哪种输出脚本；看见描述符不是已经是地址：[`../../tracks/implementation/worked-example-descriptor-vs-keys.md`](../../tracks/implementation/worked-example-descriptor-vs-keys.md)（不变量 184）。看见后继版本工作包不是已经是旧版那份固定未签交易；能再加输入输出不是已经能广播：[`../../tracks/implementation/worked-example-psbtv2-vs-v0.md`](../../tracks/implementation/worked-example-psbtv2-vs-v0.md)（不变量 186）。看见付款 URI 不是已经授权，也不是已经付了；看见路径没有链上地址不是已经没有付款指示；看见不认识的必选参数不是已经能付：[`../../tracks/lifecycle/worked-example-uri-vs-authorized.md`](../../tracks/lifecycle/worked-example-uri-vs-authorized.md)（不变量 255）。看见签过的消息不是已经证明能控制资金；看见签过不是已经证明发过上一笔；看见资金证明清单不是已经齐：[`../../tracks/lifecycle/worked-example-signed-message-vs-control.md`](../../tracks/lifecycle/worked-example-signed-message-vs-control.md)（不变量 258）。看见静默付款地址不是已经有一笔链上输出；看见扫过不是已经收到；看见同一条码再用不是已经同一笔输出：[`../../tracks/lifecycle/worked-example-silent-payment-vs-output.md`](../../tracks/lifecycle/worked-example-silent-payment-vs-output.md)（不变量 260）。看见可读名字不是已经该走 DNS；看见 TXT 不是已经是合法付款指示；看见复制了名字不是已经是 URI：[`../../tracks/lifecycle/worked-example-dns-name-vs-instruction.md`](../../tracks/lifecycle/worked-example-dns-name-vs-instruction.md)（不变量 261）。  
2. 广播到若干对等节点。  
3. 节点按本地策略决定是否进 mempool（脚本、费、标准性）。标准性 ≠ 共识合法性。策略不作用于块内交易：[`../../tracks/mempool/worked-example-policy-vs-consensus.md`](../../tracks/mempool/worked-example-policy-vs-consensus.md)（不变量 144）。选择加入替换信号不是已经换掉；nSequence 示意不是已经是相对锁；钱包看见未确认不是已经当付款：[`../../tracks/mempool/worked-example-rbf-signal-vs-replaced.md`](../../tracks/mempool/worked-example-rbf-signal-vs-replaced.md)（不变量 166）。看见跳过库存通告不是已经拒进池；看见发了费率过滤器不是对等节点已经照做；看见布隆过了不是已经过了费率门：[`../../tracks/mempool/worked-example-feefilter-vs-rejected.md`](../../tracks/mempool/worked-example-feefilter-vs-rejected.md)（不变量 245）。看见内存池查询回了一串库存不是已经有那些交易；看见只肯给最近转发过的不是已经支持整池查询；看见协议版本够了不是已经在答：[`../../tracks/mempool/worked-example-mempool-dump-vs-have.md`](../../tracks/mempool/worked-example-mempool-dump-vs-have.md)（不变量 253）。看见拒收消息不是已经共识非法；看见调试理由不是已经该给用户看；看见没拒收不是已经是当前最好链：[`../../tracks/network/worked-example-reject-vs-consensus.md`](../../tracks/network/worked-example-reject-vs-consensus.md)（不变量 254）。  
4. 矿工从 mempool 选交易，算 Merkle 根，找 nonce 使头哈希低于目标。头上的 Merkle 用各笔 txid；新规则另要 coinbase 承诺 wtxid 根：[`../../tracks/implementation/worked-example-txid-vs-wtxid.md`](../../tracks/implementation/worked-example-txid-vs-wtxid.md)（不变量 152）。  
5. 新块传播。节点验证：PoW、时间戳窗口、交易列表、脚本、无双花。旧节点看见 txid 不是已经验过见证。  
6. `ConnectBlock`：花输入、造输出，写 UTXO。coinbase 输出进了 UTXO 集，仍不能马上当输入：[`../../tracks/economic/worked-example-coinbase-vs-mature.md`](../../tracks/economic/worked-example-coinbase-vs-mature.md)（不变量 163）。coinbase 第一项写了高度不是头上已经有高度字段：[`../../tracks/implementation/worked-example-coinbase-height-vs-header.md`](../../tracks/implementation/worked-example-coinbase-height-vs-header.md)（不变量 173）。同一交易标识不是已经唯一，也不是已经同一组可花输出：[`../../tracks/consensus/worked-example-duplicate-txid-vs-unique.md`](../../tracks/consensus/worked-example-duplicate-txid-vs-unique.md)（不变量 257）。  
7. 若随后出现更重的链，可能 disconnect 再 connect（reorg）。  
8. 收款方若只看 1 个确认，仍可能被重组；交易所常用更多确认，这是经济习惯，不是协议 commit。普通确认深度也不是 coinbase 成熟窗。许多确认也不是已经不怕同一标识被覆盖（不变量 257）。

---

## 5. 状态模型

UTXO 集。见课程 L2.1。

脚本给出花费条件。P2PKH / P2WPKH / P2TR 是包装，不是另一种状态模型。看见 Bech32 地址串不是链上已经有这笔输出；校验过不是见证程序已经在链上：[`../../tracks/implementation/worked-example-address-vs-utxo.md`](../../tracks/implementation/worked-example-address-vs-utxo.md)（不变量 174）。后继校验过了不是已经是旧校验那套地址；更高版本过了旧校验不是已经合法：[`../../tracks/implementation/worked-example-bech32m-vs-bech32.md`](../../tracks/implementation/worked-example-bech32m-vs-bech32.md)（不变量 181）。脚本里的 CLTV 不是交易 nLockTime 已经把输出锁住：[`../../tracks/state-models/worked-example-cltv-vs-nlocktime.md`](../../tracks/state-models/worked-example-cltv-vs-nlocktime.md)（不变量 164）。脚本里的 CSV 不是绝对锁，也不是「CSV 部署」四个字：[`../../tracks/state-models/worked-example-csv-vs-cltv.md`](../../tracks/state-models/worked-example-csv-vs-cltv.md)（不变量 165）。付给脚本哈希不是已经揭开赎回脚本；旧节点 HASH160 EQUAL 通过不是新节点已经再跑赎回：[`../../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md`](../../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md)（不变量 170）。

---

## 6. 共识

**Nakamoto / 最重链（事实）：** 在有效链里选累计工作最多的。常见口语「最长链」在难度调整后不精确。

**PoW：** 找头哈希满足难度。假设：多数算力不合作改历史。

**最终性：** 概率。确认数越多，改写期望成本越高，不是「第 N 块后数学禁止」。许多确认也不是已经不怕同一标识被覆盖：[`../../tracks/consensus/worked-example-duplicate-txid-vs-unique.md`](../../tracks/consensus/worked-example-duplicate-txid-vs-unique.md)（不变量 257）。看见多余栈元素不是已经随便填；看见隔离见证不是已经没有这条延展；看见转发策略已经要空 dummy 不是已经是共识：[`../../tracks/implementation/worked-example-dummy-vs-empty.md`](../../tracks/implementation/worked-example-dummy-vs-empty.md)（不变量 264）。

**分叉：** 同一高度两个合法块常见于传播延迟。短分叉靠后续工作消解。

没有 Tendermint 式的锁和 +2/3 commit。

**块时间（必须拆开）：** 头不能 `<=` 父块 `GetMedianTimePast`（`time-too-old`）。CSV 软分叉部署之后交易 locktime 也看父 MTP，不看本块 `nTime`（BIP 113）。这里的「CSV」是部署名，不是 CHECKSEQUENCEVERIFY 操作码：[`../../tracks/state-models/worked-example-csv-vs-cltv.md`](../../tracks/state-models/worked-example-csv-vs-cltv.md)（不变量 165）。太新看本节点钟 + 命名宽限（`time-too-new`），不是 MTP。三把尺见 [`../../tracks/consensus/worked-example-mtp.md`](../../tracks/consensus/worked-example-mtp.md)。不要和 PBTS / BFT Time 糊。脚本里的 CLTV 比的是花费交易的 nLockTime，不是墙上现在，也不是 MTP 已经把输出锁住：[`../../tracks/state-models/worked-example-cltv-vs-nlocktime.md`](../../tracks/state-models/worked-example-cltv-vs-nlocktime.md)（不变量 164）。

---

## 7. 执行

不是虚拟机里的 gas 循环。执行 = 脚本解释 + UTXO 规则。

脚本故意非图灵完备（无一般循环），降低「无限跑」的共识风险。Taproot / Tapscript 增加了表达，仍不是 EVM。钥匙路径不是已经揭开有没有脚本树：[`../../tracks/implementation/worked-example-keypath-vs-scriptpath.md`](../../tracks/implementation/worked-example-keypath-vs-scriptpath.md)（不变量 153）。走脚本路径不是已经是 tapscript 语义：[`../../tracks/implementation/worked-example-tapscript-vs-scriptpath.md`](../../tracks/implementation/worked-example-tapscript-vs-scriptpath.md)（不变量 189）。看见 Miniscript 不是已经是链上脚本；共识健全不是已经是策略完备：[`../../tracks/implementation/worked-example-miniscript-vs-script.md`](../../tracks/implementation/worked-example-miniscript-vs-script.md)（不变量 191）。看见多余栈元素不是已经随便填；看见隔离见证不是已经没有这条延展：[`../../tracks/implementation/worked-example-dummy-vs-empty.md`](../../tracks/implementation/worked-example-dummy-vs-empty.md)（不变量 264）。

失败的脚本使该交易无效，不能进合法块（共识）。mempool 还会用更严的 standardness 拒绝「共识合法但不受欢迎」的交易。

---

## 8. 网络

无许可 P2P。地址管理、偷听、compact block（BIP152）减传播带宽。最大序列化消息长度 ≠ 读完载荷前的接收分配上限（CVE-2015-3641）。地址表递增 ID 限速 ≠ 宽度已够（CVE-2024-52919）。自动封禁表无界 + GETADDR 二次扫描（CVE-2020-14198）。UPnP 默认关是结构风险决策（CVE-2015-20111 / CVE-2024-52917）。出站 SOCKS 代理不是 P2P 对等节点（CVE-2017-18350；须先配置；明文网上的任意代理本身就可被截获）。付款 URI 远程取单不是共识验证（CVE-2024-52918；修法是删 BIP70）。看见付款 URI 不是已经授权；看见路径没有链上地址不是已经没有付款指示；看见不认识的必选参数不是已经能付：[`../../tracks/lifecycle/worked-example-uri-vs-authorized.md`](../../tracks/lifecycle/worked-example-uri-vs-authorized.md)（不变量 255；不是 55）。看见机会主义未认证加密不是已经私人；看见伪随机字节流不是已经认不出；看见仍收下第 1 版不是已经退役旧线：[`../../tracks/network/worked-example-v2-transport-vs-private.md`](../../tracks/network/worked-example-v2-transport-vs-private.md)（不变量 242）。看见客户端侧过滤器对上不是已经有块；看见过滤器头链对上不是已经写进共识；看见至少一个诚实对等节点不是已经验完脚本：[`../../tracks/light-clients/worked-example-cfilter-vs-have.md`](../../tracks/light-clients/worked-example-cfilter-vs-have.md)（不变量 243）。看见基本过滤器对上不是已经在集合里；看见装了花费脚本和收款脚本不是已经有那笔交易；看见排除了 OP_RETURN 不是已经写进共识：[`../../tracks/light-clients/worked-example-basic-filter-vs-relevant.md`](../../tracks/light-clients/worked-example-basic-filter-vs-relevant.md)（不变量 244）。看见跳过库存通告不是已经拒进池；看见发了费率过滤器不是对等节点已经照做；看见布隆过了不是已经过了费率门：[`../../tracks/mempool/worked-example-feefilter-vs-rejected.md`](../../tracks/mempool/worked-example-feefilter-vs-rejected.md)（不变量 245）。看见后继地址流言不是已经连得上；看见发了 sendaddrv2 不是已经只收后继格式；看见在传某种网上的地址不是已经连上那种网：[`../../tracks/network/worked-example-addrv2-vs-reachable.md`](../../tracks/network/worked-example-addrv2-vs-reachable.md)（不变量 246）。看见发了 sendheaders 不是已经改用头通告；看见用头通告新尖不是已经有块；看见重组时先发头不是中间块已经在手里：[`../../tracks/network/worked-example-sendheaders-vs-have.md`](../../tracks/network/worked-example-sendheaders-vs-have.md)（不变量 247）。看见按 wtxid 通告不是已经有那笔交易；看见发了 wtxidrelay 不是已经改口；看见仍用旧类型要父交易不是旧库存已经退役：[`../../tracks/network/worked-example-wtxidrelay-vs-have.md`](../../tracks/network/worked-example-wtxidrelay-vs-have.md)（不变量 248）。看见对账素描不是已经有那些交易；看见发了 sendtxrcncl 不是已经在对账；看见对账失败退回洪水不是库存通告已经退役：[`../../tracks/network/worked-example-erlay-vs-have.md`](../../tracks/network/worked-example-erlay-vs-have.md)（不变量 249）。看见有限服务位不是已经能服任意旧块；看见只保证最近窗口不是已经剪枝；看见服了最近一块不是已经暴露了剪到哪：[`../../tracks/network/worked-example-limited-service-vs-archive.md`](../../tracks/network/worked-example-limited-service-vs-archive.md)（不变量 250）。看见带见证的线上序列化不是已经有见证；看见能提供见证不是已经在传；看见库存通告仍用旧类型不是线上已经没有见证：[`../../tracks/network/worked-example-witness-wire-vs-have.md`](../../tracks/network/worked-example-witness-wire-vs-have.md)（不变量 251）。看见没开布隆服务位不是已经退役；看见开了这一位不是已经私人；看见协议版本够了不是已经在遵守：[`../../tracks/light-clients/worked-example-bloom-bit-vs-retired.md`](../../tracks/light-clients/worked-example-bloom-bit-vs-retired.md)（不变量 252）。看见内存池查询回了一串库存不是已经有那些交易；看见只肯给最近转发过的不是已经支持整池查询；看见协议版本够了不是已经在答：[`../../tracks/mempool/worked-example-mempool-dump-vs-have.md`](../../tracks/mempool/worked-example-mempool-dump-vs-have.md)（不变量 253）。看见拒收消息不是已经共识非法；看见调试理由不是已经该给用户看；看见没拒收不是已经是当前最好链：[`../../tracks/network/worked-example-reject-vs-consensus.md`](../../tracks/network/worked-example-reject-vs-consensus.md)（不变量 254）。看见版本里关掉交易转发不是已经终身只传块；看见发了停交易转发不是已经没有紧凑块；看见建议关掉地址不是已经禁止传地址：[`../../tracks/network/worked-example-disabletx-vs-lifetime.md`](../../tracks/network/worked-example-disabletx-vs-lifetime.md)（不变量 256）。看见协议版本够了不是已经支持某项功能；看见通告了 feature 不是已经启用；看见 verack 之后才来的 feature 不是已经是本页协商：[`../../tracks/network/worked-example-feature-vs-enabled.md`](../../tracks/network/worked-example-feature-vs-enabled.md)（不变量 259）。看见协议版本够了不是已经会带 nonce 的 ping；看见 pong 不是已经对上那一次 ping；看见回了 pong 不是已经还活着：[`../../tracks/network/worked-example-pong-vs-live.md`](../../tracks/network/worked-example-pong-vs-live.md)（不变量 262）。看见协议版本不是已经是客户端版本；看见 user agent 不是已经可以按实现改行为；看见同一协议版本不是已经是同一套实现：[`../../tracks/network/worked-example-ua-vs-protocol.md`](../../tracks/network/worked-example-ua-vs-protocol.md)（不变量 263）。

攻击面：eclipse（围住一个节点只给他看假图）、延迟块、向轻节点撒谎。

**事实：** 很多性能瓶颈在传播与验证，不在「脚本算得慢」。  
Sybil：身份便宜，抗 Sybil 主要靠算力成本，不是 KYC。

---

## 9. 存储

区块原始数据可剪枝（pruning）但仍要能从创世验证到尖。加速同步是**实现开关**：assumevalid 跳祖先脚本且不强迫链；assumeutxo 先装 UTXO 快照、背景再验。不是弱主观周期，也不是旧 checkpoint。见 [`../../tracks/implementation/worked-example-assumevalid.md`](../../tracks/implementation/worked-example-assumevalid.md)。

UTXO 集在 chainstate。断电必须不出现「半个块」：Bitcoin Core 用库的原子与 flush 策略。具体崩溃语义属部署/实现，Level 9 再对照源码与测试。

归档节点留全历史。剪枝节点不能给别人完整旧块。

---

## 10. 密码学 primitive

| 零件 | 用途 |
|---|---|
| SHA-256 / HASH256 | 块头、txid、Merkle。txid ≠ wtxid：[`../../tracks/implementation/worked-example-txid-vs-wtxid.md`](../../tracks/implementation/worked-example-txid-vs-wtxid.md)（不变量 152） |
| RIPEMD-160 | 地址派生（P2PKH 等） |
| ECDSA secp256k1 | 旧式花费。数学验过不是已经是严格 DER：[`../../tracks/implementation/worked-example-valid-vs-der.md`](../../tracks/implementation/worked-example-valid-vs-der.md)（不变量 172） |
| Schnorr (BIP-340) | Taproot。tagged hash 公式见 `tracks/crypto/worked-example-tagged-hash.md`；标签不是 FIPS `ctx`。钥匙路径 ≠ 揭树：[`../../tracks/implementation/worked-example-keypath-vs-scriptpath.md`](../../tracks/implementation/worked-example-keypath-vs-scriptpath.md)（不变量 153）。走脚本路径 ≠ 已经是 tapscript 语义：[`../../tracks/implementation/worked-example-tapscript-vs-scriptpath.md`](../../tracks/implementation/worked-example-tapscript-vs-scriptpath.md)（不变量 189） |
| Merkle 树 | 交易承诺、SPV |

没有 BLS，没有默认 zk。

---

## 11. 安全假设

| 假设失效 | 一起失效的保证 |
|---|---|
| 多数算力不诚实 | 重组、审查、双花未确认甚至浅确认 |
| SHA-256 抗碰撞/PoW 预图像被实质打破 | 造假块、改历史成本模型崩 |
| 椭圆曲线签名被破（含量子） | 未花费输出可被盗签 |
| 用户把 RPC/浏览器当验证 | 用户层被骗，协议层可仍健康 |
| 全节点极度稀少 | 验证文化变弱，实现/部署层变脆 |

弱主观性对 Bitcoin 不如长程 PoS 那么中心。创世与旧 checkpoint / 发行默认 assumevalid 仍是社会或实现对象，不要和 Ethereum WS 糊成一句。

---

## 12. 最大结构性优势

**可独立复验的小规则集 + 慢变更。**  
任何人可跑全节点重放。协议进化偏软分叉、偏兼容旧验证者。这与「十年还在」强相关。版本位被置上不是已经锁定；锁定不是已经激活：[`../../tracks/implementation/worked-example-versionbit-vs-active.md`](../../tracks/implementation/worked-example-versionbit-vs-active.md)（不变量 171）。

这是结构，不是市值。

---

## 13. 最大具体缺陷（对结算工程师）

1. 概率最终：深确认之前，商家必须自己承担重组风险。  
2. 吞吐与延迟受块间隔、块权重、传播约束。不是实现没写好那么简单。  
3. 脚本表达力有限；复杂应用外溢到二层。  
4. 隐私弱（链上图谱）。  
5. 挖矿与池导致权力实际集中——经济层，不是白皮书假设自动成立。

---

## 14. Trade-off

| 得到 | 用什么换 |
|---|---|
| 无许可出块、分区时仍能各自长链 | 重组、耗能或等价算力成本、概率最终 |
| 全节点可复验 | 家庭节点要跟带宽与 UTXO 增长 |
| 保守升级 | 新功能极慢 |
| 简单执行 | 不是通用世界计算机 |

---

## 15. 历史事故（抽样，须回原始出处）

| 事件 | 层 | 备注 |
|---|---|---|
| CVE-2018-17144 | 实现 | 重复输入可通胀。见 `tracks/failure-museum/cve-2018-17144.md`；五层对照 `tracks/failure-museum/worked-example-five-layers.md` |
| CVE-2010-5139 | 实现 | 输出求和溢出。见 `tracks/failure-museum/cve-2010-5139.md` |
| CVE-2012-2459 | 协议+实现 | Merkle 奇数复制 ⇒ 同根不同列表。见 `tracks/failure-museum/cve-2012-2459.md` |
| 2013 分叉 | 实现+部署 | BIP 50（BDB 锁上限）。见 `tracks/failure-museum/bip-0050-2013-fork.md` |
| transaction malleability | 协议/实现 | 促使 SegWit；结构课 L3.7。txid ≠ wtxid，不是已经修完所有身份：[`../../tracks/implementation/worked-example-txid-vs-wtxid.md`](../../tracks/implementation/worked-example-txid-vs-wtxid.md)（不变量 152） |
| CVE-2024-52912 | 实现+部署 | 调整钟绕过上限，拒收规范新块。见 `tracks/failure-museum/cve-2024-52912.md` |
| CVE-2024-52913 | 实现+网络 | 有界索取表让节点看不见未确认交易。见 `tracks/failure-museum/cve-2024-52913.md` |
| CVE-2019-25220 | 实现+部署 | 低难度头填爆内存索引；0.14 后检查点几乎只剩反垃圾。见 `tracks/failure-museum/cve-2019-25220.md`。不抄攻击成本 BTC |
| CVE-2024-52914 | 实现 | 孤儿解析二次扫描可卡住数小时。见 `tracks/failure-museum/cve-2024-52914.md` |
| CVE-2015-3641 | 实现+网络 | 最大序列化长度被当成接收分配上限。见 `tracks/failure-museum/cve-2015-3641.md` |
| CVE-2024-52919 | 实现+网络 | 地址表递增 ID 回绕；v22 限速 ≠ v29 改宽度。见 `tracks/failure-museum/cve-2024-52919.md` |
| CVE-2020-14198 | 实现+网络 | 无界封禁表 + GETADDR 二次扫描。见 `tracks/failure-museum/cve-2020-14198.md` |
| CVE-2025-46597 | 实现 | 32-bit 写盘前尺寸检查溢出；卡住 `-maxmempool` ≠ 固定宽度。见 `tracks/failure-museum/cve-2025-46597.md` |
| CVE-2015-20111 | 实现+部署 | UPnP 局域网打洞辅助；0.11.1 默认关以防库洞变结构风险。亲戚 CVE-2024-52917。见 `tracks/failure-museum/cve-2015-20111.md` |
| CVE-2017-18350 | 实现+部署 | 出站 SOCKS 代理不是 P2P 对等节点；须先配置才脆弱。见 `tracks/failure-museum/cve-2017-18350.md` |
| CVE-2024-52918 | 实现+部署 | 支付 URI 远程取单不是共识验证；修法是删 BIP70。见 `tracks/failure-museum/cve-2024-52918.md` |
| 2026-06 privatebroadcast | 实现+部署+网络 | 开关 ≠ IP 已经不暴露；v2 失败后的 v1 重连 ≠ 仍走代理。见 `tracks/failure-museum/bitcoin-2026-06-privatebroadcast-v1-retry.md` |
| 2026-01 wallet migration | 实现+部署 | 迁移失败 ≠ 目录里其它钱包已经安全；现有用户不受影响 ≠ 迁移路径已经安全。见 `tracks/failure-museum/bitcoin-2026-01-wallet-migration-delete.md` |

七问只写有 CVE / 官方披露 / BIP 原文的条目。禁止用传闻填充。

---

## 16. 源码入口（预告，对照当前 Bitcoin Core 树）

建议阅读顺序（名称以上游为准，深挖时打开仓库核对）：

1. **区块连接 / UTXO 更新** — `ConnectBlock` 所在的 validation 路径。为什么：这是 `Apply`。  
2. **最重链选择** — 链状态/工作量比较。为什么：这是 fork choice。  
3. **脚本解释** — interpreter / Taproot 验证。为什么：这是授权。

不要从 `main.cpp` 观光式从头读到尾。

---

## 17. 关键函数（逻辑级）

**`ConnectBlock`（逻辑名）**  
输入：候选块 + 当前 UTXO 视图。  
逻辑：检查头与交易、花输入、造输出、脚本。  
输出：新 UTXO 视图或拒绝。  
invariant：不引入重复花费；coinbase 成熟规则（进了块 ≠ 已经能花：[`../../tracks/economic/worked-example-coinbase-vs-mature.md`](../../tracks/economic/worked-example-coinbase-vs-mature.md)，不变量 163）；供给规则。

**`CheckTxInputs` / 脚本 VerifyScript（逻辑名）**  
输入：交易、被花的输出。  
输出：接受或拒绝。  
invariant：解锁满足锁定；金额守恒（含费）。

**fork choice（逻辑名）**  
输入：已验证的候选尖。  
输出：当前 tip。  
invariant：只在有效链上比工作量。

具体函数名以源码为准。

---

## 18. 如何测试核心协议

Bitcoin Core 传统：大量 functional / unit；fuzz（script、P2P、地址）；有时对比不同实现。

**事实：** fuzz 和保守变更，是其工程哲学的一部分，不是「测试绿了所以永远安全」。CVE-2018-17144 说明实现测试曾漏过通胀不变量。

「不确定」应偷的测试思想：供给/双花这类 invariant 必须有直接断言，不能只靠「常见交易能过」。

看见 signet 不是已经是 testnet；看见 signet 不是已经是 regtest；看见头上有合法工作量不是已经签过：[`../../tracks/implementation/worked-example-signet-vs-testnet.md`](../../tracks/implementation/worked-example-signet-vs-testnet.md)（不变量 265）。testnet 出了名不可靠不是已经是本页。regtest 造块没有代价不是已经是本页。只加网络参数就能连 / 头上有合法工作量不是已经签过，也不是已经全验证。

---

## 19. 「不确定」适用性

| 档 | 内容 | 理由 |
|---|---|---|
| 强烈建议研究 | 规则少、全节点复验、慢升级、双花/供给 invariant 测试、编码越来越严 | 结算链的寿命来自可验证与克制 |
| 可以参考 | UTXO、mempool 与共识分层（standardness）、compact block、SPV 的假设边界 | 要连假设一起抄 |
| 暂时不需要 | PoW 挖矿市场、地址类型全家桶 | 不服务后量子结算第一问 |
| 不建议采用 | 把概率最终当「已结算」文案；自创哈希；用市值证明协议正确 | 违反五层保证 |

**建议：** 偷哲学，不要偷「我们也要十分钟一块 + 能量竞赛」当默认。
