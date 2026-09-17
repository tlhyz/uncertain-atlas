# 模式：把 FinalizeBlockResponse app_hash empty / hard-coded / MUST be deterministic 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[may be empty ≠ 已经没有状态根](../../tracks/implementation/worked-example-finharddet-vs-empty.md)。

## 三个名字

1. **may be empty 不是已经没有状态根：** 看见可以空不是已经交差 / 已经印进本头 interchangeable。
2. **may be hard-coded 不是必须真是 Merkle root：** 看见可以硬编码不是已经 optional Merkle root / 必须真是默克尔根 interchangeable。
3. **MUST be deterministic / only params + previous committed state 不是 next_block_delay 非确定就代表整门非确定：** 看见必须确定不是已经印进本头 / 已经 next_block_delay 非确定 interchangeable。

## 为什么要分开叫

官方把 may be empty、may be hard-coded、MUST be deterministic / only params + previous committed state 写成三个名字。把它们叫成一个「看见回了空根或硬编码就已经没有状态、已经 next_block_delay 非确定就代表整门非确定」，会把可以空、可以硬编码和必须确定三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「FinalizeBlockResponse.app_hash may also be empty or hard-coded, but MUST be deterministic」，先数清问的是 may be empty 是不是已经没有状态根、may be hard-coded 是不是必须真是 Merkle root，还是 MUST be deterministic 是不是已经 next_block_delay 非确定就代表整门非确定，再决定要不要同一次发布。
