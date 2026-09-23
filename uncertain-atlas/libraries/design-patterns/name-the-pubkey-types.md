# 模式：把公钥类型表三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) ValidatorParams。  
**例**：[ValidatorParams.pub_key_types 是接受列表 ≠ 已经有这种钥](../../tracks/implementation/worked-example-validatorparams-vs-naming.md)。

## 三个名字

1. **ValidatorParams.pub_key_types 是接受的公钥类型列表不是已经有这种钥：** 看见一项在里面不是已经在用。
2. **命名按 ABCI 公钥命名不是 Amino 名：** 官方专门写了这一句。
3. **列了类型不是已经接受每一种：** 列表不是承诺。

## 为什么要分开叫

官方把「接受的列表」「命名按 ABCI 而非 Amino」「列表本身不是承诺」写成三件事。把它们叫成一个「看见类型表里有这种钥就已经在用」，会把列表与实态、两套命名、以及承诺强度一起吞掉。第二件事尤其值钱：同一个生态里 Amino 名还在别处出现（例如 `tendermint/PubKeyEd25519` 那种字样），两套名字看起来一样能指同一把钥，但规范只认 ABCI 那一套。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见类型表里有这种钥就已经在用」，先数清问的是 ValidatorParams.pub_key_types 是接受列表不是已经有这种钥、命名按 ABCI 不是 Amino，还是列了类型不是已经接受每一种，再决定要不要同一次发布。
