# 例：看见给自己查余额不是已经按本账户价扣不是已经按本账户价扣；看见self-query is not already self-priced不是已经是更便宜的按地址查；看见给自己查余额不是已经按本账户价扣不是已经做完 1884

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-1884](https://eips.ethereum.org/EIPS/eip-1884)（Final, Core, Repricing for trie-size-dependent opcodes）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-1884 self-query not already self-priced / not already cheaper-BALANCE / not already 1884-done 正式三事（229 余量）/ not 1432 sbal-notself interchangeable / not 229 selfbalance-vs-balance bundled interchangeable」，不是 selfbalance vs balance bundled（229），也不是已经 冷热访问（169），也不是已经 bn128降价≠已验签（228）。不要另写 怎样绕过涨价、怎样在津贴帧里再读槽、怎样按旧价赌默认函数。

## 官方三件事

1. **看见给自己查余额不是已经按本账户价扣 / 看见给自己查余额不是已经按本账户价扣 这份对象 is not already 已经按本账户价扣 interchangeable，也不是已经 selfbalance vs balance bundled（229） interchangeable / 1432 sbal-notself interchangeable / 1431 sbal-notbal interchangeable，也不是已经 EIP-1884 self-query not already self-priced / not already cheaper-BALANCE / not already 1884-done 正式三事 bundled（229 item 2 余量） interchangeable / 229 sbal item 2 interchangeable。**  
   官方把给自己查余额不是已经按本账户价扣和已经按本账户价扣写成两件。看见给自己查余额不是已经按本账户价扣，不是已经按本账户价扣。

2. **看见self-query is not already self-priced / 看见给自己查余额不是已经按本账户价扣 / 这份对象 is not already 已经是更便宜的按地址查 interchangeable，也不是已经 selfbalance vs balance bundled（229） interchangeable / 1432 sbal-notself interchangeable / 1433 sbal-notwarm interchangeable，也不是已经 冷热访问 interchangeable / 169 冷热访问 interchangeable。**  
   官方把self-query is not already self-priced和已经是更便宜的按地址查写成两件。看见self-query is not already self-priced，不是已经是更便宜的按地址查。

3. **看见给自己查余额不是已经按本账户价扣 / 看见self-query is not already self-priced / 这份对象 is not already 已经做完 1884 interchangeable，也不是已经 selfbalance vs balance bundled（229） interchangeable / 1432 sbal-notself interchangeable / 1431 sbal-notbal interchangeable，也不是已经 bn128降价≠已验签 interchangeable / 228 bn128降价≠已验签 interchangeable。**  
   官方把给自己查余额不是已经按本账户价扣和已经做完 1884写成两件。看见给自己查余额不是已经按本账户价扣，不是已经做完 1884。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样绕过涨价、怎样在津贴帧里再读槽、怎样按旧价赌默认函数。

## 官方为什么这样拆

- **给自己查余额不是已经按本账户价扣 interchangeable：官方写按地址查自己仍走按地址那条、价仍按地址。**
- **看见给自己查余额不是已经是更便宜的按地址查。**
- **看见规范编号不是已经做完 1884。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经按本账户价扣 | 不是已经按本账户价扣 | 不是已经冷热访问（169） |
| 已经是更便宜的按地址查 | 不是已经是更便宜的按地址查 | 不是已经bn128降价≠已验签（228） |
| 已经做完 1884 | 不是已经做完 1884 | 不是已经1431 sbal-notbal |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1884 self-query not already self-priced / not already cheaper-BALANCE / not already 1884-done 正式三事（229 余量），必须分开是不是已经按本账户价扣、是不是已经是更便宜的按地址查、是不是已经做完 1884。可以跳过「看见 1884 就已经是 2929」。不要另写 怎样绕过涨价、怎样在津贴帧里再读槽、怎样按旧价赌默认函数。229 selfbalance vs balance bundled unbundling 在本页 item 2 续；续 [`worked-example-sbal-notwarm-vs-bundled.md`](worked-example-sbal-notwarm-vs-bundled.md)（不变量 1433 item 3）。

## 本页不抄

- 操作码号、新旧气价、津贴数字、接口气上限。
- 怎样绕过涨价、怎样在津贴帧里再读槽、怎样按旧价赌默认函数。
