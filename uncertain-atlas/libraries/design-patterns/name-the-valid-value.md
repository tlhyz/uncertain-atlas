# 模式：把 validValue 跳过 Prepare 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**例**：[validValue 非 nil ≠ 已经还会调 Prepare](../../tracks/implementation/worked-example-validvalue-vs-prepare.md)。

## 三个名字

1. **validValue 非 nil 不是已经还会调 Prepare：** 看见本轮直接用它不是已经能再改列表。
2. **自己是提议者不是已经每轮都会调 Prepare：** 看见进了这一轮不是已经是 validValue 为 nil。
3. **没调 Prepare 不是已经又装了一份 raw 提案：** 看见用了 validValue 不是已经从池子再收一遍。

## 为什么要分开叫

官方把 validValue 非 nil 不再调 Prepare、只有提议者且 validValue 为 nil 才调、那条路上才会从池子收交易并造头写成三件事。把它们叫成一个「看见本轮直接用它就已经还会调 Prepare」，会把候选状态、Prepare 确定性和从提案拿掉一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见本轮直接用它就已经还会调 Prepare」，先数清问的是 validValue 非 nil 不是已经还会调 Prepare、自己是提议者不是已经每轮都会调 Prepare，还是没调 Prepare 不是已经又装了一份 raw 提案，再决定要不要同一次发布。
