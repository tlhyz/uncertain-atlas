# 例：看见失败不再留空合约不是已经限制代码不是已经限制返回代码长度；看见failed create no empty is not code limit不是已经限制 initcode；看见失败不再留空合约不是已经限制代码不是已经区分 empty / dead

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2](https://eips.ethereum.org/EIPS/eip-2)（Final, Core, Homestead）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-2 no-empty not already code-limit / not already initcode / not already empty-dead 正式四事（234 余量）/ not 1348 hstead-notfail interchangeable / not 234 homestead-vs-already-done bundled interchangeable」，不是 homestead vs already done bundled（234），也不是已经 返回代码长度上限（185），也不是已经 initcode 上限（176）。不要另写 怎样用创建再自毁做便宜转账、怎样调时间戳磨难度。

## 官方三件事

1. **看见失败不再留空合约不是已经限制代码 / 看见失败不再留空合约不是已经限制代码 这份对象 is not already 已经限制返回代码长度 interchangeable，也不是已经 homestead vs already done bundled（234） interchangeable / 1348 hstead-notfail interchangeable / 1346 hstead-notfee interchangeable，也不是已经 EIP-2 no-empty not already code-limit / not already initcode / not already empty-dead 正式三事 bundled（234 item 3 余量） interchangeable / 234 hstead item 3 interchangeable。**  
   官方把失败不再留空合约不是已经限制代码和已经限制返回代码长度写成两件。看见失败不再留空合约不是已经限制代码，不是已经限制返回代码长度。

2. **看见failed create no empty is not code limit / 看见失败不再留空合约不是已经限制代码 / 这份对象 is not already 已经限制 initcode interchangeable，也不是已经 homestead vs already done bundled（234） interchangeable / 1348 hstead-notfail interchangeable / 1347 hstead-notsig interchangeable，也不是已经 返回代码长度上限 interchangeable / 185 返回代码长度上限 interchangeable。**  
   官方把failed create no empty is not code limit和已经限制 initcode写成两件。看见failed create no empty is not code limit，不是已经限制 initcode。

3. **看见失败不再留空合约不是已经限制代码 / 看见failed create no empty is not code limit / 这份对象 is not already 已经区分 empty / dead interchangeable，也不是已经 homestead vs already done bundled（234） interchangeable / 1348 hstead-notfail interchangeable / 1346 hstead-notfee interchangeable，也不是已经 initcode 上限 interchangeable / 176 initcode 上限 interchangeable。**  
   官方把失败不再留空合约不是已经限制代码和已经区分 empty / dead写成两件。看见失败不再留空合约不是已经限制代码，不是已经区分 empty / dead。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样用创建再自毁做便宜转账、怎样调时间戳磨难度。

## 官方为什么这样拆

- **失败不再留空合约 不是已经限制返回代码长度：185 是另一上限。**
- **看见失败更好认 不是已经限制 initcode：176 是 initcode 上限。**
- **看见不再留空合约 不是已经区分 empty / dead：180 是另一对象。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经限制返回代码长度 | 不是已经限制返回代码长度 | 不是已经返回代码长度上限（185） |
| 已经限制 initcode | 不是已经限制 initcode | 不是已经initcode 上限（176） |
| 已经区分 empty / dead | 不是已经区分 empty / dead | 不是已经1346 hstead-notfee |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2 no-empty not already code-limit / not already initcode / not already empty-dead 正式四事（234 余量），必须分开是不是已经限制返回代码长度、是不是已经限制 initcode、是不是已经区分 empty / dead。可以跳过“看见 Homestead 就已经改了 `CREATE` / 就已经让预编译拒高 `s` / 就已经限制代码 / 就已经没有炸弹”。不要另写 怎样用创建再自毁做便宜转账、怎样调时间戳磨难度。234 Homestead 硬分叉四件事 bundled unbundling 在本页 item 3 续；续 [`worked-example-hstead-notbomb-vs-bundled.md`](worked-example-hstead-notbomb-vs-bundled.md)（不变量 1349 item 4）。

## 本页不抄

- 主网 / 测试网分叉高度、交易创建费常数、曲线阶一半、难度公式常数。
- 怎样用创建再自毁做便宜转账、怎样调时间戳磨难度。
