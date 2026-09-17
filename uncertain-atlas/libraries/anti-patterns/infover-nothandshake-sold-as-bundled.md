# 反模式：把 abci_version not already handshake / not already prioritized / not already settled 正式三事（379 余量） 说成已经是握手对齐 / 已经排了优先 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[abci_version ≠ bundled（379）](../../tracks/implementation/worked-example-infover-nothandshake-vs-bundled.md)。

## 卖法

把 Info 请求版本这句写成已经已经是握手对齐 / 已经排了优先 / 已经交差 interchangeable，或已经和 379 infover-vs-appversion bundled / infover-nothandshake-sold-as-bundled interchangeable。

## 为什么错

官方把 Info 请求 version / block_version / p2p_version / abci_version 三条核心句写成三件独立的实现事。把它们卖成已经是握手对齐 / 已经排了优先 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 abci_version 正式三事（379 余量），必须分开 not already handshake、not already prioritized、not already settled 三件事，不要和 379 / 370 / 367 / 791 / 792 糊成一句。

## 和相邻反模式

- [infover-notaligned-sold-as-bundled](infover-notaligned-sold-as-bundled.md) 是 block_version / p2p_version 单句边界（792 item 2），不是本页 abci_version 边界。
- [checktxspace-notlane-sold-as-bundled](checktxspace-notlane-sold-as-bundled.md) 是 CheckTx lane_id 就已经不设道（381/787），不是本页 abci_version 边界。
