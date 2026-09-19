# 例：看见NMT证明命名空间齐了不是扩展方阵已经可用不是已经整块可用；看见an NMT namespace-complete proof is not already a usable extended square不是已经是不变量 23；看见NMT证明命名空间齐了不是扩展方阵已经可用不是已经 124 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Celestia [NMT](https://docs.celestia.org/learn/celestia-101/data-availability/)（Namespace Merkle Tree vs DAS；官方文档）。  
**对应课文**：[L7.2](../../courses/level-07-modular/L07-M02-data-availability.md)。  
**不要写进**：`index/03` 共识行、M7.2、L7.2。本页是「NMT nmt-complete not already square-available / not already 23 / not already 124-bundled 正式三事（124 余量）/ not 1512 nmtd-notsq interchangeable / not 124 nmt-vs-das bundled interchangeable」，不是 nmt vs das bundled（124），也不是已经 KZG≠DAS（23），也不是已经 DACert≠已贴文（142）。不要另写 怎样扣份额、怎样印错扩展。

## 官方三件事

1. **看见NMT证明命名空间齐了不是扩展方阵已经可用 / 看见NMT证明命名空间齐了不是扩展方阵已经可用 这份对象 is not already 已经整块可用 interchangeable，也不是已经 nmt vs das bundled（124） interchangeable / 1512 nmtd-notsq interchangeable / 1513 nmtd-notblob interchangeable，也不是已经 NMT nmt-complete not already square-available / not already 23 / not already 124-bundled 正式三事 bundled（124 item 1 余量） interchangeable / 124 nmtd item 1 interchangeable。**  
   官方把NMT证明命名空间齐了不是扩展方阵已经可用和已经整块可用写成两件。看见NMT证明命名空间齐了不是扩展方阵已经可用，不是已经整块可用。

2. **看见an NMT namespace-complete proof is not already a usable extended square / 看见NMT证明命名空间齐了不是扩展方阵已经可用 / 这份对象 is not already 已经是不变量 23 interchangeable，也不是已经 nmt vs das bundled（124） interchangeable / 1512 nmtd-notsq interchangeable / 1514 nmtd-notenc interchangeable，也不是已经 KZG≠DAS interchangeable / 23 KZG≠DAS interchangeable。**  
   官方把an NMT namespace-complete proof is not already a usable extended square和已经是不变量 23写成两件。看见an NMT namespace-complete proof is not already a usable extended square，不是已经是不变量 23。

3. **看见NMT证明命名空间齐了不是扩展方阵已经可用 / 看见an NMT namespace-complete proof is not already a usable extended square / 这份对象 is not already 已经 124 bundled interchangeable，也不是已经 nmt vs das bundled（124） interchangeable / 1512 nmtd-notsq interchangeable / 1513 nmtd-notblob interchangeable，也不是已经 DACert≠已贴文 interchangeable / 142 DACert≠已贴文 interchangeable。**  
   官方把NMT证明命名空间齐了不是扩展方阵已经可用和已经 124 bundled写成两件。看见NMT证明命名空间齐了不是扩展方阵已经可用，不是已经 124 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样扣份额、怎样印错扩展。

## 官方为什么这样拆

- **NMT证明命名空间齐了不是扩展方阵已经可用 interchangeable：官方写 NMT 证的是这一命名空间给齐，不是整块扩展方阵已经可用。**
- **看见本页不是已经是不变量 23。**
- **看见命名空间旋钮不是已经 124 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经整块可用 | 不是已经整块可用 | 不是已经KZG≠DAS（23） |
| 已经是不变量 23 | 不是已经是不变量 23 | 不是已经DACert≠已贴文（142） |
| 已经 124 bundled | 不是已经 124 bundled | 不是已经1513 nmtd-notblob |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 NMT nmt-complete not already square-available / not already 23 / not already 124-bundled 正式三事（124 余量），必须分开是不是已经整块可用、是不是已经是不变量 23、是不是已经 124 bundled。可以跳过「看见 NMT 齐了就已经整块可用」。不要另写 怎样扣份额、怎样印错扩展。124 nmt vs das bundled unbundling 在本页 item 1 启动；续 [`worked-example-nmtd-notblob-vs-bundled.md`](worked-example-nmtd-notblob-vs-bundled.md)（不变量 1513 item 2）。

## 本页不抄

- FAQ百分比、方阵边长、中间根个数、示例份额标签。
- 怎样扣份额、怎样印错扩展。
