# 例：看见AnyTrust不是已经Rollup DA不是已经是Rollup DA；看见AnyTrust is not already Rollup DA不是已经是不变量 124；看见AnyTrust不是已经Rollup DA不是已经是不变量 9

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Arbitrum [AnyTrust](https://docs.arbitrum.io/how-arbitrum-works/deep-dives/anytrust-protocol)（Data Availability Certificate；官方文档，不是冻结 Ethereum 规范）。  
**对应课文**：[L7.2](../../courses/level-07-modular/L07-M02-data-availability.md)。  
**不要写进**：`index/03` 共识行、M7.2、L7.2。本页是「AnyTrust anytrust not already rollup-da / not already 124 / not already 9 正式三事（142 余量）/ not 1510 dcert-notroll interchangeable / not 142 dacert-vs-posted bundled interchangeable」，不是 dacert vs posted bundled（142），也不是已经 NMT≠DAS（124），也不是已经 提交≠兑付（9）。不要另写 怎样让委员不给数据、怎样拼假证书。

## 官方三件事

1. **看见AnyTrust不是已经Rollup DA / 看见AnyTrust不是已经Rollup DA 这份对象 is not already 已经是Rollup DA interchangeable，也不是已经 dacert vs posted bundled（142） interchangeable / 1510 dcert-notroll interchangeable / 1509 dcert-notpost interchangeable，也不是已经 AnyTrust anytrust not already rollup-da / not already 124 / not already 9 正式三事 bundled（142 item 2 余量） interchangeable / 142 dcert item 2 interchangeable。**  
   官方把AnyTrust不是已经Rollup DA和已经是Rollup DA写成两件。看见AnyTrust不是已经Rollup DA，不是已经是Rollup DA。

2. **看见AnyTrust is not already Rollup DA / 看见AnyTrust不是已经Rollup DA / 这份对象 is not already 已经是不变量 124 interchangeable，也不是已经 dacert vs posted bundled（142） interchangeable / 1510 dcert-notroll interchangeable / 1511 dcert-notonly interchangeable，也不是已经 NMT≠DAS interchangeable / 124 NMT≠DAS interchangeable。**  
   官方把AnyTrust is not already Rollup DA和已经是不变量 124写成两件。看见AnyTrust is not already Rollup DA，不是已经是不变量 124。

3. **看见AnyTrust不是已经Rollup DA / 看见AnyTrust is not already Rollup DA / 这份对象 is not already 已经是不变量 9 interchangeable，也不是已经 dacert vs posted bundled（142） interchangeable / 1510 dcert-notroll interchangeable / 1509 dcert-notpost interchangeable，也不是已经 提交≠兑付 interchangeable / 9 提交≠兑付 interchangeable。**  
   官方把AnyTrust不是已经Rollup DA和已经是不变量 9写成两件。看见AnyTrust不是已经Rollup DA，不是已经是不变量 9。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样让委员不给数据、怎样拼假证书。

## 官方为什么这样拆

- **AnyTrust不是已经Rollup DA interchangeable：官方写它用温和信任假设换更低费用，不是已经和 Rollup 同一安全。**
- **看见本页不是已经是不变量 124。**
- **看见本页不是已经是不变量 9。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是Rollup DA | 不是已经是Rollup DA | 不是已经NMT≠DAS（124） |
| 已经是不变量 124 | 不是已经是不变量 124 | 不是已经提交≠兑付（9） |
| 已经是不变量 9 | 不是已经是不变量 9 | 不是已经1509 dcert-notpost |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 AnyTrust anytrust not already rollup-da / not already 124 / not already 9 正式三事（142 余量），必须分开是不是已经是Rollup DA、是不是已经是不变量 124、是不是已经是不变量 9。可以跳过「看见 Inbox 有一笔就已经贴了全文」。不要另写 怎样让委员不给数据、怎样拼假证书。142 dacert vs posted bundled unbundling 在本页 item 2 续；续 [`worked-example-dcert-notonly-vs-bundled.md`](worked-example-dcert-notonly-vs-bundled.md)（不变量 1511 item 3）。

## 本页不抄

- 委员会人数、诚实人数、过期天数、回退分钟、费率。
- 怎样让委员不给数据、怎样拼假证书。
