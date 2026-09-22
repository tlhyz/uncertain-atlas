# 例：看见 h_e 必须高于当前 / 看见升级之后才能写启用高度 / 看见最早 h_u+1 is not already already writecurrent interchangeable / already height-H-prepare interchangeable / already settled interchangeable

**层次**：实现 / h_e 必须高于当前不是已经能写成当前高度 not already writecurrent / not already height-H-prepare / not already settled 正式三事（346 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Application configuration required to switch to ABCI 2.0。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「h_e 必须高于当前不是已经能写成当前高度 not already writecurrent / not already height-H-prepare / not already settled 正式三事（346 余量）/ not 792 abci20-notwritecurrent interchangeable / not 346 abci20upgrade bundled interchangeable」，不是 ABCI 2.0 协调升级 bundled（346），也不是必须协调升级不是已经只改 VoteExtensionsEnableHeight（791 item 1 余量）或引擎按当前高度决定存什么要什么不是已经按创世配好了（793 item 3 余量）。不要另写怎样做协调升级。

## 官方三件事

规范把 Requirements 里升级之后才能把启用高度写成高于当前的 *h<sub>e</sub>* 和「已经是升级过了就已经能写成当前高度 interchangeable / 已经是必须比当前高就已经是到了 H 才 Prepare 带扩展 interchangeable / 已经是升级过了就已经交差 interchangeable / 已经是 abci20upgrade bundled interchangeable」分开写成三件独立的实现事，不是「看见 h_e 必须高于当前就已经能写成当前高度 interchangeable / 就已经是到了 H 才 Prepare 带扩展 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见升级之后 *h<sub>u</sub>* 才能把 `VoteExtensionsEnableHeight` 写成 *h<sub>e</sub>* / 看见 *h<sub>e</sub>* 必须高于当前（最早 *h<sub>u</sub>*+1） / 看见必须比当前链高度高 is not already 已经能写成当前高度 interchangeable / 已经 writecurrent interchangeable / 已经写成当前交差 interchangeable / 346 abci20upgrade bundled interchangeable / 330 veheight interchangeable / abci20upgrade-sold-as-height interchangeable，也不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable / 792 abci20-notwritecurrent interchangeable / 346 abci20 item 2 interchangeable，也不是已经 h_e 必须高于当前不是已经能写成当前高度 not already writecurrent / not already height-H-prepare / not already settled 正式三事 bundled（346 item 2 余量） interchangeable / 346 abci20 item 2 interchangeable，也不是已经必须协调升级不是已经只改字段（791） interchangeable / 793 abci20-notgenesiscfg interchangeable / 58 enable-height interchangeable，也不是已经到了 H 就已经 Prepare 带了扩展（330） interchangeable。**  
   官方写：协调升级发生在高度 *h<sub>u</sub>* 之后，这个参数 **可以** 写成某个 *h<sub>e</sub>*，但 **必须** 高于当前链高度。最早的 *h<sub>e</sub>* 是 *h<sub>u</sub>*+1。看见升级过了，不是已经能写成当前这一高。看见 *h<sub>e</sub>* 必须高于当前，不是已经 writecurrent interchangeable——346 钉 bundled 三事，本页从 item 2 侧钉 not already writecurrent 单句。看见必须比当前链高度高，不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable——346 钉 bundled，本页钉 item 2 第一件事。看见最早 *h<sub>u</sub>*+1，不是已经必须协调升级不是已经只改字段（791） interchangeable——791 另钉 item 1。346 abci20 vs height bundled unbundling 在本页 item 2 续。

2. **看见必须比当前高 / 看见最早 *h<sub>u</sub>*+1 / 看见启用高度要晚于当前 is not already 已经是到了 H 才 Prepare 带扩展那种切换 interchangeable / 已经 height-H-prepare interchangeable / 已经 H Prepare 交差 interchangeable / 346 abci20upgrade bundled interchangeable / 330 veheight-sold-as-prepared interchangeable，也不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable / 792 abci20-notwritecurrent interchangeable / 346 abci20 item 1 协调升级 interchangeable / 346 abci20 item 3 当前高度 interchangeable，也不是已经 h_e 必须高于当前不是已经能写成当前高度 not already writecurrent / not already height-H-prepare / not already settled 正式三事 bundled（346 item 2 余量） interchangeable / 346 abci20 item 2 interchangeable，也不是已经能写成当前高度（本页第一件事） interchangeable。**  
   官方写：看见必须比当前高，不是已经是 330 那种到了 H 才 Prepare 带扩展。看见最早 *h<sub>u</sub>*+1，不是已经 height-H-prepare interchangeable——本页钉 not already height-H-prepare 单句。看见启用高度要晚于当前，不是已经能写成当前高度（本页第一件事） interchangeable——三件事分开钉。346 abci20 vs height bundled unbundling 在本页 item 2 续。

