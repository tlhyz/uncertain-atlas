# 失败案：preserve_origin 为真不是出站已经带了改 origin 的指令；静默跳过不是 BadOrigin

层：**协议 + 实现**（`InitiateTransfer` 在本地 origin 已被清掉时仍标 `preserve_origin`；既不别名也不再清；目的地用运输发送者当 origin；Asset Hub 被配成中继 superuser 时，已签名账户可当中继 root）

官方披露：

- Polkadot 论坛官方复盘：[Postmortem: XCM InitiateTransfer Origin Leak](https://forum.polkadot.network/t/postmortem-xcm-initiatetransfer-origin-leak/17357)（2026-03-19）。本页只采用该文已写出的句子。无 CVE。官方写未利用。

**事实（官方原文能对上的句子）：**

- 漏洞赏金报告：任意账户可经 XCM 冒充任意链。在 Asset Hub 上，对许多链等于 root。一般则能摸到各链的主权账户。
- 官方：本地 origin 已被清掉之后，再发标了 `preserve_origin` 的 `InitiateTransfer`，出站消息既不带 `AliasOrigin` 也不带 `ClearOrigin`。目的地用 HRMP/UMP **运输发送者**当 origin，再跑用户给的后续指令。
- 官方：中继把 Asset Hub 配成 `LocationAsSuperuser` 时，Asset Hub 上任意已签名账户可对中继发任意调用当 root。也可冒充本链，拿走该链在别链上的主权账户资金。
- 这是修另一件安全问题（`UnpaidExecution` 排序绕过手续费）的回归。改之前：`preserve_origin` 为真且 origin 为空会回 `XcmError::BadOrigin`。改之后：`if let Some` 静默失败，什么也不推。
- 原始 XCMv5 经过评审与审计。引入本洞的是审计之后的热修，也按惯例评审过，仍没抓住。官方：不诚实路径，系统链与社区链都没踩到；只存在于 XCMv5，多数链迁得慢。模糊测试生成的 XCM 单独不成事，必须再送到另一条链。
- 系统平行链、Polkadot、Kusama 与生态团队已打补丁。官方写未发现利用痕迹。

本页不写怎样拼跨链指令、不抄平行链编号 / 版本 / 行号 / 时间线进不确定常量。`preserve_origin` 为真，不是出站已经带了改 origin 的指令。

## 1. 发生了什么

本地门口的身份牌已经被摘掉。  
出发时还写着：把身份牌带到对岸。  
对岸信封里既没有新牌，也没有「无牌」印章。  
对岸只看见运货车的门牌。  
运货车若被配成超级用户，车上任何人都能用那块门牌。  
摘掉本地牌，不是对岸已经知道你是谁。  
写着保留，不是信封已经写了保留。

## 2. 根因

「保留 origin」与「当前 origin 还在」是两个对象。  
保留为真、当前为空时，必须失败关闭，不得静默什么都不写。  
改 origin 的指令只有两种：别名，或再清一次。两条都不写，目的地只能退回运输发送者。  
运输发送者是另一信任对象。配成 superuser，不是已签名用户已经不能当 root。  
修费绕过的热修，把 BadOrigin 改成跳过，不是后继已经更安全。

这不是：

| 案 | 对象 |
|----|------|
| 不变量 9 | 租户根被包含 ≠ 桥可兑付；本页是出站 origin 指令缺失 |
| 不变量 77 / 78 | IBC 确认 / 超时挂钩；本页是 XCM 执行器 |
| 不变量 81 | 授权代发漏内层校验；本页是跨共识消息的 origin 栏 |
| 不变量 97 | 解码深度套错对象；本页是 origin 谓词 |
| 本页 | **preserve_origin 为真 ≠ 出站已经带了改 origin 的指令；静默跳过 ≠ BadOrigin；目的地用运输发送者 ≠ 用户 origin 已经清掉** |

## 3. 被破坏的 invariant

- 跨共识消息若提供「保留 origin」，当前 origin 为空必须失败关闭，不得静默省略别名与再清（不变量 113）
- 运输发送者不得在缺 origin 指令时自动升成目的地权限
- 修相邻安全洞不得把显式错误改成跳过

## 4. 为什么测试没发现

幸福路径：本地 origin 还在，保留则别名，不保留则再清。  
绿测试与审计覆盖 XCMv5 主路径和费绕过热修。  
边角要：本地 origin 已空 + 保留为真，出站是否仍带一条确定的改 origin 指令；送到另一条链、目的地是否用运输发送者。  
官方：单链模糊测试看不见跨链效果。

## 5. 修复

官方：执行器补丁后，该组合不再把运输发送者交给用户后续指令。  
系统平行链与中继经治理升级。生态链另行打补丁。  
过程：跨链模糊、按主题的不变量清单、安全仓。那些是过程建议，不是谓词已齐。

## 6. 「不确定」若同类

1. 第一版可以不做 XCM / 跨共识消息 / 主权账户 / LocationAsSuperuser。
2. 若做跨链消息：保留 origin 的旗标必须对应一条确定的出站指令；当前 origin 为空必须失败关闭。
3. 运输发送者是另一信任对象。配成 superuser 必须写成「该跳上的任何已签名用户」。
4. 修相邻洞不得把显式错误改成静默跳过。单链测试绿不是跨链效果已覆盖。
5. 这和提交≠兑付（9）、IBC 确认（77）、授权代发（81）、解码深度（97）不是同一句。
6. 不要写怎样拼指令。不要抄平行链编号 / 版本 / 行号。

## 7. 回归测试

形状（不是利用包）：文案把 `preserve_origin` 写成出站已经带了改 origin 的指令必须红。把静默跳过写成 BadOrigin 必须红。把目的地用运输发送者写成用户 origin 已经清掉必须红。把 Asset Hub 配成 superuser 写成已签名账户不能当中继 root 必须红。与 9 / 81 糊成「跨链授权」一句必须红。

**事实来源：** [Polkadot 论坛 2026-03-19 XCM origin leak 复盘](https://forum.polkadot.network/t/postmortem-xcm-initiatetransfer-origin-leak/17357)。
