# 例：看见空扩展仍会调 Verify 不是已经跳过 Verify；看见不对本进程自己发出的 Precommit 调用不是已经自己验过；看见请求里的 hash 不是已经对该块跑过 Process

**层次**：实现 / Verify 何时调用。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「空扩展仍会调 Verify 不是已经跳过 Verify / 不对本进程自己发出的 Precommit 调用不是已经自己验过 / 请求里的 hash 不是已经对该块跑过 Process」，不是验签拒收整张预提交就已经是块非法，也不是正确进程交出的扩展必须被正确接收者 Verify Accept。不要另写怎样写 Verify 何时调用。353 verifywhen vs empty bundled unbundling 续（812+813）；精读 [`worked-example-empty-notskip-vs-bundled.md`](worked-example-empty-notskip-vs-bundled.md)（不变量 812 item 1）；精读 [`worked-example-empty-notlocal-vs-bundled.md`](worked-example-empty-notlocal-vs-bundled.md)（不变量 813 item 2）。

## 官方三件事

规范把空扩展仍会调 Verify、不调本地票、hash 不保证已经 Process 写成三件独立的实现事，不是「看见空扩展就已经跳过 Verify、已经自己验过、已经对该块跑过 Process」一件事：

1. **看见空扩展（0 长度）引擎仍会调 `VerifyVoteExtension` / 看见发送方选择不扩 不是已经跳过 Verify，也不是已经是空扩展仍验签。**  
   官方写：CometBFT 即使是 0 长度扩展也会调 `VerifyVoteExtension`。空扩展表示发送方选择不扩。看见是空的，不是已经跳过 Verify。看见选择不扩，不是已经不用调。看见仍会调，不是已经是空扩展仍验签。
2. **看见 `VerifyVoteExtension` 不对本进程自己发出的 Precommit 调用 / 看见是本地票 不是已经自己验过，也不是已经 Accept。**  
   官方写：`VerifyVoteExtension` 不对本进程自己发出的 Precommit 调用。看见不调本地票，不是已经自己验过。看见是自己签的，不是已经 Accept。看见跳过本地，不是已经过了 Req 6。
3. **看见请求里的 `hash` / 看见指向某块 不是已经对该块跑过 `ProcessProposal`，也不是已经是提议者那边也会叫 Process。**  
   官方写：请求里的 `hash` 指向某块，不保证这块已经通过 `ProcessProposal` 暴露给应用。看见有 hash，不是已经 Process 过。看见是同一块，不是已经对上这次 Process。看见不保证，不是已经是提议者那边也会叫 Process。

怎样写 Verify 何时调用、怎样写空扩展、怎样缓存 Process 是规范里的做法，本页不抄。验签拒收整张预提交是不变量 34，本页不抄。

## 官方为什么这样拆

- **空扩展仍会调 Verify ≠ 已经跳过 Verify：** 官方把仍会调 Verify 和空扩展仍验签分开。
- **不对本进程自己发出的 Precommit 调用 ≠ 已经自己验过：** 官方把不调本地票和已经 Accept 分开。
- **请求里的 hash ≠ 已经对该块跑过 Process：** 官方把有 hash 和已经 Process 过分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 空扩展仍会调 Verify | 不是已经跳过 Verify | 不是验签拒收整张预提交就已经是块非法（34） |
| 不对本进程自己发出的 Precommit 调用 | 不是已经自己验过 | 不是正确进程交出的扩展必须被正确接收者 Verify Accept（348） |
| 请求里的 hash | 不是已经对该块跑过 Process | 不是 Process 也会在提议者那边叫（351） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见空扩展就已经跳过 Verify、已经自己验过、已经对该块跑过 Process」，必须分开空扩展仍会调 Verify 是不是已经跳过 Verify、不对本进程自己发出的 Precommit 调用是不是已经自己验过、请求里的 hash 是不是已经对该块跑过 Process。可以跳过「看见空扩展就已经跳过 Verify」。不要另写怎样写 Verify 何时调用。353 verifywhen vs empty bundled unbundling 续（812+813）。

## 本页不抄

- 怎样写 Verify 何时调用、怎样写空扩展、怎样缓存 Process。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
- 正确进程交出的扩展必须被正确接收者 Verify Accept。那是不变量 348。
- Process 也会在提议者那边叫。那是不变量 351。
