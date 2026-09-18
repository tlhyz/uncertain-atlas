# 例：看见降价不是已经不伤网络延迟 / 安全不是已经不伤网络延迟 / 安全；看见cheaper is not already no delay/security impact不是已经不改安全；看见降价不是已经不伤网络延迟 / 安全不是已经是不变量 197

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2028](https://eips.ethereum.org/EIPS/eip-2028)（Final, Core, Transaction data gas cost reduction）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-2028 cheaper not already no-delay / not already no-security-change / not already 197 正式三事（226 余量）/ not 1424 cdcut-notsafe interchangeable / not 226 calldata-cut-vs-unlimited bundled interchangeable」，不是 calldata cut vs unlimited bundled（226），也不是已经 7623 地板（197），也不是已经 净计量≠瞬时存储（225）。不要另写 怎样往 calldata 里塞证明、怎样打满更大块、怎样按延迟模型定价。

## 官方三件事

1. **看见降价不是已经不伤网络延迟 / 安全 / 看见降价不是已经不伤网络延迟 / 安全 这份对象 is not already 已经不伤网络延迟 / 安全 interchangeable，也不是已经 calldata cut vs unlimited bundled（226） interchangeable / 1424 cdcut-notsafe interchangeable / 1422 cdcut-notzero interchangeable，也不是已经 EIP-2028 cheaper not already no-delay / not already no-security-change / not already 197 正式三事 bundled（226 item 3 余量） interchangeable / 226 cdcut item 3 interchangeable。**  
   官方把降价不是已经不伤网络延迟 / 安全和已经不伤网络延迟 / 安全写成两件。看见降价不是已经不伤网络延迟 / 安全，不是已经不伤网络延迟 / 安全。

2. **看见cheaper is not already no delay/security impact / 看见降价不是已经不伤网络延迟 / 安全 / 这份对象 is not already 已经不改安全 interchangeable，也不是已经 calldata cut vs unlimited bundled（226） interchangeable / 1424 cdcut-notsafe interchangeable / 1423 cdcut-notcap interchangeable，也不是已经 7623 地板 interchangeable / 197 7623 地板 interchangeable。**  
   官方把cheaper is not already no delay/security impact和已经不改安全写成两件。看见cheaper is not already no delay/security impact，不是已经不改安全。

3. **看见降价不是已经不伤网络延迟 / 安全 / 看见cheaper is not already no delay/security impact / 这份对象 is not already 已经是不变量 197 interchangeable，也不是已经 calldata cut vs unlimited bundled（226） interchangeable / 1424 cdcut-notsafe interchangeable / 1422 cdcut-notzero interchangeable，也不是已经 净计量≠瞬时存储 interchangeable / 225 净计量≠瞬时存储 interchangeable。**  
   官方把降价不是已经不伤网络延迟 / 安全和已经是不变量 197写成两件。看见降价不是已经不伤网络延迟 / 安全，不是已经是不变量 197。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样往 calldata 里塞证明、怎样打满更大块、怎样按延迟模型定价。

## 官方为什么这样拆

- **降价不是已经不伤网络延迟 / 安全 interchangeable：官方写更大块可能加大延迟、降低攻击成本。**
- **看见降价不是已经不改安全。**
- **看见本页不是已经是不变量 197。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经不伤网络延迟 / 安全 | 不是已经不伤网络延迟 / 安全 | 不是已经7623 地板（197） |
| 已经不改安全 | 不是已经不改安全 | 不是已经净计量≠瞬时存储（225） |
| 已经是不变量 197 | 不是已经是不变量 197 | 不是已经1422 cdcut-notzero |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2028 cheaper not already no-delay / not already no-security-change / not already 197 正式三事（226 余量），必须分开是不是已经不伤网络延迟 / 安全、是不是已经不改安全、是不是已经是不变量 197。可以跳过「看见 2028 就已经没有上限」。不要另写 怎样往 calldata 里塞证明、怎样打满更大块、怎样按延迟模型定价。226 calldata-cut vs unlimited bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：模幂计价≠已有界（227）。

## 本页不抄

- 每字节气价、延迟公式、测试仓库。
- 怎样往 calldata 里塞证明、怎样打满更大块、怎样按延迟模型定价。
