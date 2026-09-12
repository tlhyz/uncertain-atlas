# 先给客户端默认气限起名（name-the-default-gas）

> 类型：design pattern  
> 对读：不变量 211；C215；反模式 [`../anti-patterns/default-sold-as-cap.md`](../anti-patterns/default-sold-as-cap.md)；[`../../tracks/implementation/worked-example-default-gas-vs-cap.md`](../../tracks/implementation/worked-example-default-gas-vs-cap.md)。

设计或讲解「气限抬了」时，先分开四个名字：

1. **客户端默认气限** — 默认配置里生成的块气建议值，不是已经是协议帽。
2. **绑到硬分叉发布** — 用发版日把各家默认齐起来，不是已经改了共识。
3. **默认配置齐了** — 各家出厂值同一档，不是已经是单笔气帽。
4. **7935** — 默认配置建议，不是单笔气帽，也不是编码硬帽。

四句对照：

- 看见的是客户端默认，还是协议已经写死块气？
- 看见的是绑到一次发版，还是共识已经改了？
- 看见的是默认齐了，还是已经是单笔气帽？
- 这是 7935，还是已经是 203 / 202 / 96？

不要和单笔气帽≠块气（不变量 203）、编码硬帽≠气限（不变量 202）、通道尺寸（不变量 96）糊成「气限已经抬了」一句。
