# 例：看见 CheckTx Technically optional / Code≠0 rejected is not already four gates settled interchangeable / not already Check passed is in proposal interchangeable / not already forever valid interchangeable

**层次**：实现 / CheckTx Usage Technically optional + Code≠0 rejected not four gates settled / not Check passed is in proposal / not forever valid 正式三事（486 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx Usage Technically optional + Code≠0 rejected not four gates settled / not Check passed is in proposal / not forever valid 正式三事（486 余量）/ not 682 chktxvalidate-notoptional interchangeable / not 486 chktxvalidate-vs-apply bundled interchangeable」，不是 CheckTx Usage validate-no-apply 正式三事 bundled（486），也不是 CheckTx 技术上可选 bundled（373）或 Guardian bundled（490/405）。不要另写怎样实现 CheckTxState、怎样写验签逻辑。

## 官方三件事

规范把 CheckTx Usage 里 Technically optional - not involved in processing blocks / Guardian of the mempool / Code != 0 will be rejected 和「已经可以不跑 CheckTx / 已经四门已经结算（373） interchangeable / 已经 Check 通过就是已进提案（33） interchangeable / 已经 CheckTx 过了就永远有效（301） interchangeable / 已经 CheckTx 是内存池守卫（405） bundled 就代表 Usage 已经验完 interchangeable」分开写成三件独立的实现事，不是「看见 Technically optional / Code≠0 就已经 four gates settled interchangeable / 就已经 Check passed is in proposal interchangeable / 就已经 forever valid interchangeable」一件事：

1. **看见 Technically optional - not involved in processing blocks / Guardian of the mempool: every node runs `CheckTx` before letting a transaction into its local mempool / 看见技术上可选、不参与处理块、内存池守卫 / optional is not already 已经 CheckTx 技术上可选（373） bundled 第二句 interchangeable / 373 checktx-optional interchangeable / 已经可以不跑 CheckTx interchangeable / 已经四门已经结算（33） interchangeable，也不是已经 CheckTx Usage validate-no-apply 正式三事 bundled（486） interchangeable / 682 chktxvalidate-notoptional interchangeable / 680 chktxvalidate-notexecstate interchangeable / 486 chktxvalidate item 1 current state interchangeable，也不是已经 Technically optional + Code≠0 rejected not four gates settled / not Check passed is in proposal / not forever valid 正式三事 bundled（486 item 3 余量） interchangeable / 486 chktxvalidate item 3 interchangeable / 490 chktxguardusage interchangeable。**  
   官方 Usage 写：Technically optional - not involved in processing blocks。看见 optional / not involved in processing blocks，不是已经 CheckTx 技术上可选（373） bundled interchangeable——373 钉 optional vs block processing，本页从 486 item 3 侧钉 not four gates settled 单句。看见 Guardian / every node runs CheckTx，不是已经可以不跑 CheckTx interchangeable。486 chktxvalidate vs apply bundled unbundling 在本页 item 3 完成。

2. **看见 Transactions where `CheckTxResponse.Code != 0` will be rejected - they will not be broadcast to other nodes or included in a proposal block / 看见 Code≠0 会拒、不会广播、不会进提案块 / Code≠0 is not already 已经 Check 通过就是已进提案（33） interchangeable / 33 four gates interchangeable / 已经 CheckTx 过了就进块 interchangeable / 已经 Finalize Code≠0 仍在块里（316） interchangeable，也不是已经 CheckTx Usage validate-no-apply 正式三事 bundled（486） interchangeable / 682 chktxvalidate-notoptional interchangeable / 489 chktxcodereject interchangeable / 486 chktxvalidate item 2 does not apply interchangeable。**  
   官方把 Usage Code≠0 拒路径和「Check 通过就是已进提案」分开——486 bundled 第三件事常与 33/489 混成「看见 Code≠0 就已经 Check 通过就是已进提案 interchangeable」，本页钉 not Check passed is in proposal 单句。看见 will not be included in a proposal block，不是已经 Check 通过就是已进提案 interchangeable——33 钉四门分开，本页钉 Usage Code 拒语义。

