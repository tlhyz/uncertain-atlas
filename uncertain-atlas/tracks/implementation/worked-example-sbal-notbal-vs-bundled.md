# 例：看见本账户余额指令不是已经是按地址查余额不是已经是按地址查余额；看见SELFBALANCE is not already BALANCE不是已经改了余额语义；看见本账户余额指令不是已经是按地址查余额不是已经 229 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-1884](https://eips.ethereum.org/EIPS/eip-1884)（Final, Core, Repricing for trie-size-dependent opcodes）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-1884 selfbalance not already BALANCE / not already stack-pop-balance / not already 229-bundled 正式三事（229 余量）/ not 1431 sbal-notbal interchangeable / not 229 selfbalance-vs-balance bundled interchangeable」，不是 selfbalance vs balance bundled（229），也不是已经 本笔第一次碰≠已经热（169），也不是已经 代码哈希指令≠已看见代码（221）。不要另写 怎样绕过涨价、怎样在津贴帧里再读槽、怎样按旧价赌默认函数。

## 官方三件事

1. **看见本账户余额指令不是已经是按地址查余额 / 看见本账户余额指令不是已经是按地址查余额 这份对象 is not already 已经是按地址查余额 interchangeable，也不是已经 selfbalance vs balance bundled（229） interchangeable / 1431 sbal-notbal interchangeable / 1432 sbal-notself interchangeable，也不是已经 EIP-1884 selfbalance not already BALANCE / not already stack-pop-balance / not already 229-bundled 正式三事 bundled（229 item 1 余量） interchangeable / 229 sbal item 1 interchangeable。**  
   官方把本账户余额指令不是已经是按地址查余额和已经是按地址查余额写成两件。看见本账户余额指令不是已经是按地址查余额，不是已经是按地址查余额。

2. **看见SELFBALANCE is not already BALANCE / 看见本账户余额指令不是已经是按地址查余额 / 这份对象 is not already 已经改了余额语义 interchangeable，也不是已经 selfbalance vs balance bundled（229） interchangeable / 1431 sbal-notbal interchangeable / 1433 sbal-notwarm interchangeable，也不是已经 本笔第一次碰≠已经热 interchangeable / 169 本笔第一次碰≠已经热 interchangeable。**  
   官方把SELFBALANCE is not already BALANCE和已经改了余额语义写成两件。看见SELFBALANCE is not already BALANCE，不是已经改了余额语义。

3. **看见本账户余额指令不是已经是按地址查余额 / 看见SELFBALANCE is not already BALANCE / 这份对象 is not already 已经 229 bundled interchangeable，也不是已经 selfbalance vs balance bundled（229） interchangeable / 1431 sbal-notbal interchangeable / 1432 sbal-notself interchangeable，也不是已经 代码哈希指令≠已看见代码 interchangeable / 221 代码哈希指令≠已看见代码 interchangeable。**  
   官方把本账户余额指令不是已经是按地址查余额和已经 229 bundled写成两件。看见本账户余额指令不是已经是按地址查余额，不是已经 229 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样绕过涨价、怎样在津贴帧里再读槽、怎样按旧价赌默认函数。

## 官方为什么这样拆

- **本账户余额指令不是已经是按地址查余额 interchangeable：官方写本页加入一条不弹地址、压回当前地址余额的指令。**
- **看见本账户余额指令不是已经改了余额语义。**
- **看见读数旋钮不是已经 229 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是按地址查余额 | 不是已经是按地址查余额 | 不是已经本笔第一次碰≠已经热（169） |
| 已经改了余额语义 | 不是已经改了余额语义 | 不是已经代码哈希指令≠已看见代码（221） |
| 已经 229 bundled | 不是已经 229 bundled | 不是已经1432 sbal-notself |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1884 selfbalance not already BALANCE / not already stack-pop-balance / not already 229-bundled 正式三事（229 余量），必须分开是不是已经是按地址查余额、是不是已经改了余额语义、是不是已经 229 bundled。可以跳过「看见 1884 就已经是 2929」。不要另写 怎样绕过涨价、怎样在津贴帧里再读槽、怎样按旧价赌默认函数。229 selfbalance vs balance bundled unbundling 在本页 item 1 启动；续 [`worked-example-sbal-notself-vs-bundled.md`](worked-example-sbal-notself-vs-bundled.md)（不变量 1432 item 2）。

## 本页不抄

- 操作码号、新旧气价、津贴数字、接口气上限。
- 怎样绕过涨价、怎样在津贴帧里再读槽、怎样按旧价赌默认函数。
