# 例：看见 Verify 必须只依赖扩展、这块和上一份状态 is not already ExtendVote-style other values interchangeable / not already same ruler as ExtendVote interchangeable / not already settled interchangeable

**层次**：实现 / Verify 必须只依赖扩展、这块和上一份状态 not already ExtendVote-style other values / not already same ruler as ExtendVote / not already settled 正式三事（341 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 7–8 [`VerifyVoteExtension`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Verify 必须只依赖扩展、这块和上一份状态 not already ExtendVote-style other values / not already same ruler as ExtendVote / not already settled 正式三事（341 余量）/ not 890 verify-det-notext interchangeable / not 341 verify-det-vs-extend bundled interchangeable」，不是 VerifyVoteExtension 确定性 bundled（341），也不是 ExtendVote 没有确定性要求（338），也不是验签拒收已经是块非法（34）。不要另写怎样写 VerifyVoteExtension。

## 官方三件事

1. **看见 `VerifyVoteExtension` 必须只依赖扩展、这块和上一份状态 / 看见必须确定 这份确定 is not already 已经可以像 ExtendVote 那样依赖其它值 interchangeable，也不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable / 890 verify-det-notext interchangeable / 891 verify-det-nothonest interchangeable / 341 verify-det item 2 任意扩展 interchangeable，也不是已经 Verify 必须只依赖扩展、这块和上一份状态 not already ExtendVote-style other values / not already same ruler as ExtendVote / not already settled 正式三事 bundled（341 item 1 余量） interchangeable / 341 verify-det item 1 interchangeable。**  
   官方写：`VerifyVoteExtension` 是当前状态、收到的扩展、以及扩展所指那份提案的确定函数。正确进程 *p* 对任意扩展 *e* 和任意块 *w* 叫 Verify，Accept 或 Reject 只依赖 *e*、*w* 和 *s_{p,h-1}*。看见必须确定，不是已经可以依赖其它值或操作 interchangeable——本页从 341 item 1 侧钉 not already ExtendVote-style other values 单句。341 verify-det vs extend bundled unbundling 在本页 item 1 启动。

2. **看见只依赖扩展、这块和上一份状态 / 看见 Verify 回了 / 这份确定 is not already 已经和 ExtendVote 同一把尺 interchangeable，也不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable / 890 verify-det-notext interchangeable / 341 verify-det item 3 活性 interchangeable / 892 verify-det-notsafety interchangeable，也不是已经 ExtendVote 没有确定性要求 interchangeable / 338 extendnondet interchangeable。**  
   官方把只依赖扩展、这块和上一份状态和已经和「ExtendVote 没有确定性要求」同一句分开——341 bundled 第一件事常与 338 混成「看见必须确定就已经可以像 ExtendVote 那样或已经同一把尺 interchangeable」，本页钉 not already same ruler as ExtendVote 单句。

3. **看见 Verify 回了 / 看见必须确定 / 这份确定 is not already 已经交差 interchangeable，也不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable / 890 verify-det-notext interchangeable / 891 verify-det-nothonest interchangeable，也不是已经验签拒收已经是块非法 interchangeable / 34 sig-reject interchangeable。**  
   官方把 Verify 回了和已经交差分开。看见 Verify 回了，不是已经交差 interchangeable。341 verify-det vs extend bundled unbundling 在本页 item 1 启动。

怎样写 `VerifyVoteExtension`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Verify 必须只依赖扩展、这块和上一份状态 not already ExtendVote-style other values ≠ 已经可以像 ExtendVote 那样依赖其它值 interchangeable：** 官方把 Verify 必须确定和 ExtendVote 可以不确定分开。
- **看见只依赖扩展、这块和上一份状态 not already same ruler as ExtendVote ≠ 已经和 ExtendVote 同一把尺 interchangeable：** 官方把 Verify 这把尺和 ExtendVote 没有确定性要求分开。
- **看见 Verify 回了 not already settled ≠ 已经交差 interchangeable：** 官方把 Verify 回了和已经交差分开；341 verify-det vs extend bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Verify 必须只依赖扩展、这块和上一份状态 | 不是已经可以像 ExtendVote 那样依赖其它值 | 不是 ExtendVote 没有确定性要求（338） |
| 看见只依赖扩展、这块和上一份状态 | 不是已经和 ExtendVote 同一把尺 | 不是验签拒收已经是块非法（34） |
| 看见 Verify 回了 | 不是已经交差 | 不是两边对任意扩展同一裁决（891） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Verify 必须只依赖扩展、这块和上一份状态 not already ExtendVote-style other values / not already same ruler as ExtendVote / not already settled 正式三事（341 余量），必须分开是不是已经可以像 ExtendVote 那样依赖其它值、是不是已经和 ExtendVote 同一把尺、是不是已经交差。可以跳过「看见必须确定就已经可以像 ExtendVote 那样」。不要另写怎样写 VerifyVoteExtension。341 verify-det vs extend bundled unbundling 在本页 item 1 启动；续 [`worked-example-verify-det-nothonest-vs-bundled.md`](worked-example-verify-det-nothonest-vs-bundled.md)（不变量 891 item 2）。

## 本页不抄

- 怎样写 `VerifyVoteExtension`、怎样测确定性、怎样写测试向量。
- VerifyVoteExtension 确定性 bundled。那是不变量 341。
- 两边对任意扩展同一裁决。那是不变量 341 item 2 余量 / 891。
- ExtendVote 没有确定性要求。那是不变量 338。
- 验签拒收已经是块非法。那是不变量 34。
