# 例：看见基础费指令不是已经改了费用市场不是已经改了费用市场；看见BASEFEE is not already 1559 market不是已经是不变量 158；看见基础费指令不是已经改了费用市场不是已经 218 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-3198](https://eips.ethereum.org/EIPS/eip-3198)（Final, Core, BASEFEE opcode）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-3198 BASEFEE opcode not already 1559-market / not already 158-bundled / not already 218-bundled 正式三事（218 余量）/ not 1398 bfee-notmkt interchangeable / not 218 basefee-opcode-vs-market bundled interchangeable」，不是 basefee opcode vs market bundled（218），也不是已经 基础费≠小费（158），也不是已经 blob 基础费指令（219）。不要另写 怎样用基础费设悬赏、怎样做气期货、怎样按基础费加长挑战期。

## 官方三件事

1. **看见基础费指令不是已经改了费用市场 / 看见基础费指令不是已经改了费用市场 这份对象 is not already 已经改了费用市场 interchangeable，也不是已经 basefee opcode vs market bundled（218） interchangeable / 1398 bfee-notmkt interchangeable / 1399 bfee-notprop interchangeable，也不是已经 EIP-3198 BASEFEE opcode not already 1559-market / not already 158-bundled / not already 218-bundled 正式三事 bundled（218 item 1 余量） interchangeable / 218 bfee item 1 interchangeable。**  
   官方把基础费指令不是已经改了费用市场和已经改了费用市场写成两件。看见基础费指令不是已经改了费用市场，不是已经改了费用市场。

2. **看见BASEFEE is not already 1559 market / 看见基础费指令不是已经改了费用市场 / 这份对象 is not already 已经是不变量 158 interchangeable，也不是已经 basefee opcode vs market bundled（218） interchangeable / 1398 bfee-notmkt interchangeable / 1400 bfee-nothdr interchangeable，也不是已经 基础费≠小费 interchangeable / 158 基础费≠小费 interchangeable。**  
   官方把BASEFEE is not already 1559 market和已经是不变量 158写成两件。看见BASEFEE is not already 1559 market，不是已经是不变量 158。

3. **看见基础费指令不是已经改了费用市场 / 看见BASEFEE is not already 1559 market / 这份对象 is not already 已经 218 bundled interchangeable，也不是已经 basefee opcode vs market bundled（218） interchangeable / 1398 bfee-notmkt interchangeable / 1399 bfee-notprop interchangeable，也不是已经 blob 基础费指令 interchangeable / 219 blob 基础费指令 interchangeable。**  
   官方把基础费指令不是已经改了费用市场和已经 218 bundled写成两件。看见基础费指令不是已经改了费用市场，不是已经 218 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样用基础费设悬赏、怎样做气期货、怎样按基础费加长挑战期。

## 官方为什么这样拆

- **基础费指令不是已经改了费用市场 interchangeable：官方把读本块基础费和 1559 市场规则写成两件。**
- **看见能读基础费不是已经是不变量 158。**
- **看见读数旋钮不是已经 218 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了费用市场 | 不是已经改了费用市场 | 不是已经基础费≠小费（158） |
| 已经是不变量 158 | 不是已经是不变量 158 | 不是已经blob 基础费指令（219） |
| 已经 218 bundled | 不是已经 218 bundled | 不是已经1399 bfee-notprop |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3198 BASEFEE opcode not already 1559-market / not already 158-bundled / not already 218-bundled 正式三事（218 余量），必须分开是不是已经改了费用市场、是不是已经是不变量 158、是不是已经 218 bundled。可以跳过「看见 3198 就已经改了费用市场」。不要另写 怎样用基础费设悬赏、怎样做气期货、怎样按基础费加长挑战期。218 BASEFEE opcode vs market bundled unbundling 在本页 item 1 启动；续 [`worked-example-bfee-notprop-vs-bundled.md`](worked-example-bfee-notprop-vs-bundled.md)（不变量 1399 item 2）。

## 本页不抄

- 操作码号、气价档、测试向量、悬赏公式、规范提交哈希。
- 怎样用基础费设悬赏、怎样做气期货、怎样按基础费加长挑战期。
