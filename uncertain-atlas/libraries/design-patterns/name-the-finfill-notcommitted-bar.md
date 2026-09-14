# 模式：把 FinalizeBlock fill all fields not request complete means committed 正式三事（473 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlock fill all fields not request complete means committed ≠ bundled（473）](../../tracks/implementation/worked-example-finfill-notcommitted-vs-bundled.md)。

## 三个名字

1. **fill all fields not request complete means committed 不是 FinalizeBlock fill all fields even if Prepare/Process passed bundled：** 看见 request complete 不是已经交差，不是 473 finfill interchangeable / 583 refill not request complete means committed interchangeable / 567 not no need to provide again interchangeable。
2. **fill all fields not request complete means committed 不是 finfields / finpersist bundled：** 看见 all fields 填齐 不是已经 newly decided block fields / persist decision，不是 407 finfields interchangeable / 335 finpersist interchangeable / 576 fincand committed interchangeable。
3. **fill all fields not request complete means committed 不是 apply candidate / 583 refill：** 看见又填一遍 不是已经套用先前候选 / previously executed，不是 584 apply candidate interchangeable / 583 not refill interchangeable / 568 not passed means ran Process interchangeable。

## 为什么要分开叫

官方把 all fields / request complete 写成三个名字。把它们叫成一个「看见请求齐了就已经 committed interchangeable / 已经 finfields interchangeable / 已经 apply candidate interchangeable」，会把 not request complete means committed、not finfields / finpersist、not apply candidate / refill 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields not request complete means committed 正式三事（473 余量），先数清问的是 request complete 是不是 already committed、request complete 是不是 already finfields / finpersist、request complete 是不是 already apply candidate / refill，再决定要不要同一次发布。
