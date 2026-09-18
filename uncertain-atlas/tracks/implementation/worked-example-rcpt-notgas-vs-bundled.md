# 例：看见还剩气不是已经成功；看见气烧光不是已经失败；看见还剩气不是已经写了带回剩余气的回滚

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-658](https://eips.ethereum.org/EIPS/eip-658)（Final, Core；依赖 EIP-140）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-658 gas not already success / not already failure / not already revert-177 正式三事（236 余量）/ not 1302 rcpt-notgas interchangeable / not 236 receipt-status-vs-gas bundled interchangeable」，不是 receipt status vs gas bundled（236），也不是已经 revert-gas（177），也不是已经 history-window（207）。不要另写 怎样重放交易问 RPC，怎样改收据编码，怎样从枢轴之后补状态。

## 官方三件事

1. **看见还剩气 / 看见还剩气 这份对象 is not already 已经成功 interchangeable，也不是已经 receipt status vs gas bundled（236） interchangeable / 1302 rcpt-notgas interchangeable / 1301 rcpt-notroot interchangeable，也不是已经 EIP-658 gas not already success / not already failure / not already revert-177 正式三事 bundled（236 item 2 余量） interchangeable / 236 rcpt item 2 interchangeable。**  
   官方把还剩气和已经成功写成两件。看见还剩气，不是已经成功。

2. **看见气烧光 / 看见还剩气 / 这份对象 is not already 已经失败 interchangeable，也不是已经 receipt status vs gas bundled（236） interchangeable / 1302 rcpt-notgas interchangeable / 1303 rcpt-notrpc interchangeable，也不是已经 revert-gas interchangeable / 177 revert-gas interchangeable。**  
   官方把气烧光和已经失败写成两件。看见气烧光，不是已经失败。

3. **看见还剩气 / 看见气烧光 / 这份对象 is not already 已经写了带回剩余气的回滚 interchangeable，也不是已经 receipt status vs gas bundled（236） interchangeable / 1302 rcpt-notgas interchangeable / 1301 rcpt-notroot interchangeable，也不是已经 history-window interchangeable / 207 history-window interchangeable。**  
   官方把还剩气和已经写了带回剩余气的回滚写成两件。看见还剩气，不是已经写了带回剩余气的回滚。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样重放交易问 RPC，怎样改收据编码，怎样从枢轴之后补状态。

## 官方为什么这样拆

- **还剩气 不是已经成功：官方写用户不能再靠气是否烧光判断这笔成没成。**
- **气烧光 不是已经失败：故意回滚让气烧光才是失败这条旧假定失效。**
- **本页 不是已经写了带回剩余气的回滚：那是不变量 177。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经成功 | 不是已经成功 | 不是已经revert-gas（177） |
| 已经失败 | 不是已经失败 | 不是已经history-window（207） |
| 已经写了带回剩余气的回滚 | 不是已经写了带回剩余气的回滚 | 不是已经1301 rcpt-notroot |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-658 gas not already success / not already failure / not already revert-177 正式三事（236 余量），必须分开是不是已经成功、是不是已经失败、是不是已经写了带回剩余气的回滚。可以跳过「看见还剩气就已经知道成功」。不要另写 怎样重放交易问 RPC，怎样改收据编码，怎样从枢轴之后补状态。236 receipt status vs gas bundled unbundling 在本页 item 2 续；续 [`worked-example-rcpt-notrpc-vs-bundled.md`](worked-example-rcpt-notrpc-vs-bundled.md)（不变量 1303 item 3）。

## 本页不抄

- 分叉高度、状态码取值。
- 怎样重放交易问 RPC，怎样改收据编码，怎样从枢轴之后补状态。