3. **看见 CometBFT attributes no other value to the response code / Code≠0 will be rejected / 看见引擎对回包码不再赋予别的含义 is not already 已经 CheckTx 过了就永远有效（301） interchangeable / 301 proposed-vs-removed interchangeable / 已经 CheckTx 是内存池守卫（405） bundled 就代表 optional 已经交差 interchangeable / 已经 CheckTx Usage Guardian（490） bundled interchangeable，也不是已经 CheckTx Usage validate-no-apply 正式三事 bundled（486） interchangeable / 682 chktxvalidate-notoptional interchangeable / 680 chktxvalidate-notexecstate interchangeable / 681 chktxvalidate-notapply interchangeable。**  
   官方把 Usage Code 语义和 forever valid / Guardian bundled 分开——486 bundled 第三件事常与 301/405 混成「看见 Code≠0 就已经 forever valid interchangeable / 就已经 Guardian 交差 interchangeable」，本页钉 not forever valid 单句。看见 no other value to the response code，不是已经 CheckTx 守卫余量 bundled interchangeable——405 钉守卫余量，本页钉 Usage optional+Code 同段。486 chktxvalidate vs apply bundled unbundling 在本页 item 3 完成。

怎样做验签、怎样维护 CheckTxState、怎样区分 current state 是规范里的做法，本页不抄。CheckTx Usage validate-no-apply 正式三事 bundled（486）、validates against current state not ExecuteTxState（486 item 1 余量 / 680）、does not apply state changes（486 item 2 余量 / 681）、CheckTx 技术上可选（373）、Guardian（490/405）、Code≠0 rejected 全段（489）是另外那套，本页不抄。

## 官方为什么这样拆

- **Technically optional not four gates settled ≠ 373 checktx-optional interchangeable：** 官方把 Methods Usage optional / 不参与处理块单句和 optional vs 四门结算路径分开。
- **Code≠0 rejected not Check passed is in proposal ≠ 33 four gates interchangeable：** 官方把 Usage Code 拒路径和 Check 通过就是已进提案分开。
- **Code 语义 not forever valid ≠ 301 proposed-vs-removed interchangeable：** 官方把 Usage Code 语义和 forever valid / Guardian bundled 分开；486 chktxvalidate vs apply bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Technically optional / not involved in processing blocks | 不是四门已经结算（373/33） | 不是 validates against current state（680/486 item 1） |
| Code≠0 rejected / will not be in a proposal | 不是 Check 通过就是已进提案（33） | 不是 CheckTx Usage Code≠0 全段（489） |
| no other value to the response code | 不是 forever valid（301） | 不是 Guardian bundled（490/405） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage Technically optional + Code≠0 rejected not four gates settled / not Check passed is in proposal / not forever valid 正式三事（486 余量），必须分开 Technically optional 是不是四门已经结算 interchangeable / 373 / 33、Code≠0 拒 是不是 Check 通过就是已进提案 interchangeable / 33 / 489、Code 语义 是不是 forever valid interchangeable / 301 / 405。可以跳过「看见跑了 CheckTx 就已经交差」。不要另写怎样实现 CheckTxState。486 chktxvalidate vs apply bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样做验签、怎样维护 CheckTxState、怎样区分 current state。
- CheckTx Usage validate-no-apply 正式三事 bundled。那是不变量 486。
- validates against current state not ExecuteTxState。那是不变量 486 item 1 余量 / 680。
- does not apply state changes。那是不变量 486 item 2 余量 / 681。
- CheckTx 技术上可选、不参与处理块。那是不变量 373。
- CheckTx Usage Code≠0 rejected 全段。那是不变量 489。
- CheckTx Usage Guardian。那是不变量 490。
- 提案收了 / CheckTx 过了就永远有效。那是不变量 301。
