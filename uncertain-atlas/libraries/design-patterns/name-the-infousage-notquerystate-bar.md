# 模式：把 Info Usage Return information about application state not QueryState / not Info response data arbitrary info / not handshake sync already persisted 正式三事（494 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[Info Usage Return information about application state not QueryState ≠ bundled（494）](../../tracks/implementation/worked-example-infousage-notquerystate-vs-bundled.md)。

## 三个名字

1. **Return information about application state 不是 QueryState：** 看见 Return information about the application state，不是已经 QueryState 就已经是 ExecuteTxState interchangeable，不是 314 querystate interchangeable / 371 queryheight interchangeable / 494 infousage-vs-handshakebundled interchangeable / 668 infousage-notquerystate interchangeable。

2. **回报应用状态 不是 Info response data 任意信息：** 看见 return information about application state，不是已经 Info 回包 data 是任意信息 interchangeable，不是 389 info-lane-fields interchangeable / 379 info-req-version interchangeable / 370 info-handshake bundled interchangeable / 494 infousage item 3 app_version interchangeable。

3. **能回 Info 不是 handshake sync 就已经 persisted：** 看见能回 Info，不是已经 Used to sync during handshake on startup or on recovery 就等于已经 persisted interchangeable，不是 370 info-handshake bundled interchangeable / 320 crash recovery interchangeable / 665 infousage-notcommitpersist interchangeable / 497 infousage-persist item 1 interchangeable。

官方把 Info Usage Return state 单句、QueryState vs ExecuteTxState（314）、Info Response data 栏（389）、handshake sync = persisted 路径写成三个名字。把它们叫成一个「看见 Return information about application state 就已经 QueryState interchangeable / 就已经 Info data 栏 interchangeable / 就已经 handshake sync 交差 interchangeable」，会把 not QueryState、not Info response data arbitrary info、not handshake sync already persisted 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage Return information about application state not QueryState / not Info response data arbitrary info / not handshake sync already persisted 正式三事（494 余量），先数清问的是 Return state 是不是 QueryState / 314 / 371，是不是回报应用状态 是不是 Info data 栏 / 389 / 379，还是能回 Info 是不是 handshake sync already persisted / 370 / 320 / 665，再决定要不要同一次发布。494 infousage vs handshake bundled unbundling 在本页 item 1 启动。
