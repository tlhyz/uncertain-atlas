# 例：看见 Changes to gas size Deterministic Yes is not already only one field changed interchangeable / not already finrespend bundled interchangeable / not already next_block_delay nondet means whole gate interchangeable

**层次**：实现 / FinalizeBlockResponse consensus_param_updates gas/size/Deterministic Yes not only one field / not finrespend bundled / not next_block_delay nondet means whole gate 正式三事（471 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockResponse consensus_param_updates gas/size/Deterministic Yes not only one field / not finrespend bundled / not next_block_delay nondet means whole gate 正式三事（471 余量）/ not 711 fincparam-notpartial interchangeable / not 471 fincparam-vs-heffective bundled interchangeable」，不是 FinalizeBlockResponse consensus_param_updates H→H+1 正式三事 bundled（471），也不是 Finalize 回包末栏（432）或只填一项（319）。不要另写怎样编 ConsensusParams。

## 官方三件事

1. **看见 Changes to gas, size, and other consensus-related parameters / Deterministic = Yes / 看见改了 gas、大小和其它共识相关参数 / gas/size is not already 已经只填一个字段就只改这一项（319） interchangeable / 319 finpartial interchangeable，也不是已经 FinalizeBlockResponse consensus_param_updates H→H+1 正式三事 bundled（471） interchangeable / 711 fincparam-notpartial interchangeable / 710 fincparam-nothatH interchangeable / 471 fincparam item 1 H→H+1 interchangeable，也不是已经 gas/size/Deterministic Yes not only one field / not finrespend bundled / not next_block_delay nondet means whole gate 正式三事 bundled（471 item 2 余量） interchangeable / 471 fincparam item 2 interchangeable。**  
   官方 Response 表写：consensus_param_updates is Changes to gas, size, and other consensus-related parameters。Deterministic = Yes。看见能改 gas / size / 其它共识相关参数，不是已经只填 Block.MaxBytes 其它字段就保持原值 interchangeable——本页从 471 item 2 侧钉 not only one field 单句。471 fincparam vs heffective bundled unbundling 在本页 item 2 续。

2. **看见 Deterministic = Yes / 看见 Usage 这句 / gas/size is not already 已经 Finalize 回包末栏 bundled（432） interchangeable / 432 finrespend interchangeable，也不是已经 FinalizeBlockResponse consensus_param_updates H→H+1 正式三事 bundled（471） interchangeable / 711 fincparam-notpartial interchangeable / 471 fincparam item 3 empty interchangeable / 712 fincparam-notcleared interchangeable。**  
   官方把 consensus_param_updates 栏和回包末栏 bundled 三栏分开——432 钉 bundled 三栏，本页钉 not finrespend bundled 单句。

3. **看见 Deterministic = Yes / 看见 Usage 这句 / gas/size is not already 已经 next_block_delay Deterministic = No（469）就代表 Finalize 回包整门都可以非确定 interchangeable / 469 fndelay interchangeable，也不是已经 FinalizeBlockResponse consensus_param_updates H→H+1 正式三事 bundled（471） interchangeable / 711 fincparam-notpartial interchangeable / 710 fincparam-nothatH interchangeable。**  
   官方把 consensus_param_updates Deterministic = Yes 和 next_block_delay 非确定分开。看见 Deterministic = Yes，不是已经整门都可以非确定 interchangeable。471 fincparam vs heffective bundled unbundling 在本页 item 2 续。

怎样编 ConsensusParams、默认 MaxBytes / MaxGas、怎样选启用高度是规范里的做法，本页不抄。

## 官方为什么这样拆

- **gas/size/Deterministic Yes not only one field ≠ 319 interchangeable：** 官方把能改 gas/size/其它共识相关参数和只填一项就只改这一项分开。
- **gas/size/Deterministic Yes not finrespend bundled ≠ 432 interchangeable：** 官方把 consensus_param_updates 栏和回包末栏 bundled 分开。
- **gas/size/Deterministic Yes not next_block_delay nondet means whole gate ≠ 469 interchangeable：** 官方把 Deterministic = Yes 和 next_block_delay 非确定代表整门非确定分开；471 fincparam vs heffective bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Changes to gas, size / Deterministic = Yes | 不是只填一个字段就只改这一项（319） | 不是 H apply to H+1（710/471 item 1） |
| 看见 Deterministic = Yes | 不是 Finalize 回包末栏 bundled（432） | 不是 may be empty（712/471 item 3） |
| 看见 Usage 这句 | 不是 next_block_delay 非确定代表整门非确定（469） | 不是 consensus_param_updates bundled（471） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse consensus_param_updates gas/size/Deterministic Yes not only one field / not finrespend bundled / not next_block_delay nondet means whole gate 正式三事（471 余量），必须分开 gas/size 是不是只填一项 interchangeable / 319、是不是回包末栏 bundled interchangeable / 432、是不是 next_block_delay 非确定代表整门非确定 interchangeable / 469。可以跳过「看见回了 gas/size 就已经只改一项」。不要另写怎样编 ConsensusParams。471 fincparam vs heffective bundled unbundling 在本页 item 2 续；完成 [`worked-example-fincparam-notcleared-vs-bundled.md`](worked-example-fincparam-notcleared-vs-bundled.md)（不变量 712 item 3）。

## 本页不抄

- 怎样编 ConsensusParams、默认 MaxBytes / MaxGas、怎样选启用高度。
- FinalizeBlockResponse consensus_param_updates H→H+1 正式三事 bundled。那是不变量 471。
- H apply to H+1。那是不变量 471 item 1 余量 / 710。
- may be empty / keep current values。那是不变量 471 item 3 余量 / 712。
- Finalize 回包末栏 bundled。那是不变量 432。
- Finalize 没回 / 只填一项。那是不变量 319。
- next_block_delay 非确定。那是不变量 469。
