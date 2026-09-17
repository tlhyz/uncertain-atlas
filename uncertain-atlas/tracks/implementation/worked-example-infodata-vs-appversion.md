# 例：看见 Info 回包 data 是任意信息不是已经是握手对齐；看见 Info 回包 version 是应用软件语义版本不是已经是 app_version；看见 Query 回包 codespace 是码的命名空间不是已经是 CheckTx 码空间

**层次**：实现 / Info 回包余栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Response / Query Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Info 回包 data 是任意信息不是已经是握手对齐 / Info 回包 version 是应用软件语义版本不是已经是 app_version / Query 回包 codespace 是码的命名空间不是已经是 CheckTx 码空间」，不是 Info 用来握手对齐就已经是快照重放，也不是 Info 请求 version 就已经是 app_version。不要另写怎样写 Info 回包余栏。

## 官方三件事

规范把 Info 回包 `data` 是任意信息、`version` 是应用软件语义版本、Query 回包 `codespace` 是码的命名空间写成三件独立的实现事，不是「看见回了 Info 余栏就已经是握手对齐、已经是 app_version、已经是 CheckTx 码空间」一件事：

1. **看见 Info 回包 `data` 是任意信息 / 看见回了 data 不是已经是握手对齐，也不是已经是快照重放。**  
   官方写：`data` 是一些任意信息。看见回了 data，不是已经握手对齐。看见有任意字段，不是已经是快照重放。看见能填，不是已经交差。
2. **看见 Info 回包 `version` 是应用软件语义版本 / 看见回了应用版本 不是已经是 app_version，也不是已经印进本头 AppHash。**  
   官方写：`version` 是应用软件的语义版本。看见回了应用版本，不是已经是回包里的 `app_version`。看见有语义版本，不是已经印进每块头。看见能回，不是已经交差。
3. **看见 Query 回包 `codespace` 是码的命名空间 / 看见写了空间 不是已经是 CheckTx 码空间，也不是已经是回包码。**  
   官方写：`codespace` 是这个 `code` 的命名空间。看见写了空间，不是已经是 CheckTx 回包那份码空间。看见有命名空间，不是已经是 Query 回包码本身。看见能回，不是已经交差。

怎样写 Info 回包余栏、怎样填任意信息、怎样填应用版本是规范里的做法，本页不抄。Info 用来握手对齐就已经是快照重放是不变量 370，本页不抄。

## 官方为什么这样拆

- **Info 回包 data 是任意信息 ≠ 已经是握手对齐：** 官方把回包里的任意信息和握手对齐分开。
- **Info 回包 version 是应用软件语义版本 ≠ 已经是 app_version：** 官方把应用软件语义版本和会进每块头的 app_version 分开。
- **Query 回包 codespace 是码的命名空间 ≠ 已经是 CheckTx 码空间：** 官方把 Query 这份码空间和 CheckTx 那份码空间分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Info 回包 data 是任意信息 | 不是已经是握手对齐 | 不是 Info 用来握手对齐就已经是快照重放（370） |
| Info 回包 version 是应用软件语义版本 | 不是已经是 app_version | 不是 Info 请求 version 就已经是 app_version（379） |
| Query 回包 codespace 是码的命名空间 | 不是已经是 CheckTx 码空间 | 不是 CheckTx 回包 codespace 就已经是回包码（381） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 Info 余栏就已经是握手对齐、已经是 app_version、已经是 CheckTx 码空间」，必须分开 Info 回包 data 是任意信息是不是已经是握手对齐、Info 回包 version 是应用软件语义版本是不是已经是 app_version、Query 回包 codespace 是码的命名空间是不是已经是 CheckTx 码空间。可以跳过「看见回了 Info 余栏就已经是握手对齐」。不要另写怎样写 Info 回包余栏。389 infodata vs appversion bundled unbundling 完成（761 item 1 / 762 item 2 / 763 item 3）；精读 [`worked-example-infodata-nothandshake-vs-bundled.md`](worked-example-infodata-nothandshake-vs-bundled.md)（不变量 761 item 1）。

## 本页不抄

- 怎样写 Info 回包余栏、怎样填任意信息、怎样填应用版本。
- Info 用来握手对齐就已经是快照重放。那是不变量 370。
- Info 请求 version 就已经是 app_version。那是不变量 379。
- CheckTx 回包 codespace 就已经是回包码。那是不变量 381。
