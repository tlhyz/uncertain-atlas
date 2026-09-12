# L3.1 Nakamoto 与概率最终

优先级：必学  
先修：L0.6，L2.1，`protocols/bitcoin/report.md` 第 6、11、14 节

---

## A. 先修知识

复制需要全序。Bitcoin 用「最重的合法链」当全序，而不是 +2/3 commit。

---

## B. 核心问题

**为什么没有一张「不可逆证书」，商家仍可能把 Bitcoin 当结算层？他们到底在赌什么？**

---

## C. 直觉（ELI15）

比赛堆砖。谁的砖堆（工作量）更高，大家跟谁。  
你刚看见新的一层，对手如果暗地里堆得更高，你这一层可能被拆掉。

每多一层，对手要暗地重堆的砖就更多。砖不是免费的。  
所以「6 个确认」不是魔法数字，是：**改这段历史的期望成本，已经高于这笔货的价值**——对那个商家、那种对手而言。

换一家只看 1 个确认的咖啡店，赌的是小额 + 攻击不值得。  
换一家跨所大额，确认数会完全不同。这是经济层，不是协议 commit。

---

## D. 正式定义

**最重链：** 在所有自己验证过的合法链里，选累计工作最大的。难度调整后，「最长」不等于「最重」。

**k-confirmation：** 交易之上又长了 k 个有效块。重组深度 > k 则该交易可能从 canonical 历史消失。

**事实：** 协议不定义「最终」。最终是用户与交易所的政策。  
**事实：** 若多数算力合作改写，浅确认可被双花。白皮书第 11 节用概率谈攻击者赶上。  
进了块的 coinbase 不是已经能花。普通确认深度不是奖励成熟窗。精读：[`../../tracks/economic/worked-example-coinbase-vs-mature.md`](../../tracks/economic/worked-example-coinbase-vs-mature.md)（不变量 163）。
脚本里的 CLTV 不是交易 nLockTime 已经把输出锁住。精读：[`../../tracks/state-models/worked-example-cltv-vs-nlocktime.md`](../../tracks/state-models/worked-example-cltv-vs-nlocktime.md)（不变量 164）。
脚本里的 CSV 不是绝对锁，也不是「CSV 部署」四个字。精读：[`../../tracks/state-models/worked-example-csv-vs-cltv.md`](../../tracks/state-models/worked-example-csv-vs-cltv.md)（不变量 165）。

---

## E. 最小案例

高度 100 出现 2a（含付给商家的 T）、2b（不含 T）。你跟 2a。  
高度 101–105 都建在 2a 上。商家发货。  
攻击者出示一条从 99 分出来、工作量更大的链，T 不在上面。全节点跟重的。货已出，币不在。

CometBFT 在 commit 后不允许这个故事。Bitcoin 允许，但要用功买。

---

## F. 真实项目

Bitcoin 主网、大量侧链与交易所政策。  
「不确定」若抄确认数当 UI，必须写明这是风险偏好，不是数学锁。

---

## G. 源码

预告：Bitcoin Core 的链选择 / `nChainWork`。先读档案第 16–17 节再打开。

---

## H. 攻击者视角

1. 0-conf 双花。  
2. 租算力做浅重组。  
3. 分区：两边各长，合拢时一侧重。  
4. 让钱包把 1 confirmation 画成绿勾。

---

## I. Trade-off

得到：分区时不必立刻停机，无许可出块。  
失去：商家必须自己做经济最终性；用户会被假确认骗。

---

## J. 对「不确定」的意义

后量子结算如果对用户说「到了」，却用概率最终，是文案犯罪。  
**建议：** 要么学 Bitcoin 把确认政策写得极老实，要么学 CometBFT 给 commit。不要混成「我们 BFT 但有时会重组」。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | PoW 哈希假设；交易签另账 |
| 协议 | 最重合法链；确认是政策，不是协议最终 |
| 实现 | 难度 / 工作量计量必须相同 |
| 部署 | 你看见的最重链 ⊆ 你连到的图 |
| 经济 | k 确认只对未日蚀且看见主网算力的人有意义 |

**禁止假学习：** 「6 确认是协议最终。」「最长链永远等于最重链。」「进了块的 coinbase = 已经能花。」「填了 nLockTime = 输出已经锁住。」「CSV = CLTV。」「CSV 之后 = 已经在讲操作码。」
**边界：** 日蚀在 L3.4。见 tracks/finality。头上的时间不是「全网现在」：太早看父 MTP，locktime（BIP113 后）也看父 MTP，太新看本节点钟，见 [`../../tracks/consensus/worked-example-mtp.md`](../../tracks/consensus/worked-example-mtp.md)。进了块的 coinbase ≠ 已经能花：[`../../tracks/economic/worked-example-coinbase-vs-mature.md`](../../tracks/economic/worked-example-coinbase-vs-mature.md)（不变量 163）。脚本里的 CLTV ≠ 交易 nLockTime 已经把输出锁住：[`../../tracks/state-models/worked-example-cltv-vs-nlocktime.md`](../../tracks/state-models/worked-example-cltv-vs-nlocktime.md)（不变量 164）。脚本里的 CSV ≠ 绝对锁 / ≠ 部署名：[`../../tracks/state-models/worked-example-csv-vs-cltv.md`](../../tracks/state-models/worked-example-csv-vs-cltv.md)（不变量 165）。
