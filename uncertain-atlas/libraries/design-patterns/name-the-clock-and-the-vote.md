# 模式：逻辑钟与投票必须分开点名

**问题：** 可验时序、超多数票、最大 lockout 被收成一句「PoH 最终」。  
**方案：** 每个「到了」先点名问的是槽钟、账本票、RPC `processed` / `confirmed` / `finalized`，还是 root。钟不代替票。  
**适用：** PoH + Tower、任何「先有全局钟再投票」的结算文案。  
**优点：** 用户能指出 explorer 绿勾停在哪一档；不会把槽号当成 commit。  
**缺点：** 句子变长；不能再用「也是 PoS」交差。  
**项目：** Solana 术语 + RPC commitment。  
**常见 bug：** PoH 写成单独 BFT；`confirmed` 写成 `finalized`；槽走写成已经 root。  
**不确定：** 可以参考「钟与票必须分开」；第一版不要同时卖三套「到了」。见 [工作实例](../../tracks/consensus/worked-example-poh-vs-tower.md)。
