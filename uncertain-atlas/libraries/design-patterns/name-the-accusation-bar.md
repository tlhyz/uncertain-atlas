# 模式：把证据指控栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方现状）+ 建议（产品）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) LightClientAttackEvidence 与 [Light Client Accountability](https://github.com/cometbft/cometbft/blob/main/spec/light-client/accountability/README.md)。  
**例**：[Byzantine Validators 是过错名单 ≠ 已经成立](../../tracks/implementation/worked-example-byzantine-vs-accusation.md)。

## 三个名字

1. **Byzantine Validators 是过错名单不是已经成立：** 官方写「acted maliciously」，那是主张，判定在别处。
2. **`Read Below` 不是已经给出了定义：** 同一张表里三个字段的说明或校验写成这四个字，它是「详情在别处」的指针。
3. **摘要说三种穷尽不是已经验完：** 问责文里还有 **phantom validators**，并对是否单列留了一个 **Q** 开放问题。

**先分清一个无关的同名：** Kaspa 的 PHANTOM / GHOSTDAG 与 CometBFT 的 phantom validator 无关。

## 为什么要分开叫

官方把「名单是主张」「详情在别处」「摘要有断言」写成三件事，而第三件还牵出一个**摘要与详情不一致**的现状。把它们叫成一个「看见名单就已经坐实」，会把指控与判定、指针与内容、摘要与详情一起吞掉。

## 产品

**建议（产品，不是事实）**：实现证据校验时**不要只按 `data_structures.md` 的摘要写**，必须去问责文逐条读，并把 phantom validator 那一类当作**待决问题**处理。产品文案若说「轻客户端攻击已覆盖」，先数清问的是 Byzantine Validators 是过错名单不是已经成立、Read Below 不是已经给出了定义，还是摘要说三种穷尽不是已经验完。
