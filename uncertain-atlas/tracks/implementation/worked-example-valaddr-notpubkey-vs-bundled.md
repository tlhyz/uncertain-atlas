# 例：看见有结构 / 看见有 address / 看见有 power is not already already pubkey interchangeable / already verify interchangeable / already update interchangeable

**层次**：实现 / Validator 用 address 认人不是已经带了公钥 not already pubkey / not already verify / not already update 正式三事（364 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator / ValidatorUpdate。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Validator 用 address 认人不是已经带了公钥 not already pubkey / not already verify / not already update 正式三事（364 余量）/ not 839 valaddr-notpubkey interchangeable / not 364 validator bundled interchangeable」，不是 Validator 类型 bundled（364），也不是不带 PubKey 不是已经选型（840 item 2 余量）或 ValidatorUpdate 用公钥认人不是已经改了集合（841 item 3 余量）。不要另写怎样写 Validator 类型。

## 官方三件事

规范把 Methods 里 `Validator` 用 address 认人、字段只有 `address` 和 `power` 和「已经是有结构就已经带了公钥 interchangeable / 已经是有 address 就能验签 interchangeable / 已经是有 power 就已经是 ValidatorUpdate interchangeable / 已经是 validator bundled interchangeable」分开写成三件独立的实现事，不是「看见有结构就已经带了公钥 interchangeable / 就已经能验签 interchangeable / 就已经是 ValidatorUpdate interchangeable」一件事：

1. **看见有结构 / 看见 VoteInfo / CommitInfo / ExtendedCommitInfo 里有这份 Validator / 看见只有 address 和 power is not already 已经带了公钥 interchangeable / 已经 pubkey interchangeable / 已经带了公钥交差 interchangeable / 364 validator bundled interchangeable / 35 valupdate interchangeable / validator-sold-as-update interchangeable，也不是已经 Validator 类型 bundled（364） interchangeable / 839 valaddr-notpubkey interchangeable / 364 validator item 1 interchangeable，也不是已经 Validator 用 address 认人不是已经带了公钥 not already pubkey / not already verify / not already update 正式三事 bundled（364 item 1 余量） interchangeable / 364 validator item 1 interchangeable，也不是已经不带 PubKey 选型（840） interchangeable / 841 valupdate-notset interchangeable / 363 finresp interchangeable，也不是已经 H 的更新已经在 H+1 计票（35） interchangeable。**  
   官方写：`Validator` 用 address 认人。字段只有 `address` 和 `power`。看见 VoteInfo / CommitInfo / ExtendedCommitInfo 里有这份结构，不是已经带了公钥。看见有结构，不是已经 pubkey interchangeable——364 钉 bundled 三事，本页从 item 1 侧钉 not already pubkey 单句。看见只有 address 和 power，不是已经 Validator 类型 bundled（364） interchangeable——364 钉 bundled，本页钉 item 1 第一件事。看见有结构，不是已经不带 PubKey 选型（840） interchangeable——840 另钉 item 2。看见有结构，不是已经 ValidatorUpdate 改了集合（841） interchangeable——841 另钉 item 3。364 validator-vs-update bundled unbundling 在本页 item 1 启动。

2. **看见有 address / 看见字段有 address / 看见用 address 认人 is not already 已经能验签 interchangeable / 已经 verify interchangeable / 已经能验签交差 interchangeable / 364 validator bundled interchangeable / 35 valupdate interchangeable，也不是已经 Validator 类型 bundled（364） interchangeable / 839 valaddr-notpubkey interchangeable / 364 validator item 2 省字段 interchangeable / 364 validator item 3 更新 interchangeable，也不是已经 Validator 用 address 认人不是已经带了公钥 not already pubkey / not already verify / not already update 正式三事 bundled（364 item 1 余量） interchangeable / 364 validator item 1 interchangeable，也不是已经带了公钥（本页第一件事） interchangeable。**  
   官方写：看见有 address，不是已经能验签。看见字段有 address，不是已经 verify interchangeable——本页钉 not already verify 单句。看见用 address 认人，不是已经带了公钥（本页第一件事） interchangeable——三件事分开钉。364 validator-vs-update bundled unbundling 在本页 item 1 启动。

