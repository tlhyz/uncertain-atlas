# 工作实例：最终确定 ≠ 可以从创世安全跟上

> **事实 / 推断 / 建议** 已分开。
> 对照：[L5.2](../../courses/level-05-ethereum/L05-M02-el-cl-finality.md)、[CometBFT 信任期](../light-clients/worked-example-bft-skip.md)、[phase0 weak-subjectivity.md](https://github.com/ethereum/consensus-specs/blob/master/specs/phase0/weak-subjectivity.md)。
> 规范文件自己写：**仍是 work-in-progress**。本页只钉它已经写出的对象，不把 2014 博客当定义。

---

## 0. 先修

- [L5.2 三种「到了」](../../courses/level-05-ethereum/L05-M02-el-cl-finality.md)
- [L4.5 集合变更](../../courses/level-04-bft/L04-M05-validator-set.md)
- [不变式 20](../../libraries/invariants/README.md#20-bft-轻客户端重叠旧集合)

---

## 1. 核心问题

阿比买了一台新电脑。他说：「这是 PoS，已经 finalized，我从创世重放，和一直在线的人一样安全。」

在 Bitcoin 上，这句话的主要对手是算力与日蚀。  
在 CometBFT / Ethereum PoS 上，还有另一句：验证者会**退出、解绑、把旧钥匙卖掉**。你若从太旧的检查点往前走，路上的「2/3」可能已经不是现在还押着钱的人。

---

## 2. 直觉（ELI15）

班委每学期换人。学期结束后，旧班委把印章卖给校外的人。  
你如果拿着三年前的课表来验「谁有权盖章」，旧班委可以给你盖一套假课表。现在的班委罚不到已经离校的人。

弱主观性：新来的人必须先拿到一份**足够新**的、自己愿意信的课表（检查点），再往下跟。  
「足够新」不是口号，是用退出速度算出来的一段 epoch。

---

## 3. 正式对象（规范事实）

来自 `specs/phase0/weak-subjectivity.md`（文件声明仍可能大改）和 `specs/phase0/beacon-chain.md`。

| 对象 | 规范怎么写 | 它不是 |
|------|------------|--------|
| Weak Subjectivity Checkpoint | **任何** `Checkpoint` 都能当；由提供者分发、用户下载、或打进客户端 | 密码学免费的「创世等价物」 |
| Weak Subjectivity Period | 必须落在这段**最近 epoch** 里，才能保证：期初接管验证者集合的攻击者，若再最终确定一个冲突检查点，至少被罚到一个下限 | 固定「N 天」；也不是 Casper 的 finalized 本身 |
| `SAFETY_DECAY` | 配置常量 **10**。攻击者利用该期时，安全边际至少 `1/3 - SAFETY_DECAY/100` | 「还有整整 1/3」 |
| 周期怎么算 | `compute_weak_subjectivity_period(state)`：从 `MIN_VALIDATOR_WITHDRAWABILITY_DELAY` 起，再加 churn / 充值上限推出来的 epoch | 一张与人数无关的永恒表 |
| 解绑下限 | phase0：`MIN_VALIDATOR_WITHDRAWABILITY_DELAY = Epoch(2**8)` = **256** | 整个 WS 周期（周期 ≥ 256，通常更长） |
| 同步纪律 | 用户输入 `block_root:epoch`。对不上 canonical 路径 → **致命、不可恢复**，退出进程 | 黄条警告仍继续跟链 |
| 是否过期 | `is_within_weak_subjectivity_period`：`current_epoch <= ws_state_epoch + ws_period` | 客户端「我觉得还行」 |

**事实：** `Distributing Weak Subjectivity Checkpoints` 一节写着 **This section will be updated soon.** 检查点**怎么发到用户手里**，规范没有写完。那是部署 / 社会对象。

**事实：** 规范给了一张「假设平均余额 + 假设人数 → 周期 epoch」的参考表，并指向外部 gist。**禁止**把表里的人数抄成「现在的以太坊」，也禁止把表里的 epoch 换成「多少天」。

**事实：** 公式吃当时规范的 `MAX_EFFECTIVE_BALANCE`、churn 与 `MAX_DEPOSITS`。phase0 有效余额上限是 32 ETH；**后续分叉改过这个上限**。本页不重算现行周期，也不把 32 当永恒。

---

## 4. 和另外两句「信一个起点」的对照

| | Bitcoin 全节点 | CometBFT 轻客户端 | Ethereum WS 同步 |
|--|----------------|-------------------|------------------|
| 起点 | 创世（检查点是社会加速，不是协议必选项） | 用户负责的 trusted header + 集合 | 用户/客户端提供的 `Checkpoint` |
| 「太旧」的含义 | 主要是重放成本与日蚀 | `now - trusted.Time ≥ trustingPeriod`（且须 `< unbondingPeriod`） | `current_epoch > ws_epoch + ws_period` |
| 旧集合的经济牙 | 算力 | 解绑前还能罚 | 退出 + 256 epoch 下限 + churn 换血 |
| 对不上起点 | 你跟了另一条最重链（自己能看见） | `NOT_ENOUGH_TRUST` / 拒绝 | 规范要客户端 **退出** |
| 能得出的句子 | 「我从创世（或我接受的检查点）重放了规则」 | 「跳跃仍钉在信任期内的旧下一集合」 | 「我的同步路径经过这份未过期检查点」 |
| 得不出的句子 | — | 「新委员会自己的 2/3」 | 「finalized 所以从创世跟和一直在线一样」 |

Altair 同步委员会轻客户端是第三种亲戚：它的 bootstrap 也是一份社会/部署起点，而且分母是 512 抽样，见 [抽样精读](../light-clients/worked-example-sync-committee.md)。不要把 WS 检查点、抽样委员会、CometBFT `NextValidators` 写成一个词。

---

## 5. 攻击者

| 攻击 | 机制 | 规范能要求的 | 规范写不完的 |
|------|------|--------------|--------------|
| 卖旧钥匙 | 验证者退出、过了可取款延迟，把钥卖给攻击者 | 周期公式按 churn 把「换血」算进去 | 用户拿了一份过期检查点仍点「同步」 |
| 假检查点 | 提供者给一条从未 canonical 的根 | 对不上路径则退出 | 用户信错提供者（分发节未写完） |
| 把 finalized 当创世安全 | 钱包文案 | — | 部署层把三种「到了」糊成一句 |
| 把参考表当现状 | 抄 32768 / 2241 epoch | 表上写的是假设余额与人数 | 现行 N、现行 MAX_EB |

---

## 6. 五层

| 层 | 本页能说的 | 不能说的 |
|----|------------|----------|
| 密码学 | 签本身不告诉你检查点新不新 | 「BLS 所以没有弱主观性」 |
| 协议 | 周期函数、256 epoch 下限、`SAFETY_DECAY=10`、对不上则退出 | 现行周期是多少 epoch |
| 实现 | 客户端是否真做 `is_within_weak_subjectivity_period` | 没读实现就写「都检查了」 |
| 部署 | 检查点从哪来；文件写明分发节未完成 | 某客户端内置检查点列表当规范 |
| 经济 | 牙在解绑 / 罚没；过期后旧集合可能已无抵押 | 把参考表人数当现网 |

---

## 7. 对不确定的意义（建议）

- 若默认角色是全节点且从创世复算：弱主观性不是第一版的主产品句。仍要在威胁模型里写：「长期离线后再同步，不允许只信一份过期检查点。」
- 若提供检查点同步或轻客户端：必须同时写 **信任对象**（不变量 22）和 **新鲜度**（本期不变量 24）。`trustingPeriod` 或 WS period 必须短于（或由）解绑/取款延迟约束。
- 检查点分发不要假装是协议对象。写进部署假设。
- 不要用「PoS 已最终」代替「从创世可客观重放」。

---

## 8. 禁句

- 「PoS finalized，所以从创世同步和一直在线一样」
- 「弱主观性周期是 X 天」（把 epoch 换算当规范）
- 把规范参考表里的验证者人数 / 周期抄成现网事实
- 「检查点由协议自动分发」（分发节未写完）
- 「弱主观性 = Altair 同步委员会 = CometBFT 信任期」（三个对象）
