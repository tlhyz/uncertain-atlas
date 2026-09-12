# L5.2 执行层、共识层、三种「到了」

优先级：必学  
先修：L5.1，L4.3（知道 BFT 锁与 commit），L3.1（知道概率最终）

---

## A. 先修知识

合并之后，用户仍说「以太坊」。内部是两套软件：执行层算状态，共识层选头并给最终性。  
CometBFT：一个高度一张 commit，语义硬。Bitcoin：确认数是概率。Ethereum 夹在中间，而且多了一个「头」和「最终」的缝。

---

## B. 核心问题

**钱包上的绿勾，指的是执行算完、当前头、被证明正当，还是被最终敲定？这四者可以分开失败吗？**

---

## C. 直觉（ELI15）

一条流水线：

1. 车间把零件装配好（执行：这笔交易改了哪些余额）。
2. 班长把今天的清单钉在门口（共识：这是当前头）。
3. 教务处盖「本周课表已锁定」（最终性：再改要破坏明确规则并通常伴随惩罚）。

你若只看门口清单，明天可能换一张。  
你若把「装配完成」当成「教务处已盖章」，会过早发货。

---

## D. 正式定义

**执行层（EL）**

输入：父状态、交易列表、块环境（号、时间戳等规范字段）。  
输出：新状态根、收据根、日志。  
它**不**单独决定这条链跟谁。处理完一块不是已经改规范头。精读：[`../../tracks/finality/worked-example-processed-vs-forkchoice.md`](../../tracks/finality/worked-example-processed-vs-forkchoice.md)（不变量 149）。看见头里的请求承诺不是已经由共识层处理完。请求不是已经有权单独促成动作。精读：[`../../tracks/finality/worked-example-request-vs-action.md`](../../tracks/finality/worked-example-request-vs-action.md)（不变量 192）。看见执行层退出请求不是已经退出。进了本块请求名单不是已经由共识层办完。精读：[`../../tracks/economic/worked-example-el-exit-vs-withdrawal.md`](../../tracks/economic/worked-example-el-exit-vs-withdrawal.md)（不变量 193）。看见执行层存款日志不是已经由共识层办完。看见存款交易不是已经进了本块请求名单。精读：[`../../tracks/economic/worked-example-el-deposit-vs-eth1data.md`](../../tracks/economic/worked-example-el-deposit-vs-eth1data.md)（不变量 194）。看见合并请求不是已经并成一把。抬高有效余额上限不是已经取消最低激活额。精读：[`../../tracks/economic/worked-example-maxeb-vs-minact.md`](../../tracks/economic/worked-example-maxeb-vs-minact.md)（不变量 196）。看见状态里的历史执行哈希不是已经是 BLOCKHASH。系统写入父哈希不是已经填满窗口。精读：[`../../tracks/light-clients/worked-example-history-hash-vs-blockhash.md`](../../tracks/light-clients/worked-example-history-hash-vs-blockhash.md)（不变量 195）。

**共识层（CL）**

验证者质押、按 slot 提议、发 attestation。  
委员会下标被挪出签名消息不是已经没有委员会。AttestationData.index 写成零不是已经删掉该字段。分叉后第一块可以没有证明不是已经没有 LMD 票。精读：[`../../tracks/finality/worked-example-committee-index-vs-signed.md`](../../tracks/finality/worked-example-committee-index-vs-signed.md)（不变量 198）。
合并后共识属 Gasper 家族：**LMD-GHOST 选头** + **Casper FFG 做最终性**（事实：规范名称与结构；细节以共识规范为准）。

三种对象必须分开：

| 对象 | 含义 | 不是 |
|---|---|---|
| head | fork choice 此刻跟随的块 | 不可逆 |
| justified | FFG 给出的中间检查点 | 与 CometBFT commit 同一语义 |
| finalized | 更强的检查点；诚实多数下不应再回滚 | 「用户已经看见余额」 |

**事实：** 不是每个 slot 都像 Tendermint 那样「本高度已 commit」。头可以摆。  
**事实：** 最终性仍依赖质押与惩罚的经济/协议假设；另有弱主观性：长期离线节点需一个近期可信状态才能安全跟上（PoS 长程议题，数学后置）。  
**建议：** 结算产品若要对标「不确定」的最终语义，应钉 finalized（或自己的 BFT commit），不要钉 head。  
精读：[`../../tracks/finality/worked-example-head-vs-justified-vs-finalized.md`](../../tracks/finality/worked-example-head-vs-justified-vs-finalized.md)（不变量 127）。justified 不是已经不可逆。JSON-RPC `latest` / `safe` / `finalized` 不是同一标签；官方没有把 `safe` 写成 justified。

