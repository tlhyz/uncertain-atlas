# 反模式：看见空扩展仍会调 Verify 就当成已经跳过 Verify / 看见不对本进程自己发出的 Precommit 调用就当成已经自己验过 / 看见请求里的 hash 就当成已经对该块跑过 Process

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage。  
**例**：[空扩展仍会调 Verify ≠ 已经跳过 Verify](../../tracks/implementation/worked-example-verify-when-vs-empty.md)。

## 塌法

1. 看见空扩展（0 长度）引擎仍会调 `VerifyVoteExtension` / 看见发送方选择不扩，就当成已经跳过 Verify，或当成已经是空扩展仍验签。
2. 看见 `VerifyVoteExtension` 不对本进程自己发出的 Precommit 调用 / 看见是本地票，就当成已经自己验过，或当成已经 Accept。
3. 看见请求里的 `hash` / 看见指向某块，就当成已经对该块跑过 `ProcessProposal`，或当成已经是提议者那边也会叫 Process。

## 为什么会出事

官方写：CometBFT 即使是 0 长度扩展也会调 `VerifyVoteExtension`。空扩展表示发送方选择不扩。`VerifyVoteExtension` 不对本进程自己发出的 Precommit 调用。请求里的 `hash` 不保证这块已经通过 `ProcessProposal` 暴露给应用。

## 和相邻反模式

- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是验签拒收整张预提交就已经是块非法，不是本页这种空扩展仍会调 Verify 不是已经跳过 Verify。
- [req6coherence-sold-as-accept](req6coherence-sold-as-accept.md) 是正确进程交出的扩展必须被正确接收者 Verify Accept，不是本页这种不对本进程自己发出的 Precommit 调用不是已经自己验过。
- [processalso-sold-as-matched](processalso-sold-as-matched.md) 是 Process 也会在提议者那边叫不是已经不用再 Process，不是本页这种请求里的 hash 不是已经对该块跑过 Process。
