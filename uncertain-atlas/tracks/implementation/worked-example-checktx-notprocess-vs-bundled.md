# 例：看见从 ABCI 1.0 起有 ProcessProposal 对付这种行为 / 看见规范点名 ProcessProposal / 看见会拒提案 is not already already is-checktx interchangeable / already is-finalize interchangeable / already pool-done interchangeable

**层次**：实现 / ProcessProposal 对付这种行为不是已经是 CheckTx not already is-checktx / not already is-finalize / not already pool-done 正式三事（339 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Mempool Connection / CheckTx。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool 整池已经交差。本页是「ProcessProposal 对付这种行为不是已经是 CheckTx not already is-checktx / not already is-finalize / not already pool-done 正式三事（339 余量）/ not 772 checktx-notprocess interchangeable / not 339 checktxweak bundled interchangeable」，不是 CheckTx 弱过滤器 bundled（339），也不是不该验排序相关有效性不是已经该在 CheckTx 里验（770 item 1 余量）或拜占庭能提案一满块无效交易不是已经被池子挡住（771 item 2 余量）。不要另写怎样写 CheckTx 或怎样写 ProcessProposal。

## 官方三件事

规范把 Requirements 里从 ABCI 1.0 起有 ProcessProposal 对付这种行为、规范点名 ProcessProposal 和「已经是有 ProcessProposal 就已经是 CheckTx interchangeable / 已经是点名了这道门就已经是 Finalize interchangeable / 已经是会拒提案就已经在池子里挡完 interchangeable / 已经是 checktxweak bundled interchangeable」分开写成三件独立的实现事，不是「看见有 ProcessProposal 就已经是 CheckTx interchangeable / 就已经是 Finalize interchangeable / 就已经在池子里挡完 interchangeable」一件事：

1. **看见从 ABCI 1.0 起有 ProcessProposal 对付这种行为 / 看见有 ProcessProposal / 看见这道门对付拜占庭不守 CheckTx is not already 已经是 CheckTx interchangeable / 已经 is-checktx interchangeable / 已经是 CheckTx 交差 interchangeable / 339 checktxweak bundled interchangeable / 312 checktxstate interchangeable / checktxweak-sold-as-consensus interchangeable，也不是已经 CheckTx 弱过滤器 bundled（339） interchangeable / 772 checktx-notprocess interchangeable / 339 checktxweak item 3 interchangeable，也不是已经 ProcessProposal 对付这种行为不是已经是 CheckTx not already is-checktx / not already is-finalize / not already pool-done 正式三事 bundled（339 item 3 余量） interchangeable / 339 checktxweak item 3 interchangeable，也不是已经不该验排序相关有效性不是已经该在 CheckTx 里验（770） interchangeable / 771 checktx-notblocked interchangeable / 33 four gates interchangeable，也不是已经 CheckTxState 已经是 ExecuteTxState（312） interchangeable。**  
   官方写：从 ABCI 1.0 起，对付这种行为的机制是 `ProcessProposal`。看见有 ProcessProposal，不是已经是 CheckTx。看见有 ProcessProposal，不是已经 is-checktx interchangeable——339 钉 bundled 三事，本页从 item 3 侧钉 not already is-checktx 单句。看见这道门对付拜占庭不守 CheckTx，不是已经 CheckTx 弱过滤器 bundled（339） interchangeable——339 钉 bundled，本页钉 item 3 第一件事。看见有 ProcessProposal，不是已经 CheckTxState 已经是 ExecuteTxState（312） interchangeable——312 另钉。339 checktxweak vs process bundled unbundling 在本页 item 3 完成。

2. **看见规范点名 ProcessProposal / 看见点名了这道门 / 看见规范写了 ProcessProposal is not already 已经是 Finalize interchangeable / 已经 is-finalize interchangeable / 已经 Finalize 交差 interchangeable / 339 checktxweak bundled interchangeable / 33 four gates interchangeable，也不是已经 CheckTx 弱过滤器 bundled（339） interchangeable / 772 checktx-notprocess interchangeable / 339 checktxweak item 1 排序 interchangeable / 339 checktxweak item 2 池子挡住 interchangeable，也不是已经 ProcessProposal 对付这种行为不是已经是 CheckTx not already is-checktx / not already is-finalize / not already pool-done 正式三事 bundled（339 item 3 余量） interchangeable / 339 checktxweak item 3 interchangeable，也不是已经是 CheckTx（本页第一件事） interchangeable。**  
   官方写：看见点名了这道门，不是已经 Finalize。看见规范点名 ProcessProposal，不是已经 is-finalize interchangeable——本页钉 not already is-finalize 单句。看见规范写了 ProcessProposal，不是已经是 CheckTx（本页第一件事） interchangeable——三件事分开钉。339 checktxweak vs process bundled unbundling 在本页 item 3 完成。