3. **看见升级过了 / 看见协调升级已经发生在 *h<sub>u</sub>* 之后 / 看见可以开始写 *h<sub>e</sub>* is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经写高度交差 interchangeable / 346 abci20upgrade bundled interchangeable / 791 abci20-notonlyveheight interchangeable，也不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable / 792 abci20-notwritecurrent interchangeable / 346 abci20 item 1 / 346 abci20 item 3，也不是已经 h_e 必须高于当前不是已经能写成当前高度 not already writecurrent / not already height-H-prepare / not already settled 正式三事 bundled（346 item 2 余量） interchangeable / 346 abci20 item 2 interchangeable，也不是已经能写成当前高度（本页第一件事） interchangeable / 已经是到了 H 才 Prepare 带扩展（本页第二件事） interchangeable。**  
   官方写：看见升级过了，不是已经交差。看见协调升级已经发生在 *h<sub>u</sub>* 之后，不是已经 settled interchangeable——本页钉 not already settled 单句。看见可以开始写 *h<sub>e</sub>*，不是已经是到了 H 才 Prepare 带扩展（本页第二件事） interchangeable——三件事分开钉。346 abci20 vs height bundled unbundling 在本页 item 2 续。

怎样做协调升级、怎样设 *h<sub>e</sub>*、默认取值是规范里的做法，本页不抄。ABCI 2.0 协调升级 bundled（346）、必须协调升级不是已经只改 VoteExtensionsEnableHeight（346 item 1 余量 / 791）、引擎按当前高度决定存什么要什么不是已经按创世配好了（346 item 3 余量 / 793）、到了 H 就已经 Prepare 带了扩展（330）、写成 0 就已经启用 PBTS（343）、治理改 enable-height 会 panic（58）是另外那套，本页不抄。

## 官方为什么这样拆

- **h_e 必须高于当前 not already writecurrent ≠ 346 / 330 interchangeable：** 官方把升级之后才能写启用高度和写成当前这一高分开。
- **必须比当前高 not already height-H-prepare ≠ 已经是到了 H 才 Prepare 带扩展 interchangeable：** 官方把必须比当前高和已经是 330 那种到了 H 才 Prepare 带扩展分开。
- **升级过了 not already settled ≠ 已经交差 interchangeable：** 官方把升级过了和已经交差分开；346 abci20 vs height bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| h_e 必须高于当前 | 不是 already writecurrent | 不是到了 H 就已经 Prepare 带了扩展 alone（330） |
| 必须比当前高 | 不是 already height-H-prepare | 不是写成 0 就已经启用 PBTS alone（343） |
| 升级过了 | 不是 already settled | 不是必须协调升级就已经只改字段 alone（791） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 h_e 必须高于当前不是已经能写成当前高度 not already writecurrent / not already height-H-prepare / not already settled 正式三事（346 余量），必须分开 h_e 必须高于当前 是不是 already writecurrent interchangeable / 346 abci20upgrade bundled interchangeable / abci20upgrade-sold-as-height interchangeable、必须比当前高 是不是 already height-H-prepare interchangeable、升级过了 是不是 already settled interchangeable。可以跳过「看见必须比当前高就已经能写成当前 interchangeable / 就已经是到了 H 才 Prepare 带扩展 interchangeable / 就已经交差 interchangeable」。不要另写怎样做协调升级。346 abci20 vs height bundled unbundling 在本页 item 2 续（791 + 792）；续 [`worked-example-abci20-notgenesiscfg-vs-bundled.md`](worked-example-abci20-notgenesiscfg-vs-bundled.md)（不变量 793 item 3）；完成见 793。

## 本页不抄

- 怎样做协调升级、怎样设 *h<sub>e</sub>*、默认取值。
- ABCI 2.0 协调升级 bundled。那是不变量 346。
- 必须协调升级不是已经只改 VoteExtensionsEnableHeight。那是不变量 346 item 1 余量 / 791。
- 引擎按当前高度决定存什么要什么不是已经按创世配好了。那是不变量 346 item 3 余量 / 793。
- 到了 H 就已经 Prepare 带了扩展。那是不变量 330。
- 写成 0 就已经启用 PBTS。那是不变量 343。
- 治理改 enable-height 会 panic。那是不变量 58。
