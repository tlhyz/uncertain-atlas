# 例：看见 Prepare 里有这份 / 看见有 ExtendedVoteInfo.validator / 看见能抽 is not already already from-block interchangeable / already pubkey interchangeable / already settled interchangeable

**层次**：实现 / ExtendedVoteInfo 从本进程抽出不是已经从块里抽出 not already from-block / not already pubkey / not already settled 正式三事（369 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendedVoteInfo 从本进程抽出不是已经从块里抽出 not already from-block / not already pubkey / not already settled 正式三事（369 余量）/ not 854 extvoteinfo-notfromblock interchangeable / not 369 extvoteinfo bundled interchangeable」，不是 extvoteinfo bundled（369），也不是把验过的签交给应用不是已经按原样签（855 item 2 余量）或扩展关掉则字段全空不是已经到了启用高度（856 item 3 余量）。不要另写怎样写 ExtendedVoteInfo。

## 官方三件事

规范把 Methods 里这份信息从本进程里 CometBFT 的数据结构抽出 和「已经是 Prepare 里有这份就已经从块里抽出 interchangeable / 已经是有 ExtendedVoteInfo.validator 就已经带了公钥 interchangeable / 已经是能抽就已经交差 interchangeable / 已经是 extvoteinfo bundled interchangeable」分开写成三件独立的实现事，不是「看见 Prepare 里有这份就已经从块里抽出 interchangeable / 就已经带了公钥 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见 Prepare 里有这份 / 看见 ExtendedVoteInfo 从本进程的 CometBFT 数据结构抽出 / 看见 Prepare 里有 `ExtendedCommitInfo` is not already 已经从拟议块或已决块抽出 interchangeable / 已经 from-block interchangeable / 已经从块里抽出交差 interchangeable / 369 extvoteinfo bundled interchangeable / 365 voteinfo interchangeable / extvoteinfo-sold-as-local interchangeable，也不是已经 extvoteinfo bundled（369） interchangeable / 854 extvoteinfo-notfromblock interchangeable / 369 extvoteinfo item 1 interchangeable，也不是已经 ExtendedVoteInfo 从本进程抽出不是已经从块里抽出 not already from-block / not already pubkey / not already settled 正式三事 bundled（369 item 1 余量） interchangeable / 369 extvoteinfo item 1 interchangeable，也不是已经把验过的签交给应用就已经按原样签（855） interchangeable / 856 extvoteinfo-notveheight interchangeable / 843 voteinfo-notpubkey interchangeable，也不是已经从拟议块或已决块抽出就已经带了公钥（365） interchangeable。**  
   官方写：这份信息从本进程里 CometBFT 的数据结构抽出。看见 Prepare 里有这份，不是已经从块里抽出。看见 Prepare 里有这份，不是已经 from-block interchangeable——369 钉 bundled 三事，本页从 item 1 侧钉 not already from-block 单句。看见 ExtendedVoteInfo 从本进程的 CometBFT 数据结构抽出，不是已经 extvoteinfo bundled（369） interchangeable——369 钉 bundled，本页钉 item 1 第一件事。看见 Prepare 里有这份，不是已经把验过的签交给应用就已经按原样签（855） interchangeable——855 另钉 item 2。看见 Prepare 里有这份，不是已经扩展关掉字段全空就已经到了启用高度（856） interchangeable——856 另钉 item 3。369 extvoteinfo-vs-local bundled unbundling 在本页 item 1 启动。

2. **看见有 `ExtendedVoteInfo.validator` / 看见有 validator 字段 / 看见票里有 Validator is not already 已经带了公钥 interchangeable / 已经 pubkey interchangeable / 已经带了公钥交差 interchangeable / 369 extvoteinfo bundled interchangeable / 364 validator interchangeable，也不是已经 extvoteinfo bundled（369） interchangeable / 854 extvoteinfo-notfromblock interchangeable / 369 extvoteinfo item 2 交给应用 interchangeable / 369 extvoteinfo item 3 关掉全空 interchangeable，也不是已经 ExtendedVoteInfo 从本进程抽出不是已经从块里抽出 not already from-block / not already pubkey / not already settled 正式三事 bundled（369 item 1 余量） interchangeable / 369 extvoteinfo item 1 interchangeable，也不是已经从块里抽出（本页第一件事） interchangeable。**  
   官方写：看见有 `ExtendedVoteInfo.validator`，不是已经带了公钥。看见有 validator 字段，不是已经 pubkey interchangeable——本页钉 not already pubkey 单句。看见票里有 Validator，不是已经从块里抽出（本页第一件事） interchangeable——三件事分开钉。369 extvoteinfo-vs-local bundled unbundling 在本页 item 1 启动。

