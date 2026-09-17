# 反模式：把 app_version 进头 not already header AppHash / not already this-height settled / not already selected 正式三事（370 余量） 卖成 已经印进本头 AppHash / 已经是本高度交差 / 已经选型

**层次**：实现 / Info 握手。  
**分类**：建议（产品）。  
**对应例**：[worked-example-info-notapphash-vs-bundled.md](../../tracks/implementation/worked-example-info-notapphash-vs-bundled.md)。

官方把 Info 用来握手对齐 / app_version 进每块头 / last_block 要在 Commit 里落盘三条核心句写成三件独立的实现事。把它们卖成已经印进本头 AppHash / 已经是本高度交差 / 已经选型，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 app_version 进头 正式三事（370 余量），必须分开 not already header AppHash、not already this-height settled、not already selected 三件事，不要和 370 / 147 / 379 / 791 / 389 / 762 / 494 / 670 / 815 / 817 糊成一句。

## 和相邻反模式

- [info-notreplay-sold-as-bundled](info-notreplay-sold-as-bundled.md) 是握手对齐单句边界（815 item 1），不是本页 app_version 进头边界。
- [infover-notappver-sold-as-bundled](infover-notappver-sold-as-bundled.md) 是 Info 请求 version 就已经是 app_version（379/791），不是本页 app_version 进头边界。
