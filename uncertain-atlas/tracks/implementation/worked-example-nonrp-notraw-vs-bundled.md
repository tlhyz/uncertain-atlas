# 例：看见绑了这些字段 / 看见有包装 / 看见签了 is not already already raw-signed interchangeable / already canon-vote interchangeable / already settled interchangeable

**层次**：实现 / vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签 not already raw-signed / not already canon-vote / not already settled 正式三事（358 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签 not already raw-signed / not already canon-vote / not already settled 正式三事（358 余量）/ not 827 nonrp-notraw interchangeable / not 358 nonrp bundled interchangeable」，不是两份扩展两份签 bundled（358），也不是 non_rp_extension 按原样签不是已经有重放保护（828 item 2 余量）或要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份（829 item 3 余量）。不要另写怎样编两份扩展。

## 官方三件事

规范把 Methods 里 `ExtendVoteResponse.vote_extension` 会进 `CanonicalVoteExtension`、再填 Height、Round、ChainID 后签名 和「已经是绑了这些字段就已经按原样签 interchangeable / 已经是有包装就已经是 CanonicalVote interchangeable / 已经是签了就已经交差 interchangeable / 已经是 nonrp bundled interchangeable」分开写成三件独立的实现事，不是「看见绑了这些字段就已经按原样签 interchangeable / 就已经是 CanonicalVote interchangeable / 就已经交差 interchangeable」一件事：

1. **看见绑了 Height Round ChainID / 看见 `vote_extension` 会包进 `CanonicalVoteExtension` / 看见绑了这些字段 is not already 已经按原样签 interchangeable / 已经 raw-signed interchangeable / 已经按原样签交差 interchangeable / 358 nonrp bundled interchangeable / 34 canonvote interchangeable / nonrp-sold-as-protected interchangeable，也不是已经两份扩展两份签 bundled（358） interchangeable / 827 nonrp-notraw interchangeable / 358 nonrp item 1 interchangeable，也不是已经 vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签 not already raw-signed / not already canon-vote / not already settled 正式三事 bundled（358 item 1 余量） interchangeable / 358 nonrp item 1 interchangeable，也不是已经有重放保护（828） interchangeable / 829 nonrp-notsame interchangeable / 34 CanonicalVote interchangeable，也不是已经 CanonicalVoteExtension 就已经是 CanonicalVote（34） interchangeable。**  
   官方写：`ExtendVoteResponse.vote_extension` 会进 `CanonicalVoteExtension`，再填 Height、Round、ChainID 后签名。看见绑了这些字段，不是已经按应用给的字节原样签。看见绑了这些字段，不是已经 raw-signed interchangeable——358 钉 bundled 三事，本页从 item 1 侧钉 not already raw-signed 单句。看见 `vote_extension` 会包进 `CanonicalVoteExtension`，不是已经两份扩展两份签 bundled（358） interchangeable——358 钉 bundled，本页钉 item 1 第一件事。看见绑了这些字段，不是已经有重放保护（828） interchangeable——828 另钉 item 2。看见绑了这些字段，不是已经 CanonicalVoteExtension 就已经是 CanonicalVote（34） interchangeable——34 另钉。358 nonrp vs wrapped bundled unbundling 在本页 item 1 启动。

2. **看见有包装 / 看见进了 CanonicalVoteExtension / 看见绑了包装字段 is not already 已经是票上那份 CanonicalVote interchangeable / 已经 canon-vote interchangeable / 已经是 CanonicalVote 交差 interchangeable / 358 nonrp bundled interchangeable / 34 canonvote interchangeable，也不是已经两份扩展两份签 bundled（358） interchangeable / 827 nonrp-notraw interchangeable / 358 nonrp item 2 原样签 interchangeable / 358 nonrp item 3 第二份 interchangeable，也不是已经 vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签 not already raw-signed / not already canon-vote / not already settled 正式三事 bundled（358 item 1 余量） interchangeable / 358 nonrp item 1 interchangeable，也不是已经按原样签（本页第一件事） interchangeable。**  
   官方写：看见有包装，不是已经是票上那份 `CanonicalVote`。看见进了 CanonicalVoteExtension，不是已经 canon-vote interchangeable——本页钉 not already canon-vote 单句。看见绑了包装字段，不是已经按原样签（本页第一件事） interchangeable——三件事分开钉。358 nonrp vs wrapped bundled unbundling 在本页 item 1 启动。

