# 反模式：把必须协调升级不是已经只改 VoteExtensionsEnableHeight not already only-veheight / not already single-node / not already field-filled 正式三事（346 余量）说成已经只改 VoteExtensionsEnableHeight / 已经是单节点能切 / 已经做了这次升级

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[必须协调升级 not already only-veheight ≠ bundled（346）](../../tracks/implementation/worked-example-abci20-notonlyveheight-vs-bundled.md)。

## 卖法

把必须协调升级 / 切到带扩展的 CometBFT / 字段已经在参数表里 写成已经只改 `VoteExtensionsEnableHeight` interchangeable / 已经 only-veheight interchangeable / 已经只改字段交差 interchangeable / 346 abci20upgrade bundled interchangeable / abci20upgrade-sold-as-height interchangeable；把一个节点升了二进制 / 单节点升了版本 写成已经是单节点能切 interchangeable / 已经 single-node interchangeable / 已经单节点切完交差 interchangeable；把能改启用高度 / 字段填了 写成已经做了这次升级 interchangeable / 已经 field-filled interchangeable / 已经 field-filled 交差 interchangeable，或已经和 346 abci20upgrade bundled / abci20upgrade-sold-as-height interchangeable / 791 abci20-notonlyveheight interchangeable。

## 为什么错

官方把换二进制的协调升级、不是单节点能切、不是已经做了这次升级写成三件独立的实现事。把它们卖成 already only-veheight interchangeable / already single-node interchangeable / already field-filled interchangeable，会把 not already only-veheight、not already single-node、not already field-filled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看必须协调升级不是已经只改 VoteExtensionsEnableHeight not already only-veheight / not already single-node / not already field-filled 正式三事（346 余量），必须分开 not already only-veheight、not already single-node、not already field-filled 三件事，不要和 346 / 330 / 58 / 792 / 793 糊成一句。

## 和相邻反模式

- [abci20upgrade-sold-as-height](abci20upgrade-sold-as-height.md) 是 ABCI 2.0 协调升级 bundled 全段，不是本页必须协调升级 item 1 单句边界。
- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是到了 H 不是已经 Prepare 带了扩展（330），不是本页只改字段边界。
- [enable-height-sold-as-safe](enable-height-sold-as-safe.md) 是治理改 enable-height 会 panic（58），不是本页单节点能切边界。
