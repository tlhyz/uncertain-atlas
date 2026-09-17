# 先给 RLP 编码硬帽起名（name-the-rlp-cap）

> 类型：design pattern  
> 对读：不变量 202；C206；反模式 [`../anti-patterns/cap-sold-as-gas.md`](../anti-patterns/cap-sold-as-gas.md)；[`../../tracks/implementation/worked-example-rlp-cap-vs-gas.md`](../../tracks/implementation/worked-example-rlp-cap-vs-gas.md)。

设计或讲解「块不能太大」时，先分开四个名字：

1. **RLP 编码硬帽** — 执行块编码后的协议级字节上限，不是已经改了气限。
2. **共识层流言不传** — 更大的块不会被信标流言传开，不是执行层已经判非法。
3. **给信标块留边** — 执行帽里预留信标空间，不是已经并成一份编码。
4. **7934** — 独立于气的编码谓词，不是 7623，不是 1559，也不是不变量 96。

四句对照：

- 看见的是编码硬帽，还是已经改了气限？
- 看见的是流言不传，还是执行层已经非法？
- 看见的是给信标块留边，还是已经并成一份编码？
- 这是 7934，还是已经是 7623 / 1559 / 96？

不要和 [`name-the-calldata-floor.md`](name-the-calldata-floor.md)（地板 ≠ 执行气）、气≠墙钟（不变量 101）、通道尺寸（不变量 96）糊成「块太大」一句。
