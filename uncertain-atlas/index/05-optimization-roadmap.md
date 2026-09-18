# 优化路线图入口

读 [`../ROADMAP.md`](../ROADMAP.md) 获取：

1. **极大目标** — 可验证的全球架构图谱 + 不确定设计参考库  
2. **架构评估** — 已完善 vs 需调整  
3. **Phase 0–3 小目标** — 带 ID，可勾选  
4. **canonical 分支说明**

---

## 当前 canonical 分支（建议）

```
cursor/uncertain-atlas-optimization-5ee2
```

来源：合并 `cursor/cometbft-echousage-notdone-676-2f0b`（KB 最全）+ 本优化迭代（677–1114 Query/CheckTx/Commit/InitChain/Finalize/ProposalStatus/Prepare/Apply/Offer Result 拆句；1115–1349 BIP-44/43/85/49/48/45/67/86/89/383/386/381/382/387/371/388/384/385/328/373/87/129/88/78/69/94/325/127/137/70/38/13/321/322/352/353/47/30/147 账户发现、用途层、导出熵、嵌套找回、多签层次、联合签名人发现、确定性地址、单钥 P2TR、链码委托、多签描述符、tr 树、非隔离见证放置、隔离见证压缩、tapscript 多签、Taproot 工作包栏、钱包策略、combo、raw/addr 包装、MuSig2 聚合钥派生、MuSig2 工作包栏、BIP-87 多签路径、BIP-129 安全开户、BIP-88 路径模板、BIP-78 payjoin、BIP-69 字典序、BIP-94 Testnet 4、BIP-325 signet、BIP-127 储备证明、BIP-137 旧式签消息、BIP-70 付款协议、BIP-38 加密私钥、BIP-13 付给脚本哈希地址、BIP-321 付款 URI、BIP-322 通用签消息、BIP-352 静默付款、BIP-353 DNS 付款名、BIP-47 付款码通知、BIP-30 重复交易标识 与 BIP-147 空 dummy、BIP-155 后继地址、BIP-130 头通告偏好、BIP-133 费率过滤器、BIP-338 停交易转发、BIP-434 功能协商、BIP-339 按 wtxid 转发、BIP-330 通告集合对账、BIP-159 有限历史服务、BIP-144 带见证对等服务、BIP-111 布隆服务位、BIP-35 内存池查询、BIP-61 拒收反馈、BIP-31 pong 探活、BIP-14 协议版本、BIP-324 第 2 版传输、BIP-157 客户端侧过滤、BIP-158 基本过滤器、EIP-8 向前兼容、EIP-2124 分叉标识、EIP-778 节点记录、EIP-868 发现要记录、EIP-100 叔块难度、EIP-150 读树涨价、EIP-658 收据状态、PrepareUsage rawmust、PrepareNochecks、PrepareWhen collect、PrepareWhen return、SuggestValidate、LateUnverified、LateMay、VerifyDiscard、VerifyCall、VerifyStatusWhen、VerifyKeep、VerifyAcceptDef、ProcAcceptDef、ExtWhenBcast、EIP-2 Homestead 拆句）。  
`main` 仍只有 `qtb/` 交易框架；协议知识不在 `main`。

---

## 快速导航

| 想做什么 | 去哪 |
|---|---|
| 理解五条轨 | [`../ARCHITECTURE.md`](../ARCHITECTURE.md) |
| 通读学习 | [`04-study-path.md`](04-study-path.md) |
| 查资产进度 | [`03-knowledge-assets.md`](03-knowledge-assets.md) |
| 做不确定选型 | [`../libraries/decision-matrix/`](../libraries/decision-matrix/README.md) |
| 跑对抗语料 | [`../tools/adversarial_runner.py`](../tools/adversarial_runner.py) |
| 审核历史 | [`../AUDIT_LOG.md`](../AUDIT_LOG.md) |
