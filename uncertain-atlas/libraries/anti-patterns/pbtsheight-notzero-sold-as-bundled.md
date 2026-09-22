# 反模式：把写成 0 不是已经启用 PBTS not already enabled / not already precision-pbts / not already switched 正式三事（343 余量）说成已经启用 PBTS / 已经填了 Precision 就是 PBTS / 已经切到 PBTS

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[写成 0 not already enabled ≠ bundled（343）](../../tracks/implementation/worked-example-pbtsheight-notzero-vs-bundled.md)。

## 卖法

把写成 0 / 大于 0 才是启用高度 / `PbtsEnableHeight` 写成已经启用 PBTS interchangeable / 已经 enabled interchangeable / 已经启用交差 interchangeable / 343 pbtsheight bundled interchangeable / pbtsheight-sold-as-enabled interchangeable；把填了 Precision / MessageDelay / 同步参数在 写成已经填了 Precision 就是 PBTS interchangeable / 已经 precision-pbts interchangeable / 已经同步参数交差 interchangeable；把字段在 / 配置里有 PbtsEnableHeight 写成已经切算法 interchangeable / 已经 switched interchangeable / 已经切到 PBTS 交差 interchangeable，或已经和 343 pbtsheight bundled / pbtsheight-sold-as-enabled interchangeable / 782 pbtsheight-notzero interchangeable。

## 为什么错

官方把 0 表示关掉、同步参数两把尺、字段在配置里写成三件独立的实现事。把它们卖成 already enabled interchangeable / already precision-pbts interchangeable / already switched interchangeable，会把 not already enabled、not already precision-pbts、not already switched 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看写成 0 不是已经启用 PBTS not already enabled / not already precision-pbts / not already switched 正式三事（343 余量），必须分开 not already enabled、not already precision-pbts、not already switched 三件事，不要和 343 / 336 / 761 / 762 / 783 / 784 糊成一句。

## 和相邻反模式

- [pbtsheight-notbfttime-sold-as-bundled](pbtsheight-notbfttime-sold-as-bundled.md) 是 H 之前仍用 BFT Time ≠ 已经切到 PBTS（343 item 2），不是本页写成 0 item 1 单句边界。
- [pbtsheight-sold-as-enabled](pbtsheight-sold-as-enabled.md) 是 PbtsEnableHeight bundled 全段，不是本页写成 0 item 1 单句边界。
- [precision-sold-as-msgdelay](precision-sold-as-msgdelay.md) 是 Precision 不是已经是 MessageDelay（336 / 761），不是本页填了 Precision ≠ PBTS 边界。
- [pbts-sold-as-mtp](pbts-sold-as-mtp.md) 是块时间必须点名算法（40），不是本页字段在 ≠ 已经切算法 边界。
- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是到了 H 不是已经 Prepare 带了扩展（330），不是本页写成 0 边界。
