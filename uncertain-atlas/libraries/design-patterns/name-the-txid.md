# 模式：隔离见证必须先点名是哪一个交易 ID

**问题：** 产品把「交易哈希」写成已经解释了签名附件。用户把 txid 听成已经含见证，或把头 Merkle 听成已经承诺 wtxid。  
**方案：** 每个 SegWit 句先点名问的是 txid、wtxid，还是头上的 txid Merkle。改见证不改 txid。wtxid 承诺在 coinbase，不在头 Merkle。  
**适用：** Bitcoin SegWit / 任何「大签名放进旧节点不理解的附件」的结算文案。  
**优点：** 用户能指出编号、附件、封面目录不是同一盏灯。  
**缺点：** 句子变长；不能再用「交易 ID」交差。  
**项目：** BIP-141：每笔两个 ID；txid 不含见证；新块规则承诺 wtxid。  
**常见 bug：** txid 写成已经含签名；头 Merkle 写成已经含见证根。  
**不确定：** 若把大签放进附件，必须写清哪一个 ID 承诺了它。见 [工作实例](../../tracks/implementation/worked-example-txid-vs-wtxid.md)。
