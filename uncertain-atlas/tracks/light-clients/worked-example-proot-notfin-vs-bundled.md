# 例：看见合约里读到的根不是已经finalized不是已经finalized；看见a root read from the contract is not already finalized不是已经是不变量 149；看见合约里读到的根不是已经finalized不是已经是不变量 154

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-4788](https://eips.ethereum.org/EIPS/eip-4788)（Beacon block root in the EVM）。  
**对应课文**：[L5.2](../../courses/level-05-ethereum/L05-M02-el-cl-finality.md)。  
**不要写进**：`index/03` 共识行、M5.2、L5.2。本页是「EIP-4788 contract-root not already finalized / not already 149 / not already 154 正式三事（156 余量）/ not 1507 proot-notfin interchangeable / not 156 parent-root-vs-head bundled interchangeable」，不是 parent root vs head bundled（156），也不是已经 处理≠改头（149），也不是已经 提款≠交易（154）。不要另写 怎样塞假父根、怎样打环碰撞。

## 官方三件事

1. **看见合约里读到的根不是已经finalized / 看见合约里读到的根不是已经finalized 这份对象 is not already 已经finalized interchangeable，也不是已经 parent root vs head bundled（156） interchangeable / 1507 proot-notfin interchangeable / 1506 proot-nothead interchangeable，也不是已经 EIP-4788 contract-root not already finalized / not already 149 / not already 154 正式三事 bundled（156 item 2 余量） interchangeable / 156 proot item 2 interchangeable。**  
   官方把合约里读到的根不是已经finalized和已经finalized写成两件。看见合约里读到的根不是已经finalized，不是已经finalized。

2. **看见a root read from the contract is not already finalized / 看见合约里读到的根不是已经finalized / 这份对象 is not already 已经是不变量 149 interchangeable，也不是已经 parent root vs head bundled（156） interchangeable / 1507 proot-notfin interchangeable / 1508 proot-notperm interchangeable，也不是已经 处理≠改头 interchangeable / 149 处理≠改头 interchangeable。**  
   官方把a root read from the contract is not already finalized和已经是不变量 149写成两件。看见a root read from the contract is not already finalized，不是已经是不变量 149。

3. **看见合约里读到的根不是已经finalized / 看见a root read from the contract is not already finalized / 这份对象 is not already 已经是不变量 154 interchangeable，也不是已经 parent root vs head bundled（156） interchangeable / 1507 proot-notfin interchangeable / 1506 proot-nothead interchangeable，也不是已经 提款≠交易 interchangeable / 154 提款≠交易 interchangeable。**  
   官方把合约里读到的根不是已经finalized和已经是不变量 154写成两件。看见合约里读到的根不是已经finalized，不是已经是不变量 154。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样塞假父根、怎样打环碰撞。

## 官方为什么这样拆

- **合约里读到的根不是已经finalized interchangeable：官方写合约只存一小段历史，读到根不是已经最终。**
- **看见本页不是已经是不变量 149。**
- **看见本页不是已经是不变量 154。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经finalized | 不是已经finalized | 不是已经处理≠改头（149） |
| 已经是不变量 149 | 不是已经是不变量 149 | 不是已经提款≠交易（154） |
| 已经是不变量 154 | 不是已经是不变量 154 | 不是已经1506 proot-nothead |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-4788 contract-root not already finalized / not already 149 / not already 154 正式三事（156 余量），必须分开是不是已经finalized、是不是已经是不变量 149、是不是已经是不变量 154。可以跳过「看见合约读到就已经最终」。不要另写 怎样塞假父根、怎样打环碰撞。156 parent-root vs head bundled unbundling 在本页 item 2 续；续 [`worked-example-proot-notperm-vs-bundled.md`](worked-example-proot-notperm-vs-bundled.md)（不变量 1508 item 3）。

## 本页不抄

- 分叉时间戳、环长、系统地址、调用气限。
- 怎样塞假父根、怎样打环碰撞。
