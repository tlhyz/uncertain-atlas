# 工作实例：脚本里的 CSV 不是绝对锁，也不是「CSV 部署」四个字

> **事实 / 推断 / 建议** 已分开。
> 对照：[L2.1](../../courses/level-02-state/L02-M01-utxo.md)、[L3.1](../../courses/level-03-bitcoin/L03-M01-nakamoto-finality.md)、[CLTV ≠ nLockTime 已锁](worked-example-cltv-vs-nlocktime.md)、[MTP 三把尺](../consensus/worked-example-mtp.md)。
> 主文献：[BIP-68](https://github.com/bitcoin/bips/blob/master/bip-0068.mediawiki) Relative lock-time using consensus-enforced sequence numbers；[BIP-112](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) CHECKSEQUENCEVERIFY。官方 BIP。不另写 19 节。
> 本页钉 **脚本里的 CSV ≠ nSequence 已经把输出相对锁住**、**相对锁 ≠ 绝对锁**、**CSV 软分叉部署 ≠ 已经在讲 CHECKSEQUENCEVERIFY 操作码**、**nSequence 有数 ≠ 已经是相对锁**。不抄位旗 / 粒度 / 例脚本。不写怎样绕过相对锁。

---

## 0. 先修

- [不变量 164](../../libraries/invariants/README.md) CLTV 比的是 nLockTime
- [不变量 41](../../libraries/invariants/README.md) 「CSV 之后」locktime 看父 MTP
- [不变量 163](../../libraries/invariants/README.md) coinbase 成熟
- [不变量 165](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见文案写「CSV 之后」，以为已经在讲 CHECKSEQUENCEVERIFY；或看见输入填了 nSequence，以为输出已经相对锁住；或看见脚本写了 CSV，以为和 CLTV 一样在锁一个绝对高度。

官方句（事实）：

- BIP-68：给 nSequence 新的**共识**含义：相对锁时。一笔已签输入，在对应输出确认之后的一段年龄之内，保持非法。年龄按块数或时间跨度计。
- 官方对照：nLockTime 挡住的是「到某个日期才能挖」；nSequence 被改写成挡住「花掉的那张输出还不够老」。
- 官方：某一位关掉，则 nSequence **没有**共识相对锁含义，在目前规则下可以进任何块。
- 官方：这些新规则不作用于 coinbase 输入的 nSequence。
- BIP-112：新操作码 CHECKSEQUENCEVERIFY，**和 BIP-68 一起**，让脚本路径能按「被花输出的年龄」收紧。
- CSV 把栈顶和**该输入的 nSequence**相比，从而间接证明想要的最小年龄已经到；年龄没到，带这条路径的脚本过不了，交易不得被选进块。
- 下列任一为真，脚本必须失败（操作数没关掉相对锁时）：栈空；栈顶小于 0；交易版本不够高；该输入 nSequence 关掉了相对锁；相对锁类型不同；掩码之后栈顶大于该输入 nSequence。
- 操作数自己关掉相对锁时，官方写成继续当 NOP。
- BIP-112 写明：必须和 BIP-68、BIP-113 **同一机制同时部署**。文案里的「CSV 之后」常常指这次部署，不是已经在讲操作码。
- 规范**没有**把「填了 nSequence」写成输出已经相对锁住，也没有把 CSV 写成已经是 CLTV，也没有把部署名写成已经是脚本锁。

部署名、交易字段、输出脚本，是三件事。

---

## 2. 直觉（ELI15）

绝对锁是墙上的日期。  
相对锁是「货上架之后再等几天」。  
店门口挂着「CSV 店庆」，不等于柜台上已经在用相对锁验票。  
票根上写了序号，也不等于这张票已经按规定等过了。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| BIP-68 相对锁 | 被花输出的年龄；nSequence 的共识含义 | 交易 nLockTime；填了序号就已经锁 |
| BIP-112 CSV | 脚本拿栈顶跟**该输入 nSequence**比 | 已经是 CLTV；已经在跟现在比 |
| CSV 部署 | 与 BIP-68 / BIP-113 同时激活的那次软分叉 | 已经在讲 CHECKSEQUENCEVERIFY 操作码 |
| 关掉相对锁 | 该 nSequence 没有共识年龄含义 | 相对锁已经生效 |

---

## 4. 最小案例

一条 Bitcoin 要对齐「这一口气锁的是年龄还是日期」。

1. 输入填了 nSequence。规范：关掉相对锁则没有共识年龄含义。有数不是已经锁。
2. 输出脚本有 CSV。规范：比的是该输入 nSequence。不是 nLockTime，不是墙上现在。
3. 交易版本不够高。规范：相对锁规则不按 BIP-68 生效；CSV 这条路径必须失败。
4. 有人把「CSV 之后 locktime 看 MTP」听成已经在讲操作码。那是部署名 + BIP-113（不变量 41）。本页是脚本与 nSequence。
5. 有人把这听成 CLTV（不变量 164）。CLTV 是绝对点；本页是输出确认之后的年龄。
6. 有人把这听成 coinbase 成熟（不变量 163）。成熟是出块奖励年龄；本页是任意输出的相对脚本锁。官方：相对锁规则不作用于 coinbase 输入。
7. 时钟从输出确认才开始。官方动机：相对锁不必像绝对锁那样先关通道再重开。

「填了 nSequence 所以已经相对锁 / CSV 三个字已经是操作码 / CSV 已经是 CLTV」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | 无新原语 |
| 协议 | 必须点名问的是部署名、nSequence，还是脚本 CSV |
| 实现 | 版本不够、关掉相对锁、类型不同，两实现必须同拒 |
| 部署 | 与 BIP-68 / BIP-113 同时；旧节点把该操作码当 NOP |
| 经济 | 相对锁的钟从确认才走；不是绝对日期已经到 |

**推断：** 产品句若只写「有 CSV」，读者会把部署名、字段、脚本听成一盏灯。  
**建议：** 第一版若做相对时间锁，必须写清锁的是被花输出的年龄，并且花费输入的 nSequence 要同类、没关掉、版本够。不要发明「CSV = CLTV」。不要把「CSV 之后」写成已经在讲操作码。不要抄位旗。

---

## 6. 和另外几句不是同一句

1. **CLTV ≠ nLockTime 已锁**（不变量 164）：绝对点。本页是相对年龄。
2. **MTP 三把尺**（不变量 41）：文案「CSV 之后」指部署 + BIP-113 钟。本页是操作码与 nSequence。
3. **coinbase 成熟**（不变量 163）：奖励年龄。官方：相对锁不作用于 coinbase 输入。
4. **策略 ≠ 共识**（不变量 144）：本页是共识脚本 / 序列锁，不是本地不转发。
5. **6 确认 ≠ 协议最终**（L3.1）：商家政策。本页不是确认数。
6. **置位 ≠ 已激活**（不变量 171）：版本位四态。本页是部署名不是操作码，不是示意/锁定/激活状态机。

不要抄位旗 / 粒度秒数 / 激活时间戳 / 例脚本。不要写怎样关掉相对锁绕过 CSV，或怎样拼闪电 / HTLC / 双向通道。不编博物馆页。不另写 19 节。Tapscript 操作码、通道实现细则是另一对象。

---

## 7. 「不确定」测试句（建议）

```text
脚本里的 CSV ≠ nSequence 已经把输出相对锁住
相对锁 ≠ 绝对锁
CSV 软分叉部署 ≠ 已经在讲 CHECKSEQUENCEVERIFY 操作码
nSequence 有数 ≠ 已经是相对锁
```

语料：[C169](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「填了 nSequence = 已经相对锁。」「CSV = CLTV。」「CSV 之后 = 已经在讲操作码。」「相对锁从墙上现在开始。」  
**边界：** 不抄位旗。不另写 19 节。不写怎样绕过。CLTV 见 **C168**。MTP 见不变量 41。
