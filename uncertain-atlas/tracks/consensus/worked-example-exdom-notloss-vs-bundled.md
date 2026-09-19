# 例：看见分叉两边都能重放不是已经丢资金不是已经丢资金；看见replay on both forks is not already lost funds不是已经更安全；看见分叉两边都能重放不是已经丢资金不是已经是不变量 6

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7044](https://eips.ethereum.org/EIPS/eip-7044)（Perpetually Valid Signed Voluntary Exits）。  
**对应课文**：[L5.2](../../courses/level-05-ethereum/L05-M02-el-cl-finality.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7044 replay-both not already lost-funds / not already safer / not already 6 正式三事（213 余量）/ not 1481 exdom-notloss interchangeable / not 213 exit-domain-vs-fork bundled interchangeable」，不是 exit domain vs fork bundled（213），也不是已经 请求承诺≠已处理（192），也不是已经 域分离（6）。不要另写 怎样造锁死域的签、怎样在分叉两边重放。

## 官方三件事

1. **看见分叉两边都能重放不是已经丢资金 / 看见分叉两边都能重放不是已经丢资金 这份对象 is not already 已经丢资金 interchangeable，也不是已经 exit domain vs fork bundled（213） interchangeable / 1481 exdom-notloss interchangeable / 1479 exdom-notperm interchangeable，也不是已经 EIP-7044 replay-both not already lost-funds / not already safer / not already 6 正式三事 bundled（213 item 3 余量） interchangeable / 213 exdom item 3 interchangeable。**  
   官方把分叉两边都能重放不是已经丢资金和已经丢资金写成两件。看见分叉两边都能重放不是已经丢资金，不是已经丢资金。

2. **看见replay on both forks is not already lost funds / 看见分叉两边都能重放不是已经丢资金 / 这份对象 is not already 已经更安全 interchangeable，也不是已经 exit domain vs fork bundled（213） interchangeable / 1481 exdom-notloss interchangeable / 1480 exdom-notel interchangeable，也不是已经 请求承诺≠已处理 interchangeable / 192 请求承诺≠已处理 interchangeable。**  
   官方把replay on both forks is not already lost funds和已经更安全写成两件。看见replay on both forks is not already lost funds，不是已经更安全。

3. **看见分叉两边都能重放不是已经丢资金 / 看见replay on both forks is not already lost funds / 这份对象 is not already 已经是不变量 6 interchangeable，也不是已经 exit domain vs fork bundled（213） interchangeable / 1481 exdom-notloss interchangeable / 1479 exdom-notperm interchangeable，也不是已经 域分离 interchangeable / 6 域分离 interchangeable。**  
   官方把分叉两边都能重放不是已经丢资金和已经是不变量 6写成两件。看见分叉两边都能重放不是已经丢资金，不是已经是不变量 6。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造锁死域的签、怎样在分叉两边重放。

## 官方为什么这样拆

- **分叉两边都能重放不是已经丢资金 interchangeable：官方写没有资金风险，也不影响链的安全。**
- **看见两边能重放不是已经更安全。**
- **看见本页不是已经是不变量 6。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经丢资金 | 不是已经丢资金 | 不是已经请求承诺≠已处理（192） |
| 已经更安全 | 不是已经更安全 | 不是已经域分离（6） |
| 已经是不变量 6 | 不是已经是不变量 6 | 不是已经1479 exdom-notperm |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7044 replay-both not already lost-funds / not already safer / not already 6 正式三事（213 余量），必须分开是不是已经丢资金、是不是已经更安全、是不是已经是不变量 6。可以跳过「看见 7044 就已经永远退出」。不要另写 怎样造锁死域的签、怎样在分叉两边重放。213 exit-domain vs fork bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：lookahead（205）。

## 本页不抄

- 分叉版本字节、规范提交哈希、预签流程。
- 怎样造锁死域的签、怎样在分叉两边重放。
