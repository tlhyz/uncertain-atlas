# 反模式：pubkeytypes-sold-as-in-use

**层次**：实现 / 公钥类型命名。  
**分类**：反模式（会把三件事写成一件）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) ValidatorParams。  
**例**：[ValidatorParams.pub_key_types 是接受列表 ≠ 已经有这种钥](../../tracks/implementation/worked-example-validatorparams-vs-naming.md)。

## 病症

把 `ValidatorParams.pub_key_types` 里列了某种钥写成链已经在用这种钥，或把这一列的命名写成 Amino 名（把 `tendermint/PubKeyEd25519` 那种字样当成本字段的合法取值），或把「列表里有」写成「已经接受、已经能验」。

## 为什么错

规范写的是：`pub_key_types` 是**接受的**公钥类型列表，而且**用的是 ABCI 公钥命名，不是 Amino 名**。列在表里不等于已经在用；命名也不是另一套。把两者混起来，会在跨实现对齐时把「名字对得上」当成「算法对得上」。

## 正确写法

分开三句：ValidatorParams.pub_key_types 是接受列表不是已经有这种钥；命名按 ABCI 不是 Amino；列了类型不是已经接受每一种。

## 边界

不是 [validator-sold-as-update](validator-sold-as-update.md)（那是 `Validator`/`ValidatorUpdate` 用 address 或公钥认人，不变量 364），不是 [validatorupdate-sold-as-set](validatorupdate-sold-as-set.md)（那是 H 的更新不是已经在 H+1 计票，不变量 35），不是 FinalizeBlockResponse 的 `validator_updates`（不变量 428）。

## 本页不抄

- 怎样配公钥类型、怎样命名、怎样加一种算法。
- 怎样写利用步骤。
