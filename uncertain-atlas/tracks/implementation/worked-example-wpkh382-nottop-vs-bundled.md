# 例：看见 wpkh / wsh 不是已经只能顶层；看见能套进 sh 不是已经能再套进 wsh；看见写了隔离见证表达式不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-382](https://github.com/bitcoin/bips/blob/master/bip-0382.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-382 wpkh-wsh not already toplevel-only / not already nestable-in-wsh / not already settled 正式三事（277 余量）/ not 1151 wpkh382-nottop interchangeable / not 277 wpkh-vs-compressed bundled interchangeable」，不是隔离见证描述符 bundled（277），也不是 381 那种 sh 只能顶层（1148），也不是同一套 BIP44 账户已经能找回嵌套（1124）。不要另写怎样拼见证程序。

## 官方三件事

1. **看见 wpkh / 看见 wsh 这份栏 is not already 已经只能顶层 interchangeable，也不是已经隔离见证描述符 bundled（277） interchangeable / 1151 wpkh382-nottop interchangeable / 1152 wpkh382-notuncomp interchangeable / 277 wpkh item 2 key-not-uncomp interchangeable，也不是已经 BIP-382 wpkh-wsh not already toplevel-only / not already nestable-in-wsh / not already settled 正式三事 bundled（277 item 1 余量） interchangeable / 277 wpkh item 1 interchangeable。**  
   官方写：`wpkh` 可以当顶层，也可以套进 `sh`。`wsh` 可以当顶层，也可以套进 `sh`。看见写了隔离见证表达式，不是已经是 381 那种 `sh` 只能顶层。

2. **看见能套进 sh / 看见 wpkh / 这份栏 is not already 已经能再套进 wsh interchangeable，也不是已经隔离见证描述符 bundled（277） interchangeable / 1151 wpkh382-nottop interchangeable / 277 wpkh item 3 wsh-not-wit interchangeable / 1153 wpkh382-notwit interchangeable，也不是已经 381 那种 sh 只能顶层 interchangeable / 1148 pk381-notplace interchangeable。**  
   官方把两种表达式都写成可以顶层或套进 `sh`。看见能套进 `sh`，不是已经能再套进 `wsh`。

3. **看见写了隔离见证表达式 / 看见 wpkh / 这份栏 is not already 已经交差 interchangeable，也不是已经隔离见证描述符 bundled（277） interchangeable / 1151 wpkh382-nottop interchangeable / 1152 wpkh382-notuncomp interchangeable，也不是已经同一套 BIP44 账户已经能找回嵌套 interchangeable / 1124 nest49-notold interchangeable。**  
   官方把两种表达式的出现位置写成可以顶层或套进 `sh`。看见写了隔离见证表达式，不是已经交差。

脚本模板、测试向量、例钥、十六进制脚本是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **wpkh / wsh 不是已经只能顶层：** 官方把两种表达式都写成可以顶层或套进 sh。
- **能套进 sh 不是已经能再套进 wsh：** 官方没有写成可以再套进 wsh。
- **写了隔离见证表达式 不是已经交差：** 官方把放置写成两套，不是一句交差。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 放置 | 不是已经只能顶层 | 不是已经是 381 那种只能顶层（1148） |
| 再套 wsh | 不是已经能再套进 wsh | 不是已经有见证脚本（1153） |
| 交差 | 不是已经交差 | 不是已经能找回嵌套账户（1124） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-382 wpkh-wsh not already toplevel-only / not already nestable-in-wsh / not already settled 正式三事（277 余量），必须分开是不是已经只能顶层、是不是已经能再套进 wsh、是不是已经交差。可以跳过「看见隔离见证表达式就已经是 381 那套放置」。不要另写怎样拼见证程序。277 wpkh vs compressed bundled unbundling 在本页 item 1 启动；续 [`worked-example-wpkh382-notuncomp-vs-bundled.md`](worked-example-wpkh382-notuncomp-vs-bundled.md)（不变量 1152 item 2）。

## 本页不抄

- 脚本模板、测试向量、例钥、十六进制脚本。
- 怎样算 HASH160 / SHA256、怎样拼见证程序、怎样嵌套。
