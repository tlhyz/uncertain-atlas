# 例：看见看见收据不是收据类型已经对上该笔不是收据类型已经对上该笔；看见seeing a receipt is not already type-matched不是已经是不变量 158；看见看见收据不是收据类型已经对上该笔不是已经是不变量 161

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2718](https://eips.ethereum.org/EIPS/eip-2718)（Final, Core, Typed Transaction Envelope）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-2718 seeing-receipt not already type-matched / not already 158 / not already 161 正式三事（167 余量）/ not 1457 tenv-notrcpt interchangeable / not 167 typed-vs-legacy bundled interchangeable」，不是 typed vs legacy bundled（167），也不是已经 基础费≠小费（158），也不是已经 chainId≠已签（161）。不要另写 怎样跨类型复用签名。

## 官方三件事

1. **看见看见收据不是收据类型已经对上该笔 / 看见看见收据不是收据类型已经对上该笔 这份对象 is not already 收据类型已经对上该笔 interchangeable，也不是已经 typed vs legacy bundled（167） interchangeable / 1457 tenv-notrcpt interchangeable / 1455 tenv-notinner interchangeable，也不是已经 EIP-2718 seeing-receipt not already type-matched / not already 158 / not already 161 正式三事 bundled（167 item 3 余量） interchangeable / 167 tenv item 3 interchangeable。**  
   官方把看见收据不是收据类型已经对上该笔和收据类型已经对上该笔写成两件。看见看见收据不是收据类型已经对上该笔，不是收据类型已经对上该笔。

2. **看见seeing a receipt is not already type-matched / 看见看见收据不是收据类型已经对上该笔 / 这份对象 is not already 已经是不变量 158 interchangeable，也不是已经 typed vs legacy bundled（167） interchangeable / 1457 tenv-notrcpt interchangeable / 1456 tenv-notenv interchangeable，也不是已经 基础费≠小费 interchangeable / 158 基础费≠小费 interchangeable。**  
   官方把seeing a receipt is not already type-matched和已经是不变量 158写成两件。看见seeing a receipt is not already type-matched，不是已经是不变量 158。

3. **看见看见收据不是收据类型已经对上该笔 / 看见seeing a receipt is not already type-matched / 这份对象 is not already 已经是不变量 161 interchangeable，也不是已经 typed vs legacy bundled（167） interchangeable / 1457 tenv-notrcpt interchangeable / 1455 tenv-notinner interchangeable，也不是已经 chainId≠已签 interchangeable / 161 chainId≠已签 interchangeable。**  
   官方把看见收据不是收据类型已经对上该笔和已经是不变量 161写成两件。看见看见收据不是收据类型已经对上该笔，不是已经是不变量 161。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样跨类型复用签名。

## 官方为什么这样拆

- **看见收据不是收据类型已经对上该笔 interchangeable：官方写同一下标的收据类型必须对上那笔交易，看见不是已经对上。**
- **看见本页不是已经是不变量 158。**
- **看见本页不是已经是不变量 161。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 收据类型已经对上该笔 | 不是收据类型已经对上该笔 | 不是已经基础费≠小费（158） |
| 已经是不变量 158 | 不是已经是不变量 158 | 不是已经chainId≠已签（161） |
| 已经是不变量 161 | 不是已经是不变量 161 | 不是已经1455 tenv-notinner |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2718 seeing-receipt not already type-matched / not already 158 / not already 161 正式三事（167 余量），必须分开是不是收据类型已经对上该笔、是不是已经是不变量 158、是不是已经是不变量 161。可以跳过「带了类型 = 已经是 1559」。不要另写 怎样跨类型复用签名。167 typed vs legacy bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：default-gas（211）。

## 本页不抄

- 类型取值范围、分叉高度、字段表。
- 怎样跨类型复用签名。
