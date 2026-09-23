# 例：看见不调本地票 / 看见是自己签的 / 看见跳过本地 is not already already self-verified interchangeable / already accept interchangeable / already req6-done interchangeable

**层次**：实现 / 不对本进程自己发出的 Precommit 调用不是已经自己验过 not already self-verified / not already accept / not already req6-done 正式三事（353 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「不对本进程自己发出的 Precommit 调用不是已经自己验过 not already self-verified / not already accept / not already req6-done 正式三事（353 余量）/ not 813 empty-notlocal interchangeable / not 353 verifywhen bundled interchangeable」，不是 Verify 何时调用 bundled（353），也不是空扩展仍会调 Verify 不是已经跳过 Verify（812 item 1 余量）或请求里的 hash 不是已经对该块跑过 Process（814 item 3 余量）。不要另写怎样写 Verify 何时调用。

## 官方三件事

规范把 Methods 里 `VerifyVoteExtension` 不对本进程自己发出的 Precommit 调用 和「已经是不调本地票就已经自己验过 interchangeable / 已经是自己签的就已经 Accept interchangeable / 已经是跳过本地就已经过了 Req 6 interchangeable / 已经是 verifywhen bundled interchangeable」分开写成三件独立的实现事，不是「看见不调本地票就已经自己验过 interchangeable / 就已经 Accept interchangeable / 就已经过了 Req 6 interchangeable」一件事：

1. **看见 `VerifyVoteExtension` 不对本进程自己发出的 Precommit 调用 / 看见不调本地票 / 看见是本地票 is not already 已经自己验过 interchangeable / 已经 self-verified interchangeable / 已经自己验过交差 interchangeable / 353 verifywhen bundled interchangeable / 348 req6coherence interchangeable / verifywhen-sold-as-skipped interchangeable，也不是已经 Verify 何时调用 bundled（353） interchangeable / 813 empty-notlocal interchangeable / 353 verifywhen item 2 interchangeable，也不是已经不对本进程自己发出的 Precommit 调用不是已经自己验过 not already self-verified / not already accept / not already req6-done 正式三事 bundled（353 item 2 余量） interchangeable / 353 verifywhen item 2 interchangeable，也不是已经跳过 Verify（812） interchangeable / 814 hash-notprocess interchangeable / 34 vote-extension-block interchangeable，也不是已经正确进程交出的扩展必须被正确接收者 Verify Accept（348） interchangeable。**  
   官方写：`VerifyVoteExtension` 不对本进程自己发出的 Precommit 调用。看见不调本地票，不是已经自己验过。看见不调本地票，不是已经 self-verified interchangeable——353 钉 bundled 三事，本页从 item 2 侧钉 not already self-verified 单句。看见不对本进程自己发出的 Precommit 调用，不是已经 Verify 何时调用 bundled（353） interchangeable——353 钉 bundled，本页钉 item 2 第一件事。看见不调本地票，不是已经跳过 Verify（812） interchangeable——812 另钉 item 1。看见不调本地票，不是已经正确进程交出的扩展必须被正确接收者 Verify Accept（348） interchangeable——348 另钉。353 verifywhen vs empty bundled unbundling 在本页 item 2 续。

2. **看见是自己签的 / 看见本地签的 Precommit / 看见本进程发出的票 is not already 已经 Accept interchangeable / 已经 accept interchangeable / 已经 Accept 交差 interchangeable / 353 verifywhen bundled interchangeable / 348 req6coherence interchangeable，也不是已经 Verify 何时调用 bundled（353） interchangeable / 813 empty-notlocal interchangeable / 353 verifywhen item 1 空扩展 interchangeable / 353 verifywhen item 3 hash interchangeable，也不是已经不对本进程自己发出的 Precommit 调用不是已经自己验过 not already self-verified / not already accept / not already req6-done 正式三事 bundled（353 item 2 余量） interchangeable / 353 verifywhen item 2 interchangeable，也不是已经自己验过（本页第一件事） interchangeable。**  
   官方写：看见是自己签的，不是已经 Accept。看见本地签的 Precommit，不是已经 accept interchangeable——本页钉 not already accept 单句。看见本进程发出的票，不是已经自己验过（本页第一件事） interchangeable——三件事分开钉。353 verifywhen vs empty bundled unbundling 在本页 item 2 续。

