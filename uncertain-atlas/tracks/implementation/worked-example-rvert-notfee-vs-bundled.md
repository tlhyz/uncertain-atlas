# 例：看见不够付回滚自己的费不是已经留下剩余气不是已经按回滚语义留下剩余气；看见unpaid revert fee is not already leftover不是已经是 103 空户回滚；看见不够付回滚自己的费不是已经留下剩余气不是已经免费

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-140](https://eips.ethereum.org/EIPS/eip-140)（Final, Core, REVERT instruction）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-140 unpaid-self-fee not already leftover-semantics / not already 103 / not already free 正式三事（177 余量）/ not 1381 rvert-notfee interchangeable / not 177 revert-vs-invalid bundled interchangeable」，不是 revert vs invalid bundled（177），也不是已经 空账户 OOG 回滚（103），也不是已经 initcode≠运行时代码（176）。不要另写 怎样挑回滚或非法指令去留气或烧气。

## 官方三件事

1. **看见不够付回滚自己的费不是已经留下剩余气 / 看见不够付回滚自己的费不是已经留下剩余气 这份对象 is not already 已经按回滚语义留下剩余气 interchangeable，也不是已经 revert vs invalid bundled（177） interchangeable / 1381 rvert-notfee interchangeable / 1380 rvert-notburn interchangeable，也不是已经 EIP-140 unpaid-self-fee not already leftover-semantics / not already 103 / not already free 正式三事 bundled（177 item 2 余量） interchangeable / 177 rvert item 2 interchangeable。**  
   官方把不够付回滚自己的费不是已经留下剩余气和已经按回滚语义留下剩余气写成两件。看见不够付回滚自己的费不是已经留下剩余气，不是已经按回滚语义留下剩余气。

2. **看见unpaid revert fee is not already leftover / 看见不够付回滚自己的费不是已经留下剩余气 / 这份对象 is not already 已经是 103 空户回滚 interchangeable，也不是已经 revert vs invalid bundled（177） interchangeable / 1381 rvert-notfee interchangeable / 1382 rvert-notdep interchangeable，也不是已经 空账户 OOG 回滚 interchangeable / 103 空账户 OOG 回滚 interchangeable。**  
   官方把unpaid revert fee is not already leftover和已经是 103 空户回滚写成两件。看见unpaid revert fee is not already leftover，不是已经是 103 空户回滚。

3. **看见不够付回滚自己的费不是已经留下剩余气 / 看见unpaid revert fee is not already leftover / 这份对象 is not already 已经免费 interchangeable，也不是已经 revert vs invalid bundled（177） interchangeable / 1381 rvert-notfee interchangeable / 1380 rvert-notburn interchangeable，也不是已经 initcode≠运行时代码 interchangeable / 176 initcode≠运行时代码 interchangeable。**  
   官方把不够付回滚自己的费不是已经留下剩余气和已经免费写成两件。看见不够付回滚自己的费不是已经留下剩余气，不是已经免费。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样挑回滚或非法指令去留气或烧气。

## 官方为什么这样拆

- **不够付回滚自己的费不是已经留下剩余气 interchangeable：官方把付不起自己的费写成普通气耗尽。**
- **看见付不起不是已经是 103 空户回滚。**
- **看见留下剩余气不是已经免费。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经按回滚语义留下剩余气 | 不是已经按回滚语义留下剩余气 | 不是已经空账户 OOG 回滚（103） |
| 已经是 103 空户回滚 | 不是已经是 103 空户回滚 | 不是已经initcode≠运行时代码（176） |
| 已经免费 | 不是已经免费 | 不是已经1380 rvert-notburn |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-140 unpaid-self-fee not already leftover-semantics / not already 103 / not already free 正式三事（177 余量），必须分开是不是已经按回滚语义留下剩余气、是不是已经是 103 空户回滚、是不是已经免费。可以跳过「看见失败就已经烧光剩余气」。不要另写 怎样挑回滚或非法指令去留气或烧气。177 REVERT leftover-gas vs burn bundled unbundling 在本页 item 2 续；续 [`worked-example-rvert-notdep-vs-bundled.md`](worked-example-rvert-notdep-vs-bundled.md)（不变量 1382 item 3）。

## 本页不抄

- 操作码号、分叉高度、例气数、例返回字节。
- 怎样挑回滚或非法指令去留气或烧气。
