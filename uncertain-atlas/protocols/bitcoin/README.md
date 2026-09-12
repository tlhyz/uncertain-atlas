# Bitcoin 协议档案

优先级：必学  
对应课程：Level 0–3；本文件是 19 节档案，不是营销页。

完整报告：[`report.md`](report.md)

精读：[`../../tracks/mempool/worked-example-policy-vs-consensus.md`](../../tracks/mempool/worked-example-policy-vs-consensus.md)（不变量 144）。策略拒绝不是共识非法。费率高不是更正确。策略不作用于块内交易。

精读：[`../../tracks/implementation/worked-example-txid-vs-wtxid.md`](../../tracks/implementation/worked-example-txid-vs-wtxid.md)（不变量 152）。txid 不是 wtxid。改见证不是已经改交易身份。头上的 txid Merkle 不是已经承诺 wtxid。

精读：[`../../tracks/implementation/worked-example-keypath-vs-scriptpath.md`](../../tracks/implementation/worked-example-keypath-vs-scriptpath.md)（不变量 153）。钥匙路径不是已经揭开有没有脚本树。脚本路径不是已经揭开全部脚本。

精读：[`../../tracks/implementation/worked-example-tapscript-vs-scriptpath.md`](../../tracks/implementation/worked-example-tapscript-vs-scriptpath.md)（不变量 189）。走脚本路径不是已经是 tapscript 语义。遇见成功操作码不是已经执行完，也不是已经安全升级。

精读：[`../../tracks/implementation/worked-example-miniscript-vs-script.md`](../../tracks/implementation/worked-example-miniscript-vs-script.md)（不变量 191）。看见 Miniscript 不是已经是链上脚本。共识健全不是已经是策略完备。本页不覆盖付给脚本哈希。

精读：[`../../tracks/economic/worked-example-coinbase-vs-mature.md`](../../tracks/economic/worked-example-coinbase-vs-mature.md)（不变量 163）。进了块的 coinbase 不是已经能花。钱包看见奖励不是已经成熟。普通确认深度不是 coinbase 成熟窗。

精读：[`../../tracks/state-models/worked-example-cltv-vs-nlocktime.md`](../../tracks/state-models/worked-example-cltv-vs-nlocktime.md)（不变量 164）。脚本里的 CLTV 不是交易 nLockTime 已经把输出锁住。nLockTime 能证明将来能花不是已经证明现在不能花。

精读：[`../../tracks/state-models/worked-example-csv-vs-cltv.md`](../../tracks/state-models/worked-example-csv-vs-cltv.md)（不变量 165）。脚本里的 CSV 不是 nSequence 已经相对锁住。相对锁不是绝对锁。「CSV 之后」不是已经在讲操作码。

精读：[`../../tracks/mempool/worked-example-rbf-signal-vs-replaced.md`](../../tracks/mempool/worked-example-rbf-signal-vs-replaced.md)（不变量 166）。选择加入替换信号不是已经换掉。nSequence 用来示意可替换不是已经是相对锁。钱包看见未确认不是已经当付款。

精读：[`../../tracks/mempool/worked-example-feefilter-vs-rejected.md`](../../tracks/mempool/worked-example-feefilter-vs-rejected.md)（不变量 245）。看见跳过库存通告不是已经拒进池。看见发了费率过滤器不是对等节点已经照做。看见布隆过了不是已经过了费率门。

精读：[`../../tracks/network/worked-example-addrv2-vs-reachable.md`](../../tracks/network/worked-example-addrv2-vs-reachable.md)（不变量 246）。看见后继地址流言不是已经连得上。看见发了 sendaddrv2 不是已经只收后继格式。看见在传某种网上的地址不是已经连上那种网。

精读：[`../../tracks/network/worked-example-sendheaders-vs-have.md`](../../tracks/network/worked-example-sendheaders-vs-have.md)（不变量 247）。看见发了 sendheaders 不是已经改用头通告。看见用头通告新尖不是已经有块。看见重组时先发头不是中间块已经在手里。

