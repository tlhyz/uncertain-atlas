# 模式：把 Info 回包余栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Response / Query Response。  
**例**：[Info 回包 data 是任意信息 ≠ 已经是握手对齐](../../tracks/implementation/worked-example-infodata-vs-appversion.md)。

## 三个名字

1. **Info 回包 data 是任意信息不是已经是握手对齐：** 看见回了 data 不是已经是快照重放。
2. **Info 回包 version 是应用软件语义版本不是已经是 app_version：** 看见回了应用版本不是已经印进本头 AppHash。
3. **Query 回包 codespace 是码的命名空间不是已经是 CheckTx 码空间：** 看见写了空间不是已经是回包码。

## 为什么要分开叫

官方把 Info 回包 `data` 是任意信息、`version` 是应用软件语义版本、Query 回包 `codespace` 是码的命名空间写成三件事。把它们叫成一个「看见回了 Info 余栏就已经是握手对齐」，会把任意信息、app_version 和 CheckTx 码空间一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 Info 余栏就已经是握手对齐」，先数清问的是 Info 回包 data 是任意信息不是已经是握手对齐、Info 回包 version 是应用软件语义版本不是已经是 app_version，还是 Query 回包 codespace 是码的命名空间不是已经是 CheckTx 码空间，再决定要不要同一次发布。
