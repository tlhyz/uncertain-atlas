# 失败案：Elderflower 授权代发管道漏掉 ValidateBasic 不是消息已经过认证

层：**协议 + 实现 + 经济**（被代执行的消息仍须过基本校验；不是 vesting 挂到被挡地址，也不是 ValidateBasic 读本地钟）

官方披露（同一事故的两页）：

- 当时公告：[Cosmos-SDK Security Advisory Elderflower](https://forum.cosmos.network/t/cosmos-sdk-security-advisory-elderflower/8584)（2022-12-09，Ethan Buchman）。原文称 **critical**，影响 SDK **v0.44.x / v0.45.x / v0.46.x**。
- 事后复盘：[Dragonberry and Elderflower](https://forum.cosmos.network/t/cosmos-sdk-ibc-vulnerability-retrospective-security-advisories-dragonberry-and-elderflower-october-2022/8735)（2022-12-16）。本页只采用这两页已写出的句子。

补丁打在 Dragonberry 的公开包里：`v0.44.5-patch`、`v0.45.9`、`v0.46.3`。公告：已经打过 Dragonberry 公开补丁的，Elderflower **也已经补上**，不必另做一次。本页不另编 CVE——两页都未给 CVE ID，也没有独立 GHSA。

**事实（官方原文能对上的句子）：**

- Elderflower **起源于 Authz（Cosmos-SDK）**，能绕过消息认证系统的一部分。这条认证旁路**有可能**被升级成通胀、盗窃或其它利用，取决于链自己的实现细节。
- 模块执行消息时，应当用 `ValidateBasic()` 检查消息是否合法。复盘：Authz 的消息校验管道在 v0.44 / 0.45 / 0.46 **漏掉**一次关键的 `ValidateBasic()`。
- 漏掉这次调用，可能造出**无效状态转移**；在「恰好的交易参数」下，**可能**通胀或盗窃。
- 此前的审查没抓住；未发布的 `main` **已经修过**。
- 与 Dragonberry **无关**。发现时多方已独立报到，碰撞风险被视为更高，因此和 Dragonberry 合成一次公开发布。
- 复盘写：这次**没有丢钱**。

亲戚 **Jackfruit**（CVE-2021-41135，另一页）：同一模块里 `ValidateBasic` **读了本地钟**，会非确定停链，资金安全。那是「有检查、检查不该读钟」。本页是「代发管道里检查根本没跑」。

本页不写「恰好的交易参数」是什么、不写怎样绕过认证、不抄 authz、不把「打过 Dragonberry」写成 ICS-23 已修等于认证已修。第一版可以不装授权代发。

## 1. 发生了什么

用户把一张「代我发」的授权交给模块。  
模块替他把里面的消息拿出来执行。  
执行前本该问一句：这张里面的消息自己合法吗？  
这一问被漏掉了。  
里面那张没过基本校验的请求，仍可能被写进状态。  
授权代发不是里面的消息已经过认证。

## 2. 根因

外层授权管道被当成「已经替内层验过了」。  
`ValidateBasic` 写在模块说明书上，不等于代发路径每次都会调用。  
未发布的主干修好了，发布线还漏着——「我看过 main」不是这条线已经补。

这不是：

| 案 | 对象 |
|----|------|
| 不变量 75 / ASA-2024-003 | 未初始化被挡账户不是可 vesting / authz 的地址 |
| 不变量 77 / ISA-2025-001 | 跨链 ack JSON 反序列化必须确定 |
| 不变量 79 / Dragonberry | ICS-23 验绿 ≠ 叶子已在原树（同一天发布，另一对象） |
| 不变量 82 / Jackfruit | `ValidateBasic` 读本地钟 ≠ 已确定 |
| 本页 | **授权代发管道漏掉 ValidateBasic ≠ 内层消息已认证；无效转移不是「授权过了就合法」** |

## 3. 被破坏的 invariant

- 被代执行的消息必须仍过 `ValidateBasic`（不变量 81）
- 授权代发不是内层消息已经认证
- 打过同一天的 ICS-23 补丁，不是这条认证谓词已齐——除非用的就是把两洞打在一起的那次发布

## 4. 为什么测试没发现

幸福路径：代发的是已经自己合法的消息，外层绿、内层也绿。  
只测「授权能替人转一笔正常账」会绿，看不见「内层没跑 ValidateBasic」。  
主干修好了，旧发布线的测试仍按旧管道绿。

## 5. 修复

官方：升到含 Elderflower 的 Dragonberry 公开包。已经打过那次公开补丁的，不必另做。  
未打过的，公告要联系 security@interchain.io——私下渠道不是本页内容。  
「我升过 Dragonberry 相关依赖」必须点名是不是那三个公开标签；只换 ics23 replace 不是本条已补。

## 6. 「不确定」若同类

1. 第一版可以不装授权代发 / authz 类管道。
2. 若装：外层授权执行内层消息时，内层必须再跑与直接投递相同的基本校验。授权过了 ≠ 内层已合法。
3. 发布线与主干必须分开审。`main` 已修不是旧线已修。
4. 同一天打包发布不是同一谓词。Dragonberry 的 ics23 replace 不是本条。
5. 这和被挡账户（75）、ack 确定性（77）、ICS-23 soundness（79）、ValidateBasic 读钟（82）不是同一句。
6. 不要抄 authz。不要写「恰好的交易参数」。

## 7. 回归测试

形状（不是利用包）：文案把授权代发写成内层消息已过 `ValidateBasic` 必须红。代发路径跳过基本校验仍标 PASS 必须红。只测打过 ics23 replace、未点名 Elderflower 发布标签仍标「认证已修」必须红。

**事实来源：** [Elderflower 公告](https://forum.cosmos.network/t/cosmos-sdk-security-advisory-elderflower/8584)；[官方复盘](https://forum.cosmos.network/t/cosmos-sdk-ibc-vulnerability-retrospective-security-advisories-dragonberry-and-elderflower-october-2022/8735)。
