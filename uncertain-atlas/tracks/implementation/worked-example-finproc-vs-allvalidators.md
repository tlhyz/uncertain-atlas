# 例：看见 When calling FinalizeBlock with a block / consensus algorithm guarantees 不是已经每个验证者都跑过 Process / 已经把块落成决定；看见 at least one non-byzantine validator 不是已经提议者那边 Process 过就代表全网都 Process 过；看见 has run ProcessProposal on that block 不是已经套用 candidate / 先前跑过就不需要 Process 保证

**层次**：实现 / FinalizeBlock When calling ProcessProposal guarantee 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「When calling FinalizeBlock / consensus algorithm guarantees 不是已经每个验证者都跑过 Process / 已经把块落成决定 / at least one non-byzantine validator 不是已经提议者那边 Process 过就代表全网都 Process 过 / has run ProcessProposal on that block 不是已经套用 candidate / 先前跑过就不需要 Process 保证」，不是 Finalize 时的 Process 保证 bundled 三事，也不是 FinalizeBlock When Application executes block v 正式三事，也不是 ProcessProposal 候选执行正式三事。不要另写怎样写 Finalize、怎样缓存 candidate。

## 官方三件事

规范把 FinalizeBlock Usage 里 When calling `FinalizeBlock` with a block / consensus algorithm guarantees / at least one non-byzantine validator has run `ProcessProposal` on that block 写成三件独立的实现事，不是「看见要 Finalize 了就已经每个验证者都跑过 Process、已经提议者 Process 过就代表全网都 Process 过、已经套用 candidate 就不需要 Process 保证」一件事：

1. **看见 When calling `FinalizeBlock` with a block, the consensus algorithm run by CometBFT guarantees / 看见要 Finalize 了有共识保证 不是已经每个验证者都跑过 Process，也不是已经 `_p_`'s Application executes block _v_ / persist decision 那种已经把块落成这一高的决定（466）。**  
   官方 Usage 写：When calling `FinalizeBlock` with a block, the consensus algorithm run by CometBFT guarantees that at least one non-byzantine validator has run `ProcessProposal` on that block。看见 When calling FinalizeBlock，不是已经 +2/3 precommit 同一 id(v) 那种已经会调 Finalize interchangeable（362）。看见 consensus algorithm guarantees，不是已经每个验证者都跑过 Process。看见 guarantees at least one，不是已经 Application executes block _v_ 那种已经执行完 interchangeable——466 When 第 3 步另钉 executes block _v_ 三事，本页只钉 Usage 这句 ProcessProposal guarantee。
2. **看见 at least one non-byzantine validator / 看见至少一名非拜占庭 不是已经提议者那边 Process 过就代表全网都 Process 过，也不是已经本节点刚 Process 过就代表每个验证者都 Process 过。**  
   官方写 at least one non-byzantine validator，不是 already every validator。看见至少一名，不是已经 `ProcessProposal` 也会在这一轮的提议者那边叫（351）那种提议者 Process 过就代表不用再 Process interchangeable。看见 non-byzantine，不是已经本进程 local 路径就可以跳过别的门那种已经验完 interchangeable——VerifyVoteExtension 对 local precommit 不调用是另一门（457），本页只钉 Finalize Usage 这句 guarantee。
3. **看见 has run `ProcessProposal` on that block / 看见对这块跑过 Process 不是已经套用 candidate / previously executed via PrepareProposal or ProcessProposal 就不需要 Process 保证，也不是已经 ProcessProposal MAY 整块执行（452）那种已经交差 interchangeable。**  
   官方写 has run `ProcessProposal` on that block。看见对**这块**跑过 Process，不是已经 Alternatively apply candidate state（460）那种已经 previously executed 就不需要 guarantee interchangeable——460 另钉套用候选三事，本页只钉 guarantee 这句。看见 ran ProcessProposal，不是已经 Process MAY fully execute the block（452）那种 candidate state 就已经是同一句 interchangeable。看见 that block，不是已经 VerifyVoteExtensionRequest.hash 指拟议块时 There is no guarantee that this proposed block has previously been exposed via `ProcessProposal`（418 边界）那种拟议块无保证 interchangeable——那是 VVE 门对**拟议**块，本页钉 Finalize 对**已决**块的 guarantee。

怎样写 Finalize、怎样缓存 candidate、怎样测失败路径是规范里的做法，本页不抄。Finalize 时的 Process 保证 bundled（360）是至少一名非拜占庭跑过 Process / 字段再填一遍 / 可以套用先前候选那套另一切片，FinalizeBlock When Application executes block v（466）是 executes block _v_ / persist decision / apply candidate 那套另一切片，Process 也会在提议者那边叫（351）是提议者路径 / Prepare 对得上 / 失败时不保证那套另一切片，Finalize 套用候选（460）是 execute txs / apply candidate / previously executed 那套另一切片，ProcessProposal 候选执行（452）是 MAY 整块执行 / candidate state / read-only 那套另一切片，本页不抄。

## 官方为什么这样拆

- **When calling FinalizeBlock / consensus guarantees ≠ 已经每个验证者都跑过 Process / 已经把块落成决定：** 官方把至少一名 guarantee 和 executes block _v_ / persist decision 分开。
- **at least one non-byzantine ≠ 已经提议者 Process 过就代表全网都 Process 过：** 官方把至少一名和提议者路径 / 本节点路径分开。
- **has run ProcessProposal on that block ≠ 已经套用 candidate / 先前跑过就不需要 guarantee：** 官方把 guarantee 和 apply candidate / candidate execution 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| When calling FinalizeBlock / consensus guarantees | 不是已经每个验证者都跑过 Process | 不是 Application executes block v（466） |
| at least one non-byzantine validator | 不是已经提议者 Process 过就代表全网都 Process 过 | 不是 Process 也会在提议者那边叫（351） |
| has run ProcessProposal on that block | 不是已经套用 candidate 就不需要 guarantee | 不是 Finalize 套用候选（460） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见要 Finalize 了就已经每个验证者都跑过 Process、已经提议者 Process 过就代表全网都 Process 过、已经套用 candidate 就不需要 Process 保证」，必须分开 When calling FinalizeBlock / consensus guarantees 是不是已经每个验证者都跑过 Process、at least one non-byzantine 是不是已经提议者 Process 过就代表全网都 Process 过、has run ProcessProposal on that block 是不是已经套用 candidate 就不需要 guarantee。可以跳过「看见要 Finalize 了就已经每个验证者都跑过 Process」。不要另写怎样写 Finalize。

## 本页不抄

- 怎样写 Finalize、怎样缓存 candidate、怎样测失败路径。
- Finalize 时的 Process 保证 bundled 三事。那是不变量 360。
- FinalizeBlock When Application executes block v。那是不变量 466。
- Process 也会在提议者那边叫。那是不变量 351。
- Finalize 套用候选。那是不变量 460。
- ProcessProposal 候选执行。那是不变量 452。
- Finalize 请求把字段再填一遍。那是 bundled 360 第二件事，不是本页 dedicated 切片。
