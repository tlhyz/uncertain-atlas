# 例：看见启动 Info / 对上了 is not already already mid-height resume interchangeable / already can skip replay interchangeable / InitChain already done interchangeable

**层次**：实现 / startup Info not already mid-height resume / not already can skip replay / not InitChain already done 正式三事（320 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Crash Recovery。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「startup Info not already mid-height resume / not already can skip replay / not InitChain already done 正式三事（320 余量）/ not 688 crashsteps-notinfoskip interchangeable / not 320 crashsteps bundled interchangeable」，不是 Crash Recovery 三步 bundled（320），也不是 app taller than engine（686 item 1 余量）或块进 store 不是已经 Commit（687 item 2 余量）。不要另写怎样落盘、怎样写 Commit、怎样做 WAL 旋转。

## 官方三件事

规范把 Crash Recovery 里醒来时 CometBFT 在 Info 连接上叫 `Info`、应用**必须**回与上次成功完成 `Commit` 的那一块一致的信息、只走到 `block_stored` 要重放、`block_stored` 加 `state_stored` 要对结果、三步都齐才进下一高度、乱序会 panic、第一块 Commit 之前 `InitChain` **会再叫一次** 和「已经是 Info 绿了就能从半截高度接着走 interchangeable / 已经是对上了就能跳过重放 interchangeable / 已经是 InitChain 叫过就不用再叫 interchangeable / 已经是崩溃恢复三步已经交差 interchangeable」分开写成三件独立的实现事，不是「看见 Info 对上了 就已经能从任意高度接着走 interchangeable / 就已经能跳步 interchangeable / 就已经不用再叫 InitChain interchangeable」一件事：

1. **看见启动 Info / 看见 Info 绿了 / 看见应用回了与上次成功 Commit 一致的信息 is not already 已经能从半截高度接着走 interchangeable / 已经是任意高度 interchangeable / 已经 mid-height resume interchangeable / 314 querystate interchangeable / 370 info-vs-handshake interchangeable / 320 crashsteps bundled interchangeable，也不是已经 Crash Recovery 三步 bundled（320） interchangeable / 688 crashsteps-notinfoskip interchangeable / 320 crashsteps item 3 interchangeable，也不是已经 startup Info not already mid-height resume / not already can skip replay / not InitChain already done 正式三事 bundled（320 item 3 余量） interchangeable / 320 crashsteps item 3 interchangeable，也不是已经 app taller than engine（686） interchangeable / 687 crashsteps-notblockstore interchangeable / 685 finpersist-notrememberheight interchangeable，也不是已经崩溃恢复三步已经交差（320） interchangeable / crashsteps-sold-as-committed interchangeable。**  
   官方 Crash Recovery 写：醒来时 CometBFT 在 Info 连接上叫 `Info`，应用**必须**回与上次成功完成 `Commit` 的那一块一致的信息。看见 Info 绿了，不是已经能从半截高度接着走 interchangeable——320 钉 bundled 三事，本页从 item 3 侧钉 not already mid-height resume 单句。看见启动 Info，不是已经启动对齐已经是快照重放（314） interchangeable——314 钉 QueryState，本页钉 Crash Recovery Info 单句。看见 Info 对上了，不是已经崩溃恢复三步已经交差（320） interchangeable——320 钉 bundled，本页钉 item 3 第一件事。320 crash recovery bundled unbundling 在本页 item 3 启动。

2. **看见对上了 / 看见应用回了一致信息 / 看见 Info 对齐 is not already 已经能跳过重放 interchangeable / 已经能跳步 interchangeable / 已经 can skip replay interchangeable / 320 crashsteps bundled interchangeable / 685 finpersist-notrememberheight interchangeable / 38 genesis-replay interchangeable / 323 full-history interchangeable，也不是已经 Crash Recovery 三步 bundled（320） interchangeable / 688 crashsteps-notinfoskip interchangeable / 320 crashsteps item 1 app taller interchangeable / 320 crashsteps item 2 blockstore not Commit interchangeable，也不是已经 startup Info not already mid-height resume / not already can skip replay / not InitChain already done 正式三事 bundled（320 item 3 余量） interchangeable / 320 crashsteps item 3 interchangeable，也不是已经只走到 block_stored 就不用重放 FinalizeBlock interchangeable / 已经 state_stored 就不用再对结果 interchangeable，也不是已经 remember last Commit height 就已经能跳步（685） interchangeable。**  
   官方把 Info 必须对上上次 Commit 单句和已经能跳过重放 / 已经能跳步路径分开——只走到 `block_stored`：重放 `FinalizeBlock` 及之后；`block_stored` 加 `state_stored`：再执行一次 `FinalizeBlock` 来对结果，对不上就 panic；三步都齐：才进下一高度；乱序会 panic。看见对上了，不是已经能跳过重放 interchangeable——本页钉 not already can skip replay 单句。看见 Info 对齐，不是已经 remember last Commit height 就已经能跳步（685） interchangeable——685 钉 335 item 3，本页钉 Crash Recovery 重放路径单句。看见应用回了一致信息，不是已经块进 store 就已经交差（687） interchangeable——687 另钉 item 2，本页钉 item 3 第二件事。320 crash recovery bundled unbundling 在本页 item 3 启动。

