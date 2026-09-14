# 模式：把 FinalizeBlock fill all fields not decided/proposed interchangeable 正式三事（473 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Request。  
**例**：[FinalizeBlock fill all fields not decided/proposed interchangeable ≠ bundled（473）](../../tracks/implementation/worked-example-finfill-notdecprop-vs-bundled.md)。

## 三个名字

1. **all fields not decided/proposed interchangeable 不是 FinalizeBlock fill all fields even if Prepare/Process passed bundled：** 看见又填一遍不是已经 decided_last_commit 和 proposed_last_commit 就可以混用，不是 473 bundled interchangeable / 422 decided vs proposed interchangeable / 557 461 余量 interchangeable。
2. **all fields not Prepare/Process passed means decided/proposed interchangeable 不是 359 Prepare 同一套：** 看见 all fields 不是已经 Prepare/Process 传过就意味着 decided 和 proposed interchangeable，不是 473 bundled interchangeable / 359 Prepare 同一套字段 interchangeable / 568 even if passed interchangeable。
3. **all fields not Finalize 专有栏 same as Prepare/Process interchangeable 不是 360 Process guarantee field refill：** 看见 syncing_to_height 等 Finalize 专有栏不是已经和 Prepare/Process 同一套字段名对上就够，不是 473 bundled interchangeable / 360 Process guarantee field refill interchangeable / 428 Finalize 请求余栏 interchangeable。

## 为什么要分开叫

官方把 FinalizeBlock fill all fields not decided/proposed interchangeable 写成三个名字。把它们叫成一个「看见 all fields / 又填一遍 就已经 decided 和 proposed 就可以混用 interchangeable / Prepare/Process 传过 interchangeable」，会把 not decided/proposed、not Prepare/Process passed means decided/proposed、not Finalize 专有栏 same as Prepare/Process 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields not decided/proposed interchangeable 正式三事（473 余量），先数清问的是 all fields 是不是 decided/proposed interchangeable、all fields 是不是 Prepare/Process passed means decided/proposed interchangeable、all fields 是不是 Finalize 专有栏 same as Prepare/Process interchangeable，再决定要不要同一次发布。
