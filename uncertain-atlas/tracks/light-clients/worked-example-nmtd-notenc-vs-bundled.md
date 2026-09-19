# 例：看见DAS抽样过关不是扩展编码已经诚实不是已经编码诚实；看见a DAS sample pass is not already honest erasure encoding不是已经是不变量 23；看见DAS抽样过关不是扩展编码已经诚实不是已经是不变量 142

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Celestia [NMT](https://docs.celestia.org/learn/celestia-101/data-availability/)（Namespace Merkle Tree vs DAS；官方文档）。  
**对应课文**：[L7.2](../../courses/level-07-modular/L07-M02-data-availability.md)。  
**不要写进**：`index/03` 共识行、M7.2、L7.2。本页是「NMT das-pass not already honest-encoding / not already 23 / not already 142 正式三事（124 余量）/ not 1514 nmtd-notenc interchangeable / not 124 nmt-vs-das bundled interchangeable」，不是 nmt vs das bundled（124），也不是已经 KZG≠DAS（23），也不是已经 DACert≠已贴文（142）。不要另写 怎样扣份额、怎样印错扩展。

## 官方三件事

1. **看见DAS抽样过关不是扩展编码已经诚实 / 看见DAS抽样过关不是扩展编码已经诚实 这份对象 is not already 已经编码诚实 interchangeable，也不是已经 nmt vs das bundled（124） interchangeable / 1514 nmtd-notenc interchangeable / 1512 nmtd-notsq interchangeable，也不是已经 NMT das-pass not already honest-encoding / not already 23 / not already 142 正式三事 bundled（124 item 3 余量） interchangeable / 124 nmtd item 3 interchangeable。**  
   官方把DAS抽样过关不是扩展编码已经诚实和已经编码诚实写成两件。看见DAS抽样过关不是扩展编码已经诚实，不是已经编码诚实。

2. **看见a DAS sample pass is not already honest erasure encoding / 看见DAS抽样过关不是扩展编码已经诚实 / 这份对象 is not already 已经是不变量 23 interchangeable，也不是已经 nmt vs das bundled（124） interchangeable / 1514 nmtd-notenc interchangeable / 1513 nmtd-notblob interchangeable，也不是已经 KZG≠DAS interchangeable / 23 KZG≠DAS interchangeable。**  
   官方把a DAS sample pass is not already honest erasure encoding和已经是不变量 23写成两件。看见a DAS sample pass is not already honest erasure encoding，不是已经是不变量 23。

3. **看见DAS抽样过关不是扩展编码已经诚实 / 看见a DAS sample pass is not already honest erasure encoding / 这份对象 is not already 已经是不变量 142 interchangeable，也不是已经 nmt vs das bundled（124） interchangeable / 1514 nmtd-notenc interchangeable / 1512 nmtd-notsq interchangeable，也不是已经 DACert≠已贴文 interchangeable / 142 DACert≠已贴文 interchangeable。**  
   官方把DAS抽样过关不是扩展编码已经诚实和已经是不变量 142写成两件。看见DAS抽样过关不是扩展编码已经诚实，不是已经是不变量 142。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样扣份额、怎样印错扩展。

## 官方为什么这样拆

- **DAS抽样过关不是扩展编码已经诚实 interchangeable：官方写扩展编错时抽到够多份额，原数据仍可能拼不回来。**
- **看见本页不是已经是不变量 23。**
- **看见本页不是已经是不变量 142。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经编码诚实 | 不是已经编码诚实 | 不是已经KZG≠DAS（23） |
| 已经是不变量 23 | 不是已经是不变量 23 | 不是已经DACert≠已贴文（142） |
| 已经是不变量 142 | 不是已经是不变量 142 | 不是已经1512 nmtd-notsq |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 NMT das-pass not already honest-encoding / not already 23 / not already 142 正式三事（124 余量），必须分开是不是已经编码诚实、是不是已经是不变量 23、是不是已经是不变量 142。可以跳过「看见 NMT 齐了就已经整块可用」。不要另写 怎样扣份额、怎样印错扩展。124 nmt vs das bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的官方对象：blob-vs-das（23）。

## 本页不抄

- FAQ百分比、方阵边长、中间根个数、示例份额标签。
- 怎样扣份额、怎样印错扩展。
