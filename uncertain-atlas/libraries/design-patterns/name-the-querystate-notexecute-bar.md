# 模式：把 Query 连接不是已经是 ExecuteTxState not already ExecuteTxState / not already writable / not already same as execute 正式三事（314 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Info/Query Connection。  
**例**：[能查 not already ExecuteTxState ≠ bundled（314）](../../tracks/implementation/worked-example-querystate-notexecute-vs-bundled.md)。

## 三个名字

1. **能查 不是 already ExecuteTxState：** 看见在答用户查询 / Query 连接在答，不是已经是工作状态 interchangeable / 已经 ExecuteTxState interchangeable，不是 314 querystate bundled interchangeable / 312 checktxstate bundled interchangeable / querystate-sold-as-execute interchangeable。

2. **连接在 不是 already writable：** 看见 Info 或 Query 连接开着 / 连接活着，不是已经能改工作状态 interchangeable / 已经能写 interchangeable，不是 314 querystate item 2 interchangeable / 702 querystate-notcaughtup interchangeable。

3. **名字里有 Query 不是 already same as execute：** 看见叫 QueryState / 门上写着 Query，不是已经和执行那份同一份 interchangeable / 已经两份合并 interchangeable，不是 314 querystate item 3 interchangeable / 703 querystate-notsnapshot interchangeable。

官方把能查单句、already ExecuteTxState、already writable、already same as execute 写成三个名字。把它们叫成一个「看见能查就已经是工作状态 interchangeable / 就已经能写 interchangeable / 就已经同一份 interchangeable」，会把 not already ExecuteTxState、not already writable、not already same as execute 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 连接不是已经是 ExecuteTxState not already ExecuteTxState / not already writable / not already same as execute 正式三事（314 余量），先数清问的是能查 是不是 already ExecuteTxState / 314 / querystate-sold-as-execute，是不是连接在 是不是 already writable，还是名字里有 Query 是不是 already same as execute，再决定要不要同一次发布。314 querystate vs execute bundled unbundling 在本页 item 1 完成。
