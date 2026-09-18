# 例：看见交易创建变贵不是已经改了 CREATE不是已经改了 CREATE；看见tx create fee is not CREATE repriced不是已经重定价操作码；看见交易创建变贵不是已经改了 CREATE不是已经 Homestead 四件事 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2](https://eips.ethereum.org/EIPS/eip-2)（Final, Core, Homestead）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-2 create-fee not already CREATE-repriced / not already opcode-gas / not already 234-bundled 正式四事（234 余量）/ not 1346 hstead-notfee interchangeable / not 234 homestead-vs-already-done bundled interchangeable」，不是 homestead vs already done bundled（234），也不是已经 DELEGATECALL 同一分叉（233），也不是已经 自毁退款（160）。不要另写 怎样用创建再自毁做便宜转账、怎样调时间戳磨难度。

## 官方三件事

1. **看见交易创建变贵不是已经改了 CREATE / 看见交易创建变贵不是已经改了 CREATE 这份对象 is not already 已经改了 CREATE interchangeable，也不是已经 homestead vs already done bundled（234） interchangeable / 1346 hstead-notfee interchangeable / 1347 hstead-notsig interchangeable，也不是已经 EIP-2 create-fee not already CREATE-repriced / not already opcode-gas / not already 234-bundled 正式三事 bundled（234 item 1 余量） interchangeable / 234 hstead item 1 interchangeable。**  
   官方把交易创建变贵不是已经改了 CREATE和已经改了 CREATE写成两件。看见交易创建变贵不是已经改了 CREATE，不是已经改了 CREATE。

2. **看见tx create fee is not CREATE repriced / 看见交易创建变贵不是已经改了 CREATE / 这份对象 is not already 已经重定价操作码 interchangeable，也不是已经 homestead vs already done bundled（234） interchangeable / 1346 hstead-notfee interchangeable / 1348 hstead-notfail interchangeable，也不是已经 DELEGATECALL 同一分叉 interchangeable / 233 DELEGATECALL 同一分叉 interchangeable。**  
   官方把tx create fee is not CREATE repriced和已经重定价操作码写成两件。看见tx create fee is not CREATE repriced，不是已经重定价操作码。

3. **看见交易创建变贵不是已经改了 CREATE / 看见tx create fee is not CREATE repriced / 这份对象 is not already 已经 Homestead 四件事 bundled interchangeable，也不是已经 homestead vs already done bundled（234） interchangeable / 1346 hstead-notfee interchangeable / 1347 hstead-notsig interchangeable，也不是已经 自毁退款 interchangeable / 160 自毁退款 interchangeable。**  
   官方把交易创建变贵不是已经改了 CREATE和已经 Homestead 四件事 bundled写成两件。看见交易创建变贵不是已经改了 CREATE，不是已经 Homestead 四件事 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样用创建再自毁做便宜转账、怎样调时间戳磨难度。

## 官方为什么这样拆

- **交易创建变贵 不是已经改了 CREATE：官方把交易创建固定费和 CREATE 操作码创建费分开。**
- **看见交易创建变贵 不是已经重定价操作码：CREATE 创建费保持原样。**
- **看见创建费旋钮 不是已经 Homestead 四件事 bundled：本页钉第一件单句。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了 CREATE | 不是已经改了 CREATE | 不是已经DELEGATECALL 同一分叉（233） |
| 已经重定价操作码 | 不是已经重定价操作码 | 不是已经自毁退款（160） |
| 已经 Homestead 四件事 bundled | 不是已经 Homestead 四件事 bundled | 不是已经1347 hstead-notsig |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2 create-fee not already CREATE-repriced / not already opcode-gas / not already 234-bundled 正式四事（234 余量），必须分开是不是已经改了 CREATE、是不是已经重定价操作码、是不是已经 Homestead 四件事 bundled。可以跳过“看见 Homestead 就已经改了 `CREATE` / 就已经让预编译拒高 `s` / 就已经限制代码 / 就已经没有炸弹”。不要另写 怎样用创建再自毁做便宜转账、怎样调时间戳磨难度。234 Homestead 硬分叉四件事 bundled unbundling 在本页 item 1 启动；续 [`worked-example-hstead-notsig-vs-bundled.md`](worked-example-hstead-notsig-vs-bundled.md)（不变量 1347 item 2）。

## 本页不抄

- 主网 / 测试网分叉高度、交易创建费常数、曲线阶一半、难度公式常数。
- 怎样用创建再自毁做便宜转账、怎样调时间戳磨难度。
