# 工作实例：脚本里的 CLTV 不是交易上的 nLockTime 已经把输出锁住

> **事实 / 推断 / 建议** 已分开。
> 对照：[L2.1](../../courses/level-02-state/L02-M01-utxo.md)、[L3.1](../../courses/level-03-bitcoin/L03-M01-nakamoto-finality.md)、[MTP 三把尺](../consensus/worked-example-mtp.md)、[进块 ≠ 能花](../economic/worked-example-coinbase-vs-mature.md)。
> 主文献：[BIP-65](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) OP_CHECKLOCKTIMEVERIFY。官方 BIP。不另写 19 节。
> 本页钉 **脚本里的 CLTV ≠ 交易 nLockTime 已经把输出锁到那时**、**nLockTime 能证明将来能花 ≠ 已经证明现在不能花**、**CLTV 比的是花费交易的 nLockTime ≠ 墙上现在**、**输入已经 final ≠ CLTV 已经在生效**。不抄阈值 / 激活票数 / 例脚本。不写怎样绕过 CLTV。

---

## 0. 先修

- [L2.1](../../courses/level-02-state/L02-M01-utxo.md) 花费条件写在输出上
- [不变量 41](../../libraries/invariants/README.md) locktime 看哪把钟
- [不变量 163](../../libraries/invariants/README.md) coinbase 成熟
- [不变量 164](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见交易填了 nLockTime，以为输出已经锁到那个高度或时间；或看见脚本写了 CHECKLOCKTIMEVERIFY，以为已经在跟墙上现在比；或看见输入标成 final，以为时间锁已经生效。

官方句（事实）：

- BIP-65：新操作码让一笔**输出**可以在某个未来点之前花不掉。
- 交易上的 nLockTime 挡住的是**这笔交易**进块：高度或块时间没到，不得被挖。
- 官方对照：nLockTime 可以证明「将来**有可能**花掉这张输出」（构造一笔带 nLockTime 的合法花费）。它**不能**证明「在那之前**不可能**花」——别人可能另签一笔现在就能花的交易。
- CLTV 把栈顶和**花费交易的 nLockTime**相比，从而间接证明想要的高度或时间已经到；没到之前，这张输出保持不能花。
- 下列任一为真，脚本必须失败：栈空；栈顶小于 0；栈顶与 nLockTime 一个按高度、一个按时间戳；栈顶大于这笔交易的 nLockTime；该输入的 nSequence 是最大终值。
- 规范**没有**把「填了 nLockTime」写成输出已经锁住，也没有把 CLTV 写成已经在跟墙上现在比，也没有把输入 final 写成时间锁已经生效。

交易字段、输出脚本、墙上现在，是三件事。

---

## 2. 直觉（ELI15）

门上写「三点以后验票」，验的是票上印的时间，不是你手表。  
你手里有一张三点才能用的票，只能证明三点**可以**进；不能证明现在没有另一张立刻能用的票。  
把票根盖「作废」印，验票机就不看票上的时间了。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| nLockTime | 这笔花费交易最早何时能进块 | 输出已经锁到那时；现在不能被别的交易花 |
| CLTV | 脚本拿栈顶跟**本笔** nLockTime 比 | 已经在跟墙上现在 / 本块时间比 |
| 高度锁 vs 时间锁 | 两种类型必须同类才能比 | 填了数字就已经同类 |
| 输入 final | nSequence 最大则 nLockTime 功能被关掉 | CLTV 已经在生效 |

---

## 4. 最小案例

一条 Bitcoin 要对齐「这一口气输出锁的是哪一扇门」。

1. 交易填了 nLockTime。规范：这只约束**这一笔**何时能进块。不是输出已经锁住。
2. 输出脚本有 CLTV。规范：比的是花费交易的 nLockTime。不是墙上现在。
3. 栈顶按高度、交易按时间戳。规范：类型不同必须失败。
4. 输入 nSequence 是最大终值。规范：CLTV 这条路径必须失败；否则时间锁会被绕开。
5. 有人把这听成 MTP 三把尺（不变量 41）。本页是脚本对 nLockTime 的比较；41 是 nLockTime / 头时间看哪把钟。
6. 有人把这听成 coinbase 成熟（不变量 163）。本页是任意输出的脚本锁，不是出块奖励年龄。
7. 有人把这听成「填了 locktime = 已经不能现在花」。官方：那只证明将来可能花，不证明现在不能另花。

「填了 nLockTime 所以输出已经锁住 / CLTV 已经在看现在」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | 无新原语；签名仍不代替锁 |
| 协议 | 必须点名问的是交易字段、输出脚本，还是钟 |
| 实现 | 两实现必须同：类型不同要失败；final 输入要失败 |
| 部署 | 软分叉；旧节点把该操作码当 NOP |
| 经济 | 退款 / 托管若只靠预签 nLockTime，官方写明不能证明现在不能花 |

**推断：** 产品句若只写「有时间锁」，读者会把交易字段听成输出已经冻住。  
**建议：** 第一版若做绝对时间锁，必须写清锁在输出脚本上，并且花费交易的 nLockTime 要同类且不更早。可以跳过「看见填了 nLockTime 就已经锁住输出」。164 cltv vs nlocktime bundled unbundling 完成（1530 item 1 / 1531 item 2 / 1532 item 3）；精读 [`worked-example-cl65-notfld-vs-bundled.md`](worked-example-cl65-notfld-vs-bundled.md)（不变量 1530 item 1）、[`worked-example-cl65-notnow-vs-bundled.md`](worked-example-cl65-notnow-vs-bundled.md)（不变量 1531 item 2）、[`worked-example-cl65-notclk-vs-bundled.md`](worked-example-cl65-notclk-vs-bundled.md)（不变量 1532 item 3）。不要发明「填了 nLockTime = 输出已经锁住」。不要抄阈值。不要把输入 final 写成锁已经生效。

---

## 6. 和另外几句不是同一句

1. **MTP 三把尺**（不变量 41）：头太早 / locktime 看父 MTP / 头太新。本页是脚本与 nLockTime 比什么。
2. **coinbase 成熟**（不变量 163）：奖励年龄。本页是脚本锁。
3. **策略 ≠ 共识**（不变量 144）：本页是共识脚本失败，不是本地不转发。
4. **钥匙路径 ≠ 揭树**（不变量 153）：Taproot 路径。本页是绝对时间锁。
5. **6 确认 ≠ 协议最终**（L3.1）：商家政策。本页不是确认数。

不要抄类型阈值 / 激活票数 / 例脚本 / 实现字节宽度。不要写怎样用 final 输入绕过 CLTV，或怎样拼托管 / 支付通道退款。不编博物馆页。不另写 19 节。BIP-68 相对锁、BIP-112 CSV、BIP-113 钟、Tapscript 操作码是另一对象。

---

## 7. 「不确定」测试句（建议）

```text
脚本里的 CLTV ≠ 交易 nLockTime 已经把输出锁到那时
nLockTime 能证明将来能花 ≠ 已经证明现在不能花
CLTV 比的是花费交易的 nLockTime ≠ 墙上现在
输入已经 final ≠ CLTV 已经在生效
```

语料：[C168](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「填了 nLockTime = 输出已经锁住。」「CLTV = 已经在跟现在比。」「输入 final = 时间锁已经生效。」「高度数字和时刻数字可以直接比。」  
**边界：** 不抄阈值。不另写 19 节。不写怎样绕过。MTP 见不变量 41。成熟见 **C167**。
