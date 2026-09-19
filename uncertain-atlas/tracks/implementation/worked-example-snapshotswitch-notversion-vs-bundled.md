# 例：看见 AppHash 对上 / 看见对了下一高度 / 看见 Info 绿了 is not already already version-matched interchangeable / already current-header interchangeable / already this-header-settled interchangeable

**层次**：实现 / AppHash 对上不是已经版本也对上 not already version-matched / not already current-header / not already this-header-settled 正式三事（323 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transition to Consensus。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「AppHash 对上不是已经版本也对上 not already version-matched / not already current-header / not already this-header-settled 正式三事（323 余量）/ not 726 snapshotswitch-notversion interchangeable / not 323 snapshotswitch bundled interchangeable」，不是 Transition to Consensus bundled（323），也不是装完不是已经有了 ChainID（725 item 1 余量）或切进共识不是已经有完整历史（727 item 3 余量）。不要另写怎样切到共识或怎样配扩展。

## 官方三件事

规范把 Requirements 里还会再叫 `Info`、核对两件独立的事——交给应用的快照 AppHash 要和**下一高度**块里存的 AppHash 对上、应用在 `InfoResponse` 回的版本要和**当前高度**块头上的版本对上——和「已经是 AppHash 对上就已经版本也对上 interchangeable / 已经是对了下一高度就已经对了当前头 interchangeable / 已经是 Info 绿了就已经本头交差 interchangeable / 已经是 Transition to Consensus bundled interchangeable」分开写成三件独立的实现事，不是「看见 Info 的 AppHash 对上了就已经版本也对上 interchangeable / 就已经对了当前头 interchangeable / 就已经本头交差 interchangeable」一件事：

1. **看见 AppHash 对上 / 看见 Info 的 AppHash 对上了 / 看见快照 AppHash 对上下一高度 is not already 已经是版本也对上 interchangeable / 已经 version-matched interchangeable / 已经版本交差 interchangeable / 323 snapshotswitch bundled interchangeable / 33 four gates interchangeable / snapshotswitch-sold-as-full-history interchangeable，也不是已经 Transition to Consensus bundled（323） interchangeable / 726 snapshotswitch-notversion interchangeable / 323 snapshotswitch item 2 interchangeable，也不是已经 AppHash 对上不是已经版本也对上 not already version-matched / not already current-header / not already this-header-settled 正式三事 bundled（323 item 2 余量） interchangeable / 323 snapshotswitch item 2 interchangeable，也不是已经装完不是已经有了 ChainID（725） interchangeable / 727 snapshotswitch-nothistory interchangeable / 38 apphash interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：核对两件独立的事——下一高度 AppHash 与当前高度版本。看见 AppHash 对上，不是已经是版本也对上 interchangeable——323 钉 bundled 三事，本页从 item 2 侧钉 not already version-matched 单句。看见 Info 的 AppHash 对上了，不是已经 Transition to Consensus bundled（323） interchangeable——323 钉 bundled，本页钉 item 2 第一件事。看见快照 AppHash 对上下一高度，不是已经装完不是已经有了 ChainID（725） interchangeable——725 另钉 item 1，本页钉 item 2 第一件事。323 snapshotswitch vs history bundled unbundling 在本页 item 2 续。

2. **看见对了下一高度 / 看见对上下一高度 / 看见下一高度块里 AppHash 对上 is not already 已经对了当前头 interchangeable / 已经 current-header interchangeable / 已经当前高度头交差 interchangeable / 323 snapshotswitch bundled interchangeable / 38 apphash interchangeable，也不是已经 Transition to Consensus bundled（323） interchangeable / 726 snapshotswitch-notversion interchangeable / 323 snapshotswitch item 1 装完 interchangeable / 323 snapshotswitch item 3 切进共识 interchangeable，也不是已经 AppHash 对上不是已经版本也对上 not already version-matched / not already current-header / not already this-header-settled 正式三事 bundled（323 item 2 余量） interchangeable / 323 snapshotswitch item 2 interchangeable，也不是已经版本也对上（本页第一件事） interchangeable。**  
   官方把下一高度 AppHash 核对和当前高度头版本核对分开——对了下一高度，不等于已经对了当前头。看见对了下一高度，不是已经 current-header interchangeable——本页钉 not already current-header 单句。看见对上下一高度，不是已经切进共识不是已经有完整历史（727） interchangeable——727 另钉 item 3，本页钉 item 2 第二件事。看见下一高度块里 AppHash 对上，不是已经版本也对上（本页第一件事） interchangeable——三件事分开钉。323 snapshotswitch vs history bundled unbundling 在本页 item 2 续。

