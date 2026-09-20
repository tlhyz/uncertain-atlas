# 例：看见出块者开跑已热不是已经访问过不是已经访问过；看见coinbase warm-at-start is not already accessed不是已经是 2929 第一次访问；看见出块者开跑已热不是已经访问过不是已经 187 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-3651](https://eips.ethereum.org/EIPS/eip-3651)（Final, Core, Warm COINBASE）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-3651 coinbase-warm not already accessed / not already 2929-first / not already 187-bundled 正式三事（187 余量）/ not 1446 cbase-notacc interchangeable / not 187 coinbase-vs-prefill bundled interchangeable」，不是 coinbase vs prefill bundled（187），也不是已经 第一次≠已热（169），也不是已经 列入≠已访问（168）。不要另写 怎样把付款指到出块者、怎样预热救人。

## 官方三件事

1. **看见出块者开跑已热不是已经访问过 / 看见出块者开跑已热不是已经访问过 这份对象 is not already 已经访问过 interchangeable，也不是已经 coinbase vs prefill bundled（187） interchangeable / 1446 cbase-notacc interchangeable / 1447 cbase-notpay interchangeable，也不是已经 EIP-3651 coinbase-warm not already accessed / not already 2929-first / not already 187-bundled 正式三事 bundled（187 item 1 余量） interchangeable / 187 cbase item 1 interchangeable。**  
   官方把出块者开跑已热不是已经访问过和已经访问过写成两件。看见出块者开跑已热不是已经访问过，不是已经访问过。

2. **看见coinbase warm-at-start is not already accessed / 看见出块者开跑已热不是已经访问过 / 这份对象 is not already 已经是 2929 第一次访问 interchangeable，也不是已经 coinbase vs prefill bundled（187） interchangeable / 1446 cbase-notacc interchangeable / 1448 cbase-not169 interchangeable，也不是已经 第一次≠已热 interchangeable / 169 第一次≠已热 interchangeable。**  
   官方把coinbase warm-at-start is not already accessed和已经是 2929 第一次访问写成两件。看见coinbase warm-at-start is not already accessed，不是已经是 2929 第一次访问。

3. **看见出块者开跑已热不是已经访问过 / 看见coinbase warm-at-start is not already accessed / 这份对象 is not already 已经 187 bundled interchangeable，也不是已经 coinbase vs prefill bundled（187） interchangeable / 1446 cbase-notacc interchangeable / 1447 cbase-notpay interchangeable，也不是已经 列入≠已访问 interchangeable / 168 列入≠已访问 interchangeable。**  
   官方把出块者开跑已热不是已经访问过和已经 187 bundled写成两件。看见出块者开跑已热不是已经访问过，不是已经 187 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把付款指到出块者、怎样预热救人。

## 官方为什么这样拆

- **出块者开跑已热不是已经访问过 interchangeable：官方写本页只是开跑把出块者放进热集合，不是已经碰过这个地址。**
- **看见本页不是已经是 2929 第一次访问。**
- **看见读数旋钮不是已经 187 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经访问过 | 不是已经访问过 | 不是已经第一次≠已热（169） |
| 已经是 2929 第一次访问 | 不是已经是 2929 第一次访问 | 不是已经列入≠已访问（168） |
| 已经 187 bundled | 不是已经 187 bundled | 不是已经1447 cbase-notpay |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3651 coinbase-warm not already accessed / not already 2929-first / not already 187-bundled 正式三事（187 余量），必须分开是不是已经访问过、是不是已经是 2929 第一次访问、是不是已经 187 bundled。可以跳过「发送者已热所以出块者也热」。不要另写 怎样把付款指到出块者、怎样预热救人。187 coinbase vs prefill bundled unbundling 在本页 item 1 启动；续 [`worked-example-cbase-notpay-vs-bundled.md`](worked-example-cbase-notpay-vs-bundled.md)（不变量 1447 item 2）。

## 本页不抄

- 操作码号、气价、分叉高度。
- 怎样把付款指到出块者、怎样预热救人。
