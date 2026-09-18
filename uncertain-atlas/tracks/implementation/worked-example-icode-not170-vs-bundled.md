# 例：看见initcode 超界不是已经是部署代码超界不是已经是部署代码超界；看见initcode bound is not already the 170 runtime bound不是已经是 1014 哈希费；看见initcode 超界不是已经是部署代码超界不是已经 176 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-3860](https://eips.ethereum.org/EIPS/eip-3860)（Final, Core, Limit and meter initcode）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-3860 initcode-bound not already 170-runtime / not already 1014 / not already 176-bundled 正式三事（176 余量）/ not 1437 icode-not170 interchangeable / not 176 initcode-vs-runtime bundled interchangeable」，不是 initcode vs runtime bundled（176），也不是已经 返回代码≠initcode（185），也不是已经 上限≠还能加（175）。不要另写 怎样造超长 initcode、怎样用工厂一次塞多层合约去撞界。

## 官方三件事

1. **看见initcode 超界不是已经是部署代码超界 / 看见initcode 超界不是已经是部署代码超界 这份对象 is not already 已经是部署代码超界 interchangeable，也不是已经 initcode vs runtime bundled（176） interchangeable / 1437 icode-not170 interchangeable / 1438 icode-nottx interchangeable，也不是已经 EIP-3860 initcode-bound not already 170-runtime / not already 1014 / not already 176-bundled 正式三事 bundled（176 item 1 余量） interchangeable / 176 icode item 1 interchangeable。**  
   官方把initcode 超界不是已经是部署代码超界和已经是部署代码超界写成两件。看见initcode 超界不是已经是部署代码超界，不是已经是部署代码超界。

2. **看见initcode bound is not already the 170 runtime bound / 看见initcode 超界不是已经是部署代码超界 / 这份对象 is not already 已经是 1014 哈希费 interchangeable，也不是已经 initcode vs runtime bundled（176） interchangeable / 1437 icode-not170 interchangeable / 1439 icode-notrun interchangeable，也不是已经 返回代码≠initcode interchangeable / 185 返回代码≠initcode interchangeable。**  
   官方把initcode bound is not already the 170 runtime bound和已经是 1014 哈希费写成两件。看见initcode bound is not already the 170 runtime bound，不是已经是 1014 哈希费。

3. **看见initcode 超界不是已经是部署代码超界 / 看见initcode bound is not already the 170 runtime bound / 这份对象 is not already 已经 176 bundled interchangeable，也不是已经 initcode vs runtime bundled（176） interchangeable / 1437 icode-not170 interchangeable / 1438 icode-nottx interchangeable，也不是已经 上限≠还能加 interchangeable / 175 上限≠还能加 interchangeable。**  
   官方把initcode 超界不是已经是部署代码超界和已经 176 bundled写成两件。看见initcode 超界不是已经是部署代码超界，不是已经 176 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造超长 initcode、怎样用工厂一次塞多层合约去撞界。

## 官方为什么这样拆

- **initcode 超界不是已经是部署代码超界 interchangeable：官方写本页扩展 170，170 管运行时代码，本页管还没跑的构造代码。**
- **看见本页不是已经是 1014 哈希费。**
- **看见读数旋钮不是已经 176 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是部署代码超界 | 不是已经是部署代码超界 | 不是已经返回代码≠initcode（185） |
| 已经是 1014 哈希费 | 不是已经是 1014 哈希费 | 不是已经上限≠还能加（175） |
| 已经 176 bundled | 不是已经 176 bundled | 不是已经1438 icode-nottx |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3860 initcode-bound not already 170-runtime / not already 1014 / not already 176-bundled 正式三事（176 余量），必须分开是不是已经是部署代码超界、是不是已经是 1014 哈希费、是不是已经 176 bundled。可以跳过「一份上限管两种代码」。不要另写 怎样造超长 initcode、怎样用工厂一次塞多层合约去撞界。176 initcode vs runtime bundled unbundling 在本页 item 1 启动；续 [`worked-example-icode-nottx-vs-bundled.md`](worked-example-icode-nottx-vs-bundled.md)（不变量 1438 item 2）。

## 本页不抄

- 上限字节、每字气价、部署代码上限、例工厂。
- 怎样造超长 initcode、怎样用工厂一次塞多层合约去撞界。
