# L3.4 传播、日蚀与「我看见了」

优先级：必学（知识树 M3.2）  
先修：L3.1，L9.1 可并行；本课先把 Bitcoin 网上的具体故事钉死

---

## A. 先修知识

最重链只对**你下载并验证过的**合法块有意义。  
你没连上诚实图，你的「最重」可以是对手喂的子集。L3.1 的经济最终性默认你看见了真实主链。

---

## B. 核心问题

**块和交易怎么走？日蚀如何把「确认数」变成对手的道具？compact block 省的是带宽还是验证？**

---

## C. 直觉（ELI15）

全班堆砖，但你被六个人围住，他们只给你看他们自己堆的塔。  
你数了 6 层，以为稳了。窗帘外面真正的塔早就拐弯了。

传砖也可以偷懒：邻居说「新一层跟你桌上那堆零件一样，我只寄缺的那几块」。这是 compact block 的直觉——省的是**重复字节**，不是「可以不验证」。

---

## D. 正式定义

**传播路径（事实级）**

1. 交易进各节点本地 mempool（政策不同，见 L3.2 / L9.2）。  
2. 矿工（或池）组块。  
3. 新块头 + 体在 P2P 上流言。  
4. 节点验 PoW、验交易、更新 tip。

**Compact blocks（BIP 152 方向，细节以 BIP 为准）**

发送短标识，接收方用本地 mempool 重建。重建失败再要完整体。  
**是：** 带宽优化。  
**不是：** 跳过共识校验；不是 DA 抽样。

**Eclipse（部署/网络）**

对手占满你的出边，过滤你看见的块与交易。  
协议的最重链规则此时仍「对你本地视图正确」。它救不了你的视图是假的。

**与分区的差别**

| | 分区 | 日蚀 |
|---|---|---|
| 诚实图 | 切成两块，两边都可能有真算力 | 你被隔离，主网可仍连通 |
| 典型结果 | 两边各长，合拢重组 | 你看见假确认 / 被审查 |
| 保证层 | 协议在分区模型下的行为 | 部署：你的邻居选择 |

---

## E. 最小案例

商家节点 8 个出边全是攻击者。攻击者先给含 T 的短链，商家数到 k 确认发货。  
同时主网另一条更重的链从不含 T。窗帘拉开（或商家换节点）后重组，T 消失。  
L3.1 的「k 确认够贵」对**主网算力**成立，对**被日蚀的单一节点**不成立。

---

## F. 真实项目

Bitcoin P2P、BIP 152、关于 eclipse 的学术文献（深挖时回论文，本课不把博客当规范）。  
Solana Turbine、Ethereum 两套网络是同一攻击面的不同形状（L6.1 / L5.2 / L9.1）。

---

## G. 源码入口

预告：出边管理、地址管理、块下载、compact 重建失败回退。  
先问「我怎么认识邻居」，再问 `nChainWork`。

---

## H. 攻击者模型

- 占满新节点引导集（部署）。  
- 只给你看含双花前半的链。  
- 让钱包只连自己的 RPC——连 P2P 都没有（比日蚀更便宜）。  
- 用垃圾 inv 占带宽，让诚实块变慢（部署/经济）。

---

## I. 代价

多出边、多样引导：抗日蚀，耗连接与运营。  
少出边、只信一家 RPC：家用方便，结算语义在别人手里。

---

## J. 对「不确定」的意义

结算节点的威胁模型必须写：**最少诚实出边、引导集谁控制、RPC 是否算验证。**  
后量子大签名先挤满流言管道，再谈虚拟机。

---

## 精密检查

| 层 | 本课钉住 |
|---|---|
| 密码学 | 仍要验 PoW 与交易签名；日蚀不伪造签 |
| 协议 | 最重链对本地已见表 |
| 实现 | compact 重建错了必须回退完整体 |
| 部署 | 邻居选择、引导、NAT |
| 经济 | k 确认只对看见主网算力的人有意义 |

**禁止假学习：** 「我节点显示 6 确认所以主网不可逆。」  
**边界：** 不讲闪电路由、不讲 Tor 细节、不把某篇 eclipse 实验的百分比当永恒常数。调整钟 ≠ MTP：[`../../tracks/network/worked-example-adjusted-time.md`](../../tracks/network/worked-example-adjusted-time.md)（CVE-2024-52912）。MTP 自己还要拆太早 / locktime / 太新：[`../../tracks/consensus/worked-example-mtp.md`](../../tracks/consensus/worked-example-mtp.md)。MTP 也不是 CometBFT 的 PBTS / BFT Time：[`../../tracks/consensus/worked-example-pbts.md`](../../tracks/consensus/worked-example-pbts.md)。看不见未确认 ≠ 非法：[`../../tracks/failure-museum/cve-2024-52913.md`](../../tracks/failure-museum/cve-2024-52913.md)。库存三方向：[`../../tracks/network/worked-example-inventory-quotas.md`](../../tracks/network/worked-example-inventory-quotas.md)。privatebroadcast 开关 ≠ IP 已经不暴露：[`../../tracks/failure-museum/bitcoin-2026-06-privatebroadcast-v1-retry.md`](../../tracks/failure-museum/bitcoin-2026-06-privatebroadcast-v1-retry.md)（不变量 112）。不要写怎样关握手。