精读：[`../../tracks/network/worked-example-wtxidrelay-vs-have.md`](../../tracks/network/worked-example-wtxidrelay-vs-have.md)（不变量 248）。看见按 wtxid 通告不是已经有那笔交易。看见发了 wtxidrelay 不是已经改口。看见仍用旧类型要父交易不是旧库存已经退役。

精读：[`../../tracks/network/worked-example-erlay-vs-have.md`](../../tracks/network/worked-example-erlay-vs-have.md)（不变量 249）。看见对账素描不是已经有那些交易。看见发了 sendtxrcncl 不是已经在对账。看见对账失败退回洪水不是库存通告已经退役。

精读：[`../../tracks/network/worked-example-limited-service-vs-archive.md`](../../tracks/network/worked-example-limited-service-vs-archive.md)（不变量 250）。看见有限服务位不是已经能服任意旧块。看见只保证最近窗口不是已经剪枝。看见服了最近一块不是已经暴露了剪到哪。

精读：[`../../tracks/network/worked-example-witness-wire-vs-have.md`](../../tracks/network/worked-example-witness-wire-vs-have.md)（不变量 251）。看见带见证的线上序列化不是已经有见证。看见能提供见证不是已经在传。看见库存通告仍用旧类型不是线上已经没有见证。

精读：[`../../tracks/light-clients/worked-example-bloom-bit-vs-retired.md`](../../tracks/light-clients/worked-example-bloom-bit-vs-retired.md)（不变量 252）。看见没开布隆服务位不是已经退役。看见开了这一位不是已经私人。看见协议版本够了不是已经在遵守。看见因过滤器命令被断开不是已经共识非法。

精读：[`../../tracks/mempool/worked-example-mempool-dump-vs-have.md`](../../tracks/mempool/worked-example-mempool-dump-vs-have.md)（不变量 253）。看见内存池查询回了一串库存不是已经有那些交易。看见只肯给最近转发过的不是已经支持整池查询。看见协议版本够了不是已经在答。

精读：[`../../tracks/network/worked-example-reject-vs-consensus.md`](../../tracks/network/worked-example-reject-vs-consensus.md)（不变量 254）。看见拒收消息不是已经共识非法。看见调试理由不是已经该给用户看。看见没拒收不是已经是当前最好链。

精读：[`../../tracks/network/worked-example-disabletx-vs-lifetime.md`](../../tracks/network/worked-example-disabletx-vs-lifetime.md)（不变量 256）。看见版本里关掉交易转发不是已经终身只传块。看见发了停交易转发不是已经没有紧凑块。看见建议关掉地址不是已经禁止传地址。看见协议版本够了不是已经实现本页。

精读：[`../../tracks/lifecycle/worked-example-uri-vs-authorized.md`](../../tracks/lifecycle/worked-example-uri-vs-authorized.md)（不变量 255）。看见付款 URI 不是已经授权，也不是已经付了。看见路径没有链上地址不是已经没有付款指示。看见不认识的必选参数不是已经能付。看见打开了回执不是已经确认。

精读：[`../../tracks/lifecycle/worked-example-signed-message-vs-control.md`](../../tracks/lifecycle/worked-example-signed-message-vs-control.md)（不变量 258）。看见签过的消息不是已经证明能控制资金。看见签过不是已经证明发过上一笔。看见资金证明清单不是已经齐，也不是已经没花。

精读：[`../../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md`](../../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md)（不变量 170）。付给脚本哈希不是已经揭开赎回脚本。旧节点 HASH160 EQUAL 通过不是新节点已经再跑赎回。哈希对上不是内层已经验过。

精读：[`../../tracks/implementation/worked-example-versionbit-vs-active.md`](../../tracks/implementation/worked-example-versionbit-vs-active.md)（不变量 171）。版本位被置上不是已经锁定。锁定不是已经激活。超时未锁定不是已经可以当激活。

精读：[`../../tracks/implementation/worked-example-valid-vs-der.md`](../../tracks/implementation/worked-example-valid-vs-der.md)（不变量 172）。ECDSA 验得过不是已经是严格 DER。库接受某种变形不是共识已经接受。转发策略已经要 DER 不是共识已经要。