---

## E. 最小案例

slot N：块 A 是 head，钱包显示到账。  
slot N+k：fork choice 改跟 B，A 不在 canonical。执行结果在 A 上「发生过」，在 B 上可能没有。  
更晚：某检查点 finalized。此时再回滚，攻击者要破坏最终性规则（通常伴随可证明的slash 条件——以规范为准）。

用户在 head 发货 = 用 Nakamoto 式确认习惯套在 PoS 头上。

---

## F. 真实项目

Ethereum 合并后主网。PBS 之后，提议者可能不自己选交易（5.4）。  
对照：CometBFT 一高度一 commit；Bitcoin 只有确认深度。

---

## G. 源码入口

预告：

1. 共识规范：fork choice、justification、finalization。
2. 执行引擎 API：共识层叫执行层「请对此载荷出状态根」。
3. 客户端把「head 事件」和「finalized 事件」分成两条流。
4. 执行载荷里的提款列表：系统操作，不是用户交易。精读：[`../../tracks/economic/worked-example-withdrawal-vs-tx.md`](../../tracks/economic/worked-example-withdrawal-vs-tx.md)（不变量 154）。
5. 执行头里的父信标根：不是当前信标头，也不是已经 finalized。精读：[`../../tracks/light-clients/worked-example-parent-root-vs-head.md`](../../tracks/light-clients/worked-example-parent-root-vs-head.md)（不变量 156）。
6. 合并后旧 `DIFFICULTY` 指令：返回上一块 RANDAO mix，不是工作量，也不是无偏骰子。精读：[`../../tracks/crypto/worked-example-prevrandao-vs-difficulty.md`](../../tracks/crypto/worked-example-prevrandao-vs-difficulty.md)（不变量 157）。

---

## H. 攻击者模型

- 专打「只订阅 head」的交易所。
- 审查发生在构建者/中继，验证者人数看起来很多（部署/经济）。
- 最终性延迟：不足以最终，但足以让用户以为「PoS 所以秒到」。
- 弱主观性：给新节点一个假的旧检查点（社会/部署）。

---

## I. 代价

拆 EL/CL：可以换执行客户端、换共识客户端，升级路径更活。  
代价：两套网络、两套时钟、API 契约；「到了」必须写四次（执行、头、正当、最终）。

---

## J. 对「不确定」的意义

**可以参考** 执行与共识拆开（和 ABCI 是亲戚，不是同一实现）。  
**不建议** 第一版同时卖三种确认等级给用户。选一种结算语义，写进产品句，和协议对象对齐。  
后量子投票变大，打的是 CL 的 attestation 流量，不是 EVM 操作码列表。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | 验证者签 attestation；弱主观性是同步假设，不是签算法 |
| 协议 | head ≠ justified ≠ finalized；处理完一块 ≠ 已经改规范头；提款操作 ≠ 用户交易；父信标根 ≠ 当前头；PREVRANDAO ≠ 工作量 |
| 实现 | EL 根必须被 CL 承诺；两层客户端对齐 |
| 部署 | 出块间隔是参数，不是永恒 |
| 经济 | 罚没支撑最终性假设；不是「秒最终」口号 |

