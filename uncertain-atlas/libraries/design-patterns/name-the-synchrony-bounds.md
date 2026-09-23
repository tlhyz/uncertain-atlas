# 模式：把同步参数上界三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方标注）+ 建议（产品）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) SynchronyParams。  
**例**：[precision 上界 30s ≠ 已经是协议常数](../../tracks/implementation/worked-example-synchrony-bounds-vs-consensus.md)。

## 三个名字

1. **precision 上界 30s / message_delay 上界 24h 不是已经是协议常数：** 官方写在 `Note:` 里，不是共识参数语义。
2. **写的是「在实现里强制」不是已经进了共识：** 防的是本实现算时间戳时溢出。
3. **目的是防溢出不是已经选型：** 守卫存在不告诉你该填多少。

## 为什么要分开叫

官方把「上界是两个具体数」「由实现强制」「目的是防溢出」写成三件事。把它们叫成一个「看见同步参数有上界就已经是共识规则」，会把实现约束、协议规则和选型建议糊成一层 —— 而 GOAL.md 明令禁止混用「实现保证 / 协议保证」。

## 产品

**建议（产品，不是事实）**：`30s` 与 `24h` **不得抄成「不确定」的共识常数或产品建议值**。若必须引用，写明是 CometBFT 实现的上界，并给出处与版本。产品文案若说「同步参数已定」，先数清问的是 precision 上界 30s 不是已经是协议常数、写的是实现强制不是已经进了共识，还是目的是防溢出不是已经选型。
