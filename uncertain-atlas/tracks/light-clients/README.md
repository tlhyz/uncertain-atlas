# 横向地图：轻节点假设

详见 L9.6。本表只防串词。  
精读：[`worked-example.md`](worked-example.md)（阿比只看头就放货）；[`worked-example-bft-skip.md`](worked-example-bft-skip.md)（跳过中间块要重叠旧集合）；[`worked-example-sync-committee.md`](worked-example-sync-committee.md)（512 的 2/3 ≠ 全集的 2/3）；[`worked-example-blob-vs-das.md`](worked-example-blob-vs-das.md)（KZG blob ≠ PeerDAS 列抽样 ≠ Celestia 二维 DAS）；[`worked-example-snarked-vs-staged.md`](worked-example-snarked-vs-staged.md)（区块链 SNARK 验绿 ≠ 最新 staged 已被证明；Pickles ≠ Kimchi）；[`worked-example-nmt-vs-das.md`](worked-example-nmt-vs-das.md)（NMT 命名空间齐了 ≠ 扩展方阵已经可用）；[`worked-example-dacert-vs-posted.md`](worked-example-dacert-vs-posted.md)（DACert ≠ 全文已经贴上父链；AnyTrust ≠ Rollup DA）。验过头 ≠ 能交证据：[Alderfly](../failure-museum/alderfly.md)（朝前 lunatic 不得只等同高再出一块）。

| 名称 | 少下 | 多信 | 常见假冒 |
|---|---|---|---|
| 全节点 | 不 | 实现+网络 | — |
| 剪枝 | 旧体 | 自己曾验证 | 「所以是 SPV」 |
| SPV | 体 | 多数工作量 | 「所以验证了脚本」 |
| 状态证明 | 全状态 | 根的来源 | 根来自 RPC |
| DAS | 全体 | 编码+抽样 | 「抽到了所以执行对」 |
| 递归证明 | 历史重放 | 电路+证明系统 | 「22kB = 全状态」；验 π = 最新 staged |
| RPC App | 一切 | 服务商 | 「ZK 轻客户端」 |
| Nervos 概述中的 light | 非自己的 Cell | 所订全节点 | 「所以是 SPV」 |
| NEAR 分片 RPC | 非本分片状态 | 该 RPC 是否真跟踪并重建了 chunk | 「有块头所以执行过」 |
| Monad 延迟根（文档） | 本块体 | 能证的是 `N-D` 的根，不是刚最终的那块 | 「顺序最终所以状态可证」 |
| BFT 轻客户端（CometBFT 规范） | 中间头 | 信任期 + init 头 + 旧 `NextValidators` 重叠 | 「新委员会自己的 2/3」 |
| Altair 同步委员会 | 全验证者集合 | 当期 512 人样本的超级多数 | 「所以是全网 2/3 最终」 |
| 4844 blob sidecar | 袋里的字节（EVM 只见 hash） | 服务窗内 sidecar 可取 | 「有 KZG 所以是 DAS / 永远可重建」 |
| PeerDAS（Fulu 规范） | 未抽到的列 | 一维扩列 + 每槽抽样组 | 「抽到了所以执行对 / 就是 Celestia」 |
| Celestia DAS | 未抽到的份额 | 二维纠删 + 参数化概率 | 「有头所以有执行数据」；NMT 齐 = 方阵已可用 |
| AnyTrust DACert | 批次全文（父链常见只有证书） | 委员会诚实 + 证书未过期 + 能问到委员 | 「L1 有一笔所以数据在以太坊」；AnyTrust = Rollup DA |

「不确定」默认建议：结算用全节点路径。其他当显式配置。
