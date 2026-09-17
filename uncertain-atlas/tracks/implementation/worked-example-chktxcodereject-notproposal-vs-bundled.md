# 例：看见 CheckTx will not be broadcast / included in a proposal is not already Check passed is in proposal interchangeable / not already forever valid interchangeable / not already Finalize Code≠0 still in block interchangeable

**层次**：实现 / CheckTx Usage will not broadcast or in proposal not Check passed is in proposal / not forever valid / not Finalize Code≠0 still in block 正式三事（489 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx Usage will not broadcast or in proposal not Check passed is in proposal / not forever valid / not Finalize Code≠0 still in block 正式三事（489 余量）/ not 687 chktxcodereject-notproposal interchangeable / not 489 chktxcodereject-vs-proposal bundled interchangeable」，不是 CheckTx Usage Code≠0 rejected 正式三事 bundled（489），也不是四门已经结算（33）或 Finalize Code≠0 仍在块里（316）。不要另写怎样挑回包码、怎样写广播谓词。

## 官方三件事

规范把 CheckTx Usage 里 they will not be broadcast to other nodes or included in a proposal block 和「已经 Check 通过就是已进提案（33） interchangeable / 已经 CheckTx 过了就永远有效（301） interchangeable / 已经 Finalize `Code ≠ 0` 那种仍在块里（316） interchangeable」分开写成三件独立的实现事，不是「看见不会进提案块 就已经 Check passed is in proposal interchangeable / 就已经 forever valid interchangeable / 就已经 Finalize Code≠0 still in block interchangeable」一件事：

1. **看见 they will not be broadcast to other nodes / or included in a proposal block / 看见不会广播、也不会进提案块 / will not be included is not already 已经 Check 通过就是已进提案（33） interchangeable / 33 four gates interchangeable / 已经四门已经结算 interchangeable / 已经 Prep/Process 过了 interchangeable，也不是已经 CheckTx Usage Code≠0 rejected 正式三事 bundled（489） interchangeable / 687 chktxcodereject-notproposal interchangeable / 686 chktxcodereject-notgossip interchangeable / 489 chktxcodereject item 1 rejected interchangeable，也不是已经 will not broadcast or in proposal not Check passed is in proposal / not forever valid / not Finalize Code≠0 still in block 正式三事 bundled（489 item 2 余量） interchangeable / 489 chktxcodereject item 2 interchangeable。**  
   官方 Usage 写：… will not be broadcast to other nodes or included in a proposal block。看见 or included in a proposal block，不是已经 Check 通过就是已进提案 interchangeable——33 钉四门分开，本页从 489 item 2 侧钉 not Check passed is in proposal 单句。489 chktxcodereject vs proposal bundled unbundling 在本页 item 2 续。

2. **看见 will not be broadcast / will not be included in a proposal block / 看见不会进提案块 is not already 已经 CheckTx 过了就永远有效（301） interchangeable / 301 forever valid interchangeable / 已经提案收了就从池里删掉 interchangeable / 已经 CheckTx 过了就进块 interchangeable，也不是已经 CheckTx Usage Code≠0 rejected 正式三事 bundled（489） interchangeable / 687 chktxcodereject-notproposal interchangeable / 489 chktxcodereject item 3 no other value interchangeable / 688 chktxcodereject-notothervalue interchangeable。**  
   官方把 Usage 不会进提案块单句和 forever valid 路径分开——489 bundled 第二件事常与 301 混成「看见不会进提案块 就已经 forever valid interchangeable」，本页钉 not forever valid 单句。看见 will not be broadcast，不是已经别的节点已经从邻居收到 interchangeable。

3. **看见 will not be included in a proposal block / 看见不会进提案块 / 看见 Code 非零 is not already 已经 Finalize `ExecTxResult.Code ≠ 0` 仍在块里（316） interchangeable / 316 exectxresult interchangeable / 已经没进块 interchangeable / 已经无效就不建索引那种已经不在块里 interchangeable，也不是已经 CheckTx Usage Code≠0 rejected 正式三事 bundled（489） interchangeable / 687 chktxcodereject-notproposal interchangeable / 686 chktxcodereject-notgossip interchangeable。**  
   官方把 CheckTx 池门 Code 语义和 Finalize 回执路径分开——489 bundled 第二件事常与 316 混成「看见 CheckTx Code≠0 就已经 Finalize Code≠0 仍在块里 interchangeable」，本页钉 not Finalize Code≠0 still in block 单句。看见不会进提案块，不是已经 Finalize 无效交易不建索引 interchangeable——316 钉 Finalize 回执，本页钉 Usage 池门。489 chktxcodereject vs proposal bundled unbundling 在本页 item 2 续。

怎样做广播过滤、怎样写 CheckTx 回包码、怎样区分池门 Code 与 Finalize Code 是规范里的做法，本页不抄。CheckTx Usage Code≠0 rejected 正式三事 bundled（489）、Code≠0 will be rejected（489 item 1 余量 / 686）、no other value（489 item 3 余量 / 688）、四门已经结算（33）、Finalize Code≠0 仍在块里（316）是另外那套，本页不抄。

## 官方为什么这样拆

- **will not be in proposal not Check passed is in proposal ≠ 33 four gates interchangeable：** 官方把 Usage 不会进提案块和四门结算 / Check 通过就是已进提案路径分开。
- **will not be in proposal not forever valid ≠ 301 forever valid interchangeable：** 官方把 Usage 不会进提案块单句和 CheckTx 过了就永远有效路径分开。
- **will not be in proposal not Finalize Code≠0 still in block ≠ 316 interchangeable：** 官方把 CheckTx 池门 Code 和 Finalize 回执 Code≠0 仍在块里路径分开；489 chktxcodereject vs proposal bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| will not be included in a proposal block | 不是 Check 通过就是已进提案（33） | 不是 Code≠0 rejected 单句（686/489 item 1） |
| 不会广播 / 不会进提案块 | 不是 forever valid（301） | 不是 CheckTx Usage Guardian（490） |
| 看见 Code 非零 | 不是 Finalize Code≠0 仍在块里（316） | 不是 no other value（688/489 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage will not broadcast or in proposal not Check passed is in proposal / not forever valid / not Finalize Code≠0 still in block 正式三事（489 余量），必须分开不会进提案块 是不是 Check 通过就是已进提案 interchangeable / 33、是不是 forever valid interchangeable / 301、是不是 Finalize Code≠0 仍在块里 interchangeable / 316。可以跳过「看见不会进提案块就已经交差」。不要另写怎样挑回包码。489 chktxcodereject vs proposal bundled unbundling 在本页 item 2 续；续 [`worked-example-chktxcodereject-notothervalue-vs-bundled.md`](worked-example-chktxcodereject-notothervalue-vs-bundled.md)（不变量 688 item 3）。

## 本页不抄

- 怎样做广播过滤、怎样写 CheckTx 回包码、怎样区分池门 Code 与 Finalize Code。
- CheckTx Usage Code≠0 rejected 正式三事 bundled。那是不变量 489。
- Code≠0 will be rejected。那是不变量 489 item 1 余量 / 686。
- no other value to the response code。那是不变量 489 item 3 余量 / 688。
- Check 通过就是已进提案。那是不变量 33。
- 提案收了 / CheckTx 过了就永远有效。那是不变量 301。
- Finalize `Code ≠ 0` 仍在块里。那是不变量 316。
