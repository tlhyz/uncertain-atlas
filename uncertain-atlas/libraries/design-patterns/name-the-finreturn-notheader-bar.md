# 模式：把 FinalizeBlock When Application returns AppHash + tx outputs not printed in this header / not this header AppHash 正式三事（587 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 4。  
**例**：[FinalizeBlock When Application returns AppHash + tx outputs not printed in this header ≠ bundled（587）](../../tracks/implementation/worked-example-finreturn-notheader-vs-bundled.md)。

## 三个名字

1. **Application returns AppHash + tx outputs 不是印进本头：** 看见 calculates and returns 不是已经印进本头 interchangeable，不是 404 finapphash interchangeable / 475 finmerkle interchangeable / 432 finrespend interchangeable。
2. **Application returns AppHash + tx outputs 不是本头 AppHash：** 看见 Application returns AppHash 不是已经是本头 AppHash interchangeable，不是 147 apphash vs this block interchangeable / 335 finpersist interchangeable / 362 finwhen interchangeable。
3. **Application returns AppHash + tx outputs 不是 finreturn bundled：** 看见 Application returns AppHash + tx outputs 不是已经 finreturn bundled interchangeable，不是 615 notresulthash interchangeable / 616 notpersist interchangeable / 587 finreturn item 2 hashes into ResultHash interchangeable / 587 finreturn item 3 persists interchangeable。

## 为什么要分开叫

官方把 When 第 4 步 Application returns AppHash + tx outputs、第 5 步 hashes into ResultHash、第 6 步 persists 这三份写成三个名字。把它们叫成一个「看见 Application returns AppHash + tx outputs 就已经印进本头 interchangeable、就已经是本头 AppHash interchangeable、就已经 finreturn bundled interchangeable」，会把 not printed in this header、not this header AppHash、not finreturn bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When Application returns AppHash + tx outputs not printed in this header / not this header AppHash 正式三事（587 余量），先数清问的是 Application returns 是不是 already 印进本头 / 404 / 475，是不是 already 本头 AppHash / 147 / 335，还是 Application returns 是不是 already finreturn bundled / 615 / 616，再决定要不要同一次发布。
