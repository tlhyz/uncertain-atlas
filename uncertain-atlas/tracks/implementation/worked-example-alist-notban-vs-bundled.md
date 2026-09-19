# 例：看见列表外不是已经不能碰不是已经不能碰；看见outside the list is not already forbidden不是已经非法；看见列表外不是已经不能碰不是已经是 1559

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2930](https://eips.ethereum.org/EIPS/eip-2930)（Final, Core, Optional access lists）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-2930 outside-list not already forbidden / not already illegal / not already 1559 正式三事（168 余量）/ not 1453 alist-notban interchangeable / not 168 listed-vs-accessed bundled interchangeable」，不是 listed vs accessed bundled（168），也不是已经 基础费≠小费（158），也不是已经 信封≠内层（167）。不要另写 怎样生成列表、怎样灌重复项、怎样靠名单绕过冷访问。

## 官方三件事

1. **看见列表外不是已经不能碰 / 看见列表外不是已经不能碰 这份对象 is not already 已经不能碰 interchangeable，也不是已经 listed vs accessed bundled（168） interchangeable / 1453 alist-notban interchangeable / 1452 alist-notacc interchangeable，也不是已经 EIP-2930 outside-list not already forbidden / not already illegal / not already 1559 正式三事 bundled（168 item 2 余量） interchangeable / 168 alist item 2 interchangeable。**  
   官方把列表外不是已经不能碰和已经不能碰写成两件。看见列表外不是已经不能碰，不是已经不能碰。

2. **看见outside the list is not already forbidden / 看见列表外不是已经不能碰 / 这份对象 is not already 已经非法 interchangeable，也不是已经 listed vs accessed bundled（168） interchangeable / 1453 alist-notban interchangeable / 1454 alist-notread interchangeable，也不是已经 基础费≠小费 interchangeable / 158 基础费≠小费 interchangeable。**  
   官方把outside the list is not already forbidden和已经非法写成两件。看见outside the list is not already forbidden，不是已经非法。

3. **看见列表外不是已经不能碰 / 看见outside the list is not already forbidden / 这份对象 is not already 已经是 1559 interchangeable，也不是已经 listed vs accessed bundled（168） interchangeable / 1453 alist-notban interchangeable / 1452 alist-notacc interchangeable，也不是已经 信封≠内层 interchangeable / 167 信封≠内层 interchangeable。**  
   官方把列表外不是已经不能碰和已经是 1559写成两件。看见列表外不是已经不能碰，不是已经是 1559。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样生成列表、怎样灌重复项、怎样靠名单绕过冷访问。

## 官方为什么这样拆

- **列表外不是已经不能碰 interchangeable：官方写列表外仍可访问，只是更贵。**
- **看见列表外不是已经非法。**
- **看见本页不是已经是 1559。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经不能碰 | 不是已经不能碰 | 不是已经基础费≠小费（158） |
| 已经非法 | 不是已经非法 | 不是已经信封≠内层（167） |
| 已经是 1559 | 不是已经是 1559 | 不是已经1452 alist-notacc |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2930 outside-list not already forbidden / not already illegal / not already 1559 正式三事（168 余量），必须分开是不是已经不能碰、是不是已经非法、是不是已经是 1559。可以跳过「列入 = 已经访问」。不要另写 怎样生成列表、怎样灌重复项、怎样靠名单绕过冷访问。168 listed vs accessed bundled unbundling 在本页 item 2 续；续 [`worked-example-alist-notread-vs-bundled.md`](worked-example-alist-notread-vs-bundled.md)（不变量 1454 item 3）。

## 本页不抄

- 类型号、分叉高度、气价、例地址。
- 怎样生成列表、怎样灌重复项、怎样靠名单绕过冷访问。
