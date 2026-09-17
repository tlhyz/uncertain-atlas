# 反模式：复用 OTS 叶子

同一 `(pk, ots_index)` 签两封不同消息，或把有状态私钥拷到第二台机器再签。

RFC 8391：先更新私钥，再输出签名。  
SP 800-208：两份不同消息、同一 OTS 叶子 ⇒ 伪造变得可行；禁止导出私钥正是为了挡住「备份 = 第二份状态」。

链上若只验 Merkle 路径、不记已用 index，复用会变成合法授权。  
QRL 文档把「节点拒绝重复 OTS index」写成网络规则——那是协议钉子，不是钱包提示。

亲戚：不变量 17、语料 C19、精读 `tracks/post-quantum/worked-example-ots-reuse.md`。
