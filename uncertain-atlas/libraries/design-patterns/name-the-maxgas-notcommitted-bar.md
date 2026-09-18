# 模式：把已提交块不是已经按气验过 not already gas-checked / not already consensus-enforced / not already default Prepare Process capping 正式三事（315 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Gas。  
**例**：[块已经提交 not already gas-checked ≠ bundled（315）](../../tracks/implementation/worked-example-maxgas-notcommitted-vs-bundled.md)。

## 三个名字

1. **块已经提交 不是 already gas-checked：** 看见已提交块 / 旧版只在内存池管气，不是已经按气验过 interchangeable / 已经保证这块守了气限 interchangeable，不是 315 maxgas bundled interchangeable / 33 four gates interchangeable / maxgas-sold-as-enforced interchangeable。

2. **池子守了 不是 already consensus-enforced：** 看见内存池管了气 / 只在内存池管，不是已经共识守了 interchangeable / 已经由共识层验过 interchangeable，不是 315 maxgas item 2 interchangeable / 705 maxgas-notgasused interchangeable。

3. **有了 Prepare / Process 不是 already default Prepare Process capping：** 看见 v0.37.x 有了 PrepareProposal / ProcessProposal / 应用能用 Prepare Process 卡 MaxGas，不是已经默认在卡气 interchangeable / 已经默认守 MaxGas interchangeable，不是 315 maxgas item 1 interchangeable / 704 maxgas-notenforced interchangeable。

官方把块已经提交单句、already gas-checked、already consensus-enforced、already default Prepare Process capping 写成三个名字。把它们叫成一个「看见已提交就已经按气验过 interchangeable / 就已经共识守了 interchangeable / 就已经默认卡气 interchangeable」，会把 not already gas-checked、not already consensus-enforced、not already default Prepare Process capping 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看已提交块不是已经按气验过 not already gas-checked / not already consensus-enforced / not already default Prepare Process capping 正式三事（315 余量），先数清问的是块已经提交 是不是 already gas-checked / 315 / maxgas-sold-as-enforced，是不是池子守了 是不是 already consensus-enforced，还是有了 Prepare / Process 是不是 already default Prepare Process capping，再决定要不要同一次发布。315 maxgas vs enforced bundled unbundling 在本页 item 3 完成。
