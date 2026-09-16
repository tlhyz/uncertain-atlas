# 模式：把 FinalizeBlock When optionally re-checks not must recheck / not already settled / not finrecheck bundled 正式三事（591 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 9。  
**例**：[FinalizeBlock When optionally re-checks not must recheck ≠ bundled（591）](../../tracks/implementation/worked-example-finrecheck-notmust-vs-bundled.md)。

## 三个名字

1. **optionally re-checks 不是必须再验：** 看见 When 第 9 步 optional / optionally, re-checks，不是已经必须再验才能开下一高 interchangeable，不是 312 checktxtype RECHECK interchangeable / 484 chktxtype RECHECK interchangeable / 634 notrecheck interchangeable。
2. **optionally re-checks 不是已经交差：** 看见 When 第 9 步 optional recheck，不是已经 Finalize + Commit 交差 interchangeable，不是 33 four gates interchangeable / 335 finpersist interchangeable / 403 finafter interchangeable / 632 notsettled interchangeable。
3. **optionally re-checks 不是 finrecheck bundled：** 看见 When 第 9 步 optional recheck，不是已经 finrecheck bundled interchangeable，不是 636 notoutstanding interchangeable / 637 nottype interchangeable / 591 finrecheck item 2 outstanding vs new interchangeable / 591 finrecheck item 3 not Type=RECHECK interchangeable。

## 为什么要分开叫

官方把 When 第 9 步 optionally re-checks、必须再验 / Recheck type、交差 / 四门已经结算、591 finrecheck bundled 三事 写成三个名字。把它们叫成一个「看见 When 第 9 步再验了 就已经必须再验 interchangeable、就已经交差 interchangeable、就已经 finrecheck bundled interchangeable」，会把 not must recheck、not already settled、not finrecheck bundled / not 591 item 2 / item 3 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When optionally re-checks not must recheck / not already settled / not finrecheck bundled 正式三事（591 余量），先数清问的是 optionally re-checks 是不是 already must recheck / 312 / 484 / 634，是不是 already settled / 33 / 335 / 403，还是 optionally re-checks 是不是 already finrecheck bundled / 636 / 637，再决定要不要同一次发布。591 finrecheck unbundling 在本页 item 1 启动。
