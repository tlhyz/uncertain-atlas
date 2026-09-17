# 例：看见 app_version 进每块头 is not already header AppHash interchangeable / not already this-height settled interchangeable / not already selected interchangeable

**层次**：实现 / app_version 进头 not already header AppHash / not already this-height settled / not already selected 正式三事（370 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「app_version 进头 not already header AppHash / not already this-height settled / not already selected 正式三事（370 余量）/ not 816 info-notapphash interchangeable / not 370 info-vs-handshake bundled interchangeable」，不是 Info 握手 bundled（370），也不是本头 AppHash 就已经是本高度交差（147），也不是 Info 请求 version 就已经是 app_version（379/791），也不是 Info 回包 version 就已经是 app_version（389/762），也不是 Info Usage app_version 就已经印进本头（494/670）。不要另写怎样写 Info 握手。

## 官方三件事

1. **看见回的 `app_version` 会写进每一块的头 / 看见有版本 / 这份版本 is not already 已经印进本头 AppHash interchangeable / 147 apphash interchangeable，也不是已经 Info 握手 bundled（370） interchangeable / 816 info-notapphash interchangeable / 815 info-notreplay interchangeable / 370 info item 1 握手 interchangeable，也不是已经 app_version 进头 not already header AppHash / not already this-height settled / not already selected 正式三事 bundled（370 item 2 余量） interchangeable / 370 info item 2 interchangeable。**  
   官方写：回的 `app_version` 会写进每一块的 Header。看见有版本，不是已经印进本头 AppHash interchangeable——本页从 370 item 2 侧钉 not already header AppHash 单句。370 info vs handshake bundled unbundling 在本页 item 2 续。

2. **看见有版本 / 看见进了头 / 这份版本 is not already 已经是本高度交差 interchangeable / 147 apphash interchangeable，也不是已经 Info 握手 bundled（370） interchangeable / 816 info-notapphash interchangeable / 370 info item 3 last_block interchangeable / 817 info-notpersist interchangeable，也不是已经 Info 请求 version 就已经是 app_version interchangeable / 379 infover / 791 infover-notappver interchangeable，也不是已经 Info 回包 version 就已经是 app_version interchangeable / 389 infodata / 762 infodata-notappversion interchangeable。**  
   官方把进了头和已经是本高度交差分开——370 bundled 第二件事常与 147 / 379 / 389 混成「看见有版本就已经印进本头 AppHash 或已经交差 interchangeable」，本页钉 not already this-height settled 单句。

3. **看见有版本 / 看见字段在 / 这份版本 is not already 已经选型 interchangeable，也不是已经 Info 握手 bundled（370） interchangeable / 816 info-notapphash interchangeable / 815 info-notreplay interchangeable，也不是已经 Info Usage app_version 就已经印进本头 interchangeable / 494 infousage / 670 infousage-notappversion interchangeable。**  
   官方把字段在和已经选型分开。看见字段在，不是已经选型 interchangeable。370 info vs handshake bundled unbundling 在本页 item 2 续。

怎样写 Info 回包、怎样对版本、怎样落盘是规范里的做法，本页不抄。

## 官方为什么这样拆

- **app_version 进头 not already header AppHash ≠ 147 interchangeable：** 官方把版本进头和本头 AppHash 分开。
- **看见进了头 not already this-height settled ≠ 已经是本高度交差 interchangeable：** 官方把进了头和已经是本高度交差分开。
- **看见字段在 not already selected ≠ 已经选型 interchangeable：** 官方把字段在和已经选型分开；370 info vs handshake bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| app_version 进每块头 | 不是已经印进本头 AppHash（147） | 不是握手对齐（815/370 item 1） |
| 看见进了头 | 不是已经是本高度交差 | 不是 Info 请求 version（379/791） |
| 看见字段在 | 不是已经选型 | 不是 Info Usage app_version（494/670） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 app_version 进头 not already header AppHash / not already this-height settled / not already selected 正式三事（370 余量），必须分开是不是已经印进本头 AppHash interchangeable / 147、是不是已经是本高度交差、是不是已经选型。可以跳过「看见有版本就已经印进本头 AppHash」。不要另写怎样写 Info 握手。370 info vs handshake bundled unbundling 在本页 item 2 续；续 [`worked-example-info-notpersist-vs-bundled.md`](worked-example-info-notpersist-vs-bundled.md)（不变量 817 item 3）。

## 本页不抄

- 怎样写 Info 回包、怎样对版本、怎样落盘。
- Info 握手 bundled。那是不变量 370。
- 握手对齐。那是不变量 370 item 1 余量 / 815。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
- Info 请求 version 就已经是 app_version。那是不变量 379 / 791。
