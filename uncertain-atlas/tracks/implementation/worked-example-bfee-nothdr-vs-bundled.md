# 例：看见跑 EVM 前就已经有这个数不是已经改了头怎么算不是已经改了头怎么算；看见pre-EVM value is not already header-changed不是已经有气期货；看见跑 EVM 前就已经有这个数不是已经改了头怎么算不是已经自动加长挑战期

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-3198](https://eips.ethereum.org/EIPS/eip-3198)（Final, Core, BASEFEE opcode）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-3198 pre-evm-value not already header-changed / not already futures / not already challenge-extended 正式三事（218 余量）/ not 1400 bfee-nothdr interchangeable / not 218 basefee-opcode-vs-market bundled interchangeable」，不是 basefee opcode vs market bundled（218），也不是已经 压零≠带立即数的压 0（217），也不是已经 blob gas≠普通执行 gas（145）。不要另写 怎样用基础费设悬赏、怎样做气期货、怎样按基础费加长挑战期。

## 官方三件事

1. **看见跑 EVM 前就已经有这个数不是已经改了头怎么算 / 看见跑 EVM 前就已经有这个数不是已经改了头怎么算 这份对象 is not already 已经改了头怎么算 interchangeable，也不是已经 basefee opcode vs market bundled（218） interchangeable / 1400 bfee-nothdr interchangeable / 1398 bfee-notmkt interchangeable，也不是已经 EIP-3198 pre-evm-value not already header-changed / not already futures / not already challenge-extended 正式三事 bundled（218 item 3 余量） interchangeable / 218 bfee item 3 interchangeable。**  
   官方把跑 EVM 前就已经有这个数不是已经改了头怎么算和已经改了头怎么算写成两件。看见跑 EVM 前就已经有这个数不是已经改了头怎么算，不是已经改了头怎么算。

2. **看见pre-EVM value is not already header-changed / 看见跑 EVM 前就已经有这个数不是已经改了头怎么算 / 这份对象 is not already 已经有气期货 interchangeable，也不是已经 basefee opcode vs market bundled（218） interchangeable / 1400 bfee-nothdr interchangeable / 1399 bfee-notprop interchangeable，也不是已经 压零≠带立即数的压 0 interchangeable / 217 压零≠带立即数的压 0 interchangeable。**  
   官方把pre-EVM value is not already header-changed和已经有气期货写成两件。看见pre-EVM value is not already header-changed，不是已经有气期货。

3. **看见跑 EVM 前就已经有这个数不是已经改了头怎么算 / 看见pre-EVM value is not already header-changed / 这份对象 is not already 已经自动加长挑战期 interchangeable，也不是已经 basefee opcode vs market bundled（218） interchangeable / 1400 bfee-nothdr interchangeable / 1398 bfee-notmkt interchangeable，也不是已经 blob gas≠普通执行 gas interchangeable / 145 blob gas≠普通执行 gas interchangeable。**  
   官方把跑 EVM 前就已经有这个数不是已经改了头怎么算和已经自动加长挑战期写成两件。看见跑 EVM 前就已经有这个数不是已经改了头怎么算，不是已经自动加长挑战期。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样用基础费设悬赏、怎样做气期货、怎样按基础费加长挑战期。

## 官方为什么这样拆

- **跑 EVM 前就已经有这个数不是已经改了头怎么算 interchangeable：官方写处理交易本来就要用，不额外改头。**
- **看见动机写气期货不是已经有气期货。**
- **看见动机写挑战期不是已经自动加长挑战期。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了头怎么算 | 不是已经改了头怎么算 | 不是已经压零≠带立即数的压 0（217） |
| 已经有气期货 | 不是已经有气期货 | 不是已经blob gas≠普通执行 gas（145） |
| 已经自动加长挑战期 | 不是已经自动加长挑战期 | 不是已经1398 bfee-notmkt |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3198 pre-evm-value not already header-changed / not already futures / not already challenge-extended 正式三事（218 余量），必须分开是不是已经改了头怎么算、是不是已经有气期货、是不是已经自动加长挑战期。可以跳过「看见 3198 就已经改了费用市场」。不要另写 怎样用基础费设悬赏、怎样做气期货、怎样按基础费加长挑战期。218 BASEFEE opcode vs market bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：EIP-7516 BLOBBASEFEE（219）。

## 本页不抄

- 操作码号、气价档、测试向量、悬赏公式、规范提交哈希。
- 怎样用基础费设悬赏、怎样做气期货、怎样按基础费加长挑战期。
