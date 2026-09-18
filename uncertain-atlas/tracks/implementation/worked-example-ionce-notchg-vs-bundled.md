# 例：看见 InitChain Validators-as-update is not already set-changed interchangeable / not already has-key interchangeable / not already no-set interchangeable

**层次**：实现 / InitChain Validators-as-update not already set-changed / not already has-key / not already no-set 正式三事（412 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「InitChain Validators-as-update not already set-changed / not already has-key / not already no-set 正式三事（412 余量）/ not 1093 ionce-notchg interchangeable / not 412 initonce-vs-crash bundled interchangeable」，不是 InitChain Usage 余量 bundled（412），也不是 ValidatorUpdate 用公钥认人就已经改了集合（364），也不是 InitChain 回了空名单就已经没有集合（318）。不要另写怎样写 InitChain Usage 余量。

## 官方三件事

1. **看见 Request 和 Response 的 Validators 都是 ValidatorUpdate、技术上是从空集合更新 / 看见两边都是 ValidatorUpdate 这份栏 is not already 已经改了集合 interchangeable，也不是已经 InitChain Usage 余量 bundled（412） interchangeable / 1093 ionce-notchg interchangeable / 1091 ionce-notcrash interchangeable / 412 initonce item 1 once interchangeable，也不是已经 InitChain Validators-as-update not already set-changed / not already has-key / not already no-set 正式三事 bundled（412 item 3 余量） interchangeable / 412 initonce item 3 interchangeable。**  
   官方写：Both the Request and Response include a type Validators, which is a list of ValidatorUpdate types. Technically, this is updating the validator set from the empty set。看见两边都是 ValidatorUpdate，不是已经改了集合 interchangeable——本页从 412 item 3 侧钉 not already set-changed 单句。412 initonce vs crash bundled unbundling 在本页 item 3 完成。

2. **看见技术上是从空集合更新 / 看见两边都是 ValidatorUpdate / 这份栏 is not already 已经带了公钥 interchangeable，也不是已经 InitChain Usage 余量 bundled（412） interchangeable / 1093 ionce-notchg interchangeable / 412 initonce item 2 decide interchangeable / 1092 ionce-notempty interchangeable，也不是已经 ValidatorUpdate 用公钥认人就已经改了集合 interchangeable / 364 validator interchangeable。**  
   官方把技术上从空集合更新和已经带了公钥分开。看见技术上是从空集合更新，不是已经带了公钥 interchangeable。本页钉 not already has-key 单句。

3. **看见有更新结构 / 看见两边都是 ValidatorUpdate / 这份栏 is not already 已经没有集合 interchangeable，也不是已经 InitChain Usage 余量 bundled（412） interchangeable / 1093 ionce-notchg interchangeable / 1091 ionce-notcrash interchangeable，也不是已经 InitChain 回了空名单就已经没有集合 interchangeable / 318 validatorupdate interchangeable。**  
   官方把有更新结构和已经没有集合分开。看见有更新结构，不是已经没有集合 interchangeable。412 initonce vs crash bundled unbundling 在本页 item 3 完成。

怎样写 InitChain Usage 余量、怎样决定接受创世集合、怎样从空集合更新是规范里的做法，本页不抄。

## 官方为什么这样拆

- **InitChain Validators-as-update not already set-changed ≠ 已经改了集合 interchangeable：** 官方把两边都是 ValidatorUpdate、技术上从空集合更新和已经改了集合分开。
- **看见技术上是从空集合更新 not already has-key ≠ 已经带了公钥 interchangeable：** 官方把从空集合更新和已经带了公钥分开。
- **看见有更新结构 not already no-set ≠ 已经没有集合 interchangeable：** 官方把有更新结构和已经没有集合分开；412 initonce vs crash bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Request 和 Response 的 Validators 都是 ValidatorUpdate、技术上是从空集合更新 | 不是已经改了集合 | 不是 ValidatorUpdate 用公钥认人就已经改了集合（364） |
| 看见技术上是从空集合更新 | 不是已经带了公钥 | 不是 InitChain 回了空名单就已经没有集合（318） |
| 看见有更新结构 | 不是已经没有集合 | 不是创世时只调一次就已经是崩溃后再调（1091） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Validators-as-update not already set-changed / not already has-key / not already no-set 正式三事（412 余量），必须分开是不是已经改了集合、是不是已经带了公钥、是不是已经没有集合。可以跳过「看见填了 InitChain Usage 余量就已经是崩溃后再调」。不要另写怎样写 InitChain Usage 余量。412 initonce vs crash bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 InitChain Usage 余量、怎样决定接受创世集合、怎样从空集合更新。
- InitChain Usage 余量 bundled。那是不变量 412。
- ValidatorUpdate 用公钥认人就已经改了集合。那是不变量 364。
- InitChain 回了空名单就已经没有集合。那是不变量 318。
