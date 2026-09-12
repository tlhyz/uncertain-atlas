# 工作实例：BTC UTXO 仍在 Bitcoin，不是已经 wrap；k-deep 包含证明不是已经 commit

> **事实 / 推断 / 建议** 已分开。
> 对照：[Babylon 滤网](../../protocols/babylon/README.md)、[EigenLayer 滤网](../../protocols/eigenlayer/README.md)、[L7.3](../../courses/level-07-modular/L07-M03-shared-security.md)、[L3.1 最重链](../../courses/level-03-bitcoin/L03-M01-nakamoto-finality.md)、[证据 ≠ slash](worked-example-evidence.md)、[Casper 谓词](worked-example-casper-slashing.md)、[平行链共享安全](../finality/worked-example-backed-vs-available.md)。
> 主文献：Babylon 模块 [x/btcstaking README](https://github.com/babylonlabs-io/babylon/blob/main/x/btcstaking/README.md)、[staking-script.md](https://github.com/babylonlabs-io/babylon/blob/main/docs/staking-script.md)。资料层级是官方模块说明，不是冻结的 Bitcoin 共识规范。不写 19 节。
> 本页钉 **UTXO 仍在 Bitcoin ≠ 已经 wrap 到外链**、**k-deep 包含证明 ≠ 已经 CometBFT commit**、**看见解绑签名 ≠ 已经 k-deep**、**浅重组拿掉解绑交易 ≠ 已经恢复票权**、**契约委员会连署 ≠ Bitcoin 脚本已经单独能罚**。不抄 `k`、委员会人数、罚没比例、聪数、官网收益。

---

## 0. 先修

- [L3.1](../../courses/level-03-bitcoin/L03-M01-nakamoto-finality.md) k 确认
- [L7.3](../../courses/level-07-modular/L07-M03-shared-security.md) 共享安全
- [不变量 21](../../libraries/invariants/README.md) 证据上链 ≠ 已 slash
- [不变量 139](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见「BTC 质押」或看见包含证明已经绿，以为币已经 wrap 到外链，或以为 Bitcoin 最重链已经替租户做了 CometBFT commit，或以为解绑签名一出现、浅重组还能把票权要回来。

官方句（事实）：

- 模块 README：Bitcoin 持有人可以把 bitcoin 押给 Babylon 链和其他 PoS 链提供经济安全，**不必把 bitcoin 桥到别处**。
- staking-script：质押交易把一笔 BTC **锁在 Bitcoin 网络上的** Taproot 脚本。这不是把 UTXO 铸成外链包装币再质押。
- 质押输出只能走脚本路径。官方写密钥花费路径用 BIP341 NUMS 点关掉。本页不抄该点的十六进制。
- 三条脚本路径（官方）：时间锁（持有人签 + 相对锁高）；提前解绑（持有人签 + 契约委员会法定人数）；罚没（持有人签 + 最终性提供者钥 + 契约法定人数）。数字不抄。
- 契约委员会：官方写成 M-of-N 与持有人连署，用来强制按协议花。连署公布在 Babylon Genesis，是激活的前提。官方另写：委员会不能对持有人作恶，除了拒绝质押请求。这是额外的人集假设，不是「纯脚本自动罚」。
- 激活：把质押交易、包含证明、罚没交易、解绑交易送到 Babylon。契约模拟器先验再交预签名。EOI 路径可以先不带包含证明，等委员会签完再上 Bitcoin，再补 `MsgAddBTCDelegationInclusionProof`。
- `MsgCreateBTCDelegation` 与 `MsgAddBTCDelegationInclusionProof`：**强制 k-deep**（`BtcConfirmationDepth`）才给投票权。`k` 是部署参数，本页不抄。
- Bitcoin 侧的「已包含」仍是 Nakamoto 确认政策，不是 CometBFT 该高度 commit。
- 最终性提供者在 CometBFT **之上**再跑一轮最终性投票。票权表由本模块维护，给 `x/finality` 用。BTC 锁住不是租户块已经 commit。
- 提前解绑：持有人签解绑交易并送到 Bitcoin。模块看见这枚签名，**立刻**把委托当成已解绑。
- 普通（非 stake-expansion）解绑是 **intent-based**：持有人对质押输出的已签花费，就够 Babylon 当成已解绑。花费交易的包含证明只对已知 BTC 头做 Merkle 合法性检查，**不要求** k-deep。因此，小于 `BtcConfirmationDepth` 的 BTC 重组若把解绑交易从规范链拿掉，**不会**恢复该委托；意图一旦被看见，委托保持已解绑。
- 大重组恢复程序官方另有一页。本页不写怎样重组。stake-expansion 解绑是另一对象。

UTXO 仍在 Bitcoin、k-deep 才有票权、看见解绑意图、租户已经 commit，是不同对象。

---

## 2. 直觉（ELI15）

金库的箱子还在总行保险柜：UTXO 仍在 Bitcoin。  
柜员复印一张「这箱在第几层」的回执：包含证明。  
回执要等总行再盖几个章才算押金生效：k-deep。  
那不是分行已经把这笔账 commit。  
你先在解约书上签字：意图。分行立刻把你从投票名单划掉。  
总行那张解约交易如果被浅浅改写，名单**不会**把你加回去。

小朋友看见「BTC 质押」，以为币已经搬到外链，或以为 Bitcoin 已经替别人做了 BFT。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| Bitcoin 上的质押 UTXO | Taproot 锁在 Bitcoin 账本 | 已经 wrap；已经离开 Bitcoin 脚本 |
| 时间锁路径 | 持有人签 + 相对锁高 | 已经可立刻取回 |
| 解绑路径 | 持有人 + 契约法定人数 | 已经单独能罚；已经 k-deep |
| 罚没路径 | 持有人 + 最终性提供者 + 契约 | Bitcoin 脚本已经自动罚；Casper surround |
| 契约委员会 | 连署、可拒请求 | 「没有第三人」；Bitcoin 共识本身 |
| k-deep 包含证明 | 给投票权的激活条件 | 已经 CometBFT commit；已经租户最终 |
| EOI | 先在 Babylon 登记、后上 Bitcoin | 已经有票权 |
| 解绑意图 | 已签花费，模块立刻当已解绑 | 已经 k-deep；浅重组能恢复票权 |
| 最终性提供者票 | CometBFT 之上的最终性轮 | BTC 锁住 = 租户已经 commit |
| EigenLayer restake | 已为以太坊质押的 ETH/LST 再声明 | 本页的 Bitcoin UTXO |

---

## 4. 最小案例

用户把一枚 BTC UTXO 按官方脚本锁上。

1. UTXO 仍在 Bitcoin。不是已经 wrap。
2. 先交 EOI、还没有 k-deep 包含证明：还没有票权。
3. 包含证明过了 k-deep：模块给投票权。不是 Babylon / 租户已经 CometBFT commit。
4. 用户签了解绑交易。模块立刻当已解绑。不是已经等了 k 个 Bitcoin 块。
5. 小于 k 的 BTC 重组拿掉那笔解绑交易：官方写委托**保持**已解绑。不是票权已经回来。
6. 有人把「BTC 质押」写成 EigenLayer：那边押的是已经为以太坊质押的 ETH/LST，AVS 自己定义罚没。本页押的是 Bitcoin 脚本里的 UTXO。
7. 有人把「有包含证明」写成 Bitcoin 已经保证租户结算：房东最终 ≠ 租户应用正确。

「BTC 质押所以 Bitcoin 已经最终了你的链」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | Taproot / Schnorr / 官方点名的 EOTS。本页不证提取、不抄 NUMS 十六进制 |
| 协议 | 必须点名问的是 Bitcoin 锁、k-deep 票权、解绑意图，还是租户 commit |
| 实现 | 轻客户端头、vigilante 代交证明，是实现对象；两家必须同谓词 |
| 部署 | 契约委员会是额外人集；`k` 与法定人数是部署参数，不抄 |
| 经济 | 票权来自 Bitcoin 锁 + 模块表；浅重组不恢复已看见的解绑意图 |

**推断：** 产品句若只写「BTC 质押所以更安全」，读者会把 UTXO 还在 Bitcoin 听成租户已经 commit，或把解绑签名听成和激活同一把 k 尺。  
**建议：** 不确定第一版不要靠外链 BTC 当质押。若对照，必须点名锁在哪一条账本、哪一档确认给票权、解绑看的是意图还是 k-deep。不要抄 `k`。不要写怎样重组或提取一次性签。不要写 19 节。

---

## 6. 和另外几句不是同一句

1. **k 确认**（L3.1）：Bitcoin 自己的结算政策。本页用同一把尺给**票权**，解绑故意不用这把尺。
2. **证据 ≠ slash**（不变量 21）：ABCI 证据上链。本页是 Bitcoin 脚本路径 + 模块意图。
3. **Casper 两票谓词**（不变量 26）：surround / double。本页罚没路径要契约连署，不是信标谓词。
4. **平行链共享安全**（不变量 125）：押的是中继自己的质押。本页押的是 Bitcoin UTXO。
5. **EigenLayer restake**（滤网）：已为以太坊质押的 ETH/LST，AVS 自定罚没。本页不是那份抵押。
6. **leak ≠ slash**（不变量 130）：终局推迟。本页没有 inactivity leak。

不要把 `k`、委员会人数、罚没比例、聪数、官网收益抄进不确定常量。不要写怎样提取 EOTS、拼罚没见证或制造 BTC 重组。不编博物馆页。不写 19 节。产品页「无需第三人 / trustless」与模块里的契约委员会两句都留：营销句不是事实。大重组恢复与 stake-expansion 标成另一对象。

---

## 7. 「不确定」测试句（建议）

```text
UTXO 仍在 Bitcoin ≠ 已经 wrap / 已经离开脚本
k-deep 包含证明 ≠ 已经 CometBFT commit / 已经租户最终
EOI 已登记 ≠ 已经有票权
看见解绑签名 ≠ 已经 k-deep
浅重组拿掉解绑交易 ≠ 已经恢复票权
契约连署 ≠ Bitcoin 脚本已经单独能罚
BTC 锁住 ≠ 最终性提供者已经投过
```

语料：[C143](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「BTC 质押就是把币桥到外链。」「有包含证明就是租户已经最终。」「解绑和激活用同一把 k。」「浅重组能把票权要回来。」「没有第三人。」  
**边界：** 不讲 EOTS 提取、不填 `k` / 委员会人数。不把产品营销写成模块事实。不写 19 节。不写怎样重组。大重组恢复与 stake-expansion 另标。
