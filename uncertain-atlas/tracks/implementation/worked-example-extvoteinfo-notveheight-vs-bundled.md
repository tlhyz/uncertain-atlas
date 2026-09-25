# 例：看见空着 / 看见关掉了 / 看见字段在 is not already already ve-height interchangeable / already settled interchangeable / already from-block interchangeable

**层次**：实现 / 扩展关掉则字段全空不是已经到了启用高度 not already ve-height / not already settled / not already from-block 正式三事（369 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「扩展关掉则字段全空不是已经到了启用高度 not already ve-height / not already settled / not already from-block 正式三事（369 余量）/ not 856 extvoteinfo-notveheight interchangeable / not 369 extvoteinfo bundled interchangeable」，不是 extvoteinfo bundled（369），也不是 ExtendedVoteInfo 从本进程抽出不是已经从块里抽出（854 item 1 余量）或把验过的签交给应用不是已经按原样签（855 item 2 余量）。不要另写怎样写 ExtendedVoteInfo。

## 官方三件事

规范把 Methods 里若投票扩展关掉，`vote_extension`、`non_rp_vote_extension` 和对应的签都空 和「已经是空着就已经到了启用高度 interchangeable / 已经是关掉了就已经交差 interchangeable / 已经是字段在就已经从块里抽出 interchangeable / 已经是 extvoteinfo bundled interchangeable」分开写成三件独立的实现事，不是「看见空着就已经到了启用高度 interchangeable / 就已经交差 interchangeable / 就已经从块里抽出 interchangeable」一件事：

1. **看见空着 / 看见扩展关掉则 `vote_extension` / `non_rp_vote_extension` 和对应的签都空 / 看见扩展字段空 is not already 已经到了启用高度 interchangeable / 已经 ve-height interchangeable / 已经到了启用高度交差 interchangeable / 369 extvoteinfo bundled interchangeable / 330 veheight interchangeable / extvoteinfo-sold-as-local interchangeable，也不是已经 extvoteinfo bundled（369） interchangeable / 856 extvoteinfo-notveheight interchangeable / 369 extvoteinfo item 3 interchangeable，也不是已经扩展关掉则字段全空不是已经到了启用高度 not already ve-height / not already settled / not already from-block 正式三事 bundled（369 item 3 余量） interchangeable / 369 extvoteinfo item 3 interchangeable，也不是已经从本进程抽出就已经从块里抽出（854） interchangeable / 855 extvoteinfo-notraw interchangeable / 358 nonrp interchangeable，也不是已经到了 H 就已经 Prepare 带了扩展（330） interchangeable。**  
   官方写：若投票扩展关掉，`vote_extension`、`non_rp_vote_extension` 和对应的签都空。看见空着，不是已经到了启用高度。看见空着，不是已经 ve-height interchangeable——369 钉 bundled 三事，本页从 item 3 侧钉 not already ve-height 单句。看见扩展关掉则扩展字段和对应的签都空，不是已经 extvoteinfo bundled（369） interchangeable——369 钉 bundled，本页钉 item 3 第一件事。看见空着，不是已经从本进程抽出就已经从块里抽出（854） interchangeable——854 另钉 item 1。看见空着，不是已经把验过的签交给应用就已经按原样签（855） interchangeable——855 另钉 item 2。369 extvoteinfo-vs-local bundled unbundling 在本页 item 3 完成。

2. **看见关掉了 / 看见投票扩展关掉 / 看见扩展关 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 369 extvoteinfo bundled interchangeable / 33 fourgates interchangeable，也不是已经 extvoteinfo bundled（369） interchangeable / 856 extvoteinfo-notveheight interchangeable / 369 extvoteinfo item 1 抽出 interchangeable / 369 extvoteinfo item 2 交给应用 interchangeable，也不是已经扩展关掉则字段全空不是已经到了启用高度 not already ve-height / not already settled / not already from-block 正式三事 bundled（369 item 3 余量） interchangeable / 369 extvoteinfo item 3 interchangeable，也不是已经到了启用高度（本页第一件事） interchangeable。**  
   官方写：看见关掉了，不是已经交差。看见投票扩展关掉，不是已经 settled interchangeable——本页钉 not already settled 单句。看见扩展关，不是已经到了启用高度（本页第一件事） interchangeable——三件事分开钉。369 extvoteinfo-vs-local bundled unbundling 在本页 item 3 完成。

