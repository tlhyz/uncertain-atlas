# 例：看见回包块含元数据不能超过 16 MB is not already 4 MB snapshot message interchangeable / not already consensus constant interchangeable / not already restored interchangeable

**层次**：实现 / 16 MB 上限 not already 4 MB snapshot message / not already consensus constant / not already restored 正式三事（375 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) LoadSnapshotChunk。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「16 MB 上限 not already 4 MB snapshot message / not already consensus constant / not already restored 正式三事（375 余量）/ not 802 loadchunk-not4mb interchangeable / not 375 loadchunk-vs-retrieved bundled interchangeable」，不是 LoadSnapshotChunk bundled（375），也不是 Offer 收下就已经装完（321），也不是 Apply 这块就已经是 Offer（397/742），也不是 Usage retrieve 就已经齐（501/658）。不要另写怎样写 LoadSnapshotChunk。

## 官方三件事

1. **看见回包块含元数据不能超过 16 MB / 看见有上限 / 这份上限 is not already 已经是快照报文 4 MB interchangeable / 321 restored interchangeable，也不是已经 LoadSnapshotChunk bundled（375） interchangeable / 802 loadchunk-not4mb interchangeable / 800 loadchunk-notcomplete interchangeable / 375 loadchunk item 1 拉块 interchangeable，也不是已经 16 MB 上限 not already 4 MB snapshot message / not already consensus constant / not already restored 正式三事 bundled（375 item 3 余量） interchangeable / 375 loadchunk item 3 interchangeable。**  
   官方写：回包是任意格式的二进制块。块报文含元数据不能超过 16 MB，所以 10 MB 是个好起点。看见有上限，不是已经是网上一份快照报文最多 4 MB interchangeable——本页从 375 item 3 侧钉 not already 4 MB snapshot message 单句。375 loadchunk vs retrieved bundled unbundling 在本页 item 3 完成。

2. **看见有上限 / 看见 10 MB / 这份上限 is not already 已经是共识常数 interchangeable / 321 restored interchangeable，也不是已经 LoadSnapshotChunk bundled（375） interchangeable / 802 loadchunk-not4mb interchangeable / 375 loadchunk item 2 三列 interchangeable / 801 loadchunk-notsame interchangeable，也不是已经 Apply 这块就已经是 Offer interchangeable / 397 applychunk / 742 applychunk-notoffer interchangeable，也不是已经 Usage retrieve 就已经齐 interchangeable / 501 loadsnapusage / 658 loadsnapusage-notretrieve interchangeable。**  
   官方把 10 MB 起点和已经是共识常数分开——375 bundled 第三件事常与 321 / 397 / 501 混成「看见有上限就已经是 4 MB 或已经装完 interchangeable」，本页钉 not already consensus constant 单句。

3. **看见有上限 / 看见回了字节 / 这份上限 is not already 已经装完 interchangeable，也不是已经 LoadSnapshotChunk bundled（375） interchangeable / 802 loadchunk-not4mb interchangeable / 800 loadchunk-notcomplete interchangeable。**  
   官方把回了字节和已经装完分开。看见回了字节，不是已经装完 interchangeable。375 loadchunk vs retrieved bundled unbundling 在本页 item 3 完成。

怎样写 LoadSnapshotChunk、怎样切块、怎样挑 10 MB 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **16 MB 上限 not already 4 MB snapshot message ≠ 321 interchangeable：** 官方把块报文上限和网上一份快照报文 4 MB 分开。
- **看见 10 MB not already consensus constant ≠ 已经是共识常数 interchangeable：** 官方把 10 MB 起点和已经是共识常数分开。
- **看见回了字节 not already restored ≠ 已经装完 interchangeable：** 官方把回了字节和已经装完分开；375 loadchunk vs retrieved bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回包块含元数据不能超过 16 MB | 不是已经是快照报文 4 MB（321） | 不是从邻居拉块（800/375 item 1） |
| 看见有上限 | 不是已经是共识常数 | 不是 Apply 这块（397/742） |
| 看见回了字节 | 不是已经装完 | 不是 Usage retrieve 就已经齐（501/658） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 16 MB 上限 not already 4 MB snapshot message / not already consensus constant / not already restored 正式三事（375 余量），必须分开是不是已经是快照报文 4 MB、是不是已经是共识常数、是不是已经装完。可以跳过「看见有上限就已经是 4 MB」。不要另写怎样写 LoadSnapshotChunk。375 loadchunk vs retrieved bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 LoadSnapshotChunk、怎样切块、怎样挑 10 MB。
- LoadSnapshotChunk bundled。那是不变量 375。
- 从邻居拉快照块。那是不变量 375 item 1 余量 / 800。
- Offer 收下就已经装完。那是不变量 321。
- Apply 这块就已经是 Offer。那是不变量 397 / 742。
