# 反模式：把 block_version / p2p_version not already versions aligned / not already full history / not already settled 正式三事（379 余量） 说成已经版本也对上 / 已经有完整历史 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[block_version ≠ bundled（379）](../../tracks/implementation/worked-example-infover-notaligned-vs-bundled.md)。

## 卖法

把 Info 请求版本这句写成已经已经版本也对上 / 已经有完整历史 / 已经交差 interchangeable，或已经和 379 infover-vs-appversion bundled / infover-notaligned-sold-as-bundled interchangeable。

## 为什么错

官方把 Info 请求 version / block_version / p2p_version / abci_version 三条核心句写成三件独立的实现事。把它们卖成已经版本也对上 / 已经有完整历史 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 block_version / p2p_version 正式三事（379 余量），必须分开 not already versions aligned、not already full history、not already settled 三件事，不要和 379 / 323 / 382 / 782 / 791 / 793 糊成一句。

## 和相邻反模式

- [infover-notappver-sold-as-bundled](infover-notappver-sold-as-bundled.md) 是 Info 请求 version 单句边界（791 item 1），不是本页两列边界。
- [syncingheight-nothistory-sold-as-bundled](syncingheight-nothistory-sold-as-bundled.md) 是 syncing_to_height 就已经有完整历史（382/782），不是本页引擎版本边界。
