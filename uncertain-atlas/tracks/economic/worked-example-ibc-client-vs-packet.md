# 工作实例：轻客户端不是已经开连接，连接不是已经开通道，通道不是已经送达数据包

> **事实 / 推断 / 建议** 已分开。
> 对照：[L7.3](../../courses/level-07-modular/L07-M03-shared-security.md)、[CometBFT 档案](../../protocols/cometbft/README.md)、[提交 ≠ 兑付](worked-example.md)、[ICS-23 验绿 ≠ 在树里](../failure-museum/dragonberry.md)、[超时挂钩 ≠ 已原子](../failure-museum/asa-2024-007.md)、[ack JSON ≠ 已确定](../failure-museum/isa-2025-001.md)。
> 主文献：IBC 官方规范 [ICS-02 Client](https://github.com/cosmos/ibc/blob/main/spec/core/ics-002-client-semantics/README.md)、[ICS-03 Connection](https://github.com/cosmos/ibc/blob/main/spec/core/ics-003-connection-semantics/README.md)、[ICS-04 Channel & Packet](https://github.com/cosmos/ibc/blob/main/spec/core/ics-004-channel-and-packet-semantics/README.md)。资料层级是 IBC/TAO 规范。不另写 19 节。
> 本页钉 **客户端 ≠ 连接**、**连接 ≠ 通道**、**通道 ≠ 数据包已送达**、**发出承诺 ≠ 对岸已经 recv**。不抄握手步数、超时高度、ibc-go 版本。不写怎样构造包或嵌套 ICS-20。

---

## 0. 先修

- [L4.4](../../courses/level-04-bft/) ABCI：应用不是共识
- [L7.3](../../courses/level-07-modular/L07-M03-shared-security.md) 跨链信使
- [不变量 77](../../libraries/invariants/README.md) ack 必须确定
- [不变量 79](../../libraries/invariants/README.md) ICS-23 验绿 ≠ 叶子在树里
- [不变量 146](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见「开了 IBC」或看见链上有一个 client，以为对岸已经能收钱；或看见 connection OPEN，以为通道已经在送包；或看见 send 绿了，以为对岸已经 recv。

官方句（事实）：

- ICS-02：*client* 是远程状态机的 **validity predicate + 一份可信状态**。它让宿主验证对岸**状态更新**。规范写：轻客户端一般**不**验证整份状态转移逻辑。
- ICS-02 被 ICS-03 **要求**；有客户端不是已经有连接。
- ICS-03：*connection* 是两条链上各一个 connection end，各自绑着对岸的轻客户端，用来做跨链子状态验证，并（通过通道）关联数据包。连接 + 客户端定义 IBC 的 **授权**语义；**排序**语义在 ICS-04。
- ICS-04：*channel* 给模块之间的包提供排序、恰好一次、模块许可。每个通道绑一条连接；一条连接可以有许多通道。通道对载荷**无所知**。
- ICS-04：*packet* 由外部 relayer 从一条链读出、提交到另一条。两边独立出块；包可被延迟、审查、重排。`sendPacket` 在本链存的是数据与超时的**短哈希承诺**，不是全文。模块必须与 `sendPacket` **原子**执行应用逻辑。`recvPacket` 是对岸另一扇门。
- 规范**没有**把建客户端写成已经开连接，也没有把开连接写成已经开通道，也没有把通道写成应用已经结算，也没有把本链承诺写成对岸已经 recv。

客户端、连接、通道、数据包，是四层对象。

---

## 2. 直觉（ELI15）

先在通讯录里记下对岸派出所的验章方法（客户端）。  
再和对方派出所互换备案，证明「我认你的章」（连接）。  
再给两个具体科室拉一条管道（通道）。  
最后才有人把信封从这头送到那头（数据包）。  

记下验章方法，不是已经在寄钱。管道通了，不是信封已经到。本县柜台上盖了「已收寄」的指纹，不是邻县已经拆开。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| 客户端（ICS-02） | 对岸状态更新的验法 + 可信状态 | 已经开连接；已经验证整条对岸状态机；已经送包 |
| 连接（ICS-03） | 两端各绑一个客户端，做授权 / 子状态验证 | 已经开通道；已经排序；已经结算 |
| 通道（ICS-04） | 模块之间的管道：排序、恰好一次、许可 | 已经懂载荷；已经 ICS-20 兑付；已经 recv |
| 数据包 | 经 relayer 传的应用数据；本链只存承诺 | 对岸已经 recv；已经 ack；已经超时结算 |
| relayer | 链外读出并提交的人 | 共识；已经送达的证明 |

---

## 4. 最小案例

两条链要对齐「一笔跨链」。

1. A 上创建 B 的轻客户端。ICS-02：只能验 B 的状态更新。不是已经和 B 开连接。
2. A、B 跑完连接握手。ICS-03：授权语义齐了。不是已经有通道，也不是已经在送包。
3. 两个模块开一条通道。ICS-04：管道对载荷无所知。不是已经 ICS-20 铸了券，也不是桥已经兑付。
4. 模块调用 `sendPacket`。ICS-04：本链写下短承诺，应用逻辑必须原子执行。不是对岸已经 `recvPacket`。
5. Relayer 还没提交。规范：包可被延迟。不是高度已经停，也不是钱已经在对岸。
6. 有人把这听成 ICS-23 Verify 绿所以叶子在树里（不变量 79），或听成超时挂钩已经原子（不变量 78）。那些是证明和回调。本页是四层对象。

「开了 IBC 所以钱已经到对岸」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | 客户端验的是对岸共识承诺，不是整份应用逻辑 |
| 协议 | 必须点名问的是客户端、连接、通道还是数据包 |
| 实现 | ibc-go 分 `02-client` / `03-connection` / `04-channel`；实现名不是规范已齐 |
| 部署 | 谁跑 relayer、许可谁开通道是部署对象 |
| 经济 | 通道无所知；应用逻辑（如托管）必须与 send 原子 |

**推断：** 产品句若只写「开了 IBC」，读者会把通讯录听成已经汇款。  
**建议：** 不确定第一版可以不装 IBC。若对照，必须点名停在哪一层。不要抄握手超时。不要写怎样构造包或嵌套 ICS-20。

---

## 6. 和另外几句不是同一句

1. **ack 必须确定**（不变量 77）：确认字节。本页是对象分层。
2. **超时挂钩 ≠ 已原子**（不变量 78）：ibc-hooks 重入。本页不是中间件。
3. **ICS-23 验绿 ≠ 叶子在树里**（不变量 79）：证明语言。本页不是 soundness。
4. **提交 ≠ 兑付**（不变量 9）：租户根进房东头。本页是 IBC 四层，不是 rollup 桥。
5. **轻客户端不是结算角色**（不变量 20）：CometBFT 跳过。本页的 ICS-02 客户端是 IBC 对象，仍不是已经送包。
6. **XCM preserve_origin**（不变量 113）：另一套跨共识消息。不要糊成「都是跨链」。

不要把握手步数、超时高度、ibc-go 版本抄进不确定常量。不要写怎样构造包、怎样扣包、怎样嵌套 ICS-20。不编博物馆页。不另写 19 节。ICS-20 代币机见 [托管 ≠ 铸券](worked-example-escrow-vs-voucher.md)（不变量 155）。通道升级、WASM 客户端标成另一对象。

---

## 7. 「不确定」测试句（建议）

```text
轻客户端 ≠ 已经开连接
连接 ≠ 已经开通道
通道 ≠ 已经送达数据包
通道对载荷无所知 ≠ 已经 ICS-20 兑付
send 写下承诺 ≠ 对岸已经 recv
relayer 还没提交 ≠ 高度已经停
```

语料：[C150](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「开了 IBC = 钱已经到。」「有 client = 已经能汇款。」「connection OPEN = 通道已经在送。」「send 绿了 = 对岸已经收。」  
**边界：** 不讲某一版 ibc-go 的 keeper 函数表。不抄握手超时。不另写 19 节。不写怎样构造包。ICS-20 代币机见不变量 155。hooks / ICS-23 / 通道升级另标。
