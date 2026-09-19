# 例：看见策略拒绝不是共识非法不是已经共识非法；看见a policy rejection is not already consensus-illegal不是已经是不变量 44；看见策略拒绝不是共识非法不是已经 144 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin Core [Policy](https://github.com/bitcoin/bitcoin/blob/master/doc/policy/README.md)（Transaction Relay Policy；官方节点文档，不是冻结共识规范）。  
**对应课文**：[L3.2](../../courses/level-03-bitcoin/L03-M02-fees-and-standardness.md)。  
**不要写进**：`index/03` 共识行、M3.2、L3.2。本页是「Policy policy-reject not already consensus-illegal / not already 44 / not already 144-bundled 正式三事（144 余量）/ not 1521 polc-notill interchangeable / not 144 policy-vs-consensus bundled interchangeable」，不是 policy vs consensus bundled（144），也不是已经 入池拒绝≠免费（44），也不是已经 跳过须点名（25）。不要另写 怎样把非标准塞进块、怎样 RBF 钉死。

## 官方三件事

1. **看见策略拒绝不是共识非法 / 看见策略拒绝不是共识非法 这份对象 is not already 已经共识非法 interchangeable，也不是已经 policy vs consensus bundled（144） interchangeable / 1521 polc-notill interchangeable / 1522 polc-notblk interchangeable，也不是已经 Policy policy-reject not already consensus-illegal / not already 44 / not already 144-bundled 正式三事 bundled（144 item 1 余量） interchangeable / 144 polc item 1 interchangeable。**  
   官方把策略拒绝不是共识非法和已经共识非法写成两件。看见策略拒绝不是共识非法，不是已经共识非法。

2. **看见a policy rejection is not already consensus-illegal / 看见策略拒绝不是共识非法 / 这份对象 is not already 已经是不变量 44 interchangeable，也不是已经 policy vs consensus bundled（144） interchangeable / 1521 polc-notill interchangeable / 1523 polc-notfee interchangeable，也不是已经 入池拒绝≠免费 interchangeable / 44 入池拒绝≠免费 interchangeable。**  
   官方把a policy rejection is not already consensus-illegal和已经是不变量 44写成两件。看见a policy rejection is not already consensus-illegal，不是已经是不变量 44。

3. **看见策略拒绝不是共识非法 / 看见a policy rejection is not already consensus-illegal / 这份对象 is not already 已经 144 bundled interchangeable，也不是已经 policy vs consensus bundled（144） interchangeable / 1521 polc-notill interchangeable / 1522 polc-notblk interchangeable，也不是已经 跳过须点名 interchangeable / 25 跳过须点名 interchangeable。**  
   官方把策略拒绝不是共识非法和已经 144 bundled写成两件。看见策略拒绝不是共识非法，不是已经 144 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把非标准塞进块、怎样 RBF 钉死。

## 官方为什么这样拆

- **策略拒绝不是共识非法 interchangeable：官方写 Policy 是共识之外、对未确认交易进池之前的本地规则。**
- **看见本页不是已经是不变量 44。**
- **看见策略旋钮不是已经 144 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经共识非法 | 不是已经共识非法 | 不是已经入池拒绝≠免费（44） |
| 已经是不变量 44 | 不是已经是不变量 44 | 不是已经跳过须点名（25） |
| 已经 144 bundled | 不是已经 144 bundled | 不是已经1522 polc-notblk |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Policy policy-reject not already consensus-illegal / not already 44 / not already 144-bundled 正式三事（144 余量），必须分开是不是已经共识非法、是不是已经是不变量 44、是不是已经 144 bundled。可以跳过「看见邻居不转发就已经共识非法」。不要另写 怎样把非标准塞进块、怎样 RBF 钉死。144 policy vs consensus bundled unbundling 在本页 item 1 启动；续 [`worked-example-polc-notblk-vs-bundled.md`](worked-example-polc-notblk-vs-bundled.md)（不变量 1522 item 2）。

## 本页不抄

- 默认费率、灰尘、祖先条数、簇上限。
- 怎样把非标准塞进块、怎样 RBF 钉死。
