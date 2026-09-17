# 模式：乐观租户的「到了」必须点名停在哪颗推导头

**问题：** 产品把排序者出块、L1 当前可推导、L1 已 finalized 可推导写成一个绿勾，又和以太坊 RPC `safe` 撞名。用户把 `latest` 听成已经贴上 L1，或把桥等待听成链还没 finalized。  
**方案：** 每个「到了」先点名问的是 `unsafe` / `latest`、能从当前 canonical L1 推导的 `safe`，还是能从 L1 已 finalized 部分推导的 `finalized`。桥兑付另写。  
**适用：** 乐观 rollup、任何「先出 L2 块、再从 L1 反推」的结算文案。  
**优点：** 用户能指出手里是厨房小票，还是总店当天菜单，还是已经锁进保险柜；不会把同名 RPC 当成 Gasper。  
**缺点：** 句子变长；不能再用「和以太坊一样有 safe」交差。  
**项目：** OP Stack Derivation / Glossary：`unsafe` 尚未从 L1 推导；`safe` 从当前 canonical L1 完整推导；`finalized` 从 L1 已不可逆部分推导。官方文档：桥等待不是 L2 finalized。  
**常见 bug：** `latest` 写成已推导；OP `safe` 写成 justified；桥窗写成链还没最终。  
**不确定：** 第一版不要当别人的乐观租户。若对照，必须点名推导头，不得复用 Gasper 标签当同一对象。见 [工作实例](../../tracks/finality/worked-example-unsafe-vs-derived.md)。
