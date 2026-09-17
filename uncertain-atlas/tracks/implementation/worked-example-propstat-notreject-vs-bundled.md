# 例：看见 REJECT means app considers proposal invalid consensus prevote nil is not already can change later interchangeable / not already not in block interchangeable / not already VerifyStatus REJECT interchangeable

**层次**：实现 / ProposalStatus REJECT prevote nil not can change later / not already not in block / not VerifyStatus REJECT 正式三事（376 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ProposalStatus。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProposalStatus REJECT prevote nil not can change later / not already not in block / not VerifyStatus REJECT 正式三事（376 余量）/ not 715 propstat-notreject interchangeable / not 376 proposalstatus-vs-prevote bundled interchangeable」，不是 ProposalStatus 正式三事 bundled（376），也不是 Process 调用是同步的就已经能在返回之后再改裁决（354）或 Process REJECT assumes invalid（455）。不要另写怎样写 ProposalStatus。

## 官方三件事

1. **看见 `REJECT` 表示应用认为这份提案非法 / 共识算法拒掉这份提案，改发 Prevote nil / REJECT is not already 已经能在返回之后再改裁决 interchangeable / 354 procsync interchangeable，也不是已经 ProposalStatus 正式三事 bundled（376） interchangeable / 715 propstat-notreject interchangeable / 713 propstat-notunknown interchangeable / 376 proposalstatus item 1 UNKNOWN interchangeable，也不是已经 REJECT prevote nil not can change later / not already not in block / not VerifyStatus REJECT 正式三事 bundled（376 item 3 余量） interchangeable / 376 proposalstatus item 3 interchangeable。**  
   官方 Data Types 写：REJECT 表示应用认为这份提案非法。共识算法拒掉这份提案，改发 Prevote nil。看见回了 REJECT，不是已经能在返回之后再改裁决 interchangeable——本页从 376 item 3 侧钉 not can change later 单句。376 proposalstatus vs prevote bundled unbundling 在本页 item 3 完成。

2. **看见回了 `REJECT` / 看见发了 nil / REJECT is not already 已经没进块 interchangeable，也不是已经 ProposalStatus 正式三事 bundled（376） interchangeable / 715 propstat-notreject interchangeable / 376 proposalstatus item 2 ACCEPT interchangeable / 714 propstat-notaccept interchangeable。**  
   官方把 REJECT 发 Prevote nil 和已经没进块分开——376 bundled 第三件事常与「看见 nil 就已经没进块 interchangeable」糊成一句，本页钉 not already not in block 单句。

3. **看见回了 `REJECT` / 看见 Usage 这句 / REJECT is not already 已经 VerifyStatus REJECT 丢掉整张 Precommit interchangeable / 434 verifystatus interchangeable / 已经 Process REJECT assumes not valid 就已经当成块非法（455） interchangeable / 455 procreject interchangeable，也不是已经 ProposalStatus 正式三事 bundled（376） interchangeable / 715 propstat-notreject interchangeable / 713 propstat-notunknown interchangeable。**  
   官方把 ProposalStatus REJECT 发 Prevote nil 和 Verify REJECT 丢票 / Process REJECT 当块非法分开。看见发了 nil，不是已经扩展非法或块非法 interchangeable。376 proposalstatus vs prevote bundled unbundling 在本页 item 3 完成。

怎样写 `ProposalStatus`、怎样挑枚举、怎样发 Prevote 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **REJECT prevote nil not can change later ≠ 354 interchangeable：** 官方把发 Prevote nil 和返回之后还能再改裁决分开。
- **REJECT prevote nil not already not in block ≠ 已经没进块 interchangeable：** 官方把发 nil 和已经没进块分开。
- **REJECT prevote nil not VerifyStatus REJECT ≠ 434 / 455 interchangeable：** 官方把 Process REJECT 发 nil 和 Verify REJECT / Process assumes invalid 分开；376 proposalstatus vs prevote bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| REJECT 表示应用认为提案非法、共识会发 Prevote nil | 不是已经能稍后改裁决（354） | 不是 UNKNOWN 会崩（713/376 item 1） |
| 看见回了 REJECT | 不是已经没进块 | 不是 ProposalStatus bundled（376） |
| 看见发了 nil | 不是 VerifyStatus REJECT（434） / Process REJECT 当块非法（455） | 不是 ACCEPT 会发 Prevote（714/376 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProposalStatus REJECT prevote nil not can change later / not already not in block / not VerifyStatus REJECT 正式三事（376 余量），必须分开 REJECT 是不是已经能稍后改裁决 interchangeable / 354、是不是已经没进块、是不是 Verify REJECT / Process 当块非法 interchangeable / 434 / 455。可以跳过「看见回了 REJECT 就已经能稍后改裁决」。不要另写怎样写 ProposalStatus。376 proposalstatus vs prevote bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 ProposalStatus、怎样挑枚举、怎样发 Prevote。
- ProposalStatus 正式三事 bundled。那是不变量 376。
- UNKNOWN 一律是错、引擎当应用坏了会崩。那是不变量 376 item 1 余量 / 713。
- ACCEPT 表示应用认为提案合法、共识会发 Prevote。那是不变量 376 item 2 余量 / 714。
- Process 调用是同步的就已经能在返回之后再改裁决。那是不变量 354。
- VerifyStatus REJECT。那是不变量 434。
- Process REJECT assumes not valid。那是不变量 455。