精读：[`../../tracks/implementation/worked-example-coinbase-height-vs-header.md`](../../tracks/implementation/worked-example-coinbase-height-vs-header.md)（不变量 173）。coinbase 第一项写了高度不是头上已经有高度字段。块 version 加大不是已经按 BIP-9 位向量激活。写了高度不是已经能花。

精读：[`../../tracks/consensus/worked-example-duplicate-txid-vs-unique.md`](../../tracks/consensus/worked-example-duplicate-txid-vs-unique.md)（不变量 257）。看见同一交易标识不是已经唯一，也不是已经同一组可花输出。看见许多确认不是已经不怕被覆盖。看见已经花光后再出现不是已经非法。

精读：[`../../tracks/implementation/worked-example-address-vs-utxo.md`](../../tracks/implementation/worked-example-address-vs-utxo.md)（不变量 174）。看见 Bech32 地址串不是链上已经有这笔输出。校验过不是见证程序已经在链上。编出版本和程序不是已经付过款。BIP-173 不是 BIP-350，也不是 BIP-141，也不是 BIP-13。

精读：[`../../tracks/implementation/worked-example-bech32m-vs-bech32.md`](../../tracks/implementation/worked-example-bech32m-vs-bech32.md)（不变量 181）。后继校验过了不是已经是旧校验那套地址。版本 0 过了后继校验不是已经合法。更高版本过了旧校验不是已经合法。看见后继地址串不是已经有 UTXO。BIP-350 不是 BIP-173，也不是 BIP-141。

精读：[`../../tracks/implementation/worked-example-psbt-vs-broadcast.md`](../../tracks/implementation/worked-example-psbt-vs-broadcast.md)（不变量 179）。看见部分签名包不是已经是网上能广播的完整交易。里面有几张签不是这一输入已经凑齐。抽出完整交易不是已经广播。BIP-174 不是 BIP-173，也不是 BIP-125。

精读：[`../../tracks/implementation/worked-example-xpub-vs-spendable.md`](../../tracks/implementation/worked-example-xpub-vs-spendable.md)（不变量 182）。看见扩展公钥不是已经能花。去势后的扩展公钥不是已经是普通公钥。硬化子密钥不是已经能从公钥推出。链节点标识对得上不是已经该当成收款地址。BIP-32 不是 BIP-173，也不是 BIP-174，也不是 BIP-350。

精读：[`../../tracks/implementation/worked-example-mnemonic-vs-seed.md`](../../tracks/implementation/worked-example-mnemonic-vs-seed.md)（不变量 183）。看见助记词不是已经是二进制种子。用户自造句子不是已经是本页那种助记词。口令不同不是已经非法。助记词校验过了不是已经能改对。BIP-39 不是 BIP-32，也不是 BIP-173，也不是 BIP-380。

精读：[`../../tracks/implementation/worked-example-descriptor-vs-keys.md`](../../tracks/implementation/worked-example-descriptor-vs-keys.md)（不变量 184）。看见私钥或助记词备份不是已经知道该看哪种输出脚本。看见描述符不是已经是地址。描述符里的扩展钥不是已经能长出脚本。描述符校验过了不是已经是合法脚本集合。BIP-380 不是 BIP-39，也不是 BIP-32，也不是 BIP-173。

精读：[`../../tracks/implementation/worked-example-psbtv2-vs-v0.md`](../../tracks/implementation/worked-example-psbtv2-vs-v0.md)（不变量 186）。看见后继版本工作包不是已经是旧版那份固定未签交易。能再加输入输出不是已经凑齐，也不是已经能广播。包版本号不是已经是交易版本号。能按旧格式拆开不是已经兼容。BIP-370 不是 BIP-174，也不是 BIP-173，也不是 BIP-125。

一句话（禁止营销）：

> 用 UTXO + 工作量证明最重链，在无许可网络上对花费授权做概率最终的全网排序。
