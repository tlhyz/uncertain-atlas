# 反模式：迁移失败被写成目录里其它钱包已经安全

> 真值：[Bitcoin Core 2026-01-05](../../tracks/failure-museum/bitcoin-2026-01-wallet-migration-delete.md)、[不变式 120](../invariants/README.md)。亲戚：[wallet-load-sold-as-no-txid](wallet-load-sold-as-no-txid.md)、[uri-fetch-sold-as-verify](uri-fetch-sold-as-verify.md)。

## 一句话

看见现有用户不受影响，或看见官网下架了受影响安装包，就写成迁移失败不会动到同目录其它钱包。

## 正确写法

「迁移失败的清理必须只覆盖这次失败的对象。现有用户不受影响不是迁移路径已经安全。」
