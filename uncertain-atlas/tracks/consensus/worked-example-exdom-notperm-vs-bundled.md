# 例：看见签过的自愿退出不是已经永远有效不是已经永远有效；看见signed voluntary exit is not already perpetually valid不是已经是不变量 193；看见签过的自愿退出不是已经永远有效不是已经 213 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7044](https://eips.ethereum.org/EIPS/eip-7044)（Perpetually Valid Signed Voluntary Exits）。  
**对应课文**：[L5.2](../../courses/level-05-ethereum/L05-M02-el-cl-finality.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7044 signed-exit not already perpetual / not already 193 / not already 213-bundled 正式三事（213 余量）/ not 1479 exdom-notperm interchangeable / not 213 exit-domain-vs-fork bundled interchangeable」，不是 exit domain vs fork bundled（213），也不是已经 EL退出请求≠已退出（193），也不是已经 提款≠用户交易（154）。不要另写 怎样造锁死域的签、怎样在分叉两边重放。

## 官方三件事

1. **看见签过的自愿退出不是已经永远有效 / 看见签过的自愿退出不是已经永远有效 这份对象 is not already 已经永远有效 interchangeable，也不是已经 exit domain vs fork bundled（213） interchangeable / 1479 exdom-notperm interchangeable / 1480 exdom-notel interchangeable，也不是已经 EIP-7044 signed-exit not already perpetual / not already 193 / not already 213-bundled 正式三事 bundled（213 item 1 余量） interchangeable / 213 exdom item 1 interchangeable。**  
   官方把签过的自愿退出不是已经永远有效和已经永远有效写成两件。看见签过的自愿退出不是已经永远有效，不是已经永远有效。

2. **看见signed voluntary exit is not already perpetually valid / 看见签过的自愿退出不是已经永远有效 / 这份对象 is not already 已经是不变量 193 interchangeable，也不是已经 exit domain vs fork bundled（213） interchangeable / 1479 exdom-notperm interchangeable / 1481 exdom-notloss interchangeable，也不是已经 EL退出请求≠已退出 interchangeable / 193 EL退出请求≠已退出 interchangeable。**  
   官方把signed voluntary exit is not already perpetually valid和已经是不变量 193写成两件。看见signed voluntary exit is not already perpetually valid，不是已经是不变量 193。

3. **看见签过的自愿退出不是已经永远有效 / 看见signed voluntary exit is not already perpetually valid / 这份对象 is not already 已经 213 bundled interchangeable，也不是已经 exit domain vs fork bundled（213） interchangeable / 1479 exdom-notperm interchangeable / 1480 exdom-notel interchangeable，也不是已经 提款≠用户交易 interchangeable / 154 提款≠用户交易 interchangeable。**  
   官方把签过的自愿退出不是已经永远有效和已经 213 bundled写成两件。看见签过的自愿退出不是已经永远有效，不是已经 213 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造锁死域的签、怎样在分叉两边重放。

## 官方为什么这样拆

- **签过的自愿退出不是已经永远有效 interchangeable：官方写以前只在两代升级里有效，看见本页不是纸条已经永远有效。**
- **看见本页不是已经是不变量 193。**
- **看见读数旋钮不是已经 213 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经永远有效 | 不是已经永远有效 | 不是已经EL退出请求≠已退出（193） |
| 已经是不变量 193 | 不是已经是不变量 193 | 不是已经提款≠用户交易（154） |
| 已经 213 bundled | 不是已经 213 bundled | 不是已经1480 exdom-notel |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7044 signed-exit not already perpetual / not already 193 / not already 213-bundled 正式三事（213 余量），必须分开是不是已经永远有效、是不是已经是不变量 193、是不是已经 213 bundled。可以跳过「看见 7044 就已经永远退出」。不要另写 怎样造锁死域的签、怎样在分叉两边重放。213 exit-domain vs fork bundled unbundling 在本页 item 1 启动；续 [`worked-example-exdom-notel-vs-bundled.md`](worked-example-exdom-notel-vs-bundled.md)（不变量 1480 item 2）。

## 本页不抄

- 分叉版本字节、规范提交哈希、预签流程。
- 怎样造锁死域的签、怎样在分叉两边重放。
