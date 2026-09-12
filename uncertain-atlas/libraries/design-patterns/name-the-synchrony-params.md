# 模式：把 SynchronyParams 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / SynchronyParams.Precision / SynchronyParams.MessageDelay。  
**例**：[填了 Precision ≠ 已经是 MessageDelay](../../tracks/implementation/worked-example-precision-vs-msgdelay.md)。

## 三个名字

1. **Precision 不是已经是 MessageDelay：** 看见钟偏有界不是延迟已经有界。
2. **填了两个不是已经启用 PBTS：** 看见写了用于 PBTS 不是已经到了 PbtsEnableHeight。
3. **用于 PBTS 不是已经是永恒常数：** 看见能出合法提案不是已经是 BFT Time 中位数。

## 为什么要分开叫

官方把钟偏、消息延迟、以及这两把尺由 PBTS 使用写成三件事。把它们叫成一个「看见填了同步参数就已经是 PBTS」，会把块时间算法、扩展启用高度和提议超时一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「填了 Precision 就已经是 PBTS」，先数清问的是 Precision 不是已经是 MessageDelay、填了两个不是已经启用 PBTS，还是用于 PBTS 不是已经是永恒常数，再决定要不要同一次发布。
