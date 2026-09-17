# 反模式：自动打洞被写成全节点必开

> 真值：[UPnP 辅助](../../tracks/failure-museum/cve-2015-20111.md)、[不变式 53](../invariants/README.md)、[0.11.1 发行说明](https://bitcoincore.org/en/releases/0.11.1/)。

## 一句话

看见节点 IPv4 入口少，就写成必须默认开 UPnP；或把局域网打洞辅助写成和互联网 P2P 同一攻击面。

## 正确写法

「默认关掉自动打洞，是为了不让依赖库的洞变成全网结构风险。局域网假设备是另一类攻击者。」
