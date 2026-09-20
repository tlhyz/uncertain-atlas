# 工作实例：coinbase 第一项写了高度不是头上已经有高度字段

> **事实 / 推断 / 建议** 已分开。
> 对照：[L3.1](../../courses/level-03-bitcoin/L03-M01-nakamoto-finality.md)、[进块 ≠ 能花](../economic/worked-example-coinbase-vs-mature.md)、[置位 ≠ 已激活](worked-example-versionbit-vs-active.md)、[策略 ≠ 共识](../mempool/worked-example-policy-vs-consensus.md)。
> 主文献：[BIP-34](https://github.com/bitcoin/bips/blob/master/bip-0034.mediawiki) Block v2, Height in Coinbase。官方 BIP。共识层软分叉。不另写 19 节。
> 本页钉 **coinbase 第一项写了高度 ≠ 头上已经有高度字段**、**块 version 加大 ≠ 已经按 BIP-9 位向量激活**、**交易 version 更大当非标准 ≠ 共识已经禁止**、**写了高度 ≠ coinbase 已经能花**、**BIP-34 ≠ BIP-9 ≠ BIP-66 那条新规则**。不抄激活票数 / 版本号常数 / 编码宽度 / 例高度。不写怎样造不带头高度的 coinbase，也不写怎样靠重复 coinbase 撞身份。

---

## 0. 先修

- [L3.1](../../courses/level-03-bitcoin/L03-M01-nakamoto-finality.md) 块与 coinbase
- [不变量 163](../../libraries/invariants/README.md) 进块 ≠ 能花
- [不变量 171](../../libraries/invariants/README.md) 版本位 ≠ 已激活
- [不变量 144](../../libraries/invariants/README.md) 策略 ≠ 共识
- [不变量 173](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见块头，以为高度已经写在头上；或看见块 version 从 1 加成 2，以为已经是 BIP-9 那种位向量激活；或看见 coinbase 里推了高度，以为这笔奖励已经能花。

官方句（事实）：

- BIP-34：块和交易都是带版本的二进制结构。本页给它们一条升级路径。
- 新出的 coinbase **第一项**写上本块高度；块 version 加大。高度是这条链上的高度，创世为 0。编码是最短序列化脚本数。
- 动机有两句：全网一起同意升级二进制结构和规则；并**强制唯一**、帮助验证还没接上的块。
- 交易 version 比 1 大，官方 Satoshi 客户端不当标准：不挖、不转发。这是策略，不是「共识已经禁止更大的交易版本」。
- 激活走整数版本门槛：够数之后，不合格的新 version 块要拒；再够数，旧 version 块也拒。不要把这套门槛听成 BIP-9 的四态。
- 规范**没有**把头写成已经带高度字段，也没有把加大 version 写成已经是位向量，也没有把写了高度写成已经能花。

头、coinbase 里的高度、奖励能不能花，是三件事。

---

## 2. 直觉（ELI15）

门牌钉在信封里，门框上没写楼层。  
换一批更大号的信封，不是已经改用举手表决。  
信封里写了楼层，不是里面的钱已经能花。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| 头 | 工作量、时间、Merkle 根等 | 已经带高度字段 |
| coinbase 高度 | 花费脚本第一项写下的本块高度 | 头上已经有；已经能花 |
| 整数 version | 一次滚一条软分叉 | BIP-9 位向量；已经锁定/激活四态 |
| 交易 version 非标准 | 本客户端不挖不转发 | 共识已经禁止 |

---

## 4. 最小案例

一条 Bitcoin 要对齐「这一口气高度写在哪」。

1. 只看见块头。规范：高度写在 coinbase 第一项。不是头上已经有高度字段。
2. 块 version 加大。规范：整数升级路径。不是已经按 BIP-9 位向量激活。
3. 交易 version 比 1 大。规范：当时当非标准。不是共识已经禁止。
4. coinbase 写了高度。规范：为了唯一、为了没接上的块。不是已经能花（不变量 163）。
5. 有人把这听成 BIP-9（不变量 171）。9 是位向量四态。本页是整数 version 一次一条。
6. 有人把这听成 BIP-66（不变量 172）。66 只是后来复用这套整数开关的一条规则。本页是高度本身。
7. 有人把这听成策略大类（不变量 144）。本页的「交易 version 非标准」是其中一盏灯，不是整页已经是策略。

「看见头所以高度已在头上 / version 大了所以已经是 9 / 写了高度所以已经能花」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | 无新原语 |
| 协议 | 必须点名问的是头、coinbase 高度，还是奖励年龄 |
| 实现 | 两家必须同一套：第一项是本块高度；创世为 0 |
| 部署 | 整数 version 门槛，不是位向量四态 |
| 经济 | 写了高度不是已经能花 |

**推断：** 产品句若只写「块有版本、coinbase 有高度」，读者会把头听成已经带楼层，或把写了高度听成已经能花。  
**建议：** 第一版若块头不带高度，必须写清高度承诺在哪。可以跳过「看见头就已经有高度字段」。173 coinbase height vs header bundled unbundling 完成（1542 item 1 / 1543 item 2 / 1544 item 3）；精读 [`worked-example-cbht-nothdr-vs-bundled.md`](worked-example-cbht-nothdr-vs-bundled.md)（不变量 1542 item 1）、[`worked-example-cbht-notv9-vs-bundled.md`](worked-example-cbht-notv9-vs-bundled.md)（不变量 1543 item 2）、[`worked-example-cbht-notmat-vs-bundled.md`](worked-example-cbht-notmat-vs-bundled.md)（不变量 1544 item 3）。不要发明「看见头 = 高度已在头上」。不要抄票数。不要把整数 version 写成 BIP-9。

---

## 6. 和另外几句不是同一句

1. **进块 ≠ 能花**（不变量 163）：成熟窗。本页是高度写在哪。
2. **置位 ≠ 已激活**（不变量 171）：位向量四态。本页是整数 version 一次一条。
3. **验过 ≠ 已是 DER**（不变量 172）：签名编码。66 只复用本页这种开关。
4. **策略 ≠ 共识**（不变量 144）：本页的交易 version 非标准是策略灯，高度入 coinbase 是共识灯。
5. **地址 ≠ 已有输出**（不变量 174）：收款写法。本页是高度写在哪。

不要抄激活票数 / 版本号常数 / 编码宽度 / 例高度 / 最后一块旧 version 的编号。不要写怎样造不带头高度的 coinbase，或怎样靠重复 coinbase 撞身份。不编博物馆页。不另写 19 节。BIP-9 位向量、BIP-66 编码谓词、挖矿模板字段是另一对象。

---

## 7. 「不确定」测试句（建议）

```text
coinbase 第一项写了高度 ≠ 头上已经有高度字段
块 version 加大 ≠ 已经按 BIP-9 位向量激活
交易 version 更大当非标准 ≠ 共识已经禁止
写了高度 ≠ coinbase 已经能花
BIP-34 ≠ BIP-9 ≠ BIP-66 那条新规则
```

语料：[C177](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「看见头 = 高度已在头上。」「version 加大 = 已经是 9。」「交易 version 大 = 共识已经禁止。」「写了高度 = 已经能花。」「34 = 9。」「34 = 66。」  
**边界：** 不抄票数。不另写 19 节。不写怎样造无高度 coinbase。成熟见 **C167**。激活见 **C175**。
