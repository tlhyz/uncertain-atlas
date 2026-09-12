# 反模式：看见 Info 回包 data 是任意信息就当成已经是握手对齐 / 看见 Info 回包 version 是应用软件语义版本就当成已经是 app_version / 看见 Query 回包 codespace 是码的命名空间就当成已经是 CheckTx 码空间

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Response / Query Response。  
**例**：[Info 回包 data 是任意信息 ≠ 已经是握手对齐](../../tracks/implementation/worked-example-infodata-vs-appversion.md)。

## 塌法

1. 看见 Info 回包 `data` 是任意信息 / 看见回了 data，就当成已经是握手对齐，或当成已经是快照重放。
2. 看见 Info 回包 `version` 是应用软件语义版本 / 看见回了应用版本，就当成已经是 `app_version`，或当成已经印进本头 AppHash。
3. 看见 Query 回包 `codespace` 是码的命名空间 / 看见写了空间，就当成已经是 CheckTx 码空间，或当成已经是回包码。

## 为什么会出事

官方写：`data` 是一些任意信息。`version` 是应用软件的语义版本。Query 回包 `codespace` 是这个 `code` 的命名空间。

## 和相邻反模式

- [info-sold-as-handshake](info-sold-as-handshake.md) 是 Info 用来握手对齐就已经是快照重放，不是本页这种 Info 回包 data 是任意信息不是已经是握手对齐。
- [infover-sold-as-appversion](infover-sold-as-appversion.md) 是 Info 请求 version 就已经是 app_version，不是本页这种 Info 回包 version 是应用软件语义版本不是已经是 app_version。
- [checktxspace-sold-as-code](checktxspace-sold-as-code.md) 是 CheckTx 回包 codespace 就已经是回包码，不是本页这种 Query 回包 codespace 是码的命名空间不是已经是 CheckTx 码空间。
