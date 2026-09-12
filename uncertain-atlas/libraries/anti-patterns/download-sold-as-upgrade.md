# 反模式：自动下载二进制被写成升级已经完成

> 真值：[ASA-2023-001](../../tracks/failure-museum/asa-2023-001.md)、[不变式 80](../invariants/README.md)。亲戚：[ics23-sold-as-sound](ics23-sold-as-sound.md)、[admin-god-key](admin-god-key.md)。

## 一句话

看见升级高度到了、管家换了程序，就写成共识升级已完成；或把自动下载开关写成验证者默认安全。

## 正确写法

「升级高度是协议对象。二进制从哪来是部署对象。进程管理器不得默认从网上拉可执行文件。打开自动下载不是默认安全的升级路径。」
