# 模式：把 Snapshot Connection 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Connection。  
**例**：[四门里有 Snapshot Connection ≠ 已经必须实现快照](../../tracks/implementation/worked-example-snapshot-conn-vs-required.md)。

## 三个名字

1. **四门里有 Snapshot Connection 不是已经必须实现快照：** 看见连接名在不是已经拍过。
2. **给人快照或给自己装回不是已经必须两头都做：** 看见写了「和 / 或」不是已经两头都做了。
3. **应用选择不实现不是已经没有 state sync 这条对象：** 看见可选不是已经从创世是唯一合法路径。

## 为什么要分开叫

官方把门的存在、给人快照和 / 或给自己装回、应用可以不实现写成三件事。把它们叫成一个「看见四门就已经必须做快照」，会把发现清单、装回和从创世一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「四门里有 Snapshot Connection 就必须实现快照」，先数清问的是门在不是已经必须实现、给人快照或给自己装回不是已经必须两头都做，还是选择不实现不是已经没有这条对象，再决定要不要同一次发布。
