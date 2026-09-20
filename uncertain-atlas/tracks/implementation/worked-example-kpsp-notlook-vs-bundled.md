# 例：看见看见Taproot输出不是已经分辨付款给钥还是付款给脚本不是已经分辨付款给钥还是付款给脚本；看见seeing a Taproot output is not already telling whether it pays to key or to script不是已经是不变量 170；看见看见Taproot输出不是已经分辨付款给钥还是付款给脚本不是已经是不变量 174

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki)（Taproot: SegWit version 1 spending rules）。  
**对应课文**：[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)。  
**不要写进**：`index/03` 共识行、M3.7、L3.7。本页是「BIP-341 taproot-output not already look-pubkey-or-script / not already 170 / not already 174 正式三事（153 余量）/ not 1556 kpsp-notlook interchangeable / not 153 keypath-vs-scriptpath bundled interchangeable」，不是 keypath vs scriptpath bundled（153），也不是已经 哈希≠已揭开赎回（170），也不是已经 地址≠已有输出（174）。不要另写 怎样藏一条别人看不见的脚本路径。

## 官方三件事

1. **看见看见Taproot输出不是已经分辨付款给钥还是付款给脚本 / 看见看见Taproot输出不是已经分辨付款给钥还是付款给脚本 这份对象 is not already 已经分辨付款给钥还是付款给脚本 interchangeable，也不是已经 keypath vs scriptpath bundled（153） interchangeable / 1556 kpsp-notlook interchangeable / 1554 kpsp-notree interchangeable，也不是已经 BIP-341 taproot-output not already look-pubkey-or-script / not already 170 / not already 174 正式三事 bundled（153 item 3 余量） interchangeable / 153 kpsp item 3 interchangeable。**  
   官方把看见Taproot输出不是已经分辨付款给钥还是付款给脚本和已经分辨付款给钥还是付款给脚本写成两件。看见看见Taproot输出不是已经分辨付款给钥还是付款给脚本，不是已经分辨付款给钥还是付款给脚本。

2. **看见seeing a Taproot output is not already telling whether it pays to key or to script / 看见看见Taproot输出不是已经分辨付款给钥还是付款给脚本 / 这份对象 is not already 已经是不变量 170 interchangeable，也不是已经 keypath vs scriptpath bundled（153） interchangeable / 1556 kpsp-notlook interchangeable / 1555 kpsp-notall interchangeable，也不是已经 哈希≠已揭开赎回 interchangeable / 170 哈希≠已揭开赎回 interchangeable。**  
   官方把seeing a Taproot output is not already telling whether it pays to key or to script和已经是不变量 170写成两件。看见seeing a Taproot output is not already telling whether it pays to key or to script，不是已经是不变量 170。

3. **看见看见Taproot输出不是已经分辨付款给钥还是付款给脚本 / 看见seeing a Taproot output is not already telling whether it pays to key or to script / 这份对象 is not already 已经是不变量 174 interchangeable，也不是已经 keypath vs scriptpath bundled（153） interchangeable / 1556 kpsp-notlook interchangeable / 1554 kpsp-notree interchangeable，也不是已经 地址≠已有输出 interchangeable / 174 地址≠已有输出 interchangeable。**  
   官方把看见Taproot输出不是已经分辨付款给钥还是付款给脚本和已经是不变量 174写成两件。看见看见Taproot输出不是已经分辨付款给钥还是付款给脚本，不是已经是不变量 174。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样藏一条别人看不见的脚本路径。

## 官方为什么这样拆

- **看见Taproot输出不是已经分辨付款给钥还是付款给脚本 interchangeable：官方写 Taproot 输出钥与脚本条件不可分辨。**
- **看见本页不是已经是不变量 170。**
- **看见本页不是已经是不变量 174。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经分辨付款给钥还是付款给脚本 | 不是已经分辨付款给钥还是付款给脚本 | 不是已经哈希≠已揭开赎回（170） |
| 已经是不变量 170 | 不是已经是不变量 170 | 不是已经地址≠已有输出（174） |
| 已经是不变量 174 | 不是已经是不变量 174 | 不是已经1554 kpsp-notree |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-341 taproot-output not already look-pubkey-or-script / not already 170 / not already 174 正式三事（153 余量），必须分开是不是已经分辨付款给钥还是付款给脚本、是不是已经是不变量 170、是不是已经是不变量 174。可以跳过「看见一个签名所以脚本树已经公开」。不要另写 怎样藏一条别人看不见的脚本路径。153 keypath vs scriptpath bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的官方对象：tapscript-vs-scriptpath（189）。

## 本页不抄

- 控制块长度、叶子版本、annex 字节、NUMS 点。
- 怎样藏一条别人看不见的脚本路径。
