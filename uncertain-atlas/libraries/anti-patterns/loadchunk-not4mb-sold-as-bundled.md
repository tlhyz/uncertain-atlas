# 反模式：把回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB not already 4mb / not already constant / not already restored 正式三事（375 余量）说成已经是快照报文 4 MB / 已经是共识常数 / 已经装完

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[有上限 not already 4mb ≠ bundled（375）](../../tracks/implementation/worked-example-loadchunk-not4mb-vs-bundled.md)。

## 卖法

把有上限 / 回包块含元数据不能超过 16 MB / 有 16 MB 上限 写成已经是快照报文 4 MB interchangeable / 已经 4mb interchangeable / 已经是快照报文 4 MB 交差 interchangeable / 375 loadchunk bundled interchangeable / loadchunk-sold-as-retrieved interchangeable；把 10 MB / 10 MB 是个好起点 / 挑了 10 MB 写成已经是共识常数 interchangeable / 已经 constant interchangeable / 已经是共识常数交差 interchangeable；把回了字节 / 回了块字节 / 回包有字节 写成已经装完 interchangeable / 已经 restored interchangeable / 已经装完交差 interchangeable，或已经和 375 loadchunk bundled / loadchunk-sold-as-retrieved interchangeable / 874 loadchunk-not4mb interchangeable。

## 为什么错

官方把有上限、不是已经是共识常数、不是已经装完写成三件独立的实现事。把它们卖成 already 4mb interchangeable / already constant interchangeable / already restored interchangeable，会把 not already 4mb、not already constant、not already restored 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB not already 4mb / not already constant / not already restored 正式三事（375 余量），必须分开 not already 4mb、not already constant、not already restored 三件事，不要和 375 / 321 / 872 / 873 糊成一句。

## 和相邻反模式

- [loadchunk-sold-as-retrieved](loadchunk-sold-as-retrieved.md) 是 loadchunk bundled 全段，不是本页有上限 item 3 单句边界。
- [loadchunk-notcomplete-sold-as-bundled](loadchunk-notcomplete-sold-as-bundled.md) 是在拉 not already complete（375 item 1），不是本页 not already 4mb 边界。
- [loadchunk-notidentical-sold-as-bundled](loadchunk-notidentical-sold-as-bundled.md) 是填了三列 not already identical（375 item 2），不是本页 not already constant 边界。
- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是 Offer 收下就已经装完（321），不是本页 not already restored 单句。
