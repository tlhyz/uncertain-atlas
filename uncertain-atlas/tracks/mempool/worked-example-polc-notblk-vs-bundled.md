# 例：看见策略通过不是已经进块不是已经进块；看见a policy pass is not already inclusion in a block不是已经是不变量 25；看见策略通过不是已经进块不是已经是不变量 166

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin Core [Policy](https://github.com/bitcoin/bitcoin/blob/master/doc/policy/README.md)（Transaction Relay Policy；官方节点文档，不是冻结共识规范）。  
**对应课文**：[L3.2](../../courses/level-03-bitcoin/L03-M02-fees-and-standardness.md)。  
**不要写进**：`index/03` 共识行、M3.2、L3.2。本页是「Policy policy-pass not already in-block / not already 25 / not already 166 正式三事（144 余量）/ not 1522 polc-notblk interchangeable / not 144 policy-vs-consensus bundled interchangeable」，不是 policy vs consensus bundled（144），也不是已经 跳过须点名（25），也不是已经 RBF信号≠已替换（166）。不要另写 怎样把非标准塞进块、怎样 RBF 钉死。

## 官方三件事

1. **看见策略通过不是已经进块 / 看见策略通过不是已经进块 这份对象 is not already 已经进块 interchangeable，也不是已经 policy vs consensus bundled（144） interchangeable / 1522 polc-notblk interchangeable / 1521 polc-notill interchangeable，也不是已经 Policy policy-pass not already in-block / not already 25 / not already 166 正式三事 bundled（144 item 2 余量） interchangeable / 144 polc item 2 interchangeable。**  
   官方把策略通过不是已经进块和已经进块写成两件。看见策略通过不是已经进块，不是已经进块。

2. **看见a policy pass is not already inclusion in a block / 看见策略通过不是已经进块 / 这份对象 is not already 已经是不变量 25 interchangeable，也不是已经 policy vs consensus bundled（144） interchangeable / 1522 polc-notblk interchangeable / 1523 polc-notfee interchangeable，也不是已经 跳过须点名 interchangeable / 25 跳过须点名 interchangeable。**  
   官方把a policy pass is not already inclusion in a block和已经是不变量 25写成两件。看见a policy pass is not already inclusion in a block，不是已经是不变量 25。

3. **看见策略通过不是已经进块 / 看见a policy pass is not already inclusion in a block / 这份对象 is not already 已经是不变量 166 interchangeable，也不是已经 policy vs consensus bundled（144） interchangeable / 1522 polc-notblk interchangeable / 1521 polc-notill interchangeable，也不是已经 RBF信号≠已替换 interchangeable / 166 RBF信号≠已替换 interchangeable。**  
   官方把策略通过不是已经进块和已经是不变量 166写成两件。看见策略通过不是已经进块，不是已经是不变量 166。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把非标准塞进块、怎样 RBF 钉死。

## 官方为什么这样拆

- **策略通过不是已经进块 interchangeable：官方写策略只管未确认、进池之前，不作用于块内交易。**
- **看见本页不是已经是不变量 25。**
- **看见本页不是已经是不变量 166。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经进块 | 不是已经进块 | 不是已经跳过须点名（25） |
| 已经是不变量 25 | 不是已经是不变量 25 | 不是已经RBF信号≠已替换（166） |
| 已经是不变量 166 | 不是已经是不变量 166 | 不是已经1521 polc-notill |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Policy policy-pass not already in-block / not already 25 / not already 166 正式三事（144 余量），必须分开是不是已经进块、是不是已经是不变量 25、是不是已经是不变量 166。可以跳过「看见邻居不转发就已经共识非法」。不要另写 怎样把非标准塞进块、怎样 RBF 钉死。144 policy vs consensus bundled unbundling 在本页 item 2 续；续 [`worked-example-polc-notfee-vs-bundled.md`](worked-example-polc-notfee-vs-bundled.md)（不变量 1523 item 3）。

## 本页不抄

- 默认费率、灰尘、祖先条数、簇上限。
- 怎样把非标准塞进块、怎样 RBF 钉死。
