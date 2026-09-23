# 例：看见 ValidatorParams.pub_key_types 是接受列表不是已经有这种钥；看见命名按 ABCI 不是 Amino；看见列了类型不是已经接受每一种

**层次**：实现 / 公钥类型命名。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) ValidatorParams。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「ValidatorParams.pub_key_types 是接受列表不是已经有这种钥 / 命名按 ABCI 不是 Amino / 列了类型不是已经接受每一种」，不是 Validator 用 address 认人就已经带了公钥，也不是 H 的更新已经在 H+1 计票。不要另写怎样配公钥类型。

## 官方三件事

规范把 `ValidatorParams.pub_key_types` 是**接受的**公钥类型列表、它的命名按 **ABCI** 公钥命名、以及它只是一份列表，写成三件独立的实现事，不是「看见表里有这种钥就已经在用、已经命名一致、已经接受每一种」一件事：

1. **看见 `pub_key_types` 是列表 / 看见有列表 不是已经有这种钥，也不是已经在用。**  
   官方写：`pub_key_types` 是**接受的**公钥类型列表。看见列表里有某一项，不是已经有这种钥在投票。看见字段在，不是已经验过。看见能填，不是已经交差。
2. **看见命名按 ABCI / 看见名字像旧的 不是已经是 Amino 名，也不是两个名字能互换。**  
   官方另起一句写明：`pub_key_types` 用的是 **ABCI 公钥命名，不是 Amino 名**。看见名字长得像 Amino 那一套，不是已经是同一个标识。看见两处都写了类型，不是已经同一套命名。看见对得上，不是已经能互换。
3. **看见列了类型 / 看见一项在里面 不是已经接受每一种，也不是已经不需要点名是哪一种。**  
   官方把它写成列表，本身不保证链会接受其中每一项。看见列了，不是已经在收。看见勾了，不是已经能验。看见表在，不是已经选型。

怎样配公钥类型、怎样命名、怎样加一种算法是规范里的做法，本页不抄。`Validator` 用 address 认人不是不变量 364，本页不抄。H 的更新不是已经在 H+1 计票是不变量 35，本页不抄。

## 官方为什么这样拆

- **`pub_key_types` 是接受列表 ≠ 已经有这种钥：** 官方把「列表」和「实际在用」分开。
- **命名按 ABCI ≠ 是 Amino 名：** 官方专门写了这一句，正因为两套命名曾在同一生态里并存。
- **列了类型 ≠ 已经接受每一种：** 官方没把列表写成承诺。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ValidatorParams.pub_key_types 是接受列表 | 不是已经有这种钥 | 不是 Validator 用 address 认人就已经带了公钥（364） |
| 命名按 ABCI 不是 Amino | 不是两个名字能互换 | 不是 ValidatorUpdate 用 pub_key_type 认人就已经改了集合（35） |
| 列了类型 | 不是已经接受每一种 | 不是 FinalizeBlockResponse.validator_updates 已经在 H+1 换人（428） |
| 本页不涉及 | — | 不是跳过中间高度时重叠旧集合（20） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见类型表里有这种钥就已经在用」，必须分开 ValidatorParams.pub_key_types 是接受列表是不是已经有这种钥、命名按 ABCI 是不是 Amino、列了类型是不是已经接受每一种。可以跳过「看见类型表里有这种钥就已经在用」。不要另写怎样配公钥类型。

## 本页不抄

- 怎样配公钥类型、怎样命名、怎样加一种算法。
- `Validator` 用 address 认人不是已经带了公钥。那是不变量 364。
- H 的更新不是已经在 H+1 计票。那是不变量 35。
- `FinalizeBlockResponse.validator_updates` 不是已经在 H+1 换人。那是不变量 428。
