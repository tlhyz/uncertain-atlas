# 例：看见带回剩余气的回滚不是已经烧光不是已经像非法指令那样烧光剩余气；看见leftover-gas revert is not already burn不是已经是气耗尽烧光；看见带回剩余气的回滚不是已经烧光不是已经 177 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-140](https://eips.ethereum.org/EIPS/eip-140)（Final, Core, REVERT instruction）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-140 leftover-gas revert not already INVALID-burn / not already OOG-burn / not already 177-bundled 正式三事（177 余量）/ not 1380 rvert-notburn interchangeable / not 177 revert-vs-invalid bundled interchangeable」，不是 revert vs invalid bundled（177），也不是已经 OOG≠空户已回滚（103），也不是已经 返回缓冲≠已是内存（232）。不要另写 怎样挑回滚或非法指令去留气或烧气。

## 官方三件事

1. **看见带回剩余气的回滚不是已经烧光 / 看见带回剩余气的回滚不是已经烧光 这份对象 is not already 已经像非法指令那样烧光剩余气 interchangeable，也不是已经 revert vs invalid bundled（177） interchangeable / 1380 rvert-notburn interchangeable / 1381 rvert-notfee interchangeable，也不是已经 EIP-140 leftover-gas revert not already INVALID-burn / not already OOG-burn / not already 177-bundled 正式三事 bundled（177 item 1 余量） interchangeable / 177 rvert item 1 interchangeable。**  
   官方把带回剩余气的回滚不是已经烧光和已经像非法指令那样烧光剩余气写成两件。看见带回剩余气的回滚不是已经烧光，不是已经像非法指令那样烧光剩余气。

2. **看见leftover-gas revert is not already burn / 看见带回剩余气的回滚不是已经烧光 / 这份对象 is not already 已经是气耗尽烧光 interchangeable，也不是已经 revert vs invalid bundled（177） interchangeable / 1380 rvert-notburn interchangeable / 1382 rvert-notdep interchangeable，也不是已经 OOG≠空户已回滚 interchangeable / 103 OOG≠空户已回滚 interchangeable。**  
   官方把leftover-gas revert is not already burn和已经是气耗尽烧光写成两件。看见leftover-gas revert is not already burn，不是已经是气耗尽烧光。

3. **看见带回剩余气的回滚不是已经烧光 / 看见leftover-gas revert is not already burn / 这份对象 is not already 已经 177 bundled interchangeable，也不是已经 revert vs invalid bundled（177） interchangeable / 1380 rvert-notburn interchangeable / 1381 rvert-notfee interchangeable，也不是已经 返回缓冲≠已是内存 interchangeable / 232 返回缓冲≠已是内存 interchangeable。**  
   官方把带回剩余气的回滚不是已经烧光和已经 177 bundled写成两件。看见带回剩余气的回滚不是已经烧光，不是已经 177 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样挑回滚或非法指令去留气或烧气。

## 官方为什么这样拆

- **带回剩余气的回滚不是已经烧光 interchangeable：官方把留下剩余气和非法指令烧光写成两件。**
- **看见回滚不是已经是气耗尽烧光。**
- **看见回滚旋钮不是已经 177 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经像非法指令那样烧光剩余气 | 不是已经像非法指令那样烧光剩余气 | 不是已经OOG≠空户已回滚（103） |
| 已经是气耗尽烧光 | 不是已经是气耗尽烧光 | 不是已经返回缓冲≠已是内存（232） |
| 已经 177 bundled | 不是已经 177 bundled | 不是已经1381 rvert-notfee |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-140 leftover-gas revert not already INVALID-burn / not already OOG-burn / not already 177-bundled 正式三事（177 余量），必须分开是不是已经像非法指令那样烧光剩余气、是不是已经是气耗尽烧光、是不是已经 177 bundled。可以跳过「看见失败就已经烧光剩余气」。不要另写 怎样挑回滚或非法指令去留气或烧气。177 REVERT leftover-gas vs burn bundled unbundling 在本页 item 1 启动；续 [`worked-example-rvert-notfee-vs-bundled.md`](worked-example-rvert-notfee-vs-bundled.md)（不变量 1381 item 2）。

## 本页不抄

- 操作码号、分叉高度、例气数、例返回字节。
- 怎样挑回滚或非法指令去留气或烧气。