3. **看见 InitChain 叫过 / 看见第一块 Commit 之前 InitChain 之后崩了 / 看见应用仍在高度 0 is not already 已经不用再叫 InitChain interchangeable / 已经 InitChain already done interchangeable / 已经创世已经齐 interchangeable / 411 initonce interchangeable / 495 initchainusage bundled interchangeable / 303 validatorupdate interchangeable，也不是已经 Crash Recovery 三步 bundled（320） interchangeable / 688 crashsteps-notinfoskip interchangeable / 320 crashsteps item 1 / 320 crashsteps item 2，也不是已经 startup Info not already mid-height resume / not already can skip replay / not InitChain already done 正式三事 bundled（320 item 3 余量） interchangeable / 320 crashsteps item 3 interchangeable，也不是已经 Info 握手对齐（370） interchangeable / 668 infousage-notquerystate interchangeable / 669 infousage-nothandshake interchangeable，也不是已经崩溃恢复三步已经交差（320） interchangeable / crashsteps-sold-as-committed interchangeable。**  
   官方把第一块 Commit 之前、`InitChain` 之后崩了：应用应仍在高度 0，`InitChain` **会再叫一次** 和 InitChain 叫过就不用再叫路径分开——320 bundled 第三件事常与「看见 InitChain 叫过 就已经不用再叫 interchangeable / 就已经创世已经齐 interchangeable」混成一句，本页钉 not InitChain already done 单句。看见 InitChain 叫过，不是已经 InitChain Usage 创世只调一次（411 / 495） interchangeable——那些钉 Usage，本页钉 Crash Recovery 再叫路径单句。看见应用仍在高度 0，不是已经 app taller than engine（686） interchangeable——686 另钉 item 1，本页钉 item 3 第三件事。320 crash recovery bundled unbundling 在本页 item 3 完成。

怎样落盘、怎样写 Commit、怎样做 WAL 旋转是规范里的做法，本页不抄。Crash Recovery 三步 bundled（320）、app taller than engine（320 item 1 余量 / 686）、块进 store 不是已经 Commit（320 item 2 余量 / 687）、半写已经原子（5）、WAL 已经 fsync（298）、启动对齐当快照重放（314）、remember last Commit height（685）、Info 握手对齐（370）是另外那套，本页不抄。

## 官方为什么这样拆

- **startup Info not already mid-height resume ≠ 314 / 370 interchangeable：** 官方把 Info 必须对上上次 Commit 单句和已经能从半截高度接着走路径分开。
- **Info 对上 not already can skip replay ≠ 685 / 38 interchangeable：** 官方把 Info 对齐单句和已经能跳过重放 / 已经能跳步路径分开。
- **InitChain 叫过 not InitChain already done ≠ 411 / 495 interchangeable：** 官方把 Crash Recovery 再叫 InitChain 单句和创世只调一次 / 已经不用再叫路径分开；320 crash recovery bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 启动 Info 绿了 | 不是 already mid-height resume | 不是 querystate alone（314） |
| Info 对上了 | 不是 already can skip replay | 不是 remember height alone（685） |
| InitChain 叫过 | 不是 InitChain already done | 不是 InitChain Usage alone（495） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 startup Info not already mid-height resume / not already can skip replay / not InitChain already done 正式三事（320 余量），必须分开 Info 绿了 是不是 already mid-height resume interchangeable / 314 querystate interchangeable / 370 info-vs-handshake interchangeable、对上了 是不是 already can skip replay interchangeable / 685 finpersist-notrememberheight interchangeable / 38 genesis-replay interchangeable、InitChain 叫过 是不是 InitChain already done interchangeable / 411 initonce interchangeable / 495 initchainusage bundled interchangeable。可以跳过「看见 Info 对上了 就已经能从任意高度接着走 interchangeable / 就已经能跳步 interchangeable / 就已经不用再叫 InitChain interchangeable」。不要另写怎样落盘。320 crash recovery bundled unbundling 在本页 item 3 完成（686 + 687 + 688）。

## 本页不抄

- 怎样落盘、怎样写 Commit、怎样做 WAL 旋转。
- Crash Recovery 三步 bundled。那是不变量 320。
- app taller than engine。那是不变量 320 item 1 余量 / 686。
- 块进 store 不是已经 Commit。那是不变量 320 item 2 余量 / 687。
- 半写已经原子。那是不变量 5。
- WAL 已经 fsync。那是不变量 298。
- 启动对齐当快照重放。那是不变量 314。
- remember last Commit height。那是不变量 685。
- Info 握手对齐。那是不变量 370。
