# 反模式：把 Query 连接不是已经是 ExecuteTxState not already ExecuteTxState / not already writable / not already same as execute 正式三事（314 余量）说成已经是 ExecuteTxState / 已经能写 / 已经同一份

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[能查 not already ExecuteTxState ≠ bundled（314）](../../tracks/implementation/worked-example-querystate-notexecute-vs-bundled.md)。

## 卖法

把能查 / 在答用户查询 / Query 连接在答 写成已经是 ExecuteTxState interchangeable / 已经 working state interchangeable / 已经是工作状态 interchangeable / 314 querystate bundled interchangeable / 312 checktxstate bundled interchangeable / querystate-sold-as-execute interchangeable；把连接在 / Info 或 Query 连接开着 写成已经能改工作状态 interchangeable / 已经 writable interchangeable；把名字里有 Query / 叫 QueryState 写成已经和执行那份同一份 interchangeable / 已经 same as execute interchangeable，或已经和 314 querystate bundled / querystate-sold-as-execute interchangeable / 701 querystate-notexecute interchangeable。

## 为什么错

官方把能查单句、already ExecuteTxState、already writable、already same as execute 写成三件独立的实现事。把它们卖成 already ExecuteTxState interchangeable / already writable interchangeable / already same as execute interchangeable，会把 not already ExecuteTxState、not already writable、not already same as execute 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 连接不是已经是 ExecuteTxState not already ExecuteTxState / not already writable / not already same as execute 正式三事（314 余量），必须分开 not already ExecuteTxState、not already writable、not already same as execute 三件事，不要和 314 / 312 / 702 / 703 / 310 / 33 糊成一句。

## 和相邻反模式

- [querystate-sold-as-execute](querystate-sold-as-execute.md) 是 QueryState vs ExecuteTxState bundled 全段，不是本页能查 item 1 单句边界。
- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 CheckTxState vs ExecuteTxState（312），不是本页 Query 只读副本边界。
- [indexer-notappprotect-sold-as-bundled](indexer-notappprotect-sold-as-bundled.md) 是过了 CheckTx ≠ 应用级保护（313），不是本页连接在能否写边界。
