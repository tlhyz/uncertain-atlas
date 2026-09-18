# 例：看见 wsh 产出不是已经有见证脚本；看见 381 另造了赎回脚本不是已经是本页这份见证脚本；看见 P2WSH 输出脚本不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-382](https://github.com/bitcoin/bips/blob/master/bip-0382.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-382 wsh-output not already have-witness-script / not already 381-redeem / not already settled 正式三事（277 余量）/ not 1153 wpkh382-notwit interchangeable / not 277 wpkh-vs-compressed bundled interchangeable」，不是隔离见证描述符 bundled（277），也不是 381 那种另造赎回脚本（1149），也不是付给脚本哈希就已经揭开赎回（170）。不要另写怎样拼见证程序。

## 官方三件事

1. **看见 wsh 产出 / 看见 P2WSH 输出脚本 这份栏 is not already 已经有见证脚本 interchangeable，也不是已经隔离见证描述符 bundled（277） interchangeable / 1153 wpkh382-notwit interchangeable / 1151 wpkh382-nottop interchangeable / 277 wpkh item 1 wpkh-not-top interchangeable，也不是已经 BIP-382 wsh-output not already have-witness-script / not already 381-redeem / not already settled 正式三事 bundled（277 item 3 余量） interchangeable / 277 wpkh item 3 interchangeable。**  
   官方写：`wsh` 还会另造一份见证脚本，花费时要用。看见 `wsh` 产出了 P2WSH 输出脚本，不是已经把见证脚本交出来。

2. **看见 381 另造了赎回脚本 / 看见 wsh 产出 / 这份栏 is not already 已经是本页这份见证脚本 interchangeable，也不是已经隔离见证描述符 bundled（277） interchangeable / 1153 wpkh382-notwit interchangeable / 277 wpkh item 2 key-not-uncomp interchangeable / 1152 wpkh382-notuncomp interchangeable，也不是已经 381 那种另造赎回脚本 interchangeable / 1149 pk381-notredeem interchangeable。**  
   官方随后把参数那条脚本表达式产出的输出脚本叫做这份赎回脚本。看见 381 另造了赎回脚本，不是已经是本页这份见证脚本。

3. **看见 P2WSH 输出脚本 / 看见 wsh 产出 / 这份栏 is not already 已经交差 interchangeable，也不是已经隔离见证描述符 bundled（277） interchangeable / 1153 wpkh382-notwit interchangeable / 1151 wpkh382-nottop interchangeable，也不是已经付给脚本哈希就已经揭开赎回 interchangeable / 170 hash interchangeable。**  
   官方把输出脚本和另造的见证脚本写成两份对象。看见 P2WSH 输出脚本，不是已经交差。

脚本模板、测试向量、例钥、十六进制脚本是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **wsh 产出 不是已经有见证脚本：** 官方把输出脚本和见证脚本写成两份。
- **381 赎回脚本 不是已经是本页见证脚本：** 官方把本页另造对象写成见证脚本。
- **P2WSH 输出脚本 不是已经交差：** 官方把两份对象写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 见证脚本 | 不是已经有见证脚本 | 不是已经有 381 赎回（1149） |
| 381 赎回 | 不是已经是本页见证脚本 | 不是已经揭开赎回（170） |
| 交差 | 不是已经交差 | 不是已经只能顶层（1151） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-382 wsh-output not already have-witness-script / not already 381-redeem / not already settled 正式三事（277 余量），必须分开是不是已经有见证脚本、是不是已经是 381 那份赎回脚本、是不是已经交差。可以跳过「看见隔离见证表达式就已经是 381 那套放置」。不要另写怎样拼见证程序。277 wpkh vs compressed bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 脚本模板、测试向量、例钥、十六进制脚本。
- 怎样算 HASH160 / SHA256、怎样拼见证程序、怎样嵌套。
