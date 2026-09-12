# Level 4 · BFT 与 CometBFT 锁

优先级：必学（「不确定」主骨架）  
先修：L0.6、L1.2、Bitcoin L3.1  
档案：[`../../protocols/cometbft/report.md`](../../protocols/cometbft/report.md)

毕业：能讲清为什么 `Propose → Prevote → Precommit → Commit` 不能收成「投票过 2/3」，以及 `V(h)` 必须唯一。

| 课 | 文件 | 覆盖 | 核心问题 |
|---|---|---|---|
| 4.1 | [L04-M01-quorum-intersection.md](L04-M01-quorum-intersection.md) | M4.1 | 2/3 从哪来 |
| 4.2 | [L04-M02-rounds-and-steps.md](L04-M02-rounds-and-steps.md) | M4.2 | 高度、轮、步；本头 LastCommit ≠ 本高已 +2/3（不变量 148）；本地 State ≠ 已经进了块 / 头上的根 ≠ 已经有了 State（不变量 300）；同一高度换轮 ≠ 已经换了集合（不变量 302）；票上 Timestamp ≠ 已经验过 / 冲突提案 ≠ 已经有证据（不变量 304） |
| 4.3 | [L04-M03-locks.md](L04-M03-locks.md) | M4.3 | 锁、解锁、超时 |
| 4.4 | [L04-M04-abci-and-wal.md](L04-M04-abci-and-wal.md) | M4.5 / M4.6 / M4.8 入口 | 应用分离、四门、崩溃不投矛盾票；本头 AppHash ≠ 本块已交差（不变量 147）；写下每条消息 ≠ 已经 fsync / 回放时又要签 ≠ 已经双签（不变量 298）；先装证据 ≠ 已经装满交易 / 两条收交易上限 ≠ 已经同一条（不变量 299）；本地 State ≠ 已经进了块 / 头上的根 ≠ 已经有了 State（不变量 300）；提案收了 ≠ 已经从池里删掉 / CheckTx 过了 ≠ 已经永远有效（不变量 301）；创世 app_state ≠ 已经验过应用状态 / 进程起来 ≠ 已经过了 genesis_time（不变量 303）；同进程 ≠ 已经隔离 / 一条连接 ≠ 已经是四门（不变量 307）；默认锁 ≠ 已经 RPC 安全 / Commit 里等广播 ≠ 已经能往下走（不变量 310）；候选 ≠ 已经是 ExecuteTxState / Prepare 没有头哈希 ≠ 已经知道本头（不变量 311）；CheckTxState ≠ 已经是 ExecuteTxState / RECHECK ≠ 已经是新交易（不变量 312）；内存池去重 ≠ 已经保证不重放 / 过了 CheckTx ≠ 已经有应用级保护（不变量 313）；QueryState ≠ 已经是 ExecuteTxState / 启动对齐 ≠ 已经是快照重放（不变量 314）；MaxGas ≠ 已经在执行 / GasUsed ≠ 已经算进共识（不变量 315）；结果列表 ≠ 已经同一顺序 / Code 非零 ≠ 已经没进块（不变量 316）；CheckTx 的 Data ≠ 已经被引擎用了 / Priority ≠ 已经是共识顺序（不变量 317）；InitChain 空名单 ≠ 已经没有集合 / 同一批重复公钥 ≠ 已经能恢复 / power 0 ≠ 已经删掉不在集合里的人（不变量 318）；InitChain 空参数 ≠ 已经没有参数 / Finalize 没回 ≠ 已经清掉 / 只改一个字段 ≠ 已经只改这一项（不变量 319）；应用高度比引擎高 ≠ 已经允许 / 块进 store ≠ 已经 Commit / 启动 Info 对上 ≠ 已经能跳步（不变量 320）；Offer 收下 ≠ 已经装完 / 一块 chunk 收下 ≠ 已经齐 / 拉失败换一份 ≠ 已经能接着装（不变量 321）；ListSnapshots 回了 ≠ 已经有了全部快照 / 挑了最高 ≠ 已经收下 / Offer 被拒 ≠ 已经停（不变量 322）；装完 ≠ 已经有了 ChainID / AppHash 对上 ≠ 已经版本也对上 / 切进共识 ≠ 已经有完整历史（不变量 323）；拍了这个高度 ≠ 已经交差之后拍的 / 没停链 ≠ 已经一致 / 只留最近两份 ≠ 已经有了全部历史快照（不变量 324）；头上有 AppHash ≠ 已经是交易默克尔 / Query 回了 Proof ≠ 已经对上 AppHash / 一层 ProofOp 的根 ≠ 已经对上最终 AppHash（不变量 325）；发了 addr 过滤查询 ≠ 已经收下这个人 / id 过滤查询绿了 ≠ 已经过了 addr / 有 /store 路径 ≠ 已经是引擎在用（不变量 326）；立刻整块执行 ≠ 已经离开提议超时的关键路径（不变量 327）；同一高度回了不同码 ≠ 已经有了 CheckTxCode（不变量 328）；Query 回了 ≠ 已经复制到各节点（不变量 329）；到了 H ≠ 已经 Prepare 带了扩展（不变量 330）；填了证据 MaxBytes ≠ 已经落在块上限下面（不变量 331）；装完又对上 LastBlockAppHash ≠ 已经在装回当中验过（不变量 332）；本高回了 ConsensusParams ≠ 已经在本高生效 / H+1 立刻用了新参数 ≠ 已经是验证人集合那种 H+2 才计票（不变量 333）；四门里有 Snapshot Connection ≠ 已经必须实现快照 / 给人快照或给自己装回 ≠ 已经必须两头都做（不变量 334）；Finalize 改了状态 ≠ 已经落盘 / 必须在 Commit 落盘 ≠ 已经在 Finalize 落了（不变量 335）；填了 Precision ≠ 已经是 MessageDelay / 填了两个 ≠ 已经启用 PBTS（不变量 336）；-1 就按 100 MB 验 ≠ 已经没有上限 / 应用自己卡体积 ≠ 已经引擎不管了（不变量 337） |
| 4.5 | [L04-M05-validator-set.md](L04-M05-validator-set.md) | M4.4 | 集合何时算数；当选后单位见 NPoS 等权精读；同一高度换轮 ≠ 已经换了集合 / 新加入 ≠ 已经能跳到队头（不变量 302）；InitChain 空名单 ≠ 已经没有集合 / 同一批重复公钥 ≠ 已经能恢复 / power 0 ≠ 已经删掉不在集合里的人（不变量 318） |
| 4.6 | [L04-M06-hotstuff-casper-contrast.md](L04-M06-hotstuff-casper-contrast.md) | M4.7 | QC / FFG 对照，不深挖变体；BABE ≠ GRANDPA、Snow 抽样 ≠ QC 见共识精读 |
