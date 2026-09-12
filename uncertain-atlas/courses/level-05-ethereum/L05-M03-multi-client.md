# L5.3 多客户端：实现保证被逼到台面上

优先级：必学  
先修：L5.1，L1.4，L0.8

---

## A. 先修知识

五层保证里，**实现保证**常被一句「开源了」打发。  
Ethereum 故意让多个独立团队实现同一规范。这不是品味，是假设：一个客户端的 bug 不该等于全网跟着错。

---

## B. 核心问题

**两个客户端怎么保证对同一块算出同一状态根？若算不同，是协议坏了还是实现坏了？测试绿了够不够？**

---

## C. 直觉（ELI15）

同一张乐谱，两个乐团必须奏出能对上的音。  
若对不上：

- 可能谱印错了（规范含糊）——这是协议/规范事故。
- 可能一个乐团看错小节（实现 bug）——这是实现事故。
- 可能有人用了自己的节拍器（本地时间进共识）——这是实现偷运非确定输入。

多乐团的好处：一个乐团集体食物中毒，音乐会还能演。  
坏处：谱必须精确到可怕；否则「多样性」变成「合法地分裂」。

---

## D. 正式定义

**多客户端纪律（事实级描述）**

对同一 canonical 载荷：

```text
Client_A.Apply(S, B) .state_root  ==  Client_B.Apply(S, B) .state_root
```

这是实现保证的可观测断言。它不是密码学定理。

**规范必须可执行或可差分**

含糊的黄皮书段落会变成两家各自「合理」的实现。  
Ethereum 用可执行规范、测试向量、hive 类套件、客户端交叉跑同一块，把分歧从「主网才炸」往前推。

**多样性的安全论点（推断，需用份额与相关失效来检验）**

若超半数验证者跑同一有 bug 的客户端，多样性名存实亡。  
协议允许的多样性 ≠ 部署上真的多样。

**测试通过 ≠ 协议安全（本目标铁律）**

差分测试抓住「两实现不一致」。它不证明：

- 规范本身没有通胀洞；
- 经济假设成立；
- RPC 没骗人。

看见协议自己写死的 RLP 编码硬帽，不是已经改了气限，也不是已经修了各家出块通道尺寸。Sepolia 那次是 Engine API 沿用 HTTP 上限（不变量 96）。EIP-7934 是另一道、独立于气的编码谓词。精读：[`../../tracks/implementation/worked-example-rlp-cap-vs-gas.md`](../../tracks/implementation/worked-example-rlp-cap-vs-gas.md)（不变量 202）。看见单笔气帽不是已经改了块气限，也不是已经是通道尺寸。精读：[`../../tracks/implementation/worked-example-tx-gas-cap-vs-block.md`](../../tracks/implementation/worked-example-tx-gas-cap-vs-block.md)（不变量 203）。看见对等节点宣布历史窗不是已经改了共识历史；线上收据没有布隆不是已经改了共识收据编码；换线协议版本不是已经硬分叉。精读：[`../../tracks/network/worked-example-history-window-vs-consensus.md`](../../tracks/network/worked-example-history-window-vs-consensus.md)（不变量 207）。看见分叉配置 RPC 对上了不是已经过多客户端同根；看见 current / next / last 不是已经改了共识；RPC 绿不是对等节点没有撒谎。精读：[`../../tracks/implementation/worked-example-config-rpc-vs-aligned.md`](../../tracks/implementation/worked-example-config-rpc-vs-aligned.md)（不变量 210）。看见客户端默认气限不是已经是协议帽，也不是已经是通道尺寸。精读：[`../../tracks/implementation/worked-example-default-gas-vs-cap.md`](../../tracks/implementation/worked-example-default-gas-vs-cap.md)（不变量 211 ≠ 203 ≠ 96）。

---

## E. 最小案例

块 B 含一笔边界 gas 的预编译调用。

- 客户端 A：gas 扣 3200，成功。
- 客户端 B：gas 扣 3199，out of gas。

状态根分叉。两边都认为自己忠于「印象中的规范」。  
修复：规范钉死数字 + 回归向量 + 两家齐发补丁。  
在补丁之前，选哪边是社会/部署协调，不是「链自动知道谁对」。

历史方向（须回官方 postmortem 再填七问）：共识客户端分歧导致最终性或头异常。本课不编日期与根因。

---

## F. 真实项目

执行层：geth、nethermind 等。共识层：lighthouse、prysm 等。  
对照：Bitcoin Core 实际单实现文化更重；CometBFT 也有多语言实现压力。  
「不确定」要偷的是纪律，不是客户端名单。

---

## G. 源码入口

预告：

1. 共识/执行测试向量目录。
2. 状态根计算与校验。
3. 差分测试如何喂同一创世与同一块。

先读一条失败向量，再读实现。

---

## H. 攻击者模型

- 专找未覆盖的预编译/边界 gas。
- 让少数派客户端看起来「有问题」从而把份额赶回一家（社会）。
- 规范模糊处写一篇博客当权威（资料优先级：规范 > 源码 > 博客）。

