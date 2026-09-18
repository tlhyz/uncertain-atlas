# 例：看见降价不是已经没有块大小上限不是已经没有块大小上限；看见cheaper is not already no block-size cap不是已经解决数据可用性；看见降价不是已经没有块大小上限不是已经是 4844

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2028](https://eips.ethereum.org/EIPS/eip-2028)（Final, Core, Transaction data gas cost reduction）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-2028 cheaper not already no-block-cap / not already DA-solved / not already 4844 正式三事（226 余量）/ not 1423 cdcut-notcap interchangeable / not 226 calldata-cut-vs-unlimited bundled interchangeable」，不是 calldata cut vs unlimited bundled（226），也不是已经 blob 气≠执行气（145），也不是已经 基础费≠小费（158）。不要另写 怎样往 calldata 里塞证明、怎样打满更大块、怎样按延迟模型定价。

## 官方三件事

1. **看见降价不是已经没有块大小上限 / 看见降价不是已经没有块大小上限 这份对象 is not already 已经没有块大小上限 interchangeable，也不是已经 calldata cut vs unlimited bundled（226） interchangeable / 1423 cdcut-notcap interchangeable / 1422 cdcut-notzero interchangeable，也不是已经 EIP-2028 cheaper not already no-block-cap / not already DA-solved / not already 4844 正式三事 bundled（226 item 2 余量） interchangeable / 226 cdcut item 2 interchangeable。**  
   官方把降价不是已经没有块大小上限和已经没有块大小上限写成两件。看见降价不是已经没有块大小上限，不是已经没有块大小上限。

2. **看见cheaper is not already no block-size cap / 看见降价不是已经没有块大小上限 / 这份对象 is not already 已经解决数据可用性 interchangeable，也不是已经 calldata cut vs unlimited bundled（226） interchangeable / 1423 cdcut-notcap interchangeable / 1424 cdcut-notsafe interchangeable，也不是已经 blob 气≠执行气 interchangeable / 145 blob 气≠执行气 interchangeable。**  
   官方把cheaper is not already no block-size cap和已经解决数据可用性写成两件。看见cheaper is not already no block-size cap，不是已经解决数据可用性。

3. **看见降价不是已经没有块大小上限 / 看见cheaper is not already no block-size cap / 这份对象 is not already 已经是 4844 interchangeable，也不是已经 calldata cut vs unlimited bundled（226） interchangeable / 1423 cdcut-notcap interchangeable / 1422 cdcut-notzero interchangeable，也不是已经 基础费≠小费 interchangeable / 158 基础费≠小费 interchangeable。**  
   官方把降价不是已经没有块大小上限和已经是 4844写成两件。看见降价不是已经没有块大小上限，不是已经是 4844。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样往 calldata 里塞证明、怎样打满更大块、怎样按延迟模型定价。

## 官方为什么这样拆

- **降价不是已经没有块大小上限 interchangeable：官方写一块里能多塞数据，不是已经没有上限。**
- **看见贴在 calldata 不是已经解决数据可用性。**
- **看见本页不是已经是 4844。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经没有块大小上限 | 不是已经没有块大小上限 | 不是已经blob 气≠执行气（145） |
| 已经解决数据可用性 | 不是已经解决数据可用性 | 不是已经基础费≠小费（158） |
| 已经是 4844 | 不是已经是 4844 | 不是已经1422 cdcut-notzero |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2028 cheaper not already no-block-cap / not already DA-solved / not already 4844 正式三事（226 余量），必须分开是不是已经没有块大小上限、是不是已经解决数据可用性、是不是已经是 4844。可以跳过「看见 2028 就已经没有上限」。不要另写 怎样往 calldata 里塞证明、怎样打满更大块、怎样按延迟模型定价。226 calldata-cut vs unlimited bundled unbundling 在本页 item 2 续；续 [`worked-example-cdcut-notsafe-vs-bundled.md`](worked-example-cdcut-notsafe-vs-bundled.md)（不变量 1424 item 3）。

## 本页不抄

- 每字节气价、延迟公式、测试仓库。
- 怎样往 calldata 里塞证明、怎样打满更大块、怎样按延迟模型定价。
