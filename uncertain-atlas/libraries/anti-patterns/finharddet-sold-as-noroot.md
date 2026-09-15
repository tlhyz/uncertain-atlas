# 反模式：把 FinalizeBlockResponse app_hash empty / hard-coded / MUST be deterministic 正式三事卖成已经没有状态根

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[may be empty ≠ 已经没有状态根](../../tracks/implementation/worked-example-finharddet-vs-empty.md)。

## 卖法

- 「看见 Finalize 回了空 app_hash 就已经没有状态根 / 已经交差。」
- 「看见可以硬编码，就必须真是 Merkle root 才算合法。」
- 「看见 next_block_delay 非确定，Finalize 回包整门都可以非确定。」

## 为什么错

官方把 may be empty、may be hard-coded、MUST be deterministic / only params + previous committed state 写成三件独立的实现事。把它们卖成已经没有状态根、必须真是 Merkle root、next_block_delay 非确定就代表整门非确定，会把可以空、可以硬编码和 app_hash 必须确定三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 回包 app_hash 可以空或硬编码但必须确定，必须分开 may be empty、may be hard-coded、MUST be deterministic 三个名字，不要把它们卖成已经没有状态根。

## 和相邻反模式

- [finapphash-sold-as-header](finapphash-sold-as-header.md) 是 Finalize 回包 app_hash 可以空或硬编码就已经印进本头，不是本页这种 may be empty / hard-coded / MUST be deterministic 三事。
- [findet-sold-as-prepare](findet-sold-as-prepare.md) 是 app_hash MUST be deterministic 已经 next_block_delay 非确定就代表整门非确定，不是本页这种 empty / hard-coded / MUST be deterministic 专用切片。
- [finmerkle-sold-as-header](finmerkle-sold-as-header.md) 是 optional Merkle root 已经印进本头，不是本页这种 may be hard-coded 不是必须真是 Merkle root。
