# 例：看见旧式 RLP 列表不是已经是类型信封不是已经是类型信封；看见legacy RLP list is not already a typed envelope不是已经是 155；看见旧式 RLP 列表不是已经是类型信封不是已经把类型签进哈希

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2718](https://eips.ethereum.org/EIPS/eip-2718)（Final, Core, Typed Transaction Envelope）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-2718 legacy-RLP not already envelope / not already 155 / not already signed-type 正式三事（167 余量）/ not 1456 tenv-notenv interchangeable / not 167 typed-vs-legacy bundled interchangeable」，不是 typed vs legacy bundled（167），也不是已经 chainId≠已签（161），也不是已经 基础费≠小费（158）。不要另写 怎样跨类型复用签名。

## 官方三件事

1. **看见旧式 RLP 列表不是已经是类型信封 / 看见旧式 RLP 列表不是已经是类型信封 这份对象 is not already 已经是类型信封 interchangeable，也不是已经 typed vs legacy bundled（167） interchangeable / 1456 tenv-notenv interchangeable / 1455 tenv-notinner interchangeable，也不是已经 EIP-2718 legacy-RLP not already envelope / not already 155 / not already signed-type 正式三事 bundled（167 item 2 余量） interchangeable / 167 tenv item 2 interchangeable。**  
   官方把旧式 RLP 列表不是已经是类型信封和已经是类型信封写成两件。看见旧式 RLP 列表不是已经是类型信封，不是已经是类型信封。

2. **看见legacy RLP list is not already a typed envelope / 看见旧式 RLP 列表不是已经是类型信封 / 这份对象 is not already 已经是 155 interchangeable，也不是已经 typed vs legacy bundled（167） interchangeable / 1456 tenv-notenv interchangeable / 1457 tenv-notrcpt interchangeable，也不是已经 chainId≠已签 interchangeable / 161 chainId≠已签 interchangeable。**  
   官方把legacy RLP list is not already a typed envelope和已经是 155写成两件。看见legacy RLP list is not already a typed envelope，不是已经是 155。

3. **看见旧式 RLP 列表不是已经是类型信封 / 看见legacy RLP list is not already a typed envelope / 这份对象 is not already 已经把类型签进哈希 interchangeable，也不是已经 typed vs legacy bundled（167） interchangeable / 1456 tenv-notenv interchangeable / 1455 tenv-notinner interchangeable，也不是已经 基础费≠小费 interchangeable / 158 基础费≠小费 interchangeable。**  
   官方把旧式 RLP 列表不是已经是类型信封和已经把类型签进哈希写成两件。看见旧式 RLP 列表不是已经是类型信封，不是已经把类型签进哈希。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样跨类型复用签名。

## 官方为什么这样拆

- **旧式 RLP 列表不是已经是类型信封 interchangeable：官方写一笔交易要么是类型信封，要么是仍合法的旧式列表。**
- **看见本页不是已经是 155。**
- **看见信封在不是已经把类型签进哈希。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是类型信封 | 不是已经是类型信封 | 不是已经chainId≠已签（161） |
| 已经是 155 | 不是已经是 155 | 不是已经基础费≠小费（158） |
| 已经把类型签进哈希 | 不是已经把类型签进哈希 | 不是已经1455 tenv-notinner |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2718 legacy-RLP not already envelope / not already 155 / not already signed-type 正式三事（167 余量），必须分开是不是已经是类型信封、是不是已经是 155、是不是已经把类型签进哈希。可以跳过「带了类型 = 已经是 1559」。不要另写 怎样跨类型复用签名。167 typed vs legacy bundled unbundling 在本页 item 2 续；续 [`worked-example-tenv-notrcpt-vs-bundled.md`](worked-example-tenv-notrcpt-vs-bundled.md)（不变量 1457 item 3）。

## 本页不抄

- 类型取值范围、分叉高度、字段表。
- 怎样跨类型复用签名。
