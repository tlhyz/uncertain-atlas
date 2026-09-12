# 模式：头上的应用根必须先点名是哪一块的

**问题：** 产品把「头上有 AppHash」写成已经解释了本块入账。用户把本头根听成本高度交易已经交差，把 DataHash 听成效果已经进本头。  
**方案：** 每个状态根句先点名问的是本头 `AppHash`（上一块 Finalize）、本块 `DataHash`，还是本高度刚回、要进下一块头的根。  
**适用：** CometBFT / 任何「先定序、执行根印到下一块头」的结算文案。  
**优点：** 用户能指出昨天封条、今天目录、散会后新封条不是同一枚章。  
**缺点：** 句子变长；不能再用「有状态根」交差。  
**项目：** cometbft `spec/core/data_structures.md`；ABCI++ `ResponseFinalizeBlock.app_hash` 进下一块头。  
**常见 bug：** 本头 AppHash 写成本块已入账；Finalize 回根写成已印本头。  
**不确定：** 若抄 CometBFT 头，必须写清滞后一块。不要发明本头同时带本块根却不另写提交规则。见 [工作实例](../../tracks/consensus/worked-example-apphash-vs-this-block.md)。
