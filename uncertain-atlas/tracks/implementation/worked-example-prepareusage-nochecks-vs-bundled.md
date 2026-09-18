# 例：看见 CometBFT does NOT provide additional validity checks 不是已经验过重复 interchangeable；看见 fails to validate PrepareProposalResponse 引擎崩溃 不是已经是 Process REJECT interchangeable；看见 PrepareProposal MAY be non-deterministic 不是已经必须确定 interchangeable

**层次**：实现 / PrepareProposal Usage no checks / crash / nondet 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「no additional validity checks 不是已经验过重复 interchangeable / crash on invalid response 不是 Process REJECT interchangeable / MAY be non-deterministic 不是必须确定 interchangeable」，不是 Prepare 回包校验 bundled（357），也不是 Prepare 没有确定性要求 bundled（338）。不要另写怎样再验 Prepare 回包、怎样查重复。

## 官方三件事

规范把 PrepareProposal Methods Usage 末尾 no checks / crash / nondet 写成三件独立的实现事，不是「看见回了 Prepare 回包就已经验过重复、已经是 Process REJECT、已经必须确定」一件事：

1. **看见 CometBFT does NOT provide any additional validity checks (such as checking for duplicate transactions) / 看见引擎不再做额外有效性检查 不是已经验过重复 interchangeable / 已经有应用级重放保护 interchangeable，也不是已经 Prepare 回包校验 bundled（357） interchangeable / 已经交给引擎 interchangeable / 已经印进 LastResultsHash interchangeable，也不是已经内存池去重就已经保证不重放（313） interchangeable。**  
   官方 Usage 写：CometBFT does NOT provide any additional validity checks (such as checking for duplicate transactions)。看见 does NOT provide additional validity checks，不是已经 Prepare 回包校验 bundled（357） interchangeable——357 钉 no checks + crash + events 三事 bundled，本页钉 Methods Usage no checks 单句。看见 such as checking for duplicate transactions，不是已经内存池去重（313） interchangeable——313 钉 CheckTx 池门，本页钉 Prepare Usage 侧引擎不再查重复。看见不再做额外检查，不是已经回了提案就已经验过重复 interchangeable。
2. **看见 If CometBFT fails to validate the `PrepareProposalResponse`, CometBFT will assume the Application is faulty and crash / 看见 Prepare 回包验不过引擎崩溃 不是已经是 Process REJECT interchangeable / 已经是正确提议者的准备提案必须被正确接收者 Accept（347） interchangeable / 已经 prevote nil interchangeable，也不是已经 Prepare 回包校验 bundled（357） interchangeable / 已经交给引擎 interchangeable，也不是已经 ProposalStatus REJECT（376） interchangeable。**  
   官方 Usage 写：If CometBFT fails to validate the `PrepareProposalResponse`, CometBFT will assume the Application is faulty and crash。看见 fails to validate → crash，不是已经 ProcessProposalResponse.status REJECT（455） interchangeable——455 钉 Process REJECT 共识假设，本页钉 Prepare Usage crash 单句。看见 assume Application is faulty and crash，不是已经 honest proposal 必须 Accept（347） interchangeable——347 钉 Req 3，本页钉 Prepare 回包坏了就停进程。看见 crash，不是已经 Process REJECT = prevote nil（33） interchangeable。
3. **看见 The implementation of `PrepareProposal` MAY be non-deterministic / 看见 Prepare 实现可以非确定 不是已经必须确定 interchangeable / 已经和 Process / Finalize 同一把尺 interchangeable，也不是已经 Prepare 没有确定性要求 bundled（338） interchangeable / 已经必须同一份 prepared 提案 interchangeable，也不是已经 Process MUST be deterministic（430） interchangeable / 已经 status exclusively depend interchangeable。**  
   官方 Usage 写：The implementation of `PrepareProposal` MAY be non-deterministic。看见 MAY be non-deterministic，不是已经 Process MUST be deterministic（430） interchangeable——430 钉 Process 回包栏 MUST deterministic，本页钉 Prepare Usage MAY nondet 单句。看见 Prepare 可以非确定，不是已经两边 raw 一样就必须是同一份 prepared 提案（338 bundled） interchangeable——338 钉 Requirements 侧 Prepare nondet，本页钉 Methods Usage MAY nondet 单句。看见 MAY nondet，不是已经 Finalize MUST deterministic（470） interchangeable——470 钉 Finalize determinism，本页钉 Prepare Usage 侧 MAY nondet 语义。

怎样做再验 Prepare 回包、怎样查重复、怎样写 Prepare 确定性是规范里的做法，本页不抄。Prepare 回包校验 bundled（357）、Prepare 没有确定性要求 bundled（338）、Prepare 事件保留路径（451）是另外那套，本页不抄。

## 官方为什么这样拆

- **no additional validity checks ≠ 已经验过重复 interchangeable：** 官方把 Methods Usage no checks 单句和 Prepare 回包校验 bundled、内存池去重分开。
- **crash on invalid response ≠ Process REJECT interchangeable：** 官方把 Prepare crash 单句和 Process REJECT / Req 3 Accept 分开。
- **MAY be non-deterministic ≠ 必须确定 interchangeable：** 官方把 Prepare Usage MAY nondet 单句和 Process MUST deterministic 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| no additional validity checks | 不是已经验过重复 | 不是内存池去重就已经保证不重放（313） |
| crash on invalid PrepareProposalResponse | 不是 Process REJECT | 不是 honest proposal 必须 Accept（347） |
| PrepareProposal MAY be non-deterministic | 不是必须确定 | 不是 Process MUST deterministic（430） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal Usage no checks / crash / nondet 正式三事，必须分开 no additional validity checks 是不是已经验过重复 interchangeable、crash on invalid response 是不是 Process REJECT interchangeable、MAY be non-deterministic 是不是必须确定 interchangeable。可以跳过「看见回了 Prepare 回包就已经验过重复、已经是 Process REJECT、已经必须确定 interchangeable」。504 PrepareProposal Usage nochecks bundled unbundling 完成（1307 item 1 / 1308 item 2 / 1309 item 3）；精读 [`worked-example-nochecks-notdup-vs-bundled.md`](worked-example-nochecks-notdup-vs-bundled.md)（不变量 1307 item 1）、[`worked-example-nochecks-notcrash-vs-bundled.md`](worked-example-nochecks-notcrash-vs-bundled.md)（不变量 1308 item 2）、[`worked-example-nochecks-notdet-vs-bundled.md`](worked-example-nochecks-notdet-vs-bundled.md)（不变量 1309 item 3）。不要另写怎样再验 Prepare 回包。

## 本页不抄

- 怎样做再验 Prepare 回包、怎样查重复、怎样写 Prepare 确定性。
- Prepare 回包校验 bundled。那是不变量 357。
- Prepare 没有确定性要求 bundled。那是不变量 338。
- Prepare 事件保留路径。那是不变量 451。
- Process MUST deterministic / status exclusively depend。那是不变量 430。
