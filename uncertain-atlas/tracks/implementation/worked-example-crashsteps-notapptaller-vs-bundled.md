# 例：看见应用高度比引擎高 / 应用先落了盘 is not already already allowed interchangeable / already can wake separately interchangeable / half-write atomic interchangeable

**层次**：实现 / app taller than engine not already allowed / not already can wake separately / not half-write atomic 正式三事（320 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Crash Recovery。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「app taller than engine not already allowed / not already can wake separately / not half-write atomic 正式三事（320 余量）/ not 686 crashsteps-notapptaller interchangeable / not 320 crashsteps bundled interchangeable」，不是 Crash Recovery 三步 bundled（320），也不是块进 store 不是已经 Commit（687 item 2 余量）或 remember last Commit height（685）。不要另写怎样落盘、怎样写 Commit、怎样做 WAL 旋转。

## 官方三件事

规范把 Crash Recovery 里 CometBFT 和应用**被指望一起崩**、不该出现应用已经持久化的高度高于 CometBFT 已经持久化的最新高度 和「已经是已经允许应用领先 interchangeable / 已经是两边高度不一样就能各醒各的 interchangeable / 已经是半写已经原子 interchangeable / 已经是崩溃恢复三步已经交差 interchangeable」分开写成三件独立的实现事，不是「看见应用比引擎高 就已经允许 interchangeable / 就已经能各醒各的 interchangeable / 就已经半写原子 interchangeable」一件事：

1. **看见应用高度比引擎高 / 看见应用先落了盘 / 看见应用已经持久化的高度高于 CometBFT 已经持久化的最新高度 is not already 已经允许 interchangeable / 已经合法 interchangeable / 已经应用领先已经 OK interchangeable / 320 crashsteps bundled interchangeable / 685 finpersist-notrememberheight interchangeable / 335 finpersist item 3 remember last Commit height interchangeable，也不是已经 Crash Recovery 三步 bundled（320） interchangeable / 686 crashsteps-notapptaller interchangeable / 320 crashsteps item 1 interchangeable，也不是已经 app taller than engine not already allowed / not already can wake separately / not half-write atomic 正式三事 bundled（320 item 1 余量） interchangeable / 320 crashsteps item 1 interchangeable，也不是已经块进 store 不是已经 Commit（687） interchangeable / 688 crashsteps-notinfoskip interchangeable / 5 half-write atomic interchangeable，也不是已经一起崩就已经交差（320） interchangeable / crashsteps-sold-as-committed interchangeable。**  
   官方 Crash Recovery 写：CometBFT 和应用**被指望一起崩**。不该出现应用已经持久化的高度，高于 CometBFT 已经持久化的最新高度。看见应用先写完，不是已经合法 interchangeable——320 钉 bundled 三事，本页从 item 1 侧钉 not already allowed 单句。看见应用比引擎高，不是已经 remember last Commit height（685） interchangeable——685 钉 335 item 3 记住高度，本页钉 Crash Recovery 不许领先单句。看见应用已经持久化的高度更高，不是已经崩溃恢复三步已经交差（320） interchangeable——320 钉 bundled，本页钉 item 1 第一件事。320 crash recovery bundled unbundling 在本页 item 1 启动。

2. **看见应用高度比引擎高 / 看见两边高度不一样 / 看见应用先落了盘 is not already 已经能各醒各的 interchangeable / 已经能单独恢复 interchangeable / 已经能各醒各的 / already can wake separately interchangeable / 320 crashsteps bundled interchangeable / 314 querystate interchangeable / 370 info-vs-handshake interchangeable，也不是已经 Crash Recovery 三步 bundled（320） interchangeable / 686 crashsteps-notapptaller interchangeable / 320 crashsteps item 2 blockstore not Commit interchangeable / 320 crashsteps item 3 Info not skip interchangeable，也不是已经 app taller than engine not already allowed / not already can wake separately / not half-write atomic 正式三事 bundled（320 item 1 余量） interchangeable / 320 crashsteps item 1 interchangeable，也不是已经启动 Info 对上就已经能跳步（320 item 3 / 688） interchangeable / 685 finpersist-notrememberheight interchangeable，也不是已经 WAL 已经 fsync（298） interchangeable / 298 wal-fsync interchangeable。**  
   官方把一起崩 / 不许应用领先单句和两边高度不一样就能各醒各的 / 已经能单独恢复路径分开——320 bundled 第一件事常与「看见高度不一样 就已经能各醒各的 interchangeable / 就已经能单独恢复 interchangeable」混成一句，本页钉 not already can wake separately 单句。看见两边高度不一样，不是已经块进 store 不是已经 Commit（687） interchangeable——687 另钉 item 2，本页钉 item 1 第二件事。看见应用先落了盘，不是已经启动 Info 对上就已经能跳步（688） interchangeable——688 另钉 item 3，本页钉 item 1 第二件事。320 crash recovery bundled unbundling 在本页 item 1 启动。

