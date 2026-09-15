# 反模式：把 ProcessProposal read-only checks/processes not mutate committed 正式三事卖成 ProcessProposal 候选执行 bundled / 已经改了上一份已提交状态 / 已经 async 了还能 Reject

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ProcessProposal read-only checks/processes not mutate committed ≠ bundled](../../tracks/implementation/worked-example-proccand-readonly-notcommitted-vs-bundled.md)。

## 卖法

- 「看见 Application checks/processes the proposed block, which is read-only / 看见 read-only 处理 就已经改了上一份已提交状态 interchangeable / 已经 ProcessProposal 候选执行 bundled interchangeable。」
- 「看见 checks/processes 就已经立刻执行交差 interchangeable / 已经 Process MAY fully execute interchangeable / 已经 immediate execution 交差 interchangeable。」
- 「看见 read-only 处理 就已经 async 了还能 Reject interchangeable / 已经 Process 调用是同步的 interchangeable。」

## 为什么错

官方把 read-only checks/processes not mutate committed、read-only not immediate execution committed、read-only not async can still Reject 写成三件独立的实现事。把它们卖成 ProcessProposal 候选执行 bundled、已经改了上一份已提交状态、已经 async 了还能 Reject，会把 Req 9 mutate committed、MAY execute committed、async can still Reject 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal read-only checks/processes not mutate committed 正式三事，必须分开 read-only checks/processes not mutate committed、read-only not immediate execution committed、read-only not async can still Reject 三个名字，不要把它们卖成 ProcessProposal 候选执行 bundled / 已经改了上一份已提交状态 / 已经 async 了还能 Reject。

## 和相邻反模式

- [proccand-sold-as-commit](proccand-sold-as-commit.md) 是 452 bundled 三事专用，不是本页 read-only checks/processes 单句边界。
- [req9noside-sold-as-commit](req9noside-sold-as-commit.md) 是四门不得改已提交状态 bundled，不是本页 read-only not mutate committed 边界。
- [proccand-candidate-notcommitted-sold-as-bundled](proccand-candidate-notcommitted-sold-as-bundled.md) 是 candidate state not committed 单句边界，不是本页 read-only 边界。
