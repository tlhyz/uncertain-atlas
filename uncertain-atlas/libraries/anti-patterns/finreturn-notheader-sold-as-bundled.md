# 反模式：把 FinalizeBlock When Application returns AppHash + tx outputs not printed in this header / not this header AppHash 正式三事（587 余量）说成已经印进本头 / 已经是本头 AppHash / 已经 finreturn bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When Application returns AppHash + tx outputs not printed in this header ≠ bundled（587）](../../tracks/implementation/worked-example-finreturn-notheader-vs-bundled.md)。

## 错在哪里

把 Application calculates and returns AppHash along with tx outputs 写成已经印进本头 interchangeable，或已经写入本头 interchangeable；把 Application returns AppHash 写成已经是本头 AppHash interchangeable，或已经本头 AppHash 就代表本高度交差 interchangeable；把 Application returns AppHash + tx outputs 写成已经是 FinalizeBlock When AppHash tx outputs ResultHash persist 正式三事 bundled（587） interchangeable，或已经 finreturn bundled interchangeable，或已经和 CometBFT hashes into ResultHash / CometBFT persists tx outputs / AppHash / ResultsHash / 147 / 404 / 466 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When Application returns AppHash + tx outputs not printed in this header / not this header AppHash 正式三事（587 余量），必须分开 not printed in this header、not this header AppHash、not finreturn bundled 三件事，不要和 587 / 147 / 404 / 615 / 616 糊成一句。

## 和相邻反模式

- [finreturn-sold-as-header](finreturn-sold-as-header.md) 是 587 finreturn bundled 三事专用，不是本页 587 item 1 单句边界。
- [finmerkle-sold-as-header](finmerkle-sold-as-header.md) 是 optional Merkle root / next block Header.AppHash，不是本页 When 第 4 步 returns 单句边界。
- [finapphash-sold-as-header](finapphash-sold-as-header.md) 是 Response app_hash 可以空或硬编码，不是本页 Application returns AppHash + tx outputs 单句边界。
