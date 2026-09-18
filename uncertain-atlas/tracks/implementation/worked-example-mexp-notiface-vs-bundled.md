# 例：看见更便宜不是已经改了接口或算法不是已经改了接口或算法；看见cheaper is not already interface/algo-changed不是已经是不变量 206；看见更便宜不是已经改了接口或算法不是已经换了得数

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2565](https://eips.ethereum.org/EIPS/eip-2565)（Final, Core, ModExp Gas Cost）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-2565 cheaper not already iface-changed / not already algo-changed / not already 206 正式三事（227 余量）/ not 1426 mexp-notiface interchangeable / not 227 modexp-price-vs-bound bundled interchangeable」，不是 modexp price vs bound bundled（227），也不是已经 7823 输入帽（206），也不是已经 单笔气帽≠已改块气（203）。不要另写 怎样造便宜模幂、怎样打满一块、怎样按新价实现签名或可验证延迟函数。

## 官方三件事

1. **看见更便宜不是已经改了接口或算法 / 看见更便宜不是已经改了接口或算法 这份对象 is not already 已经改了接口或算法 interchangeable，也不是已经 modexp price vs bound bundled（227） interchangeable / 1426 mexp-notiface interchangeable / 1425 mexp-not198 interchangeable，也不是已经 EIP-2565 cheaper not already iface-changed / not already algo-changed / not already 206 正式三事 bundled（227 item 2 余量） interchangeable / 227 mexp item 2 interchangeable。**  
   官方把更便宜不是已经改了接口或算法和已经改了接口或算法写成两件。看见更便宜不是已经改了接口或算法，不是已经改了接口或算法。

2. **看见cheaper is not already interface/algo-changed / 看见更便宜不是已经改了接口或算法 / 这份对象 is not already 已经是不变量 206 interchangeable，也不是已经 modexp price vs bound bundled（227） interchangeable / 1426 mexp-notiface interchangeable / 1427 mexp-notmin interchangeable，也不是已经 7823 输入帽 interchangeable / 206 7823 输入帽 interchangeable。**  
   官方把cheaper is not already interface/algo-changed和已经是不变量 206写成两件。看见cheaper is not already interface/algo-changed，不是已经是不变量 206。

3. **看见更便宜不是已经改了接口或算法 / 看见cheaper is not already interface/algo-changed / 这份对象 is not already 已经换了得数 interchangeable，也不是已经 modexp price vs bound bundled（227） interchangeable / 1426 mexp-notiface interchangeable / 1425 mexp-not198 interchangeable，也不是已经 单笔气帽≠已改块气 interchangeable / 203 单笔气帽≠已改块气 interchangeable。**  
   官方把更便宜不是已经改了接口或算法和已经换了得数写成两件。看见更便宜不是已经改了接口或算法，不是已经换了得数。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造便宜模幂、怎样打满一块、怎样按新价实现签名或可验证延迟函数。

## 官方为什么这样拆

- **更便宜不是已经改了接口或算法 interchangeable：官方写底层接口和算术算法没有改。**
- **看见本页不是已经是不变量 206。**
- **看见重计价不是已经换了得数。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了接口或算法 | 不是已经改了接口或算法 | 不是已经7823 输入帽（206） |
| 已经是不变量 206 | 不是已经是不变量 206 | 不是已经单笔气帽≠已改块气（203） |
| 已经换了得数 | 不是已经换了得数 | 不是已经1425 mexp-not198 |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2565 cheaper not already iface-changed / not already algo-changed / not already 206 正式三事（227 余量），必须分开是不是已经改了接口或算法、是不是已经是不变量 206、是不是已经换了得数。可以跳过「看见 2565 就已经加了帽」。不要另写 怎样造便宜模幂、怎样打满一块、怎样按新价实现签名或可验证延迟函数。227 modexp-price vs bound bundled unbundling 在本页 item 2 续；续 [`worked-example-mexp-notmin-vs-bundled.md`](worked-example-mexp-notmin-vs-bundled.md)（不变量 1427 item 3）。

## 本页不抄

- 预编译地址、最低气价、除数常数、复杂度公式、测试向量数字。
- 怎样造便宜模幂、怎样打满一块、怎样按新价实现签名或可验证延迟函数。
