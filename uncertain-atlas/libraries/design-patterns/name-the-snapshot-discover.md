# 模式：把快照发现三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Discovery。  
**例**：[ListSnapshots 回了 ≠ 已经有了全部快照](../../tracks/implementation/worked-example-snapshot-discover-vs-offer.md)。

## 三个名字

1. **ListSnapshots 回了不是已经有了全部快照：** 看见每节点 10 份不是已经齐。
2. **挑了最高不是已经收下：** 看见按高度排了不是已经是应用要的那份。
3. **Offer 被拒不是已经停：** 看见拒了格式不是已经没有快照。

## 为什么要分开叫

官方把每节点限额、本地挑选再 Offer、被拒继续发现写成三件事。把它们叫成一个「看见问了邻居就已经齐」，会把装回、轻验 AppHash 和启动对齐一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「已经在发现快照」，先数清问的是 ListSnapshots 回了不是已经齐、挑了最高不是已经收下，还是 Offer 被拒不是已经停，再决定要不要同一次发布。
