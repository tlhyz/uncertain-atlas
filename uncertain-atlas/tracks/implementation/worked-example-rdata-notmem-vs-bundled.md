# 例：看见返回数据缓冲不是已经是内存不是已经是内存；看见returndata buffer is not already memory不是已经是 CALL 预留输出区；看见返回数据缓冲不是已经是内存不是已经 232 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-211](https://eips.ethereum.org/EIPS/eip-211)（Final, Core, RETURNDATASIZE / RETURNDATACOPY）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-211 returndata-buffer not already memory / not already CALL-out / not already 232-bundled 正式三事（232 余量）/ not 1386 rdata-notmem interchangeable / not 232 returndata-vs-memory bundled interchangeable」，不是 returndata vs memory bundled（232），也不是已经 回滚≠烧光（177），也不是已经 内存拷≠身份预编译（216）。不要另写 怎样做通用转发合约、怎样在失败后再抽超长回滚数据、怎样把缓冲和内存叠成同一块后备。

## 官方三件事

1. **看见返回数据缓冲不是已经是内存 / 看见返回数据缓冲不是已经是内存 这份对象 is not already 已经是内存 interchangeable，也不是已经 returndata vs memory bundled（232） interchangeable / 1386 rdata-notmem interchangeable / 1387 rdata-notcalld interchangeable，也不是已经 EIP-211 returndata-buffer not already memory / not already CALL-out / not already 232-bundled 正式三事 bundled（232 item 1 余量） interchangeable / 232 rdata item 1 interchangeable。**  
   官方把返回数据缓冲不是已经是内存和已经是内存写成两件。看见返回数据缓冲不是已经是内存，不是已经是内存。

2. **看见returndata buffer is not already memory / 看见返回数据缓冲不是已经是内存 / 这份对象 is not already 已经是 CALL 预留输出区 interchangeable，也不是已经 returndata vs memory bundled（232） interchangeable / 1386 rdata-notmem interchangeable / 1388 rdata-not140 interchangeable，也不是已经 回滚≠烧光 interchangeable / 177 回滚≠烧光 interchangeable。**  
   官方把returndata buffer is not already memory和已经是 CALL 预留输出区写成两件。看见returndata buffer is not already memory，不是已经是 CALL 预留输出区。

3. **看见返回数据缓冲不是已经是内存 / 看见returndata buffer is not already memory / 这份对象 is not already 已经 232 bundled interchangeable，也不是已经 returndata vs memory bundled（232） interchangeable / 1386 rdata-notmem interchangeable / 1387 rdata-notcalld interchangeable，也不是已经 内存拷≠身份预编译 interchangeable / 216 内存拷≠身份预编译 interchangeable。**  
   官方把返回数据缓冲不是已经是内存和已经 232 bundled写成两件。看见返回数据缓冲不是已经是内存，不是已经 232 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样做通用转发合约、怎样在失败后再抽超长回滚数据、怎样把缓冲和内存叠成同一块后备。

## 官方为什么这样拆

- **返回数据缓冲不是已经是内存 interchangeable：官方把虚拟缓冲和调用方内存写成两件。**
- **看见缓冲不是已经是 CALL 预留输出区。**
- **看见缓冲旋钮不是已经 232 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是内存 | 不是已经是内存 | 不是已经回滚≠烧光（177） |
| 已经是 CALL 预留输出区 | 不是已经是 CALL 预留输出区 | 不是已经内存拷≠身份预编译（216） |
| 已经 232 bundled | 不是已经 232 bundled | 不是已经1387 rdata-notcalld |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-211 returndata-buffer not already memory / not already CALL-out / not already 232-bundled 正式三事（232 余量），必须分开是不是已经是内存、是不是已经是 CALL 预留输出区、是不是已经 232 bundled。可以跳过「看见返回数据缓冲就已经是内存」。不要另写 怎样做通用转发合约、怎样在失败后再抽超长回滚数据、怎样把缓冲和内存叠成同一块后备。232 returndata buffer vs memory bundled unbundling 在本页 item 1 启动；续 [`worked-example-rdata-notcalld-vs-bundled.md`](worked-example-rdata-notcalld-vs-bundled.md)（不变量 1387 item 2）。

## 本页不抄

- 操作码号、气价公式、分叉块号。
- 怎样做通用转发合约、怎样在失败后再抽超长回滚数据、怎样把缓冲和内存叠成同一块后备。
