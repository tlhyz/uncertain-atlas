# 例：看见 ListSnapshots 回了不是已经有了全部快照；看见挑了最高不是已经收下；看见 Offer 被拒不是已经停

**层次**：实现 / Snapshot Discovery。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Discovery。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「ListSnapshots 回了不是已经有了全部快照 / 挑了最高不是已经收下 / Offer 被拒不是已经停」，不是 Offer 收下已经装完，也不是只有 AppHash 可信任。不要另写怎样列快照或怎样挑。

## 官方三件事

规范把快照发现写成三件独立的实现事，不是「看见问了邻居就已经有了全部快照、已经收下、已经停」一件事：

1. **看见问了邻居 / 看见 ListSnapshots 回了 不是已经有了全部快照，也不是已经没有上限。**  
   官方写：空节点进网之后，会问所有邻居用 `ListSnapshots` 报快照，**每个节点限 10 份**。看见问了，不是已经齐。看见回了，不是已经没有上限。看见 10，不是已经是不确定默认。
2. **看见挑了最高 / 看见按高度、格式、邻居数排了 不是已经是应用收下的那份，也不是已经装完。**  
   官方写：过一段时间，节点挑一份最合适的（一般按高度、格式、有多少邻居），再经 `OfferSnapshot` 交给应用。看见挑了，不是已经收下。看见最高，不是已经装完。看见排过了，不是已经是应用要的格式。
3. **看见 Offer 被拒 / 看见拒了格式或邻居 不是已经没有快照，也不是已经停。**  
   官方写：应用可以收下、拒掉、拒这种格式、拒这个邻居，以及别的回法。CometBFT **会继续发现并继续 Offer**，直到有一份被收下，或应用中止。看见被拒，不是已经没有快照。看见拒了邻居，不是已经停。看见能中止，不是已经发现完。

怎样实现 `ListSnapshots`、怎样挑、把 10 当产品常数是规范里的取值或做法，本页不抄。Offer 收下已经装完是不变量 321，本页不抄。

## 官方为什么这样拆

- **ListSnapshots 回了 ≠ 已经有了全部快照：** 官方把每节点 10 份上限和已经齐分开。
- **挑了最高 ≠ 已经收下：** 官方把本地挑选和 Offer 交给应用分开。
- **Offer 被拒 ≠ 已经停：** 官方把继续发现和应用中止分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ListSnapshots 回了 | 不是已经有了全部快照 | 不是 Offer 收下已经装完（321） |
| 挑了最高 | 不是已经收下 | 不是只有 AppHash 可信任（38） |
| Offer 被拒 | 不是已经停 | 不是启动对齐已经是快照重放（314） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「已经在发现快照」，必须分开 ListSnapshots 回了是不是已经有了全部快照、挑了最高是不是已经收下、Offer 被拒是不是已经停。可以跳过「看见问了就已经齐」。不要另写怎样列快照或怎样挑。不要把每节点 10 份当不确定默认。322 snapshotdiscover vs offer bundled unbundling 续（722 + 723）；精读 [`worked-example-snapshotdiscover-notall-vs-bundled.md`](worked-example-snapshotdiscover-notall-vs-bundled.md)（不变量 722 item 1）；[`worked-example-snapshotdiscover-notaccepted-vs-bundled.md`](worked-example-snapshotdiscover-notaccepted-vs-bundled.md)（不变量 723 item 2）。

## 本页不抄

- 怎样实现 `ListSnapshots`、怎样挑、把 10 当产品常数。
- Offer 收下已经装完。那是不变量 321。
- 只有 AppHash 可信任。那是不变量 38。
- 启动对齐当快照重放。那是不变量 314。