---

## I. 代价

| 得到 | 换 |
|---|---|
| 单实现灭绝风险下降 | 规范必须硬；升级要多团队协调 |
| 实现 bug 更早暴露 | 工程税高 |
| 「规范是真的」 | 不能靠口头共识改行为 |

---

## J. 对「不确定」的意义

**强烈建议研究。** 后量子结算一旦上主网，验签与编码的一点点不一致就是裂链。  
第一版甚至可以先只有一个客户端，但必须从第一天留下：

- 可执行的 `Apply` 规范；
- 状态根断言；
- 「第二个实现必须能对上」的位置。

模式库：[multi-client-determinism](../../libraries/design-patterns/multi-client-determinism.md)。  
博物馆（官方 postmortem，不是方法空话）：[`../../tracks/failure-museum/cve-2021-39137.md`](../../tracks/failure-museum/cve-2021-39137.md)。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | 编码 / 哈希域必须相同，否则「都验签」仍裂 |
| 协议 | 可执行的 `Apply` 规范 |
| 实现 | 多客户端同根；绿测试 ≠ 差分完备 |
| 部署 | 多数客户端停机是部署集中 |
| 经济 | 客户端多样性成本 vs 单实现垄断 |

**禁止假学习：** 「开源了所以实现正确。」「测试绿了所以两客户端不会分叉。」「客户端多所以一定去中心。」「看见协议编码帽 = 已经修了各家通道尺寸。」「7934 = 96。」「看见单笔气帽 = 已经改了块气。」「7825 = 96。」「看见对等窗 = 共识已删历史。」「线上无布隆 = 共识收据已改。」「去掉总难度 = 已判断同步。」「7642 = 硬分叉。」「7642 = 23。」「看见配置 RPC 对上 = 已经同根。」「看见 current / next / last = 共识已改。」「RPC 绿 = 没人撒谎。」「7910 = 149。」「7910 = 209。」「7910 = 207。」「看见默认气限 = 已经是协议帽。」「7935 = 203。」「7935 = 96。」  
**边界：** 不写市场份额。已归档实现案：CVE-2021-39137；单笔低于入池上限 ≠ 拼块已被所有客户端接受：[`../../tracks/failure-museum/ethereum-2024-03-sepolia-engine-rpc.md`](../../tracks/failure-museum/ethereum-2024-03-sepolia-engine-rpc.md)（不变量 96）。看见 RLP 编码硬帽 ≠ 已经改了气限，也不是已经是通道尺寸：[`../../tracks/implementation/worked-example-rlp-cap-vs-gas.md`](../../tracks/implementation/worked-example-rlp-cap-vs-gas.md)（不变量 202）。看见单笔气帽 ≠ 已经改了块气限，也不是已经是通道尺寸：[`../../tracks/implementation/worked-example-tx-gas-cap-vs-block.md`](../../tracks/implementation/worked-example-tx-gas-cap-vs-block.md)（不变量 203）。看见对等节点宣布历史窗 ≠ 已经改了共识历史：[`../../tracks/network/worked-example-history-window-vs-consensus.md`](../../tracks/network/worked-example-history-window-vs-consensus.md)（不变量 207）。看见分叉配置 RPC 对上了 ≠ 已经过多客户端同根：[`../../tracks/implementation/worked-example-config-rpc-vs-aligned.md`](../../tracks/implementation/worked-example-config-rpc-vs-aligned.md)（不变量 210）。看见客户端默认气限 ≠ 已经是协议帽，也不是已经是通道尺寸：[`../../tracks/implementation/worked-example-default-gas-vs-cap.md`](../../tracks/implementation/worked-example-default-gas-vs-cap.md)（不变量 211）。Engine API `VALID` ≠ 已经改规范头：[`../../tracks/finality/worked-example-processed-vs-forkchoice.md`](../../tracks/finality/worked-example-processed-vs-forkchoice.md)（不变量 149）。块 gas 上限 ≠ 墙钟已有界：[`../../tracks/failure-museum/ethereum-2021-05-state-gas-not-time.md`](../../tracks/failure-museum/ethereum-2021-05-state-gas-not-time.md)（不变量 101）。OOG 结束 ≠ 空账户删除已回滚：[`../../tracks/failure-museum/ethereum-2016-11-oog-empty-account.md`](../../tracks/failure-museum/ethereum-2016-11-oog-empty-account.md)（不变量 103）。子群过了 ≠ 点已经在曲线上：[`../../tracks/failure-museum/cve-2025-30147.md`](../../tracks/failure-museum/cve-2025-30147.md)（不变量 116）。精读：[`../../tracks/implementation/worked-example-encoding.md`](../../tracks/implementation/worked-example-encoding.md)。跨链 ack JSON 不是已经确定：[`../../tracks/failure-museum/isa-2025-001.md`](../../tracks/failure-museum/isa-2025-001.md)。
