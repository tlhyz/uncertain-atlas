# 例：看见配置里的blob日程不是已经不需要分叉不是已经不需要分叉；看见a config blob schedule is not already a forkless change不是已经是不变量 201；看见配置里的blob日程不是已经不需要分叉不是已经是不变量 23

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7892](https://eips.ethereum.org/EIPS/eip-7892)（Blob Parameter Only Hardforks）。  
**对应课文**：[L5.4](../../courses/level-05-ethereum/L05-M04-state-blobs-mev.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7892 config-schedule not already forkless / not already 201 / not already 23 正式三事（209 余量）/ not 1504 bpof-notcfg interchangeable / not 209 bpo-vs-hardfork bundled interchangeable」，不是 bpo vs hardfork bundled（209），也不是已经 底价≠已并账（201），也不是已经 KZG≠DAS（23）。不要另写 怎样把执行层和共识层的日程对不齐。

## 官方三件事

1. **看见配置里的blob日程不是已经不需要分叉 / 看见配置里的blob日程不是已经不需要分叉 这份对象 is not already 已经不需要分叉 interchangeable，也不是已经 bpo vs hardfork bundled（209） interchangeable / 1504 bpof-notcfg interchangeable / 1503 bpof-notexec interchangeable，也不是已经 EIP-7892 config-schedule not already forkless / not already 201 / not already 23 正式三事 bundled（209 item 2 余量） interchangeable / 209 bpof item 2 interchangeable。**  
   官方把配置里的blob日程不是已经不需要分叉和已经不需要分叉写成两件。看见配置里的blob日程不是已经不需要分叉，不是已经不需要分叉。

2. **看见a config blob schedule is not already a forkless change / 看见配置里的blob日程不是已经不需要分叉 / 这份对象 is not already 已经是不变量 201 interchangeable，也不是已经 bpo vs hardfork bundled（209） interchangeable / 1504 bpof-notcfg interchangeable / 1505 bpof-notver interchangeable，也不是已经 底价≠已并账 interchangeable / 201 底价≠已并账 interchangeable。**  
   官方把a config blob schedule is not already a forkless change和已经是不变量 201写成两件。看见a config blob schedule is not already a forkless change，不是已经是不变量 201。

3. **看见配置里的blob日程不是已经不需要分叉 / 看见a config blob schedule is not already a forkless change / 这份对象 is not already 已经是不变量 23 interchangeable，也不是已经 bpo vs hardfork bundled（209） interchangeable / 1504 bpof-notcfg interchangeable / 1503 bpof-notexec interchangeable，也不是已经 KZG≠DAS interchangeable / 23 KZG≠DAS interchangeable。**  
   官方把配置里的blob日程不是已经不需要分叉和已经是不变量 23写成两件。看见配置里的blob日程不是已经不需要分叉，不是已经是不变量 23。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把执行层和共识层的日程对不齐。

## 官方为什么这样拆

- **配置里的blob日程不是已经不需要分叉 interchangeable：官方写新参数在写明的激活时刻立刻生效，仍是分叉。**
- **看见本页不是已经是不变量 201。**
- **看见本页不是已经是不变量 23。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经不需要分叉 | 不是已经不需要分叉 | 不是已经底价≠已并账（201） |
| 已经是不变量 201 | 不是已经是不变量 201 | 不是已经KZG≠DAS（23） |
| 已经是不变量 23 | 不是已经是不变量 23 | 不是已经1503 bpof-notexec |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7892 config-schedule not already forkless / not already 201 / not already 23 正式三事（209 余量），必须分开是不是已经不需要分叉、是不是已经是不变量 201、是不是已经是不变量 23。可以跳过「看见 7892 就已经改了执行」。不要另写 怎样把执行层和共识层的日程对不齐。209 bpo vs hardfork bundled unbundling 在本页 item 2 续；续 [`worked-example-bpof-notver-vs-bundled.md`](worked-example-bpof-notver-vs-bundled.md)（不变量 1505 item 3）。

## 本页不抄

- 目标条数、上限条数、调价分母、激活时间、示例日程。
- 怎样把执行层和共识层的日程对不齐。
