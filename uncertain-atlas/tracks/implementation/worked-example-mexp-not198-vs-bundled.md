# 例：看见模幂重计价不是已经是 198 那道复杂度公式不是已经是 198 那道复杂度公式；看见reprice is not already the 198 formula不是已经是 7823；看见模幂重计价不是已经是 198 那道复杂度公式不是已经 227 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2565](https://eips.ethereum.org/EIPS/eip-2565)（Final, Core, ModExp Gas Cost）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-2565 reprice not already 198-formula / not already 7823 / not already 227-bundled 正式三事（227 余量）/ not 1425 mexp-not198 interchangeable / not 227 modexp-price-vs-bound bundled interchangeable」，不是 modexp price vs bound bundled（227），也不是已经 模幂长度帽≠已改计价（206），也不是已经 BLS 预编译算术（198）。不要另写 怎样造便宜模幂、怎样打满一块、怎样按新价实现签名或可验证延迟函数。

## 官方三件事

1. **看见模幂重计价不是已经是 198 那道复杂度公式 / 看见模幂重计价不是已经是 198 那道复杂度公式 这份对象 is not already 已经是 198 那道复杂度公式 interchangeable，也不是已经 modexp price vs bound bundled（227） interchangeable / 1425 mexp-not198 interchangeable / 1426 mexp-notiface interchangeable，也不是已经 EIP-2565 reprice not already 198-formula / not already 7823 / not already 227-bundled 正式三事 bundled（227 item 1 余量） interchangeable / 227 mexp item 1 interchangeable。**  
   官方把模幂重计价不是已经是 198 那道复杂度公式和已经是 198 那道复杂度公式写成两件。看见模幂重计价不是已经是 198 那道复杂度公式，不是已经是 198 那道复杂度公式。

2. **看见reprice is not already the 198 formula / 看见模幂重计价不是已经是 198 那道复杂度公式 / 这份对象 is not already 已经是 7823 interchangeable，也不是已经 modexp price vs bound bundled（227） interchangeable / 1425 mexp-not198 interchangeable / 1427 mexp-notmin interchangeable，也不是已经 模幂长度帽≠已改计价 interchangeable / 206 模幂长度帽≠已改计价 interchangeable。**  
   官方把reprice is not already the 198 formula和已经是 7823写成两件。看见reprice is not already the 198 formula，不是已经是 7823。

3. **看见模幂重计价不是已经是 198 那道复杂度公式 / 看见reprice is not already the 198 formula / 这份对象 is not already 已经 227 bundled interchangeable，也不是已经 modexp price vs bound bundled（227） interchangeable / 1425 mexp-not198 interchangeable / 1426 mexp-notiface interchangeable，也不是已经 BLS 预编译算术 interchangeable / 198 BLS 预编译算术 interchangeable。**  
   官方把模幂重计价不是已经是 198 那道复杂度公式和已经 227 bundled写成两件。看见模幂重计价不是已经是 198 那道复杂度公式，不是已经 227 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造便宜模幂、怎样打满一块、怎样按新价实现签名或可验证延迟函数。

## 官方为什么这样拆

- **模幂重计价不是已经是 198 那道复杂度公式 interchangeable：官方把新公式和 198 分段复杂度写成两件。**
- **看见规范编号不是已经是 7823。**
- **看见读数旋钮不是已经 227 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是 198 那道复杂度公式 | 不是已经是 198 那道复杂度公式 | 不是已经模幂长度帽≠已改计价（206） |
| 已经是 7823 | 不是已经是 7823 | 不是已经BLS 预编译算术（198） |
| 已经 227 bundled | 不是已经 227 bundled | 不是已经1426 mexp-notiface |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2565 reprice not already 198-formula / not already 7823 / not already 227-bundled 正式三事（227 余量），必须分开是不是已经是 198 那道复杂度公式、是不是已经是 7823、是不是已经 227 bundled。可以跳过「看见 2565 就已经加了帽」。不要另写 怎样造便宜模幂、怎样打满一块、怎样按新价实现签名或可验证延迟函数。227 modexp-price vs bound bundled unbundling 在本页 item 1 启动；续 [`worked-example-mexp-notiface-vs-bundled.md`](worked-example-mexp-notiface-vs-bundled.md)（不变量 1426 item 2）。

## 本页不抄

- 预编译地址、最低气价、除数常数、复杂度公式、测试向量数字。
- 怎样造便宜模幂、怎样打满一块、怎样按新价实现签名或可验证延迟函数。
