# 反模式：把 FinalizeBlock When AppHash tx outputs ResultHash persist 正式三事说成已经印进本头

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[Application returns AppHash + tx outputs ≠ 已经印进本头](../../tracks/implementation/worked-example-finreturn-vs-header.md)。

## 错在哪里

把 Application calculates and returns AppHash along with tx outputs 写成已经印进本头，或已经是本头 AppHash；把 CometBFT hashes transaction outputs into ResultHash 写成已经 Code / Data 印进本头 LastResultsHash，或已经印进本头；把 CometBFT persists tx outputs / AppHash / ResultsHash 写成已经交差，或已经 Commit 落盘应用状态，或已经和 362 / 403 / 404 / 316 / 147 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When AppHash tx outputs ResultHash persist 正式三事，必须分开 Application returns AppHash + tx outputs、CometBFT hashes into ResultHash、CometBFT persists 这三份三件事，不要和 362 / 403 / 404 / 316 / 147 糊成一句。
