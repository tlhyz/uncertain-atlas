# 例：看见是空的 / 看见选择不扩 / 看见仍会调 is not already already skip-verify interchangeable / already no-call interchangeable / already empty-signed interchangeable

**层次**：实现 / 空扩展仍会调 Verify 不是已经跳过 Verify not already skip-verify / not already no-call / not already empty-signed 正式三事（353 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「空扩展仍会调 Verify 不是已经跳过 Verify not already skip-verify / not already no-call / not already empty-signed 正式三事（353 余量）/ not 812 empty-notskip interchangeable / not 353 verifywhen bundled interchangeable」，不是 Verify 何时调用 bundled（353），也不是不对本进程自己发出的 Precommit 调用不是已经自己验过（813 item 2 余量）或请求里的 hash 不是已经对该块跑过 Process（814 item 3 余量）。不要另写怎样写 Verify 何时调用。

## 官方三件事

规范把 Methods 里 CometBFT 即使是 0 长度扩展也会调 `VerifyVoteExtension`、空扩展表示发送方选择不扩 和「已经是空的就已经跳过 Verify interchangeable / 已经是选择不扩就已经不用调 interchangeable / 已经是仍会调就已经是空扩展仍验签 interchangeable / 已经是 verifywhen bundled interchangeable」分开写成三件独立的实现事，不是「看见是空的就已经跳过 Verify interchangeable / 就已经不用调 interchangeable / 就已经是空扩展仍验签 interchangeable」一件事：

1. **看见空扩展（0 长度）引擎仍会调 `VerifyVoteExtension` / 看见是空的 / 看见 0 长度扩展 is not already 已经跳过 Verify interchangeable / 已经 skip-verify interchangeable / 已经跳过 Verify 交差 interchangeable / 353 verifywhen bundled interchangeable / 34 vote-extension-block interchangeable / verifywhen-sold-as-skipped interchangeable，也不是已经 Verify 何时调用 bundled（353） interchangeable / 812 empty-notskip interchangeable / 353 verifywhen item 1 interchangeable，也不是已经空扩展仍会调 Verify 不是已经跳过 Verify not already skip-verify / not already no-call / not already empty-signed 正式三事 bundled（353 item 1 余量） interchangeable / 353 verifywhen item 1 interchangeable，也不是已经自己验过（813） interchangeable / 814 hash-notprocess interchangeable / 348 req6coherence interchangeable，也不是已经验签拒收整张预提交就已经是块非法（34） interchangeable。**  
   官方写：CometBFT 即使是 0 长度扩展也会调 `VerifyVoteExtension`。看见是空的，不是已经跳过 Verify。看见是空的，不是已经 skip-verify interchangeable——353 钉 bundled 三事，本页从 item 1 侧钉 not already skip-verify 单句。看见空扩展仍会调 Verify，不是已经 Verify 何时调用 bundled（353） interchangeable——353 钉 bundled，本页钉 item 1 第一件事。看见是空的，不是已经自己验过（813） interchangeable——813 另钉 item 2。看见是空的，不是已经验签拒收整张预提交就已经是块非法（34） interchangeable——34 另钉。353 verifywhen vs empty bundled unbundling 在本页 item 1 启动。

2. **看见发送方选择不扩 / 看见选择不扩 / 看见不扩 is not already 已经不用调 interchangeable / 已经 no-call interchangeable / 已经不用调交差 interchangeable / 353 verifywhen bundled interchangeable / 348 req6coherence interchangeable，也不是已经 Verify 何时调用 bundled（353） interchangeable / 812 empty-notskip interchangeable / 353 verifywhen item 2 本地票 interchangeable / 353 verifywhen item 3 hash interchangeable，也不是已经空扩展仍会调 Verify 不是已经跳过 Verify not already skip-verify / not already no-call / not already empty-signed 正式三事 bundled（353 item 1 余量） interchangeable / 353 verifywhen item 1 interchangeable，也不是已经跳过 Verify（本页第一件事） interchangeable。**  
   官方写：空扩展表示发送方选择不扩。看见选择不扩，不是已经不用调。看见选择不扩，不是已经 no-call interchangeable——本页钉 not already no-call 单句。看见不扩，不是已经跳过 Verify（本页第一件事） interchangeable——三件事分开钉。353 verifywhen vs empty bundled unbundling 在本页 item 1 启动。

