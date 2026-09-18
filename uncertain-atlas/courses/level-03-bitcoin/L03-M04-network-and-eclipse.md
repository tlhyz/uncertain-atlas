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

**禁止假学习：** 「我节点显示 6 确认所以主网不可逆。」「网上加密了 = 已经私人。」「字节看起来随机 = 已经认不出。」「支持第 2 版 = 第 1 版已经退役。」「看见后继地址 = 已经连得上。」「发了 sendaddrv2 = 已经只收后继格式。」「在传某种网的地址 = 已经连上那种网。」「发了 sendheaders = 已经有块。」「用头通告新尖 = 已经有块。」「重组时先发头 = 中间块已经在手里。」「按 wtxid 通告 = 已经有交易。」「发了 wtxidrelay = 已经改口。」「仍用旧类型要父交易 = 旧库存已经退役。」「对账素描 = 已经有交易。」「发了 sendtxrcncl = 已经在对账。」「对账失败退回洪水 = 库存通告已经退役。」「带见证的线上序列化 = 已经有见证。」「能提供见证 = 已经在传。」「库存通告仍用旧类型 = 线上已经没有见证。」「版本里关掉交易转发 = 已经终身只传块。」「发了停交易转发 = 已经没有紧凑块。」「建议关掉地址 = 已经禁止传地址。」「协议版本够了 = 已经支持某项功能。」「通告了 feature = 已经启用。」「verack 之后才来的 feature = 已经是本页协商。」「协议版本够了 = 已经会带 nonce 的 ping。」「看见 pong = 已经对上那一次 ping。」「回了 pong = 已经还活着。」「协议版本 = 已经是客户端版本。」「user agent = 已经可以按实现改行为。」「同一协议版本 = 已经是同一套实现。」  
**边界：** 不讲闪电路由、不讲洋葱隐藏服务路由细节、不把某篇 eclipse 实验的百分比当永恒常数。后继地址流言 ≠ 已经连得上；sendaddrv2 ≠ 已经只收后继格式；在传某种网上的地址 ≠ 已经连上那种网：[`../../tracks/network/worked-example-addrv2-vs-reachable.md`](../../tracks/network/worked-example-addrv2-vs-reachable.md) BIP-155 addrv2-gossip not already connected / not already reachable / not already old-retired 正式三事（246 余量）：[`../../tracks/network/worked-example-addr155-notreach-vs-bundled.md`](../../tracks/network/worked-example-addr155-notreach-vs-bundled.md)（不变量 1232）。 BIP-155 sendaddrv2 not already only-v2 / not already old-retired / not already unsolicited-pref 正式三事（246 余量）：[`../../tracks/network/worked-example-addr155-notpref-vs-bundled.md`](../../tracks/network/worked-example-addr155-notpref-vs-bundled.md)（不变量 1233）。 BIP-155 gossip-net not already connected-to-net / not already two-peers / not already hidden-service 正式三事（246 余量）：[`../../tracks/network/worked-example-addr155-notnet-vs-bundled.md`](../../tracks/network/worked-example-addr155-notnet-vs-bundled.md)（不变量 1234）。（不变量 246）。发了 sendheaders ≠ 已经改用头通告；用头通告新尖 ≠ 已经有块；重组时先发头 ≠ 中间块已经在手里：[`../../tracks/network/worked-example-sendheaders-vs-have.md`](../../tracks/network/worked-example-sendheaders-vs-have.md) BIP-130 sendheaders not already switched / not already have-block / not already headers-first 正式三事（247 余量）：[`../../tracks/network/worked-example-hdr130-notswitch-vs-bundled.md`](../../tracks/network/worked-example-hdr130-notswitch-vs-bundled.md)（不变量 1235）。 BIP-130 permission not already must / not already sending / not already forever 正式三事（247 余量）：[`../../tracks/network/worked-example-hdr130-notmust-vs-bundled.md`](../../tracks/network/worked-example-hdr130-notmust-vs-bundled.md)（不变量 1236）。 BIP-130 tip-headers not already have-block / not already have-middle / not already reorg-done 正式三事（247 余量）：[`../../tracks/network/worked-example-hdr130-nothave-vs-bundled.md`](../../tracks/network/worked-example-hdr130-nothave-vs-bundled.md)（不变量 1237）。（不变量 247）。按 wtxid 通告 ≠ 已经有交易；发了 wtxidrelay ≠ 已经改口；仍用旧类型要父交易 ≠ 旧库存已经退役：[`../../tracks/network/worked-example-wtxidrelay-vs-have.md`](../../tracks/network/worked-example-wtxidrelay-vs-have.md) BIP-339 wtxid-ann not already have / not already accepted / not already never-again 正式三事（248 余量）：[`../../tracks/network/worked-example-wtx339-nothave-vs-bundled.md`](../../tracks/network/worked-example-wtx339-nothave-vs-bundled.md)（不变量 1247）。 BIP-339 wtxidrelay not already switched / not already negotiated / not already using 正式三事（248 余量）：[`../../tracks/network/worked-example-wtx339-notswitch-vs-bundled.md`](../../tracks/network/worked-example-wtx339-notswitch-vs-bundled.md)（不变量 1248）。 BIP-339 old-getdata not already retired / not already have-wit / not already net-wide 正式三事（248 余量）：[`../../tracks/network/worked-example-wtx339-notold-vs-bundled.md`](../../tracks/network/worked-example-wtx339-notold-vs-bundled.md)（不变量 1249）。（不变量 248）。对账素描 ≠ 已经有那些交易；发了 sendtxrcncl ≠ 已经在对账；对账失败退回洪水 ≠ 库存通告已经退役：[`../../tracks/network/worked-example-erlay-vs-have.md`](../../tracks/network/worked-example-erlay-vs-have.md)（不变量 249）。带见证的线上序列化 ≠ 已经有见证；能提供见证 ≠ 已经在传；库存通告仍用旧类型 ≠ 线上已经没有见证：[`../../tracks/network/worked-example-witness-wire-vs-have.md`](../../tracks/network/worked-example-witness-wire-vs-have.md)（不变量 251）。调整钟 ≠ MTP：[`../../tracks/network/worked-example-adjusted-time.md`](../../tracks/network/worked-example-adjusted-time.md)（CVE-2024-52912）。MTP 自己还要拆太早 / locktime / 太新：[`../../tracks/consensus/worked-example-mtp.md`](../../tracks/consensus/worked-example-mtp.md)。MTP 也不是 CometBFT 的 PBTS / BFT Time：[`../../tracks/consensus/worked-example-pbts.md`](../../tracks/consensus/worked-example-pbts.md)。看不见未确认 ≠ 非法：[`../../tracks/failure-museum/cve-2024-52913.md`](../../tracks/failure-museum/cve-2024-52913.md)。库存三方向：[`../../tracks/network/worked-example-inventory-quotas.md`](../../tracks/network/worked-example-inventory-quotas.md)。privatebroadcast 开关 ≠ IP 已经不暴露：[`../../tracks/failure-museum/bitcoin-2026-06-privatebroadcast-v1-retry.md`](../../tracks/failure-museum/bitcoin-2026-06-privatebroadcast-v1-retry.md)（不变量 112）。机会主义未认证加密 ≠ 已经私人；伪随机字节流 ≠ 已经认不出；仍收下第 1 版 ≠ 已经退役旧线：[`../../tracks/network/worked-example-v2-transport-vs-private.md`](../../tracks/network/worked-example-v2-transport-vs-private.md)（不变量 242）。不要写怎样关握手。不要抄握手长度 / 再密钥间隔。不要抄网络编号 / 各网编码步骤。不要抄协议版本号 / 头定位器做法。不要写怎样做中间人或按时间认协议。不要写怎样按传了哪些网认出节点。不要写怎样扣头。不要写怎样改见证挡住转发。不要抄协议版本号 / 库存类型取值。不要写怎样造碰撞短标识。不要抄短标识算法 / 素描有限域 / 容量公式。不要抄标记 / 旗标 / 库存类型取值。不要写怎样拼能骗过旧解析器的字节。版本里关掉交易转发 ≠ 已经终身只传块；发了停交易转发 ≠ 已经没有紧凑块；建议关掉地址 ≠ 已经禁止：[`../../tracks/network/worked-example-disabletx-vs-lifetime.md`](../../tracks/network/worked-example-disabletx-vs-lifetime.md) BIP-338 version-flag not already lifetime / not already implemented / not already default-on 正式三事（256 余量）：[`../../tracks/network/worked-example-dis338-notlife-vs-bundled.md`](../../tracks/network/worked-example-dis338-notlife-vs-bundled.md)（不变量 1241）。 BIP-338 disabletx not already no-compact / not already tx-illegal / not already no-block 正式三事（256 余量）：[`../../tracks/network/worked-example-dis338-notcmpct-vs-bundled.md`](../../tracks/network/worked-example-dis338-notcmpct-vs-bundled.md)（不变量 1242）。 BIP-338 addr-suggest not already forbidden / not already disconnected / not already illegal 正式三事（256 余量）：[`../../tracks/network/worked-example-dis338-notaddr-vs-bundled.md`](../../tracks/network/worked-example-dis338-notaddr-vs-bundled.md)（不变量 1243）。（不变量 256）。不要抄协议版本号 / 消息类型字面量。不要写怎样按只传块连接认人。不要把关闭状态写成已经在主网默认打开。看见协议版本够了 ≠ 已经支持某项功能；看见通告了 feature ≠ 已经启用；看见 verack 之后才来的 feature ≠ 已经是本页协商：[`../../tracks/network/worked-example-feature-vs-enabled.md`](../../tracks/network/worked-example-feature-vs-enabled.md) BIP-434 version-enough not already support / not already sent-page / not already merged-old 正式三事（259 余量）：[`../../tracks/network/worked-example-feat434-notver-vs-bundled.md`](../../tracks/network/worked-example-feat434-notver-vs-bundled.md)（不变量 1244）。 BIP-434 feature-adv not already enabled / not already understood / not already illegal 正式三事（259 余量）：[`../../tracks/network/worked-example-feat434-noton-vs-bundled.md`](../../tracks/network/worked-example-feat434-noton-vs-bundled.md)（不变量 1245）。 BIP-434 after-verack not already this-handshake / not already enabled / not already implemented 正式三事（259 余量）：[`../../tracks/network/worked-example-feat434-notlate-vs-bundled.md`](../../tracks/network/worked-example-feat434-notlate-vs-bundled.md)（不变量 1246）。（不变量 259）。不要抄协议版本号 / 一字节消息类型。不要写怎样按功能标识认人。看见协议版本够了 ≠ 已经会带 nonce 的 ping；看见 pong ≠ 已经对上那一次 ping；看见回了 pong ≠ 已经还活着：[`../../tracks/network/worked-example-pong-vs-live.md`](../../tracks/network/worked-example-pong-vs-live.md)（不变量 262）。不要抄协议版本门槛数字。不要写怎样叠 ping 做日蚀。看见协议版本 ≠ 已经是客户端版本；看见 user agent ≠ 已经可以按实现改行为；看见同一协议版本 ≠ 已经是同一套实现：[`../../tracks/network/worked-example-ua-vs-protocol.md`](../../tracks/network/worked-example-ua-vs-protocol.md)（不变量 263）。不要抄栈写法或例串。不要写怎样按 user agent 认人。
