# 反模式：看见到了 H 就当成已经 Prepare 带了扩展 / 看见 H+1 带了扩展就当成已经是本高度刚签的 / 看见 h < H 带了扩展就当成已经合法

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / Application configuration required to switch to ABCI 2.0。  
**例**：[到了 H ≠ 已经 Prepare 带了扩展](../../tracks/implementation/worked-example-ve-height-vs-prepare.md)。

## 塌法

1. 看见到了 H / 看见已经叫了 `ExtendVote`，就当成已经 Prepare 带了扩展。
2. 看见 H+1 的 `PrepareProposal` 带了扩展，就当成已经是本高度刚签的扩展。
3. 看见 `h < H` 的预提交带了扩展，就当成已经合法，或当成已经启用。

## 为什么会出事

官方写：到了 H，Prepare 还不会带投票扩展，但会调 ExtendVote 和 VerifyVoteExtension。到 H+1，Prepare 才带高度 H 的扩展。h < H 时，带扩展的预提交被当成畸形拒收。H 之后不能关，扩展必须签过且在场。

## 和相邻反模式

- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是验签拒收整张预提交、`s_h` 不得依赖本高收到的 *e*，不是本页这种 H / H+1 切换。
- [enable-height-sold-as-safe](enable-height-sold-as-safe.md) 是治理改 enable-height 会让未升级节点 panic，不是本页。
- [extension-sold-as-voting-power](extension-sold-as-voting-power.md) 是提议者注入的扩展不是投票权，不是本页。
