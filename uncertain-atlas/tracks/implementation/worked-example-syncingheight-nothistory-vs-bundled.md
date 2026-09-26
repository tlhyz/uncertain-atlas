# 例：看见填了目标 / 看见在同步 / 看见等于本高 is not already already history interchangeable / already restored interchangeable / already settled interchangeable

**层次**：实现 / syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史 not already history / not already restored / not already settled 正式三事（382 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史 not already history / not already restored / not already settled 正式三事（382 余量）/ not 893 syncingheight-nothistory interchangeable / not 382 syncingheight bundled interchangeable」，不是 syncingheight bundled（382），也不是 validator_updates 空则引擎保持当前集合不是已经没有集合（382 item 2 余量）或 Finalize 回包 events 标成非确定不是已经必须确定（382 item 3 余量）。不要另写怎样写 Finalize 请求回包。

## 官方三件事

规范把 Methods 里 syncing_to_height 同步或重放时是目标高、否则等于本高 和「已经是填了目标就已经有完整历史 interchangeable / 已经是在同步就已经是快照重放 interchangeable / 已经是等于本高就已经交差 interchangeable / 已经是 syncingheight bundled interchangeable」分开写成三件独立的实现事，不是「看见填了目标就已经有完整历史 interchangeable / 就已经是快照重放 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见填了目标 / 看见 syncing_to_height 同步或重放时是目标高、否则等于本高 / 看见填了 syncing_to_height is not already 已经有完整历史 interchangeable / 已经 history interchangeable / 已经有从创世的完整历史交差 interchangeable / 382 syncingheight bundled interchangeable / 323 transition interchangeable / syncingheight-sold-as-history interchangeable，也不是已经 syncingheight bundled（382） interchangeable / 893 syncingheight-nothistory interchangeable / 382 syncingheight item 1 interchangeable，也不是已经 syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史 not already history / not already restored / not already settled 正式三事 bundled（382 item 1 余量） interchangeable / 382 syncingheight item 1 interchangeable，也不是已经空着就已经没有集合（382 item 2） interchangeable / 回了事件就已经必须确定（382 item 3） interchangeable / 323 transition interchangeable，也不是已经切进共识就已经有从创世的完整历史（323） interchangeable。**  
   官方写：节点在同步或重放块时，`syncing_to_height` 等于目标高度。否则 `syncing_to_height` 等于本高。看见填了目标，不是已经有从创世的完整历史。看见填了目标，不是已经 history interchangeable——382 钉 bundled 三事，本页从 item 1 侧钉 not already history 单句。看见 syncing_to_height 同步或重放时是目标高、否则等于本高，不是已经 syncingheight bundled（382） interchangeable——382 钉 bundled，本页钉 item 1 第一件事。看见填了 syncing_to_height，不是已经切进共识就已经有从创世的完整历史（323） interchangeable——323 另钉。382 syncingheight-vs-history bundled unbundling 在本页 item 1 启动。

2. **看见在同步 / 看见在同步或重放 / 看见正在追目标高 is not already 已经是快照重放 interchangeable / 已经 restored interchangeable / 已经是快照重放交差 interchangeable / 382 syncingheight bundled interchangeable / 321 offerrestored interchangeable，也不是已经 syncingheight bundled（382） interchangeable / 893 syncingheight-nothistory interchangeable / 382 syncingheight item 2 空着 interchangeable / 382 syncingheight item 3 回了事件 interchangeable，也不是已经 syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史 not already history / not already restored / not already settled 正式三事 bundled（382 item 1 余量） interchangeable / 382 syncingheight item 1 interchangeable，也不是已经有完整历史（本页第一件事） interchangeable。**  
   官方写：看见在同步，不是已经是快照重放。看见在同步或重放，不是已经 restored interchangeable——本页钉 not already restored 单句。看见正在追目标高，不是已经有完整历史（本页第一件事） interchangeable——三件事分开钉。382 syncingheight-vs-history bundled unbundling 在本页 item 1 启动。

3. **看见等于本高 / 看见 syncing_to_height 等于本高 / 看见目标就是本高 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 382 syncingheight bundled interchangeable / 316 txresults interchangeable，也不是已经 syncingheight bundled（382） interchangeable / 893 syncingheight-nothistory interchangeable / 382 syncingheight item 2 / 382 syncingheight item 3，也不是已经 syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史 not already history / not already restored / not already settled 正式三事 bundled（382 item 1 余量） interchangeable / 382 syncingheight item 1 interchangeable，也不是已经有完整历史（本页第一件事） interchangeable / 已经是快照重放（本页第二件事） interchangeable。**  
   官方写：看见等于本高，不是已经交差。看见 syncing_to_height 等于本高，不是已经 settled interchangeable——本页钉 not already settled 单句。看见目标就是本高，不是已经是快照重放（本页第二件事） interchangeable——三件事分开钉。382 syncingheight-vs-history bundled unbundling 在本页 item 1 启动。

怎样写 Finalize 请求、怎样空着更新、怎样编事件是规范里的做法，本页不抄。syncingheight bundled（382）、validator_updates 空则引擎保持当前集合不是已经没有集合（382 item 2 余量）、Finalize 回包 events 标成非确定不是已经必须确定（382 item 3 余量）、切进共识就已经有从创世的完整历史（323）、InitChain 空名单就已经没有集合（相关 InitChain 页）、结果列表就已经同一顺序（316）是另外那套，本页不抄。

## 官方为什么这样拆

- **填了目标 not already history ≠ 382 / 323 interchangeable：** 官方把同步目标高和已经有完整历史分开。
- **在同步 not already restored ≠ 已经是快照重放 interchangeable：** 官方把在同步和已经是快照重放分开。
- **等于本高 not already settled ≠ 已经交差 interchangeable：** 官方把等于本高和已经交差分开；382 syncingheight-vs-history bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 填了目标 | 不是 already history | 不是切进共识就已经有从创世的完整历史 alone（323） |
| 在同步 | 不是 already restored | 不是 Offer 收下就已经装完 alone（321） |
| 等于本高 | 不是 already settled | 不是空着 already empty alone（382 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史 not already history / not already restored / not already settled 正式三事（382 余量），必须分开填了目标 是不是 already history interchangeable / 382 syncingheight bundled interchangeable / syncingheight-sold-as-history interchangeable、在同步 是不是 already restored interchangeable、等于本高 是不是 already settled interchangeable。可以跳过「看见填了目标就已经有完整历史 interchangeable / 就已经是快照重放 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Finalize 请求回包。382 syncingheight-vs-history bundled unbundling 在本页 item 1 启动（893）。

## 本页不抄

- 怎样写 Finalize 请求、怎样空着更新、怎样编事件。
- syncingheight bundled。那是不变量 382。
- validator_updates 空则引擎保持当前集合不是已经没有集合。那是不变量 382 item 2 余量。
- Finalize 回包 events 标成非确定不是已经必须确定。那是不变量 382 item 3 余量。
- 切进共识就已经有从创世的完整历史。那是不变量 323。
- Offer 收下就已经装完。那是不变量 321。
- 结果列表就已经同一顺序。那是不变量 316。
