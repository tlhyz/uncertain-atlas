# 例：看见块级访问名单不是已经并行跑完不是已经并行跑完；看见block-level access list is not already parallel-done不是已经是不变量 168；看见块级访问名单不是已经并行跑完不是已经 212 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7928](https://eips.ethereum.org/EIPS/eip-7928)（Block-Level Access Lists）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7928 block-list not already parallel-done / not already 168 / not already 212-bundled 正式三事（212 余量）/ not 1476 blal-notpar interchangeable / not 212 block-list-vs-parallel bundled interchangeable」，不是 block list vs parallel bundled（212），也不是已经 列出≠已访问（168），也不是已经 谓词过了≠脚本已跑（143）。不要另写 怎样造名单、怎样申报从未碰过的只读槽。

## 官方三件事

1. **看见块级访问名单不是已经并行跑完 / 看见块级访问名单不是已经并行跑完 这份对象 is not already 已经并行跑完 interchangeable，也不是已经 block list vs parallel bundled（212） interchangeable / 1476 blal-notpar interchangeable / 1477 blal-not2930 interchangeable，也不是已经 EIP-7928 block-list not already parallel-done / not already 168 / not already 212-bundled 正式三事 bundled（212 item 1 余量） interchangeable / 212 blal item 1 interchangeable。**  
   官方把块级访问名单不是已经并行跑完和已经并行跑完写成两件。看见块级访问名单不是已经并行跑完，不是已经并行跑完。

2. **看见block-level access list is not already parallel-done / 看见块级访问名单不是已经并行跑完 / 这份对象 is not already 已经是不变量 168 interchangeable，也不是已经 block list vs parallel bundled（212） interchangeable / 1476 blal-notpar interchangeable / 1478 blal-notrun interchangeable，也不是已经 列出≠已访问 interchangeable / 168 列出≠已访问 interchangeable。**  
   官方把block-level access list is not already parallel-done和已经是不变量 168写成两件。看见block-level access list is not already parallel-done，不是已经是不变量 168。

3. **看见块级访问名单不是已经并行跑完 / 看见block-level access list is not already parallel-done / 这份对象 is not already 已经 212 bundled interchangeable，也不是已经 block list vs parallel bundled（212） interchangeable / 1476 blal-notpar interchangeable / 1477 blal-not2930 interchangeable，也不是已经 谓词过了≠脚本已跑 interchangeable / 143 谓词过了≠脚本已跑 interchangeable。**  
   官方把块级访问名单不是已经并行跑完和已经 212 bundled写成两件。看见块级访问名单不是已经并行跑完，不是已经 212 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造名单、怎样申报从未碰过的只读槽。

## 官方为什么这样拆

- **块级访问名单不是已经并行跑完 interchangeable：官方写本页能用来并行读盘、并行验交易，看见本页不是这些已经发生。**
- **看见本页不是已经是不变量 168。**
- **看见读数旋钮不是已经 212 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经并行跑完 | 不是已经并行跑完 | 不是已经列出≠已访问（168） |
| 已经是不变量 168 | 不是已经是不变量 168 | 不是已经谓词过了≠脚本已跑（143） |
| 已经 212 bundled | 不是已经 212 bundled | 不是已经1477 blal-not2930 |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7928 block-list not already parallel-done / not already 168 / not already 212-bundled 正式三事（212 余量），必须分开是不是已经并行跑完、是不是已经是不变量 168、是不是已经 212 bundled。可以跳过「看见 7928 就已经并行」。不要另写 怎样造名单、怎样申报从未碰过的只读槽。212 block-list vs parallel bundled unbundling 在本页 item 1 启动；续 [`worked-example-blal-not2930-vs-bundled.md`](worked-example-blal-not2930-vs-bundled.md)（不变量 1477 item 2）。

## 本页不抄

- 条数上限、气价、地址、示例名单、体积估算。
- 怎样造名单、怎样申报从未碰过的只读槽。
