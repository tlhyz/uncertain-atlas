# 例：看见 persist-context Historical blocks required is not already retain_height default 0 is pruning interchangeable / not already all-nodes-remove only statesync interchangeable / not already caution Historical blocks bundled interchangeable

**层次**：实现 / Commit Usage persist-context Historical blocks required not default 0 is pruning / not all-nodes-remove only statesync / not caution Historical blocks bundled 正式三事（481 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Commit Usage persist-context Historical blocks required not default 0 is pruning / not all-nodes-remove only statesync / not caution Historical blocks bundled 正式三事（481 余量）/ not 703 commitpersist-nothistorical interchangeable / not 481 commitpersist-vs-finalize bundled interchangeable」，不是 Commit Usage persist signal 正式三事 bundled（481），也不是 Commit Usage retain_height caution bundled（491）或 caution Historical blocks（694）。不要另写怎样填 retain_height。

## 官方三件事

1. **看见 Historical blocks may also be required for other purposes, e.g. auditing, replay of non-persisted heights, light client verification, and so on / 看见历史块还可能用于审计、回放没落盘高度、轻客户端验 / persist-context Historical blocks is not already 已经 retain_height defaults to 0 (retain all)（366） interchangeable / 366 retain interchangeable / 已经默认 0 就等于已经在剪 interchangeable，也不是已经 Commit Usage persist signal 正式三事 bundled（481） interchangeable / 703 commitpersist-nothistorical interchangeable / 701 commitpersist-notfinalize interchangeable / 481 commitpersist item 1 signal interchangeable，也不是已经 persist-context Historical blocks not default 0 is pruning / not all-nodes-remove only statesync / not caution Historical blocks bundled 正式三事 bundled（481 item 3 余量） interchangeable / 481 commitpersist item 3 interchangeable。**  
   官方把 persist signal 段里的 Historical blocks may also be required 和 retain_height 默认全留分开。看见 auditing / replay / light client，不是已经默认 0 就等于已经在剪 interchangeable——366 钉字段默认，本页从 481 item 3 侧钉 persist 语境 not default 0 单句。481 commitpersist vs finalize bundled unbundling 在本页 item 3 完成。

2. **看见 may also be required / 看见 persist 语境 other purposes / 看见 Usage 这句 is not already 已经全网删了就只有 state sync 能加新节点 interchangeable / 已经能剪就等于已经没有历史 interchangeable，也不是已经 Commit Usage persist signal 正式三事 bundled（481） interchangeable / 703 commitpersist-nothistorical interchangeable / 481 commitpersist item 2 expected interchangeable / 702 commitpersist-notempty interchangeable。**  
   官方把 persist 语境 other purposes 和全网删了就只有 state sync 路径分开——481 bundled 第三件事常与 366/323 混成「看见 may also be required 就已经能剪就等于没有历史 interchangeable」，本页钉 not all-nodes-remove only statesync 单句。看见 other purposes，不是已经切进共识就已经有完整历史 interchangeable——323 钉切进共识，本页钉 persist 语境。

3. **看见 persist 语境 Historical blocks required / 看见 Usage 这句 / auditing replay light client is not already 已经 Commit Usage retain_height caution bundled（491） interchangeable / 491 commitretaincaution interchangeable / 694 commitretaincaution-nothistorical interchangeable / 已经 caution 段 other purposes interchangeable，也不是已经 Commit Usage persist signal 正式三事 bundled（481） interchangeable / 703 commitpersist-nothistorical interchangeable / 701 commitpersist-notfinalize interchangeable。**  
   官方把 persist signal 段里的 Historical blocks 和 caution 段里的 Historical blocks 分开——481 bundled 第三件事常与 491/694 混成「看见 persist Historical blocks 就已经 caution Historical blocks bundled interchangeable」，本页钉 not caution Historical blocks bundled 单句。481 钉 persist 语境，491/694 钉 caution 语境。481 commitpersist vs finalize bundled unbundling 在本页 item 3 完成。

怎样落盘、怎样填 retain_height、怎样开 state sync 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **persist Historical blocks not default 0 is pruning ≠ 366 interchangeable：** 官方把 persist 语境 other purposes 和默认 0 就等于已经在剪分开。
- **persist Historical blocks not all-nodes-remove only statesync ≠ 能剪就等于没有历史 interchangeable：** 官方把 persist 语境 other purposes 和全网删了就只有 state sync 分开。
- **persist Historical blocks not caution Historical blocks bundled ≠ 491 / 694 interchangeable：** 官方把 persist 段 Historical blocks 和 caution 段 Historical blocks 分开；481 commitpersist vs finalize bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| persist-context Historical blocks required | 不是默认 0 就等于已经在剪（366） | 不是 caution Historical blocks（694/491 item 3） |
| 看见 may also be required | 不是全网删了就只有 state sync | 不是 persist signal 单句（701/481 item 1） |
| 看见 Usage 这句 | 不是 caution bundled（491） | 不是 expected at end of call（702/481 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage persist-context Historical blocks required not default 0 is pruning / not all-nodes-remove only statesync / not caution Historical blocks bundled 正式三事（481 余量），必须分开 persist 语境 Historical blocks 是不是默认 0 就等于已经在剪 interchangeable / 366、是不是全网删了就只有 state sync、是不是已经 caution Historical blocks bundled interchangeable / 491 / 694。可以跳过「看见叫了 Commit 就已经在剪」。不要另写怎样填 retain_height。481 commitpersist vs finalize bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样落盘、怎样填 retain_height、怎样开 state sync。
- Commit Usage persist signal 正式三事 bundled。那是不变量 481。
- Signal persist application state。那是不变量 481 item 1 余量 / 701。
- Expected persist at end of this call。那是不变量 481 item 2 余量 / 702。
- Commit Usage retain_height caution / caution Historical blocks。那是不变量 491 / 694。
- Commit 保留高度。那是不变量 366。
