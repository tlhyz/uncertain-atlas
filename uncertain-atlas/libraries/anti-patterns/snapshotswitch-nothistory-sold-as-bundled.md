# 反模式：把切进共识不是已经有完整历史 not already full-history / not already genesis-replay / not already no-extension-care 正式三事（323 余量）说成已经有完整历史 / 已经从创世重放 / 已经不用管扩展高度

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[能出块 not already full-history ≠ bundled（323）](../../tracks/implementation/worked-example-snapshotswitch-nothistory-vs-bundled.md)。

## 卖法

把能出块 / 切进共识 / 能给新高度 写成已经有从创世的完整历史 interchangeable / 已经 full-history interchangeable / 已经能给任意旧高度 interchangeable / 323 snapshotswitch bundled interchangeable / 33 four gates interchangeable / snapshotswitch-sold-as-full-history interchangeable；把和其他节点一样跑 / 切过去之后一样跑 / 能出块之后 写成已经从创世重放 interchangeable / 已经 genesis-replay interchangeable；把透明 / 对应用透明 / 操作透明 写成已经不用管扩展高度 interchangeable / 已经 no-extension-care interchangeable，或已经和 323 snapshotswitch bundled / snapshotswitch-sold-as-full-history interchangeable / 727 snapshotswitch-nothistory interchangeable。

## 为什么错

官方把能出块单句、already full-history、already genesis-replay、already no-extension-care 写成三件独立的实现事。把它们卖成 already full-history interchangeable / already genesis-replay interchangeable / already no-extension-care interchangeable，会把 not already full-history、not already genesis-replay、not already no-extension-care 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看切进共识不是已经有完整历史 not already full-history / not already genesis-replay / not already no-extension-care 正式三事（323 余量），必须分开 not already full-history、not already genesis-replay、not already no-extension-care 三件事，不要和 323 / 33 / 725 / 726 / 321 / 38 / 314 糊成一句。

## 和相邻反模式

- [snapshotswitch-sold-as-full-history](snapshotswitch-sold-as-full-history.md) 是 Transition to Consensus bundled 全段，不是本页切进共识 item 3 单句边界。
- [snapshotswitch-notversion-sold-as-bundled](snapshotswitch-notversion-sold-as-bundled.md) 是 AppHash 对上 item 2，不是本页历史截断边界。
- [snapshotswitch-notchainid-sold-as-bundled](snapshotswitch-notchainid-sold-as-bundled.md) 是装完 item 1，不是本页切进共识边界。
