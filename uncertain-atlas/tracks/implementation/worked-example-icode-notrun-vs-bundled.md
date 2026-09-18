# 例：看见按字收跳转分析费不是已经跑完 initcode不是已经跑完 initcode；看见jumpdest fee is not already having run initcode不是已经是 CREATE2 算地址的哈希费；看见按字收跳转分析费不是已经跑完 initcode不是已经创建

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-3860](https://eips.ethereum.org/EIPS/eip-3860)（Final, Core, Limit and meter initcode）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-3860 jumpdest-fee not already ran-initcode / not already CREATE2-hash-fee / not already created 正式三事（176 余量）/ not 1439 icode-notrun interchangeable / not 176 initcode-vs-runtime bundled interchangeable」，不是 initcode vs runtime bundled（176），也不是已经 返回代码≠initcode（185），也不是已经 保留首字节≠已是对象格式（188）。不要另写 怎样造超长 initcode、怎样用工厂一次塞多层合约去撞界。

## 官方三件事

1. **看见按字收跳转分析费不是已经跑完 initcode / 看见按字收跳转分析费不是已经跑完 initcode 这份对象 is not already 已经跑完 initcode interchangeable，也不是已经 initcode vs runtime bundled（176） interchangeable / 1439 icode-notrun interchangeable / 1437 icode-not170 interchangeable，也不是已经 EIP-3860 jumpdest-fee not already ran-initcode / not already CREATE2-hash-fee / not already created 正式三事 bundled（176 item 3 余量） interchangeable / 176 icode item 3 interchangeable。**  
   官方把按字收跳转分析费不是已经跑完 initcode和已经跑完 initcode写成两件。看见按字收跳转分析费不是已经跑完 initcode，不是已经跑完 initcode。

2. **看见jumpdest fee is not already having run initcode / 看见按字收跳转分析费不是已经跑完 initcode / 这份对象 is not already 已经是 CREATE2 算地址的哈希费 interchangeable，也不是已经 initcode vs runtime bundled（176） interchangeable / 1439 icode-notrun interchangeable / 1438 icode-nottx interchangeable，也不是已经 返回代码≠initcode interchangeable / 185 返回代码≠initcode interchangeable。**  
   官方把jumpdest fee is not already having run initcode和已经是 CREATE2 算地址的哈希费写成两件。看见jumpdest fee is not already having run initcode，不是已经是 CREATE2 算地址的哈希费。

3. **看见按字收跳转分析费不是已经跑完 initcode / 看见jumpdest fee is not already having run initcode / 这份对象 is not already 已经创建 interchangeable，也不是已经 initcode vs runtime bundled（176） interchangeable / 1439 icode-notrun interchangeable / 1437 icode-not170 interchangeable，也不是已经 保留首字节≠已是对象格式 interchangeable / 188 保留首字节≠已是对象格式 interchangeable。**  
   官方把按字收跳转分析费不是已经跑完 initcode和已经创建写成两件。看见按字收跳转分析费不是已经跑完 initcode，不是已经创建。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造超长 initcode、怎样用工厂一次塞多层合约去撞界。

## 官方为什么这样拆

- **按字收跳转分析费不是已经跑完 initcode interchangeable：官方写这道费在算新地址、跑 initcode 之前扣。**
- **看见本页不是已经是 CREATE2 算地址的哈希费。**
- **看见收了分析费不是已经创建。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经跑完 initcode | 不是已经跑完 initcode | 不是已经返回代码≠initcode（185） |
| 已经是 CREATE2 算地址的哈希费 | 不是已经是 CREATE2 算地址的哈希费 | 不是已经保留首字节≠已是对象格式（188） |
| 已经创建 | 不是已经创建 | 不是已经1437 icode-not170 |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3860 jumpdest-fee not already ran-initcode / not already CREATE2-hash-fee / not already created 正式三事（176 余量），必须分开是不是已经跑完 initcode、是不是已经是 CREATE2 算地址的哈希费、是不是已经创建。可以跳过「一份上限管两种代码」。不要另写 怎样造超长 initcode、怎样用工厂一次塞多层合约去撞界。176 initcode vs runtime bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：returned（185）。

## 本页不抄

- 上限字节、每字气价、部署代码上限、例工厂。
- 怎样造超长 initcode、怎样用工厂一次塞多层合约去撞界。
