# 乐观 Rollup 档案（Arbitrum / Optimism 对照）

优先级：重要（独特思想：先执行后揭穿）  
完整报告：[`report.md`](report.md)

一句话：

> 执行在 L2，承诺与数据落到 L1；默认根为真，争议期内可用欺诈/过错证明推翻。排序与 DA 是单独的失败点。

精读：[`../../tracks/finality/worked-example-unsafe-vs-derived.md`](../../tracks/finality/worked-example-unsafe-vs-derived.md)（不变量 141）。OP Stack 规范把 `unsafe` / `safe` / `finalized` 写成三颗推导头，不是 Gasper 三等，也不是桥已经兑付。  
AnyTrust：[`../../tracks/light-clients/worked-example-dacert-vs-posted.md`](../../tracks/light-clients/worked-example-dacert-vs-posted.md)（不变量 142）。DACert 不是全文已经贴上父链。凑不齐签回退贴全文不是已经只走委员会。
