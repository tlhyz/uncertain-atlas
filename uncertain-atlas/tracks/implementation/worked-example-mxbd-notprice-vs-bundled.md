# 例：看见MODEXP输入长度帽不是已经改了计价公式不是已经改了计价公式；看见MODEXP input bound is not already a price change不是已经是不变量 227；看见MODEXP输入长度帽不是已经改了计价公式不是已经 206 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7823](https://eips.ethereum.org/EIPS/eip-7823)（Set upper bounds for MODEXP）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7823 input-bound not already price-changed / not already 227 / not already 206-bundled 正式三事（206 余量）/ not 1473 mxbd-notprice interchangeable / not 206 modexp-bound-vs-price bundled interchangeable」，不是 modexp bound vs price bundled（206），也不是已经 2565计价≠本页帽（227），也不是已经 单笔气帽≠已改块气（203）。不要另写 怎样造超长输入。

## 官方三件事

1. **看见MODEXP输入长度帽不是已经改了计价公式 / 看见MODEXP输入长度帽不是已经改了计价公式 这份对象 is not already 已经改了计价公式 interchangeable，也不是已经 modexp bound vs price bundled（206） interchangeable / 1473 mxbd-notprice interchangeable / 1474 mxbd-notok interchangeable，也不是已经 EIP-7823 input-bound not already price-changed / not already 227 / not already 206-bundled 正式三事 bundled（206 item 1 余量） interchangeable / 206 mxbd item 1 interchangeable。**  
   官方把MODEXP输入长度帽不是已经改了计价公式和已经改了计价公式写成两件。看见MODEXP输入长度帽不是已经改了计价公式，不是已经改了计价公式。

2. **看见MODEXP input bound is not already a price change / 看见MODEXP输入长度帽不是已经改了计价公式 / 这份对象 is not already 已经是不变量 227 interchangeable，也不是已经 modexp bound vs price bundled（206） interchangeable / 1473 mxbd-notprice interchangeable / 1475 mxbd-notevm interchangeable，也不是已经 2565计价≠本页帽 interchangeable / 227 2565计价≠本页帽 interchangeable。**  
   官方把MODEXP input bound is not already a price change和已经是不变量 227写成两件。看见MODEXP input bound is not already a price change，不是已经是不变量 227。

3. **看见MODEXP输入长度帽不是已经改了计价公式 / 看见MODEXP input bound is not already a price change / 这份对象 is not already 已经 206 bundled interchangeable，也不是已经 modexp bound vs price bundled（206） interchangeable / 1473 mxbd-notprice interchangeable / 1474 mxbd-notok interchangeable，也不是已经 单笔气帽≠已改块气 interchangeable / 203 单笔气帽≠已改块气 interchangeable。**  
   官方把MODEXP输入长度帽不是已经改了计价公式和已经 206 bundled写成两件。看见MODEXP输入长度帽不是已经改了计价公式，不是已经 206 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造超长输入。

## 官方为什么这样拆

- **MODEXP输入长度帽不是已经改了计价公式 interchangeable：官方写现在不建议借本页重写计价，上限落地之后以后才可能改。**
- **看见本页不是已经是不变量 227。**
- **看见读数旋钮不是已经 206 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了计价公式 | 不是已经改了计价公式 | 不是已经2565计价≠本页帽（227） |
| 已经是不变量 227 | 不是已经是不变量 227 | 不是已经单笔气帽≠已改块气（203） |
| 已经 206 bundled | 不是已经 206 bundled | 不是已经1474 mxbd-notok |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7823 input-bound not already price-changed / not already 227 / not already 206-bundled 正式三事（206 余量），必须分开是不是已经改了计价公式、是不是已经是不变量 227、是不是已经 206 bundled。可以跳过「看见 7823 就已经改了计价」。不要另写 怎样造超长输入。206 modexp-bound vs price bundled unbundling 在本页 item 1 启动；续 [`worked-example-mxbd-notok-vs-bundled.md`](worked-example-mxbd-notok-vs-bundled.md)（不变量 1474 item 2）。

## 本页不抄

- 长度上限比特、字节、预编译地址、历史块号、调用次数表。
- 怎样造超长输入。
