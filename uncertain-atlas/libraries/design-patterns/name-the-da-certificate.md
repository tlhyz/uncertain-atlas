# 模式：乐观租户的 DA 必须点名是全文还是证书

**问题：** 产品把「数据在以太坊」写成已经解释了 AnyTrust。用户把父链 Inbox 里的 DACert 听成批次全文，或把委员会听成纠删抽样。  
**方案：** 每个 DA 句先点名问的是父链上的 blob/calldata 全文、委员会 DACert，还是凑不齐签名后的回退贴文。证书必须写出过期，不是已经永存。  
**适用：** AnyTrust / DAC、任何「父链只收证明、数据在委员会」的结算文案。  
**优点：** 用户能指出储物柜里是练习册还是签字条。  
**缺点：** 句子变长；不能再用「也是 Arbitrum」交差。  
**项目：** 官方 AnyTrust Protocol：排序者可贴全文或 DACert；Inbox 拒无效 Keyset；子链验其余；凑不齐签则回退贴全文。  
**常见 bug：** 证书写成全文；AnyTrust 写成 Rollup DA；委员会写成 DAS。  
**不确定：** 第一版不要靠外部 DA 委员会。若对照，必须点名数据在哪。见 [工作实例](../../tracks/light-clients/worked-example-dacert-vs-posted.md)。
