# 例：看见有 hash / 看见是同一块 / 看见不保证 is not already already ran-process interchangeable / already this-process interchangeable / already processalso interchangeable

**层次**：实现 / 请求里的 hash 不是已经对该块跑过 Process not already ran-process / not already this-process / not already processalso 正式三事（353 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「请求里的 hash 不是已经对该块跑过 Process not already ran-process / not already this-process / not already processalso 正式三事（353 余量）/ not 814 hash-notprocess interchangeable / not 353 verifywhen bundled interchangeable」，不是 Verify 何时调用 bundled（353），也不是空扩展仍会调 Verify 不是已经跳过 Verify（812 item 1 余量）或不对本进程自己发出的 Precommit 调用不是已经自己验过（813 item 2 余量）。不要另写怎样写 Verify 何时调用。

## 官方三件事

规范把 Methods 里请求里的 `hash` 指向某块、不保证这块已经通过 `ProcessProposal` 暴露给应用 和「已经是有 hash 就已经 Process 过 interchangeable / 已经是同一块就已经对上这次 Process interchangeable / 已经是不保证就已经是提议者那边也会叫 Process interchangeable / 已经是 verifywhen bundled interchangeable」分开写成三件独立的实现事，不是「看见有 hash 就已经 Process 过 interchangeable / 就已经对上这次 Process interchangeable / 就已经是提议者那边也会叫 Process interchangeable」一件事：

1. **看见请求里的 `hash` / 看见有 hash / 看见指向某块 is not already 已经对该块跑过 `ProcessProposal` interchangeable / 已经 ran-process interchangeable / 已经 Process 过交差 interchangeable / 353 verifywhen bundled interchangeable / 351 processalso interchangeable / verifywhen-sold-as-skipped interchangeable，也不是已经 Verify 何时调用 bundled（353） interchangeable / 814 hash-notprocess interchangeable / 353 verifywhen item 3 interchangeable，也不是已经请求里的 hash 不是已经对该块跑过 Process not already ran-process / not already this-process / not already processalso 正式三事 bundled（353 item 3 余量） interchangeable / 353 verifywhen item 3 interchangeable，也不是已经跳过 Verify（812） interchangeable / 813 empty-notlocal interchangeable / 34 vote-extension-block interchangeable，也不是已经 Process 也会在提议者那边叫（351） interchangeable。**  
   官方写：请求里的 `hash` 指向某块，不保证这块已经通过 `ProcessProposal` 暴露给应用。看见有 hash，不是已经 Process 过。看见有 hash，不是已经 ran-process interchangeable——353 钉 bundled 三事，本页从 item 3 侧钉 not already ran-process 单句。看见请求里的 hash，不是已经 Verify 何时调用 bundled（353） interchangeable——353 钉 bundled，本页钉 item 3 第一件事。看见有 hash，不是已经跳过 Verify（812） interchangeable——812 另钉 item 1。看见有 hash，不是已经 Process 也会在提议者那边叫（351） interchangeable——351 另钉。353 verifywhen vs empty bundled unbundling 在本页 item 3 完成。

2. **看见是同一块 / 看见 hash 指向同一块 / 看见同一块身份 is not already 已经对上这次 Process interchangeable / 已经 this-process interchangeable / 已经对上这次 Process 交差 interchangeable / 353 verifywhen bundled interchangeable / 351 processalso interchangeable，也不是已经 Verify 何时调用 bundled（353） interchangeable / 814 hash-notprocess interchangeable / 353 verifywhen item 1 空扩展 interchangeable / 353 verifywhen item 2 本地票 interchangeable，也不是已经请求里的 hash 不是已经对该块跑过 Process not already ran-process / not already this-process / not already processalso 正式三事 bundled（353 item 3 余量） interchangeable / 353 verifywhen item 3 interchangeable，也不是已经 Process 过（本页第一件事） interchangeable。**  
   官方写：看见是同一块，不是已经对上这次 Process。看见 hash 指向同一块，不是已经 this-process interchangeable——本页钉 not already this-process 单句。看见同一块身份，不是已经 Process 过（本页第一件事） interchangeable——三件事分开钉。353 verifywhen vs empty bundled unbundling 在本页 item 3 完成。

