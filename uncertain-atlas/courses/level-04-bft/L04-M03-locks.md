# L4.3 锁、解锁、超时

优先级：必学  
先修：L4.1，L4.2

---

## A. 先修知识

相交保证两拨人的重叠里有诚实者。  
若诚实者可以随意改口，重叠也救不了两个最终值。

---

## B. 核心问题

**锁究竟锁住什么？什么时候允许解锁？为什么解锁规则写错会同时搞砸安全或活性？**

---

## C. 直觉

你在 r=0 已经对稿 A 举起「我愿意入档」的手。  
秘书还没盖章，起草人换了，新稿是 B。

若你可以立刻对 B 也举「入档」：骗子拼两张入档纸。  
若你永远不许改口：稿 A 其实没凑齐入档，全场卡死在 A。

所以锁是：

> 我一旦做过某种关键表态，就只能继续为那个值说话，**除非**我看见更高轮的合法证据，证明大家已经合法地放弃旧值。

超时强迫你换轮，但不自动允许你对冲突值做同等承诺。

---

## D. 正式定义（Tendermint/CometBFT 风格，逻辑级）

节点维护：

- `lockedValue` / `lockedRound`：我锁定的值与轮  
- 有的实现还有 `validValue`：我见过的、带足够 prevote 的较好值，供下一轮 proposer 重提，以免活性饿死

**锁上：** 当我发出（或决定发出）针对 v 的 precommit，且有 +2/3 prevote(v) 支撑时，锁定 v。  
**遵守锁：** 之后的 prevote/precommit 不得支持与 v 冲突的值，除非解锁条件满足。  
**解锁：** 看到更高轮 `r' > lockedRound` 的 +2/3 prevote(v')（合法证明「新一轮多数在看 v'」）。精确谓词以规范为准。

**事实：** 没有这套锁，第 4.1 节的相交推不出「同一高度至多一个 commit」。  
**推断：** 实现里最常见的事故是崩溃后忘记自己锁过什么（见 WAL 课）。

安全：两个 commit 需要两张 +2/3 precommit，相交诚实者因锁不能签两份。  
活性：解锁 + validValue + 超时，让旧锁在「其实没 commit」时能被更高轮带走。

---

## E. 最小案例

V2 在 r=0 锁定 A（已 precommit A，但全网没凑齐 commit）。  
r=1 的 proposer 若乱提 B，V2 仍 prevote A（或按规则投 nil），直到看见 r=1 上针对某值的合法 +2/3 prevote 证明。  
若规范允许用 validValue 重提 A，活性更好：不要无故换值。

错误实现：重启后 `lockedValue` 空了，V2 对 B 预提交 → 安全洞。

---

## F. 真实项目

CometBFT 规范中的 locking 规则。  
HotStuff：锁往往体现在「我认的最高 QC」。对照：都是「可引用的多数证据 + 不得后退」。

---

## G. 源码

预告：写 lock 的赋值点、所有投票出口是否检查 lock、重启是否从 WAL 恢复 lock。三处缺一即事故。

---

## H. 攻击者视角

1. 诱使节点对两个值 precommit。  
2. 崩溃注入：杀进程再拉起，看第二张票。  
3. 卡在永远解锁不成或永远锁死（活性）。

---

## I. Trade-off

锁越死：越安全，某一轮越容易饿死。  
锁越松：越好走，越像「过 2/3 就完事」。

---

## J. 对「不确定」的意义

这是主骨架。任何「我们用了某种 BFT」的 PR，先问：

1. 锁存在哪  
2. 崩溃后锁在哪  
3. 哪条测试证明不会对两值 precommit  

答不出，就是还没做共识。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | 锁值上的证明仍是签过的 prevote / QC |
| 协议 | 锁阻止同高度两值被诚实节点双承诺 |
| 实现 | 崩溃后忘掉 lock = 实现破坏协议 |
| 部署 | 锁必须进 WAL / 磁盘（L4.4） |
| 经济 | 为 safety 牺牲一轮活性是设计，不是性能开关 |

**禁止假学习：** 「锁是性能优化。」「崩溃后忘掉 lock 只是掉线。」
**边界：** WAL 在 L4.4。锁被打破时，链上对象是 `DuplicateVoteEvidence`，不是钱包截图。见 [`../../tracks/economic/worked-example-evidence.md`](../../tracks/economic/worked-example-evidence.md)。飞行中的 last commit 不是证据身份：看见双签立刻用本机当前块打时间戳，会让双签变成 DoS，见 [CVE-2021-21271](../../tracks/failure-museum/cve-2021-21271.md)。Casper 的两票谓词与谁执行 slash：[`../../tracks/economic/worked-example-casper-slashing.md`](../../tracks/economic/worked-example-casper-slashing.md)。不 timely 的 prevote `nil` 是活性代价，不是解锁，见 [`../../tracks/consensus/worked-example-pbts.md`](../../tracks/consensus/worked-example-pbts.md)。超时强迫换轮，但不改锁定值；`timeout_commit` 更不是锁，见 [`../../tracks/consensus/worked-example-timeouts.md`](../../tracks/consensus/worked-example-timeouts.md)。
