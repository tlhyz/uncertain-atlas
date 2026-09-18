# 例：看见更便宜不是已经在验签不是已经在验签；看见cheaper is not already verifying signatures不是已经上了隐私 / 扩容产品；看见更便宜不是已经在验签不是已经是 2537

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-1108](https://eips.ethereum.org/EIPS/eip-1108)（Final, Core, Reduce alt_bn128 precompile gas costs）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-1108 cheaper not already verifying / not already privacy-live / not already 2537 正式三事（228 余量）/ not 1429 bn128-notsig interchangeable / not 228 bn128-cut-vs-verify bundled interchangeable」，不是 bn128 cut vs verify bundled（228），也不是已经 2537 BLS12 算术（199），也不是已经 子群过了≠在曲线上（116）。不要另写 怎样拼配对、怎样做机密交易、怎样把状态收成一棵树再上证。

## 官方三件事

1. **看见更便宜不是已经在验签 / 看见更便宜不是已经在验签 这份对象 is not already 已经在验签 interchangeable，也不是已经 bn128 cut vs verify bundled（228） interchangeable / 1429 bn128-notsig interchangeable / 1428 bn128-notalgo interchangeable，也不是已经 EIP-1108 cheaper not already verifying / not already privacy-live / not already 2537 正式三事 bundled（228 item 2 余量） interchangeable / 228 bn128 item 2 interchangeable。**  
   官方把更便宜不是已经在验签和已经在验签写成两件。看见更便宜不是已经在验签，不是已经在验签。

2. **看见cheaper is not already verifying signatures / 看见更便宜不是已经在验签 / 这份对象 is not already 已经上了隐私 / 扩容产品 interchangeable，也不是已经 bn128 cut vs verify bundled（228） interchangeable / 1429 bn128-notsig interchangeable / 1430 bn128-notgen interchangeable，也不是已经 2537 BLS12 算术 interchangeable / 199 2537 BLS12 算术 interchangeable。**  
   官方把cheaper is not already verifying signatures和已经上了隐私 / 扩容产品写成两件。看见cheaper is not already verifying signatures，不是已经上了隐私 / 扩容产品。

3. **看见更便宜不是已经在验签 / 看见cheaper is not already verifying signatures / 这份对象 is not already 已经是 2537 interchangeable，也不是已经 bn128 cut vs verify bundled（228） interchangeable / 1429 bn128-notsig interchangeable / 1428 bn128-notalgo interchangeable，也不是已经 子群过了≠在曲线上 interchangeable / 116 子群过了≠在曲线上 interchangeable。**  
   官方把更便宜不是已经在验签和已经是 2537写成两件。看见更便宜不是已经在验签，不是已经是 2537。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样拼配对、怎样做机密交易、怎样把状态收成一棵树再上证。

## 官方为什么这样拆

- **更便宜不是已经在验签 interchangeable：官方把帮助隐私 / 扩容方案和已经在验签写成两件。**
- **看见更便宜不是已经上了隐私 / 扩容产品。**
- **看见规范编号不是已经是 2537。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经在验签 | 不是已经在验签 | 不是已经2537 BLS12 算术（199） |
| 已经上了隐私 / 扩容产品 | 不是已经上了隐私 / 扩容产品 | 不是已经子群过了≠在曲线上（116） |
| 已经是 2537 | 不是已经是 2537 | 不是已经1428 bn128-notalgo |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1108 cheaper not already verifying / not already privacy-live / not already 2537 正式三事（228 余量），必须分开是不是已经在验签、是不是已经上了隐私 / 扩容产品、是不是已经是 2537。可以跳过「看见 1108 就已经在验签」。不要另写 怎样拼配对、怎样做机密交易、怎样把状态收成一棵树再上证。228 bn128-cut vs verify bundled unbundling 在本页 item 2 续；续 [`worked-example-bn128-notgen-vs-bundled.md`](worked-example-bn128-notgen-vs-bundled.md)（不变量 1430 item 3）。

## 本页不抄

- 预编译地址、新旧气价、基准微秒、产品气账。
- 怎样拼配对、怎样做机密交易、怎样把状态收成一棵树再上证。
