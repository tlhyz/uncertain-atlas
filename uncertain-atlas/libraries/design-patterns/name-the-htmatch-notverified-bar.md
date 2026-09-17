# 模式：把头字段对上余量 Process height/time match header not already verified 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage / When。  
**例**：[头字段对上余量 Process height/time match header not already verified ≠ bundled](../../tracks/implementation/worked-example-htmatch-notverified-vs-bundled.md)。

## 三个名字

1. **Process height/time match header not already verified 不是头字段对上余量 bundled：** 看见 Process 对上了不是已经验过块头，不是 417 bundled interchangeable / 416 When verify header interchangeable / 354 When async interchangeable。
2. **Process height/time match header not already ran Process 不是 351 Process follows Prepare：** 看见 Usage match 不是已经跑过 Process，不是 417 bundled interchangeable / 351 Process follows Prepare interchangeable / 430 ACCEPT prevote interchangeable。
3. **Process height/time match header not header fields bundled know hash 不是 311 Prepare 没有头哈希：** 看见对上了不是已经知道本头哈希，不是 417 bundled interchangeable / 311 Prepare no header hash interchangeable / 419 Process hash interchangeable。

## 为什么要分开叫

官方把头字段对上余量 Process height/time match header not already verified 写成三个名字。把它们叫成一个「看见 Process 对上了 就已经验过块头 / 已经跑过 Process」，会把 Process match vs verified、Process match vs ran Process、Process match vs know hash 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头字段对上余量 Process height/time match header not already verified 正式三事，先数清问的是 Process match 是不是 already verified、Process match 是不是 already ran Process、Process match 是不是 header fields bundled know hash，再决定要不要同一次发布。
