# 例：看见开跑已热不是已经付给出块者不是已经付给出块者；看见warm-at-start is not already paid to coinbase不是已经是 1559 小费；看见开跑已热不是已经付给出块者不是已经是不变量 158

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-3651](https://eips.ethereum.org/EIPS/eip-3651)（Final, Core, Warm COINBASE）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-3651 warm-start not already paid / not already 1559 / not already 158 正式三事（187 余量）/ not 1447 cbase-notpay interchangeable / not 187 coinbase-vs-prefill bundled interchangeable」，不是 coinbase vs prefill bundled（187），也不是已经 基础费≠小费（158），也不是已经 第一次≠已热（169）。不要另写 怎样把付款指到出块者、怎样预热救人。

## 官方三件事

1. **看见开跑已热不是已经付给出块者 / 看见开跑已热不是已经付给出块者 这份对象 is not already 已经付给出块者 interchangeable，也不是已经 coinbase vs prefill bundled（187） interchangeable / 1447 cbase-notpay interchangeable / 1446 cbase-notacc interchangeable，也不是已经 EIP-3651 warm-start not already paid / not already 1559 / not already 158 正式三事 bundled（187 item 2 余量） interchangeable / 187 cbase item 2 interchangeable。**  
   官方把开跑已热不是已经付给出块者和已经付给出块者写成两件。看见开跑已热不是已经付给出块者，不是已经付给出块者。

2. **看见warm-at-start is not already paid to coinbase / 看见开跑已热不是已经付给出块者 / 这份对象 is not already 已经是 1559 小费 interchangeable，也不是已经 coinbase vs prefill bundled（187） interchangeable / 1447 cbase-notpay interchangeable / 1448 cbase-not169 interchangeable，也不是已经 基础费≠小费 interchangeable / 158 基础费≠小费 interchangeable。**  
   官方把warm-at-start is not already paid to coinbase和已经是 1559 小费写成两件。看见warm-at-start is not already paid to coinbase，不是已经是 1559 小费。

3. **看见开跑已热不是已经付给出块者 / 看见warm-at-start is not already paid to coinbase / 这份对象 is not already 已经是不变量 158 interchangeable，也不是已经 coinbase vs prefill bundled（187） interchangeable / 1447 cbase-notpay interchangeable / 1446 cbase-notacc interchangeable，也不是已经 第一次≠已热 interchangeable / 169 第一次≠已热 interchangeable。**  
   官方把开跑已热不是已经付给出块者和已经是不变量 158写成两件。看见开跑已热不是已经付给出块者，不是已经是不变量 158。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把付款指到出块者、怎样预热救人。

## 官方为什么这样拆

- **开跑已热不是已经付给出块者 interchangeable：官方写补上这一盏灯是为了对齐读账户的代价，不是已经付过奖励或小费。**
- **看见本页不是已经是 1559 小费。**
- **看见本页不是已经是不变量 158。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经付给出块者 | 不是已经付给出块者 | 不是已经基础费≠小费（158） |
| 已经是 1559 小费 | 不是已经是 1559 小费 | 不是已经第一次≠已热（169） |
| 已经是不变量 158 | 不是已经是不变量 158 | 不是已经1446 cbase-notacc |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3651 warm-start not already paid / not already 1559 / not already 158 正式三事（187 余量），必须分开是不是已经付给出块者、是不是已经是 1559 小费、是不是已经是不变量 158。可以跳过「发送者已热所以出块者也热」。不要另写 怎样把付款指到出块者、怎样预热救人。187 coinbase vs prefill bundled unbundling 在本页 item 2 续；续 [`worked-example-cbase-not169-vs-bundled.md`](worked-example-cbase-not169-vs-bundled.md)（不变量 1448 item 3）。

## 本页不抄

- 操作码号、气价、分叉高度。
- 怎样把付款指到出块者、怎样预热救人。
