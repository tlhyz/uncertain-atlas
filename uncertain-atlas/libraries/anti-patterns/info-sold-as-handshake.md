# 反模式：看见 Info 用来握手对齐就当成已经是快照重放 / 看见 app_version 进每块头就当成已经印进本头 AppHash / 看见 last_block_app_hash / last_block_height 要在 Commit 里落盘就当成已经交差

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[Info 用来握手对齐 ≠ 已经是快照重放](../../tracks/implementation/worked-example-info-vs-handshake.md)。

## 塌法

1. 看见 Info 用来在启动或恢复时让引擎和应用握手对齐 / 看见能回，就当成已经是快照重放，或当成已经是 QueryState。
2. 看见回的 `app_version` 会写进每一块的头 / 看见有版本，就当成已经印进本头 AppHash，或当成已经交差。
3. 看见引擎指望 `last_block_app_hash` 和 `last_block_height` 在 `Commit` 里更新并落盘 / 看见回了这两列，就当成已经交差，或当成已经在剪。

## 为什么会出事

官方写：Info 用来回报应用状态。启动或恢复时，CometBFT 用这次握手和应用对齐。回的 `app_version` 会写进每一块的 Header。CometBFT 指望 `last_block_app_hash` 和 `last_block_height` 在 `Commit` 里更新并落盘。

## 和相邻反模式

- [infousage-sold-as-handshakebundled](infousage-sold-as-handshakebundled.md) 是 Info Usage 正式三事就等于 QueryState / bundled handshake / 已经 persist，不是本页 Info 握手 bundled 三事。
- [infousage-persist-sold-as-committed](infousage-persist-sold-as-committed.md) 是 Info Usage last_block persisted during Commit / lane_priorities 正式三事 part 2，不是本页 Info 握手 bundled 三事。
- [querystate-sold-as-execute](querystate-sold-as-execute.md) 是 QueryState 就已经是 ExecuteTxState，不是本页这种 Info 用来握手对齐不是已经是快照重放。
- [apphash-sold-as-this-block](apphash-sold-as-this-block.md) 是本头 AppHash 就已经是本高度交差，不是本页这种 app_version 进每块头不是已经印进本头 AppHash。
- [crashsteps-sold-as-committed](crashsteps-sold-as-committed.md) 是崩溃三步就已经 Commit，不是本页这种 last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差。
