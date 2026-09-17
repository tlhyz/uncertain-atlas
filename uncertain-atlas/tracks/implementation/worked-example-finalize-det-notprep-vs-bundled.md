# 例：看见 Finalize 算出的状态必须只依赖上一份状态和决定块 is not already Prepare-style other values interchangeable / not already same ruler as Prepare interchangeable / not already settled interchangeable

**层次**：实现 / Finalize 算出的状态必须只依赖上一份状态和决定块 not already Prepare-style other values / not already same ruler as Prepare / not already settled 正式三事（342 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 11–12 [`FinalizeBlock`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize 算出的状态必须只依赖上一份状态和决定块 not already Prepare-style other values / not already same ruler as Prepare / not already settled 正式三事（342 余量）/ not 887 finalize-det-notprep interchangeable / not 342 finalize-det-vs-prepare bundled interchangeable」，不是 FinalizeBlock 确定性 bundled（342），也不是 Prepare 没有确定性要求（338），也不是回执已经交差。不要另写怎样写 FinalizeBlock。

## 官方三件事

1. **看见 `FinalizeBlock` 算出的状态必须只依赖上一份状态和决定块 / 看见必须确定 这份状态 is not already 已经可以像 Prepare 那样依赖其它值 interchangeable，也不是已经 FinalizeBlock 确定性 bundled（342） interchangeable / 887 finalize-det-notprep interchangeable / 888 finalize-det-notreceipt interchangeable / 342 finalize-det item 2 T_h interchangeable，也不是已经 Finalize 算出的状态必须只依赖上一份状态和决定块 not already Prepare-style other values / not already same ruler as Prepare / not already settled 正式三事 bundled（342 item 1 余量） interchangeable / 342 finalize-det item 1 interchangeable。**  
   官方写：正确进程 *p* 在高度 *h* 叫 `FinalizeBlock`，把决定块 *v_{p,h}* 交进去，造出状态 *s_{p,h}*。Requirement 11：*s_{p,h}* 只依赖 *s_{p,h-1}* 和 *v_{p,h}*。看见必须确定，不是已经可以依赖其它值或操作 interchangeable——本页从 342 item 1 侧钉 not already Prepare-style other values 单句。342 finalize-det vs prepare bundled unbundling 在本页 item 1 启动。

2. **看见只依赖上一份状态和决定块 / 看见 Finalize 回了 / 这份状态 is not already 已经和 Prepare / ExtendVote 同一把尺 interchangeable，也不是已经 FinalizeBlock 确定性 bundled（342） interchangeable / 887 finalize-det-notprep interchangeable / 342 finalize-det item 3 复制 interchangeable / 889 finalize-det-notprocess interchangeable，也不是已经 Prepare 没有确定性要求 interchangeable / 338 preparenondet interchangeable。**  
   官方把只依赖上一份状态和决定块和已经和「Prepare 没有确定性要求」同一句分开——342 bundled 第一件事常与 338 混成「看见必须确定就已经可以像 Prepare 那样或已经同一把尺 interchangeable」，本页钉 not already same ruler as Prepare 单句。

3. **看见 Finalize 回了 / 看见必须确定 / 这份状态 is not already 已经交差 interchangeable，也不是已经 FinalizeBlock 确定性 bundled（342） interchangeable / 887 finalize-det-notprep interchangeable / 888 finalize-det-notreceipt interchangeable，也不是已经造出 *s_h* 就已经落盘 interchangeable。**  
   官方把 Finalize 回了和已经交差分开。看见 Finalize 回了，不是已经交差 interchangeable。342 finalize-det vs prepare bundled unbundling 在本页 item 1 启动。

怎样写 `FinalizeBlock`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Finalize 算出的状态必须只依赖上一份状态和决定块 not already Prepare-style other values ≠ 已经可以像 Prepare 那样依赖其它值 interchangeable：** 官方把 Finalize 必须确定和 Prepare 可以不确定分开。
- **看见只依赖上一份状态和决定块 not already same ruler as Prepare ≠ 已经和 Prepare 同一把尺 interchangeable：** 官方把 Finalize 这把尺和 Prepare 没有确定性要求分开。
- **看见 Finalize 回了 not already settled ≠ 已经交差 interchangeable：** 官方把 Finalize 回了和已经交差分开；342 finalize-det vs prepare bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 算出的状态必须只依赖上一份状态和决定块 | 不是已经可以像 Prepare 那样依赖其它值 | 不是 Prepare 没有确定性要求（338） |
| 看见只依赖上一份状态和决定块 | 不是已经和 Prepare 同一把尺 | 不是结果列表已经同一顺序（316） |
| 看见 Finalize 回了 | 不是已经交差 | 不是结果必须确定就已经印进本头（888） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 算出的状态必须只依赖上一份状态和决定块 not already Prepare-style other values / not already same ruler as Prepare / not already settled 正式三事（342 余量），必须分开是不是已经可以像 Prepare 那样依赖其它值、是不是已经和 Prepare 同一把尺、是不是已经交差。可以跳过「看见必须确定就已经可以像 Prepare 那样」。不要把造出 *s_h* 当已经落盘。不要另写怎样写 FinalizeBlock。342 finalize-det vs prepare bundled unbundling 在本页 item 1 启动；续 [`worked-example-finalize-det-notreceipt-vs-bundled.md`](worked-example-finalize-det-notreceipt-vs-bundled.md)（不变量 888 item 2）。

## 本页不抄

- 怎样写 `FinalizeBlock`、怎样测确定性、怎样写测试向量。
- FinalizeBlock 确定性 bundled。那是不变量 342。
- Finalize 算出的结果必须只依赖上一份状态和决定块。那是不变量 342 item 2 余量 / 888。
- Prepare 没有确定性要求。那是不变量 338。
- 结果列表已经同一顺序。那是不变量 316。
