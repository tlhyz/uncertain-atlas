# Level 0 · 区块链作为一台机器

优先级：必学  
位置：`uncertain-atlas/courses/`（课程轨）  
与交易回测代码无关。

---

## 你读完应该能做什么

1. 一条链首先是一台**复制状态机**，不是一个「更快的数据库」。
2. 交易是「签名过的状态变更请求」，不是「转账按钮」。
3. 「我点了发送」「节点看见了」「打进某个块」「再也不大可能被撤」是四件不同的事。
4. 双花、假余额、假确认，分别破坏哪一层保证。
5. 为什么现在还不能为「不确定」挑选共识算法。

---

## 课程序列

| 课 | 文件 | 核心问题 |
|---|---|---|
| 0.1 | [L00-M01-ledger-problem.md](L00-M01-ledger-problem.md) | 为什么不能各记各的账？ |
| 0.2 | [L00-M02-replicated-state-machine.md](L00-M02-replicated-state-machine.md) | 一条链到底在计算什么？ |
| 0.3 | [L00-M03-identity-and-authority.md](L00-M03-identity-and-authority.md) | 链怎么知道谁有权改状态？ |
| 0.4 | [L00-M04-transaction.md](L00-M04-transaction.md) | 交易究竟是什么对象？ |
| 0.5 | [L00-M05-block-and-order.md](L00-M05-block-and-order.md) | 为什么要把交易装进区块？ |
| 0.6 | [L00-M06-agreement-problem.md](L00-M06-agreement-problem.md) | 为什么「投个票过半数」不够？ |
| 0.7 | [L00-M07-one-payment-lifecycle.md](L00-M07-one-payment-lifecycle.md) | 一笔转账从点击到确认经过哪些门？看见付款 URI ≠ 已经授权（不变量 255）；看见签过的消息 ≠ 已经控制资金（不变量 258）；看见静默付款地址 ≠ 已经有输出（不变量 260）；看见付款码 ≠ 已经是存款地址 / 通知输出 ≠ 已经能花（不变量 273）；看见可读名字 ≠ 已经该走 DNS（不变量 261）；带 pj= 的付款 URI ≠ 已经是 payjoin 付款 / 原始包 ≠ 已经是提案 / 收款方加了输入 ≠ 已经另开一笔（不变量 290）；储备证明交易 ≠ 已经能花 / 其余输入签过 ≠ 已经控制资金 / POR 栏 ≠ 已经是普通花费（不变量 293）；本页这种签消息 ≠ 已经是 322 / 头字节标了种类 ≠ 已经有地址 / 旧 P2PKH 习惯 ≠ 已经互操作（不变量 294）；付款请求 ≠ 已经授权 / 付款报文 ≠ 已经是回执 / 回执 ≠ 已经最终（不变量 295） |
| 0.8 | [L00-M08-five-kinds-of-guarantees.md](L00-M08-five-kinds-of-guarantees.md) | 五种保证如何分开？ |
| 0.9 | [L00-M09-fake-learning.md](L00-M09-fake-learning.md) | 哪些常见说法其实在害你？ |
| 0.10 | [L00-M10-uncertain-lens.md](L00-M10-uncertain-lens.md) | 「不确定」该问什么、还不该决定什么？ |

试题已集中到 [`../../exams/level-00.md`](../../exams/level-00.md)，现在先不要做。

下一层课程：[`../level-01-crypto/`](../level-01-crypto/README.md)