3. **看见不保证 / 看见不保证已经暴露给应用 / 看见规范说不保证 is not already 已经是提议者那边也会叫 Process interchangeable / 已经 processalso interchangeable / 已经 processalso 交差 interchangeable / 353 verifywhen bundled interchangeable / 351 processalso interchangeable，也不是已经 Verify 何时调用 bundled（353） interchangeable / 814 hash-notprocess interchangeable / 353 verifywhen item 1 / 353 verifywhen item 2，也不是已经请求里的 hash 不是已经对该块跑过 Process not already ran-process / not already this-process / not already processalso 正式三事 bundled（353 item 3 余量） interchangeable / 353 verifywhen item 3 interchangeable，也不是已经 Process 过（本页第一件事） interchangeable / 已经对上这次 Process（本页第二件事） interchangeable。**  
   官方写：看见不保证，不是已经是提议者那边也会叫 Process。看见不保证已经暴露给应用，不是已经 processalso interchangeable——本页钉 not already processalso 单句。看见规范说不保证，不是已经对上这次 Process（本页第二件事） interchangeable——三件事分开钉。353 verifywhen vs empty bundled unbundling 在本页 item 3 完成。

怎样写 Verify 何时调用、怎样写空扩展、怎样缓存 Process 是规范里的做法，本页不抄。Verify 何时调用 bundled（353）、空扩展仍会调 Verify 不是已经跳过 Verify（353 item 1 余量 / 812）、不对本进程自己发出的 Precommit 调用不是已经自己验过（353 item 2 余量 / 813）、验签拒收整张预提交就已经是块非法（34）、正确进程交出的扩展必须被正确接收者 Verify Accept（348）、Process 也会在提议者那边叫（351）是另外那套，本页不抄。

## 官方为什么这样拆

- **有 hash not already ran-process ≠ 353 / 351 interchangeable：** 官方把有 hash 和已经 Process 过分开。
- **是同一块 not already this-process ≠ 已经对上这次 Process interchangeable：** 官方把是同一块和已经对上这次 Process 分开。
- **不保证 not already processalso ≠ 已经是提议者那边也会叫 Process interchangeable：** 官方把不保证和已经是提议者那边也会叫 Process 分开；353 verifywhen vs empty bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 有 hash | 不是 already ran-process | 不是 Process 也会在提议者那边叫 alone（351） |
| 是同一块 | 不是 already this-process | 不是不调本地票 already self-verified alone（813） |
| 不保证 | 不是 already processalso | 不是是空的 already skip-verify alone（812） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看请求里的 hash 不是已经对该块跑过 Process not already ran-process / not already this-process / not already processalso 正式三事（353 余量），必须分开有 hash 是不是 already ran-process interchangeable / 353 verifywhen bundled interchangeable / verifywhen-sold-as-skipped interchangeable、是同一块 是不是 already this-process interchangeable、不保证 是不是 already processalso interchangeable。可以跳过「看见有 hash 就已经 Process 过 interchangeable / 就已经对上这次 Process interchangeable / 就已经是提议者那边也会叫 Process interchangeable」。不要另写怎样写 Verify 何时调用。353 verifywhen vs empty bundled unbundling 在本页 item 3 完成（812 + 813 + 814）。

## 本页不抄

- 怎样写 Verify 何时调用、怎样写空扩展、怎样缓存 Process。
- Verify 何时调用 bundled。那是不变量 353。
- 空扩展仍会调 Verify 不是已经跳过 Verify。那是不变量 353 item 1 余量 / 812。
- 不对本进程自己发出的 Precommit 调用不是已经自己验过。那是不变量 353 item 2 余量 / 813。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
- 正确进程交出的扩展必须被正确接收者 Verify Accept。那是不变量 348。
- Process 也会在提议者那边叫。那是不变量 351。