3. **看见能抽 / 看见能从本进程抽出 / 看见抽得出来 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 369 extvoteinfo bundled interchangeable / 33 fourgates interchangeable，也不是已经 extvoteinfo bundled（369） interchangeable / 854 extvoteinfo-notfromblock interchangeable / 369 extvoteinfo item 2 / 369 extvoteinfo item 3，也不是已经 ExtendedVoteInfo 从本进程抽出不是已经从块里抽出 not already from-block / not already pubkey / not already settled 正式三事 bundled（369 item 1 余量） interchangeable / 369 extvoteinfo item 1 interchangeable，也不是已经从块里抽出（本页第一件事） interchangeable / 已经带了公钥（本页第二件事） interchangeable。**  
   官方写：看见能抽，不是已经交差。看见能从本进程抽出，不是已经 settled interchangeable——本页钉 not already settled 单句。看见抽得出来，不是已经带了公钥（本页第二件事） interchangeable——三件事分开钉。369 extvoteinfo-vs-local bundled unbundling 在本页 item 1 启动。

怎样编 `ExtendedVoteInfo`、怎样验签、怎样开关扩展是规范里的做法，本页不抄。extvoteinfo bundled（369）、把验过的签交给应用不是已经按原样签（369 item 2 余量 / 855）、扩展关掉则字段全空不是已经到了启用高度（369 item 3 余量 / 856）、从拟议块或已决块抽出就已经带了公钥（365）、Validator 用 address 认人就已经带了公钥（364）、vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358）是另外那套，本页不抄。

## 官方为什么这样拆

- **Prepare 里有这份 not already from-block ≠ 369 / 365 interchangeable：** 官方把本进程抽出和从块里抽出分开。
- **有 ExtendedVoteInfo.validator not already pubkey ≠ 已经带了公钥 interchangeable：** 官方把有 validator 字段和已经带了公钥分开。
- **能抽 not already settled ≠ 已经交差 interchangeable：** 官方把能抽和已经交差分开；369 extvoteinfo-vs-local bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Prepare 里有这份 | 不是 already from-block | 不是从拟议块或已决块抽出就已经带了公钥 alone（365） |
| 有 ExtendedVoteInfo.validator | 不是 already pubkey | 不是把验过的签交给应用 already raw alone（855） |
| 能抽 | 不是 already settled | 不是扩展关掉字段全空 already ve-height alone（856） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendedVoteInfo 从本进程抽出不是已经从块里抽出 not already from-block / not already pubkey / not already settled 正式三事（369 余量），必须分开 Prepare 里有这份 是不是 already from-block interchangeable / 369 extvoteinfo bundled interchangeable / extvoteinfo-sold-as-local interchangeable、有 ExtendedVoteInfo.validator 是不是 already pubkey interchangeable、能抽 是不是 already settled interchangeable。可以跳过「看见 Prepare 里有这份就已经从块里抽出 interchangeable / 就已经带了公钥 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 ExtendedVoteInfo。369 extvoteinfo-vs-local bundled unbundling 在本页 item 1 启动；完成 [`worked-example-extvoteinfo-notraw-vs-bundled.md`](worked-example-extvoteinfo-notraw-vs-bundled.md)（不变量 855 item 2）；完成 [`worked-example-extvoteinfo-notveheight-vs-bundled.md`](worked-example-extvoteinfo-notveheight-vs-bundled.md)（不变量 856 item 3）。

## 本页不抄

- 怎样编 `ExtendedVoteInfo`、怎样验签、怎样开关扩展。
- extvoteinfo bundled。那是不变量 369。
- 把验过的签交给应用不是已经按原样签。那是不变量 369 item 2 余量 / 855。
- 扩展关掉则字段全空不是已经到了启用高度。那是不变量 369 item 3 余量 / 856。
- 从拟议块或已决块抽出就已经带了公钥。那是不变量 365。
- Validator 用 address 认人就已经带了公钥。那是不变量 364。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。那是不变量 358。
