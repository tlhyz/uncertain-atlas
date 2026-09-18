# 例：看见 pk 不是已经是 pkh 那种放置；看见写了脚本表达式不是已经能再套一层 sh；看见 pk 可以出现在任何一层不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-381](https://github.com/bitcoin/bips/blob/master/bip-0381.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-381 pk-placement not already pkh-place / not already sh-only-top / not already settled 正式三事（276 余量）/ not 1148 pk381-notplace interchangeable / not 276 pk-vs-toplevel bundled interchangeable」，不是非隔离见证描述符 bundled（276），也不是看见描述符就已经是地址（184），也不是 tr 没有树就已经有脚本路径（1145）。不要另写怎样拼 P2PK。

## 官方三件事

1. **看见 pk / 看见写在某一层 这份栏 is not already 已经是 pkh 那种放置 interchangeable，也不是已经非隔离见证描述符 bundled（276） interchangeable / 1148 pk381-notplace interchangeable / 1149 pk381-notredeem interchangeable / 276 pk item 2 sh-not-redeem interchangeable，也不是已经 BIP-381 pk-placement not already pkh-place / not already sh-only-top / not already settled 正式三事 bundled（276 item 1 余量） interchangeable / 276 pk item 1 interchangeable。**  
   官方把 `pk` 写成可以出现在任何上下文或任何一层，把 `pkh` 写成可以当顶层也可以套进 `sh` 或 `wsh`。看见写了 `pk`，不是已经是 `pkh` 那种放置。

2. **看见写了脚本表达式 / 看见 pk / 这份栏 is not already 已经能再套一层 sh interchangeable，也不是已经非隔离见证描述符 bundled（276） interchangeable / 1148 pk381-notplace interchangeable / 276 pk item 3 familiar-not-compat interchangeable / 1150 pk381-notcompat interchangeable，也不是已经看见描述符就已经是地址 interchangeable / 184 descriptor interchangeable。**  
   官方把 `sh` 写成只能当顶层。看见写了脚本表达式，不是已经能再套一层 `sh`。看见写了 `pk`，不是已经能套进任意外层。

3. **看见 pk 可以出现在任何一层 / 看见 pk / 这份栏 is not already 已经交差 interchangeable，也不是已经非隔离见证描述符 bundled（276） interchangeable / 1148 pk381-notplace interchangeable / 1149 pk381-notredeem interchangeable，也不是已经 tr 没有树就已经有脚本路径 interchangeable / 1145 tr386-notpath interchangeable。**  
   官方把三种表达式的出现位置写成三套规则。看见 `pk` 可以出现在任何一层，不是已经交差。

脚本模板、测试向量、例钥、十六进制脚本是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **pk 不是已经是 pkh 那种放置：** 官方把 pk 和 pkh 的出现位置写成两套。
- **写了脚本表达式 不是已经能再套一层 sh：** 官方把 sh 写成只能顶层。
- **pk 可以出现在任何一层 不是已经交差：** 官方把三套放置写成三句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 放置 | 不是已经是 pkh 那种放置 | 不是已经是地址（184） |
| 再套 sh | 不是已经能再套一层 | 不是已经有赎回脚本（1149） |
| 交差 | 不是已经交差 | 不是 tr 没有树就已经有脚本路径（1145） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-381 pk-placement not already pkh-place / not already sh-only-top / not already settled 正式三事（276 余量），必须分开是不是已经是 pkh 那种放置、是不是已经能再套一层 sh、是不是已经交差。可以跳过「看见熟悉脚本就已经能互操作」。不要另写怎样拼 P2PK。276 pk vs toplevel bundled unbundling 在本页 item 1 启动；续 [`worked-example-pk381-notredeem-vs-bundled.md`](worked-example-pk381-notredeem-vs-bundled.md)（不变量 1149 item 2）。

## 本页不抄

- 脚本模板、测试向量、例钥、十六进制脚本。
- 怎样算 HASH160、怎样拼赎回、怎样嵌套。
