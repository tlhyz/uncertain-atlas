# 例：看见coinbase第一项写了高度不是头上已经有高度字段不是已经有高度字段；看见writing height in coinbase is not already a height field in the header不是已经是不变量 171；看见coinbase第一项写了高度不是头上已经有高度字段不是已经 173 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-34](https://github.com/bitcoin/bips/blob/master/bip-0034.mediawiki)（Block v2, Height in Coinbase）。  
**对应课文**：[L3.1](../../courses/level-03-bitcoin/L03-M01-nakamoto-finality.md)。  
**不要写进**：`index/03` 共识行、M3.1、L3.1。本页是「BIP-34 coinbase-height not already header-field / not already 171 / not already 173-bundled 正式三事（173 余量）/ not 1542 cbht-nothdr interchangeable / not 173 coinbase-height-vs-header bundled interchangeable」，不是 coinbase height vs header bundled（173），也不是已经 版本位≠已激活（171），也不是已经 进块≠能花（163）。不要另写 怎样造不带头高度的coinbase、怎样靠重复coinbase撞身份。

## 官方三件事

1. **看见coinbase第一项写了高度不是头上已经有高度字段 / 看见coinbase第一项写了高度不是头上已经有高度字段 这份对象 is not already 已经有高度字段 interchangeable，也不是已经 coinbase height vs header bundled（173） interchangeable / 1542 cbht-nothdr interchangeable / 1543 cbht-notv9 interchangeable，也不是已经 BIP-34 coinbase-height not already header-field / not already 171 / not already 173-bundled 正式三事 bundled（173 item 1 余量） interchangeable / 173 cbht item 1 interchangeable。**  
   官方把coinbase第一项写了高度不是头上已经有高度字段和已经有高度字段写成两件。看见coinbase第一项写了高度不是头上已经有高度字段，不是已经有高度字段。

2. **看见writing height in coinbase is not already a height field in the header / 看见coinbase第一项写了高度不是头上已经有高度字段 / 这份对象 is not already 已经是不变量 171 interchangeable，也不是已经 coinbase height vs header bundled（173） interchangeable / 1542 cbht-nothdr interchangeable / 1544 cbht-notmat interchangeable，也不是已经 版本位≠已激活 interchangeable / 171 版本位≠已激活 interchangeable。**  
   官方把writing height in coinbase is not already a height field in the header和已经是不变量 171写成两件。看见writing height in coinbase is not already a height field in the header，不是已经是不变量 171。

3. **看见coinbase第一项写了高度不是头上已经有高度字段 / 看见writing height in coinbase is not already a height field in the header / 这份对象 is not already 已经 173 bundled interchangeable，也不是已经 coinbase height vs header bundled（173） interchangeable / 1542 cbht-nothdr interchangeable / 1543 cbht-notv9 interchangeable，也不是已经 进块≠能花 interchangeable / 163 进块≠能花 interchangeable。**  
   官方把coinbase第一项写了高度不是头上已经有高度字段和已经 173 bundled写成两件。看见coinbase第一项写了高度不是头上已经有高度字段，不是已经 173 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造不带头高度的coinbase、怎样靠重复coinbase撞身份。

## 官方为什么这样拆

- **coinbase第一项写了高度不是头上已经有高度字段 interchangeable：官方写新出的 coinbase 第一项写上本块高度，不是头上已经有高度字段。**
- **看见本页不是已经是不变量 171。**
- **看见高度承诺不是已经 173 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经有高度字段 | 不是已经有高度字段 | 不是已经版本位≠已激活（171） |
| 已经是不变量 171 | 不是已经是不变量 171 | 不是已经进块≠能花（163） |
| 已经 173 bundled | 不是已经 173 bundled | 不是已经1543 cbht-notv9 |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-34 coinbase-height not already header-field / not already 171 / not already 173-bundled 正式三事（173 余量），必须分开是不是已经有高度字段、是不是已经是不变量 171、是不是已经 173 bundled。可以跳过「看见头就已经有高度字段」。不要另写 怎样造不带头高度的coinbase、怎样靠重复coinbase撞身份。173 coinbase height vs header bundled unbundling 在本页 item 1 启动；续 [`worked-example-cbht-notv9-vs-bundled.md`](worked-example-cbht-notv9-vs-bundled.md)（不变量 1543 item 2）。

## 本页不抄

- 激活票数、版本号常数、编码宽度、例高度。
- 怎样造不带头高度的coinbase、怎样靠重复coinbase撞身份。
