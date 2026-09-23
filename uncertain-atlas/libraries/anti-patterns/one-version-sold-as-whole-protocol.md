# 反模式：one-version-sold-as-whole-protocol

**层次**：实现 / 头版本栏。  
**分类**：反模式（会把三件事写成一件）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) Header / Version。  
**例**：[Header.Version 是应用与块版本 ≠ 已经知道是哪一版的什么](../../tracks/implementation/worked-example-headerversion-vs-whole.md)。

## 病症

把 `Header.Version` 里的一个数写成「这条链是哪个版本」，或把 `Version.Block` 必须全网一致写成 `Version.App` 也一致（或反过来把应用自定的版本写成协议规定），或把这一节当成完整的版本说明。

## 为什么错

官方在 `Version` 一节顶上写明：这一节**更确切地说是共识版本**，而且**不包含 P2P 版本**这类信息，并留了**两条 TODO**（要写一篇能引用的版本通论）。表里 `Block` 的校验是等于网络在用的块版本、`App` 的校验是与 `state` 比对且描述写「由应用决定」——**两者权威来源不同**。所以一个数既不是完整版本信息，也不能代表整条链的「版本」。别处的 `block_version` / `p2p_version` / `abci_version` 是另一批列。

## 正确写法

分开三句：Header.Version 是应用与块版本不是已经知道是哪一版的什么；`Block` 必须全网一致不是 `App` 也走同一条；一个版本号不是已经点名了整个协议。产品句必须点名是哪一种版本并写出处。

## 边界

不是 [info-sold-as-handshake](info-sold-as-handshake.md)（那是 Info 握手，不变量 370 一族），不是 [infover-sold-as-appversion](infover-sold-as-appversion.md)（那是 Info 请求的 version 不是 app_version，不变量 379），不是 [paramsdocs-sold-as-one-table](paramsdocs-sold-as-one-table.md)（那是 ConsensusParams 跨文档不齐，不变量 447）。

## 本页不抄

- 怎样填版本、怎样做版本升级。
- 怎样写利用步骤。
