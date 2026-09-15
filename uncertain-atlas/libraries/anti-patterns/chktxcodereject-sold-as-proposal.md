# 反模式：把 CheckTx Usage Code≠0 rejected 正式三事卖成没进块 / 已经 Check 通过 / 已经 forever valid

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Code≠0 rejected ≠ 已经 Check 通过就是已进提案](../../tracks/implementation/worked-example-chktxcodereject-vs-proposal.md)。

## 卖法

- 「看见 Transactions where CheckTxResponse.Code != 0 will be rejected / Code≠0 会拒 就已经没进块 / 已经不会广播 / 已经 CheckTx 守卫 bundled 第二句 interchangeable / 已经 RPC broadcast 别的节点也收不到。」
- 「看见 will not be broadcast to other nodes / or included in a proposal block / 不会进提案块 就已经 Check 通过就是已进提案 / 已经 CheckTx 过了就 forever valid / 已经像 Finalize Code≠0 那样没进块。」
- 「看见 CometBFT attributes no other value to the response code / 引擎对回包码不再赋予别的含义 就已经 CheckTx Data 被引擎用了 / 已经是 optional bundled 第二句 / 已经是 validate-no-apply bundled 第三件事 interchangeable。」

## 为什么错

官方把 Code≠0 will be rejected、will not be broadcast / included in a proposal block、CometBFT attributes no other value to the response code 写成三件独立的实现事。把它们卖成没进块 / 已经 Check 通过 / 已经 forever valid，会把 CheckTx 池门 Code 拒路径、不进提案块、Code 语义三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage Code≠0 rejected，必须分开 Code≠0 会拒 / 不会广播、不会进提案块、CometBFT attributes no other value 三个名字，不要把它们卖成没进块 / 已经 Check 通过 / 已经 forever valid。

## 和相邻反模式

- [chktxvalidate-sold-as-applied](chktxvalidate-sold-as-applied.md) 是 validate-no-apply 全段卖成交差，不是本页 Code≠0 拒路径专用三事。
- [checktxopt-sold-as-block](checktxopt-sold-as-block.md) 是 optional 就等于四门结算，不是本页 Code≠0 拒路径专用三事。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是 Check 通过就是已进提案，不是本页 will not be included in a proposal block 专用边界。
