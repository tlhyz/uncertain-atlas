# 例：看见到了 H 不是已经 Prepare 带了扩展；看见 H+1 带了扩展不是已经是本高度刚签的；看见 h < H 带了扩展不是已经合法

**层次**：实现 / VoteExtensionsEnableHeight。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / Application configuration required to switch to ABCI 2.0。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「到了 H 不是已经 Prepare 带了扩展 / H+1 带了扩展不是已经是本高度刚签的 / h < H 带了扩展不是已经合法」，不是验签拒收整张预提交，也不是治理改 enable-height 会 panic。不要另写怎样设 VoteExtensionsEnableHeight 或怎样写空扩展。 330 veheight vs prepare bundled unbundling 续（746 + 747）；精读 [`worked-example-veheight-notprepare-vs-bundled.md`](worked-example-veheight-notprepare-vs-bundled.md)；[`worked-example-veheight-notthissigned-vs-bundled.md`](worked-example-veheight-notthissigned-vs-bundled.md)（不变量 747 item 2）。

## 官方三件事

规范把 `VoteExtensionsEnableHeight` 写成三件独立的实现事，不是「看见到了 H 就已经 Prepare 带了扩展、已经是本高度刚签的、已经合法」一件事：

1. **看见到了 H / 看见已经叫了 `ExtendVote` 不是已经 Prepare 带了扩展。**  
   官方写：到了配置高度 **H**，`PrepareProposal` **还不会**带投票扩展，但 **会** 调 `ExtendVote` 和 `VerifyVoteExtension`。看见高度到了 H，不是已经在 Prepare 里带了扩展。看见已经叫了 ExtendVote，不是已经把扩展写进本高提议。
2. **看见 H+1 的 `PrepareProposal` 带了扩展 不是已经是本高度刚签的扩展。**  
   官方写：到 **H+1**，`PrepareProposal` 才带 **高度 H** 的扩展。看见 H+1 带了扩展，不是已经是本高度刚签的那份。看见 Prepare 列表里有扩展，不是已经是这一高的 *e*。
3. **看见 `h < H` 的预提交带了扩展 不是已经合法，也不是已经启用。**  
   官方写：对所有高度 `h < H`，带投票扩展的预提交被当成畸形拒收。H 之后不能关，扩展必须签过且在场。看见 h < H 的票带了扩展，不是已经合法。看见字段在，不是已经切到 ABCI 2.0。

怎样设 `VoteExtensionsEnableHeight`、默认 `0`、怎样写空扩展是规范里的取值或做法，本页不抄。验签拒收整张预提交、空扩展仍验签是不变量 34，本页不抄。

## 官方为什么这样拆

- **到了 H ≠ 已经 Prepare 带了扩展：** 官方把开始叫 ExtendVote 和 Prepare 开始带扩展分开。
- **H+1 带了扩展 ≠ 已经是本高度刚签的：** 官方把带进来的扩展和本高度刚签的扩展分开。
- **h < H 带了扩展 ≠ 已经合法：** 官方把启用前带扩展的预提交和启用后必须在场的扩展分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 到了 H | 不是已经 Prepare 带了扩展 | 不是验签拒收整张预提交、空扩展仍验签（34） |
| H+1 带了扩展 | 不是已经是本高度刚签的 | 不是治理改 enable-height 会让未升级节点 panic（58） |
| h < H 带了扩展 | 不是已经合法 | 不是验证人集合 H+1 / H+2 / H+3（35） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「到了 H 就已经 Prepare 带了扩展、已经是本高度刚签的、已经合法」，必须分开到了 H 是不是已经 Prepare 带了扩展、H+1 带了扩展是不是已经是本高度刚签的、h < H 带了扩展是不是已经合法。可以跳过「看见到了 H 就已经切到 ABCI 2.0」。不要另写怎样设 VoteExtensionsEnableHeight 或怎样写空扩展。 330 veheight vs prepare bundled unbundling 续（746 + 747 item 2）。

## 本页不抄

- 怎样设 `VoteExtensionsEnableHeight`、默认 `0`、怎样写空扩展。
- 验签拒收整张预提交、空扩展仍验签、`s_h` 不得依赖本高收到的 *e*。那是不变量 34。
- 治理改 enable-height 会让未升级节点在开启高 panic。那是不变量 58。
- 验证人集合 H+1 / H+2 / H+3。那是不变量 35。
