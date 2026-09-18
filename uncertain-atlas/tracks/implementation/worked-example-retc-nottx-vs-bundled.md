# 例：看见这次失败是耗尽气不是已经整笔非法不是已经整笔非法；看见OOG fail is not already whole-tx illegal不是已经是带回剩余气的回滚；看见这次失败是耗尽气不是已经整笔非法不是已经是不变量 177

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-170](https://eips.ethereum.org/EIPS/eip-170)（Final, Core, Contract code size limit）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-170 oog-fail not already whole-tx-illegal / not already leftover-gas / not already 177 正式三事（185 余量）/ not 1441 retc-nottx interchangeable / not 185 returned-vs-initcode bundled interchangeable」，不是 returned vs initcode bundled（185），也不是已经 回滚≠烧光（177），也不是已经 initcode≠运行时代码（176）。不要另写 怎样造超长返回代码。

## 官方三件事

1. **看见这次失败是耗尽气不是已经整笔非法 / 看见这次失败是耗尽气不是已经整笔非法 这份对象 is not already 已经整笔非法 interchangeable，也不是已经 returned vs initcode bundled（185） interchangeable / 1441 retc-nottx interchangeable / 1440 retc-notinit interchangeable，也不是已经 EIP-170 oog-fail not already whole-tx-illegal / not already leftover-gas / not already 177 正式三事 bundled（185 item 2 余量） interchangeable / 185 retc item 2 interchangeable。**  
   官方把这次失败是耗尽气不是已经整笔非法和已经整笔非法写成两件。看见这次失败是耗尽气不是已经整笔非法，不是已经整笔非法。

2. **看见OOG fail is not already whole-tx illegal / 看见这次失败是耗尽气不是已经整笔非法 / 这份对象 is not already 已经是带回剩余气的回滚 interchangeable，也不是已经 returned vs initcode bundled（185） interchangeable / 1441 retc-nottx interchangeable / 1442 retc-notfree interchangeable，也不是已经 回滚≠烧光 interchangeable / 177 回滚≠烧光 interchangeable。**  
   官方把OOG fail is not already whole-tx illegal和已经是带回剩余气的回滚写成两件。看见OOG fail is not already whole-tx illegal，不是已经是带回剩余气的回滚。

3. **看见这次失败是耗尽气不是已经整笔非法 / 看见OOG fail is not already whole-tx illegal / 这份对象 is not already 已经是不变量 177 interchangeable，也不是已经 returned vs initcode bundled（185） interchangeable / 1441 retc-nottx interchangeable / 1440 retc-notinit interchangeable，也不是已经 initcode≠运行时代码 interchangeable / 176 initcode≠运行时代码 interchangeable。**  
   官方把这次失败是耗尽气不是已经整笔非法和已经是不变量 177写成两件。看见这次失败是耗尽气不是已经整笔非法，不是已经是不变量 177。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造超长返回代码。

## 官方为什么这样拆

- **这次失败是耗尽气不是已经整笔非法 interchangeable：官方写返回超界按耗尽气处理，不是 3860 创建交易那种整笔非法。**
- **看见本页不是已经是带回剩余气的回滚。**
- **看见本页不是已经是不变量 177。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经整笔非法 | 不是已经整笔非法 | 不是已经回滚≠烧光（177） |
| 已经是带回剩余气的回滚 | 不是已经是带回剩余气的回滚 | 不是已经initcode≠运行时代码（176） |
| 已经是不变量 177 | 不是已经是不变量 177 | 不是已经1440 retc-notinit |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-170 oog-fail not already whole-tx-illegal / not already leftover-gas / not already 177 正式三事（185 余量），必须分开是不是已经整笔非法、是不是已经是带回剩余气的回滚、是不是已经是不变量 177。可以跳过「规范 170 就已经是不变量 170」。不要另写 怎样造超长返回代码。185 returned vs initcode bundled unbundling 在本页 item 2 续；续 [`worked-example-retc-notfree-vs-bundled.md`](worked-example-retc-notfree-vs-bundled.md)（不变量 1442 item 3）。

## 本页不抄

- 上限字节、分叉高度、链号、气价表。
- 怎样造超长返回代码。
