# 例：看见头里的父信标根不是当前信标头不是已经是当前信标头；看见the parent beacon root is not already the current head不是已经是不变量 127；看见头里的父信标根不是当前信标头不是已经 156 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-4788](https://eips.ethereum.org/EIPS/eip-4788)（Beacon block root in the EVM）。  
**对应课文**：[L5.2](../../courses/level-05-ethereum/L05-M02-el-cl-finality.md)。  
**不要写进**：`index/03` 共识行、M5.2、L5.2。本页是「EIP-4788 parent-root not already current-head / not already 127 / not already 156-bundled 正式三事（156 余量）/ not 1506 proot-nothead interchangeable / not 156 parent-root-vs-head bundled interchangeable」，不是 parent root vs head bundled（156），也不是已经 head≠justified≠finalized（127），也不是已经 处理≠改头（149）。不要另写 怎样塞假父根、怎样打环碰撞。

## 官方三件事

1. **看见头里的父信标根不是当前信标头 / 看见头里的父信标根不是当前信标头 这份对象 is not already 已经是当前信标头 interchangeable，也不是已经 parent root vs head bundled（156） interchangeable / 1506 proot-nothead interchangeable / 1507 proot-notfin interchangeable，也不是已经 EIP-4788 parent-root not already current-head / not already 127 / not already 156-bundled 正式三事 bundled（156 item 1 余量） interchangeable / 156 proot item 1 interchangeable。**  
   官方把头里的父信标根不是当前信标头和已经是当前信标头写成两件。看见头里的父信标根不是当前信标头，不是已经是当前信标头。

2. **看见the parent beacon root is not already the current head / 看见头里的父信标根不是当前信标头 / 这份对象 is not already 已经是不变量 127 interchangeable，也不是已经 parent root vs head bundled（156） interchangeable / 1506 proot-nothead interchangeable / 1508 proot-notperm interchangeable，也不是已经 head≠justified≠finalized interchangeable / 127 head≠justified≠finalized interchangeable。**  
   官方把the parent beacon root is not already the current head和已经是不变量 127写成两件。看见the parent beacon root is not already the current head，不是已经是不变量 127。

3. **看见头里的父信标根不是当前信标头 / 看见the parent beacon root is not already the current head / 这份对象 is not already 已经 156 bundled interchangeable，也不是已经 parent root vs head bundled（156） interchangeable / 1506 proot-nothead interchangeable / 1507 proot-notfin interchangeable，也不是已经 处理≠改头 interchangeable / 149 处理≠改头 interchangeable。**  
   官方把头里的父信标根不是当前信标头和已经 156 bundled写成两件。看见头里的父信标根不是当前信标头，不是已经 156 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样塞假父根、怎样打环碰撞。

## 官方为什么这样拆

- **头里的父信标根不是当前信标头 interchangeable：官方写每个执行块含父信标块的根，漏槽时父根不变。**
- **看见本页不是已经是不变量 127。**
- **看见父根旋钮不是已经 156 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是当前信标头 | 不是已经是当前信标头 | 不是已经head≠justified≠finalized（127） |
| 已经是不变量 127 | 不是已经是不变量 127 | 不是已经处理≠改头（149） |
| 已经 156 bundled | 不是已经 156 bundled | 不是已经1507 proot-notfin |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-4788 parent-root not already current-head / not already 127 / not already 156-bundled 正式三事（156 余量），必须分开是不是已经是当前信标头、是不是已经是不变量 127、是不是已经 156 bundled。可以跳过「看见合约读到就已经最终」。不要另写 怎样塞假父根、怎样打环碰撞。156 parent-root vs head bundled unbundling 在本页 item 1 启动；续 [`worked-example-proot-notfin-vs-bundled.md`](worked-example-proot-notfin-vs-bundled.md)（不变量 1507 item 2）。

## 本页不抄

- 分叉时间戳、环长、系统地址、调用气限。
- 怎样塞假父根、怎样打环碰撞。
