# 模式：把切到共识三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transition to Consensus。  
**例**：[装完 ≠ 已经有了 ChainID](../../tracks/implementation/worked-example-snapshot-switch-vs-history.md)。

## 三个名字

1. **装完不是已经有了 ChainID：** 看见状态机恢复不是已经能出块。
2. **AppHash 对上不是已经版本也对上：** 看见对了下一高度不是已经对了当前头。
3. **切进共识不是已经有完整历史：** 看见能出块不是已经能给任意旧高度。

## 为什么要分开叫

官方把再凑引导信息、两次 Info 核对、历史截断写成三件事。把它们叫成一个「看见装完就已经是全节点」，会把轻验 AppHash、装回和发现一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「快照已经切进共识」，先数清问的是装完不是已经有了 ChainID、AppHash 对上不是已经版本也对上，还是切进共识不是已经有完整历史，再决定要不要同一次发布。
