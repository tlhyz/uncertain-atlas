# 例：看见 Application calculates and returns the AppHash, along with a list containing the outputs of each of the transactions executed / 看见应用回 AppHash 和各笔 tx outputs is not already 印进本头 interchangeable / 已经是本头 AppHash interchangeable；不是已经 FinalizeBlock When AppHash tx outputs ResultHash persist 正式三事 bundled（587） interchangeable / 已经 finreturn bundled interchangeable

**层次**：实现 / FinalizeBlock When Application returns AppHash + tx outputs not printed in this header / not this header AppHash 正式三事（587 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 4。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock When Application returns AppHash + tx outputs not printed in this header / not this header AppHash 正式三事（587 余量）/ not 614 notheader interchangeable / not 147 apphash vs this block interchangeable / not 404 finapphash interchangeable / not 466 executes block v interchangeable」，不是 FinalizeBlock When AppHash tx outputs ResultHash persist 正式三事 bundled（587），也不是 Finalize 何时调用 bundled（362），也不是 Finalize 回包 app_hash 可以空或硬编码 bundled（404）。不要另写怎样算 AppHash、怎样算 ResultHash、怎样落盘这三份。

## 官方三件事

规范把 FinalizeBlock When 第 4 步 Application calculates and returns the AppHash, along with a list containing the outputs of each of the transactions executed 和「已经是印进本头 interchangeable / 已经是本头 AppHash interchangeable / 已经是 finreturn bundled interchangeable」分开写成三件独立的实现事，不是「看见 Application returns AppHash + tx outputs 就已经印进本头、就已经是本头 AppHash、就已经 finreturn bundled interchangeable」一件事：

1. **看见 Application calculates and returns the AppHash, along with a list containing the outputs of each of the transactions executed / 看见应用回 AppHash 和各笔 tx outputs is not already 印进本头 interchangeable / 已经写入本头 interchangeable / 已经 Header.AppHash 对上 interchangeable，也不是已经 FinalizeBlock When AppHash tx outputs ResultHash persist 正式三事 bundled（587） interchangeable / 614 notheader interchangeable / 587 finreturn interchangeable / 147 apphash vs this block interchangeable / 404 finapphash interchangeable，也不是已经 FinalizeBlockResponse app_hash optional Merkle root bundled（475 余量） interchangeable / 475 finmerkle interchangeable / 404 finapphash interchangeable / 432 finrespend interchangeable / 470 findet not apphash interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466 余量） interchangeable / 466 finexecbv interchangeable / 572 not execbv interchangeable / 573 not persist interchangeable / 584 apply candidate interchangeable，也不是已经 Finalize 含刚决定那块的字段 bundled（461 余量） interchangeable / 461 finnewfields interchangeable / 407 finfields interchangeable / 474 finnewdec interchangeable / 335 finpersist interchangeable。**  
   官方 When 第 4 步写：Application calculates and returns the _AppHash_, along with a list containing the outputs of each of the transactions executed。看见 calculates and returns，不是已经 executes block _v_ 那种已经执行完（466 第 3 步）——587 bundled 第一件事常被写成「看见 Application returns AppHash + tx outputs 就已经印进本头 interchangeable」，本页从 587 item 1 侧钉 not printed in this header 单句。看见回了 AppHash 和各笔输出，不是已经写入当前块头 interchangeable——Usage 写：`FinalizeBlockResponse.app_hash` is included as the `Header.AppHash` in the **next** block，本页钉 When 第 4 步 returns 单句。看见 tx outputs 列表，不是已经 Finalize 回包 app_hash 可以空或硬编码（404） interchangeable——404 钉 Response app_hash 语义，本页钉 587 item 1 第一件事。
2. **看见 Application calculates and returns AppHash along with tx outputs / 看见应用回 AppHash 和各笔 tx outputs is not already 已经是本头 AppHash interchangeable / 已经本头 AppHash 就代表本高度交差 interchangeable / 147 apphash vs this block interchangeable / 362 finwhen item 4 Application returns AppHash interchangeable，也不是已经 FinalizeBlock When AppHash tx outputs ResultHash persist 正式三事 bundled（587） interchangeable / 614 notheader interchangeable / 147 apphash vs this block interchangeable / 404 finapphash interchangeable / 335 finpersist interchangeable，也不是已经 本头 AppHash ≠ 本高度交易已经交差 bundled（147 余量） interchangeable / 147 apphash vs this block interchangeable / 362 +2/3 precommit interchangeable / 33 four gates interchangeable / 601 notsettled interchangeable，也不是已经 FinalizeBlockResponse optional Merkle root not 已经是本头 AppHash bundled（475 余量） interchangeable / 475 finmerkle interchangeable / 404 finapphash interchangeable / 470 findet not apphash interchangeable / 581 findet not replication interchangeable，也不是已经 FinalizeBlock When persist decision not 已经交差 bundled（605 余量） interchangeable / 605 notpersist interchangeable / 478 finpersist interchangeable / 587 finreturn interchangeable / 606 notoutputs interchangeable。**  
   官方把 Application returns AppHash 和 next block Header.AppHash / 本头 AppHash 分开——587 item 1 常与 147 混成「看见回了 app_hash 就已经是本头 AppHash interchangeable」，本页钉 not this header AppHash 单句。看见 calculates and returns，不是已经本头 AppHash 就代表本高度交易已经交差（147） interchangeable——147 钉本头 AppHash vs 本高度交差，本页钉 587 item 1 第二件事。看见 tx outputs 列表，不是已经 Finalize 改了就已经落盘（335） interchangeable——335 钉应用在 Finalize 里落盘，本页钉 not this header AppHash 单句。
