# 模式：把 PrepareProposal When return / use-as-proposal 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When steps 4–5。  
**例**：[return / use-as-proposal ≠ bundled](../../tracks/implementation/worked-example-preparewhen-return-vs-bundled.md)。

## 三个名字

1. **includes tx list in return 不是 raw proposal bundled：** 看见 whether modified or not in return parameters per Usage，不是 503 Usage raw proposal interchangeable。
2. **returns from call 不是 Process 紧跟 Prepare bundled：** 看见 returns from the call，不是 351 Process 通常 txs 对得上 interchangeable。
3. **uses modified block as proposal 不是 validValue 跳过 Prepare：** 看见 uses possibly modified block as proposal，不是 356 validValue 跳过 interchangeable。

## 为什么要分开叫

官方把 includes in return、returns from call、uses as proposal、raw proposal bundled（503）、Process 提议者 Process bundled（351）、validValue 跳过 Prepare（356）写成三个名字。把它们叫成一个「看见应用改了列表就已经 raw proposal bundled interchangeable、已经 Process 紧跟 Prepare interchangeable、已经 validValue 跳过 Prepare interchangeable」，会把 return、returns、use-as-proposal 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When return / use-as-proposal 正式三事，先数清问的是 includes tx list in return 是不是 raw proposal bundled interchangeable、returns from call 是不是 Process 紧跟 Prepare bundled interchangeable、uses modified block as proposal 是不是 validValue 跳过 Prepare interchangeable，再决定要不要同一次发布。
