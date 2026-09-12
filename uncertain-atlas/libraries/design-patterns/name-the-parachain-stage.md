# 模式：先点名平行块停在哪一行

**问题：** 「已经上链」下面叠着 Candidate、Backable、Backed、Pending availability、Included、Pending approval、Approved、GRANDPA。  
**方案：** 每个产品句只点名一行。回执、纠删片、二次检查、最终性装置分开写绿勾。  
**适用：** 共享安全、平行链 / 核心时间、任何「小链借用大验证者」的文案。  
**优点：** 用户能指出自己还在等哪一盏灯；RPC、回执、可用不会并成一句。  
**缺点：** 句子变长；不能再用「平行链已出块」交差。  
**项目：** Polkadot 官方 Inclusion Pipeline + Approval Process；回执进中继，片在验证者磁盘。  
**常见 bug：** backed 写成可用；可用写成有效；审批写成最终；collator RPC 写成共享安全。  
**不确定：** 可以参考「阶段必须点名」；第一版不要做平行链租户。见 [工作实例](../../tracks/finality/worked-example-backed-vs-available.md)。
