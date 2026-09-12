# 横向地图：一笔转账到「到了」

目的 A 的验收：能不靠背词，把同一笔「阿安付给阿比」在不同系统里走完，并指出绿勾指哪一层。  
先修：L0.7。细节回各课与档案第 4 节。

「到了」必须写成协议对象，不能写成钱包颜色。

| 门 | Bitcoin | CometBFT 应用链 | Ethereum L1 | 乐观 L2 | Zcash 完全屏蔽 |
|---|---|---|---|---|---|
| 签名 | 花指定 UTXO | 应用定义的 tx | nonce+gas 域 | L2 域（须与 L1 分开） | 证明 + 花费权 |
| RPC | 可骗 | 可骗 | 可骗 | 常是排序者 RPC | 可骗；还可拿走查看钥 |
| 池 | 本地政策 / 标准性 | CheckTx ≠ Prepare ≠ Finalize | 本地池或构建者 | 排序者队列 | 证明大，DoS 面大 |
| 排序 | 矿工选入最重链 | 引擎 raw 列表 + 应用 Prepare；Process 不能改。见 [`../consensus/worked-example-prepare-process.md`](../consensus/worked-example-prepare-process.md) | EL 载荷可能由外部 builder 写；提议者可只签盲头。见 [`../mempool/worked-example-who-orders.md`](../mempool/worked-example-who-orders.md) | 排序者；L1 事后锚 | 矿工选入最重链 |
| 执行 | 脚本 + UTXO 花费 | Apply / ABCI | EVM；失败也可含 | L2 先跑 | 验 π、登记 N 与 C' |
| 用户常说的确认 | k 个块 | commit 高度 | head 事件 | L2 出块 | 进块 |
| 更硬的「到了」 | 经济确认政策 | 该高度 commit | finalized | L1 最终 + 窗口 + DA | 同 Bitcoin + nullifier 已上链 |
| 仍能翻的方式 | 更深重组、日蚀 | 集合分叉、实现不同根 | 头摆、弱主观性 | 假根+无揭穿、扣数据 | 重组吐出 N；电路通胀 |

**事实：** 五列都经过「签名 → 别人的机器 → 排序 → 执行 → 磁盘」。名字不同，门还在。  
**事实：** 只有 CometBFT 列把「协议最终」和「一个高度」对齐得最硬；其余都要再问一句。  
**建议：** 「不确定」产品只选一列当结算语义，写进用户能看见的句子。

精读实例：[`worked-example.md`](worked-example.md)（Bitcoin / CometBFT / Ethereum 走同一笔「1」）。  
对照：`../finality/`。有效性租户四档：[`../finality/worked-example-l2-status-vs-l1.md`](../finality/worked-example-l2-status-vs-l1.md)（`PRE_CONFIRMED` ≠ `ACCEPTED_ON_L2` ≠ `ACCEPTED_ON_L1`）。文案：[`../../libraries/settlement-copy.md`](../../libraries/settlement-copy.md)。RPC 当验证：反模式 rpc-as-verification。付款 URI 远程取单 ≠ 验证：[`../failure-museum/cve-2024-52918.md`](../failure-museum/cve-2024-52918.md)。付款 URI 方案本身 ≠ 已经授权：[`worked-example-uri-vs-authorized.md`](worked-example-uri-vs-authorized.md)（不变量 255；不是 55）。签过的消息 ≠ 已经控制资金：[`worked-example-signed-message-vs-control.md`](worked-example-signed-message-vs-control.md)（不变量 258；不是 174 / 179 / 255）。静默付款地址 ≠ 已经有输出：[`worked-example-silent-payment-vs-output.md`](worked-example-silent-payment-vs-output.md)（不变量 260；不是 174 / 255 / 258）。可读名字 ≠ 已经该走 DNS：[`worked-example-dns-name-vs-instruction.md`](worked-example-dns-name-vs-instruction.md)（不变量 261；不是 255 / 55 / 260）。
