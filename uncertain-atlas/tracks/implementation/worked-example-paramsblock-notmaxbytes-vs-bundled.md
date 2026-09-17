# 例：看见 ConsensusParams.block 限制块大小和块间隔 is not already MaxBytes cap interchangeable / not already next_block_delay interchangeable / not already settled interchangeable

**层次**：实现 / ConsensusParams.block not already MaxBytes cap / not already next_block_delay / not already settled 正式三事（385 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ConsensusParams。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ConsensusParams.block not already MaxBytes cap / not already next_block_delay / not already settled 正式三事（385 余量）/ not 773 paramsblock-notmaxbytes interchangeable / not 385 paramsblock-vs-maxbytes bundled interchangeable」，不是 ConsensusParams 字段 bundled（385），也不是 -1 就按 100 MB 验就已经没有上限（337），也不是 ConsensusParams.evidence 就已经是证据 MaxBytes（386/770）。不要另写怎样写 ConsensusParams 字段。

## 官方三件事

1. **看见 ConsensusParams.`block` 限制块大小和块间隔 / 看见填了 block / ConsensusParams 这份块栏 is not already 已经是 MaxBytes 写成 -1 那种上限 interchangeable / 337 nocap interchangeable，也不是已经 ConsensusParams 字段 bundled（385） interchangeable / 773 paramsblock-notmaxbytes interchangeable / 774 paramsblock-notpubkey interchangeable / 385 paramsblock item 2 validator interchangeable，也不是已经 block not already MaxBytes cap / not already next_block_delay / not already settled 正式三事 bundled（385 item 1 余量） interchangeable / 385 paramsblock item 1 interchangeable。**  
   官方写：`block` 限制一块的大小和两块之间的时间。看见填了 block，不是已经是 MaxBytes 写成 -1 那种上限 interchangeable——本页从 385 item 1 侧钉 not already MaxBytes cap 单句。385 paramsblock vs maxbytes bundled unbundling 在本页 item 1 启动。

2. **看见填了 block / 看见能卡间隔 / ConsensusParams 这份块栏 is not already 已经是应用回的 `next_block_delay` interchangeable，也不是已经 ConsensusParams 字段 bundled（385） interchangeable / 773 paramsblock-notmaxbytes interchangeable / 385 paramsblock item 3 version interchangeable / 775 paramsblock-notappver interchangeable。**  
   官方把这一栏和已经是 next_block_delay 分开——385 bundled 第一件事常与 337 混成「看见填了 block 就已经是 MaxBytes 上限或已经是 next_block_delay interchangeable」，本页钉 not already next_block_delay 单句。

3. **看见填了 block / 看见有字段 / ConsensusParams 这份块栏 is not already 已经交差 interchangeable，也不是已经 ConsensusParams 字段 bundled（385） interchangeable / 773 paramsblock-notmaxbytes interchangeable / 774 paramsblock-notpubkey interchangeable。**  
   官方把能填 ConsensusParams.block 和已经交差分开。看见有字段，不是已经交差 interchangeable。385 paramsblock vs maxbytes bundled unbundling 在本页 item 1 启动。

怎样写 ConsensusParams、怎样选 MaxBytes、怎样限钥型是规范里的做法，本页不抄。

## 官方为什么这样拆

- **block not already MaxBytes cap ≠ 337 interchangeable：** 官方把这一栏和 MaxBytes 写成 -1 那种上限分开。
- **block not already next_block_delay ≠ 已经是 next_block_delay interchangeable：** 官方把能卡间隔和已经是应用回的 next_block_delay 分开。
- **block not already settled ≠ 已经交差 interchangeable：** 官方把有字段和已经交差分开；385 paramsblock vs maxbytes bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ConsensusParams.block 限制块大小和块间隔 | 不是已经是 MaxBytes 上限（337） | 不是 ConsensusParams.validator（774/385 item 2） |
| 看见填了 block | 不是已经是 next_block_delay | 不是 ConsensusParams.evidence（386/770） |
| 看见有字段 | 不是已经交差 | 不是 ConsensusParams 字段 bundled（385） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ConsensusParams.block not already MaxBytes cap / not already next_block_delay / not already settled 正式三事（385 余量），必须分开 block 是不是已经是 MaxBytes 上限 interchangeable / 337、是不是已经是 next_block_delay、是不是已经交差。可以跳过「看见填了 block 就已经是 MaxBytes 上限」。不要另写怎样写 ConsensusParams 字段。385 paramsblock vs maxbytes bundled unbundling 在本页 item 1 启动；续 [`worked-example-paramsblock-notpubkey-vs-bundled.md`](worked-example-paramsblock-notpubkey-vs-bundled.md)（不变量 774 item 2）。

## 本页不抄

- 怎样写 ConsensusParams、怎样选 MaxBytes、怎样限钥型。
- ConsensusParams 字段 bundled。那是不变量 385。
- ConsensusParams.validator。那是不变量 385 item 2 余量 / 774。
- ConsensusParams.version。那是不变量 385 item 3 余量 / 775。
- -1 就按 100 MB 验就已经没有上限。那是不变量 337。
- ConsensusParams.evidence 就已经是证据 MaxBytes。那是不变量 386 / 770。
