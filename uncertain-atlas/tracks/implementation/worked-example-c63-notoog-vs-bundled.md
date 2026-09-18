# 例：看见问超了不是已经耗尽气；看见去掉六十四分之一不是已经没有调用深度上限；看见问超了不是已经把父帧气全给了子执行

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-150](https://eips.ethereum.org/EIPS/eip-150)（Final, Core；Tangerine Whistle）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-150 63rds not already oog / not already no-depth / not already all-parent 正式三事（237 余量）/ not 1299 c63-notoog interchangeable / not 237 call-63rds-vs-oog bundled interchangeable」，不是 call 63rds vs oog bundled（237），也不是已经 gas-wallclock（101），也不是已经 default-gas（211）。不要另写 怎样造读树垃圾交易，怎样按「剩下的再减一截」复刻旧合约，怎样打满一块。

## 官方三件事

1. **看见问超了 / 看见问超了 这份对象 is not already 已经耗尽气 interchangeable，也不是已经 call 63rds vs oog bundled（237） interchangeable / 1299 c63-notoog interchangeable / 1298 c63-notprice interchangeable，也不是已经 EIP-150 63rds not already oog / not already no-depth / not already all-parent 正式三事 bundled（237 item 2 余量） interchangeable / 237 c63 item 2 interchangeable。**  
   官方把问超了和已经耗尽气写成两件。看见问超了，不是已经耗尽气。

2. **看见去掉六十四分之一 / 看见问超了 / 这份对象 is not already 已经没有调用深度上限 interchangeable，也不是已经 call 63rds vs oog bundled（237） interchangeable / 1299 c63-notoog interchangeable / 1300 c63-notcap interchangeable，也不是已经 gas-wallclock interchangeable / 101 gas-wallclock interchangeable。**  
   官方把去掉六十四分之一和已经没有调用深度上限写成两件。看见去掉六十四分之一，不是已经没有调用深度上限。

3. **看见问超了 / 看见去掉六十四分之一 / 这份对象 is not already 已经把父帧气全给了子执行 interchangeable，也不是已经 call 63rds vs oog bundled（237） interchangeable / 1299 c63-notoog interchangeable / 1298 c63-notprice interchangeable，也不是已经 default-gas interchangeable / 211 default-gas interchangeable。**  
   官方把问超了和已经把父帧气全给了子执行写成两件。看见问超了，不是已经把父帧气全给了子执行。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造读树垃圾交易，怎样按「剩下的再减一截」复刻旧合约，怎样打满一块。

## 官方为什么这样拆

- **问超了 不是已经耗尽气：官方写不要报耗尽气，改成只给去掉六十四分之一那一截。**
- **去掉六十四分之一 不是已经没有调用深度上限：官方把硬调用栈深度上限换成按气收紧的软限制。**
- **还能开子调用 不是已经把父帧气全给了子执行：官方写 CREATE 也只把父帧去掉六十四分之一之后的气给子执行。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经耗尽气 | 不是已经耗尽气 | 不是已经gas-wallclock（101） |
| 已经没有调用深度上限 | 不是已经没有调用深度上限 | 不是已经default-gas（211） |
| 已经把父帧气全给了子执行 | 不是已经把父帧气全给了子执行 | 不是已经1298 c63-notprice |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-150 63rds not already oog / not already no-depth / not already all-parent 正式三事（237 余量），必须分开是不是已经耗尽气、是不是已经没有调用深度上限、是不是已经把父帧气全给了子执行。可以跳过「看见读树涨价就已经齐了」。不要另写 怎样造读树垃圾交易，怎样按「剩下的再减一截」复刻旧合约，怎样打满一块。237 call 63rds vs oog bundled unbundling 在本页 item 2 续；续 [`worked-example-c63-notcap-vs-bundled.md`](worked-example-c63-notcap-vs-bundled.md)（不变量 1300 item 3）。

## 本页不抄

- 分叉高度、操作码新旧气价、建议气限取值、读盘字节估计、软深度大约能到几层。
- 怎样造读树垃圾交易，怎样按「剩下的再减一截」复刻旧合约，怎样打满一块。