3. **看见 Application calculates and returns AppHash along with tx outputs / 看见应用回 AppHash 和各笔 tx outputs is not already finreturn bundled（587） interchangeable / 已经 CometBFT hashes into ResultHash interchangeable / 已经 CometBFT persists tx outputs / AppHash / ResultsHash interchangeable / 587 finreturn item 2 interchangeable / 587 finreturn item 3 interchangeable，也不是已经 FinalizeBlock When AppHash tx outputs ResultHash persist 正式三事 bundled（587） interchangeable / 614 notheader interchangeable / 615 notresulthash interchangeable / 616 notpersist interchangeable / 467 finpersist interchangeable / 403 finafter interchangeable，也不是已经 CometBFT hashes all the transaction outputs and stores it in ResultHash bundled（587 item 2 余量 / 615） interchangeable / 615 notresulthash interchangeable / 316 ExecTxResult interchangeable / 404 finapphash interchangeable / 432 finrespend interchangeable，也不是已经 CometBFT persists the transaction outputs, AppHash, and ResultsHash bundled（587 item 3 余量 / 616） interchangeable / 616 notpersist interchangeable / 335 finpersist interchangeable / 481 commitpersist interchangeable / 403 finafter interchangeable，也不是已经 FinalizeBlock When calls FinalizeBlock not persist outputs bundled（606 余量） interchangeable / 606 notoutputs interchangeable / 478 finpersist item 2 interchangeable / 587 finreturn interchangeable / 362 finwhen interchangeable。**  
   官方把 587 finreturn bundled 三事里的 Application returns AppHash + tx outputs 和 hashes into ResultHash / persists 这三份 分开——587 bundled 常与 item 2 / item 3 混成「看见 Application returns AppHash + tx outputs 就已经 finreturn bundled interchangeable」，本页钉 587 item 1 第三件事。看见 calculates and returns，不是已经 CometBFT hashes into ResultHash（587 item 2 余量 / 615） interchangeable——615 另钉 not Code / Data 印进本头 LastResultsHash，本页钉 item 1 单句。看见 tx outputs 列表，不是已经 CometBFT persists tx outputs / AppHash / ResultsHash（587 item 3 余量 / 616） interchangeable——616 另钉 not Commit 落盘应用状态，本页钉 not finreturn bundled 单句。

怎样算 AppHash、怎样算 ResultHash、怎样落盘这三份、怎样 Commit 是规范里的做法，本页不抄。FinalizeBlock When AppHash tx outputs ResultHash persist 正式三事 bundled（587）、CometBFT hashes into ResultHash not Code / Data 印进本头（587 item 2 余量 / 615）、CometBFT persists tx outputs / AppHash / ResultsHash not Commit 落盘（587 item 3 余量 / 616）、Finalize 何时调用 bundled（362）、Finalize 回包 app_hash 可以空或硬编码（404）、Application executes block v（466）是另外那套，本页不抄。

## 官方为什么这样拆

- **Application returns AppHash + tx outputs not printed in this header ≠ 475 finmerkle / 404 finapphash interchangeable：** 官方把 When 第 4 步 returns 和 Response app_hash / next block Header.AppHash 分开。
- **Application returns AppHash + tx outputs not this header AppHash ≠ 147 apphash vs this block / 335 finpersist interchangeable：** 官方把 587 item 1 和本头 AppHash / Finalize 落盘分开。
- **Application returns AppHash + tx outputs not finreturn bundled ≠ 615 notresulthash / 616 notpersist interchangeable：** 官方把 587 item 1 和 item 2 / item 3 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Application returns AppHash + tx outputs | 不是 already printed in this header | 不是 finmerkle / finapphash（404 / 475） |
| Application returns AppHash + tx outputs | 不是 already this header AppHash | 不是 apphash vs this block（147） |
| Application returns AppHash + tx outputs | 不是 already finreturn bundled | 不是 hashes into ResultHash（587 item 2 / 615） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When Application returns AppHash + tx outputs not printed in this header / not this header AppHash 正式三事（587 余量），必须分开 Application returns 是不是 already 印进本头 interchangeable / 404 finapphash interchangeable / 475 finmerkle interchangeable、Application returns 是不是 already 本头 AppHash interchangeable / 147 apphash vs this block interchangeable / 335 finpersist interchangeable / 362 finwhen interchangeable、Application returns 是不是 already finreturn bundled interchangeable / 615 notresulthash interchangeable / 616 notpersist interchangeable / 467 finpersist interchangeable / 606 notoutputs interchangeable。可以跳过「看见 Application returns AppHash + tx outputs 就已经印进本头 interchangeable」。不要另写怎样算 AppHash。

## 本页不抄

- 怎样算 AppHash、怎样算 ResultHash、怎样落盘这三份、怎样 Commit。
- FinalizeBlock When AppHash tx outputs ResultHash persist 正式三事 bundled。那是不变量 587。
- CometBFT hashes into ResultHash not Code / Data 印进本头。那是不变量 587 item 2 余量 / 615。
- CometBFT persists tx outputs / AppHash / ResultsHash not Commit 落盘。那是不变量 587 item 3 余量 / 616。
- Finalize 何时调用 bundled。那是不变量 362。
- Finalize 回包 app_hash 可以空或硬编码。那是不变量 404。
- Application executes block v bundled。那是不变量 466。
- 本头 AppHash vs 本高度交差。那是不变量 147。
