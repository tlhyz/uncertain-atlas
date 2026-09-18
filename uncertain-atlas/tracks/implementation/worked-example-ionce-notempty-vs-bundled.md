# 例：看见 InitChain may-choose-set is not already no-set interchangeable / not already genesis-used interchangeable / not already app-checked interchangeable

**层次**：实现 / InitChain may-choose-set not already no-set / not already genesis-used / not already app-checked 正式三事（412 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「InitChain may-choose-set not already no-set / not already genesis-used / not already app-checked 正式三事（412 余量）/ not 1092 ionce-notempty interchangeable / not 412 initonce-vs-crash bundled interchangeable」，不是 InitChain Usage 余量 bundled（412），也不是 InitChain 回了空名单就已经没有集合（318），也不是 ValidatorUpdate 用公钥认人就已经改了集合（364）。不要另写怎样写 InitChain Usage 余量。

## 官方三件事

1. **看见应用可以决定接受创世验证者集合或用创世应用信息算出另一套 / 看见能决定 这份栏 is not already 已经没有集合 interchangeable，也不是已经 InitChain Usage 余量 bundled（412） interchangeable / 1092 ionce-notempty interchangeable / 1091 ionce-notcrash interchangeable / 412 initonce item 1 once interchangeable，也不是已经 InitChain may-choose-set not already no-set / not already genesis-used / not already app-checked 正式三事 bundled（412 item 2 余量） interchangeable / 412 initonce item 2 interchangeable。**  
   官方写：The application can decide to accept the initial validator set or use a different one, potentially computed based on the initial application state。看见能决定，不是已经没有集合 interchangeable——本页从 412 item 2 侧钉 not already no-set 单句。412 initonce vs crash bundled unbundling 在本页 item 2 续。

2. **看见能算另一套 / 看见能决定 / 这份栏 is not already 已经用了创世文件里的验证者 interchangeable，也不是已经 InitChain Usage 余量 bundled（412） interchangeable / 1092 ionce-notempty interchangeable / 412 initonce item 3 empty-update interchangeable / 1093 ionce-notchg interchangeable，也不是已经 InitChain 回了空名单就已经没有集合 interchangeable / 318 validatorupdate interchangeable。**  
   官方把能算另一套和已经用了创世文件里的验证者分开。看见能算另一套，不是已经用了创世文件里的验证者 interchangeable。本页钉 not already genesis-used 单句。

3. **看见有创世应用信息 / 看见能决定 / 这份栏 is not already 已经验过应用状态 interchangeable，也不是已经 InitChain Usage 余量 bundled（412） interchangeable / 1092 ionce-notempty interchangeable / 1091 ionce-notcrash interchangeable，也不是已经 ValidatorUpdate 用公钥认人就已经改了集合 interchangeable / 364 validator interchangeable。**  
   官方把有创世应用信息和已经验过应用状态分开。看见有创世应用信息，不是已经验过应用状态 interchangeable。412 initonce vs crash bundled unbundling 在本页 item 2 续。

怎样写 InitChain Usage 余量、怎样决定接受创世集合、怎样从空集合更新是规范里的做法，本页不抄。

## 官方为什么这样拆

- **InitChain may-choose-set not already no-set ≠ 已经没有集合 interchangeable：** 官方把应用自己决定用哪一套和回了空名单就已经没有集合分开。
- **看见能算另一套 not already genesis-used ≠ 已经用了创世文件里的验证者 interchangeable：** 官方把能算另一套和已经用了创世文件里的验证者分开。
- **看见有创世应用信息 not already app-checked ≠ 已经验过应用状态 interchangeable：** 官方把有创世应用信息和已经验过应用状态分开；412 initonce vs crash bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 应用可以决定接受创世验证者集合或用创世应用信息算出另一套 | 不是已经没有集合 | 不是 InitChain 回了空名单就已经没有集合（318） |
| 看见能算另一套 | 不是已经用了创世文件里的验证者 | 不是 ValidatorUpdate 用公钥认人就已经改了集合（364） |
| 看见有创世应用信息 | 不是已经验过应用状态 | 不是两边都是 ValidatorUpdate 就已经改了集合（1093） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain may-choose-set not already no-set / not already genesis-used / not already app-checked 正式三事（412 余量），必须分开是不是已经没有集合、是不是已经用了创世文件里的验证者、是不是已经验过应用状态。可以跳过「看见填了 InitChain Usage 余量就已经是崩溃后再调」。不要另写怎样写 InitChain Usage 余量。412 initonce vs crash bundled unbundling 在本页 item 2 续；续 [`worked-example-ionce-notchg-vs-bundled.md`](worked-example-ionce-notchg-vs-bundled.md)（不变量 1093 item 3）。

## 本页不抄

- 怎样写 InitChain Usage 余量、怎样决定接受创世集合、怎样从空集合更新。
- InitChain Usage 余量 bundled。那是不变量 412。
- InitChain 回了空名单就已经没有集合。那是不变量 318。
- ValidatorUpdate 用公钥认人就已经改了集合。那是不变量 364。
