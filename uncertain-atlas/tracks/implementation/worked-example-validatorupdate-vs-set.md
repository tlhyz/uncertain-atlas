# 例：看见 InitChain 回了空名单不是已经没有集合；看见一次更新里重复公钥不是已经能恢复；看见 power 写成 0 不是已经删掉一个不在集合里的人

**层次**：实现 / ValidatorUpdate。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating the Validator Set。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)、[L4.5](../../courses/level-04-bft/L04-M05-validator-set.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「InitChain 空名单不是已经没有集合 / 重复公钥不是已经能恢复 / power 0 不是已经删掉不在集合里的人」，不是 H 的更新已经在 H+1 计票，也不是创世 validators 空已经没有集合。不要另写怎样编更新或怎样算总权。

## 官方三件事

规范把更新验证者集合写成三件独立的实现事，不是「看见 InitChain 回了名单就已经定了、已经能重复改、已经能对任何人写 0」一件事：

1. **看见 InitChain 回了空名单 / 看见没回验证者 不是已经没有集合，也不是已经用了应用自己的空集。**  
   官方写：应用可在 `InitChain` 设集合，也可在 `FinalizeBlock` 更新。`InitChain` 回的名单若**空**，CometBFT **用创世文件里的验证者**。若**不空**，CometBFT 用回包这份当集合。看见回了空，不是已经没有集合。看见没回人，不是已经删掉创世名单。看见能设初始集合，不是已经和创世 validators 空同一句。
2. **看见一次更新里同一把公钥出现两次 / 看见重复 不是已经按后一条改权，也不是已经能恢复。**  
   官方写：应用必须保证**同一批**更新里没有重复，一把公钥在这一次更新里只能出现一次。若带了重复，**块执行会不可恢复地失败**。看见重复，不是已经按后一条算。看见失败，不是已经能重放修好。看见同一把钥，不是已经能写两行。
3. **看见 power 写成 0 / 看见名单里没有这个人 不是已经删掉，也不是已经能对不在集合里的人写 0。**  
   官方写：投票权必须非负。写成 0 时，这个人**必须已经在集合里**，才会被删掉。大于 0：不在就加入，在就改成这个权。新集合总投票权不得超过 `MaxTotalVotingPower`。看见写成 0，不是已经能删一个不在名单里的人。看见总权，不是已经没有上限。看见四种钥型，不是已经选型。

怎样编 `ValidatorUpdate`、怎样算总权、公钥类型表是规范里的取值或做法，本页不抄。H 的更新哪一高度生效是不变量 35，本页不抄。

## 官方为什么这样拆

- **InitChain 空名单 ≠ 已经没有集合：** 官方把回空和改用创世名单分开。
- **重复公钥 ≠ 已经能恢复：** 官方把同一批不得重复和不可恢复失败分开。
- **power 0 ≠ 已经删掉不在集合里的人：** 官方把必须已在集合里才删，和总权上限分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| InitChain 回空 | 不是已经没有集合 | 不是创世 validators 空已经没有集合（303） |
| 同一批重复公钥 | 不是已经能恢复 | 不是 H 的更新已经在 H+1 计票（35） |
| power 写成 0 | 不是已经删掉不在集合里的人 | 不是同一高度换轮已经换了集合（302） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「InitChain 已经回了名单」，必须分开回空是不是已经没有集合、重复是不是已经能恢复、power 0 是不是已经删掉不在集合里的人。可以跳过「看见回了就已经定了」。不要另写怎样编更新或怎样算总权。不要把 `MaxTotalVotingPower` 当不确定默认。318 validatorupdate vs set bundled unbundling 完成（713 + 714 + 715）；精读 [`worked-example-validatorupdate-notempty-vs-bundled.md`](worked-example-validatorupdate-notempty-vs-bundled.md)（不变量 713 item 1）；[`worked-example-validatorupdate-notdup-vs-bundled.md`](worked-example-validatorupdate-notdup-vs-bundled.md)（不变量 714 item 2）；[`worked-example-validatorupdate-notpower0-vs-bundled.md`](worked-example-validatorupdate-notpower0-vs-bundled.md)（不变量 715 item 3）。

## 本页不抄

- 怎样编 `ValidatorUpdate`、怎样算总权、公钥类型表。
- H+1 / H+2 / H+3。那是不变量 35。
- 创世字段表。那是不变量 303。
