# 例：看见 all fields / request complete in FinalizeBlockRequest is not already committed / settled / not FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / not Finalize 含刚决定那块的字段 interchangeable

**层次**：实现 / FinalizeBlock fill all fields not request complete means committed 正式三事（473 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock fill all fields not request complete means committed / not FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / not Finalize 含刚决定那块的字段 interchangeable」，不是 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473），也不是 Finalize 请求把字段再填一遍 not no need to provide again 正式三事（583 余量）第三件事。不要另写怎样写 Finalize、怎样再填字段。

## 官方三件事

规范把 FinalizeBlock Usage 里 all fields in `FinalizeBlockRequest` will be filled up / request complete 和「已经交差 / 已经 Finalize 改了就已经落盘 / 已经是 finfields / finpersist bundled interchangeable」分开写成三件独立的实现事，不是「看见请求齐了就已经 committed interchangeable、已经 Finalize + Commit interchangeable、已经 473 finfill bundled interchangeable」一件事：

1. **看见 all fields / 又填一遍 / request complete in FinalizeBlockRequest is not already committed / already settled interchangeable / 看见请求齐了 is not already FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / 已经交差 interchangeable / 已经 Finalize 改了就已经落盘 interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable / 已经不用再给 interchangeable / 已经套用先前候选 interchangeable，也不是已经 Finalize 请求把字段再填一遍 not no need to provide again bundled（583 余量） interchangeable / 583 refill not request complete means committed interchangeable / 567 not no need to provide again interchangeable，也不是已经 apply candidate state not ExecuteTxState bundled（584 余量） interchangeable / 584 apply candidate interchangeable / 568 not passed means ran Process interchangeable。**  
   官方 Usage 写：all fields in `FinalizeBlockRequest` will be filled up。看见 all fields / 又填一遍 / 请求齐了，不是已经交差——473 item 3 常被写成「看见 request complete 就已经 committed interchangeable」，本页钉 fill all fields not request complete means committed 单句。看见 request complete，不是已经 FinalizeBlock fill all fields even if Prepare/Process passed（473） interchangeable——473 另钉 will fill up / even if passed 三事，本页钉 item 3 边界。看见又填一遍，不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable——360 另钉 at least one / apply candidate bundled，本页钉 finfill notcommitted 单句。
2. **看见 all fields / request complete is not already Finalize 含刚决定那块的字段 bundled（407 余量） interchangeable / 看见请求齐了 is not already newly decided block fields interchangeable / 407 finfields interchangeable / 335 finpersist interchangeable / 576 fincand committed interchangeable，也不是已经 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / 569 not request complete means committed interchangeable / 567 not no need to provide again interchangeable，也不是已经 FinalizeBlock persist decision not committed bundled（335 余量） interchangeable / 335 finpersist interchangeable / 576 fincand committed interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable / 已经 persist decision interchangeable / 584 apply candidate interchangeable。**  
   官方把 request complete 和 newly decided block fields / persist decision 分开——473 item 3 常与 407 / 335 混成「看见请求齐了就已经是 Finalize 含刚决定那块的字段 interchangeable」，本页钉 request complete not finfields / finpersist 单句。看见 all fields 填齐，不是已经 Finalize + Commit 那种已经交差 interchangeable——335 / 576 各钉 committed 边界，本页钉 473 item 3 单句。看见 request complete，不是已经 FinalizeBlock persist decision not committed（335 余量） interchangeable——335 钉 persist 边界，本页钉 finfill notcommitted 单句。
3. **看见 all fields / request complete is not already apply candidate state not ExecuteTxState bundled（584 余量） interchangeable / 看见又填一遍 is not already previously executed interchangeable / 584 apply candidate interchangeable / 583 refill not request complete means committed interchangeable，也不是已经 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） interchangeable / 569 not request complete means committed interchangeable / 568 not passed means ran Process interchangeable，也不是已经 Finalize 请求把字段再填一遍 not no need to provide again bundled（583 余量） interchangeable / 583 not refill interchangeable / 567 not no need to provide again interchangeable，也不是已经 Finalize 含刚决定那块的字段 bundled（407 余量） interchangeable / 407 finfields interchangeable / 335 finpersist interchangeable。**  
   官方把 request complete 和 apply candidate / refill not committed 分开——473 item 3 常与 584 / 583 混成「看见又填一遍就已经套用先前候选 interchangeable」，本页钉 request complete not apply candidate / refill 单句。看见 all fields，不是已经 apply candidate / previously executed（584 余量） interchangeable——584 钉 360 item 3 边界，本页钉 473 item 3 第三件事。看见 request complete，不是已经 Finalize 请求把字段再填一遍 not no need to provide again（583 余量） interchangeable——583 钉 360 item 2 refill 边界，本页钉 finfill notcommitted 单句。

怎样写 Finalize、怎样再填字段、怎样从 Prepare/Process 复制字段是规范里的做法，本页不抄。FinalizeBlock fill all fields even if Prepare/Process passed bundled（473）、FinalizeBlock fill all fields not no need to provide again 正式三事（567 余量）、FinalizeBlock fill all fields not passed means ran Process 正式三事（568 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **fill all fields not request complete means committed ≠ FinalizeBlock fill all fields even if Prepare/Process passed bundled interchangeable：** 官方把 request complete 和已经交差分开。
- **fill all fields not request complete means committed ≠ finfields / finpersist bundled interchangeable：** 官方把 request complete 和 newly decided block fields / persist decision 分开。
- **fill all fields not request complete means committed ≠ apply candidate / 583 refill interchangeable：** 官方把 request complete 和 apply candidate / refill not committed 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| all fields / request complete | 不是 already committed / settled | 不是 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473） |
| all fields / request complete | 不是 already finfields / finpersist | 不是 Finalize 含刚决定那块的字段（407） |
| all fields / request complete | 不是 already apply candidate / 583 refill | 不是 apply candidate state not ExecuteTxState（584） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields not request complete means committed 正式三事（473 余量），必须分开 request complete 是不是 already committed interchangeable / 473 finfill interchangeable / 583 refill not request complete means committed interchangeable、request complete 是不是 already finfields / finpersist interchangeable / 407 finfields interchangeable / 335 finpersist interchangeable、request complete 是不是 already apply candidate interchangeable / 584 apply candidate interchangeable / 567 not no need to provide again interchangeable。可以跳过「看见请求齐了就已经交差 interchangeable」。不要另写怎样再填字段。

## 本页不抄

- 怎样写 Finalize、怎样再填字段、怎样从 Prepare/Process 复制字段。
- will fill up all fields not no need to provide again。那是不变量 565（473 余量）。
- even if passed not field names match means ran Process。那是不变量 568（473 item 2 余量）。
- FinalizeBlock fill all fields even if Prepare/Process passed bundled 三事。那是不变量 473。
- Finalize 请求把字段再填一遍 not no need to provide again 正式三事（360 余量）。那是不变量 583。