**禁止假学习：** 「PoS 所以秒最终。」「出块了 = finalized。」「justified 就是不可逆。」「`safe` 就是 finalized。」「和 Tendermint 一样一槽一 commit。」「好久没最终就是停链。」「不投票就是已经 slash。」「执行层刚跑完 / Engine API `VALID` = 已经改规范头。」「事件里的 head = 已经 finalized。」「信标提款 = 用户转账。」「出队 = 执行账户已到。」「EVM 能读信标 = 当前头。」「合约里的根 = 已经 finalized。」「DIFFICULTY 还是工作量。」「PREVRANDAO = 公平骰子。」「头上有请求承诺 = 共识层已经处理完。」「看见类型字节 = 已经解开载荷。」「7685 = 4895。」「看见执行层退出请求 = 已经退出。」「进了本块名单 = 已经办完。」「付了费进队 = 已经出队。」「7002 = 4895 / 7685。」「看见存款交易 / 日志 = 已经是验证者。」「旧投票有了新字段 = 已经关掉。」「6110 = 7685 / 7002。」「看见合并请求 = 已经并成一把。」「抬高上限 = 已经取消最低激活额。」「7251 = 7002。」「状态里能读哈希 = 已经改了 BLOCKHASH。」「2935 = 4788。」「委员会下标挪出签名 = 已经没有委员会。」「index 写成零 = 已经删字段。」「分叉后第一块没有证明 = 已经没有 LMD。」「7549 = 已经改了执行层。」「7549 = 同步委员会。」
**边界：** 不写当前 slot 秒数当永恒；不证弱主观性数学、不填现行 WS 周期。精读：[`../../tracks/finality/worked-example-head-vs-justified-vs-finalized.md`](../../tracks/finality/worked-example-head-vs-justified-vs-finalized.md)（不变量 127）；[`../../tracks/finality/worked-example-weak-subjectivity.md`](../../tracks/finality/worked-example-weak-subjectivity.md)。终局推迟 ≠ 停链，leak ≠ slash：[`../../tracks/finality/worked-example-inactivity-leak.md`](../../tracks/finality/worked-example-inactivity-leak.md)（不变量 130）。处理完一块 ≠ 已经改规范头：[`../../tracks/finality/worked-example-processed-vs-forkchoice.md`](../../tracks/finality/worked-example-processed-vs-forkchoice.md)（不变量 149）。看见头里的请求承诺 ≠ 已经由共识层处理完：[`../../tracks/finality/worked-example-request-vs-action.md`](../../tracks/finality/worked-example-request-vs-action.md)（不变量 192）。看见执行层退出请求 ≠ 已经退出：[`../../tracks/economic/worked-example-el-exit-vs-withdrawal.md`](../../tracks/economic/worked-example-el-exit-vs-withdrawal.md)（不变量 193）。看见执行层存款日志 ≠ 已经由共识层办完：[`../../tracks/economic/worked-example-el-deposit-vs-eth1data.md`](../../tracks/economic/worked-example-el-deposit-vs-eth1data.md)（不变量 194）。看见合并请求 ≠ 已经并成一把：[`../../tracks/economic/worked-example-maxeb-vs-minact.md`](../../tracks/economic/worked-example-maxeb-vs-minact.md)（不变量 196）。委员会下标被挪出签名 ≠ 已经没有委员会：[`../../tracks/finality/worked-example-committee-index-vs-signed.md`](../../tracks/finality/worked-example-committee-index-vs-signed.md)（不变量 198）。看见状态里的历史执行哈希 ≠ 已经是 BLOCKHASH：[`../../tracks/light-clients/worked-example-history-hash-vs-blockhash.md`](../../tracks/light-clients/worked-example-history-hash-vs-blockhash.md)（不变量 195）。提款操作 ≠ 用户交易：[`../../tracks/economic/worked-example-withdrawal-vs-tx.md`](../../tracks/economic/worked-example-withdrawal-vs-tx.md)（不变量 154）。父信标根 ≠ 当前头：[`../../tracks/light-clients/worked-example-parent-root-vs-head.md`](../../tracks/light-clients/worked-example-parent-root-vs-head.md)（不变量 156）。PREVRANDAO ≠ 工作量 / 无偏骰子：[`../../tracks/crypto/worked-example-prevrandao-vs-difficulty.md`](../../tracks/crypto/worked-example-prevrandao-vs-difficulty.md)（不变量 157）。attestation 与 proposer 的 `DomainType` 见 [`../../tracks/consensus/worked-example-vote-signbytes.md`](../../tracks/consensus/worked-example-vote-signbytes.md)；不是 EIP-712。Altair 同步委员会轻客户端：[`../../tracks/light-clients/worked-example-sync-committee.md`](../../tracks/light-clients/worked-example-sync-committee.md)。可罚关系与谁执行 slash：[`../../tracks/economic/worked-example-casper-slashing.md`](../../tracks/economic/worked-example-casper-slashing.md)。不抄罚金数字、epoch 个数、美元。不抄过渡总难度。不写怎样发假 forkchoice。不抄每块提款条数。不写怎样往载荷里塞假提款。不抄环长。不写怎样塞假父根。不抄 PREVRANDAO 阈值或前瞻 epoch。不写怎样扣块。
