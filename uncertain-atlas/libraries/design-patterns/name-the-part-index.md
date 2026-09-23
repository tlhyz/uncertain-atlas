# 模式：把片下标三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方现状）+ 建议（产品）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) Part。  
**例**：[Part.index 是这片的下标 ≠ 已经有整叠](../../tracks/implementation/worked-example-partindex-vs-whole.md)。

## 三个名字

1. **Part.index 是这片的下标不是已经有整叠：** 一片只是整叠里的一片。
2. **校验写 `Must be >= 0` 不是已经有序：** 是下限，不是范围上界，也不是顺序保证。
3. **Part 表的校验栏不是已经是本对象的校验：** 该表把 `PartSetHeader` 的「32 字节」抄到了 `Part` 的 `bytes` / `proof` 行上，而 `proof` 的类型是 `[Proof]`（结构）。

## 为什么要分开叫

官方把「一片的下标」「一条下限」「一张表的校验栏」写成三件事，而第三件还带出规范自身的**复制粘贴错误**：`index` 的说明写成「Total amount of parts for a block」、`bytes` 与 `proof` 的说明都写成「MerkleRoot of a serialized block」——按下文，这两条语义分别属于 `PartSetHeader.Total` 与 `PartSetHeader.Hash`。把它们叫成一个「看见下标在就已经有整叠」，会把片与整叠、下限与有序、以及本对象与表的错位一起吞掉。

## 产品

**建议（产品，不是事实）**：实现里**不要照抄 `Part` 表的校验栏与说明栏**（那一栏与它自己的类型不符），要以下文 `PartSetHeader` 的定义为准。产品文案若说「分片已齐」，先数清问的是 Part.index 是这片的下标不是已经有整叠、写成 ≥ 0 不是已经有序，还是 Part 表的校验栏不是已经是本对象的校验。
