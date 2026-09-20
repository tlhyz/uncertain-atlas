# 例：看见钥匙路径不是已经揭开有没有脚本树不是已经揭开有没有脚本树；看见keypath spend is not already revealing whether a script tree exists不是已经是不变量 189；看见钥匙路径不是已经揭开有没有脚本树不是已经 153 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki)（Taproot: SegWit version 1 spending rules）。  
**对应课文**：[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)。  
**不要写进**：`index/03` 共识行、M3.7、L3.7。本页是「BIP-341 keypath not already revealed-tree / not already 189 / not already 153-bundled 正式三事（153 余量）/ not 1554 kpsp-notree interchangeable / not 153 keypath-vs-scriptpath bundled interchangeable」，不是 keypath vs scriptpath bundled（153），也不是已经 脚本路径≠已是tapscript语义（189），也不是已经 哈希≠已揭开赎回（170）。不要另写 怎样藏一条别人看不见的脚本路径。

## 官方三件事

1. **看见钥匙路径不是已经揭开有没有脚本树 / 看见钥匙路径不是已经揭开有没有脚本树 这份对象 is not already 已经揭开有没有脚本树 interchangeable，也不是已经 keypath vs scriptpath bundled（153） interchangeable / 1554 kpsp-notree interchangeable / 1555 kpsp-notall interchangeable，也不是已经 BIP-341 keypath not already revealed-tree / not already 189 / not already 153-bundled 正式三事 bundled（153 item 1 余量） interchangeable / 153 kpsp item 1 interchangeable。**  
   官方把钥匙路径不是已经揭开有没有脚本树和已经揭开有没有脚本树写成两件。看见钥匙路径不是已经揭开有没有脚本树，不是已经揭开有没有脚本树。

2. **看见keypath spend is not already revealing whether a script tree exists / 看见钥匙路径不是已经揭开有没有脚本树 / 这份对象 is not already 已经是不变量 189 interchangeable，也不是已经 keypath vs scriptpath bundled（153） interchangeable / 1554 kpsp-notree interchangeable / 1556 kpsp-notlook interchangeable，也不是已经 脚本路径≠已是tapscript语义 interchangeable / 189 脚本路径≠已是tapscript语义 interchangeable。**  
   官方把keypath spend is not already revealing whether a script tree exists和已经是不变量 189写成两件。看见keypath spend is not already revealing whether a script tree exists，不是已经是不变量 189。

3. **看见钥匙路径不是已经揭开有没有脚本树 / 看见keypath spend is not already revealing whether a script tree exists / 这份对象 is not already 已经 153 bundled interchangeable，也不是已经 keypath vs scriptpath bundled（153） interchangeable / 1554 kpsp-notree interchangeable / 1555 kpsp-notall interchangeable，也不是已经 哈希≠已揭开赎回 interchangeable / 170 哈希≠已揭开赎回 interchangeable。**  
   官方把钥匙路径不是已经揭开有没有脚本树和已经 153 bundled写成两件。看见钥匙路径不是已经揭开有没有脚本树，不是已经 153 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样藏一条别人看不见的脚本路径。

## 官方为什么这样拆

- **钥匙路径不是已经揭开有没有脚本树 interchangeable：官方写走钥匙路径不揭开当时是否还允许脚本路径。**
- **看见本页不是已经是不变量 189。**
- **看见钥路径不是已经 153 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经揭开有没有脚本树 | 不是已经揭开有没有脚本树 | 不是已经脚本路径≠已是tapscript语义（189） |
| 已经是不变量 189 | 不是已经是不变量 189 | 不是已经哈希≠已揭开赎回（170） |
| 已经 153 bundled | 不是已经 153 bundled | 不是已经1555 kpsp-notall |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-341 keypath not already revealed-tree / not already 189 / not already 153-bundled 正式三事（153 余量），必须分开是不是已经揭开有没有脚本树、是不是已经是不变量 189、是不是已经 153 bundled。可以跳过「看见一个签名所以脚本树已经公开」。不要另写 怎样藏一条别人看不见的脚本路径。153 keypath vs scriptpath bundled unbundling 在本页 item 1 启动；续 [`worked-example-kpsp-notall-vs-bundled.md`](worked-example-kpsp-notall-vs-bundled.md)（不变量 1555 item 2）。

## 本页不抄

- 控制块长度、叶子版本、annex 字节、NUMS 点。
- 怎样藏一条别人看不见的脚本路径。
