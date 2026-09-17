# 模式：把 InitChain Usage Response Validators empty → Request Validators not empty list means no set / not not-empty ignores Request / not ValidatorUpdate already changed set 正式三事（495 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**例**：[empty → Request not empty list means no set ≠ bundled（495）](../../tracks/implementation/worked-example-initchainusage-notempty-vs-bundled.md)。

## 三个名字

1. **Response Validators empty → Request Validators 不是空名单就没有集合：** 看见 empty response 规则，不是已经 318 emptyset interchangeable / 696 initchainusage-notempty interchangeable。
2. **看见 will be Request Validators 不是 not empty 就无视 Request：** 看见 empty 路径，不是已经第三件事 interchangeable。
3. **看见 initial validator set 不是 ValidatorUpdate 已经改了集合：** 看见 empty → Request，不是已经 364 interchangeable。

官方把 InitChain Usage empty 规则、空名单语义、not empty 规则、ValidatorUpdate 已经改了集合写成三个名字。把它们叫成一个「看见 InitChain 了就已经没有集合」，会把 not empty list means no set、not not-empty ignores Request、not ValidatorUpdate already changed set 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage empty 正式三事（495 余量），先数清问的是 empty → Request 是不是空名单就没有集合 / 318、是不是 not empty 规则、还是看见 Usage 是不是 ValidatorUpdate 已经改了集合 / 364，再决定要不要同一次发布。495 initchainusage vs bundled unbundling 在本页 item 2 续。