3. **看见会拒提案 / 看见 ProcessProposal 可以拒 / 看见会拒 is not already 已经在池子里挡完 interchangeable / 已经 pool-done interchangeable / 已经池子挡完交差 interchangeable / 339 checktxweak bundled interchangeable / 313 indexer interchangeable，也不是已经 CheckTx 弱过滤器 bundled（339） interchangeable / 772 checktx-notprocess interchangeable / 339 checktxweak item 1 / 339 checktxweak item 2，也不是已经 ProcessProposal 对付这种行为不是已经是 CheckTx not already is-checktx / not already is-finalize / not already pool-done 正式三事 bundled（339 item 3 余量） interchangeable / 339 checktxweak item 3 interchangeable，也不是已经是 CheckTx（本页第一件事） interchangeable / 已经是 Finalize（本页第二件事） interchangeable。**  
   官方写：看见会拒提案，不是已经在池子里挡完。看见 ProcessProposal 可以拒，不是已经 pool-done interchangeable——本页钉 not already pool-done 单句。看见会拒，不是已经是 Finalize（本页第二件事） interchangeable——三件事分开钉。339 checktxweak vs process bundled unbundling 在本页 item 3 完成。

怎样写 `CheckTx`、怎样挑哪些检查留给 Process、怎样写 `ProcessProposal` 是规范里的做法，本页不抄。CheckTx 弱过滤器 bundled（339）、不该验排序相关有效性不是已经该在 CheckTx 里验（339 item 1 余量 / 770）、拜占庭能提案一满块无效交易不是已经被池子挡住（339 item 2 余量 / 771）、CheckTxState 已经是 ExecuteTxState（312）、四门已经结算（33）、索引器已经保证不重放（313）是另外那套，本页不抄。

## 官方为什么这样拆

- **有 ProcessProposal not already is-checktx ≠ 339 / 312 interchangeable：** 官方把这道门写成对付拜占庭不守 CheckTx 的机制，不是 CheckTx 自己。
- **点名了这道门 not already is-finalize ≠ 已经是 Finalize interchangeable：** 官方把点名 ProcessProposal 和已经是 Finalize 分开。
- **会拒提案 not already pool-done ≠ 已经在池子里挡完 interchangeable：** 官方把会拒提案和已经在池子里挡完分开；339 checktxweak vs process bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 有 ProcessProposal | 不是 already is-checktx | 不是 CheckTxState 已经是 ExecuteTxState alone（312） |
| 点名了这道门 | 不是 already is-finalize | 不是不该验排序就已经该在 CheckTx 里验 alone（770） |
| 会拒提案 | 不是 already pool-done | 不是拜占庭已经被池子挡住 alone（771） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal 对付这种行为不是已经是 CheckTx not already is-checktx / not already is-finalize / not already pool-done 正式三事（339 余量），必须分开有 ProcessProposal 是不是 already is-checktx interchangeable / 339 checktxweak bundled interchangeable / checktxweak-sold-as-consensus interchangeable、点名了这道门 是不是 already is-finalize interchangeable、会拒提案 是不是 already pool-done interchangeable。可以跳过「看见有 ProcessProposal 就已经是 CheckTx interchangeable / 就已经是 Finalize interchangeable / 就已经在池子里挡完 interchangeable」。不要把「不验排序」当不确定已经验完。不要另写怎样写 CheckTx 或怎样写 ProcessProposal。339 checktxweak vs process bundled unbundling 在本页 item 3 完成（770 + 771 + 772）。

## 本页不抄

- 怎样写 `CheckTx`、怎样挑哪些检查留给 Process、怎样写 `ProcessProposal`。
- CheckTx 弱过滤器 bundled。那是不变量 339。
- 不该验排序相关有效性不是已经该在 CheckTx 里验。那是不变量 339 item 1 余量 / 770。
- 拜占庭能提案一满块无效交易不是已经被池子挡住。那是不变量 339 item 2 余量 / 771。
- CheckTxState 已经是 ExecuteTxState。那是不变量 312。
- 四门已经结算。那是不变量 33。
- 索引器已经保证不重放。那是不变量 313。
