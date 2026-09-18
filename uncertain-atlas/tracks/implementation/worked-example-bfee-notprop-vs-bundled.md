# 例：看见能读本块基础费不是已经给了出块者不是已经给了出块者；看见readable basefee is not already paid to proposer不是已经是 blob 基础费指令；看见能读本块基础费不是已经给了出块者不是已经是不变量 219

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-3198](https://eips.ethereum.org/EIPS/eip-3198)（Final, Core, BASEFEE opcode）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-3198 read-basefee not already paid-to-proposer / not already blob-basefee / not already 219 正式三事（218 余量）/ not 1399 bfee-notprop interchangeable / not 218 basefee-opcode-vs-market bundled interchangeable」，不是 basefee opcode vs market bundled（218），也不是已经 基础费烧掉/小费（158），也不是已经 blob 底价指令（219）。不要另写 怎样用基础费设悬赏、怎样做气期货、怎样按基础费加长挑战期。

## 官方三件事

1. **看见能读本块基础费不是已经给了出块者 / 看见能读本块基础费不是已经给了出块者 这份对象 is not already 已经给了出块者 interchangeable，也不是已经 basefee opcode vs market bundled（218） interchangeable / 1399 bfee-notprop interchangeable / 1398 bfee-notmkt interchangeable，也不是已经 EIP-3198 read-basefee not already paid-to-proposer / not already blob-basefee / not already 219 正式三事 bundled（218 item 2 余量） interchangeable / 218 bfee item 2 interchangeable。**  
   官方把能读本块基础费不是已经给了出块者和已经给了出块者写成两件。看见能读本块基础费不是已经给了出块者，不是已经给了出块者。

2. **看见readable basefee is not already paid to proposer / 看见能读本块基础费不是已经给了出块者 / 这份对象 is not already 已经是 blob 基础费指令 interchangeable，也不是已经 basefee opcode vs market bundled（218） interchangeable / 1399 bfee-notprop interchangeable / 1400 bfee-nothdr interchangeable，也不是已经 基础费烧掉/小费 interchangeable / 158 基础费烧掉/小费 interchangeable。**  
   官方把readable basefee is not already paid to proposer和已经是 blob 基础费指令写成两件。看见readable basefee is not already paid to proposer，不是已经是 blob 基础费指令。

3. **看见能读本块基础费不是已经给了出块者 / 看见readable basefee is not already paid to proposer / 这份对象 is not already 已经是不变量 219 interchangeable，也不是已经 basefee opcode vs market bundled（218） interchangeable / 1399 bfee-notprop interchangeable / 1398 bfee-notmkt interchangeable，也不是已经 blob 底价指令 interchangeable / 219 blob 底价指令 interchangeable。**  
   官方把能读本块基础费不是已经给了出块者和已经是不变量 219写成两件。看见能读本块基础费不是已经给了出块者，不是已经是不变量 219。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样用基础费设悬赏、怎样做气期货、怎样按基础费加长挑战期。

## 官方为什么这样拆

- **能读本块基础费不是已经给了出块者 interchangeable：官方写头上本来就公开，不是已经给了出块者。**
- **看见能读到不是已经是 blob 基础费指令。**
- **看见合约读数不是已经是不变量 219。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经给了出块者 | 不是已经给了出块者 | 不是已经基础费烧掉/小费（158） |
| 已经是 blob 基础费指令 | 不是已经是 blob 基础费指令 | 不是已经blob 底价指令（219） |
| 已经是不变量 219 | 不是已经是不变量 219 | 不是已经1398 bfee-notmkt |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3198 read-basefee not already paid-to-proposer / not already blob-basefee / not already 219 正式三事（218 余量），必须分开是不是已经给了出块者、是不是已经是 blob 基础费指令、是不是已经是不变量 219。可以跳过「看见 3198 就已经改了费用市场」。不要另写 怎样用基础费设悬赏、怎样做气期货、怎样按基础费加长挑战期。218 BASEFEE opcode vs market bundled unbundling 在本页 item 2 续；续 [`worked-example-bfee-nothdr-vs-bundled.md`](worked-example-bfee-nothdr-vs-bundled.md)（不变量 1400 item 3）。

## 本页不抄

- 操作码号、气价档、测试向量、悬赏公式、规范提交哈希。
- 怎样用基础费设悬赏、怎样做气期货、怎样按基础费加长挑战期。
