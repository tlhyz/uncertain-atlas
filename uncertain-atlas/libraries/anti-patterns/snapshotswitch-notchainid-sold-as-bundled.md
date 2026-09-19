# 反模式：把装完不是已经有了 ChainID not already has-ChainID / not already can-propose / not already genesis-RPC-checked 正式三事（323 余量）说成已经有了这些 / 已经能出块 / 已经和轻客户端对过

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[装完 not already has-ChainID ≠ bundled（323）](../../tracks/implementation/worked-example-snapshotswitch-notchainid-vs-bundled.md)。

## 卖法

把装完 / 快照已经装完 / 状态机已经恢复 写成已经有了 ChainID、参数、集合和头 interchangeable / 已经 has-ChainID interchangeable / 已经引导信息交差 interchangeable / 323 snapshotswitch bundled interchangeable / 33 four gates interchangeable / snapshotswitch-sold-as-full-history interchangeable；把状态机在 / 状态机已经恢复 / 装完之后 写成已经能出块 interchangeable / 已经 can-propose interchangeable；把有创世文件 / 要从创世文件再凑 / 还要轻客户端 RPC 写成已经和轻客户端那份对过 interchangeable / 已经 genesis-RPC-checked interchangeable，或已经和 323 snapshotswitch bundled / snapshotswitch-sold-as-full-history interchangeable / 725 snapshotswitch-notchainid interchangeable。

## 为什么错

官方把装完单句、already has-ChainID、already can-propose、already genesis-RPC-checked 写成三件独立的实现事。把它们卖成 already has-ChainID interchangeable / already can-propose interchangeable / already genesis-RPC-checked interchangeable，会把 not already has-ChainID、not already can-propose、not already genesis-RPC-checked 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看装完不是已经有了 ChainID not already has-ChainID / not already can-propose / not already genesis-RPC-checked 正式三事（323 余量），必须分开 not already has-ChainID、not already can-propose、not already genesis-RPC-checked 三件事，不要和 323 / 33 / 321 / 726 / 727 / 38 / 314 糊成一句。

## 和相邻反模式

- [snapshotswitch-sold-as-full-history](snapshotswitch-sold-as-full-history.md) 是 Transition to Consensus bundled 全段，不是本页装完 item 1 单句边界。
- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是 Offer 收下已经装完（321），不是本页再凑引导信息边界。
- [snapshotdiscover-notstop-sold-as-bundled](snapshotdiscover-notstop-sold-as-bundled.md) 是 Discovery Offer 被拒（322），不是本页切共识边界。
