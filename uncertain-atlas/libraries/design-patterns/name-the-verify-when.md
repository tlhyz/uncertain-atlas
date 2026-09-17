# 模式：把 Verify 何时调用三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage。  
**例**：[空扩展仍会调 Verify ≠ 已经跳过 Verify](../../tracks/implementation/worked-example-verify-when-vs-empty.md)。

## 三个名字

1. **空扩展仍会调 Verify 不是已经跳过 Verify：** 看见发送方选择不扩不是已经是空扩展仍验签。
2. **不对本进程自己发出的 Precommit 调用不是已经自己验过：** 看见是本地票不是已经 Accept。
3. **请求里的 hash 不是已经对该块跑过 Process：** 看见指向某块不是已经是提议者那边也会叫 Process。

## 为什么要分开叫

官方把空扩展仍会调 Verify、不调本地票、hash 不保证已经 Process 写成三件事。把它们叫成一个「看见空扩展就已经跳过 Verify」，会把拒收整张预提交、Req 6 必须 Accept 和提议者 Process 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见空扩展就已经跳过 Verify」，先数清问的是空扩展仍会调 Verify 不是已经跳过 Verify、不对本进程自己发出的 Precommit 调用不是已经自己验过，还是请求里的 hash 不是已经对该块跑过 Process，再决定要不要同一次发布。
