# NEAR · Nightshade（思想级）

优先级：进阶（独特思想：一条块链 + 每高度每分片最多一个 chunk；头上两种最终性标记分开）  
完整报告：[`report.md`](report.md)

过滤器通过理由：Bitcoin / CometBFT 不分片；Polkadot 是中继 + 平行链各自候选；Celestia 切的是 DA 不是执行分片。NEAR 把「分片」做成**同一条链上的 chunk**，不是再养 N 条分片链。

一句话：

> 全网一个块哈希；块里挂各分片的 chunk（0 或 1 个）。执行只对你拿到的、且你跟踪的那些 chunk。头上的 Doomslug 标记 ≠ 头上的 BFT 最终标记。
