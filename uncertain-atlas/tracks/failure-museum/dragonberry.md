# 失败案：Dragonberry ICS-23 验通过不是叶子已在原树

层：**密码 + 协议 + 经济**（Merkle 证明语言必须有 soundness；不是超时挂钩重入，也不是 ack JSON 确定性）

官方披露（同一事故的两页，都由核心 Cosmos / Informal / Interchain 署名）：

- 当时公告：[IBC Security Advisory Dragonberry](https://forum.cosmos.network/t/ibc-security-advisory-dragonberry/7702)（2022-10-13，Ethan Buchman）。原文称 **critical**，影响**所有开了 IBC 的 Cosmos 链、所有 IBC 版本**。
- 事后复盘：[Dragonberry and Elderflower](https://forum.cosmos.network/t/cosmos-sdk-ibc-vulnerability-retrospective-security-advisories-dragonberry-and-elderflower-october-2022/8735)（2022-12-16）。本页只采用这两页已写出的句子。

公开补丁入口：Cosmos SDK **v0.45.9**（以及复盘写的 2022-10-14 同日发布线）。公告另写：升 SDK **还必须**在 `go.mod` 加 `confio/ics23` → `cosmos/cosmos-sdk/ics23` 的 replace；**最初贴出的 replace 写错过，随后更正**。本页不另编 CVE——两页都未给 CVE ID。下游产品自己发过 GHSA（例如 cheqd `GHSA-j92c-mmf7-j5x5`），那是回声，不是本条规范出处。

**事实（官方原文能对上的句子）：**

- Dragonberry **起源于 ICS-23（IBC）**，使攻击者能**伪造 IBC 超时**。伪造超时**可以升级成 ICS-20 双花**。
- 发现句：IBC **会接受伪造的缺席证明**（假称某个包没被收到）。
- IBC 超时本是用户可配的：包没被及时中继，可以拿回钱。能伪造「没收到」之后，攻击者可让协议以为**同一笔 transfer 既成功又失败**。
- 复盘写：这可能被用来**迭代抽空所有 ICS-20 托管账户**；当时跨 Cosmos 网络的 IBC 通道里的资金都暴露在这个利用面下。
- ICS-23 是一套描述 Merkle 存在/缺席证明的语言。复盘原文：该语言与规范**缺少 soundness 定义**，因此**有可能**给出一张 ICS-23 存在或缺席证明，而对应对象**并不在原来的 Merkle 树里**。
- 修法：对 ICS-23 **IAVL** 证明的结构加校验，随后拒绝非法证明。
- 公告：一条链在 **⅓ 投票权**打上补丁后，对这条 critical 漏洞「安全」——复盘补了一句机制：过了 +⅓ 之后，再利用会表现为**可见的非确定性停链**；停链比「又能打又能被抽」好。**100%** 打上才算本条完全修完。
- 公告：补丁可以由验证者**各自部署、不必先做一次停链升级**；仍可能在升级过程中停。私下已经打过补丁的，仍须跟上公开版。
- 复盘写：这次**没有丢钱**。

亲戚 **Elderflower**（同一复盘、同一天公开发布，**另页**）：Authz 消息管道漏掉一次 `ValidateBasic()`，不是 ICS-23 soundness。见 [elderflower.md](elderflower.md)。

本页不写怎样伪造缺席证明、不写叶子前缀怎么改、不抄 replace 行当不确定常量、不把 ⅓ 抄进不确定法定人数、不把 CosmWasm / ibc-hooks / 某条主网写成已选。第一版可以不装 IBC。

## 1. 发生了什么

对岸说：这张包我没见过。  
出示一张 ICS-23 缺席证明。本地验绿了。  
超时路径把托管退回去。  
可是对岸其实已经收过、已经把钱放出去了。  
同一笔 transfer 被协议写成既成功又失败。  
托管账户可以被一遍一遍抽。  
验绿不是叶子已在原树。

## 2. 根因

跨链运输把「ICS-23 Verify 通过」当成「原树里真有 / 真没有」。  
描述语言没有 soundness：证明可以在语言里合法，对象却不在那棵树上。  
超时把「没收到」兑成退款，于是假缺席变成双花。

这不是：

| 案 | 对象 |
|----|------|
| 不变量 12 / CVE-2012-2459 | 奇数复制让两个叶列表同根 |
| 不变量 13 / CVE-2019-7167 | `VerifyProof=接受` 不得单独充当供给守恒 |
| 不变量 66 / Alderfly | 朝前 lunatic：验过头 ≠ 已经能交证据 |
| 不变量 77 / ISA-2025-001 | 跨链 ack JSON 反序列化必须确定 |
| 不变量 78 / ASA-2024-007 | OnTimeout 里再跑同一 MsgTimeout ≠ ICS-20 已原子 |
| 不变量 80 / ASA-2023-001 | 升级高度上的进程管理器 ≠ 可信下载通道 |
| 本页 | **ICS-23 验通过 ≠ 叶子已在原树；缺席证明被接受 ≠ 包真的没收到；伪造超时 ≠ ICS-20 已结算** |

## 3. 被破坏的 invariant

- ICS-23 验通过不是叶子已在原来的 Merkle 树（不变量 79）
- 缺席证明被接受不是包真的没收到
- 伪造超时不是 ICS-20 已经结算（不得既成功又失败）

## 4. 为什么测试没发现

幸福路径：证明是从自己那棵 IAVL 树老老实实编出来的，验绿、超时也对。  
只测「超时能退一次钱」会绿，看不见「假缺席让成功和失败同时成立」。  
规范有描述语言、没有 soundness，测试按描述语言写也会绿。

## 5. 修复

官方：对 ICS-23 IAVL 证明结构加校验；升到公开补丁线；**另写** ics23 replace。只升 SDK、不换证明库，不是本条已补。  
最初公开的 replace 写错过，随后更正——「我已经贴过一行 replace」不是已经换对。  
+⅓ 投票权打上之后，再利用会停链可见；那是止血，不是 soundness 已齐。100% 才算修完。  
私下热补 ≠ 公开补丁已跟上。

## 6. 「不确定」若同类

1. 第一版可以不装 IBC / 跨链 Merkle 证明语言。
2. 若装：必须先写 soundness。Verify 绿不得单独充当「对岸没收到」，也不得单独充当「对岸已写入」。
3. 超时兑付必须点名：缺席证明的对象是哪棵树、哪一个包承诺。假缺席不得让同一笔既成功又失败。
4. 升依赖版本不是证明库已经换。replace / 供应商置换必须写成部署谓词。
5. 不要抄 ⅓ 当不确定法定人数。不要把「停链可见」写成已经不能被抽。
6. 这和挂钩重入（78）、ack 确定性（77）、验证明≠供给（13）、同根不同列表（12）不是同一句。
7. Elderflower 是另一对象（Authz 漏 `ValidateBasic`，不变量 81）。不要把「同一天发布」写成同一谓词。不要抄 authz。

## 7. 回归测试

形状（不是利用包）：文案把 ICS-23 Verify 绿写成叶子已在原树、或包真的没收到，必须红。伪造超时仍标 ICS-20 已结算必须红。只升 SDK、未换 ics23 仍标已补必须红。把 +⅓ 打补丁写成 soundness 已齐必须红。

**事实来源：** [IBC Security Advisory Dragonberry](https://forum.cosmos.network/t/ibc-security-advisory-dragonberry/7702)；[官方复盘](https://forum.cosmos.network/t/cosmos-sdk-ibc-vulnerability-retrospective-security-advisories-dragonberry-and-elderflower-october-2022/8735)。
