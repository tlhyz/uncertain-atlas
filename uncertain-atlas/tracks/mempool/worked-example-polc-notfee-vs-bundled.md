# 例：看见费率高不是更正确不是已经更正确；看见a higher fee is not already more correct不是已经是不变量 245；看见费率高不是更正确不是已经是不变量 44

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin Core [Policy](https://github.com/bitcoin/bitcoin/blob/master/doc/policy/README.md)（Transaction Relay Policy；官方节点文档，不是冻结共识规范）。  
**对应课文**：[L3.2](../../courses/level-03-bitcoin/L03-M02-fees-and-standardness.md)。  
**不要写进**：`index/03` 共识行、M3.2、L3.2。本页是「Policy higher-fee not already more-correct / not already 245 / not already 44 正式三事（144 余量）/ not 1523 polc-notfee interchangeable / not 144 policy-vs-consensus bundled interchangeable」，不是 policy vs consensus bundled（144），也不是已经 费率过滤≠已拒池（245），也不是已经 入池拒绝≠免费（44）。不要另写 怎样把非标准塞进块、怎样 RBF 钉死。

## 官方三件事

1. **看见费率高不是更正确 / 看见费率高不是更正确 这份对象 is not already 已经更正确 interchangeable，也不是已经 policy vs consensus bundled（144） interchangeable / 1523 polc-notfee interchangeable / 1521 polc-notill interchangeable，也不是已经 Policy higher-fee not already more-correct / not already 245 / not already 44 正式三事 bundled（144 item 3 余量） interchangeable / 144 polc item 3 interchangeable。**  
   官方把费率高不是更正确和已经更正确写成两件。看见费率高不是更正确，不是已经更正确。

2. **看见a higher fee is not already more correct / 看见费率高不是更正确 / 这份对象 is not already 已经是不变量 245 interchangeable，也不是已经 policy vs consensus bundled（144） interchangeable / 1523 polc-notfee interchangeable / 1522 polc-notblk interchangeable，也不是已经 费率过滤≠已拒池 interchangeable / 245 费率过滤≠已拒池 interchangeable。**  
   官方把a higher fee is not already more correct和已经是不变量 245写成两件。看见a higher fee is not already more correct，不是已经是不变量 245。

3. **看见费率高不是更正确 / 看见a higher fee is not already more correct / 这份对象 is not already 已经是不变量 44 interchangeable，也不是已经 policy vs consensus bundled（144） interchangeable / 1523 polc-notfee interchangeable / 1521 polc-notill interchangeable，也不是已经 入池拒绝≠免费 interchangeable / 44 入池拒绝≠免费 interchangeable。**  
   官方把费率高不是更正确和已经是不变量 44写成两件。看见费率高不是更正确，不是已经是不变量 44。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把非标准塞进块、怎样 RBF 钉死。

## 官方为什么这样拆

- **费率高不是更正确 interchangeable：官方写 base fee 是输入减输出，正确性在脚本与无双花。**
- **看见本页不是已经是不变量 245。**
- **看见本页不是已经是不变量 44。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经更正确 | 不是已经更正确 | 不是已经费率过滤≠已拒池（245） |
| 已经是不变量 245 | 不是已经是不变量 245 | 不是已经入池拒绝≠免费（44） |
| 已经是不变量 44 | 不是已经是不变量 44 | 不是已经1521 polc-notill |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Policy higher-fee not already more-correct / not already 245 / not already 44 正式三事（144 余量），必须分开是不是已经更正确、是不是已经是不变量 245、是不是已经是不变量 44。可以跳过「看见邻居不转发就已经共识非法」。不要另写 怎样把非标准塞进块、怎样 RBF 钉死。144 policy vs consensus bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的官方对象：rbf-signal（166）。

## 本页不抄

- 默认费率、灰尘、祖先条数、簇上限。
- 怎样把非标准塞进块、怎样 RBF 钉死。
