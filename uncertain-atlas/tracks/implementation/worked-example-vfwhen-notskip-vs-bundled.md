# 例：看见 Precommit unsigned discard is not already skip-verify interchangeable / not already verified interchangeable / not already accept interchangeable

**层次**：实现 / Precommit unsigned discard not already skip-verify / not already verified / not already accept 正式三事（435 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Precommit unsigned discard not already skip-verify / not already verified / not already accept 正式三事（435 余量）/ not 1085 vfwhen-notskip interchangeable / not 435 verify-formal-when-vs-flow bundled interchangeable」，不是 Verify When 正式流程 bundled（435），也不是空扩展仍会调 Verify 就已经跳过 Verify（353），也不是 ExtendVote 请求对应即将发 Precommit 就已经跳过 Verify（409）。不要另写怎样写 Verify When 正式流程。

## 官方三件事

1. **看见 Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify / 看见丢掉了 这份栏 is not already 已经跳过 Verify interchangeable，也不是已经 Verify When 正式流程 bundled（435） interchangeable / 1085 vfwhen-notskip interchangeable / 1086 vfwhen-notverif interchangeable / 435 verify-formal-when item 2 call interchangeable，也不是已经 Precommit unsigned discard not already skip-verify / not already verified / not already accept 正式三事 bundled（435 item 1 余量） interchangeable / 435 verify-formal-when item 1 interchangeable。**  
   官方写：若 Precommit 没有带有效签的扩展，p 把这张 Precommit 当非法丢掉。0 长度扩展只要伴随签名也合法，就算有效。看见丢掉了，不是已经跳过 Verify interchangeable——本页从 435 item 1 侧钉 not already skip-verify 单句。435 verify-formal-when vs flow bundled unbundling 在本页 item 1 启动。

2. **看见没调 Verify / 看见丢掉了 / 这份栏 is not already 已经验过扩展 interchangeable，也不是已经 Verify When 正式流程 bundled（435） interchangeable / 1085 vfwhen-notskip interchangeable / 435 verify-formal-when item 3 accept-reject interchangeable / 1087 vfwhen-notcommit interchangeable，也不是已经空扩展仍会调 Verify 就已经跳过 Verify interchangeable / 353 verifyusage interchangeable。**  
   官方把没调 Verify 和已经验过扩展分开。看见没调 Verify，不是已经验过扩展 interchangeable。本页钉 not already verified 单句。

3. **看见没签 / 看见丢掉了 / 这份栏 is not already 已经 Accept interchangeable，也不是已经 Verify When 正式流程 bundled（435） interchangeable / 1085 vfwhen-notskip interchangeable / 1086 vfwhen-notverif interchangeable，也不是已经 ExtendVote 请求对应即将发 Precommit 就已经跳过 Verify interchangeable / 409 extpre interchangeable。**  
   官方把没签和已经 Accept 分开。看见没签，不是已经 Accept interchangeable。435 verify-formal-when vs flow bundled unbundling 在本页 item 1 启动。

怎样写 Verify When 正式流程、怎样验伴随签名、怎样攒下一高 Prepare 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Precommit unsigned discard not already skip-verify ≠ 已经跳过 Verify interchangeable：** 官方把签先丢掉和已经跳过 Verify 分开。
- **看见没调 Verify not already verified ≠ 已经验过扩展 interchangeable：** 官方把没调 Verify 和已经验过扩展分开。
- **看见没签 not already accept ≠ 已经 Accept interchangeable：** 官方把没签和已经 Accept 分开；435 verify-formal-when vs flow bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify | 不是已经跳过 Verify | 不是空扩展仍会调 Verify 就已经跳过 Verify（353） |
| 看见没调 Verify | 不是已经验过扩展 | 不是 ExtendVote 请求对应即将发 Precommit 就已经跳过 Verify（409） |
| 看见没签 | 不是已经 Accept | 不是带有效签就会调 Verify 就已经验过扩展（1086） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Precommit unsigned discard not already skip-verify / not already verified / not already accept 正式三事（435 余量），必须分开是不是已经跳过 Verify、是不是已经验过扩展、是不是已经 Accept。可以跳过「看见收到 Precommit 就已经验过扩展」。不要另写怎样写 Verify When 正式流程。435 verify-formal-when vs flow bundled unbundling 在本页 item 1 启动；续 [`worked-example-vfwhen-notverif-vs-bundled.md`](worked-example-vfwhen-notverif-vs-bundled.md)（不变量 1086 item 2）。

## 本页不抄

- 怎样写 Verify When 正式流程、怎样验伴随签名、怎样攒下一高 Prepare。
- Verify When 正式流程 bundled。那是不变量 435。
- 空扩展仍会调 Verify 就已经跳过 Verify。那是不变量 353。
- ExtendVote 请求对应即将发 Precommit 就已经跳过 Verify。那是不变量 409。
