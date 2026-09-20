# 例：看见bn128 加 / 乘 / 配对降价不是已经换了算法不是已经换了算法；看见bn128 cut is not already algo-changed不是已经重新加入这三条预编译；看见bn128 加 / 乘 / 配对降价不是已经换了算法不是已经 228 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-1108](https://eips.ethereum.org/EIPS/eip-1108)（Final, Core, Reduce alt_bn128 precompile gas costs）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-1108 bn128-cut not already algo-changed / not already 196-197-readded / not already 228-bundled 正式三事（228 余量）/ not 1428 bn128-notalgo interchangeable / not 228 bn128-cut-vs-verify bundled interchangeable」，不是 bn128 cut vs verify bundled（228），也不是已经 预编译算术≠已验 BLS（199），也不是已经 模幂重计价≠已加帽（227）。不要另写 怎样拼配对、怎样做机密交易、怎样把状态收成一棵树再上证。

## 官方三件事

1. **看见bn128 加 / 乘 / 配对降价不是已经换了算法 / 看见bn128 加 / 乘 / 配对降价不是已经换了算法 这份对象 is not already 已经换了算法 interchangeable，也不是已经 bn128 cut vs verify bundled（228） interchangeable / 1428 bn128-notalgo interchangeable / 1429 bn128-notsig interchangeable，也不是已经 EIP-1108 bn128-cut not already algo-changed / not already 196-197-readded / not already 228-bundled 正式三事 bundled（228 item 1 余量） interchangeable / 228 bn128 item 1 interchangeable。**  
   官方把bn128 加 / 乘 / 配对降价不是已经换了算法和已经换了算法写成两件。看见bn128 加 / 乘 / 配对降价不是已经换了算法，不是已经换了算法。

2. **看见bn128 cut is not already algo-changed / 看见bn128 加 / 乘 / 配对降价不是已经换了算法 / 这份对象 is not already 已经重新加入这三条预编译 interchangeable，也不是已经 bn128 cut vs verify bundled（228） interchangeable / 1428 bn128-notalgo interchangeable / 1430 bn128-notgen interchangeable，也不是已经 预编译算术≠已验 BLS interchangeable / 199 预编译算术≠已验 BLS interchangeable。**  
   官方把bn128 cut is not already algo-changed和已经重新加入这三条预编译写成两件。看见bn128 cut is not already algo-changed，不是已经重新加入这三条预编译。

3. **看见bn128 加 / 乘 / 配对降价不是已经换了算法 / 看见bn128 cut is not already algo-changed / 这份对象 is not already 已经 228 bundled interchangeable，也不是已经 bn128 cut vs verify bundled（228） interchangeable / 1428 bn128-notalgo interchangeable / 1429 bn128-notsig interchangeable，也不是已经 模幂重计价≠已加帽 interchangeable / 227 模幂重计价≠已加帽 interchangeable。**  
   官方把bn128 加 / 乘 / 配对降价不是已经换了算法和已经 228 bundled写成两件。看见bn128 加 / 乘 / 配对降价不是已经换了算法，不是已经 228 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样拼配对、怎样做机密交易、怎样把状态收成一棵树再上证。

## 官方为什么这样拆

- **bn128 加 / 乘 / 配对降价不是已经换了算法 interchangeable：官方写底层算法没有改，只改气价。**
- **看见对照 196/197 不是已经重新加入这三条预编译。**
- **看见读数旋钮不是已经 228 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经换了算法 | 不是已经换了算法 | 不是已经预编译算术≠已验 BLS（199） |
| 已经重新加入这三条预编译 | 不是已经重新加入这三条预编译 | 不是已经模幂重计价≠已加帽（227） |
| 已经 228 bundled | 不是已经 228 bundled | 不是已经1429 bn128-notsig |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1108 bn128-cut not already algo-changed / not already 196-197-readded / not already 228-bundled 正式三事（228 余量），必须分开是不是已经换了算法、是不是已经重新加入这三条预编译、是不是已经 228 bundled。可以跳过「看见 1108 就已经在验签」。不要另写 怎样拼配对、怎样做机密交易、怎样把状态收成一棵树再上证。228 bn128-cut vs verify bundled unbundling 在本页 item 1 启动；续 [`worked-example-bn128-notsig-vs-bundled.md`](worked-example-bn128-notsig-vs-bundled.md)（不变量 1429 item 2）。

## 本页不抄

- 预编译地址、新旧气价、基准微秒、产品气账。
- 怎样拼配对、怎样做机密交易、怎样把状态收成一棵树再上证。
