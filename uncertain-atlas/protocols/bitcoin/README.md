# Bitcoin 协议档案

优先级：必学  
对应课程：Level 0–3；本文件是 19 节档案，不是营销页。

完整报告：[`report.md`](report.md)

精读：[`../../tracks/mempool/worked-example-policy-vs-consensus.md`](../../tracks/mempool/worked-example-policy-vs-consensus.md)（不变量 144）。策略拒绝不是共识非法。费率高不是更正确。策略不作用于块内交易。

精读：[`../../tracks/implementation/worked-example-txid-vs-wtxid.md`](../../tracks/implementation/worked-example-txid-vs-wtxid.md)（不变量 152）。txid 不是 wtxid。改见证不是已经改交易身份。头上的 txid Merkle 不是已经承诺 wtxid。

精读：[`../../tracks/implementation/worked-example-keypath-vs-scriptpath.md`](../../tracks/implementation/worked-example-keypath-vs-scriptpath.md)（不变量 153）。钥匙路径不是已经揭开有没有脚本树。脚本路径不是已经揭开全部脚本。

精读：[`../../tracks/economic/worked-example-coinbase-vs-mature.md`](../../tracks/economic/worked-example-coinbase-vs-mature.md)（不变量 163）。进了块的 coinbase 不是已经能花。钱包看见奖励不是已经成熟。普通确认深度不是 coinbase 成熟窗。

精读：[`../../tracks/state-models/worked-example-cltv-vs-nlocktime.md`](../../tracks/state-models/worked-example-cltv-vs-nlocktime.md)（不变量 164）。脚本里的 CLTV 不是交易 nLockTime 已经把输出锁住。nLockTime 能证明将来能花不是已经证明现在不能花。

精读：[`../../tracks/state-models/worked-example-csv-vs-cltv.md`](../../tracks/state-models/worked-example-csv-vs-cltv.md)（不变量 165）。脚本里的 CSV 不是 nSequence 已经相对锁住。相对锁不是绝对锁。「CSV 之后」不是已经在讲操作码。

精读：[`../../tracks/mempool/worked-example-rbf-signal-vs-replaced.md`](../../tracks/mempool/worked-example-rbf-signal-vs-replaced.md)（不变量 166）。选择加入替换信号不是已经换掉。nSequence 用来示意可替换不是已经是相对锁。钱包看见未确认不是已经当付款。

精读：[`../../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md`](../../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md)（不变量 170）。付给脚本哈希不是已经揭开赎回脚本。旧节点 HASH160 EQUAL 通过不是新节点已经再跑赎回。哈希对上不是内层已经验过。

精读：[`../../tracks/implementation/worked-example-versionbit-vs-active.md`](../../tracks/implementation/worked-example-versionbit-vs-active.md)（不变量 171）。版本位被置上不是已经锁定。锁定不是已经激活。超时未锁定不是已经可以当激活。

精读：[`../../tracks/implementation/worked-example-valid-vs-der.md`](../../tracks/implementation/worked-example-valid-vs-der.md)（不变量 172）。ECDSA 验得过不是已经是严格 DER。库接受某种变形不是共识已经接受。转发策略已经要 DER 不是共识已经要。

一句话（禁止营销）：

> 用 UTXO + 工作量证明最重链，在无许可网络上对花费授权做概率最终的全网排序。
