# 例：看见失败数据能再取不是已经是 140不是已经是 EIP-140；看见refetch fail data is not already 140不是输出区已经自动够大；看见失败数据能再取不是已经是 140不是通用转发产品已经上线

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-211](https://eips.ethereum.org/EIPS/eip-211)（Final, Core, RETURNDATASIZE / RETURNDATACOPY）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-211 refetch-fail-data not already 140 / not already auto-sized-out / not already forwarder-product 正式三事（232 余量）/ not 1388 rdata-not140 interchangeable / not 232 returndata-vs-memory bundled interchangeable」，不是 returndata vs memory bundled（232），也不是已经 EIP-140 REVERT（177），也不是已经 返回缓冲别名 CVE（3）。不要另写 怎样做通用转发合约、怎样在失败后再抽超长回滚数据、怎样把缓冲和内存叠成同一块后备。

## 官方三件事

1. **看见失败数据能再取不是已经是 140 / 看见失败数据能再取不是已经是 140 这份对象 is not already 已经是 EIP-140 interchangeable，也不是已经 returndata vs memory bundled（232） interchangeable / 1388 rdata-not140 interchangeable / 1386 rdata-notmem interchangeable，也不是已经 EIP-211 refetch-fail-data not already 140 / not already auto-sized-out / not already forwarder-product 正式三事 bundled（232 item 3 余量） interchangeable / 232 rdata item 3 interchangeable。**  
   官方把失败数据能再取不是已经是 140和已经是 EIP-140写成两件。看见失败数据能再取不是已经是 140，不是已经是 EIP-140。

2. **看见refetch fail data is not already 140 / 看见失败数据能再取不是已经是 140 / 这份对象 is not already 输出区已经自动够大 interchangeable，也不是已经 returndata vs memory bundled（232） interchangeable / 1388 rdata-not140 interchangeable / 1387 rdata-notcalld interchangeable，也不是已经 EIP-140 REVERT interchangeable / 177 EIP-140 REVERT interchangeable。**  
   官方把refetch fail data is not already 140和输出区已经自动够大写成两件。看见refetch fail data is not already 140，不是输出区已经自动够大。

3. **看见失败数据能再取不是已经是 140 / 看见refetch fail data is not already 140 / 这份对象 is not already 通用转发产品已经上线 interchangeable，也不是已经 returndata vs memory bundled（232） interchangeable / 1388 rdata-not140 interchangeable / 1386 rdata-notmem interchangeable，也不是已经 返回缓冲别名 CVE interchangeable / 3 返回缓冲别名 CVE interchangeable。**  
   官方把失败数据能再取不是已经是 140和通用转发产品已经上线写成两件。看见失败数据能再取不是已经是 140，不是通用转发产品已经上线。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样做通用转发合约、怎样在失败后再抽超长回滚数据、怎样把缓冲和内存叠成同一块后备。

## 官方为什么这样拆

- **失败数据能再取不是已经是 140 interchangeable：官方写本页让 140 更好用，不是已经是 140。**
- **看见能再取不是输出区已经自动够大。**
- **看见本页不是通用转发产品已经上线。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是 EIP-140 | 不是已经是 EIP-140 | 不是已经EIP-140 REVERT（177） |
| 输出区已经自动够大 | 不是输出区已经自动够大 | 不是已经返回缓冲别名 CVE（3） |
| 通用转发产品已经上线 | 不是通用转发产品已经上线 | 不是已经1386 rdata-notmem |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-211 refetch-fail-data not already 140 / not already auto-sized-out / not already forwarder-product 正式三事（232 余量），必须分开是不是已经是 EIP-140、是不是输出区已经自动够大、是不是通用转发产品已经上线。可以跳过「看见返回数据缓冲就已经是内存」。不要另写 怎样做通用转发合约、怎样在失败后再抽超长回滚数据、怎样把缓冲和内存叠成同一块后备。232 returndata buffer vs memory bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：EIP-1014 CREATE2（222）。

## 本页不抄

- 操作码号、气价公式、分叉块号。
- 怎样做通用转发合约、怎样在失败后再抽超长回滚数据、怎样把缓冲和内存叠成同一块后备。
