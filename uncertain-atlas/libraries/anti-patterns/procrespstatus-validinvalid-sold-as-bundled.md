# 反模式：把 ProcessProposal Response status valid/invalid 正式三事卖成 Process 回包栏 bundled / 已经当成块非法 / 已经不能整块执行候选

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[status valid/invalid ≠ bundled](../../tracks/implementation/worked-example-procrespstatus-validinvalid-vs-bundled.md)。

## 卖法

- 「看见 ProcessProposalResponse.status 是应用认为这份提案合法还是非法 就已经 Process 回包栏 bundled interchangeable / 已经当成块非法 interchangeable。」
- 「看见 REJECT 时共识 assumes not valid 就已经 Verify REJECT whole vote interchangeable / 已经当成块非法 interchangeable。」
- 「看见 REJECT 就已经不能整块执行候选 interchangeable / 已经 Process MAY 整块执行就意味着已经交差 interchangeable。」

## 为什么错

官方把 status valid/invalid、REJECT assumes not valid not block invalid、REJECT not can't execute candidate 写成三件独立的实现事。把它们卖成 Process 回包栏 bundled、已经当成块非法、已经不能整块执行候选，会把 status 语义、assumes not valid、candidate 可执行三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Response status valid/invalid 正式三事，必须分开 status valid/invalid、REJECT assumes not valid not block invalid、REJECT not can't execute candidate 三个名字，不要把它们卖成 Process 回包栏 bundled / 已经当成块非法 / 已经不能整块执行候选。

## 和相邻反模式

- [procrespstatus-sold-as-procstatus](procrespstatus-sold-as-procstatus.md) 是 430 bundled 三事专用；本页是 status valid/invalid 单句边界。
- [procreject-sold-as-invalid](procreject-sold-as-invalid.md) 是 455 REJECT consensus assume 专用，不是本页 Response status 语义边界。
- [proposalstatus-sold-as-prevote](proposalstatus-sold-as-prevote.md) 是 ProposalStatus 376 专用，不是本页 Response status 边界。
