# 反模式：后来的 SELFDESTRUCT 被写成账户已经删掉

> 真值：[后来的自毁 ≠ 已删](../../tracks/state-models/worked-example-selfdestruct-vs-delete.md)、[不变式 160](../invariants/README.md)、[不变式 103](../invariants/README.md)。亲戚：[oog-sold-as-reverted](oog-sold-as-reverted.md)、[transient-sold-as-storage](transient-sold-as-storage.md)。

## 一句话

看见合约调了 `SELFDESTRUCT` 或余额转到了目标，就把后来的转账写成账户已经拆掉，或把同笔创建仍能拆写成以后任意一笔还能拆，或把自己当收款人写成已经烧掉。

## 正确写法

「后来的 SELFDESTRUCT 不是账户已经删掉。只转走余额不是代码和存储已经清。同笔创建再销毁不是以后任意一笔还能拆户。自己当收款人不是已经烧掉。」
