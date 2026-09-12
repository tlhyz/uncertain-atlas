# 反模式：看见后继地址流言就当成已经连得上 / 已经只收后继格式 / 已经连上那种网

**层次**：网络 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-155](https://github.com/bitcoin/bips/blob/master/bip-0155.mediawiki)。  
**例**：[后继地址 ≠ 已经连得上](../../tracks/network/worked-example-addrv2-vs-reachable.md)。

## 塌法

1. 看见后继地址消息，就当成已经连上这个节点，或当成已经可达。
2. 看见发了 sendaddrv2，就当成已经只收后继格式，或当成旧地址消息已经退役。
3. 看见发或不发这条信号，就当成未请求地址偏好已经谈妥。
4. 看见在传某种网上的地址，就当成已经连上那种网。
5. 看见同一份地址换了编号，就当成已经是另一个人。
6. 看见旧洋葱类型编号，就当成已经能当隐藏服务用。
7. 看见本页，就当成已经写了传输加密，或当成已经是发现记录。

## 为什么会出事

官方写：这条消息只换能装更长端点的容器。偏好信号不管未请求地址。认识的网即使没连上也可以传。旧洋葱类型不得再传。本页不是网上已经私人，也不是已经有当前记录。

## 和相邻反模式

- [v2-sold-as-private](v2-sold-as-private.md) 是传输加密 ≠ 已经私人，不是本页。
- [privatebroadcast-sold-as-hidden](privatebroadcast-sold-as-hidden.md) 是隐私广播降级 ≠ 仍走代理，不是本页。
- [enr-seq-sold-as-have](enr-seq-sold-as-have.md) 是 ping 序号 ≠ 已经有当前记录，不是本页。
