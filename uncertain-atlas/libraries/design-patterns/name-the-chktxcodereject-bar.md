# 模式：把 CheckTx Usage Code≠0 rejected 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[Code≠0 rejected ≠ 已经 Check 通过就是已进提案](../../tracks/implementation/worked-example-chktxcodereject-vs-proposal.md)。

## 三个名字

1. **Code≠0 will be rejected / will not be broadcast 不是已经流言 / CheckTx 守卫 bundled interchangeable：** 看见 Methods Usage 侧 Code 拒路径，不是 mempool guard 或 P2P 流言 bundled interchangeable。
2. **will not be included in a proposal block 不是 Check 通过就是已进提案 / forever valid / Finalize Code≠0 仍在块里：** 看见不会进提案块，不是四门结算或 Finalize 回执 interchangeable。
3. **CometBFT attributes no other value 不是 CheckTx Data 已被引擎用了 / optional bundled / validate-no-apply bundled interchangeable：** 看见 Usage Code 语义，不是 CheckTx 回包 Data 或 optional / validate-no-apply bundled interchangeable。

## 为什么要分开叫

官方把 CheckTx Usage 里 Code≠0 will be rejected、will not be broadcast / included in a proposal block、CometBFT attributes no other value to the response code，和 Check 通过就是已进提案（33）、forever valid（301）、Finalize Code≠0 仍在块里（316）、CheckTx 回包 Data（317）、optional（373）、validate-no-apply（486）写成三个名字。把它们叫成一个「看见 CheckTx 回了非零码就已经没进块、已经交差、已经 forever valid」，会把池门 Code 拒路径、不进提案块、Code 语义三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage Code≠0 rejected，先数清问的是 Code≠0 会拒 / 不会广播 是不是已经流言 / CheckTx 守卫 bundled interchangeable、不会进提案块 是不是 Check 通过就是已进提案 / forever valid / Finalize Code≠0 仍在块里 interchangeable、CometBFT attributes no other value 是不是 CheckTx Data 已被引擎用了 / optional bundled / validate-no-apply bundled interchangeable，再决定要不要同一次发布。
