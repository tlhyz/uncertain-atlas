# 例：看见动机写了后量子签不是已经有后量子签名不是已经有后量子签名；看见PQ motive is not already a PQ signature不是已经是不变量 199；看见动机写了后量子签不是已经有后量子签名不是已经是不变量 204

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7939](https://eips.ethereum.org/EIPS/eip-7939)（Count leading zeros (CLZ) opcode）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7939 pq-motive not already pq-sig / not already 199 / not already 204 正式三事（208 余量）/ not 1471 clz-notpq interchangeable / not 208 clz-vs-zk bundled interchangeable」，不是 clz vs zk bundled（208），也不是已经 预编译算术≠已验BLS（199），也不是已经 P256≠k1（204）。不要另写 怎样用它拼数尾零、怎样压证明费。

## 官方三件事

1. **看见动机写了后量子签不是已经有后量子签名 / 看见动机写了后量子签不是已经有后量子签名 这份对象 is not already 已经有后量子签名 interchangeable，也不是已经 clz vs zk bundled（208） interchangeable / 1471 clz-notpq interchangeable / 1470 clz-notzk interchangeable，也不是已经 EIP-7939 pq-motive not already pq-sig / not already 199 / not already 204 正式三事 bundled（208 item 2 余量） interchangeable / 208 clz item 2 interchangeable。**  
   官方把动机写了后量子签不是已经有后量子签名和已经有后量子签名写成两件。看见动机写了后量子签不是已经有后量子签名，不是已经有后量子签名。

2. **看见PQ motive is not already a PQ signature / 看见动机写了后量子签不是已经有后量子签名 / 这份对象 is not already 已经是不变量 199 interchangeable，也不是已经 clz vs zk bundled（208） interchangeable / 1471 clz-notpq interchangeable / 1472 clz-notctz interchangeable，也不是已经 预编译算术≠已验BLS interchangeable / 199 预编译算术≠已验BLS interchangeable。**  
   官方把PQ motive is not already a PQ signature和已经是不变量 199写成两件。看见PQ motive is not already a PQ signature，不是已经是不变量 199。

3. **看见动机写了后量子签不是已经有后量子签名 / 看见PQ motive is not already a PQ signature / 这份对象 is not already 已经是不变量 204 interchangeable，也不是已经 clz vs zk bundled（208） interchangeable / 1471 clz-notpq interchangeable / 1470 clz-notzk interchangeable，也不是已经 P256≠k1 interchangeable / 204 P256≠k1 interchangeable。**  
   官方把动机写了后量子签不是已经有后量子签名和已经是不变量 204写成两件。看见动机写了后量子签不是已经有后量子签名，不是已经是不变量 204。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样用它拼数尾零、怎样压证明费。

## 官方为什么这样拆

- **动机写了后量子签不是已经有后量子签名 interchangeable：官方写它是一块积木，不是签名已经换完。**
- **看见本页不是已经是不变量 199。**
- **看见本页不是已经是不变量 204。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经有后量子签名 | 不是已经有后量子签名 | 不是已经预编译算术≠已验BLS（199） |
| 已经是不变量 199 | 不是已经是不变量 199 | 不是已经P256≠k1（204） |
| 已经是不变量 204 | 不是已经是不变量 204 | 不是已经1470 clz-notzk |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7939 pq-motive not already pq-sig / not already 199 / not already 204 正式三事（208 余量），必须分开是不是已经有后量子签名、是不是已经是不变量 199、是不是已经是不变量 204。可以跳过「看见 7939 就已经更便宜的 ZK」。不要另写 怎样用它拼数尾零、怎样压证明费。208 clz vs zk bundled unbundling 在本页 item 2 续；续 [`worked-example-clz-notctz-vs-bundled.md`](worked-example-clz-notctz-vs-bundled.md)（不变量 1472 item 3）。

## 本页不抄

- 操作码号、气价、高级语言实现、测试向量。
- 怎样用它拼数尾零、怎样压证明费。
