# 反模式：把 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 not already only liveness / not already block invalid / not already nondet 正式三事（348 余量） 卖成 已经只是活性问题 / 已经是块非法 / 已经是非确定 bug

**层次**：实现 / Extend–Verify 一致性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-req6-notliveness-vs-bundled.md](../../tracks/implementation/worked-example-req6-notliveness-vs-bundled.md)。

官方把正确进程交出的扩展必须被正确接收者 Verify Accept / Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 / 会面对和 Req 5 同一类活性问题 三条核心句写成三件独立的实现事。把它们卖成已经只是活性问题 / 已经是块非法 / 已经是非确定 bug，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 正式三事（348 余量），必须分开 not already only liveness、not already block invalid、not already nondet 三件事，不要和 348 / 341 / 34 / 869 / 871 糊成一句。

## 和相邻反模式

- [req6-notany-sold-as-bundled](req6-notany-sold-as-bundled.md) 是必须 Accept 单句边界（869 item 1），不是本页确定 bug 边界。
- Verify 必须只依赖扩展、这块和上一份状态是不变量 341，不是本页确定 bug 边界。
