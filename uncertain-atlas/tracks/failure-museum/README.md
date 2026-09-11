# 失败博物馆

每案固定 7 问：发生了什么 / 根因 / 哪个 invariant / 为何测试没发现 / 修复 / 「不确定」怎么办 / 回归测试。

已归档：

- [cve-2018-17144](cve-2018-17144.md)（实现：重复输入）
- [cve-2010-5139](cve-2010-5139.md)（实现：输出求和溢出）
- [bip-0050-2013-fork](bip-0050-2013-fork.md)（实现：BDB 锁上限变成未写明的共识；BIP 50）
- [cve-2012-2459](cve-2012-2459.md)（协议构造+实现：Merkle 奇数复制 ⇒ 同根不同列表）
- [cve-2019-7167](cve-2019-7167.md)（密码：Sprout 证明可靠性破 ⇒ 屏蔽池可伪造）
- [cve-2021-39137](cve-2021-39137.md)（实现：Geth RETURNDATA 别名 ⇒ 少数分叉）

待补（有原始出处再写，不写传闻）：各链 halt、桥、其它客户端分歧、其它池的后续披露。

写法：[`../../courses/level-09-systems/L09-M09-failure-museum-method.md`](../../courses/level-09-systems/L09-M09-failure-museum-method.md)  
五层对照精读：[`worked-example-five-layers.md`](worked-example-five-layers.md)（同一通胀案，五层各说什么）。  
回流测试目录：[`../../libraries/adversarial-corpus/`](../../libraries/adversarial-corpus/README.md)。
