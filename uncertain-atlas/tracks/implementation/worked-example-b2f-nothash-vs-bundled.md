# 例：看见BLAKE2 压缩函数 F 不是已经是 BLAKE2b 哈希不是已经是 BLAKE2b 哈希；看见F is not already BLAKE2b hash不是已经是 keccak / SHA3；看见BLAKE2 压缩函数 F 不是已经是 BLAKE2b 哈希不是已经 230 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-152](https://eips.ethereum.org/EIPS/eip-152)（Final, Core, Add BLAKE2 compression function F precompile）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-152 F not already BLAKE2b-hash / not already keccak / not already 230-bundled 正式三事（230 余量）/ not 1434 b2f-nothash interchangeable / not 230 blake2f-vs-hash bundled interchangeable」，不是 blake2f vs hash bundled（230），也不是已经 预编译算术≠已验 BLS（199），也不是已经 bn128降价≠已验签（228）。不要另写 怎样叠压缩函数去验工作量、怎样做跨链中继或原子交换。

## 官方三件事

1. **看见BLAKE2 压缩函数 F 不是已经是 BLAKE2b 哈希 / 看见BLAKE2 压缩函数 F 不是已经是 BLAKE2b 哈希 这份对象 is not already 已经是 BLAKE2b 哈希 interchangeable，也不是已经 blake2f vs hash bundled（230） interchangeable / 1434 b2f-nothash interchangeable / 1435 b2f-notprod interchangeable，也不是已经 EIP-152 F not already BLAKE2b-hash / not already keccak / not already 230-bundled 正式三事 bundled（230 item 1 余量） interchangeable / 230 b2f item 1 interchangeable。**  
   官方把BLAKE2 压缩函数 F 不是已经是 BLAKE2b 哈希和已经是 BLAKE2b 哈希写成两件。看见BLAKE2 压缩函数 F 不是已经是 BLAKE2b 哈希，不是已经是 BLAKE2b 哈希。

2. **看见F is not already BLAKE2b hash / 看见BLAKE2 压缩函数 F 不是已经是 BLAKE2b 哈希 / 这份对象 is not already 已经是 keccak / SHA3 interchangeable，也不是已经 blake2f vs hash bundled（230） interchangeable / 1434 b2f-nothash interchangeable / 1436 b2f-notapi interchangeable，也不是已经 预编译算术≠已验 BLS interchangeable / 199 预编译算术≠已验 BLS interchangeable。**  
   官方把F is not already BLAKE2b hash和已经是 keccak / SHA3写成两件。看见F is not already BLAKE2b hash，不是已经是 keccak / SHA3。

3. **看见BLAKE2 压缩函数 F 不是已经是 BLAKE2b 哈希 / 看见F is not already BLAKE2b hash / 这份对象 is not already 已经 230 bundled interchangeable，也不是已经 blake2f vs hash bundled（230） interchangeable / 1434 b2f-nothash interchangeable / 1435 b2f-notprod interchangeable，也不是已经 bn128降价≠已验签 interchangeable / 228 bn128降价≠已验签 interchangeable。**  
   官方把BLAKE2 压缩函数 F 不是已经是 BLAKE2b 哈希和已经 230 bundled写成两件。看见BLAKE2 压缩函数 F 不是已经是 BLAKE2b 哈希，不是已经 230 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样叠压缩函数去验工作量、怎样做跨链中继或原子交换。

## 官方为什么这样拆

- **BLAKE2 压缩函数 F 不是已经是 BLAKE2b 哈希 interchangeable：官方写本页只实现压缩函数 F，完整哈希是加分项。**
- **看见本页不是已经是 keccak / SHA3。**
- **看见读数旋钮不是已经 230 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是 BLAKE2b 哈希 | 不是已经是 BLAKE2b 哈希 | 不是已经预编译算术≠已验 BLS（199） |
| 已经是 keccak / SHA3 | 不是已经是 keccak / SHA3 | 不是已经bn128降价≠已验签（228） |
| 已经 230 bundled | 不是已经 230 bundled | 不是已经1435 b2f-notprod |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-152 F not already BLAKE2b-hash / not already keccak / not already 230-bundled 正式三事（230 余量），必须分开是不是已经是 BLAKE2b 哈希、是不是已经是 keccak / SHA3、是不是已经 230 bundled。可以跳过「看见 152 就已经能验 Equihash」。不要另写 怎样叠压缩函数去验工作量、怎样做跨链中继或原子交换。230 blake2f vs hash bundled unbundling 在本页 item 1 启动；续 [`worked-example-b2f-notprod-vs-bundled.md`](worked-example-b2f-notprod-vs-bundled.md)（不变量 1435 item 2）。

## 本页不抄

- 预编译地址、输入宽度、每轮气价、测试向量。
- 怎样叠压缩函数去验工作量、怎样做跨链中继或原子交换。
