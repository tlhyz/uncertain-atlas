# 例：看见超帽不是已经成功返回不是已经成功返回；看见over-cap is not already a successful return不是已经是不变量 177；看见超帽不是已经成功返回不是已经是不变量 204

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7823](https://eips.ethereum.org/EIPS/eip-7823)（Set upper bounds for MODEXP）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7823 over-cap not already success / not already 177 / not already 204 正式三事（206 余量）/ not 1474 mxbd-notok interchangeable / not 206 modexp-bound-vs-price bundled interchangeable」，不是 modexp bound vs price bundled（206），也不是已经 回滚≠烧光（177），也不是已经 P256失败不revert（204）。不要另写 怎样造超长输入。

## 官方三件事

1. **看见超帽不是已经成功返回 / 看见超帽不是已经成功返回 这份对象 is not already 已经成功返回 interchangeable，也不是已经 modexp bound vs price bundled（206） interchangeable / 1474 mxbd-notok interchangeable / 1473 mxbd-notprice interchangeable，也不是已经 EIP-7823 over-cap not already success / not already 177 / not already 204 正式三事 bundled（206 item 2 余量） interchangeable / 206 mxbd item 2 interchangeable。**  
   官方把超帽不是已经成功返回和已经成功返回写成两件。看见超帽不是已经成功返回，不是已经成功返回。

2. **看见over-cap is not already a successful return / 看见超帽不是已经成功返回 / 这份对象 is not already 已经是不变量 177 interchangeable，也不是已经 modexp bound vs price bundled（206） interchangeable / 1474 mxbd-notok interchangeable / 1475 mxbd-notevm interchangeable，也不是已经 回滚≠烧光 interchangeable / 177 回滚≠烧光 interchangeable。**  
   官方把over-cap is not already a successful return和已经是不变量 177写成两件。看见over-cap is not already a successful return，不是已经是不变量 177。

3. **看见超帽不是已经成功返回 / 看见over-cap is not already a successful return / 这份对象 is not already 已经是不变量 204 interchangeable，也不是已经 modexp bound vs price bundled（206） interchangeable / 1474 mxbd-notok interchangeable / 1473 mxbd-notprice interchangeable，也不是已经 P256失败不revert interchangeable / 204 P256失败不revert interchangeable。**  
   官方把超帽不是已经成功返回和已经是不变量 204写成两件。看见超帽不是已经成功返回，不是已经是不变量 204。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造超长输入。

## 官方为什么这样拆

- **超帽不是已经成功返回 interchangeable：官方写任一段超帽停住、报错、把剩余气烧光，不是已经算出结果。**
- **看见本页不是已经是不变量 177。**
- **看见本页不是已经是不变量 204。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经成功返回 | 不是已经成功返回 | 不是已经回滚≠烧光（177） |
| 已经是不变量 177 | 不是已经是不变量 177 | 不是已经P256失败不revert（204） |
| 已经是不变量 204 | 不是已经是不变量 204 | 不是已经1473 mxbd-notprice |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7823 over-cap not already success / not already 177 / not already 204 正式三事（206 余量），必须分开是不是已经成功返回、是不是已经是不变量 177、是不是已经是不变量 204。可以跳过「看见 7823 就已经改了计价」。不要另写 怎样造超长输入。206 modexp-bound vs price bundled unbundling 在本页 item 2 续；续 [`worked-example-mxbd-notevm-vs-bundled.md`](worked-example-mxbd-notevm-vs-bundled.md)（不变量 1475 item 3）。

## 本页不抄

- 长度上限比特、字节、预编译地址、历史块号、调用次数表。
- 怎样造超长输入。
