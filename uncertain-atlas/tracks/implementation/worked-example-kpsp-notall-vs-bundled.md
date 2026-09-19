# 例：看见脚本路径不是已经揭开全部脚本不是已经揭开全部脚本；看见scriptpath spend is not already revealing all scripts不是已经是不变量 189；看见脚本路径不是已经揭开全部脚本不是已经是不变量 152

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki)（Taproot: SegWit version 1 spending rules）。  
**对应课文**：[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)。  
**不要写进**：`index/03` 共识行、M3.7、L3.7。本页是「BIP-341 scriptpath not already all-scripts-exposed / not already 189 / not already 152 正式三事（153 余量）/ not 1555 kpsp-notall interchangeable / not 153 keypath-vs-scriptpath bundled interchangeable」，不是 keypath vs scriptpath bundled（153），也不是已经 脚本路径≠已是tapscript语义（189），也不是已经 txid≠wtxid（152）。不要另写 怎样藏一条别人看不见的脚本路径。

## 官方三件事

1. **看见脚本路径不是已经揭开全部脚本 / 看见脚本路径不是已经揭开全部脚本 这份对象 is not already 已经揭开全部脚本 interchangeable，也不是已经 keypath vs scriptpath bundled（153） interchangeable / 1555 kpsp-notall interchangeable / 1554 kpsp-notree interchangeable，也不是已经 BIP-341 scriptpath not already all-scripts-exposed / not already 189 / not already 152 正式三事 bundled（153 item 2 余量） interchangeable / 153 kpsp item 2 interchangeable。**  
   官方把脚本路径不是已经揭开全部脚本和已经揭开全部脚本写成两件。看见脚本路径不是已经揭开全部脚本，不是已经揭开全部脚本。

2. **看见scriptpath spend is not already revealing all scripts / 看见脚本路径不是已经揭开全部脚本 / 这份对象 is not already 已经是不变量 189 interchangeable，也不是已经 keypath vs scriptpath bundled（153） interchangeable / 1555 kpsp-notall interchangeable / 1556 kpsp-notlook interchangeable，也不是已经 脚本路径≠已是tapscript语义 interchangeable / 189 脚本路径≠已是tapscript语义 interchangeable。**  
   官方把scriptpath spend is not already revealing all scripts和已经是不变量 189写成两件。看见scriptpath spend is not already revealing all scripts，不是已经是不变量 189。

3. **看见脚本路径不是已经揭开全部脚本 / 看见scriptpath spend is not already revealing all scripts / 这份对象 is not already 已经是不变量 152 interchangeable，也不是已经 keypath vs scriptpath bundled（153） interchangeable / 1555 kpsp-notall interchangeable / 1554 kpsp-notree interchangeable，也不是已经 txid≠wtxid interchangeable / 152 txid≠wtxid interchangeable。**  
   官方把脚本路径不是已经揭开全部脚本和已经是不变量 152写成两件。看见脚本路径不是已经揭开全部脚本，不是已经是不变量 152。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样藏一条别人看不见的脚本路径。

## 官方为什么这样拆

- **脚本路径不是已经揭开全部脚本 interchangeable：官方写 Merkle 枝只把实际执行的那一支脚本揭到链上。**
- **看见本页不是已经是不变量 189。**
- **看见本页不是已经是不变量 152。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经揭开全部脚本 | 不是已经揭开全部脚本 | 不是已经脚本路径≠已是tapscript语义（189） |
| 已经是不变量 189 | 不是已经是不变量 189 | 不是已经txid≠wtxid（152） |
| 已经是不变量 152 | 不是已经是不变量 152 | 不是已经1554 kpsp-notree |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-341 scriptpath not already all-scripts-exposed / not already 189 / not already 152 正式三事（153 余量），必须分开是不是已经揭开全部脚本、是不是已经是不变量 189、是不是已经是不变量 152。可以跳过「看见一个签名所以脚本树已经公开」。不要另写 怎样藏一条别人看不见的脚本路径。153 keypath vs scriptpath bundled unbundling 在本页 item 2 续；续 [`worked-example-kpsp-notlook-vs-bundled.md`](worked-example-kpsp-notlook-vs-bundled.md)（不变量 1556 item 3）。

## 本页不抄

- 控制块长度、叶子版本、annex 字节、NUMS 点。
- 怎样藏一条别人看不见的脚本路径。
