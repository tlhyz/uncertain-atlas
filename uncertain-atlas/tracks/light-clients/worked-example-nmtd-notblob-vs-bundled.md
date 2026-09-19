# 例：看见DAS抽样过关不是已经拿到自己的blob不是已经拿到自己的blob；看见a DAS sample pass is not already holding your own blob不是已经是不变量 142；看见DAS抽样过关不是已经拿到自己的blob不是已经是不变量 9

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Celestia [NMT](https://docs.celestia.org/learn/celestia-101/data-availability/)（Namespace Merkle Tree vs DAS；官方文档）。  
**对应课文**：[L7.2](../../courses/level-07-modular/L07-M02-data-availability.md)。  
**不要写进**：`index/03` 共识行、M7.2、L7.2。本页是「NMT das-pass not already own-blob / not already 142 / not already 9 正式三事（124 余量）/ not 1513 nmtd-notblob interchangeable / not 124 nmt-vs-das bundled interchangeable」，不是 nmt vs das bundled（124），也不是已经 DACert≠已贴文（142），也不是已经 提交≠兑付（9）。不要另写 怎样扣份额、怎样印错扩展。

## 官方三件事

1. **看见DAS抽样过关不是已经拿到自己的blob / 看见DAS抽样过关不是已经拿到自己的blob 这份对象 is not already 已经拿到自己的blob interchangeable，也不是已经 nmt vs das bundled（124） interchangeable / 1513 nmtd-notblob interchangeable / 1512 nmtd-notsq interchangeable，也不是已经 NMT das-pass not already own-blob / not already 142 / not already 9 正式三事 bundled（124 item 2 余量） interchangeable / 124 nmtd item 2 interchangeable。**  
   官方把DAS抽样过关不是已经拿到自己的blob和已经拿到自己的blob写成两件。看见DAS抽样过关不是已经拿到自己的blob，不是已经拿到自己的blob。

2. **看见a DAS sample pass is not already holding your own blob / 看见DAS抽样过关不是已经拿到自己的blob / 这份对象 is not already 已经是不变量 142 interchangeable，也不是已经 nmt vs das bundled（124） interchangeable / 1513 nmtd-notblob interchangeable / 1514 nmtd-notenc interchangeable，也不是已经 DACert≠已贴文 interchangeable / 142 DACert≠已贴文 interchangeable。**  
   官方把a DAS sample pass is not already holding your own blob和已经是不变量 142写成两件。看见a DAS sample pass is not already holding your own blob，不是已经是不变量 142。

3. **看见DAS抽样过关不是已经拿到自己的blob / 看见a DAS sample pass is not already holding your own blob / 这份对象 is not already 已经是不变量 9 interchangeable，也不是已经 nmt vs das bundled（124） interchangeable / 1513 nmtd-notblob interchangeable / 1512 nmtd-notsq interchangeable，也不是已经 提交≠兑付 interchangeable / 9 提交≠兑付 interchangeable。**  
   官方把DAS抽样过关不是已经拿到自己的blob和已经是不变量 9写成两件。看见DAS抽样过关不是已经拿到自己的blob，不是已经是不变量 9。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样扣份额、怎样印错扩展。

## 官方为什么这样拆

- **DAS抽样过关不是已经拿到自己的blob interchangeable：官方写随机格子答上了，口袋里仍没有自己的命名空间字节。**
- **看见本页不是已经是不变量 142。**
- **看见本页不是已经是不变量 9。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经拿到自己的blob | 不是已经拿到自己的blob | 不是已经DACert≠已贴文（142） |
| 已经是不变量 142 | 不是已经是不变量 142 | 不是已经提交≠兑付（9） |
| 已经是不变量 9 | 不是已经是不变量 9 | 不是已经1512 nmtd-notsq |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 NMT das-pass not already own-blob / not already 142 / not already 9 正式三事（124 余量），必须分开是不是已经拿到自己的blob、是不是已经是不变量 142、是不是已经是不变量 9。可以跳过「看见 NMT 齐了就已经整块可用」。不要另写 怎样扣份额、怎样印错扩展。124 nmt vs das bundled unbundling 在本页 item 2 续；续 [`worked-example-nmtd-notenc-vs-bundled.md`](worked-example-nmtd-notenc-vs-bundled.md)（不变量 1514 item 3）。

## 本页不抄

- FAQ百分比、方阵边长、中间根个数、示例份额标签。
- 怎样扣份额、怎样印错扩展。
