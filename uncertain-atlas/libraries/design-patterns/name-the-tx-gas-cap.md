# 先给单笔气帽起名（name-the-tx-gas-cap）

> 类型：design pattern  
> 对读：不变量 203；C207；反模式 [`../anti-patterns/txcap-sold-as-blockgas.md`](../anti-patterns/txcap-sold-as-blockgas.md)；[`../../tracks/implementation/worked-example-tx-gas-cap-vs-block.md`](../../tracks/implementation/worked-example-tx-gas-cap-vs-block.md)。

设计或讲解「交易不能太大」时，先分开四个名字：

1. **单笔气帽** — 任何一笔交易的协议级气上限，不是已经改了块气限。
2. **入池拒掉** — 超帽的单笔不进池，不是已经验过这块。
3. **块里有一笔超帽** — 整块非法，不是只是策略拒绝。
4. **7825** — 独立于块气限的单笔气谓词，不是 7934，不是 7623，也不是不变量 96。

四句对照：

- 看见的是单笔气帽，还是已经改了块气限？
- 看见的是入池拒掉，还是已经验过块？
- 看见的是块里有一笔超帽，还是只是策略拒绝？
- 这是 7825，还是已经是 7934 / 7623 / 96？

不要和 [`name-the-rlp-cap.md`](name-the-rlp-cap.md)（编码帽 ≠ 气限）、[`name-the-calldata-floor.md`](name-the-calldata-floor.md)（地板 ≠ 执行气）、通道尺寸（不变量 96）糊成「交易太大」一句。
