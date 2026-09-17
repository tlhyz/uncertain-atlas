# 模式：有效性租户的「到了」必须点名停在哪一档

**问题：** 排序者回执、L2 共识最终、L1 高度追上，产品却写成一个绿勾。用户把 `PRE_CONFIRMED` 听成已经在房东入账。  
**方案：** 每个「到了」先点名问的是 `CANDIDATE`、`PRE_CONFIRMED`、`ACCEPTED_ON_L2` 还是 `ACCEPTED_ON_L1`。验证明必须写出当前登记的 program hash。  
**适用：** 有效性 rollup、任何「租户先绿、房东后更新」的结算文案。  
**优点：** 用户能指出手里是厨房小票，还是总店账本高度；不会把 explorer 绿勾当成可提款。  
**缺点：** 句子变长；不能再用「ZK 所以秒最终」交差。  
**项目：** Starknet 官方 Transactions：`PRE_CONFIRMED` 是排序者已执行写回执；`ACCEPTED_ON_L2` 是共识最终块；`ACCEPTED_ON_L1` 是 L1 高度追上。SNOS 页：Core 登记 program hash。  
**常见 bug：** 回执写成 L2 最终；L2 写成 L1；验证明写成物理定律。  
**不确定：** 第一版不要当别人的有效性租户。若对照，必须点名档位和被锁程序。见 [工作实例](../../tracks/finality/worked-example-l2-status-vs-l1.md)。
