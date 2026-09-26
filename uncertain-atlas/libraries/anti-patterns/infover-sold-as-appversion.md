# 反模式：看见 Info 请求 version 是 CometBFT 软件语义版本就当成已经是 app_version / 看见 block_version / p2p_version 是引擎块版本和 P2P 版本就当成已经版本也对上 / 看见 abci_version 是 ABCI 语义版本、按 X.X.x 显示就当成已经是握手对齐

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Request。  
**例**：[Info 请求 version 是 CometBFT 软件语义版本 ≠ 已经是 app_version](../../tracks/implementation/worked-example-infover-vs-appversion.md)。

## 塌法

1. 看见 Info 请求 `version` 是 CometBFT 软件语义版本 / 看见填了 `version`，就当成已经是 `app_version`，或当成已经印进本头 AppHash。
2. 看见 `block_version` / `p2p_version` 是引擎块版本和 P2P 版本 / 看见填了两列，就当成已经版本也对上，或当成已经有完整历史。
3. 看见 `abci_version` 是 ABCI 语义版本、按 X.X.x 显示 / 看见写了语义版本，就当成已经是握手对齐，或当成已经排了优先。

## 为什么会出事

官方写：请求里的 `version` 是 CometBFT 软件的语义版本。`block_version` 是 CometBFT 的块版本。`p2p_version` 是 CometBFT 的 P2P 版本。`abci_version` 是 CometBFT 的 ABCI 语义版本。脚注写：语义版本指向 semver；Info 里的语义版本会显示成 X.X.x。

## 和相邻反模式

- [infover-notmatched-sold-as-bundled](infover-notmatched-sold-as-bundled.md) 是 block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上 not already matched / not already history / not already settled 正式三事（379 item 2），不是本页 bundled 全段 alone。
- [infover-notappversion-sold-as-bundled](infover-notappversion-sold-as-bundled.md) 是 Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version not already appversion / not already matched / not already settled 正式三事（379 item 1），不是本页 bundled 全段 alone。
- [info-sold-as-handshake](info-sold-as-handshake.md) 是 Info 用来握手对齐就已经是快照重放，不是本页这种 Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version。
- [snapshotswitch-sold-as-full-history](snapshotswitch-sold-as-full-history.md) 是 Info 的 AppHash 对上就已经是版本也对上，不是本页这种 block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上。
- [lane-sold-as-priority](lane-sold-as-priority.md) 是没定义 lane_priorities 就已经排了优先，不是本页这种 abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐。
