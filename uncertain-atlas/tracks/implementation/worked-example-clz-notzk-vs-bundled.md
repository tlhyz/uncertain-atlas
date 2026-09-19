# 例：看见数前导零操作码不是已经更便宜的ZK证明不是已经更便宜的ZK证明；看见CLZ opcode is not already cheaper ZK不是已经是不变量 206；看见数前导零操作码不是已经更便宜的ZK证明不是已经 208 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7939](https://eips.ethereum.org/EIPS/eip-7939)（Count leading zeros (CLZ) opcode）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7939 clz not already cheaper-zk / not already 206 / not already 208-bundled 正式三事（208 余量）/ not 1470 clz-notzk interchangeable / not 208 clz-vs-zk bundled interchangeable」，不是 clz vs zk bundled（208），也不是已经 模幂长度帽≠已改计价（206），也不是已经 预编译算术≠已验BLS（199）。不要另写 怎样用它拼数尾零、怎样压证明费。

## 官方三件事

1. **看见数前导零操作码不是已经更便宜的ZK证明 / 看见数前导零操作码不是已经更便宜的ZK证明 这份对象 is not already 已经更便宜的ZK证明 interchangeable，也不是已经 clz vs zk bundled（208） interchangeable / 1470 clz-notzk interchangeable / 1471 clz-notpq interchangeable，也不是已经 EIP-7939 clz not already cheaper-zk / not already 206 / not already 208-bundled 正式三事 bundled（208 item 1 余量） interchangeable / 208 clz item 1 interchangeable。**  
   官方把数前导零操作码不是已经更便宜的ZK证明和已经更便宜的ZK证明写成两件。看见数前导零操作码不是已经更便宜的ZK证明，不是已经更便宜的ZK证明。

2. **看见CLZ opcode is not already cheaper ZK / 看见数前导零操作码不是已经更便宜的ZK证明 / 这份对象 is not already 已经是不变量 206 interchangeable，也不是已经 clz vs zk bundled（208） interchangeable / 1470 clz-notzk interchangeable / 1472 clz-notctz interchangeable，也不是已经 模幂长度帽≠已改计价 interchangeable / 206 模幂长度帽≠已改计价 interchangeable。**  
   官方把CLZ opcode is not already cheaper ZK和已经是不变量 206写成两件。看见CLZ opcode is not already cheaper ZK，不是已经是不变量 206。

3. **看见数前导零操作码不是已经更便宜的ZK证明 / 看见CLZ opcode is not already cheaper ZK / 这份对象 is not already 已经 208 bundled interchangeable，也不是已经 clz vs zk bundled（208） interchangeable / 1470 clz-notzk interchangeable / 1471 clz-notpq interchangeable，也不是已经 预编译算术≠已验BLS interchangeable / 199 预编译算术≠已验BLS interchangeable。**  
   官方把数前导零操作码不是已经更便宜的ZK证明和已经 208 bundled写成两件。看见数前导零操作码不是已经更便宜的ZK证明，不是已经 208 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样用它拼数尾零、怎样压证明费。

## 官方为什么这样拆

- **数前导零操作码不是已经更便宜的ZK证明 interchangeable：官方写预期证明更便宜，不是证明系统已经便宜。**
- **看见本页不是已经是不变量 206。**
- **看见读数旋钮不是已经 208 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经更便宜的ZK证明 | 不是已经更便宜的ZK证明 | 不是已经模幂长度帽≠已改计价（206） |
| 已经是不变量 206 | 不是已经是不变量 206 | 不是已经预编译算术≠已验BLS（199） |
| 已经 208 bundled | 不是已经 208 bundled | 不是已经1471 clz-notpq |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7939 clz not already cheaper-zk / not already 206 / not already 208-bundled 正式三事（208 余量），必须分开是不是已经更便宜的ZK证明、是不是已经是不变量 206、是不是已经 208 bundled。可以跳过「看见 7939 就已经更便宜的 ZK」。不要另写 怎样用它拼数尾零、怎样压证明费。208 clz vs zk bundled unbundling 在本页 item 1 启动；续 [`worked-example-clz-notpq-vs-bundled.md`](worked-example-clz-notpq-vs-bundled.md)（不变量 1471 item 2）。

## 本页不抄

- 操作码号、气价、高级语言实现、测试向量。
- 怎样用它拼数尾零、怎样压证明费。