3. **看见仍会调 / 看见引擎仍会调 / 看见仍调 `VerifyVoteExtension` is not already 已经是空扩展仍验签 interchangeable / 已经 empty-signed interchangeable / 已经空扩展仍验签交差 interchangeable / 353 verifywhen bundled interchangeable / 34 vote-extension-block interchangeable，也不是已经 Verify 何时调用 bundled（353） interchangeable / 812 empty-notskip interchangeable / 353 verifywhen item 2 / 353 verifywhen item 3，也不是已经空扩展仍会调 Verify 不是已经跳过 Verify not already skip-verify / not already no-call / not already empty-signed 正式三事 bundled（353 item 1 余量） interchangeable / 353 verifywhen item 1 interchangeable，也不是已经跳过 Verify（本页第一件事） interchangeable / 已经不用调（本页第二件事） interchangeable。**  
   官方写：看见仍会调，不是已经是空扩展仍验签。看见引擎仍会调，不是已经 empty-signed interchangeable——本页钉 not already empty-signed 单句。看见仍调 `VerifyVoteExtension`，不是已经不用调（本页第二件事） interchangeable——三件事分开钉。353 verifywhen vs empty bundled unbundling 在本页 item 1 启动。

怎样写 Verify 何时调用、怎样写空扩展、怎样缓存 Process 是规范里的做法，本页不抄。Verify 何时调用 bundled（353）、不对本进程自己发出的 Precommit 调用不是已经自己验过（353 item 2 余量 / 813）、请求里的 hash 不是已经对该块跑过 Process（353 item 3 余量 / 814）、验签拒收整张预提交就已经是块非法（34）、正确进程交出的扩展必须被正确接收者 Verify Accept（348）、Process 也会在提议者那边叫（351）是另外那套，本页不抄。

## 官方为什么这样拆

- **是空的 not already skip-verify ≠ 353 / 34 interchangeable：** 官方把仍会调 Verify 和已经跳过 Verify 分开。
- **选择不扩 not already no-call ≠ 已经不用调 interchangeable：** 官方把选择不扩和已经不用调分开。
- **仍会调 not already empty-signed ≠ 已经是空扩展仍验签 interchangeable：** 官方把仍会调和已经是空扩展仍验签分开；353 verifywhen vs empty bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 是空的 | 不是 already skip-verify | 不是验签拒收整张预提交就已经是块非法 alone（34） |
| 选择不扩 | 不是 already no-call | 不是不调本地票 already self-verified alone（813） |
| 仍会调 | 不是 already empty-signed | 不是有 hash already process alone（814） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看空扩展仍会调 Verify 不是已经跳过 Verify not already skip-verify / not already no-call / not already empty-signed 正式三事（353 余量），必须分开是空的 是不是 already skip-verify interchangeable / 353 verifywhen bundled interchangeable / verifywhen-sold-as-skipped interchangeable、选择不扩 是不是 already no-call interchangeable、仍会调 是不是 already empty-signed interchangeable。可以跳过「看见是空的就已经跳过 Verify interchangeable / 就已经不用调 interchangeable / 就已经是空扩展仍验签 interchangeable」。不要另写怎样写 Verify 何时调用。353 verifywhen vs empty bundled unbundling 在本页 item 1 启动（812 + 813）；续 [`worked-example-empty-notlocal-vs-bundled.md`](worked-example-empty-notlocal-vs-bundled.md)（不变量 813 item 2）；完成见 814。

## 本页不抄

- 怎样写 Verify 何时调用、怎样写空扩展、怎样缓存 Process。
- Verify 何时调用 bundled。那是不变量 353。
- 不对本进程自己发出的 Precommit 调用不是已经自己验过。那是不变量 353 item 2 余量 / 813。
- 请求里的 hash 不是已经对该块跑过 Process。那是不变量 353 item 3 余量 / 814。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
- 正确进程交出的扩展必须被正确接收者 Verify Accept。那是不变量 348。
- Process 也会在提议者那边叫。那是不变量 351。
