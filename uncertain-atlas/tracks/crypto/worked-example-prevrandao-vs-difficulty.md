# 工作实例：合并后的 DIFFICULTY 不是工作量

> **事实 / 推断 / 建议** 已分开。
> 对照：[L1.6](../../courses/level-01-crypto/L01-M06-randomness-and-determinism.md)、[L5.2](../../courses/level-05-ethereum/L05-M02-el-cl-finality.md)、[处理 ≠ 改头](../finality/worked-example-processed-vs-forkchoice.md)。
> 主文献：[EIP-4399](https://eips.ethereum.org/EIPS/eip-4399) Supplant DIFFICULTY opcode with PREVRANDAO。官方 EIP。不另写 19 节。
> 本页钉 **合并后的 DIFFICULTY ≠ 工作量**、**PREVRANDAO ≠ 本块刚掷的骰子**、**信标 RANDAO ≠ 应用级无偏随机**。不抄过渡块号 / 阈值 / 前瞻 epoch。不写怎样扣块或审查掷骰交易。

---

## 0. 先修

- [L1.6](../../courses/level-01-crypto/L01-M06-randomness-and-determinism.md) 三种随机与 `Apply` 禁骰
- [不变量 3](../../libraries/invariants/README.md) 确定性
- [不变量 149](../../libraries/invariants/README.md) 处理完一块 ≠ 已经改规范头
- [不变量 156](../../libraries/invariants/README.md) 父信标根 ≠ 当前头
- [不变量 157](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见合约还在调 `DIFFICULTY`，以为那还是挖矿有多难；或看见 `PREVRANDAO`，以为本块刚掷了一枚公平骰子；或把信标 RANDAO 听成应用已经拿到无偏随机。

官方句（事实）：

- EIP-4399：改现有 `DIFFICULTY` 指令的返回值语义，并把操作码改名为 `PREVRANDAO`。改名后返回值是信标链随机信标的输出。
- 与 EIP-3675 的过渡块绑死：过渡之后 `difficulty` 字段必须是 `0`，因为块上不再有工作量封印。`DIFFICULTY` 不再有旧语义，也没有一个「正确」的旧值可回。
- 过渡之后，头上的 `mixHash` 必须写成**上一块**信标后状态里最新的 RANDAO mix。`DIFFICULTY` 必须返回这个 `mixHash`。
- 字段宜改名 `prevRandao`，操作码宜改名 `PREVRANDAO`。故意复用旧字段、旧操作码，是为了少占字节、并让旧合约继续把该指令当随机源。
- 不用 `difficulty` 字段装随机，是为了躲开合并后隐匿的 fork choice / 总难度 bug。
- 安全节：PoS 下的 `PREVRANDAO` 和 PoW 下的 `BLOCKHASH` / `DIFFICULTY` **性质不同**。信标 RANDAO 让每个出块者对这一槽有 **1 bit** 影响力（可以不提议）。随后一次诚实揭示就拆掉这段偏向，即使前面连着偏过好几槽。
- 历史随机对任何去中心预言机都是 **100% 可预测**。未来随机只在有限范围内可预测。
- 规范**没有**把合并后的 `DIFFICULTY` 写成工作量，也没有把 `PREVRANDAO` 写成无偏应用骰子，也没有把 `mixHash` 写成本块刚掷的结果。

`difficulty` 字段、`PREVRANDAO` 指令、应用公平性，是三件事。

---

## 2. 直觉（ELI15）

旧路牌写着「坡度」。合并之后路还在，牌子被改成「昨天教室抽签结果」。  
看见旧字「坡度」，不是这座山还在比谁挖得猛。  
昨天的抽签结果能当今天的种子，不是这节课刚掷了公平骰子，也不是没人能少翻一张牌。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| 合并后的 `difficulty` 字段 | 必须为 0；不再有工作量封印 | 还在量挖矿难度；已经等于 RANDAO |
| `PREVRANDAO` / 旧 `DIFFICULTY` 指令 | 返回头上的 `mixHash`，即上一块信标后状态的 RANDAO mix | 本块刚掷的骰子；无偏应用随机；PoW 难度 |
| 信标 RANDAO | 共识层混合；出块者有 1 bit 影响力 | 已经是应用级公平；历史值不可预测 |

---

## 4. 最小案例

一条以太坊要对齐「合约里的随机从哪来」。

1. 合并后 `difficulty` 字段为 0。规范：这不是「难度变成 0 所以更好挖」，是工作量封印没了。
2. 合约仍调旧 `DIFFICULTY`。规范：返回的是上一块的 RANDAO mix，不是工作量。
3. 有人把这听成无偏骰子。规范：出块者有 1 bit 影响力；历史值 100% 可预测。
4. 有人把这听成父信标根（不变量 156）。那是块根，用来证共识状态。本页是 RANDAO mix。
5. 有人把这听成处理≠改头（不变量 149）。那是哪一次调用才改头。本页是头上一个字段换了语义。
6. 有人把这听成 `Apply` 读本地熵（不变量 3）。本页的值已经写进头，是块内输入；它仍不是公平骰子。

「看见 DIFFICULTY 所以还在比工作量 / 已经公平」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | RANDAO mix 是共识混合，不是 VRF 抽签，也不是主机 RNG |
| 协议 | 必须点名问的是工作量字段、上一块 mix，还是应用公平 |
| 实现 | 旧操作码号还在；语义已经换 |
| 部署 | 与 EIP-3675 过渡块绑死，不是另选一个槽号 |
| 经济 | 1 bit 影响力有机会成本；不是「免费所以无偏」 |

**推断：** 产品句若只写「链上随机」，读者会把旧坡度牌听成公平骰子。  
**建议：** 第一版可以不把共识随机暴露进执行 VM。若暴露，必须写清问的是工作量、上一块 mix 还是应用公平，并写清历史值可预测、提议者有 1 bit 影响力。不要抄阈值或前瞻 epoch。不要发明「PREVRANDAO = 无偏」。

---

## 6. 和另外几句不是同一句

1. **父根 ≠ 头**（不变量 156）：头上另一份信标累加器。本页是 RANDAO mix。
2. **处理 ≠ 改头**（不变量 149）：哪一次调用才改规范头。本页是字段语义。
3. **确定性**（不变量 3）：`Apply` 禁本地熵。本页的值已经进头。
4. **DKG / 链上信标**（不变量 93）：失败裁决要落盘。本页不是 Sui DKG。
5. **VRF 抽中 ≠ 已认证**（不变量 134）：抽签委员会。本页不是 Algorand。

不要抄过渡阈值 / 字段下标 / 前瞻 epoch / 漏块率。不要写怎样扣块、怎样审查掷骰交易、怎样叠 1 bit。不编博物馆页。不另写 19 节。RANDAO 揭示公式、应用 commit-reveal、`BLOCKHASH` 当随机源、EIP-2935 标成另一对象。

---

## 7. 「不确定」测试句（建议）

```text
合并后的 difficulty 字段 ≠ 工作量
PREVRANDAO ≠ 本块刚掷的骰子
信标 RANDAO ≠ 应用级无偏随机
历史 mix ≠ 不可预测
DIFFICULTY 指令还在 ≠ 语义没换
```

语料：[C161](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「DIFFICULTY 还是工作量。」「PREVRANDAO = 公平骰子。」「mixHash 是本块刚掷的。」「链上随机 = 无偏。」  
**边界：** 不讲 RANDAO 揭示公式。不抄阈值或前瞻。不另写 19 节。不写怎样扣块或审查掷骰。父信标根见 **C160**。DKG / VRF 另标。
