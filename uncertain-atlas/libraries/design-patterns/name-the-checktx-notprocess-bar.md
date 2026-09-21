# 模式：把 ProcessProposal 对付这种行为不是已经是 CheckTx not already is-checktx / not already is-finalize / not already pool-done 正式三事（339 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Mempool Connection / CheckTx。  
**例**：[ProcessProposal 对付这种行为 not already is-checktx ≠ bundled（339）](../../tracks/implementation/worked-example-checktx-notprocess-vs-bundled.md)。

## 三个名字

1. **有 ProcessProposal 不是 already is-checktx：** 看见从 ABCI 1.0 起有 ProcessProposal 对付这种行为 / 有 ProcessProposal / 这道门对付拜占庭不守 CheckTx，不是已经是 CheckTx interchangeable / 已经是 CheckTx 交差 interchangeable，不是 339 checktxweak bundled interchangeable / 312 checktxstate interchangeable / checktxweak-sold-as-consensus interchangeable。

2. **点名了这道门 不是 already is-finalize：** 看见规范点名 ProcessProposal / 点名了这道门 / 规范写了 ProcessProposal，不是已经是 Finalize interchangeable / 已经 Finalize 交差 interchangeable，不是 33 four gates interchangeable / 339 checktxweak item 1 interchangeable。

3. **会拒提案 不是 already pool-done：** 看见会拒提案 / ProcessProposal 可以拒 / 会拒，不是已经在池子里挡完 interchangeable / 已经池子挡完交差 interchangeable，不是 313 indexer interchangeable / 339 checktxweak item 2 interchangeable。

官方把有 ProcessProposal 单句、already is-checktx、already is-finalize、already pool-done 写成三个名字。把它们叫成一个「看见有 ProcessProposal 就已经是 CheckTx interchangeable / 就已经是 Finalize interchangeable / 就已经在池子里挡完 interchangeable」，会把 not already is-checktx、not already is-finalize、not already pool-done 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal 对付这种行为不是已经是 CheckTx not already is-checktx / not already is-finalize / not already pool-done 正式三事（339 余量），先数清问的是有 ProcessProposal 是不是 already is-checktx / 339 / checktxweak-sold-as-consensus，是不是点名了这道门 是不是 already is-finalize，还是会拒提案 是不是 already pool-done，再决定要不要同一次发布。339 checktxweak vs process bundled unbundling 在本页 item 3 完成。
