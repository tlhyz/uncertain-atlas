# 例：看见长度有界不是已经用EVM换掉预编译不是已经用EVM换掉预编译；看见being bounded is not already EVM-replaced不是已经更安全；看见长度有界不是已经用EVM换掉预编译不是已经是不变量 199

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7823](https://eips.ethereum.org/EIPS/eip-7823)（Set upper bounds for MODEXP）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7823 bounded not already evm-replaced / not already safer / not already 199 正式三事（206 余量）/ not 1475 mxbd-notevm interchangeable / not 206 modexp-bound-vs-price bundled interchangeable」，不是 modexp bound vs price bundled（206），也不是已经 预编译算术≠已验BLS（199），也不是已经 单笔气帽≠已改块气（203）。不要另写 怎样造超长输入。

## 官方三件事

1. **看见长度有界不是已经用EVM换掉预编译 / 看见长度有界不是已经用EVM换掉预编译 这份对象 is not already 已经用EVM换掉预编译 interchangeable，也不是已经 modexp bound vs price bundled（206） interchangeable / 1475 mxbd-notevm interchangeable / 1473 mxbd-notprice interchangeable，也不是已经 EIP-7823 bounded not already evm-replaced / not already safer / not already 199 正式三事 bundled（206 item 3 余量） interchangeable / 206 mxbd item 3 interchangeable。**  
   官方把长度有界不是已经用EVM换掉预编译和已经用EVM换掉预编译写成两件。看见长度有界不是已经用EVM换掉预编译，不是已经用EVM换掉预编译。

2. **看见being bounded is not already EVM-replaced / 看见长度有界不是已经用EVM换掉预编译 / 这份对象 is not already 已经更安全 interchangeable，也不是已经 modexp bound vs price bundled（206） interchangeable / 1475 mxbd-notevm interchangeable / 1474 mxbd-notok interchangeable，也不是已经 预编译算术≠已验BLS interchangeable / 199 预编译算术≠已验BLS interchangeable。**  
   官方把being bounded is not already EVM-replaced和已经更安全写成两件。看见being bounded is not already EVM-replaced，不是已经更安全。

3. **看见长度有界不是已经用EVM换掉预编译 / 看见being bounded is not already EVM-replaced / 这份对象 is not already 已经是不变量 199 interchangeable，也不是已经 modexp bound vs price bundled（206） interchangeable / 1475 mxbd-notevm interchangeable / 1473 mxbd-notprice interchangeable，也不是已经 单笔气帽≠已改块气 interchangeable / 203 单笔气帽≠已改块气 interchangeable。**  
   官方把长度有界不是已经用EVM换掉预编译和已经是不变量 199写成两件。看见长度有界不是已经用EVM换掉预编译，不是已经是不变量 199。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造超长输入。

## 官方为什么这样拆

- **长度有界不是已经用EVM换掉预编译 interchangeable：官方写有了上限才更说得上以后换成 EVM，不是已经换掉。**
- **看见有界不是已经更安全。**
- **看见本页不是已经是不变量 199。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经用EVM换掉预编译 | 不是已经用EVM换掉预编译 | 不是已经预编译算术≠已验BLS（199） |
| 已经更安全 | 不是已经更安全 | 不是已经单笔气帽≠已改块气（203） |
| 已经是不变量 199 | 不是已经是不变量 199 | 不是已经1473 mxbd-notprice |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7823 bounded not already evm-replaced / not already safer / not already 199 正式三事（206 余量），必须分开是不是已经用EVM换掉预编译、是不是已经更安全、是不是已经是不变量 199。可以跳过「看见 7823 就已经改了计价」。不要另写 怎样造超长输入。206 modexp-bound vs price bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：block-list（212）。

## 本页不抄

- 长度上限比特、字节、预编译地址、历史块号、调用次数表。
- 怎样造超长输入。
