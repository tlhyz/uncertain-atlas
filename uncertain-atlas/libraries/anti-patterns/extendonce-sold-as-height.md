# 反模式：看见一轮最多一张 Precommit 就当成已经能再签一张 / 看见 ExtendVote 只在即将广播非 nil Precommit 时才叫就当成已经签了 nil 票 / 看见一轮只能交出一份扩展就当成已经是每一高度一份

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Requirement 6 之前。  
**例**：[一轮最多一张 Precommit ≠ 已经能再签一张](../../tracks/implementation/worked-example-extend-once-vs-round.md)。

## 塌法

1. 看见正确进程在一轮 *r*、高度 *h* 最多广播一张 Precommit / 看见到了 Precommit 步，就当成已经能再签一张，或当成已经是扩展本身。
2. 看见 `ExtendVote` 只在即将广播非 `nil` Precommit 时才叫 / 看见叫了 ExtendVote，就当成已经签了 nil 票，或当成每张票都会叫。
3. 看见正确进程在一轮 *r*、高度 *h* 只能交出一份扩展 / 看见交了一份，就当成已经是每一高度一份，或当成已经是正确进程交出的扩展必须被正确接收者 Verify Accept。

## 为什么会出事

官方写：正确进程在一轮 *r*、高度 *h* 最多广播一张 Precommit。`ExtendVote` 只在即将广播非 `nil` Precommit 时才叫。因此正确进程在这一轮这一高只能交出一份扩展。

## 和相邻反模式

- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是验签拒收整张预提交就已经是块非法，不是本页这种一轮最多一张 Precommit 不是已经能再签一张。
- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是同一块不是已经是同一份扩展，不是本页这种 ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票。
- [req6coherence-sold-as-accept](req6coherence-sold-as-accept.md) 是正确进程交出的扩展必须被正确接收者 Verify Accept，不是本页这种一轮只能交出一份扩展不是已经是每一高度一份。
