# 例：看见多余栈元素不是已经随便填；看见多重签验过不是已经看过 dummy；看见 dummy 不是空不是已经合法

**层次**：共识 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-147](https://github.com/bitcoin/bips/blob/master/bip-0147.mediawiki)（Deployed, Consensus soft fork）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.3](../../courses/level-03-bitcoin/L03-M03-conservative-evolution.md)、[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4。本页是「BIP-147 dummy not already arbitrary / not already legal / not already settled 正式三事（264 余量）/ not 1229 dum147-notany interchangeable / not 264 dummy-vs-empty bundled interchangeable」，不是 dummy bundled（264），也不是验得过就已经是严格 DER（172），也不是 txid 就已经等于 wtxid（152）。不要另写怎样改 dummy 撞身份。

## 官方三件事

1. **看见多余栈元素 / 看见 CHECKMULTISIG 多吃的那一个 这份元素 is not already 已经随便填 interchangeable，也不是已经 dummy bundled（264） interchangeable / 1229 dum147-notany interchangeable / 1230 dum147-notwit interchangeable / 264 dummy item 2 wit-not-gone interchangeable，也不是已经 BIP-147 dummy not already arbitrary / not already legal / not already settled 正式三事 bundled（264 item 1 余量） interchangeable / 264 dummy item 1 interchangeable。**  
   官方写：OP_CHECKMULTISIG / OP_CHECKMULTISIGVERIFY 在验签之后还会再吃一个多余的栈元素（dummy）。以前这个元素完全不看，换成任何值脚本仍过。本页新增一条共识规则：dummy 必须是空字节数组。看见多余栈元素，不是已经随便填。

2. **看见多重签验过 / 看见多余栈元素 / 这份元素 is not already 已经看过 dummy interchangeable，也不是已经 dummy bundled（264） interchangeable / 1229 dum147-notany interchangeable / 264 dummy item 3 pol-not-cons interchangeable / 1231 dum147-notpol interchangeable，也不是已经验得过就已经是严格 DER interchangeable / 172 der interchangeable。**  
   官方写：本页同时管隔离见证之前的脚本，也管 BIP-141 那种付给见证脚本哈希。看见多重签验过，不是已经看过 dummy。

3. **看见 dummy 不是空 / 看见多余栈元素 / 这份元素 is not already 已经合法 interchangeable，也不是已经 dummy bundled（264） interchangeable / 1229 dum147-notany interchangeable / 1230 dum147-notwit interchangeable，也不是已经 txid 就已经等于 wtxid interchangeable / 152 wtxid interchangeable。**  
   官方写：别的任何值让脚本立刻为假。看见 dummy 不是空，不是已经合法，也不是已经交差。

激活日程、版本位编号是规范里的取值，本页不抄。不要另写怎样改 dummy 撞身份。

## 官方为什么这样拆

- **多余栈元素 不是已经随便填：** 官方把验签之后多吃一个却不看写成设计缺陷。
- **多重签验过 不是已经看过 dummy：** 官方把验签和看 dummy 写成两件。
- **dummy 不是空 不是已经合法：** 官方把非空 dummy 写成立刻为假。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 随便填 | 不是已经随便填 | 不是已经严格 DER（172） |
| 看过 dummy | 不是已经看过 dummy | 不是已经等于 wtxid（152） |
| 合法 | 不是已经合法 | 不是已经没有延展（1230） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-147 dummy not already arbitrary / not already legal / not already settled 正式三事（264 余量），必须分开是不是已经随便填、是不是已经看过 dummy、是不是已经合法。可以跳过「看见多重签验过就已经不可延展」。不要另写怎样改 dummy 撞身份。264 dummy vs empty bundled unbundling 在本页 item 1 启动；续 [`worked-example-dum147-notwit-vs-bundled.md`](worked-example-dum147-notwit-vs-bundled.md)（不变量 1230 item 2）。

## 本页不抄

- 激活时间、版本位编号、部署名、参考客户端版本号。
- 怎样造非空 dummy、怎样把非兼容签改成兼容、怎样靠改 dummy 挡紧凑块。