3. **看见有 power / 看见字段有 power / 看见有投票权 is not already 已经是 ValidatorUpdate interchangeable / 已经 update interchangeable / 已经是 ValidatorUpdate 交差 interchangeable / 364 validator bundled interchangeable / 33 fourgates interchangeable，也不是已经 Validator 类型 bundled（364） interchangeable / 839 valaddr-notpubkey interchangeable / 364 validator item 2 / 364 validator item 3，也不是已经 Validator 用 address 认人不是已经带了公钥 not already pubkey / not already verify / not already update 正式三事 bundled（364 item 1 余量） interchangeable / 364 validator item 1 interchangeable，也不是已经带了公钥（本页第一件事） interchangeable / 已经能验签（本页第二件事） interchangeable。**  
   官方写：看见有 power，不是已经是 `ValidatorUpdate`。看见字段有 power，不是已经 update interchangeable——本页钉 not already update 单句。看见有投票权，不是已经能验签（本页第二件事） interchangeable——三件事分开钉。364 validator-vs-update bundled unbundling 在本页 item 1 启动。

怎样编 `Validator`、怎样编 `ValidatorUpdate`、怎样在 ABCI 上传钥是规范里的做法，本页不抄。Validator 类型 bundled（364）、不带 PubKey 不是已经选型（364 item 2 余量 / 840）、ValidatorUpdate 用公钥认人不是已经改了集合（364 item 3 余量 / 841）、H 的更新已经在 H+1 计票（35）、InitChain 空名单就已经没有集合（318）、必须回四列就已经改了集合（363）是另外那套，本页不抄。

## 官方为什么这样拆

- **有结构 not already pubkey ≠ 364 / 35 interchangeable：** 官方把有结构和已经带了公钥分开。
- **有 address not already verify ≠ 已经能验签 interchangeable：** 官方把有 address 和已经能验签分开。
- **有 power not already update ≠ 已经是 ValidatorUpdate interchangeable：** 官方把有 power 和已经是 ValidatorUpdate 分开；364 validator-vs-update bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 有结构 | 不是 already pubkey | 不是 H 的更新已经在 H+1 计票 alone（35） |
| 有 address | 不是 already verify | 不是不带 PubKey already algo alone（840） |
| 有 power | 不是 already update | 不是 ValidatorUpdate already changed-set alone（841） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Validator 用 address 认人不是已经带了公钥 not already pubkey / not already verify / not already update 正式三事（364 余量），必须分开有结构 是不是 already pubkey interchangeable / 364 validator bundled interchangeable / validator-sold-as-update interchangeable、有 address 是不是 already verify interchangeable、有 power 是不是 already update interchangeable。可以跳过「看见有结构就已经带了公钥 interchangeable / 就已经能验签 interchangeable / 就已经是 ValidatorUpdate interchangeable」。不要另写怎样写 Validator 类型。364 validator-vs-update bundled unbundling 在本页 item 1 启动；完成 [`worked-example-valnopub-notalgo-vs-bundled.md`](worked-example-valnopub-notalgo-vs-bundled.md)（不变量 840 item 2）；完成 [`worked-example-valupdate-notset-vs-bundled.md`](worked-example-valupdate-notset-vs-bundled.md)（不变量 841 item 3）。

## 本页不抄

- 怎样编 `Validator`、怎样编 `ValidatorUpdate`、怎样在 ABCI 上传钥。
- Validator 类型 bundled。那是不变量 364。
- 不带 PubKey 不是已经选型。那是不变量 364 item 2 余量 / 840。
- ValidatorUpdate 用公钥认人不是已经改了集合。那是不变量 364 item 3 余量 / 841。
- H 的更新已经在 H+1 计票。那是不变量 35。
- InitChain 空名单就已经没有集合。那是不变量 318。
- 必须回四列就已经改了集合。那是不变量 363。
