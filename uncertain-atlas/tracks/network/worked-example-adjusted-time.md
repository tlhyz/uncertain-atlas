# 实例：本地钟被对等节点拧歪，真块变成「太未来」

> **事实 / 推断 / 建议** 已分开。
> 对照：[分区](../consensus/worked-example-partition.md)、[日蚀](worked-example-eclipse.md)、[CVE-2024-52912](../failure-museum/cve-2024-52912.md)、[PBTS ≠ MTP](../consensus/worked-example-pbts.md)。
> 主文献：[Bitcoin Core 披露](https://bitcoincore.org/en/2024/07/03/disclose-timestamp-overflow/)。

---

## 故事

阿比的全节点还连着主网邻居。签名、PoW、脚本都可以验。  
可是它用来判断「这个块是不是从太远的未来来的」的钟，已经被最先连上的对等节点带偏。规范链尖上的新块，在它看来全是未来票。它停在旧尖，钱包仍可能显示「已同步」。

日蚀：对手换了你看见的图。  
分区：两边诚实，帘子隔开。  
本页：图还在，规则还在，**判时间的尺子坏了**。

---

## 事实

- 共识可以写「块时间不得超出现在太多」。那是协议对象。
- 「现在」若等于 `系统钟 + 对等偏移`，偏移的算术与上限是**实现**。CVE-2024-52912：有符号溢出 + `abs64(INT64_MIN)` 绕过上限。
- 旧实现只把最先 200 个对等偏移算进调整时间——部署窗口，不是 MTP。

---

## 五层

| 层 | 本故事 |
|----|--------|
| 密码 | 新块的 PoW / 签名可以仍真 |
| 协议 | 「太未来则拒」的意图仍在 |
| 实现 | 偏移计算与 abs 不得绕过上限 |
| 部署 | 引导期的前 N 个邻居 |
| 经济 | 一台收款节点离开规范尖，不必买算力 |

---

## 对不确定（建议）

产品句「本节点拒绝该块」必须能点名是：共识规则、本节点钟、还是实现上限。缺这句，就和「链判定非法」糊了。  
调整钟也不是 PBTS timely 窗，更不是 BFT Time 中位数。四把尺见 [`../consensus/worked-example-pbts.md`](../consensus/worked-example-pbts.md)。  
MTP 在 Bitcoin 里还要再拆三把：太早、BIP113 locktime、太新，见 [`../consensus/worked-example-mtp.md`](../consensus/worked-example-mtp.md)。调整钟打的是太新那条实现路径，不是 MTP 公式。
