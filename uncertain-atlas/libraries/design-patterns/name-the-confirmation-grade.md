# 模式：确认必须点名是哪一等

**问题：** 一条链上同时有「此刻的头」「中间检查点」「不可逆检查点」，产品却只说「确认了」。  
**方案：** 每个用户可见的绿勾只点名一等。出块、justified、finalized 分开写。RPC 标签与协议对象分开写；没有官方句就不要把 `safe` 写成 justified。  
**适用：** 头可摆 + 检查点最终的混合共识；任何把「提出」「安全头」「最终」做成不同 API 的结算文案。  
**优点：** 用户能指出自己还在等哪一等；交易所不会在头上发货还以为已经归档。  
**缺点：** 句子变长；不能再用「PoS 所以秒到」交差。  
**项目：** Ethereum Gasper（LMD-GHOST 选头 + Casper-FFG 两步升级）。JSON-RPC `latest` / `safe` / `finalized`。  
**常见 bug：** 出块写成最终；justified 写成不可逆；`safe` 写成 finalized；与 BABE/GRANDPA 或 NEAR 双标记糊成一句。  
**不确定：** 可以参考「确认必须点名」；第一版不要同时卖三等。见 [工作实例](../../tracks/finality/worked-example-head-vs-justified-vs-finalized.md)。
