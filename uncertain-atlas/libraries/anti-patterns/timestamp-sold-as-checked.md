# 反模式：看见票或提案带了 Timestamp 就当成已经验过这个时间 / 看见冲突提案就当成已经有证据 / 看见非法票被断开就当成已经罚了签的人

**层次**：共识 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Validator Signing](https://github.com/cometbft/cometbft/blob/main/spec/consensus/signing.md)。  
**例**：[票上 Timestamp ≠ 已经验过](../../tracks/consensus/worked-example-vote-ts-vs-checked.md)。

## 塌法

1. 看见票或提案带了 Timestamp / 看见字段在，就当成已经验过这个时间。
2. 看见冲突提案 / 看见双签证据机制，就当成已经有提案证据。
3. 看见非法票被断开 / 看见没过基本校验，就当成已经罚了签的人。
4. 看见 BFT Time 会用 precommit 时间，就当成收到时已经验过。
5. 看见「以后也许有提案证据」，就当成已经有。

## 为什么会出事

官方写：收到的提案或票上的时间戳目前没有校验。冲突提案目前没有证据。非法对象可能让对等节点被断开，但没有明确机制去罚签了它们的验证者。

## 和相邻反模式

- [rejoin-sold-as-head](rejoin-sold-as-head.md) 是换轮 ≠ 已经换了集合，不是本页。
- [wal-sold-as-signed](wal-sold-as-signed.md) 是写下 ≠ 已经 fsync，不是本页这种收到时校验。
