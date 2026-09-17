# 例：看见诚实验证者 MAY 出满 MaxBytes is not already only default 21 MB interchangeable / not already no limit interchangeable / not already settled interchangeable

**层次**：实现 / 诚实验证者 MAY 出满 MaxBytes not already only default 21 MB / not already no limit / not already settled 正式三事（344 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「诚实验证者 MAY 出满 MaxBytes not already only default 21 MB / not already no limit / not already settled 正式三事（344 余量）/ not 882 maxbytes-overhead-not21mb interchangeable / not 344 maxbytes-overhead-vs-full bundled interchangeable」，不是 MaxBytes 开销与投递 bundled（344），也不是 -1 就按 100 MB 验已经没有上限（337），也不是四门已经结算（33）。不要另写怎样算头和证据开销。

## 官方三件事

1. **看见诚实验证者 MAY 出满 MaxBytes / 看见能广播到配置上限 这份 MAY is not already 已经只会出默认 21 MB interchangeable，也不是已经 MaxBytes 开销与投递 bundled（344） interchangeable / 882 maxbytes-overhead-not21mb interchangeable / 881 maxbytes-overhead-notfull interchangeable / 344 maxbytes item 1 扣开销 interchangeable，也不是已经诚实验证者 MAY 出满 MaxBytes not already only default 21 MB / not already no limit / not already settled 正式三事 bundled（344 item 2 余量） interchangeable / 344 maxbytes item 2 interchangeable。**  
   官方写：应用应当知道，诚实验证者可以造出并广播达到配置 `MaxBytes` 的块。看见默认能接到 21 MB，不是诚实者已经只会出那一档 interchangeable——本页从 344 item 2 侧钉 not already only default 21 MB 单句。344 maxbytes vs full bundled unbundling 在本页 item 2 续。

2. **看见写了 MAY / 看见能打到配置上限 / 这份 MAY is not already 已经没有上限 interchangeable，也不是已经 MaxBytes 开销与投递 bundled（344） interchangeable / 882 maxbytes-overhead-not21mb interchangeable / 344 maxbytes item 3 timeout interchangeable / 883 maxbytes-overhead-nottimeout interchangeable，也不是已经 -1 就按 100 MB 验已经没有上限 interchangeable / 337 minus-one interchangeable。**  
   官方把能打到配置上限和已经写成 -1、已经没有上限分开——344 bundled 第二件事常与 337 混成「看见写了 MAY 就已经只会出 21 MB 或已经没有上限 interchangeable」，本页钉 not already no limit 单句。

3. **看见写了 MAY / 看见能打到配置上限 / 这份 MAY is not already 已经交差 interchangeable，也不是已经 MaxBytes 开销与投递 bundled（344） interchangeable / 882 maxbytes-overhead-not21mb interchangeable / 881 maxbytes-overhead-notfull interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把写了 MAY 和已经打满 / 已经交差分开。看见写了 MAY，不是已经打满 interchangeable。344 maxbytes vs full bundled unbundling 在本页 item 2 续。

怎样算头 / 集合 / 证据开销、默认秒数、怎样设 `MaxBytes` 是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **诚实验证者 MAY 出满 MaxBytes not already only default 21 MB ≠ 已经只会出默认 21 MB interchangeable：** 官方把配置上限和默认 21 MB 那一档分开。
- **看见能打到配置上限 not already no limit ≠ 已经没有上限 interchangeable：** 官方把能打到配置上限和已经没有上限分开。
- **看见写了 MAY not already settled ≠ 已经交差 interchangeable：** 官方把写了 MAY 和已经交差分开；344 maxbytes vs full bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 诚实验证者 MAY 出满 MaxBytes | 不是已经只会出默认 21 MB | 不是 -1 就按 100 MB 验已经没有上限（337） |
| 看见能打到配置上限 | 不是已经没有上限 | 不是四门已经结算（33） |
| 看见写了 MAY | 不是已经交差 | 不是扣了开销就已经整块都能装（881） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看诚实验证者 MAY 出满 MaxBytes not already only default 21 MB / not already no limit / not already settled 正式三事（344 余量），必须分开是不是已经只会出默认 21 MB、是不是已经没有上限、是不是已经交差。可以跳过「看见写了 MAY 就已经只会出 21 MB」。不要把 21 MB 当不确定常数。不要另写怎样算头和证据开销。344 maxbytes vs full bundled unbundling 在本页 item 2 续；续 [`worked-example-maxbytes-overhead-nottimeout-vs-bundled.md`](worked-example-maxbytes-overhead-nottimeout-vs-bundled.md)（不变量 883 item 3）。

## 本页不抄

- 怎样算头 / 集合 / 证据开销、默认秒数、怎样设 `MaxBytes`。
- MaxBytes 开销与投递 bundled。那是不变量 344。
- MaxBytes 减去头集合证据才是交易上限。那是不变量 344 item 1 余量 / 881。
- -1 就按 100 MB 验已经没有上限。那是不变量 337。
- 四门已经结算。那是不变量 33。
