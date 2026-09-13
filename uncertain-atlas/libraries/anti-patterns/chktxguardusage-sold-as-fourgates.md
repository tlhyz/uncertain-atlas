# 反模式：把 CheckTx Usage Guardian 正式三事卖成 optional / 四门已经结算 / 已经保证不重放

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Guardian of the mempool ≠ Technically optional](../../tracks/implementation/worked-example-chktxguardusage-vs-optional.md)。

## 卖法

- 「看见 Guardian of the mempool / 内存池守卫 就已经是 Technically optional / 可以不跑 CheckTx / 已经四门已经结算 / validate-no-apply bundled 第三件事 interchangeable。」
- 「看见 every node runs CheckTx before letting a transaction into its local mempool / 每条节点先跑 CheckTx 才让进本地池 就已经 RPC broadcast 别的节点也会跑 / 已经进了池就开始流言 / Check 通过就是已进提案 / CheckTx 过了就 forever valid。」
- 「看见 before letting into its local mempool / 才让进本地池 就已经 may come from external user or another node 交差 / 已经保证不重放 / Code≠0 rejected bundled interchangeable。」

## 为什么错

官方把 Guardian of the mempool、every node runs CheckTx before letting into its local mempool、before letting into its local mempool 写成三件独立的实现事。把它们卖成 optional / 四门已经结算 / 已经保证不重放，会把 Methods Usage Guardian 语义、本地池入口守卫、来源/重放三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage Guardian，必须分开 Guardian of the mempool、every node runs CheckTx before letting into local mempool、before letting into its local mempool 三个名字，不要把它们卖成 optional / 四门已经结算 / 已经保证不重放。

## 和相邻反模式

- [checktxguard-sold-as-optional](checktxguard-sold-as-optional.md) 是 CheckTx 守卫余量 bundled 全段，不是本页 Usage Guardian 专用三事。
- [chktxsource-sold-as-replay](chktxsource-sold-as-replay.md) 是 tx source 就等于已经保证不重放，不是本页 before letting into local mempool 专用边界。
- [checktxopt-sold-as-block](checktxopt-sold-as-block.md) 是 optional 就等于四门结算，不是本页 Guardian 单句。
