# 例：看见非零 calldata 降价不是已经给零字节也降价不是已经给零字节也降价；看见nonzero cut is not already zero-byte cut不是已经是 7623；看见非零 calldata 降价不是已经给零字节也降价不是已经 226 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2028](https://eips.ethereum.org/EIPS/eip-2028)（Final, Core, Transaction data gas cost reduction）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-2028 nonzero-cut not already zero-cut / not already 7623 / not already 226-bundled 正式三事（226 余量）/ not 1422 cdcut-notzero interchangeable / not 226 calldata-cut-vs-unlimited bundled interchangeable」，不是 calldata cut vs unlimited bundled（226），也不是已经 calldata 地板≠已改执行气（197），也不是已经 blob 气≠执行气（145）。不要另写 怎样往 calldata 里塞证明、怎样打满更大块、怎样按延迟模型定价。

## 官方三件事

1. **看见非零 calldata 降价不是已经给零字节也降价 / 看见非零 calldata 降价不是已经给零字节也降价 这份对象 is not already 已经给零字节也降价 interchangeable，也不是已经 calldata cut vs unlimited bundled（226） interchangeable / 1422 cdcut-notzero interchangeable / 1423 cdcut-notcap interchangeable，也不是已经 EIP-2028 nonzero-cut not already zero-cut / not already 7623 / not already 226-bundled 正式三事 bundled（226 item 1 余量） interchangeable / 226 cdcut item 1 interchangeable。**  
   官方把非零 calldata 降价不是已经给零字节也降价和已经给零字节也降价写成两件。看见非零 calldata 降价不是已经给零字节也降价，不是已经给零字节也降价。

2. **看见nonzero cut is not already zero-byte cut / 看见非零 calldata 降价不是已经给零字节也降价 / 这份对象 is not already 已经是 7623 interchangeable，也不是已经 calldata cut vs unlimited bundled（226） interchangeable / 1422 cdcut-notzero interchangeable / 1424 cdcut-notsafe interchangeable，也不是已经 calldata 地板≠已改执行气 interchangeable / 197 calldata 地板≠已改执行气 interchangeable。**  
   官方把nonzero cut is not already zero-byte cut和已经是 7623写成两件。看见nonzero cut is not already zero-byte cut，不是已经是 7623。

3. **看见非零 calldata 降价不是已经给零字节也降价 / 看见nonzero cut is not already zero-byte cut / 这份对象 is not already 已经 226 bundled interchangeable，也不是已经 calldata cut vs unlimited bundled（226） interchangeable / 1422 cdcut-notzero interchangeable / 1423 cdcut-notcap interchangeable，也不是已经 blob 气≠执行气 interchangeable / 145 blob 气≠执行气 interchangeable。**  
   官方把非零 calldata 降价不是已经给零字节也降价和已经 226 bundled写成两件。看见非零 calldata 降价不是已经给零字节也降价，不是已经 226 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样往 calldata 里塞证明、怎样打满更大块、怎样按延迟模型定价。

## 官方为什么这样拆

- **非零 calldata 降价不是已经给零字节也降价 interchangeable：官方只动非零字节，零字节气价不变。**
- **看见规范编号不是已经是 7623。**
- **看见读数旋钮不是已经 226 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经给零字节也降价 | 不是已经给零字节也降价 | 不是已经calldata 地板≠已改执行气（197） |
| 已经是 7623 | 不是已经是 7623 | 不是已经blob 气≠执行气（145） |
| 已经 226 bundled | 不是已经 226 bundled | 不是已经1423 cdcut-notcap |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2028 nonzero-cut not already zero-cut / not already 7623 / not already 226-bundled 正式三事（226 余量），必须分开是不是已经给零字节也降价、是不是已经是 7623、是不是已经 226 bundled。可以跳过「看见 2028 就已经没有上限」。不要另写 怎样往 calldata 里塞证明、怎样打满更大块、怎样按延迟模型定价。226 calldata-cut vs unlimited bundled unbundling 在本页 item 1 启动；续 [`worked-example-cdcut-notcap-vs-bundled.md`](worked-example-cdcut-notcap-vs-bundled.md)（不变量 1423 item 2）。

## 本页不抄

- 每字节气价、延迟公式、测试仓库。
- 怎样往 calldata 里塞证明、怎样打满更大块、怎样按延迟模型定价。
