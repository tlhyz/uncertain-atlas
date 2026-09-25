# 模式：把回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB not already 4mb / not already constant / not already restored 正式三事（375 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) LoadSnapshotChunk Usage。  
**例**：[有上限 not already 4mb ≠ bundled（375）](../../tracks/implementation/worked-example-loadchunk-not4mb-vs-bundled.md)。

## 三个名字

1. **有上限 不是 already 4mb：** 看见有上限 / 回包块含元数据不能超过 16 MB / 有 16 MB 上限，不是已经是快照报文 4 MB interchangeable / 已经 4mb interchangeable / 已经是快照报文 4 MB 交差 interchangeable，不是 375 loadchunk bundled interchangeable / loadchunk-sold-as-retrieved interchangeable。

2. **10 MB 不是 already constant：** 看见 10 MB / 10 MB 是个好起点 / 挑了 10 MB，不是已经是共识常数 interchangeable / 已经 constant interchangeable / 已经是共识常数交差 interchangeable，不是 872 loadchunk-notcomplete interchangeable / 873 loadchunk-notidentical interchangeable。

3. **回了字节 不是 already restored：** 看见回了字节 / 回了块字节 / 回包有字节，不是已经装完 interchangeable / 已经 restored interchangeable / 已经装完交差 interchangeable，不是 321 Offer restored interchangeable / 375 loadchunk item 1 interchangeable。

官方把有上限、不是已经是共识常数、不是已经装完写成三个名字。把它们叫成一个「看见有上限就已经是快照报文 4 MB interchangeable / 就已经是共识常数 interchangeable / 就已经装完 interchangeable」，会把 not already 4mb、not already constant、not already restored 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB not already 4mb / not already constant / not already restored 正式三事（375 余量），先数清问的是有上限 是不是 already 4mb / 375 / loadchunk-sold-as-retrieved，是不是 10 MB 是不是 already constant，还是回了字节 是不是 already restored，再决定要不要同一次发布。375 loadchunk-vs-retrieved bundled unbundling 在本页 item 3 完成。
