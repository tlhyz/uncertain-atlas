# 反模式：把 H 之前仍用 BFT Time 不是已经切到 PBTS not already switched-to-pbts / not already mtp / not already clock-changed 正式三事（343 余量）说成已经切到 PBTS / 已经是 MTP / 已经换完钟

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[H 之前仍用 BFT Time not already switched-to-pbts ≠ bundled（343）](../../tracks/implementation/worked-example-pbtsheight-notbfttime-vs-bundled.md)。

## 卖法

把 H 之前或写成 0 仍用 BFT Time / 到了 H 才用 PBTS / 旧钟还在 写成已经切到 PBTS interchangeable / 已经 switched-to-pbts interchangeable / 已经切到 PBTS 交差 interchangeable / 343 pbtsheight bundled interchangeable / pbtsheight-sold-as-enabled interchangeable；把到了 H / 写了用于 PBTS / 配置高度到了 写成已经是 MTP interchangeable / 已经 mtp interchangeable / 已经中位数时间交差 interchangeable；把还能出合法提案 / 仍能出合法提案 写成已经换完钟 interchangeable / 已经 clock-changed interchangeable / 已经换钟交差 interchangeable，或已经和 343 pbtsheight bundled / pbtsheight-sold-as-enabled interchangeable / 783 pbtsheight-notbfttime interchangeable。

## 为什么错

官方把旧钟还在、到了启用高度、还能提案写成三件独立的实现事。把它们卖成 already switched-to-pbts interchangeable / already mtp interchangeable / already clock-changed interchangeable，会把 not already switched-to-pbts、not already mtp、not already clock-changed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 H 之前仍用 BFT Time 不是已经切到 PBTS not already switched-to-pbts / not already mtp / not already clock-changed 正式三事（343 余量），必须分开 not already switched-to-pbts、not already mtp、not already clock-changed 三件事，不要和 343 / 40 / 782 / 784 / 330 糊成一句。

## 和相邻反模式

- [pbtsheight-notzero-sold-as-bundled](pbtsheight-notzero-sold-as-bundled.md) 是写成 0 ≠ 已启用（343 item 1），不是本页 H 之前仍用 BFT Time item 2 单句边界。
- [pbtsheight-notveheight-sold-as-bundled](pbtsheight-notveheight-sold-as-bundled.md) 是启用之后不能关 ≠ 扩展启用高度那种切换（343 item 3），不是本页 H 之前仍用 BFT Time item 2 单句边界。
- [pbtsheight-sold-as-enabled](pbtsheight-sold-as-enabled.md) 是 PbtsEnableHeight bundled 全段，不是本页 item 2 单句边界。
- [pbts-sold-as-mtp](pbts-sold-as-mtp.md) 是块时间必须点名算法（40），不是本页到了 H ≠ 已经是 MTP 边界。
- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是到了 H 不是已经 Prepare 带了扩展（330），不是本页旧钟还在边界。
