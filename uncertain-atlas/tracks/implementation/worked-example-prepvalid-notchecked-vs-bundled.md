# 例：看见 engine does NOT recheck duplicate txs is not already checked interchangeable / not already app-level replay protection interchangeable / not already pool dedup interchangeable

**层次**：实现 / Prepare 回包校验 no extra checks not already checked / not app-level replay / not pool dedup 正式三事（357 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Prepare 回包校验 no extra checks not already checked / not app-level replay / not pool dedup 正式三事（357 余量）/ not 716 prepvalid-notchecked interchangeable / not 357 prepare-valid-vs-checked bundled interchangeable」，不是 Prepare 回包校验 bundled（357），也不是 Prepare Usage no checks / crash / nondet bundled（504）或内存池去重（313）。不要另写怎样再验 Prepare 回包。

## 官方三件事

1. **看见引擎没有再验重复交易 / 看见回了提案 / CometBFT 不再做额外有效性检查，例如查有没有重复交易 / no checks is not already 已经验过重复 interchangeable，也不是已经 Prepare 回包校验 bundled（357） interchangeable / 716 prepvalid-notchecked interchangeable / 717 prepvalid-notcrash interchangeable / 357 preparevalid item 2 crash interchangeable，也不是已经 no extra checks not already checked / not app-level replay / not pool dedup 正式三事 bundled（357 item 1 余量） interchangeable / 357 preparevalid item 1 interchangeable。**  
   官方 Usage 写：CometBFT 不再做额外有效性检查，例如查有没有重复交易。看见回了提案，不是引擎已经验过重复 interchangeable——本页从 357 item 1 侧钉 not already checked 单句。357 prepare-valid vs checked bundled unbundling 在本页 item 1 启动。

2. **看见回了提案 / 看见能提 / no checks is not already 已经有应用级重放保护 interchangeable，也不是已经 Prepare 回包校验 bundled（357） interchangeable / 716 prepvalid-notchecked interchangeable / 357 preparevalid item 3 events interchangeable / 718 prepvalid-notevents interchangeable。**  
   官方把引擎不再查重复和应用级重放保护分开——357 bundled 第一件事常与「看见能提就已经有重放保护 interchangeable」糊成一句，本页钉 not app-level replay 单句。

3. **看见没有再验 / 看见 Usage 这句 / no checks is not already 已经内存池去重就已经保证不重放（313） interchangeable / 313 pooldedup interchangeable / 已经 Prepare Usage no checks / crash / nondet bundled（504） interchangeable / 504 nochecks interchangeable，也不是已经 Prepare 回包校验 bundled（357） interchangeable / 716 prepvalid-notchecked interchangeable / 717 prepvalid-notcrash interchangeable。**  
   官方把 357 回包校验侧不再查重复和 313 池门去重 / 504 Usage 末尾 no checks 单句分开。看见没有再验，不是已经 504 交差 interchangeable。357 prepare-valid vs checked bundled unbundling 在本页 item 1 启动。

怎样再验 Prepare 回包、怎样查重复、怎样攒事件是规范里的做法，本页不抄。

## 官方为什么这样拆

- **no extra checks not already checked ≠ 已经验过重复 interchangeable：** 官方把不再检查和已经验过分开。
- **no extra checks not app-level replay ≠ 已经有应用级重放保护 interchangeable：** 官方把引擎不再查重复和应用级重放保护分开。
- **no extra checks not pool dedup ≠ 313 / 504 interchangeable：** 官方把 357 回包校验侧和池门去重 / Usage 末尾 no checks 分开；357 prepare-valid vs checked bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 引擎没有再验重复交易 | 不是已经验过重复 | 不是回包验不过会崩（717/357 item 2） |
| 看见回了提案 | 不是已经有应用级重放保护 | 不是 Prepare 回包校验 bundled（357） |
| 看见没有再验 | 不是内存池去重（313） / Usage 末尾 no checks（504） | 不是 Prepare 事件已交（718/357 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 回包校验 no extra checks not already checked / not app-level replay / not pool dedup 正式三事（357 余量），必须分开没有再验是不是已经验过重复、是不是已经有应用级重放保护、是不是池门去重 / Usage 末尾 no checks interchangeable / 313 / 504。可以跳过「看见回了提案就已经验过重复」。不要另写怎样再验 Prepare 回包。357 prepare-valid vs checked bundled unbundling 在本页 item 1 启动；续 [`worked-example-prepvalid-notcrash-vs-bundled.md`](worked-example-prepvalid-notcrash-vs-bundled.md)（不变量 717 item 2）。

## 本页不抄

- 怎样再验 Prepare 回包、怎样查重复、怎样攒事件。
- Prepare 回包校验 bundled。那是不变量 357。
- Prepare 回包验不过引擎崩溃。那是不变量 357 item 2 余量 / 717。
- Prepare 里产出了事件。那是不变量 357 item 3 余量 / 718。
- 内存池去重就已经保证不重放。那是不变量 313。
- Prepare Usage no checks / crash / nondet bundled。那是不变量 504。
