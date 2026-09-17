# 例：看见 expected persist at end of this call is not already Commit no params means persisted interchangeable / not already signal means done interchangeable / not already Finalize+Commit settled interchangeable

**层次**：实现 / Commit Usage expected persist at end of this call not Commit no params means persisted / not signal means done / not Finalize+Commit settled 正式三事（481 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Commit Usage expected persist at end of this call not Commit no params means persisted / not signal means done / not Finalize+Commit settled 正式三事（481 余量）/ not 702 commitpersist-notempty interchangeable / not 481 commitpersist-vs-finalize bundled interchangeable」，不是 Commit Usage persist signal 正式三事 bundled（481），也不是 Commit 空请求（399）或 Finalize 落盘禁令（335）。不要另写怎样落盘。

## 官方三件事

1. **看见 Application is expected to persist its state at the end of this call, before returning from `Commit` / 看见应在这次 Commit 返回前落盘应用状态 / expected is not already 已经 Commit 不带参数就等于已经落盘（399） interchangeable / 399 commitnoparam interchangeable，也不是已经 Commit Usage persist signal 正式三事 bundled（481） interchangeable / 702 commitpersist-notempty interchangeable / 701 commitpersist-notfinalize interchangeable / 481 commitpersist item 1 signal interchangeable，也不是已经 expected persist not Commit no params / not signal means done / not Finalize+Commit settled 正式三事 bundled（481 item 2 余量） interchangeable / 481 commitpersist item 2 interchangeable。**  
   官方 Usage 写：Application is expected to persist its state at the end of this call, before returning from Commit。看见 expected at end of this call，不是已经 Commit 空请求就等于已经落盘 interchangeable——399 钉空请求，本页从 481 item 2 侧钉 not Commit no params 单句。481 commitpersist vs finalize bundled unbundling 在本页 item 2 续。

2. **看见返回前落盘 / 看见 expected at end of this call / 看见 Usage 这句 is not already 已经 persist signal 就已经交差 interchangeable / 701 commitpersist-notfinalize interchangeable，也不是已经 Commit Usage persist signal 正式三事 bundled（481） interchangeable / 702 commitpersist-notempty interchangeable / 481 commitpersist item 3 Historical blocks interchangeable / 703 commitpersist-nothistorical interchangeable。**  
   官方把 Usage expected at end of this call 单句和 signal 就已经交差路径分开——481 bundled 第二件事常与第一件事混成「看见应在 Commit 里做 就已经 signal 交差 interchangeable」，本页钉 not signal means done 单句。

3. **看见应在 Commit 里做 / 看见 Usage 这句 / expected is not already 已经 Finalize + Commit 那种已经交差（335） interchangeable / 335 finpersist interchangeable，也不是已经 Commit Usage persist signal 正式三事 bundled（481） interchangeable / 702 commitpersist-notempty interchangeable / 701 commitpersist-notfinalize interchangeable。**  
   官方把 Usage expected at end of this call 单句和 Finalize+Commit 已经交差路径分开。看见应在 Commit 返回前落盘，不是已经 Finalize 改了就已经落盘 interchangeable。481 commitpersist vs finalize bundled unbundling 在本页 item 2 续。

怎样落盘、怎样填 retain_height、怎样开 state sync 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **expected persist not Commit no params means persisted ≠ 399 interchangeable：** 官方把应在这次 Commit 返回前落盘和 Commit 空请求就等于落盘分开。
- **expected persist not signal means done ≠ 481 item 1 interchangeable：** 官方把 expected at end of this call 和 persist signal 就已经交差分开。
- **expected persist not Finalize+Commit settled ≠ 335 interchangeable：** 官方把 Usage expected 单句和 Finalize 改了就已经落盘分开；481 commitpersist vs finalize bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Expected persist at end of this call | 不是 Commit 不带参数就等于已经落盘（399） | 不是 persist signal 单句（701/481 item 1） |
| 看见返回前落盘 | 不是 signal 就已经交差 | 不是 Historical blocks（703/481 item 3） |
| 看见 Usage 这句 | 不是 Finalize+Commit 已经交差（335） | 不是 Commit Usage persist signal bundled（481） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage expected persist at end of this call not Commit no params means persisted / not signal means done / not Finalize+Commit settled 正式三事（481 余量），必须分开 expected 是不是 Commit 空请求就等于落盘 interchangeable / 399、是不是 signal 就已经交差、是不是 Finalize+Commit 已经交差 interchangeable / 335。可以跳过「看见叫了 Commit 就已经交差」。不要另写怎样落盘。481 commitpersist vs finalize bundled unbundling 在本页 item 2 续；完成 [`worked-example-commitpersist-nothistorical-vs-bundled.md`](worked-example-commitpersist-nothistorical-vs-bundled.md)（不变量 703 item 3）。

## 本页不抄

- 怎样落盘、怎样填 retain_height、怎样开 state sync。
- Commit Usage persist signal 正式三事 bundled。那是不变量 481。
- Signal persist application state。那是不变量 481 item 1 余量 / 701。
- Historical blocks required（persist 语境）。那是不变量 481 item 3 余量 / 703。
- Commit 空请求。那是不变量 399。
- FinalizeBlock 落盘禁令。那是不变量 335。
