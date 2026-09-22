# 例：看见写成 0 不是已经启用 PBTS 不是已经填了 Precision 就是 PBTS；看见 H 之前仍用 BFT Time 不是已经切到 PBTS；看见启用之后不能关不是已经是扩展启用高度那种切换

**层次**：实现 / PbtsEnableHeight。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / FeatureParams.PbtsEnableHeight。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「写成 0 不是已经启用 PBTS 不是已经填了 Precision 就是 PBTS / H 之前仍用 BFT Time 不是已经切到 PBTS / 启用之后不能关不是已经是扩展启用高度那种切换」，不是 Precision 已经是 MessageDelay，也不是到了 H 已经 Prepare 带了扩展。不要另写怎样设 PbtsEnableHeight。343 pbtsheight vs params bundled unbundling 完成（782+783+784）；精读 [`worked-example-pbtsheight-notzero-vs-bundled.md`](worked-example-pbtsheight-notzero-vs-bundled.md)（不变量 782 item 1）、[`worked-example-pbtsheight-notbfttime-vs-bundled.md`](worked-example-pbtsheight-notbfttime-vs-bundled.md)（不变量 783 item 2）、[`worked-example-pbtsheight-notveheight-vs-bundled.md`](worked-example-pbtsheight-notveheight-vs-bundled.md)（不变量 784 item 3）。

## 官方三件事

规范把 PBTS 启用高度写成三件独立的实现事，不是「看见填了同步参数就已经启用、已经切到 PBTS、已经能关」一件事：

1. **看见写成 0 / 看见大于 0 才是启用高度 不是已经启用 PBTS，也不是已经填了 Precision 就是 PBTS。**  
   官方写：`PbtsEnableHeight` 要么是 0，要么是一个正高度。**0 表示 PBTS 关掉**。大于 0 才标出将要（或已经）启用的那一高。看见写成 0，不是已经启用。看见填了 Precision / MessageDelay，不是已经到了这个高度。看见字段在，不是已经切算法。
2. **看见 H 之前或写成 0 仍用 BFT Time / 看见到了 H 才用 PBTS 不是已经切到 PBTS，也不是已经是 MTP。**  
   官方写：到了配置高度，并且之后每一高，才用 PBTS 算法出时间戳、验时间戳。**这一高之前，或这个值是 0**，仍用旧的 BFT Time。看见写了用于 PBTS，不是已经切了。看见到了 H，不是已经是中位数时间。看见还能出合法提案，不是已经换完钟。
3. **看见启用之后不能关 / 看见不能写成当前高度或更矮 不是已经是扩展启用高度那种切换，也不是已经能关。**  
   官方写：PBTS 一旦启用就不能关。不能写成低于或等于当前链高度。必须 `PbtsEnableHeight > [当前高度]`。看见不能关，不是已经是到了 H 才开始叫 ExtendVote 那种切换。看见必须比当前高，不是已经能改回 0。看见字段锁死，不是已经 Prepare 带了扩展。

怎样设 `PbtsEnableHeight`、默认取值、怎样选启用高度是规范里的做法，本页不抄。Precision 不是 MessageDelay 是不变量 336，本页不抄。

## 官方为什么这样拆

- **写成 0 不是已经启用 PBTS ≠ 已经填了 Precision 就是 PBTS：** 官方把关掉取值和同步参数两把尺分开。
- **H 之前仍用 BFT Time ≠ 已经切到 PBTS：** 官方把旧钟和新钟哪一高换分开。
- **启用之后不能关 ≠ 已经是扩展启用高度那种切换：** 官方把时间戳算法锁死和投票扩展切换分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 写成 0 不是已经启用 PBTS | 不是已经填了 Precision 就是 PBTS | 不是 Precision 已经是 MessageDelay（336） |
| H 之前仍用 BFT Time | 不是已经切到 PBTS | 不是块时间必须点名算法（40） |
| 启用之后不能关 | 不是已经是扩展启用高度那种切换 | 不是到了 H 已经 Prepare 带了扩展（330） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了同步参数就已经启用、已经切到 PBTS、已经能关」，必须分开写成 0 不是已经启用 PBTS 是不是已经填了 Precision 就是 PBTS、H 之前仍用 BFT Time 是不是已经切到 PBTS、启用之后不能关是不是已经是扩展启用高度那种切换。可以跳过「看见填了同步参数就已经启用」。不要把写成 0 当已经切到 PBTS。不要另写怎样设 PbtsEnableHeight。343 pbtsheight vs params bundled unbundling 完成（782+783+784）。

## 本页不抄

- 怎样设 `PbtsEnableHeight`、默认取值、怎样选启用高度。
- Precision 已经是 MessageDelay。那是不变量 336。
- 到了 H 已经 Prepare 带了扩展。那是不变量 330。
- 块时间必须点名算法。那是不变量 40。
