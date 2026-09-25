# 例：看见有上限 / 看见 10 MB / 看见回了字节 is not already already 4mb interchangeable / already constant interchangeable / already restored interchangeable

**层次**：实现 / 回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB not already 4mb / not already constant / not already restored 正式三事（375 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) LoadSnapshotChunk Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB not already 4mb / not already constant / not already restored 正式三事（375 余量）/ not 874 loadchunk-not4mb interchangeable / not 375 loadchunk bundled interchangeable」，不是 loadchunk bundled（375），也不是 LoadSnapshotChunk 用来从邻居拉快照块不是已经齐（872 item 1 余量）或请求用 height / format / chunk（从 0 起）认这块不是已经是同一份（873 item 2 余量）。不要另写怎样写 LoadSnapshotChunk。

## 官方三件事

规范把 Methods 里回包块含元数据不能超过 16 MB 和「已经是有上限就已经是快照报文 4 MB interchangeable / 已经是 10 MB 就已经是共识常数 interchangeable / 已经是回了字节就已经装完 interchangeable / 已经是 loadchunk bundled interchangeable」分开写成三件独立的实现事，不是「看见有上限就已经是快照报文 4 MB interchangeable / 就已经是共识常数 interchangeable / 就已经装完 interchangeable」一件事：

1. **看见有上限 / 看见回包块含元数据不能超过 16 MB / 看见有 16 MB 上限 is not already 已经是快照报文 4 MB interchangeable / 已经 4mb interchangeable / 已经是快照报文 4 MB 交差 interchangeable / 375 loadchunk bundled interchangeable / 321 Offer restored interchangeable / loadchunk-sold-as-retrieved interchangeable，也不是已经 loadchunk bundled（375） interchangeable / 874 loadchunk-not4mb interchangeable / 375 loadchunk item 3 interchangeable，也不是已经回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB not already 4mb / not already constant / not already restored 正式三事 bundled（375 item 3 余量） interchangeable / 375 loadchunk item 3 interchangeable，也不是已经在拉就已经齐（872） interchangeable / 填了三列就已经是同一份（873） interchangeable / 368 Snapshot identical interchangeable，也不是已经 Offer 收下就已经装完（321） interchangeable。**  
   官方写：回包是任意格式的二进制块。块报文含元数据不能超过 16 MB，所以 10 MB 是个好起点。看见有上限，不是已经是网上一份快照报文最多 4 MB。看见有上限，不是已经 4mb interchangeable——375 钉 bundled 三事，本页从 item 3 侧钉 not already 4mb 单句。看见回包块含元数据不能超过 16 MB，不是已经 loadchunk bundled（375） interchangeable——375 钉 bundled，本页钉 item 3 第一件事。看见有 16 MB 上限，不是已经 Offer 收下就已经装完（321） interchangeable——321 另钉。375 loadchunk-vs-retrieved bundled unbundling 在本页 item 3 完成。

2. **看见 10 MB / 看见 10 MB 是个好起点 / 看见挑了 10 MB is not already 已经是共识常数 interchangeable / 已经 constant interchangeable / 已经是共识常数交差 interchangeable / 375 loadchunk bundled interchangeable / 872 loadchunk-notcomplete interchangeable，也不是已经 loadchunk bundled（375） interchangeable / 874 loadchunk-not4mb interchangeable / 375 loadchunk item 1 在拉 interchangeable / 375 loadchunk item 2 填了三列 interchangeable，也不是已经回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB not already 4mb / not already constant / not already restored 正式三事 bundled（375 item 3 余量） interchangeable / 375 loadchunk item 3 interchangeable，也不是已经是快照报文 4 MB（本页第一件事） interchangeable。**  
   官方写：看见 10 MB，不是已经是共识常数。看见 10 MB 是个好起点，不是已经 constant interchangeable——本页钉 not already constant 单句。看见挑了 10 MB，不是已经是快照报文 4 MB（本页第一件事） interchangeable——三件事分开钉。375 loadchunk-vs-retrieved bundled unbundling 在本页 item 3 完成。

3. **看见回了字节 / 看见回了块字节 / 看见回包有字节 is not already 已经装完 interchangeable / 已经 restored interchangeable / 已经装完交差 interchangeable / 375 loadchunk bundled interchangeable / 321 Offer restored interchangeable，也不是已经 loadchunk bundled（375） interchangeable / 874 loadchunk-not4mb interchangeable / 375 loadchunk item 1 / 375 loadchunk item 2，也不是已经回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB not already 4mb / not already constant / not already restored 正式三事 bundled（375 item 3 余量） interchangeable / 375 loadchunk item 3 interchangeable，也不是已经是快照报文 4 MB（本页第一件事） interchangeable / 已经是共识常数（本页第二件事） interchangeable。**  
   官方写：看见回了字节，不是已经装完。看见回了块字节，不是已经 restored interchangeable——本页钉 not already restored 单句。看见回包有字节，不是已经是共识常数（本页第二件事） interchangeable——三件事分开钉。375 loadchunk-vs-retrieved bundled unbundling 在本页 item 3 完成。

怎样写 LoadSnapshotChunk、怎样切块、怎样挑 10 MB 是规范里的做法，本页不抄。loadchunk bundled（375）、LoadSnapshotChunk 用来从邻居拉快照块不是已经齐（375 item 1 余量 / 872）、请求用 height / format / chunk（从 0 起）认这块不是已经是同一份（375 item 2 余量 / 873）、ListSnapshots 回了就已经齐（322）、全字段（含 Metadata）对上就已经装完（368）、Offer 收下就已经装完（321）是另外那套，本页不抄。

## 官方为什么这样拆

- **有上限 not already 4mb ≠ 375 / 321 interchangeable：** 官方把块报文上限和快照报文上限分开。
- **10 MB not already constant ≠ 已经是共识常数 interchangeable：** 官方把 10 MB 好起点和已经是共识常数分开。
- **回了字节 not already restored ≠ 已经装完 interchangeable：** 官方把回了字节和已经装完分开；375 loadchunk-vs-retrieved bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 有上限 | 不是 already 4mb | 不是 Offer 收下就已经装完 alone（321） |
| 10 MB | 不是 already constant | 不是在拉 already complete alone（872） |
| 回了字节 | 不是 already restored | 不是填了三列 already identical alone（873） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB not already 4mb / not already constant / not already restored 正式三事（375 余量），必须分开有上限 是不是 already 4mb interchangeable / 375 loadchunk bundled interchangeable / loadchunk-sold-as-retrieved interchangeable、10 MB 是不是 already constant interchangeable、回了字节 是不是 already restored interchangeable。可以跳过「看见有上限就已经是快照报文 4 MB interchangeable / 就已经是共识常数 interchangeable / 就已经装完 interchangeable」。不要另写怎样写 LoadSnapshotChunk。375 loadchunk-vs-retrieved bundled unbundling 在本页 item 3 完成（872 + 873 + 874）。

## 本页不抄

- 怎样写 LoadSnapshotChunk、怎样切块、怎样挑 10 MB。
- loadchunk bundled。那是不变量 375。
- LoadSnapshotChunk 用来从邻居拉快照块不是已经齐。那是不变量 375 item 1 余量 / 872。
- 请求用 height / format / chunk（从 0 起）认这块不是已经是同一份。那是不变量 375 item 2 余量 / 873。
- ListSnapshots 回了就已经齐。那是不变量 322。
- 全字段（含 Metadata）对上就已经装完。那是不变量 368。
- Offer 收下就已经装完。那是不变量 321。
