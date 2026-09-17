# 模式：抽签步骤必须点名停在哪一步

**问题：** VRF 中签、最低哈希过滤、soft vote、certify 被收成一句「密码抽签所以最终」。  
**方案：** 每个「到了」先点名问的是抽中、最低提案、soft vote 还是证书入账。参与钥与花费钥分开写。抽签与问邻居分开写。  
**适用：** Algorand 味委员会、任何「私下抽签再 BA」的结算文案。  
**优点：** 用户能指出手里是信封还是出版章；不会把 VRF 证明当成已经落账。  
**缺点：** 句子变长；不能再用「Pure PoS」交差。  
**项目：** Algorand 官方 Consensus Overview：propose / soft vote / certify。  
**常见 bug：** 抽中写成已认证；最低哈希写成已最终；抽签写成 Avalanche 抽样；拆账户写成更占便宜。  
**不确定：** 可以参考「抽签必须点名步骤」；第一版可以不上 VRF 委员会。见 [工作实例](../../tracks/consensus/worked-example-vrf-sortition-vs-certified.md)。
