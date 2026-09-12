# 模式：把 Info 请求版本三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Request。  
**例**：[Info 请求 version 是 CometBFT 软件语义版本 ≠ 已经是 app_version](../../tracks/implementation/worked-example-infover-vs-appversion.md)。

## 三个名字

1. **Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version：** 看见填了 version 不是已经印进本头 AppHash。
2. **block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上：** 看见填了两列不是已经有完整历史。
3. **abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐：** 看见写了语义版本不是已经排了优先。

## 为什么要分开叫

官方把 Info 请求 `version` 是 CometBFT 软件语义版本、`block_version` / `p2p_version` 是引擎块版本和 P2P 版本、`abci_version` 是 ABCI 语义版本写成三件事。把它们叫成一个「看见 Info 请求带了版本就已经是 app_version」，会把握手、快照切共识和车道一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Info 请求带了版本就已经是 app_version」，先数清问的是 Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version、block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上，还是 abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐，再决定要不要同一次发布。
