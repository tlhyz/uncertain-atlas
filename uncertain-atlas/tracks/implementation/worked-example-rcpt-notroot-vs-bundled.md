# 例：看见状态码不是收据里还印着中间状态根；看见本页不是已经写了那份废掉中间根的规范；看见状态码不是已经另开一栏

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-658](https://eips.ethereum.org/EIPS/eip-658)（Final, Core；依赖 EIP-140）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-658 status not already mid-root / not already deprecated-spec / not already extra-column 正式三事（236 余量）/ not 1301 rcpt-notroot interchangeable / not 236 receipt-status-vs-gas bundled interchangeable」，不是 receipt status vs gas bundled（236），也不是已经 revert-gas（177），也不是已经 returndata（232）。不要另写 怎样重放交易问 RPC，怎样改收据编码，怎样从枢轴之后补状态。

## 官方三件事

1. **看见状态码 / 看见状态码 这份对象 is not already 收据里还印着中间状态根 interchangeable，也不是已经 receipt status vs gas bundled（236） interchangeable / 1301 rcpt-notroot interchangeable / 1302 rcpt-notgas interchangeable，也不是已经 EIP-658 status not already mid-root / not already deprecated-spec / not already extra-column 正式三事 bundled（236 item 1 余量） interchangeable / 236 rcpt item 1 interchangeable。**  
   官方把状态码和收据里还印着中间状态根写成两件。看见状态码，不是收据里还印着中间状态根。

2. **看见本页 / 看见状态码 / 这份对象 is not already 已经写了那份废掉中间根的规范 interchangeable，也不是已经 receipt status vs gas bundled（236） interchangeable / 1301 rcpt-notroot interchangeable / 1303 rcpt-notrpc interchangeable，也不是已经 revert-gas interchangeable / 177 revert-gas interchangeable。**  
   官方把本页和已经写了那份废掉中间根的规范写成两件。看见本页，不是已经写了那份废掉中间根的规范。

3. **看见状态码 / 看见本页 / 这份对象 is not already 已经另开一栏 interchangeable，也不是已经 receipt status vs gas bundled（236） interchangeable / 1301 rcpt-notroot interchangeable / 1302 rcpt-notgas interchangeable，也不是已经 returndata interchangeable / 232 returndata interchangeable。**  
   官方把状态码和已经另开一栏写成两件。看见状态码，不是已经另开一栏。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样重放交易问 RPC，怎样改收据编码，怎样从枢轴之后补状态。

## 官方为什么这样拆

- **状态码 不是中间状态根：官方说本页替换的是收据里已经过时的中间根字段，不是另开一栏。**
- **本页 不是已经写了那份废掉中间根的规范：官方写中间状态根已经被另一份规范废掉。**
- **看见状态码 不是已经另开一栏：官方写本页是最小改动，用来取出成功或失败。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 收据里还印着中间状态根 | 不是收据里还印着中间状态根 | 不是已经revert-gas（177） |
| 已经写了那份废掉中间根的规范 | 不是已经写了那份废掉中间根的规范 | 不是已经returndata（232） |
| 已经另开一栏 | 不是已经另开一栏 | 不是已经1302 rcpt-notgas |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-658 status not already mid-root / not already deprecated-spec / not already extra-column 正式三事（236 余量），必须分开是不是收据里还印着中间状态根、是不是已经写了那份废掉中间根的规范、是不是已经另开一栏。可以跳过「看见还剩气就已经知道成功」。不要另写 怎样重放交易问 RPC，怎样改收据编码，怎样从枢轴之后补状态。236 receipt status vs gas bundled unbundling 在本页 item 1 启动；续 [`worked-example-rcpt-notgas-vs-bundled.md`](worked-example-rcpt-notgas-vs-bundled.md)（不变量 1302 item 2）。

## 本页不抄

- 分叉高度、状态码取值。
- 怎样重放交易问 RPC，怎样改收据编码，怎样从枢轴之后补状态。
