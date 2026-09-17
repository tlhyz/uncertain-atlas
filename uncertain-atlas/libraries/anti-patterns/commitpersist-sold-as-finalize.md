# 反模式：把 Commit Usage persist signal 正式三事卖成已经在 Finalize 改了就已经落盘 / 已经 Commit 不带参数就等于已经落盘

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Signal persist ≠ 已经在 Finalize 改了就已经落盘](../../tracks/implementation/worked-example-commitpersist-vs-finalize.md)。

## 卖法

- 「看见 Signal the Application to persist application state / 看见叫 Commit 就已经在 Finalize 改了状态 / 已经引擎 persist tx outputs / AppHash / ResultsHash。」
- 「看见 Application is expected to persist its state at the end of this call / 看见 Commit 不带参数就已经落盘 / 已经交差。」
- 「看见 Historical blocks may also be required for auditing / replay / light client verification / 看见 retain_height 默认 0 就已经在剪 / 已经没有历史。」

## 为什么错

官方把 persist signal、expected persist at end of this call、Historical blocks may also be required 写成三件独立的实现事。把它们卖成已经在 Finalize 落了、Commit 空请求就等于落盘、retain_height 默认 0 就等于在剪，会把应用 Commit 落盘、Commit 空请求、历史块用途 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage，必须分开 Signal persist application state、Expected persist at end of this call、Historical blocks required for auditing / replay / light client 三个名字，不要把它们卖成已经在 Finalize 改了就已经落盘 / 已经 Commit 不带参数就等于已经落盘。

## 和相邻反模式

- [crashsteps-sold-as-committed](../../libraries/anti-patterns/crashsteps-sold-as-committed.md) 是崩溃三步就已经 Commit，不是本页 Signal persist。
- [commitnoparam-sold-as-persist](../../libraries/anti-patterns/commitnoparam-sold-as-persist.md) 是 Commit 不带参数就已经落盘，不是本页 expected at end of this call。
- [retain-sold-as-kept](../../libraries/anti-patterns/retain-sold-as-kept.md) 是 retain_height 默认 0 就已经在剪，不是本页 Historical blocks required。
