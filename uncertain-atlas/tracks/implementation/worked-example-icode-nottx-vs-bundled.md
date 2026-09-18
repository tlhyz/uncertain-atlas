# 例：看见创建交易超界不是已经是 CREATE 指令失败不是已经是 CREATE 指令失败；看见create-tx oversize is not already CREATE fail不是已经是 2681 序号上限；看见创建交易超界不是已经是 CREATE 指令失败不是已经进 EVM 再失败

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-3860](https://eips.ethereum.org/EIPS/eip-3860)（Final, Core, Limit and meter initcode）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-3860 create-tx-oversize not already CREATE-fail / not already 2681 / not already in-EVM 正式三事（176 余量）/ not 1438 icode-nottx interchangeable / not 176 initcode-vs-runtime bundled interchangeable」，不是 initcode vs runtime bundled（176），也不是已经 上限≠还能加（175），也不是已经 第一次≠已热（169）。不要另写 怎样造超长 initcode、怎样用工厂一次塞多层合约去撞界。

## 官方三件事

1. **看见创建交易超界不是已经是 CREATE 指令失败 / 看见创建交易超界不是已经是 CREATE 指令失败 这份对象 is not already 已经是 CREATE 指令失败 interchangeable，也不是已经 initcode vs runtime bundled（176） interchangeable / 1438 icode-nottx interchangeable / 1437 icode-not170 interchangeable，也不是已经 EIP-3860 create-tx-oversize not already CREATE-fail / not already 2681 / not already in-EVM 正式三事 bundled（176 item 2 余量） interchangeable / 176 icode item 2 interchangeable。**  
   官方把创建交易超界不是已经是 CREATE 指令失败和已经是 CREATE 指令失败写成两件。看见创建交易超界不是已经是 CREATE 指令失败，不是已经是 CREATE 指令失败。

2. **看见create-tx oversize is not already CREATE fail / 看见创建交易超界不是已经是 CREATE 指令失败 / 这份对象 is not already 已经是 2681 序号上限 interchangeable，也不是已经 initcode vs runtime bundled（176） interchangeable / 1438 icode-nottx interchangeable / 1439 icode-notrun interchangeable，也不是已经 上限≠还能加 interchangeable / 175 上限≠还能加 interchangeable。**  
   官方把create-tx oversize is not already CREATE fail和已经是 2681 序号上限写成两件。看见create-tx oversize is not already CREATE fail，不是已经是 2681 序号上限。

3. **看见创建交易超界不是已经是 CREATE 指令失败 / 看见create-tx oversize is not already CREATE fail / 这份对象 is not already 已经进 EVM 再失败 interchangeable，也不是已经 initcode vs runtime bundled（176） interchangeable / 1438 icode-nottx interchangeable / 1437 icode-not170 interchangeable，也不是已经 第一次≠已热 interchangeable / 169 第一次≠已热 interchangeable。**  
   官方把创建交易超界不是已经是 CREATE 指令失败和已经进 EVM 再失败写成两件。看见创建交易超界不是已经是 CREATE 指令失败，不是已经进 EVM 再失败。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造超长 initcode、怎样用工厂一次塞多层合约去撞界。

## 官方为什么这样拆

- **创建交易超界不是已经是 CREATE 指令失败 interchangeable：官方写交易超界整笔非法，指令超界才是异常中止。**
- **看见本页不是已经是 2681 序号上限。**
- **看见创建交易超界不是已经进 EVM 再失败。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是 CREATE 指令失败 | 不是已经是 CREATE 指令失败 | 不是已经上限≠还能加（175） |
| 已经是 2681 序号上限 | 不是已经是 2681 序号上限 | 不是已经第一次≠已热（169） |
| 已经进 EVM 再失败 | 不是已经进 EVM 再失败 | 不是已经1437 icode-not170 |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3860 create-tx-oversize not already CREATE-fail / not already 2681 / not already in-EVM 正式三事（176 余量），必须分开是不是已经是 CREATE 指令失败、是不是已经是 2681 序号上限、是不是已经进 EVM 再失败。可以跳过「一份上限管两种代码」。不要另写 怎样造超长 initcode、怎样用工厂一次塞多层合约去撞界。176 initcode vs runtime bundled unbundling 在本页 item 2 续；续 [`worked-example-icode-notrun-vs-bundled.md`](worked-example-icode-notrun-vs-bundled.md)（不变量 1439 item 3）。

## 本页不抄

- 上限字节、每字气价、部署代码上限、例工厂。
- 怎样造超长 initcode、怎样用工厂一次塞多层合约去撞界。
