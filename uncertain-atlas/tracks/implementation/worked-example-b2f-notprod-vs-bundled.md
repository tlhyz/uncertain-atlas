# 例：看见本页不是已经能验 Equihash不是已经能验 Equihash；看见this page is not already Equihash-live不是已经是跨链中继 / 原子交换；看见本页不是已经能验 Equihash不是已经有隐私

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-152](https://eips.ethereum.org/EIPS/eip-152)（Final, Core, Add BLAKE2 compression function F precompile）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-152 this-page not already Equihash / not already relay / not already privacy 正式三事（230 余量）/ not 1435 b2f-notprod interchangeable / not 230 blake2f-vs-hash bundled interchangeable」，不是 blake2f vs hash bundled（230），也不是已经 2537 BLS12 算术（199），也不是已经 本账户余额指令≠已是 BALANCE（229）。不要另写 怎样叠压缩函数去验工作量、怎样做跨链中继或原子交换。

## 官方三件事

1. **看见本页不是已经能验 Equihash / 看见本页不是已经能验 Equihash 这份对象 is not already 已经能验 Equihash interchangeable，也不是已经 blake2f vs hash bundled（230） interchangeable / 1435 b2f-notprod interchangeable / 1434 b2f-nothash interchangeable，也不是已经 EIP-152 this-page not already Equihash / not already relay / not already privacy 正式三事 bundled（230 item 2 余量） interchangeable / 230 b2f item 2 interchangeable。**  
   官方把本页不是已经能验 Equihash和已经能验 Equihash写成两件。看见本页不是已经能验 Equihash，不是已经能验 Equihash。

2. **看见this page is not already Equihash-live / 看见本页不是已经能验 Equihash / 这份对象 is not already 已经是跨链中继 / 原子交换 interchangeable，也不是已经 blake2f vs hash bundled（230） interchangeable / 1435 b2f-notprod interchangeable / 1436 b2f-notapi interchangeable，也不是已经 2537 BLS12 算术 interchangeable / 199 2537 BLS12 算术 interchangeable。**  
   官方把this page is not already Equihash-live和已经是跨链中继 / 原子交换写成两件。看见this page is not already Equihash-live，不是已经是跨链中继 / 原子交换。

3. **看见本页不是已经能验 Equihash / 看见this page is not already Equihash-live / 这份对象 is not already 已经有隐私 interchangeable，也不是已经 blake2f vs hash bundled（230） interchangeable / 1435 b2f-notprod interchangeable / 1434 b2f-nothash interchangeable，也不是已经 本账户余额指令≠已是 BALANCE interchangeable / 229 本账户余额指令≠已是 BALANCE interchangeable。**  
   官方把本页不是已经能验 Equihash和已经有隐私写成两件。看见本页不是已经能验 Equihash，不是已经有隐私。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样叠压缩函数去验工作量、怎样做跨链中继或原子交换。

## 官方为什么这样拆

- **本页不是已经能验 Equihash interchangeable：官方把便宜跑更高轮和已经能验工作量写成两件。**
- **看见本页不是已经是跨链中继 / 原子交换。**
- **看见互操作动机不是已经有隐私。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经能验 Equihash | 不是已经能验 Equihash | 不是已经2537 BLS12 算术（199） |
| 已经是跨链中继 / 原子交换 | 不是已经是跨链中继 / 原子交换 | 不是已经本账户余额指令≠已是 BALANCE（229） |
| 已经有隐私 | 不是已经有隐私 | 不是已经1434 b2f-nothash |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-152 this-page not already Equihash / not already relay / not already privacy 正式三事（230 余量），必须分开是不是已经能验 Equihash、是不是已经是跨链中继 / 原子交换、是不是已经有隐私。可以跳过「看见 152 就已经能验 Equihash」。不要另写 怎样叠压缩函数去验工作量、怎样做跨链中继或原子交换。230 blake2f vs hash bundled unbundling 在本页 item 2 续；续 [`worked-example-b2f-notapi-vs-bundled.md`](worked-example-b2f-notapi-vs-bundled.md)（不变量 1436 item 3）。

## 本页不抄

- 预编译地址、输入宽度、每轮气价、测试向量。
- 怎样叠压缩函数去验工作量、怎样做跨链中继或原子交换。
