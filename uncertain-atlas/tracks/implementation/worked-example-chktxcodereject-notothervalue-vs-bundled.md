# 例：看见 CheckTx attributes no other value to the response code is not already CheckTx Data used interchangeable / not already optional bundled interchangeable / not already validate-no-apply bundled interchangeable

**层次**：实现 / CheckTx Usage no other value to the response code not CheckTx Data used / not optional bundled / not validate-no-apply bundled 正式三事（489 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx Usage no other value to the response code not CheckTx Data used / not optional bundled / not validate-no-apply bundled 正式三事（489 余量）/ not 688 chktxcodereject-notothervalue interchangeable / not 489 chktxcodereject-vs-proposal bundled interchangeable」，不是 CheckTx Usage Code≠0 rejected 正式三事 bundled（489），也不是 CheckTx 回包 Data（317）或 Technically optional（373）。不要另写怎样挑回包码、怎样写广播谓词。

## 官方三件事

规范把 CheckTx Usage 里 CometBFT attributes no other value to the response code 和「已经 CheckTx 回包 `Data` 就被引擎用了（317） interchangeable / 已经 CheckTx 技术上可选（373） bundled 第二句 interchangeable / 已经 CheckTx Usage validate-no-apply（486） bundled 第三件事 interchangeable」分开写成三件独立的实现事，不是「看见 no other value 就已经 Data used interchangeable / 就已经 optional bundled interchangeable / 就已经 validate-no-apply bundled interchangeable」一件事：

1. **看见 CometBFT attributes no other value to the response code / 看见引擎对 CheckTx 回包码不再赋予别的含义 / no other value is not already 已经 CheckTx 回包 `Data` 就被引擎用了（317） interchangeable / 317 priority / Data interchangeable / 已经回包栏就被引擎读 interchangeable，也不是已经 CheckTx Usage Code≠0 rejected 正式三事 bundled（489） interchangeable / 688 chktxcodereject-notothervalue interchangeable / 686 chktxcodereject-notgossip interchangeable / 489 chktxcodereject item 1 rejected interchangeable，也不是已经 no other value not CheckTx Data used / not optional bundled / not validate-no-apply bundled 正式三事 bundled（489 item 3 余量） interchangeable / 489 chktxcodereject item 3 interchangeable。**  
   官方 Usage 写：CometBFT attributes no other value to the response code。看见 no other value，不是已经 CheckTx 回包 `Data` 就被引擎用了 interchangeable——317 钉回包 Data / Priority，本页从 489 item 3 侧钉 not Data used 单句。489 chktxcodereject vs proposal bundled unbundling 在本页 item 3 完成。

2. **看见 attributes no other value / 看见引擎不再赋予别的含义 / 看见 response code is not already 已经 CheckTx 技术上可选（373） bundled 第二句 interchangeable / 373 checktxopt interchangeable / 已经可以不跑 CheckTx interchangeable / 已经四门已经结算 interchangeable，也不是已经 CheckTx Usage Code≠0 rejected 正式三事 bundled（489） interchangeable / 688 chktxcodereject-notothervalue interchangeable / 489 chktxcodereject item 2 not in proposal interchangeable / 687 chktxcodereject-notproposal interchangeable。**  
   官方把 Usage Code 语义单句和 optional bundled 路径分开——489 bundled 第三件事常与 373 混成「看见 no other value 就已经 optional bundled 就代表 Code 语义交差 interchangeable」，本页钉 not optional bundled 单句。看见 attributes no other value，不是已经可以不跑 CheckTx interchangeable——373 钉 optional vs block processing，本页钉 Usage Code 语义。

3. **看见 no other value to the response code / 看见 Usage 这句 / 看见 response code is not already 已经 CheckTx Usage validate-no-apply（486） bundled 第三件事 interchangeable / 486 chktxvalidate interchangeable / 682 chktxvalidate-notoptional interchangeable / 已经 Technically optional + Code≠0 正式三事 bundled interchangeable / 已经 Finalize `tx_results[i].Code == 0` only if fully valid（464） interchangeable，也不是已经 CheckTx Usage Code≠0 rejected 正式三事 bundled（489） interchangeable / 688 chktxcodereject-notothervalue interchangeable / 686 chktxcodereject-notgossip interchangeable。**  
   官方把 Usage Code≠0 拒路径和 validate-no-apply bundled 第三件事分开——489 bundled 第三件事常与 486 混成「看见 Usage 这句 就已经 validate-no-apply bundled interchangeable」，本页钉 not validate-no-apply bundled 单句。看见 response code，不是已经 Finalize Code==0 only if fully valid interchangeable——464/585 钉 Finalize 回执，本页钉 CheckTx Usage item 3。489 chktxcodereject vs proposal bundled unbundling 在本页 item 3 完成。

怎样做广播过滤、怎样写 CheckTx 回包码、怎样区分池门 Code 与 Finalize Code 是规范里的做法，本页不抄。CheckTx Usage Code≠0 rejected 正式三事 bundled（489）、Code≠0 will be rejected（489 item 1 余量 / 686）、will not be in proposal（489 item 2 余量 / 687）、CheckTx 回包 Data（317）、Technically optional（373）、validate-no-apply（486）是另外那套，本页不抄。

## 官方为什么这样拆

- **no other value not CheckTx Data used ≠ 317 interchangeable：** 官方把 Usage Code 语义和回包 Data 就被引擎用了路径分开。
- **no other value not optional bundled ≠ 373 checktxopt interchangeable：** 官方把 Usage Code 语义单句和 Technically optional bundled 路径分开。
- **no other value not validate-no-apply bundled ≠ 486 / 682 interchangeable：** 官方把 Usage Code≠0 拒路径和 validate-no-apply bundled 第三件事分开；489 chktxcodereject vs proposal bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| no other value to the response code | 不是 CheckTx Data 已被引擎用了（317） | 不是 Code≠0 rejected 单句（686/489 item 1） |
| 看见引擎不再赋予别的含义 | 不是 optional bundled（373） | 不是 will not be in proposal（687/489 item 2） |
| 看见 Usage 这句 | 不是 validate-no-apply bundled（486/682） | 不是 CheckTx Usage Guardian（490） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage no other value to the response code not CheckTx Data used / not optional bundled / not validate-no-apply bundled 正式三事（489 余量），必须分开 no other value 是不是 Data 已被引擎用了 interchangeable / 317、是不是 optional bundled interchangeable / 373、是不是 validate-no-apply bundled interchangeable / 486。可以跳过「看见引擎不再赋予别的含义就已经交差」。不要另写怎样挑回包码。489 chktxcodereject vs proposal bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样做广播过滤、怎样写 CheckTx 回包码、怎样区分池门 Code 与 Finalize Code。
- CheckTx Usage Code≠0 rejected 正式三事 bundled。那是不变量 489。
- Code≠0 will be rejected。那是不变量 489 item 1 余量 / 686。
- will not be included in a proposal block。那是不变量 489 item 2 余量 / 687。
- CheckTx 回包 `Data` 已被引擎用了。那是不变量 317。
- CheckTx 技术上可选。那是不变量 373。
- CheckTx Usage validate-no-apply。那是不变量 486。
