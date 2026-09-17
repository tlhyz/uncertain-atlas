# 例：看见 Process 必须只依赖请求和上一份状态 is not already Prepare-style other values interchangeable / not already same ruler as Prepare interchangeable / not already settled interchangeable

**层次**：实现 / Process 必须只依赖请求和上一份状态 not already Prepare-style other values / not already same ruler as Prepare / not already settled 正式三事（340 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 4–5 [`ProcessProposal`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Process 必须只依赖请求和上一份状态 not already Prepare-style other values / not already same ruler as Prepare / not already settled 正式三事（340 余量）/ not 893 process-det-notprep interchangeable / not 340 process-det-vs-prepare bundled interchangeable」，不是 ProcessProposal 确定性 bundled（340），也不是 Prepare 没有确定性要求（338），也不是四门已经结算（33）。不要另写怎样写 ProcessProposal。

## 官方三件事

1. **看见 `ProcessProposal` 必须只依赖本次请求和 `s_{h-1}` / 看见必须确定 这份确定 is not already 已经可以像 Prepare 那样依赖其它值 interchangeable，也不是已经 ProcessProposal 确定性 bundled（340） interchangeable / 893 process-det-notprep interchangeable / 894 process-det-nothonest interchangeable / 340 process-det item 2 任意块 interchangeable，也不是已经 Process 必须只依赖请求和上一份状态 not already Prepare-style other values / not already same ruler as Prepare / not already settled 正式三事 bundled（340 item 1 余量） interchangeable / 340 process-det item 1 interchangeable。**  
   官方写：`ProcessProposal` 是当前状态和即将应用的那块的确定函数。正确进程 *p* 对任意块 *u* 叫 Process，Accept 或 Reject 只依赖 *u* 和 *s_{p,h-1}*。看见必须确定，不是已经可以依赖其它值或操作 interchangeable——本页从 340 item 1 侧钉 not already Prepare-style other values 单句。340 process-det vs prepare bundled unbundling 在本页 item 1 启动。

2. **看见只依赖请求和上一份状态 / 看见 Process 回了 / 这份确定 is not already 已经和 Prepare / ExtendVote 同一把尺 interchangeable，也不是已经 ProcessProposal 确定性 bundled（340） interchangeable / 893 process-det-notprep interchangeable / 340 process-det item 3 无解 interchangeable / 895 process-det-notfix interchangeable，也不是已经 Prepare 没有确定性要求 interchangeable / 338 preparenondet interchangeable。**  
   官方把只依赖请求和上一份状态和已经和「Prepare 没有确定性要求」同一句分开——340 bundled 第一件事常与 338 混成「看见必须确定就已经可以像 Prepare 那样或已经同一把尺 interchangeable」，本页钉 not already same ruler as Prepare 单句。

3. **看见 Process 回了 / 看见必须确定 / 这份确定 is not already 已经交差 interchangeable，也不是已经 ProcessProposal 确定性 bundled（340） interchangeable / 893 process-det-notprep interchangeable / 894 process-det-nothonest interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把 Process 回了和已经交差分开。看见 Process 回了，不是已经交差 interchangeable。340 process-det vs prepare bundled unbundling 在本页 item 1 启动。

怎样写 `ProcessProposal`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Process 必须只依赖请求和上一份状态 not already Prepare-style other values ≠ 已经可以像 Prepare 那样依赖其它值 interchangeable：** 官方把 Process 必须确定和 Prepare 可以不确定分开。
- **看见只依赖请求和上一份状态 not already same ruler as Prepare ≠ 已经和 Prepare 同一把尺 interchangeable：** 官方把 Process 这把尺和 Prepare 没有确定性要求分开。
- **看见 Process 回了 not already settled ≠ 已经交差 interchangeable：** 官方把 Process 回了和已经交差分开；340 process-det vs prepare bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Process 必须只依赖请求和上一份状态 | 不是已经可以像 Prepare 那样依赖其它值 | 不是 Prepare 没有确定性要求（338） |
| 看见只依赖请求和上一份状态 | 不是已经和 Prepare 同一把尺 | 不是四门已经结算（33） |
| 看见 Process 回了 | 不是已经交差 | 不是两边对任意块同一裁决（894） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 必须只依赖请求和上一份状态 not already Prepare-style other values / not already same ruler as Prepare / not already settled 正式三事（340 余量），必须分开是不是已经可以像 Prepare 那样依赖其它值、是不是已经和 Prepare 同一把尺、是不是已经交差。可以跳过「看见必须确定就已经可以像 Prepare 那样」。不要另写怎样写 ProcessProposal。340 process-det vs prepare bundled unbundling 在本页 item 1 启动；续 [`worked-example-process-det-nothonest-vs-bundled.md`](worked-example-process-det-nothonest-vs-bundled.md)（不变量 894 item 2）。

## 本页不抄

- 怎样写 `ProcessProposal`、怎样测确定性、怎样写测试向量。
- ProcessProposal 确定性 bundled。那是不变量 340。
- 两边对任意块同一裁决。那是不变量 340 item 2 余量 / 894。
- Prepare 没有确定性要求。那是不变量 338。
- 四门已经结算。那是不变量 33。