3. **看见跳过本地 / 看见不调本地 / 看见本地票被跳过 is not already 已经过了 Req 6 interchangeable / 已经 req6-done interchangeable / 已经 Req 6 交差 interchangeable / 353 verifywhen bundled interchangeable / 351 processalso interchangeable，也不是已经 Verify 何时调用 bundled（353） interchangeable / 813 empty-notlocal interchangeable / 353 verifywhen item 1 / 353 verifywhen item 3，也不是已经不对本进程自己发出的 Precommit 调用不是已经自己验过 not already self-verified / not already accept / not already req6-done 正式三事 bundled（353 item 2 余量） interchangeable / 353 verifywhen item 2 interchangeable，也不是已经自己验过（本页第一件事） interchangeable / 已经 Accept（本页第二件事） interchangeable。**  
   官方写：看见跳过本地，不是已经过了 Req 6。看见不调本地，不是已经 req6-done interchangeable——本页钉 not already req6-done 单句。看见本地票被跳过，不是已经 Accept（本页第二件事） interchangeable——三件事分开钉。353 verifywhen vs empty bundled unbundling 在本页 item 2 续。

怎样写 Verify 何时调用、怎样写空扩展、怎样缓存 Process 是规范里的做法，本页不抄。Verify 何时调用 bundled（353）、空扩展仍会调 Verify 不是已经跳过 Verify（353 item 1 余量 / 812）、请求里的 hash 不是已经对该块跑过 Process（353 item 3 余量 / 814）、验签拒收整张预提交就已经是块非法（34）、正确进程交出的扩展必须被正确接收者 Verify Accept（348）、Process 也会在提议者那边叫（351）是另外那套，本页不抄。

## 官方为什么这样拆

- **不调本地票 not already self-verified ≠ 353 / 348 interchangeable：** 官方把不调本地票和已经自己验过分开。
- **是自己签的 not already accept ≠ 已经 Accept interchangeable：** 官方把是自己签的和已经 Accept 分开。
- **跳过本地 not already req6-done ≠ 已经过了 Req 6 interchangeable：** 官方把跳过本地和已经过了 Req 6 分开；353 verifywhen vs empty bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 不调本地票 | 不是 already self-verified | 不是正确进程交出的扩展必须被正确接收者 Verify Accept alone（348） |
| 是自己签的 | 不是 already accept | 不是是空的 already skip-verify alone（812） |
| 跳过本地 | 不是 already req6-done | 不是有 hash already process alone（814） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看不对本进程自己发出的 Precommit 调用不是已经自己验过 not already self-verified / not already accept / not already req6-done 正式三事（353 余量），必须分开不调本地票 是不是 already self-verified interchangeable / 353 verifywhen bundled interchangeable / verifywhen-sold-as-skipped interchangeable、是自己签的 是不是 already accept interchangeable、跳过本地 是不是 already req6-done interchangeable。可以跳过「看见不调本地票就已经自己验过 interchangeable / 就已经 Accept interchangeable / 就已经过了 Req 6 interchangeable」。不要另写怎样写 Verify 何时调用。353 verifywhen vs empty bundled unbundling 在本页 item 2 续（812 + 813）；完成 [`worked-example-hash-notprocess-vs-bundled.md`](worked-example-hash-notprocess-vs-bundled.md)（不变量 814 item 3）。

## 本页不抄

- 怎样写 Verify 何时调用、怎样写空扩展、怎样缓存 Process。
- Verify 何时调用 bundled。那是不变量 353。
- 空扩展仍会调 Verify 不是已经跳过 Verify。那是不变量 353 item 1 余量 / 812。
- 请求里的 hash 不是已经对该块跑过 Process。那是不变量 353 item 3 余量 / 814。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
- 正确进程交出的扩展必须被正确接收者 Verify Accept。那是不变量 348。
- Process 也会在提议者那边叫。那是不变量 351。