3. **看见应用高度比引擎高 / 看见能单独重启应用 / 看见应用先落了盘 is not already 已经半写已经原子 interchangeable / 已经 half-write atomic interchangeable / 5 half-write atomic interchangeable / 298 wal-fsync interchangeable / 335 finpersist bundled interchangeable，也不是已经 Crash Recovery 三步 bundled（320） interchangeable / 686 crashsteps-notapptaller interchangeable / 320 crashsteps item 2 / 320 crashsteps item 3，也不是已经 app taller than engine not already allowed / not already can wake separately / not half-write atomic 正式三事 bundled（320 item 1 余量） interchangeable / 320 crashsteps item 1 interchangeable，也不是已经 remember last Commit height（685） interchangeable / 683 finpersist-notmustnot interchangeable / 684 finpersist-notmustincommit interchangeable，也不是已经崩溃恢复三步已经交差（320） interchangeable / crashsteps-sold-as-committed interchangeable。**  
   官方把一起崩 / 不许应用领先单句和半写已经原子路径分开——320 bundled 第一件事常与 5 混成「看见能单独重启应用 就已经半写原子 interchangeable / 就已经和半写已经原子同一句 interchangeable」，本页钉 not half-write atomic 单句。看见能单独重启应用，不是已经半写已经原子（5） interchangeable——5 钉半写原子，本页钉 Crash Recovery item 1 第三件事。看见应用先落了盘，不是已经 WAL 已经 fsync（298） interchangeable——298 另钉 WAL fsync，本页钉 item 1 第三件事。320 crash recovery bundled unbundling 在本页 item 1 完成。

怎样落盘、怎样写 Commit、怎样做 WAL 旋转是规范里的做法，本页不抄。Crash Recovery 三步 bundled（320）、块进 store 不是已经 Commit（320 item 2 余量 / 687）、启动 Info 对上不是已经能跳步（320 item 3 余量 / 688）、半写已经原子（5）、WAL 已经 fsync（298）、remember last Commit height（685）、FinalizeBlock 落盘禁令 bundled（335）是另外那套，本页不抄。

## 官方为什么这样拆

- **app taller than engine not already allowed ≠ 320 crashsteps bundled interchangeable：** 官方把一起崩 / 不许应用领先单句和崩溃恢复三步 bundled 分开。
- **app taller than engine not already can wake separately ≠ 314 / 370 interchangeable：** 官方把不许应用领先单句和两边高度不一样就能各醒各的路径分开。
- **app taller than engine not half-write atomic ≠ 5 half-write atomic interchangeable：** 官方把不许应用领先单句和半写已经原子路径分开；320 crash recovery bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 应用高度比引擎高 | 不是 already allowed | 不是 remember height alone（685） |
| 两边高度不一样 | 不是 already can wake separately | 不是 blockstore not Commit alone（687） |
| 能单独重启应用 | 不是 half-write atomic（5） | 不是 Info not skip alone（688） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 app taller than engine not already allowed / not already can wake separately / not half-write atomic 正式三事（320 余量），必须分开应用比引擎高 是不是 already allowed interchangeable / 320 crashsteps bundled interchangeable / 685 finpersist-notrememberheight interchangeable、两边高度不一样 是不是 already can wake separately interchangeable / 314 querystate interchangeable / 370 info-vs-handshake interchangeable、能单独重启应用 是不是 half-write atomic interchangeable / 5 half-write atomic interchangeable / 298 wal-fsync interchangeable。可以跳过「看见应用比引擎高 就已经允许 interchangeable / 就已经能各醒各的 interchangeable / 就已经半写原子 interchangeable」。不要另写怎样落盘。320 crash recovery bundled unbundling 在本页 item 1 完成；续 [`worked-example-crashsteps-notblockstore-vs-bundled.md`](worked-example-crashsteps-notblockstore-vs-bundled.md)（不变量 687 item 2）。

## 本页不抄

- 怎样落盘、怎样写 Commit、怎样做 WAL 旋转。
- Crash Recovery 三步 bundled。那是不变量 320。
- 块进 store 不是已经 Commit。那是不变量 320 item 2 余量 / 687。
- 启动 Info 对上不是已经能跳步。那是不变量 320 item 3 余量 / 688。
- 半写已经原子。那是不变量 5。
- WAL 已经 fsync。那是不变量 298。
- remember last Commit height。那是不变量 685。
- FinalizeBlock 落盘禁令 bundled。那是不变量 335。