3. **看见签了 / 看见填完字段后签名 / 看见签名挂上 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 358 nonrp bundled interchangeable / 33 fourgates interchangeable，也不是已经两份扩展两份签 bundled（358） interchangeable / 827 nonrp-notraw interchangeable / 358 nonrp item 2 / 358 nonrp item 3，也不是已经 vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签 not already raw-signed / not already canon-vote / not already settled 正式三事 bundled（358 item 1 余量） interchangeable / 358 nonrp item 1 interchangeable，也不是已经按原样签（本页第一件事） interchangeable / 已经是 CanonicalVote（本页第二件事） interchangeable。**  
   官方写：看见签了，不是已经交差。看见填完字段后签名，不是已经 settled interchangeable——本页钉 not already settled 单句。看见签名挂上，不是已经是 CanonicalVote（本页第二件事） interchangeable——三件事分开钉。358 nonrp vs wrapped bundled unbundling 在本页 item 1 启动。

怎样编两份扩展、怎样自防重放、怎样选空是规范里的做法，本页不抄。两份扩展两份签 bundled（358）、non_rp_extension 按原样签不是已经有重放保护（358 item 2 余量 / 828）、要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份（358 item 3 余量 / 829）、CanonicalVoteExtension 就已经是 CanonicalVote（34）、一轮只能交出一份扩展就已经是每一高度一份（350）、空扩展仍会调 Verify 就已经跳过 Verify（353）是另外那套，本页不抄。

## 官方为什么这样拆

- **绑了这些字段 not already raw-signed ≠ 358 / 34 interchangeable：** 官方把包装签名和按原样签分开。
- **有包装 not already canon-vote ≠ 已经是 CanonicalVote interchangeable：** 官方把有包装和已经是票上那份 CanonicalVote 分开。
- **签了 not already settled ≠ 已经交差 interchangeable：** 官方把签了和已经交差分开；358 nonrp vs wrapped bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 绑了这些字段 | 不是 already raw-signed | 不是 CanonicalVoteExtension 就已经是 CanonicalVote alone（34） |
| 有包装 | 不是 already canon-vote | 不是原样签 already replay-protected alone（828） |
| 签了 | 不是 already settled | 不是第二份字段 already same-as-ve alone（829） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签 not already raw-signed / not already canon-vote / not already settled 正式三事（358 余量），必须分开绑了这些字段 是不是 already raw-signed interchangeable / 358 nonrp bundled interchangeable / nonrp-sold-as-protected interchangeable、有包装 是不是 already canon-vote interchangeable、签了 是不是 already settled interchangeable。可以跳过「看见绑了这些字段就已经按原样签 interchangeable / 就已经是 CanonicalVote interchangeable / 就已经交差 interchangeable」。不要另写怎样编两份扩展。358 nonrp vs wrapped bundled unbundling 在本页 item 1 启动；完成 [`worked-example-nonrp-notprotected-vs-bundled.md`](worked-example-nonrp-notprotected-vs-bundled.md)（不变量 828 item 2）；完成 [`worked-example-nonrp-notsame-vs-bundled.md`](worked-example-nonrp-notsame-vs-bundled.md)（不变量 829 item 3）。

## 本页不抄

- 怎样编两份扩展、怎样自防重放、怎样选空。
- 两份扩展两份签 bundled。那是不变量 358。
- non_rp_extension 按原样签不是已经有重放保护。那是不变量 358 item 2 余量 / 828。
- 要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份。那是不变量 358 item 3 余量 / 829。
- CanonicalVoteExtension 就已经是 CanonicalVote。那是不变量 34。
- 一轮只能交出一份扩展就已经是每一高度一份。那是不变量 350。
- 空扩展仍会调 Verify 就已经跳过 Verify。那是不变量 353。
