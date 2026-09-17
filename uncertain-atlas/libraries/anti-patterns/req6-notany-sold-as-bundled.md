# 反模式：把 正确进程交出的扩展必须被正确接收者 Verify Accept not already any extension Accepts / not already default Accept / not already settled 正式三事（348 余量） 卖成 已经是任意扩展都会 Accept / 已经写了默认 Accept / 已经交差

**层次**：实现 / Extend–Verify 一致性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-req6-notany-vs-bundled.md](../../tracks/implementation/worked-example-req6-notany-vs-bundled.md)。

官方把正确进程交出的扩展必须被正确接收者 Verify Accept / Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 / 会面对和 Req 5 同一类活性问题 三条核心句写成三件独立的实现事。把它们卖成已经是任意扩展都会 Accept / 已经写了默认 Accept / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看正确进程交出的扩展必须被正确接收者 Verify Accept 正式三事（348 余量），必须分开 not already any extension Accepts、not already default Accept、not already settled 三件事，不要和 348 / 34 / 349 / 868 / 870 / 871 糊成一句。

## 和相邻反模式

- [req9-notext-sold-as-bundled](req9-notext-sold-as-bundled.md) 是 Extend/Verify 无副作用（349/868），不是本页必须 Accept 边界。
- 验签拒收整张预提交就已经是块非法是不变量 34，不是本页必须 Accept 边界。
