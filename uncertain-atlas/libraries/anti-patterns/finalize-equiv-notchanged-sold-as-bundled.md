# 反模式：把 必须回四列 not already changed set / not already settled / not already header AppHash 正式三事（363 余量） 卖成 已经改了集合 / 已经交差 / 已经印进本头

**层次**：实现 / Finalize 回包义务。  
**分类**：建议（产品）。  
**对应例**：[worked-example-finalize-equiv-notchanged-vs-bundled.md](../../tracks/implementation/worked-example-finalize-equiv-notchanged-vs-bundled.md)。

官方把 Finalize 等价于 ABCI 1.0 那三步 / 可以用 decided_last_commit 和 misbehavior 定奖惩 / 必须回四列三条核心句写成三件独立的实现事。把它们卖成已经改了集合 / 已经交差 / 已经印进本头，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看必须回四列 正式三事（363 余量），必须分开 not already changed set、not already settled、not already header AppHash 三件事，不要和 363 / 364 / 835 / 147 / 318 / 836 / 837 糊成一句。

## 和相邻反模式

- [finalize-equiv-notslashed-sold-as-bundled](finalize-equiv-notslashed-sold-as-bundled.md) 是定奖惩单句边界（837 item 2），不是本页必须回四列边界。
- [validator-notchanged-sold-as-bundled](validator-notchanged-sold-as-bundled.md) 是 ValidatorUpdate 就已经改了集合（364/835），不是本页必须回四列边界。
