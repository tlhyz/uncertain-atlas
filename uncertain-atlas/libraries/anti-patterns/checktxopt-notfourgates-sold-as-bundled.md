# 反模式：把 CheckTx 技术上可选、不参与处理块不是已经是四门已经结算 not already fourgates / not already settled / not already removed 正式三事（373 余量）说成已经是四门已经结算 / 已经交差 / 已经从池里删掉

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[能回 not already fourgates ≠ bundled（373）](../../tracks/implementation/worked-example-checktxopt-notfourgates-vs-bundled.md)。

## 卖法

把能回 / CheckTx 技术上可选、不参与处理块 / 能回 CheckTx 写成已经是四门已经结算 interchangeable / 已经 fourgates interchangeable / 已经是四门已经结算交差 interchangeable / 373 checktxopt bundled interchangeable / checktxopt-sold-as-block interchangeable；把可选 / 技术上可选 / CheckTx 可选 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable；把没参与处理块 / 不参与处理块 / 没处理块 写成已经从池里删掉 interchangeable / 已经 removed interchangeable / 已经从池里删掉交差 interchangeable，或已经和 373 checktxopt bundled / checktxopt-sold-as-block interchangeable / 866 checktxopt-notfourgates interchangeable。

## 为什么错

官方把能回、不是已经交差、不是已经从池里删掉写成三件独立的实现事。把它们卖成 already fourgates interchangeable / already settled interchangeable / already removed interchangeable，会把 not already fourgates、not already settled、not already removed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 技术上可选、不参与处理块不是已经是四门已经结算 not already fourgates / not already settled / not already removed 正式三事（373 余量），必须分开 not already fourgates、not already settled、not already removed 三件事，不要和 373 / 33 / 301 / 316 糊成一句。

## 和相邻反模式

- [checktxopt-sold-as-block](checktxopt-sold-as-block.md) 是 checktxopt bundled 全段，不是本页能回 item 1 单句边界。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页 not already fourgates 单句。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是 Finalize 的 Code 非零就已经没进块（316），不是本页 not already settled 边界。
- [proposed-sold-as-removed](proposed-sold-as-removed.md) 是提案收了就已经从池里删掉（301），不是本页 not already removed 单句。