3. **看见 Info 绿了 / 看见再叫 Info 绿了 / 看见 InfoResponse 对上 is not already 已经是本头已经交差 interchangeable / 已经 this-header-settled interchangeable / 已经本头 AppHash 交差 interchangeable / 323 snapshotswitch bundled interchangeable / 725 snapshotswitch-notchainid interchangeable，也不是已经 Transition to Consensus bundled（323） interchangeable / 726 snapshotswitch-notversion interchangeable / 323 snapshotswitch item 1 / 323 snapshotswitch item 3，也不是已经 AppHash 对上不是已经版本也对上 not already version-matched / not already current-header / not already this-header-settled 正式三事 bundled（323 item 2 余量） interchangeable / 323 snapshotswitch item 2 interchangeable，也不是已经版本也对上（本页第一件事） interchangeable / 已经对了当前头（本页第二件事） interchangeable。**  
   官方把再叫 Info 核对和已经是本头已经交差路径分开——Info 绿了，不等于已经是本头交差。看见 Info 绿了，不是已经 this-header-settled interchangeable——本页钉 not already this-header-settled 单句。看见再叫 Info 绿了，不是已经版本也对上（本页第一件事） interchangeable——三件事分开钉。看见 InfoResponse 对上，不是已经只有 AppHash 可信任（38） interchangeable——38 另钉信任边界。323 snapshotswitch vs history bundled unbundling 在本页 item 2 完成。

怎样切到共识、怎样配 RFC-100、怎样写扩展高度是规范里的取值或做法，本页不抄。Transition to Consensus bundled（323）、装完不是已经有了 ChainID（323 item 1 余量 / 725）、切进共识不是已经有完整历史（323 item 3 余量 / 727）、Offer 收下已经装完（321）、只有 AppHash 可信任（38）、启动对齐当快照重放（314）是另外那套，本页不抄。

## 官方为什么这样拆

- **AppHash 对上 not already version-matched ≠ 323 / 33 interchangeable：** 官方把下一高度 AppHash 与当前高度版本分成两次核对。
- **对了下一高度 not already current-header ≠ 已经对了当前头 interchangeable：** 官方把下一高度核对和当前头核对分开。
- **Info 绿了 not already this-header-settled ≠ 已经本头交差 interchangeable：** 官方把再叫 Info 核对和本头已经交差路径分开；323 snapshotswitch vs history bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| AppHash 对上 | 不是 already version-matched | 不是装完 ChainID alone（725） |
| 对了下一高度 | 不是 already current-header | 不是切进共识 alone（727） |
| Info 绿了 | 不是 already this-header-settled | 不是 Only AppHash alone（38） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 AppHash 对上不是已经版本也对上 not already version-matched / not already current-header / not already this-header-settled 正式三事（323 余量），必须分开 AppHash 对上 是不是 already version-matched interchangeable / 323 snapshotswitch bundled interchangeable / snapshotswitch-sold-as-full-history interchangeable、对了下一高度 是不是 already current-header interchangeable、Info 绿了 是不是 already this-header-settled interchangeable。可以跳过「看见 Info 的 AppHash 对上了就已经版本也对上 interchangeable / 就已经对了当前头 interchangeable / 就已经本头交差 interchangeable」。不要另写怎样切到共识。323 snapshotswitch vs history bundled unbundling 在本页 item 2 续；续 [`worked-example-snapshotswitch-nothistory-vs-bundled.md`](worked-example-snapshotswitch-nothistory-vs-bundled.md)（不变量 727 item 3，待写）。

## 本页不抄

- 怎样切到共识、怎样配 RFC-100、怎样写扩展高度。
- Transition to Consensus bundled。那是不变量 323。
- 装完不是已经有了 ChainID。那是不变量 323 item 1 余量 / 725。
- 切进共识不是已经有完整历史。那是不变量 323 item 3 余量 / 727。
- Offer 收下已经装完。那是不变量 321。
- 只有 AppHash 可信任。那是不变量 38。
- 启动对齐当快照重放。那是不变量 314。
