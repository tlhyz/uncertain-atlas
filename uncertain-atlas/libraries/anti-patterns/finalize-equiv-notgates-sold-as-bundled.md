# 反模式：把 Finalize 等价于 ABCI 1.0 那三步 not already four gates / not already settled / not already no Prepare-Process 正式三事（363 余量） 卖成 已经是四门已经结算 / 已经交差 / 已经没有 Prepare / Process

**层次**：实现 / Finalize 回包义务。  
**分类**：建议（产品）。  
**对应例**：[worked-example-finalize-equiv-notgates-vs-bundled.md](../../tracks/implementation/worked-example-finalize-equiv-notgates-vs-bundled.md)。

官方把 Finalize 等价于 ABCI 1.0 那三步 / 可以用 decided_last_commit 和 misbehavior 定奖惩 / 必须回四列三条核心句写成三件独立的实现事。把它们卖成已经是四门已经结算 / 已经交差 / 已经没有 Prepare / Process，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 等价于 ABCI 1.0 那三步 正式三事（363 余量），必须分开 not already four gates、not already settled、not already no Prepare-Process 三件事，不要和 363 / 33 / 403 / ~600 finresp-notgates / 837 / 838 糊成一句。

## 和相邻反模式

- [finresp-notgates 别前缀](../../tracks/implementation/worked-example-finresp-notgates-vs-bundled.md) 是另一前缀的 363 侧钉（~600），不是本页 finalize-equiv-notgates 边界。
- 四门已经结算是不变量 33，不是本页收成一门边界。
