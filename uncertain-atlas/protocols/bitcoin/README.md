# Bitcoin 协议档案

优先级：必学  
对应课程：Level 0–3；本文件是 19 节档案，不是营销页。

完整报告：[`report.md`](report.md)

精读：[`../../tracks/mempool/worked-example-policy-vs-consensus.md`](../../tracks/mempool/worked-example-policy-vs-consensus.md)（不变量 144）。策略拒绝不是共识非法。费率高不是更正确。策略不作用于块内交易。

精读：[`../../tracks/implementation/worked-example-txid-vs-wtxid.md`](../../tracks/implementation/worked-example-txid-vs-wtxid.md)（不变量 152）。txid 不是 wtxid。改见证不是已经改交易身份。头上的 txid Merkle 不是已经承诺 wtxid。

精读：[`../../tracks/implementation/worked-example-keypath-vs-scriptpath.md`](../../tracks/implementation/worked-example-keypath-vs-scriptpath.md)（不变量 153）。钥匙路径不是已经揭开有没有脚本树。脚本路径不是已经揭开全部脚本。

一句话（禁止营销）：

> 用 UTXO + 工作量证明最重链，在无许可网络上对花费授权做概率最终的全网排序。
