# 例：看见 ExtendVoteResponse.non_rp_extension is not already signed-as-is interchangeable / not already replay-protected interchangeable / not already must-fill interchangeable

**层次**：实现 / ExtendVoteResponse.non_rp_extension not already signed-as-is / not already replay-protected / not already must-fill 正式三事（418 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Response / VerifyVoteExtension Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVoteResponse.non_rp_extension not already signed-as-is / not already replay-protected / not already must-fill 正式三事（418 余量）/ not 1083 eresp-notraw interchangeable / not 418 extresp-vs-wrap bundled interchangeable」，不是扩展回包栏 bundled（418），也不是 non_rp_extension 按应用给的字节原样签就已经有重放保护（358），也不是 Verify 请求栏 non_rp 就已经按原样签（436）。不要另写怎样写扩展回包栏。

## 官方三件事

1. **看见 ExtendVoteResponse.non_rp_extension 是 CometBFT 签的信息、可以 0 长、标成非确定 / 看见回了第二份 这份栏 is not already 已经按原样签 interchangeable，也不是已经扩展回包栏 bundled（418） interchangeable / 1083 eresp-notraw interchangeable / 1082 eresp-notwrap interchangeable / 418 extresp item 1 vote_extension interchangeable，也不是已经 ExtendVoteResponse.non_rp_extension not already signed-as-is / not already replay-protected / not already must-fill 正式三事 bundled（418 item 2 余量） interchangeable / 418 extresp item 2 interchangeable。**  
   官方写：non_rp_extension 是 CometBFT 签的信息，可以 0 长。表上 Deterministic = No。看见回了第二份，不是已经按原样签 interchangeable——本页从 418 item 2 侧钉 not already signed-as-is 单句。418 extresp vs wrap bundled unbundling 在本页 item 2 续。

2. **看见标成非确定 / 看见回了第二份 / 这份栏 is not already 已经有重放保护 interchangeable，也不是已经扩展回包栏 bundled（418） interchangeable / 1083 eresp-notraw interchangeable / 418 extresp item 3 verify-nonrp interchangeable / 1084 eresp-nottable interchangeable，也不是已经 non_rp_extension 按应用给的字节原样签就已经有重放保护 interchangeable / 358 extresp interchangeable。**  
   官方把标成非确定和已经有重放保护分开。看见标成非确定，不是已经有重放保护 interchangeable。本页钉 not already replay-protected 单句。

3. **看见可以 0 长 / 看见回了第二份 / 这份栏 is not already 已经必须填 interchangeable，也不是已经扩展回包栏 bundled（418） interchangeable / 1083 eresp-notraw interchangeable / 1082 eresp-notwrap interchangeable，也不是已经 Verify 请求栏 non_rp 就已经按原样签 interchangeable / 436 verifyreqbar interchangeable。**  
   官方把可以 0 长和已经必须填分开。看见可以 0 长，不是已经必须填 interchangeable。418 extresp vs wrap bundled unbundling 在本页 item 2 续。

怎样写扩展回包栏、怎样填 vote_extension、怎样填 non_rp_extension 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ExtendVoteResponse.non_rp_extension not already signed-as-is ≠ 已经按原样签 interchangeable：** 官方把回包表描述和 Usage 里那份原样签分开。
- **看见标成非确定 not already replay-protected ≠ 已经有重放保护 interchangeable：** 官方把标成非确定和已经有重放保护分开。
- **看见可以 0 长 not already must-fill ≠ 已经必须填 interchangeable：** 官方把可以 0 长和已经必须填分开；418 extresp vs wrap bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendVoteResponse.non_rp_extension 是 CometBFT 签的信息、可以 0 长、标成非确定 | 不是已经按原样签 | 不是 non_rp_extension 按应用给的字节原样签就已经有重放保护（358） |
| 看见标成非确定 | 不是已经有重放保护 | 不是 Verify 请求栏 non_rp 就已经按原样签（436） |
| 看见可以 0 长 | 不是已经必须填 | 不是 Verify non_rp 就已经是 vote_extension 表（1084） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVoteResponse.non_rp_extension not already signed-as-is / not already replay-protected / not already must-fill 正式三事（418 余量），必须分开是不是已经按原样签、是不是已经有重放保护、是不是已经必须填。可以跳过「看见填了扩展回包栏就已经会包进 CanonicalVoteExtension」。不要另写怎样写扩展回包栏。418 extresp vs wrap bundled unbundling 在本页 item 2 续；续 [`worked-example-eresp-nottable-vs-bundled.md`](worked-example-eresp-nottable-vs-bundled.md)（不变量 1084 item 3）。

## 本页不抄

- 怎样写扩展回包栏、怎样填 vote_extension、怎样填 non_rp_extension。
- 扩展回包栏 bundled。那是不变量 418。
- non_rp_extension 按应用给的字节原样签就已经有重放保护。那是不变量 358。
- Verify 请求栏 non_rp 就已经按原样签。那是不变量 436。
