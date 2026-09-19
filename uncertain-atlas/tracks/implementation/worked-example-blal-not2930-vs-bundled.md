# 例：看见强制名单不是已经是2930不是已经是2930；看见forced list is not already 2930不是已经是不变量 143；看见强制名单不是已经是2930不是已经是不变量 122

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7928](https://eips.ethereum.org/EIPS/eip-7928)（Block-Level Access Lists）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7928 forced-list not already 2930 / not already 143 / not already 122 正式三事（212 余量）/ not 1477 blal-not2930 interchangeable / not 212 block-list-vs-parallel bundled interchangeable」，不是 block list vs parallel bundled（212），也不是已经 谓词过了≠脚本已跑（143），也不是已经 STM跑完≠最终（122）。不要另写 怎样造名单、怎样申报从未碰过的只读槽。

## 官方三件事

1. **看见强制名单不是已经是2930 / 看见强制名单不是已经是2930 这份对象 is not already 已经是2930 interchangeable，也不是已经 block list vs parallel bundled（212） interchangeable / 1477 blal-not2930 interchangeable / 1476 blal-notpar interchangeable，也不是已经 EIP-7928 forced-list not already 2930 / not already 143 / not already 122 正式三事 bundled（212 item 2 余量） interchangeable / 212 blal item 2 interchangeable。**  
   官方把强制名单不是已经是2930和已经是2930写成两件。看见强制名单不是已经是2930，不是已经是2930。

2. **看见forced list is not already 2930 / 看见强制名单不是已经是2930 / 这份对象 is not already 已经是不变量 143 interchangeable，也不是已经 block list vs parallel bundled（212） interchangeable / 1477 blal-not2930 interchangeable / 1478 blal-notrun interchangeable，也不是已经 谓词过了≠脚本已跑 interchangeable / 143 谓词过了≠脚本已跑 interchangeable。**  
   官方把forced list is not already 2930和已经是不变量 143写成两件。看见forced list is not already 2930，不是已经是不变量 143。

3. **看见强制名单不是已经是2930 / 看见forced list is not already 2930 / 这份对象 is not already 已经是不变量 122 interchangeable，也不是已经 block list vs parallel bundled（212） interchangeable / 1477 blal-not2930 interchangeable / 1476 blal-notpar interchangeable，也不是已经 STM跑完≠最终 interchangeable / 122 STM跑完≠最终 interchangeable。**  
   官方把强制名单不是已经是2930和已经是不变量 122写成两件。看见强制名单不是已经是2930，不是已经是不变量 122。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造名单、怎样申报从未碰过的只读槽。

## 官方为什么这样拆

- **强制名单不是已经是2930 interchangeable：官方写 2930 是可选的交易级名单并不强制，本页是块级强制。**
- **看见本页不是已经是不变量 143。**
- **看见本页不是已经是不变量 122。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是2930 | 不是已经是2930 | 不是已经谓词过了≠脚本已跑（143） |
| 已经是不变量 143 | 不是已经是不变量 143 | 不是已经STM跑完≠最终（122） |
| 已经是不变量 122 | 不是已经是不变量 122 | 不是已经1476 blal-notpar |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7928 forced-list not already 2930 / not already 143 / not already 122 正式三事（212 余量），必须分开是不是已经是2930、是不是已经是不变量 143、是不是已经是不变量 122。可以跳过「看见 7928 就已经并行」。不要另写 怎样造名单、怎样申报从未碰过的只读槽。212 block-list vs parallel bundled unbundling 在本页 item 2 续；续 [`worked-example-blal-notrun-vs-bundled.md`](worked-example-blal-notrun-vs-bundled.md)（不变量 1478 item 3）。

## 本页不抄

- 条数上限、气价、地址、示例名单、体积估算。
- 怎样造名单、怎样申报从未碰过的只读槽。
