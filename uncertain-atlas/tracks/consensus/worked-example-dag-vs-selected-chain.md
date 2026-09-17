# 工作实例：进了 DAG，不等于已经在 selected chain 上，更不等于已经最终

> **事实 / 推断 / 建议** 已分开。
> 对照：[L3.8](../../courses/level-03-bitcoin/L03-M08-block-dag.md)、[Kaspa 档案](../../protocols/kaspa/report.md)、[Snow 抽样](worked-example-snow-sample-vs-qc.md)、[Bitcoin 最重链](../../courses/level-03-bitcoin/L03-M01-nakamoto-finality.md)。
> 主文献：Kaspa Wiki [Developers Knowledge Base](https://wiki.kaspa.org/en/developers-knowledge-base)、[Kaspa](https://wiki.kaspa.org/en/kaspa)。论文 / 归档 gitbook 不是本页现行对象。
> 本页钉 **并行块进 DAG ≠ 已经 orphan 扔掉**、**进了某个块 ≠ 已经在 selected chain**、**蓝 ≠ 已经最终**、**GHOSTDAG 全序 ≠ Avalanche 抽样**。不抄 BPS、DAA 窗长、45 分钟、k、官网确认秒数。

---

## 0. 先修

- [L3.1](../../courses/level-03-bitcoin/L03-M01-nakamoto-finality.md) 最重链
- [L3.8](../../courses/level-03-bitcoin/L03-M08-block-dag.md) 孤块与 DAG
- [不变量 131](../../libraries/invariants/README.md) 抽样 α ≠ QC
- [不变量 137](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见交易进了一个 Kaspa 块，或看见「也是 DAG」，以为这块已经进了规范历史，或以为和 Avalanche 抽样是同一把尺子，或以为并行块像 Bitcoin 那样已经作废。

官方句（事实）：

- Wiki：Kaspa 是实现 PHANTOM GHOSTDAG 的工作量证明。和单链不同，**并行长出来的块不被 orphan**，而是共存，再按共识排序。
- Wiki：双花靠**块被怎样排序**来防。DAG 被走成一条链，不跟前面冲突的交易才被收进。
- 开发者知识库：每个块都有一个由 GHOSTDAG 选出的 **selected parent**。
- `virtual` 是一个虚块，指向本节点当前所有 tip。它也有 selected parent，叫做 **selected tip**。
- 从 selected tip 顺着 selected parent 往下走，这条路叫 **selected chain**。它决定 DAG 上事件的顺序。链上的块（chain blocks）有特殊地位：节点递归接受它们的视角。
- 官方写：selected chain **可以改**（virtual 的视角变了），这就叫 reorg。宽 DAG 上小 reorg 常见。同页写 GHOSTDAG 的安全意味着链稳健，会在一个小后缀上稳定下来。本页不抄「很快」当产品秒数。
- 链块 `C` 的 **mergeset**：在 `C` 的过去里、但不在 `C` 的 selected parent 过去里的块；**包含** selected parent 自己。`C` 是 mergeset 里有效交易的 **accepting block**。
- mergeset 的 GHOSTDAG 序：按 **blue work** 升序，哈希字典序打破平局。
- 从 `C` 看，mergeset 里的 `B` 有两档分类：是不是 **blue**（官方：连接得好、对安全有贡献）；是不是在 `C` 的 DAA 窗里。Selected parent 按定义既是蓝，也在 DAA 窗里。
- 若 `C` **不是** chain block，它做的 coinbase / 自奖在 DAG 稳定之后不被当成有效，节点会丢掉。
- KIP 表另有 DagKnight、Crescendo、KIP-0015（selected parent 已接受交易承诺）。那是升级对象，不是本页已经切完。

进了某个块、进了 mergeset、被标蓝、留在 selected chain、已经稳定，是不同对象。

---

## 2. 直觉（ELI15）

工地上同时卸了好几车砖：DAG。  
工头指定「这车是主线父车」：selected parent。  
顺着主线父车往回走，才是今天的砌墙顺序单：selected chain。  
旁边卸下的车会被主线某车**合并**进来：mergeset。  
合并进来仍可能标成红，工钱算法不同。  
顺序单末尾几行还会改——卸到工地不是墙已经验收。

小朋友看见「进了一个块」或「也是 DAG」，以为已经最终，或以为这和问邻居是同一件事。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| 并行块共存 | 官方：不被 orphan，再排序 | 已经进规范历史；已经最终 |
| `virtual` | 指向本节点当前所有 tip 的虚块 | 全网已经同一 tip |
| selected parent | GHOSTDAG 为每块选的那个父 | 唯一物理父；Bitcoin 最重子 |
| selected chain | 从 selected tip 沿 selected parent 走回去 | 进了 DAG 的所有块；不可改的历史 |
| chain block | selected chain 上的块；别人递归接受它的视角 | 任意 DAG 块 |
| mergeset | `C` 的过去减去 selected parent 的过去 | 已经全部是蓝；已经最终 |
| accepting block | 链块 `C` 接收 mergeset 里有效交易 | 交易进了任意块就已经接受 |
| blue | 官方：连接得好、对安全有贡献 | 已经最终；QC |
| blue work 序 | mergeset 排序键 | Avalanche 抽样 α |
| 小 reorg | selected chain 可改 | 已经和 CometBFT 一样不可逆 |
| DagKnight / Crescendo | KIP 升级对象 | 本页现行 GHOSTDAG 已经切完 |

---

## 4. 最小案例

用户在 Kaspa 转一笔。

1. 某矿工把它打进块 B。B 进了 DAG。不是已经在 selected chain。
2. 后来链块 C 把 B 推进自己的 mergeset。C 才是这笔的 accepting block。不是 B 一出现就已经接受。
3. B 可能是蓝，也可能是红。红仍在 DAG 里。不是 Bitcoin 那种路边作废，也不是已经最终。
4. virtual 的 selected tip 一变，selected chain 末尾可以改。官方把这叫 reorg。
5. 有人把「DAG」写成 Avalanche：那边问邻居、数连续轮。本页按 blue work 抽 selected parent，没有样本 α。
6. 有人把「进块」写成 Bitcoin 最重链上的确认：Bitcoin 并行块常被 orphan。本页官方写并行块留下再排序。
7. 有人把 DagKnight 写成已经替换 GHOSTDAG：KIP 表在，不是本页现行对象。

「进了一个块所以已经最终」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | PoW + 交易签；本页不证 heavyhash |
| 协议 | 必须点名问的是 DAG 成员、mergeset、蓝，还是 selected chain |
| 实现 | 两实现必须同序；wiki 不是论文伪代码已经冻结 |
| 部署 | 宽 DAG 上小 reorg 常见；传播分裂会改本地 virtual |
| 经济 | 只有 chain block 的 coinbase 在稳定后仍有效；红块奖给合并者 |

**推断：** 产品句若只写「DAG 所以秒确认」，读者会把「进了某个块」听成 selected chain 已经锁死。  
**建议：** 不确定第一版不必上高块率 DAG。若对照，用户可见的「到了」必须点名是 DAG 成员还是 selected chain 前缀。不要抄 BPS。不要写怎样推倒 selected chain。

---

## 6. 和另外几句不是同一句

1. **最重链孤块**（L3.1）：并行块常扔掉。本页官方写留下再排序。
2. **抽样 α ≠ QC**（不变量 131）：Snow 问邻居。本页是 PoW DAG 上的 selected parent / blue work。
3. **官方顺序 ≠ 状态根**（不变量 136）：先定序再揭开。本页是块 DAG 怎么抽出那条序。
4. **Narwhal / 交易池 DAG**（L3.8）：mempool 图。本页是出块 DAG。
5. **processed ≠ finalized**（不变量 133）：Tower。本页没有 PoH。
6. **Doomslug ≠ BFT**（不变量 135）：头上两枚哈希。本页没有那两枚字段。

不要把 BPS、DAA 窗长、45 分钟、k、确认秒数、官网吞吐抄进不确定常量。不要写怎样制造宽 DAG reorg。不编博物馆页。论文着色伪代码与归档 gitbook 不是本页现行规范。DagKnight 不在本页展开。

---

## 7. 「不确定」测试句（建议）

```text
并行块进 DAG ≠ 已经 orphan 扔掉
进了某个块 ≠ 已经在 selected chain
进了 mergeset ≠ 已经是蓝 / 已经最终
蓝 ≠ QC / 已经不可逆
selected chain 可 reorg ≠ 已经和 commit 一样
accepting block 是合并它的链块 ≠ 出块当时已经接受
非 chain block 的 coinbase ≠ 稳定后仍有效
GHOSTDAG ≠ Avalanche 抽样
DagKnight 在 KIP 表 ≠ 现行已经切完
```

语料：[C141](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「进了一个块就是已经最终。」「DAG 所以无需顺序。」「和 Avalanche 都是 DAG 所以一样。」「并行块已经像 Bitcoin 那样作废。」「蓝就是 QC。」  
**边界：** 不讲着色伪代码、不填 BPS / k / 窗长。不把论文或归档页写成现行规范。不写怎样 reorg。DagKnight 另标。
