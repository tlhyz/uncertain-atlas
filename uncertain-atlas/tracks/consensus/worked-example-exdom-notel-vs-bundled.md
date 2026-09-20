# 例：看见域锁在某次分叉不是已经改了执行层不是已经改了执行层；看见domain lock is not already an EL change不是已经是不变量 154；看见域锁在某次分叉不是已经改了执行层不是已经是不变量 192

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7044](https://eips.ethereum.org/EIPS/eip-7044)（Perpetually Valid Signed Voluntary Exits）。  
**对应课文**：[L5.2](../../courses/level-05-ethereum/L05-M02-el-cl-finality.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7044 domain-lock not already el-changed / not already 154 / not already 192 正式三事（213 余量）/ not 1480 exdom-notel interchangeable / not 213 exit-domain-vs-fork bundled interchangeable」，不是 exit domain vs fork bundled（213），也不是已经 提款≠用户交易（154），也不是已经 请求承诺≠已处理（192）。不要另写 怎样造锁死域的签、怎样在分叉两边重放。

## 官方三件事

1. **看见域锁在某次分叉不是已经改了执行层 / 看见域锁在某次分叉不是已经改了执行层 这份对象 is not already 已经改了执行层 interchangeable，也不是已经 exit domain vs fork bundled（213） interchangeable / 1480 exdom-notel interchangeable / 1479 exdom-notperm interchangeable，也不是已经 EIP-7044 domain-lock not already el-changed / not already 154 / not already 192 正式三事 bundled（213 item 2 余量） interchangeable / 213 exdom item 2 interchangeable。**  
   官方把域锁在某次分叉不是已经改了执行层和已经改了执行层写成两件。看见域锁在某次分叉不是已经改了执行层，不是已经改了执行层。

2. **看见domain lock is not already an EL change / 看见域锁在某次分叉不是已经改了执行层 / 这份对象 is not already 已经是不变量 154 interchangeable，也不是已经 exit domain vs fork bundled（213） interchangeable / 1480 exdom-notel interchangeable / 1481 exdom-notloss interchangeable，也不是已经 提款≠用户交易 interchangeable / 154 提款≠用户交易 interchangeable。**  
   官方把domain lock is not already an EL change和已经是不变量 154写成两件。看见domain lock is not already an EL change，不是已经是不变量 154。

3. **看见域锁在某次分叉不是已经改了执行层 / 看见domain lock is not already an EL change / 这份对象 is not already 已经是不变量 192 interchangeable，也不是已经 exit domain vs fork bundled（213） interchangeable / 1480 exdom-notel interchangeable / 1479 exdom-notperm interchangeable，也不是已经 请求承诺≠已处理 interchangeable / 192 请求承诺≠已处理 interchangeable。**  
   官方把域锁在某次分叉不是已经改了执行层和已经是不变量 192写成两件。看见域锁在某次分叉不是已经改了执行层，不是已经是不变量 192。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造锁死域的签、怎样在分叉两边重放。

## 官方为什么这样拆

- **域锁在某次分叉不是已经改了执行层 interchangeable：官方写只改共识层处理自愿退出时怎么算域，不要求改执行层。**
- **看见本页不是已经是不变量 154。**
- **看见本页不是已经是不变量 192。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了执行层 | 不是已经改了执行层 | 不是已经提款≠用户交易（154） |
| 已经是不变量 154 | 不是已经是不变量 154 | 不是已经请求承诺≠已处理（192） |
| 已经是不变量 192 | 不是已经是不变量 192 | 不是已经1479 exdom-notperm |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7044 domain-lock not already el-changed / not already 154 / not already 192 正式三事（213 余量），必须分开是不是已经改了执行层、是不是已经是不变量 154、是不是已经是不变量 192。可以跳过「看见 7044 就已经永远退出」。不要另写 怎样造锁死域的签、怎样在分叉两边重放。213 exit-domain vs fork bundled unbundling 在本页 item 2 续；续 [`worked-example-exdom-notloss-vs-bundled.md`](worked-example-exdom-notloss-vs-bundled.md)（不变量 1481 item 3）。

## 本页不抄

- 分叉版本字节、规范提交哈希、预签流程。
- 怎样造锁死域的签、怎样在分叉两边重放。
