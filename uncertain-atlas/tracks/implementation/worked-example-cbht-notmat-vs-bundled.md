# 例：看见写了高度不是coinbase已经能花不是已经能花；看见writing the height is not already making the coinbase spendable不是已经是不变量 163；看见写了高度不是coinbase已经能花不是已经是不变量 144

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-34](https://github.com/bitcoin/bips/blob/master/bip-0034.mediawiki)（Block v2, Height in Coinbase）。  
**对应课文**：[L3.1](../../courses/level-03-bitcoin/L03-M01-nakamoto-finality.md)。  
**不要写进**：`index/03` 共识行、M3.1、L3.1。本页是「BIP-34 wrote-height not already spendable / not already 163 / not already 144 正式三事（173 余量）/ not 1544 cbht-notmat interchangeable / not 173 coinbase-height-vs-header bundled interchangeable」，不是 coinbase height vs header bundled（173），也不是已经 进块≠能花（163），也不是已经 策略≠共识（144）。不要另写 怎样造不带头高度的coinbase、怎样靠重复coinbase撞身份。

## 官方三件事

1. **看见写了高度不是coinbase已经能花 / 看见写了高度不是coinbase已经能花 这份对象 is not already 已经能花 interchangeable，也不是已经 coinbase height vs header bundled（173） interchangeable / 1544 cbht-notmat interchangeable / 1542 cbht-nothdr interchangeable，也不是已经 BIP-34 wrote-height not already spendable / not already 163 / not already 144 正式三事 bundled（173 item 3 余量） interchangeable / 173 cbht item 3 interchangeable。**  
   官方把写了高度不是coinbase已经能花和已经能花写成两件。看见写了高度不是coinbase已经能花，不是已经能花。

2. **看见writing the height is not already making the coinbase spendable / 看见写了高度不是coinbase已经能花 / 这份对象 is not already 已经是不变量 163 interchangeable，也不是已经 coinbase height vs header bundled（173） interchangeable / 1544 cbht-notmat interchangeable / 1543 cbht-notv9 interchangeable，也不是已经 进块≠能花 interchangeable / 163 进块≠能花 interchangeable。**  
   官方把writing the height is not already making the coinbase spendable和已经是不变量 163写成两件。看见writing the height is not already making the coinbase spendable，不是已经是不变量 163。

3. **看见写了高度不是coinbase已经能花 / 看见writing the height is not already making the coinbase spendable / 这份对象 is not already 已经是不变量 144 interchangeable，也不是已经 coinbase height vs header bundled（173） interchangeable / 1544 cbht-notmat interchangeable / 1542 cbht-nothdr interchangeable，也不是已经 策略≠共识 interchangeable / 144 策略≠共识 interchangeable。**  
   官方把写了高度不是coinbase已经能花和已经是不变量 144写成两件。看见写了高度不是coinbase已经能花，不是已经是不变量 144。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造不带头高度的coinbase、怎样靠重复coinbase撞身份。

## 官方为什么这样拆

- **写了高度不是coinbase已经能花 interchangeable：官方没有把写了高度写成已经能花。**
- **看见本页不是已经是不变量 163。**
- **看见本页不是已经是不变量 144。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经能花 | 不是已经能花 | 不是已经进块≠能花（163） |
| 已经是不变量 163 | 不是已经是不变量 163 | 不是已经策略≠共识（144） |
| 已经是不变量 144 | 不是已经是不变量 144 | 不是已经1542 cbht-nothdr |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-34 wrote-height not already spendable / not already 163 / not already 144 正式三事（173 余量），必须分开是不是已经能花、是不是已经是不变量 163、是不是已经是不变量 144。可以跳过「看见头就已经有高度字段」。不要另写 怎样造不带头高度的coinbase、怎样靠重复coinbase撞身份。173 coinbase height vs header bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的官方对象：versionbit-vs-active（171）。

## 本页不抄

- 激活票数、版本号常数、编码宽度、例高度。
- 怎样造不带头高度的coinbase、怎样靠重复coinbase撞身份。