3. **看见字段在 / 看见扩展字段仍在报文里 / 看见字段还在 is not already 已经从块里抽出 interchangeable / 已经 from-block interchangeable / 已经从块里抽出交差 interchangeable / 369 extvoteinfo bundled interchangeable / 365 voteinfo interchangeable，也不是已经 extvoteinfo bundled（369） interchangeable / 856 extvoteinfo-notveheight interchangeable / 369 extvoteinfo item 1 / 369 extvoteinfo item 2，也不是已经扩展关掉则字段全空不是已经到了启用高度 not already ve-height / not already settled / not already from-block 正式三事 bundled（369 item 3 余量） interchangeable / 369 extvoteinfo item 3 interchangeable，也不是已经到了启用高度（本页第一件事） interchangeable / 已经交差（本页第二件事） interchangeable。**  
   官方写：看见字段在，不是已经从块里抽出。看见扩展字段仍在报文里，不是已经 from-block interchangeable——本页钉 not already from-block 单句。看见字段还在，不是已经交差（本页第二件事） interchangeable——三件事分开钉。369 extvoteinfo-vs-local bundled unbundling 在本页 item 3 完成。

怎样编 `ExtendedVoteInfo`、怎样验签、怎样开关扩展是规范里的做法，本页不抄。extvoteinfo bundled（369）、ExtendedVoteInfo 从本进程抽出不是已经从块里抽出（369 item 1 余量 / 854）、把验过的签交给应用不是已经按原样签（369 item 2 余量 / 855）、到了 H 就已经 Prepare 带了扩展（330）、vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358）、从拟议块或已决块抽出就已经带了公钥（365）是另外那套，本页不抄。

## 官方为什么这样拆

- **空着 not already ve-height ≠ 369 / 330 interchangeable：** 官方把关掉全空和已经到了启用高度分开。
- **关掉了 not already settled ≠ 已经交差 interchangeable：** 官方把关掉了和已经交差分开。
- **字段在 not already from-block ≠ 已经从块里抽出 interchangeable：** 官方把字段在和已经从块里抽出分开；369 extvoteinfo-vs-local bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 空着 | 不是 already ve-height | 不是到了 H 就已经 Prepare 带了扩展 alone（330） |
| 关掉了 | 不是 already settled | 不是从本进程抽出 already from-block alone（854） |
| 字段在 | 不是 already from-block | 不是把验过的签交给应用 already raw alone（855） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看扩展关掉则字段全空不是已经到了启用高度 not already ve-height / not already settled / not already from-block 正式三事（369 余量），必须分开空着 是不是 already ve-height interchangeable / 369 extvoteinfo bundled interchangeable / extvoteinfo-sold-as-local interchangeable、关掉了 是不是 already settled interchangeable、字段在 是不是 already from-block interchangeable。可以跳过「看见空着就已经到了启用高度 interchangeable / 就已经交差 interchangeable / 就已经从块里抽出 interchangeable」。不要另写怎样写 ExtendedVoteInfo。369 extvoteinfo-vs-local bundled unbundling 在本页 item 3 完成（854 + 855 + 856）。

## 本页不抄

- 怎样编 `ExtendedVoteInfo`、怎样验签、怎样开关扩展。
- extvoteinfo bundled。那是不变量 369。
- ExtendedVoteInfo 从本进程抽出不是已经从块里抽出。那是不变量 369 item 1 余量 / 854。
- 把验过的签交给应用不是已经按原样签。那是不变量 369 item 2 余量 / 855。
- 到了 H 就已经 Prepare 带了扩展。那是不变量 330。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。那是不变量 358。
- 从拟议块或已决块抽出就已经带了公钥。那是不变量 365。
