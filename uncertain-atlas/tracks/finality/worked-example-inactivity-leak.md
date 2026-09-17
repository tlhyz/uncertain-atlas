# 工作实例：终局卡住了，不等于已经停链，也不等于已经 slash

> **事实 / 推断 / 建议** 已分开。
> 对照：[三等确认](worked-example-head-vs-justified-vs-finalized.md)、[弱主观性](worked-example-weak-subjectivity.md)、[Casper 两票](../economic/worked-example-casper-slashing.md)、[停链面](../failure-museum/worked-example-halt-surfaces.md)、[L5.2](../../courses/level-05-ethereum/L05-M02-el-cl-finality.md)、[Ethereum 档案](../../protocols/ethereum/report.md)。
> 主文献：ethereum.org [Rewards and penalties](https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/)、[Attack and defense](https://ethereum.org/developers/docs/consensus-mechanisms/pos/attack-and-defense/)、[Gasper](https://ethereum.org/developers/docs/consensus-mechanisms/pos/gasper/)、[Proof-of-stake](https://ethereum.org/developers/docs/consensus-mechanisms/pos/)。
> 本页钉 **终局推迟 ≠ 高度已经停**、**inactivity leak ≠ slash**、**两边都 leak 到 finalized ≠ 协议已经选出唯一规范链**。不抄官方写的 epoch 个数、罚没天数、押金、美元、百分比里程碑。

---

## 0. 先修

- [L5.2](../../courses/level-05-ethereum/L05-M02-el-cl-finality.md) 头 / justified / finalized
- [不变量 127](../../libraries/invariants/README.md) 三等确认
- [不变量 26](../../libraries/invariants/README.md) 两票谓词与谁执行 slash
- [不变量 130](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见「好久没 finalized」，以为链已经停，或以为不投票的人已经被 slash，或以为 leak 跑完就自动只剩一条规范链。

官方句（事实）：

- Gasper 另有一条活性防线，叫 **inactivity leak**。共识层超过官方写的若干 epoch 还不能最终，就启动这个紧急协议。目标是**重新创造能最终的条件**，不是把高度停住。
- 最终需要总质押的三分之二对 source / target 检查点达成一致。官方：代表超过三分之一的验证者离线或交不出正确 attestation，就凑不齐这把超多数。
- Leak 把**不活跃**验证者的质押慢慢抽走，直到他们占不到总质押的三分之一，剩下还在投的人重新够三分之二。官方写：不活跃的池子无论多大，剩下活跃的人**终将**控制超过三分之二。
- Attack-and-defense 页把 leak 认的人写成两类：没 attestation，或 attestation **跟多数相反**。目的仍是让链再最终。同一页立刻补一句：持续不活跃**很贵，但这些人没有被 slash**。
- Rewards 页把 slash 写成另一条：同槽两块、包围、同块双投，才会强制退出并烧质押。Leak 抽的是不跟着多数走的余额，不是这三条可罚关系。
- 官方另写两类「两条链都最终」的故事，**不是 leak 本身**：约三分之一以上再加双投 / 计时，可能双最终，恢复要链下协调；约一半对半分叉时，**两边都会 leak，两边都会最终**，这时官方写只剩社会恢复。两边都 finalized 不是协议已经选出唯一规范链。
- Rewards 页记：Medalla 测试网曾启动 leak，后来终局回来。那是官方历史句，不是本图谱新馆藏。

终局推迟、头还在走、leak 在抽、slash 在烧、两边都最终、社会恢复，是不同对象。

---

## 2. 直觉（ELI15）

班委开会要三分之二到齐才能把上周课表归档。  
三分之一的人请假或不举手，归档停住。门口课表（头）还可以换。  
教务处开始扣请假人的学分，直到到场的人重新够三分之二：leak。扣学分不是开除学籍：slash 才是同槽贴两张黑板那种。  
若两边各开一个教室、两边都扣到能归档：两个档案室都盖了章。哪一间算学校，教务处自己选不了，要全校开会。

小朋友看见「好久没归档」，以为学校停课了，或以为请假的人已经被开除，或以为扣完学分就自动只剩一间教室。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| 终局推迟 | 凑不齐三分之二检查点升级 | 高度已经停；头已经不能摆 |
| Inactivity leak | 终局卡住时抽不跟多数走的质押，好让剩下的人再够三分之二 | slash；已经换了一套新集合；高度已停 |
| 不活跃 / 跟多数反着投 | leak 认的两类人 | 已经可罚的双投 / 包围 / 同槽两块 |
| Slash | 官方三条可罚关系；强制退出并烧质押 | leak；错过头票 |
| 双最终 | 两条分叉都能 finalized | leak 的日常结果；协议已经选出唯一链 |
| 约一半对半 + 两边 leak | 官方写两边都会最终 | 已经有唯一规范链 |
| 社会恢复 | 链下约定跟哪一条 | 协议对象已经替你选好 |
| Medalla 启动过 leak | 官方奖励页上的测试网历史句 | 本图谱新博物馆案 |

---

## 4. 最小案例

用户等 finalized，钱包头还在走。

1. 检查点升不上去。这是终局推迟。出块和头票仍可能继续。
2. 官方紧急协议启动：不举手、或举手跟多数反着的人，质押被慢慢抽。这是 leak。
3. 抽到他们占不到三分之一，剩下的人再给检查点升级。这是活性回来，不是「已经停过一次」。
4. 若有人把这写成 slash：官方明确写持续不活跃很贵，但**没有**被 slash。Slash 要能指出双投 / 包围 / 同槽两块。
5. 若出现两条都 finalized：官方写要社会恢复。不要写成 leak 已经替你选好唯一链。

「好久没最终所以停了」和「leak 过了所以已经唯一」都是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | leak 改的是有效余额，不是另一套签 |
| 协议 | 终局推迟、leak、slash、双最终、社会恢复必须分列 |
| 实现 | 客户端继续出块 / 选头，不等于 finalized 还在升 |
| 部署 | explorer 停在旧 finalized，不是高度已经停 |
| 经济 | 抽干是活性杠杆；不是已经执行了 slash 公式 |

**推断：** 产品句若只写「PoS 不会停」或「不投票就 slash」，读者会把终局推迟听成停链，把 leak 听成可罚关系。  
**建议：** 不确定第一版若用检查点最终，必须另写终局推迟时怎么办。不要抄官方 epoch 个数或美元当产品证明。不要把 leak 写成已经替代 slash，也不要把两边都最终写成协议已经收口。

---

## 6. 和另外几句不是同一句

1. **head ≠ justified ≠ finalized**（不变量 127）：三等确认。本页是终局卡住之后的活性路径，不是再解释三等。
2. **两票可罚**（不变量 26）：double / surround / 同槽头。本页是 leak **不是**这三条。
3. **停链不是一种事故**（不变量 84）：真停要点名路径。本页是看起来像停、其实是终局推迟。
4. **出块还在 ≠ 纪元已转**（不变量 110）：选举地板。本页是 Gasper 活性，不是 NPoS 冷冻。
5. **弱主观性**（不变量 24）：新节点信哪份检查点。双最终之后的社会恢复是亲戚，不是同一句。
6. **抽样委员会 2/3**（不变量 22）：Altair 样本。本页是全集质押被抽。
7. **NPoS 等权**（不变量 129）：超多数单位。本页是以太坊按总质押，不是人数。

不要把官方写的 epoch 个数、罚没天数、押金、美元、百分比里程碑抄进不确定常量。不要写怎样扣块、怎样对半、怎样双投造双最终。Medalla 只保留官方「启动过 leak、后来回来」一句，不编博物馆页。

---

## 7. 「不确定」测试句（建议）

```text
终局推迟 ≠ 高度已经停
头还在走 ≠ finalized 还在升
inactivity leak ≠ slash
没 attestation ≠ 已经可罚
跟多数反着投 ≠ 已经 surround
抽到剩下的人够三分之二 ≠ 已经换了一套新集合
两边都 leak 到 finalized ≠ 协议已经选出唯一规范链
双最终 ≠ leak 的日常结果
社会恢复 ≠ 协议对象已经替你选好
Medalla 启动过 leak ≠ 本图谱新馆藏
```

语料：[C134](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「好久没最终就是停链。」「不投票就是已经 slash。」「leak 跑完就自动只剩一条链。」「两边都 finalized 所以协议已经收口。」「这和选举地板 / 弱主观性是同一句话。」  
**边界：** 不讲 leak 公式、不填 epoch 个数、不抄罚金 / 美元。不写怎样做终局推迟或双最终。攻击面上的扣块 / 平衡 / 弹跳只点名「官方另有研究句」，不展开步骤。三等确认仍指 [head ≠ justified ≠ finalized](worked-example-head-vs-justified-vs-finalized.md)。可罚关系仍指 [Casper 两票](../economic/worked-example-casper-slashing.md)。
