# 怎么读这套图谱（目的 A）

不是浏览目录。按下面顺序走，每步结束时必须能用自己的话讲，不能只复述标题。  
不出题。试题仍在 `exams/`，后置。

---

## 第一通：一笔钱

1. L0.1–L0.8：机器、授权、门、五层。  
2. L0.7 画自己的门。  
3. [`../tracks/lifecycle/README.md`](../tracks/lifecycle/README.md) 五列表。  
4. [`../tracks/lifecycle/worked-example.md`](../tracks/lifecycle/worked-example.md) 跟完阿安付 1。  
5. 停。若还不能指出「钱包绿勾」在每一列指哪一层，不要进 L6。日蚀 / 内存池：[`../tracks/network/worked-example-eclipse.md`](../tracks/network/worked-example-eclipse.md)、[`../tracks/mempool/worked-example.md`](../tracks/mempool/worked-example.md)。

## 第二通：工具

6. L1 哈希 / 签名 / Merkle / 编码 / 随机数与确定性（L1.6）。域分离三层编码：[`../tracks/crypto/worked-example-tagged-hash.md`](../tracks/crypto/worked-example-tagged-hash.md)（BIP-340 ≠ EIP-712 ≠ FIPS `ctx`）。  
7. L2.1–L2.4 状态；L2.5 只在你关心「输出带数据」时读；L2.6 在你关心「谁为磁盘付钱」时读。  
8. 打开决策矩阵状态表，确认最后一列是空的。

## 第三通：两种最终

9. L3.1 + Bitcoin 档案第 6、11、14 节。IBD 加速：[`../tracks/implementation/worked-example-assumevalid.md`](../tracks/implementation/worked-example-assumevalid.md)（跳过签名 ≠ 锁死历史）。  
10. L4.1–L4.5 + CometBFT 档案。投票 SignBytes：[`../tracks/consensus/worked-example-vote-signbytes.md`](../tracks/consensus/worked-example-vote-signbytes.md)（prevote 的印不能验成 precommit）。  
11. [`../tracks/finality/README.md`](../tracks/finality/README.md) 只看 Bitcoin 与 CometBFT 两行，再读 [`../tracks/consensus/worked-example-partition.md`](../tracks/consensus/worked-example-partition.md)。先不要横扫全表。读 L5.2 时补 [`../tracks/finality/worked-example-weak-subjectivity.md`](../tracks/finality/worked-example-weak-subjectivity.md)（finalized ≠ 从创世同步同样安全）。

## 第四通：实现会骗人

12. L5.3 多客户端同根。  
13. [`../tracks/implementation/`](../tracks/implementation/README.md) 编码实例 + 崩溃实例。  
14. 博物馆：CVE-2010-5139、CVE-2018-17144、CVE-2012-2459、BIP 50、CVE-2021-39137；先用 [`../tracks/failure-museum/worked-example-five-layers.md`](../tracks/failure-museum/worked-example-five-layers.md) 把 17144 拆进五层。隐私通再读 CVE-2019-7167。  
15. L9.3 / L9.7 + [`../tracks/testing/worked-example.md`](../tracks/testing/worked-example.md)。问：绿测试守哪一层。形式化缝：[`../tracks/formal-methods/worked-example.md`](../tracks/formal-methods/worked-example.md)。

## 第五通：别人用什么换

16. L6.4 三种并行（先读对照，再按需回 6.1–6.3）。  
17. L7.1–L7.4 + 生命周期表的乐观 L2 列。NEAR 只在你关心「一条链上的 chunk」时读 `protocols/near/`；不要和 Polkadot 共享安全混成一词。blob ≠ DAS：[`../tracks/light-clients/worked-example-blob-vs-das.md`](../tracks/light-clients/worked-example-blob-vs-das.md)（KZG sidecar ≠ PeerDAS 列 ≠ Celestia 二维抽样；4096 epoch 服务窗）。  
18. L8.1–L8.3；L8.4 若要碰证明。  
19. [`../tracks/light-clients/worked-example.md`](../tracks/light-clients/worked-example.md) 后再看 L9.6 表。BFT 跳过：[`../tracks/light-clients/worked-example-bft-skip.md`](../tracks/light-clients/worked-example-bft-skip.md)（新委员会自己的 2/3 ≠ 轻客户端信任）。Altair 抽样：[`../tracks/light-clients/worked-example-sync-committee.md`](../tracks/light-clients/worked-example-sync-committee.md)（512 的 2/3 ≠ 全集的 2/3；EIP-8390 是草案）。共享安全对照再读 [`../protocols/eigenlayer/README.md`](../protocols/eigenlayer/README.md)（仅过滤器；restake ≠ 中继质押 ≠ BTC 仍在比特币）。  
20. 每读完一条档案，回 `tracks/` 对应表改一格或确认已有格。

## 第六通：不确定镜头（仍不选型）

21. L10.1 纪律。  
22. 威胁模型 + [`../libraries/settlement-copy.md`](../libraries/settlement-copy.md) + [`../tracks/upgrades/worked-example.md`](../tracks/upgrades/worked-example.md) + [`../tracks/economic/worked-example.md`](../tracks/economic/worked-example.md) + [`../tracks/economic/worked-example-evidence.md`](../tracks/economic/worked-example-evidence.md) + [`../tracks/economic/worked-example-casper-slashing.md`](../tracks/economic/worked-example-casper-slashing.md)（两张签不够；要指出 double / surround / 同 slot 头 / 应用裁量）。  
23. L10.3 最小机器清单。  
24. L10.4 / PQ 迁移状态机 + [`../tracks/post-quantum/worked-example-migration.md`](../tracks/post-quantum/worked-example-migration.md)。不填算法。尺寸卡：[`../tracks/post-quantum/nist-size-card.md`](../tracks/post-quantum/nist-size-card.md)；投票字节：[`../tracks/post-quantum/worked-example-vote-bytes.md`](../tracks/post-quantum/worked-example-vote-bytes.md)。有状态哈希签：[`../tracks/post-quantum/stateful-hbs.md`](../tracks/post-quantum/stateful-hbs.md) + OTS 复用精读。FIPS 外部 `ctx`：[`../tracks/post-quantum/fips-context.md`](../tracks/post-quantum/fips-context.md) + 空 ctx 精读。CPU 仍空。 QRL 只读过滤器页，不抄生态。  
25. [`../libraries/adversarial-corpus/README.md`](../libraries/adversarial-corpus/README.md) 对照不变量。这不是考试。

若有人丢给你一条新链：用 [`../libraries/new-chain-intake.md`](../libraries/new-chain-intake.md)，不要先打开官网首页。
