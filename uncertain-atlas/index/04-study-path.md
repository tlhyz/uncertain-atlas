# 怎么读这套图谱（目的 A）

不是浏览目录。按下面顺序走，每步结束时必须能用自己的话讲，不能只复述标题。  
不出题。试题仍在 `exams/`，后置。

---

## 第一通：一笔钱

1. L0.1–L0.8：机器、授权、门、五层。  
2. L0.7 画自己的门。  
3. [`../tracks/lifecycle/README.md`](../tracks/lifecycle/README.md) 五列表。  
4. [`../tracks/lifecycle/worked-example.md`](../tracks/lifecycle/worked-example.md) 跟完阿安付 1。  
5. 停。若还不能指出「钱包绿勾」在每一列指哪一层，不要进 L6。

## 第二通：工具

6. L1 哈希 / 签名 / Merkle / 编码。  
7. L2.1–L2.4 状态；L2.5 只在你关心「输出带数据」时读。  
8. 打开决策矩阵状态表，确认最后一列是空的。

## 第三通：两种最终

9. L3.1 + Bitcoin 档案第 6、11、14 节。  
10. L4.1–L4.5 + CometBFT 档案。  
11. [`../tracks/finality/README.md`](../tracks/finality/README.md) 只看 Bitcoin 与 CometBFT 两行，先不要横扫全表。

## 第四通：实现会骗人

12. L5.3 多客户端同根。  
13. 博物馆：CVE-2010-5139、CVE-2018-17144、BIP 50。  
14. L9.3 / L9.7。问：绿测试守哪一层。

## 第五通：别人用什么换

15. L6.4 三种并行（先读对照，再按需回 6.1–6.3）。  
16. L7.1–L7.4 + 生命周期表的乐观 L2 列。  
17. L8.1–L8.3；L8.4 若要碰证明。  
18. 每读完一条档案，回 `tracks/` 对应表改一格或确认已有格。

## 第六通：不确定镜头（仍不选型）

19. L10.1 纪律。  
20. 威胁模型 + [`../libraries/settlement-copy.md`](../libraries/settlement-copy.md)。  
21. L10.3 最小机器清单。  
22. L10.4 / PQ 迁移状态机 + [`../tracks/post-quantum/worked-example-migration.md`](../tracks/post-quantum/worked-example-migration.md)。不填算法。

若有人丢给你一条新链：用 [`../libraries/new-chain-intake.md`](../libraries/new-chain-intake.md)，不要先打开官网首页。
