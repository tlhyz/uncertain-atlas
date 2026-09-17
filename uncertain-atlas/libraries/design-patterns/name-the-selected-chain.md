# 模式：DAG 上的「到了」必须点名是成员还是 selected chain

**问题：** 并行块留下再排序，产品却把「进了一个块」写成已经最终。用户把 DAG 成员听成规范历史。  
**方案：** 每个「到了」先点名问的是 DAG 里有、mergeset、蓝，还是 selected chain 前缀。并行共存与 orphan 扔掉分开写。  
**适用：** 块 DAG、任何「留下并行块再线性化」的结算文案。  
**优点：** 用户能指出手里是卸在工地的砖，还是砌墙顺序单；不会把 explorer 绿勾当成 commit。  
**缺点：** 句子变长；不能再用「DAG 所以秒确认」交差。  
**项目：** Kaspa Wiki：并行块不被 orphan；selected chain 决定顺序且可 reorg；accepting block 是合并它的链块。  
**常见 bug：** 进块写成已最终；DAG 写成 Avalanche；蓝写成 QC。  
**不确定：** 第一版不必上高块率 DAG。若对照，必须点名成员还是 selected chain。见 [工作实例](../../tracks/consensus/worked-example-dag-vs-selected-chain.md)。
