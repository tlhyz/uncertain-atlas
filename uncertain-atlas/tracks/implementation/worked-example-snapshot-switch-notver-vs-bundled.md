# 例：看见 Info 的 AppHash 对上 is not already version-matched interchangeable / not already this-header interchangeable / not already settled interchangeable

**层次**：实现 / AppHash 对上 not already version-matched / not already this-header / not already settled 正式三事（323 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transition to Consensus。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「AppHash 对上 not already version-matched / not already this-header / not already settled 正式三事（323 余量）/ not 954 snapshot-switch-notver interchangeable / not 323 snapshot-switch-vs-history bundled interchangeable」，不是切进 bundled（323），也不是本头 AppHash 已经是本高度交差（147），也不是拍了就已经交差之后拍（324/950）。不要另写怎样切到共识或怎样配扩展。

## 官方三件事

1. **看见 Info 的 AppHash 对上了 / 看见对上下一高度 这份核对 is not already 已经是版本也对上 interchangeable，也不是已经切进 bundled（323） interchangeable / 954 snapshot-switch-notver interchangeable / 953 snapshot-switch-notchain interchangeable / 323 snapshot-switch item 1 装完 interchangeable，也不是已经 AppHash 对上 not already version-matched / not already this-header / not already settled 正式三事 bundled（323 item 2 余量） interchangeable / 323 snapshot-switch item 2 interchangeable。**  
   官方写：还会再叫 Info，核对两件独立的事：交给应用的快照 AppHash，要和下一高度块里存的 AppHash 对上；应用在 InfoResponse 回的版本，要和当前高度块头上的版本对上。看见 AppHash 对上，不是已经是版本也对上 interchangeable——本页从 323 item 2 侧钉 not already version-matched 单句。323 snapshot-switch vs history bundled unbundling 在本页 item 2 续。

2. **看见对了下一高度 / 看见 AppHash 对上 / 这份核对 is not already 已经对了当前头 interchangeable，也不是已经切进 bundled（323） interchangeable / 954 snapshot-switch-notver interchangeable / 323 snapshot-switch item 3 切进共识 interchangeable / 955 snapshot-switch-nothist interchangeable，也不是已经本头 AppHash 已经是本高度交差 interchangeable / 147 apphash-commit interchangeable。**  
   官方把下一高度的根和当前头的版本分成两次核对。看见对了下一高度，不是已经对了当前头 interchangeable。本页钉 not already this-header 单句。

3. **看见 Info 绿了 / 看见 AppHash 对上 / 这份核对 is not already 已经交差 interchangeable，也不是已经切进 bundled（323） interchangeable / 954 snapshot-switch-notver interchangeable / 953 snapshot-switch-notchain interchangeable，也不是已经拍了就已经交差之后拍 interchangeable / 324/950 snapshot-take-notafter interchangeable。**  
   官方把 Info 绿了和已经是本头已经交差分开。看见 Info 绿了，不是已经交差 interchangeable。323 snapshot-switch vs history bundled unbundling 在本页 item 2 续。

怎样切到共识、怎样配 RFC-100、怎样写扩展高度是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **AppHash 对上 not already version-matched ≠ 已经版本也对上 interchangeable：** 官方把下一高度的根和当前头的版本分成两次核对。
- **看见对了下一高度 not already this-header ≠ 已经对了当前头 interchangeable：** 官方把对上下一高度和已经对了当前头分开。
- **看见 Info 绿了 not already settled ≠ 已经交差 interchangeable：** 官方把 Info 绿了和已经是本头交差分开；323 snapshot-switch vs history bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| AppHash 对上 | 不是已经版本也对上 | 不是本头 AppHash 已经是本高度交差（147） |
| 看见对了下一高度 | 不是已经对了当前头 | 不是拍了就已经交差之后拍（324/950） |
| 看见 Info 绿了 | 不是已经交差 | 不是切进共识就已经有完整历史（955） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 AppHash 对上 not already version-matched / not already this-header / not already settled 正式三事（323 余量），必须分开是不是已经版本也对上、是不是已经对了当前头、是不是已经交差。可以跳过「看见装完就已经是全节点」。不要另写怎样切到共识或怎样配扩展。323 snapshot-switch vs history bundled unbundling 在本页 item 2 续；续 [`worked-example-snapshot-switch-nothist-vs-bundled.md`](worked-example-snapshot-switch-nothist-vs-bundled.md)（不变量 955 item 3）。

## 本页不抄

- 怎样切到共识、怎样配 RFC-100、怎样写扩展高度。
- 切进 bundled。那是不变量 323。
- 本头 AppHash 已经是本高度交差。那是不变量 147。
- 拍了就已经交差之后拍。那是不变量 324/950。
