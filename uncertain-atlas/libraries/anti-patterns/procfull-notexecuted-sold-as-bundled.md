# 反模式：把 ProcessProposal Contains all information not already executed 正式三事卖成 ProcessProposal 含执行所需全部信息 bundled / 已经执行那些交易 / 已经 Finalize 跑过

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ProcessProposal Contains all information not already executed ≠ bundled](../../tracks/implementation/worked-example-procfull-notexecuted-vs-bundled.md)。

## 卖法

- 「看见 ProcessProposal Contains all information on the proposed block needed to fully execute it / 看见含执行所需全部信息 就已经执行那些交易 interchangeable / 已经 Finalize 跑过 interchangeable / 已经 ProcessProposal 含执行所需全部信息 bundled interchangeable。」
- 「看见含执行所需全部信息 就已经 Process MAY 整块执行交差 interchangeable / 已经 immediate execution 交差 interchangeable / 已经是 ExecuteTxState interchangeable。」
- 「看见含执行所需全部信息 就已经 read-only 处理交差 interchangeable / 已经 checks/processes 就已经执行那些交易 interchangeable / 已经 Process 回了 ACCEPT 就交差 interchangeable。」

## 为什么错

官方把 Contains all information needed to fully execute、Process MAY fully execute not committed、read-only checks/processes 写成三件独立的实现事。把它们卖成 ProcessProposal 含执行所需全部信息 bundled、已经执行那些交易、已经 Finalize 跑过，会把 already executed、MAY execute committed、read-only settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Contains all information not already executed 正式三事，必须分开 Contains all information not already executed、Contains all information not MAY execute committed、Contains all information not read-only settled 三个名字，不要把它们卖成 ProcessProposal 含执行所需全部信息 bundled / 已经执行那些交易 / 已经 Finalize 跑过。

## 和相邻反模式

- [procfull-sold-as-execute](procfull-sold-as-execute.md) 是 453 bundled 三事专用，不是本页 Contains all information not already executed 单句边界。
- [proccand-mayexecute-notcommitted-sold-as-bundled](proccand-mayexecute-notcommitted-sold-as-bundled.md) 是 MAY execute not committed 单句边界，不是本页 Contains all information 边界。
- [proccand-readonly-notcommitted-sold-as-bundled](proccand-readonly-notcommitted-sold-as-bundled.md) 是 read-only checks/processes 单句边界，不是本页 Contains all information 边界。
