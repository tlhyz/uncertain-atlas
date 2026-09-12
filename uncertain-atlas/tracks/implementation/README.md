# 横向：实现保证

协议对，两台诚实机器仍可能算出两个世界。  
目的 A：看见「绿勾」时能指出死的是哪一层。  
目的 B：把确定性写成可测句子，而不是「我们写得很小心」。

精读：

- [`worked-example-encoding.md`](worked-example-encoding.md) — 意思一样、字节不一样
- [`worked-example-crash.md`](worked-example-crash.md) — 写到一半断电
- [`worked-example-wal-vs-signed.md`](worked-example-wal-vs-signed.md) — 写下每条消息 ≠ 已经 fsync；回放时又要签 ≠ 已经双签；LastSignBytes 对上 ≠ 已经换了高度（不变量 298）
- [`worked-example-state-vs-gossip.md`](worked-example-state-vs-gossip.md) — 本地 State ≠ 已经进了块；头上的根 ≠ 已经有了 State；能读本地 State ≠ 已经进了规范（不变量 300）
- [`worked-example-genesis-vs-app.md`](worked-example-genesis-vs-app.md) — 创世 app_state ≠ 已经验过应用状态；进程起来 ≠ 已经过了 genesis_time；空 validators ≠ 已经没有集合（不变量 303）
- [`worked-example-abci-conn-vs-gates.md`](worked-example-abci-conn-vs-gates.md) — 同进程 ≠ 已经有套接字隔离；gRPC 最容易 ≠ 已经高性能；一条连接 ≠ 已经够用，也不是已经是四门（不变量 307）
- [`worked-example-commit-lock-vs-rpc.md`](worked-example-commit-lock-vs-rpc.md) — 默认锁 ≠ 已经 RPC 安全；Commit 前上锁 ≠ 已经解锁；Commit 里等广播 ≠ 已经能往下走（不变量 310）
- [`worked-example-candidate-vs-execute.md`](worked-example-candidate-vs-execute.md) — Prepare 没有头哈希 ≠ 已经知道本头；候选 ≠ 已经是 ExecuteTxState；丢掉 ≠ 已经永远不用再执行（不变量 311）
- [`worked-example-checktxstate-vs-execute.md`](worked-example-checktxstate-vs-execute.md) — CheckTx 过了 ≠ 已经按 ExecuteTxState 验过；两份同时在改 ≠ 已经同一份；RECHECK ≠ 已经是新交易（不变量 312）
- [`worked-example-mempool-indexer-vs-replay.md`](worked-example-mempool-indexer-vs-replay.md) — 内存池去重 ≠ 已经保证不重放；过了 CheckTx ≠ 已经有应用级保护；通常不受欢迎 ≠ 已经没有幂等例外（不变量 313）
- [`worked-example-querystate-vs-execute.md`](worked-example-querystate-vs-execute.md) — QueryState ≠ 已经是 ExecuteTxState；上次 Commit ≠ 已经跟上正在跑的块；启动对齐 ≠ 已经是快照重放（不变量 314）
- [`worked-example-maxgas-vs-enforced.md`](worked-example-maxgas-vs-enforced.md) — MaxGas ≠ 已经在执行；GasUsed ≠ 已经算进共识；已提交块 ≠ 已经按气验过（不变量 315）
- [`worked-example-exectxresult-vs-consensus.md`](worked-example-exectxresult-vs-consensus.md) — 结果列表 ≠ 已经同一顺序；Code 非零 ≠ 已经没进块；Code / Data ≠ 已经印进本头（不变量 316）
- [`worked-example-checktxresponse-vs-exec.md`](worked-example-checktxresponse-vs-exec.md) — CheckTx 的 Data ≠ 已经被引擎用了；各节点 Data 不一样 ≠ 已经分叉；Priority ≠ 已经是共识顺序（不变量 317）
- [`worked-example-validatorupdate-vs-set.md`](worked-example-validatorupdate-vs-set.md) — InitChain 空名单 ≠ 已经没有集合；同一批重复公钥 ≠ 已经能恢复；power 0 ≠ 已经删掉不在集合里的人（不变量 318）
- [`worked-example-consensusparams-vs-update.md`](worked-example-consensusparams-vs-update.md) — InitChain 空参数 ≠ 已经没有参数；Finalize 没回 ≠ 已经清掉；只改一个字段 ≠ 已经只改这一项（不变量 319）
- [`worked-example-crash-steps-vs-commit.md`](worked-example-crash-steps-vs-commit.md) — 应用高度比引擎高 ≠ 已经允许；块进 store ≠ 已经 Commit；启动 Info 对上 ≠ 已经能跳步（不变量 320）
- [`worked-example-snapshot-restore-vs-offer.md`](worked-example-snapshot-restore-vs-offer.md) — Offer 收下 ≠ 已经装完；一块 chunk 收下 ≠ 已经齐；拉失败换一份 ≠ 已经能接着装（不变量 321）
- [`worked-example-snapshot-discover-vs-offer.md`](worked-example-snapshot-discover-vs-offer.md) — ListSnapshots 回了 ≠ 已经有了全部快照；挑了最高 ≠ 已经收下；Offer 被拒 ≠ 已经停（不变量 322）
- [`worked-example-snapshot-switch-vs-history.md`](worked-example-snapshot-switch-vs-history.md) — 装完 ≠ 已经有了 ChainID；AppHash 对上 ≠ 已经版本也对上；切进共识 ≠ 已经有完整历史（不变量 323）
- [`worked-example-snapshot-take-vs-commit.md`](worked-example-snapshot-take-vs-commit.md) — 拍了这个高度 ≠ 已经交差之后拍的；没停链 ≠ 已经一致；只留最近两份 ≠ 已经有了全部历史快照（不变量 324）
- [`worked-example-query-proof-vs-apphash.md`](worked-example-query-proof-vs-apphash.md) — 头上有 AppHash ≠ 已经是交易默克尔；Query 回了 Proof ≠ 已经对上 AppHash；一层 ProofOp 的根 ≠ 已经对上最终 AppHash（不变量 325）
- [`worked-example-peerfilter-vs-query.md`](worked-example-peerfilter-vs-query.md) — 发了 addr 过滤查询 ≠ 已经收下这个人；id 过滤查询绿了 ≠ 已经过了 addr；有 /store 路径 ≠ 已经是引擎在用（不变量 326）
- [`worked-example-prepare-timeout-vs-liveness.md`](worked-example-prepare-timeout-vs-liveness.md) — 立刻整块执行 ≠ 已经离开提议超时的关键路径；填了 TimeoutPropose ≠ 已经装得下；又开一轮 ≠ 已经丢了活性（不变量 327）
- [`worked-example-checktx-oscillate-vs-stable.md`](worked-example-checktx-oscillate-vs-stable.md) — 同一高度回了不同码 ≠ 已经有了 CheckTxCode；还在振荡 ≠ 已经过了 h_stable；本地不再振荡 ≠ 已经各节点同一份 b（不变量 328）
- [`worked-example-query-vs-replicated.md`](worked-example-query-vs-replicated.md) — Query 回了 ≠ 已经复制到各节点；查到了 ≠ 已经新鲜；实现了 Query ≠ 已经是正常运转必须有（不变量 329）
- [`worked-example-ve-height-vs-prepare.md`](worked-example-ve-height-vs-prepare.md) — 到了 H ≠ 已经 Prepare 带了扩展；H+1 带了扩展 ≠ 已经是本高度刚签的；h < H 带了扩展 ≠ 已经合法（不变量 330）
- [`worked-example-evidence-maxbytes-vs-block.md`](worked-example-evidence-maxbytes-vs-block.md) — 填了证据 MaxBytes ≠ 已经落在块上限下面；> 0 ≠ 已经盖住解绑；证据 MaxBytes ≠ 已经是块 MaxBytes（不变量 331）
- [`worked-example-snapshot-verify-vs-early.md`](worked-example-snapshot-verify-vs-early.md) — 装完又对上 LastBlockAppHash ≠ 已经在装回当中验过；增量验了 chunk ≠ 已经是唯一可信的 AppHash；封禁邻居 ≠ 已经没有快照 DoS（不变量 332）
- [`worked-example-params-delay-vs-set.md`](worked-example-params-delay-vs-set.md) — 本高回了 ConsensusParams ≠ 已经在本高生效；H+1 立刻用了新参数 ≠ 已经是验证人集合那种 H+2 才计票；参数更新写了 H+1 ≠ 已经是扩展启用高度那种切换（不变量 333）
- [`worked-example-snapshot-conn-vs-required.md`](worked-example-snapshot-conn-vs-required.md) — 四门里有 Snapshot Connection ≠ 已经必须实现快照；给人快照或给自己装回 ≠ 已经必须两头都做；应用选择不实现 ≠ 已经没有 state sync 这条对象（不变量 334）
- [`worked-example-finalize-persist-vs-commit.md`](worked-example-finalize-persist-vs-commit.md) — Finalize 改了状态 ≠ 已经落盘；必须在 Commit 落盘 ≠ 已经在 Finalize 落了；记住上次成功 Commit 高度 ≠ 已经能跳步（不变量 335）
- [`worked-example-precision-vs-msgdelay.md`](worked-example-precision-vs-msgdelay.md) — 填了 Precision ≠ 已经是 MessageDelay；填了两个 ≠ 已经启用 PBTS；用于 PBTS ≠ 已经是永恒常数（不变量 336）
- [`worked-example-maxbytes-cap-vs-unlimited.md`](worked-example-maxbytes-cap-vs-unlimited.md) — -1 就按 100 MB 验 ≠ 已经没有上限；应用自己卡体积 ≠ 已经引擎不管了；必须 -1 或不超过 100 MB ≠ 已经是默认 21 MB（不变量 337）
- [`worked-example-prepare-nondet-vs-process.md`](worked-example-prepare-nondet-vs-process.md) — Prepare 没有确定性要求 ≠ 已经必须确定；两边 raw 一样 ≠ 已经是同一份提案；ExtendVote 没有确定性要求 ≠ 已经是同一份扩展（不变量 338）
- [`worked-example-checktx-weak-vs-process.md`](worked-example-checktx-weak-vs-process.md) — 不该验排序相关有效性 ≠ 已经该在 CheckTx 里验；拜占庭能提案一满块无效交易 ≠ 已经被池子挡住；ProcessProposal 对付这种行为 ≠ 已经是 CheckTx（不变量 339）
- [`worked-example-process-det-vs-prepare.md`](worked-example-process-det-vs-prepare.md) — Process 必须只依赖请求和上一份状态 ≠ 已经可以像 Prepare 那样依赖其它值；两边对任意块同一裁决 ≠ 已经只对诚实提案同一裁决；Process 非确定 bug 没有现成解法 ≠ 已经丢了安全性（不变量 340）
- [`worked-example-verify-det-vs-extend.md`](worked-example-verify-det-vs-extend.md) — Verify 必须只依赖扩展、这块和上一份状态 ≠ 已经可以像 ExtendVote 那样依赖其它值；两边对任意扩展同一裁决 ≠ 已经只对诚实扩展同一裁决；Verify 非确定会伤活性 ≠ 已经丢了安全性（不变量 341）
- [`worked-example-finalize-det-vs-prepare.md`](worked-example-finalize-det-vs-prepare.md) — Finalize 算出的状态必须只依赖上一份状态和决定块 ≠ 已经可以像 Prepare 那样依赖其它值；Finalize 算出的结果必须只依赖上一份状态和决定块 ≠ 已经是 Code/Data 印进本头；两边状态机复制 ≠ 已经是 Process 对任意块同一裁决（不变量 342）
- [`worked-example-pbts-height-vs-params.md`](worked-example-pbts-height-vs-params.md) — 写成 0 不是已经启用 PBTS ≠ 已经填了 Precision 就是 PBTS；H 之前仍用 BFT Time ≠ 已经切到 PBTS；启用之后不能关 ≠ 已经是扩展启用高度那种切换（不变量 343）
- [`worked-example-maxbytes-overhead-vs-full.md`](worked-example-maxbytes-overhead-vs-full.md) — MaxBytes 减去头集合证据才是交易上限 ≠ 已经整块都能装交易；诚实验证者 MAY 出满 MaxBytes ≠ 已经只会出默认 21 MB；timeout 必须按满块投递延迟算 ≠ 已经填了 TimeoutPropose 就装得下这次 Prepare 执行（不变量 344）
- [`worked-example-prepare-return-vs-pool.md`](worked-example-prepare-return-vs-pool.md) — 整池可见 ≠ 已经只能看见装得进一块的子集；聚合体积可以超过 max_tx_bytes ≠ 已经能回超限列表；Req 2 保证回的列表不让块超字节上限 ≠ 已经是引擎会帮你裁（不变量 345）
- [`worked-example-abci20-upgrade-vs-height.md`](worked-example-abci20-upgrade-vs-height.md) — 必须协调升级 ≠ 已经只改 VoteExtensionsEnableHeight；h_e 必须高于当前 ≠ 已经能写成当前高度；引擎按当前高度决定存什么要什么 ≠ 已经按创世配好了（不变量 346）
- [`worked-example-req3-coherence-vs-accept.md`](worked-example-req3-coherence-vs-accept.md) — 正确提议者的准备提案必须被正确接收者 Accept ≠ 已经是任意块都会 Accept；Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 ≠ 已经只是活性问题；Req 3 是大量测试和自动验证的目标 ≠ 已经测过（不变量 347）
- [`worked-example-req6-coherence-vs-accept.md`](worked-example-req6-coherence-vs-accept.md) — 正确进程交出的扩展必须被正确接收者 Verify Accept ≠ 已经是任意扩展都会 Accept；Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 ≠ 已经只是活性问题；会面对和 Req 5 同一类活性问题 ≠ 已经丢了安全性（不变量 348）
- [`worked-example-req9-noside-vs-commit.md`](worked-example-req9-noside-vs-commit.md) — Prepare 不得改已提交状态 ≠ 已经立刻执行就已经交差；Process 不得改已提交状态 ≠ 已经 Accept 就已经改了；Extend 和 Verify 不得改已提交状态 ≠ 已经签了扩展就已经进状态（不变量 349）
- [`worked-example-extend-once-vs-round.md`](worked-example-extend-once-vs-round.md) — 一轮最多一张 Precommit ≠ 已经能再签一张；ExtendVote 只在即将广播非 nil Precommit 时才叫 ≠ 已经签了 nil 票；一轮只能交出一份扩展 ≠ 已经是每一高度一份（不变量 350）
- [`worked-example-process-also-vs-prepare.md`](worked-example-process-also-vs-prepare.md) — Process 也会在提议者那边叫 ≠ 已经不用再 Process；通常紧跟 Prepare、列表对得上 ≠ 已经保证是这一次；失败时可能对上更早一次或根本不调 ≠ 已经每轮都会叫（不变量 351）
- [`worked-example-late-extension-vs-verified.md`](worked-example-late-extension-vs-verified.md) — +2/3 之后才进来的扩展写进了 commit info ≠ 已经 Verify 过；建议按 Verify 同款逻辑再看一遍 ≠ 已经是引擎会再 Verify；下一高度 round 0 写进 ExtendedCommitInfo ≠ 已经又叫了 Verify（不变量 352）
- [`worked-example-verify-when-vs-empty.md`](worked-example-verify-when-vs-empty.md) — 空扩展仍会调 Verify ≠ 已经跳过 Verify；不对本进程自己发出的 Precommit 调用 ≠ 已经自己验过；请求里的 hash ≠ 已经对该块跑过 Process（不变量 353）
- [`worked-example-process-when-vs-later.md`](worked-example-process-when-vs-later.md) — Process 调用是同步的 ≠ 已经能在返回之后再改裁决；只做基本检查再异步 Process ≠ 已经还能再 Reject；非验证者可以立刻回 ACCEPT ≠ 已经验过这块（不变量 354）
- [`worked-example-prepare-drop-vs-mempool.md`](worked-example-prepare-drop-vs-mempool.md) — 从提案拿掉 tx ≠ 已经从内存池删掉；往提案加了一笔新的 ≠ 已经进了内存池；把 t1 改成 t2 ≠ 已经还能按 t1 查到（不变量 355）
- [`worked-example-validvalue-vs-prepare.md`](worked-example-validvalue-vs-prepare.md) — validValue 非 nil ≠ 已经还会调 Prepare；自己是提议者 ≠ 已经每轮都会调 Prepare；没调 Prepare ≠ 已经又装了一份 raw 提案（不变量 356）
- [`worked-example-prepare-valid-vs-checked.md`](worked-example-prepare-valid-vs-checked.md) — 引擎没有再验重复交易 ≠ 已经验过重复；Prepare 回包验不过引擎崩溃 ≠ 已经是 Process REJECT；Prepare 里产出了事件 ≠ 已经交给引擎（不变量 357）
- [`worked-example-nonrp-vs-wrapped.md`](worked-example-nonrp-vs-wrapped.md) — vote_extension 会包进 CanonicalVoteExtension ≠ 已经按原样签；non_rp_extension 按原样签 ≠ 已经有重放保护；要签原样数据可以用 non_rp ≠ 已经和 vote_extension 同一份（不变量 358）
- [`worked-example-prepare-fields-vs-same.md`](worked-example-prepare-fields-vs-same.md) — Prepare 和 Process / Finalize 同一套字段 ≠ 已经跑过 Process；local_last_commit 是上一高度的预提交带扩展 ≠ 已经是本高度刚签的扩展；height / time / proposer_address 对上拟议头 ≠ 已经知道本头哈希（不变量 359）
- [`worked-example-finalize-vs-processed.md`](worked-example-finalize-vs-processed.md) — 至少一名非拜占庭验证者跑过 Process ≠ 已经每个验证者都跑过 Process；Finalize 请求把字段再填一遍 ≠ 已经不用再给；可以套用先前候选 ≠ 已经是 ExecuteTxState（不变量 360）
- [`worked-example-extend-when-vs-locked.md`](worked-example-extend-when-vs-locked.md) — +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote ≠ 已经会调 ExtendVote；ExtendVote 调用是同步的 ≠ 已经能在返回之后再改扩展；回包字节不被共识算法解释 ≠ 已经是同一份扩展（不变量 361）
- [`worked-example-finalize-when-vs-decided.md`](worked-example-finalize-when-vs-decided.md) — +2/3 precommit 同一 id(v) 才决定再调 Finalize ≠ 已经会调 Finalize；先把 v 落成这一高的决定再调 Finalize ≠ 已经交差；应用回了 AppHash 和各笔输出 ≠ 已经印进本头（不变量 362）
- [`worked-example-finalize-equiv-vs-gates.md`](worked-example-finalize-equiv-vs-gates.md) — Finalize 等价于 ABCI 1.0 那三步 ≠ 已经是四门已经结算；可以用 decided_last_commit 定奖惩 ≠ 已经罚没；必须回四列 ≠ 已经改了集合（不变量 363）
- [`worked-example-assumevalid.md`](worked-example-assumevalid.md) — 跳过签名 ≠ 换共识链；assumevalid ≠ assumeutxo ≠ 旧 checkpoint
- [`worked-example-header-work.md`](worked-example-header-work.md) — 头先够工作量再入库；检查点第三份工作是反垃圾
- [`worked-example-statesync.md`](worked-example-statesync.md) — 应用快照 ≠ 从创世重放；只有轻验 AppHash 可信。亲戚：轻验集合 ≠ 提议者选择，[ASA-2024-009](../failure-museum/asa-2024-009.md)
- [`worked-example-txid-vs-wtxid.md`](worked-example-txid-vs-wtxid.md) — txid ≠ wtxid；改见证 ≠ 已经改交易身份；头上的 txid Merkle ≠ 已经承诺 wtxid（不变量 152）
- [`worked-example-keypath-vs-scriptpath.md`](worked-example-keypath-vs-scriptpath.md) — 钥匙路径 ≠ 已经揭开脚本树；脚本路径 ≠ 已经揭开全部脚本（不变量 153）
- [`worked-example-tapscript-vs-scriptpath.md`](worked-example-tapscript-vs-scriptpath.md) — 走脚本路径 ≠ 已经是 tapscript 语义；遇见成功操作码 ≠ 已经执行完；342 ≠ 341 ≠ 141 ≠ 16（不变量 189）
- [`worked-example-miniscript-vs-script.md`](worked-example-miniscript-vs-script.md) — 看见 Miniscript ≠ 已经是链上脚本；共识健全 ≠ 已经是策略完备；379 ≠ 380 ≠ 342 ≠ 16（不变量 191）
- [`worked-example-typed-vs-legacy.md`](worked-example-typed-vs-legacy.md) — 类型字节 ≠ 已经解开内层；旧式列表 ≠ 已经是信封；2718 ≠ 1559 ≠ 155（不变量 167）
- [`../finality/worked-example-request-vs-action.md`](../finality/worked-example-request-vs-action.md) — 看见头里的请求承诺 ≠ 已经由共识层处理完；请求 ≠ 已经有权单独促成动作；7685 ≠ 4895 ≠ 2718（不变量 192）
- [`../state-models/worked-example-delegation-vs-code.md`](../state-models/worked-example-delegation-vs-code.md) — 看见授权名单 ≠ 已经委托成功；委托指示 ≠ 已经是目标代码；7702 ≠ 3607 ≠ 3541 ≠ 2718（不变量 190）
- [`worked-example-listed-vs-accessed.md`](worked-example-listed-vs-accessed.md) — 列出地址或槽 ≠ 已经访问过；列表外 ≠ 已经不能碰；2930 ≠ 2718 ≠ 1559（不变量 168）
- [`worked-example-cold-vs-warm.md`](worked-example-cold-vs-warm.md) — 本笔第一次碰 ≠ 已经热；本笔再碰 ≠ 又是冷访问；2929 ≠ 2930 ≠ 墙钟（不变量 169）
- [`worked-example-coinbase-vs-prefill.md`](worked-example-coinbase-vs-prefill.md) — 出块者地址开跑时已在热集合 ≠ 已经访问过；开跑已热 ≠ 已经付给出块者；开跑已热 ≠ 169 那几个预填已经覆盖出块者；3651 ≠ 2929 ≠ 2930 ≠ 1559（不变量 187）
- [`worked-example-versionbit-vs-active.md`](worked-example-versionbit-vs-active.md) — 版本位被置上 ≠ 已经锁定；锁定 ≠ 已经激活；9 ≠ 34 ≠ 被部署的那条规则（不变量 171）
- [`worked-example-valid-vs-der.md`](worked-example-valid-vs-der.md) — ECDSA 验得过 ≠ 已经是严格 DER；库收下 ≠ 共识已经接受；66 ≠ 62 ≠ 146 ≠ 34（不变量 172）
- [`worked-example-dummy-vs-empty.md`](worked-example-dummy-vs-empty.md) — 多余栈元素 ≠ 已经随便填；隔离见证 ≠ 已经没有这条延展；策略已经要空 dummy ≠ 已经是共识（不变量 264）
- [`worked-example-signet-vs-testnet.md`](worked-example-signet-vs-testnet.md) — signet ≠ 已经是 testnet；signet ≠ 已经是 regtest；头上有合法工作量 ≠ 已经签过（不变量 265）
- [`worked-example-purpose-vs-compatible.md`](worked-example-purpose-vs-compatible.md) — BIP32 compatible ≠ 已经能互操作；自称 BIPxx compatible ≠ 已经是那份结构；同一套扩展钥前缀 ≠ 已经是比特币专用（不变量 266）
- [`worked-example-account-vs-discovered.md`](worked-example-account-vs-discovered.md) — 同一份种子 ≠ 已经是同一条币；下一个账户号 ≠ 已经有过往；余额为零 ≠ 已经发现完（不变量 267）
- [`worked-example-nested-vs-same-account.md`](worked-example-nested-vs-same-account.md) — 同一套 BIP44 账户 ≠ 已经能找回嵌套隔离见证；专用账户 ≠ 已经向后兼容；账户出现了 ≠ 已经不用核余额（不变量 268）
- [`worked-example-script-type-vs-account.md`](worked-example-script-type-vs-account.md) — 现有多签派生习惯 ≠ 已经要搬家；脚本类型层 ≠ 已经是账户层；本页多签 ≠ 已经不排序（不变量 269）
- [`worked-example-sorted-vs-one-address.md`](worked-example-sorted-vs-one-address.md) — 同一套钥 ≠ 已经是同一条 P2SH 地址；只共享门限和主公钥 ≠ 已经够了；未压缩钥 ≠ 已经是本页（不变量 270）
- [`worked-example-cosigner-vs-discovered.md`](worked-example-cosigner-vs-discovered.md) — 共享主公钥 ≠ 已经是本页；能独立长地址 ≠ 已经能独立签；前面分支没有交易 ≠ 已经发现完（不变量 271）
- [`worked-example-derived-vs-output-key.md`](worked-example-derived-vs-output-key.md) — 派生钥 ≠ 已经是输出钥；不需要脚本路径 ≠ 已经不承诺；种子备份 ≠ 已经能找回单钥 P2TR（不变量 272）
- [`worked-example-multi-vs-sortedmulti.md`](worked-example-multi-vs-sortedmulti.md) — multi ≠ 已经按字典序排；门限和钥数 ≠ 已经同一套上限；多把扩展钥 ≠ 已经各自编号（不变量 274）
- [`worked-example-tr-vs-tree.md`](worked-example-tr-vs-tree.md) — tr 没有树 ≠ 已经有脚本路径；树表达式 ≠ 已经是旧脚本套法；压缩钥 ≠ 已经是 x-only（不变量 275）
- [`worked-example-pk-vs-toplevel.md`](worked-example-pk-vs-toplevel.md) — pk ≠ 已经和 pkh / sh 同一套放置；sh 产出 ≠ 已经有赎回脚本；熟悉的标准脚本 ≠ 已经能互操作（不变量 276）
- [`worked-example-wpkh-vs-compressed.md`](worked-example-wpkh-vs-compressed.md) — wpkh / wsh ≠ 已经只能顶层；未压缩钥 ≠ 已经允许；wsh 产出 ≠ 已经有见证脚本（不变量 277）
- [`worked-example-multia-vs-tr.md`](worked-example-multia-vs-tr.md) — multi_a ≠ 已经是 383 那种 multi；门限 ≠ 已经同一套编码；sortedmulti_a ≠ 已经是 383 那种排序（不变量 278）
- [`worked-example-tap-psbt-vs-old.md`](worked-example-tap-psbt-vs-old.md) — 旧 PSBT 栏 ≠ 已经能装 Taproot；输出脚本里的钥 ≠ 已经是内部钥；Taproot 输入 ≠ 已经必须带整笔前交易（不变量 279）
- [`worked-example-policy-vs-descriptor.md`](worked-example-policy-vs-descriptor.md) — 钱包策略 ≠ 已经是一条描述符；钥占位 ≠ 已经是那把精确公钥；登记过 ≠ 已经批准这笔花（不变量 280）
- [`worked-example-combo-vs-one-script.md`](worked-example-combo-vs-one-script.md) — combo ≠ 已经只能产出一种脚本；未压缩钥 ≠ 已经带齐见证对；一份 combo ≠ 已经是一份钱包策略（不变量 281）
- [`worked-example-raw-vs-named.md`](worked-example-raw-vs-named.md) — raw ≠ 已经能套进具名表达式；addr ≠ 已经是那份输出脚本；一份包装 ≠ 已经是 combo（不变量 282）
- [`worked-example-musig-xpub-vs-aggregate.md`](worked-example-musig-xpub-vs-aggregate.md) — 聚合钥 ≠ 已经是扩展公钥；合成扩展公钥 ≠ 已经能硬化派生；派生出的子钥 ≠ 已经能不带微调去签（不变量 283）
- [`worked-example-musig-psbt-vs-tap.md`](worked-example-musig-psbt-vs-tap.md) — 旧 PSBT 栏 ≠ 已经能装 MuSig2；聚合钥栏 ≠ 已经是输出钥；参与者钥 ≠ 已经能出部分签（不变量 284）
- [`worked-example-multisig-path-vs-script.md`](worked-example-multisig-path-vs-script.md) — 脚本各走各的路径 ≠ 已经是多签该有的树；路径里的脚本类型 ≠ 已经必要；主种子 ≠ 已经够找回（不变量 285）
- [`worked-example-entropy-vs-seed.md`](worked-example-entropy-vs-seed.md) — 一份助记词 ≠ 已经能备齐所有钱包；扩展根钥 ≠ 已经能倒回助记词；派生出的熵 ≠ 已经是目标钱包的种子（不变量 286）
- [`worked-example-setup-vs-psbt.md`](worked-example-setup-vs-psbt.md) — 部分签名包 ≠ 已经是跨厂安全多签开户；指纹对上 ≠ 已经核过 KEY；TOKEN ≠ 已经是钱包种子（不变量 287）
- [`worked-example-template-vs-path.md`](worked-example-template-vs-path.md) — 一条派生路径 ≠ 已经是一份路径模板；写死了熟路径检查 ≠ 已经能互操作；完整模板 ≠ 已经是半截模板（不变量 288）
- [`worked-example-delegation-vs-xpub.md`](worked-example-delegation-vs-xpub.md) — 共享了扩展公钥 ≠ 已经是链码委托；委托方那把非扩展钥 ≠ 已经能推出整棵钱包；这一输入的微调 ≠ 已经是盲签（不变量 289）
- [`../lifecycle/worked-example-payjoin-vs-original.md`](../lifecycle/worked-example-payjoin-vs-original.md) — 带 pj= 的付款 URI ≠ 已经是 payjoin 付款；原始包 ≠ 已经是提案；收款方加了输入 ≠ 已经另开一笔（不变量 290）
- [`worked-example-order-vs-lex.md`](worked-example-order-vs-lex.md) — 自家习惯的输入输出顺序 ≠ 已经是字典序标准；按字典序排了 ≠ 已经是共识 / ≠ 已经私人（不变量 291）
- [`worked-example-testnet4-vs-testnet3.md`](worked-example-testnet4-vs-testnet3.md) — Testnet 4 ≠ 已经是 Testnet 3；20 分钟例外 ≠ 已经没有块风暴；会 Testnet 3 ≠ 已经能安全跟（不变量 292）
- [`../lifecycle/worked-example-reserves-vs-spend.md`](../lifecycle/worked-example-reserves-vs-spend.md) — 储备证明交易 ≠ 已经能花；其余输入签过 ≠ 已经控制资金；POR 栏 ≠ 已经是普通花费（不变量 293）
- [`worked-example-encrypted-key-vs-usable.md`](worked-example-encrypted-key-vs-usable.md) — 加密私钥记录 ≠ 已经能用；厂家代生成 ≠ 已经能兑；地址哈希片段 ≠ 已经是地址（不变量 296）
- [`worked-example-p2sh-address-vs-redeem.md`](worked-example-p2sh-address-vs-redeem.md) — 本页这种地址 ≠ 已经是赎回脚本；旧软件报无效 ≠ 已经付过；只有地址 ≠ 已经知道付给谁（不变量 297）
- [`worked-example-coinbase-height-vs-header.md`](worked-example-coinbase-height-vs-header.md) — coinbase 第一项写了高度 ≠ 头上已经有高度字段；34 ≠ 9 ≠ 66（不变量 173）
- [`worked-example-address-vs-utxo.md`](worked-example-address-vs-utxo.md) — 看见 Bech32 地址串 ≠ 链上已经有这笔输出；校验过 ≠ 程序已经上链；173 ≠ 350 ≠ 141 ≠ 13（不变量 174）
- [`worked-example-bech32m-vs-bech32.md`](worked-example-bech32m-vs-bech32.md) — 后继校验过了 ≠ 已经是旧校验那套地址；版本与编码必须配对；350 ≠ 173 ≠ 141（不变量 181）
- [`worked-example-xpub-vs-spendable.md`](worked-example-xpub-vs-spendable.md) — 看见扩展公钥 ≠ 已经能花；硬化 ≠ 已经能从公钥推出；32 ≠ 173 ≠ 174 ≠ 350（不变量 182）
- [`worked-example-mnemonic-vs-seed.md`](worked-example-mnemonic-vs-seed.md) — 看见助记词 ≠ 已经是二进制种子；口令不同 ≠ 已经非法；39 ≠ 32 ≠ 173 ≠ 380（不变量 183）
- [`worked-example-descriptor-vs-keys.md`](worked-example-descriptor-vs-keys.md) — 看见私钥或助记词备份 ≠ 已经知道该看哪种输出脚本；看见描述符 ≠ 已经是地址；380 ≠ 39 ≠ 32 ≠ 173（不变量 184）
- [`worked-example-initcode-vs-runtime.md`](worked-example-initcode-vs-runtime.md) — initcode 超界 ≠ 已经是部署代码超界；按字分析费 ≠ 已经跑完构造；3860 ≠ 170 ≠ 1014 ≠ 2681（不变量 176）
- [`worked-example-calldata-floor-vs-execution.md`](worked-example-calldata-floor-vs-execution.md) — 看见 calldata 地板 ≠ 已经改了执行气；数据为主更贵 ≠ 已经让普通转账更贵；预留地板气限 ≠ 已经烧到地板；7623 ≠ 4844 ≠ 1559 ≠ 2028（不变量 197）
- [`worked-example-rlp-cap-vs-gas.md`](worked-example-rlp-cap-vs-gas.md) — 看见 RLP 编码硬帽 ≠ 已经改了气限；共识层流言不传 ≠ 已经让执行层非法；给信标块留边 ≠ 已经并成一份编码；7934 ≠ 7623 ≠ 1559 ≠ 96（不变量 202）
- [`worked-example-tx-gas-cap-vs-block.md`](worked-example-tx-gas-cap-vs-block.md) — 看见单笔气帽 ≠ 已经改了块气限；入池拒掉 ≠ 已经验过块；块里有一笔超帽 ≠ 已经只是策略拒绝；7825 ≠ 7934 ≠ 7623 ≠ 96（不变量 203）
- [`worked-example-modexp-bound-vs-price.md`](worked-example-modexp-bound-vs-price.md) — 看见 MODEXP 输入长度帽 ≠ 已经改了计价公式；超帽 ≠ 已经成功返回；长度有界 ≠ 已经换成 EVM；7823 ≠ 198 重定价 ≠ 7825 ≠ 7951（不变量 206）
- [`worked-example-clz-vs-zk.md`](worked-example-clz-vs-zk.md) — 看见数前导零操作码 ≠ 已经更便宜的 ZK 证明；动机写了后量子签 ≠ 已经有后量子签名；能表达最低位 ≠ 已经有数尾零；7939 ≠ 206 ≠ 199 ≠ 204（不变量 208）
- [`worked-example-config-rpc-vs-aligned.md`](worked-example-config-rpc-vs-aligned.md) — 看见分叉配置 RPC 对上了 ≠ 已经过多客户端同根；看见 current / next / last ≠ 已经改了共识；RPC 绿 ≠ 对等节点没有撒谎；7910 ≠ 149 ≠ 209 ≠ 207（不变量 210）
- [`worked-example-default-gas-vs-cap.md`](worked-example-default-gas-vs-cap.md) — 看见客户端默认气限 ≠ 已经是协议帽；看见绑到硬分叉发布 ≠ 已经改了共识；看见默认配置齐了 ≠ 已经是单笔气帽；7935 ≠ 203 ≠ 202 ≠ 96（不变量 211）
- [`worked-example-block-list-vs-parallel.md`](worked-example-block-list-vs-parallel.md) — 看见块级访问名单 ≠ 已经并行跑完；看见强制名单 ≠ 已经是 2930；看见事后状态差 ≠ 已经不跑交易；7928 ≠ 168 ≠ 143 ≠ 122（不变量 212）
- [`worked-example-mcopy-vs-identity.md`](worked-example-mcopy-vs-identity.md) — 看见内存拷贝指令 ≠ 已经是身份预编译；看见「像用了中间缓冲」 ≠ 已经必须真分配一块缓冲；看见能重叠拷 ≠ 已经是 calldata / 返回数据拷；5656 ≠ 2929 ≠ 208（不变量 216）
- [`worked-example-push0-vs-push1.md`](worked-example-push0-vs-push1.md) — 看见压零指令 ≠ 已经是带立即数的压 0；看见没有立即数 ≠ 已经改了跳转目的分析；看见已经部署碰巧用了这个字节 ≠ 行为已经不变；3855 ≠ 5656 ≠ 216（不变量 217）
- [`worked-example-basefee-opcode-vs-market.md`](worked-example-basefee-opcode-vs-market.md) — 看见基础费指令 ≠ 已经改了费用市场；看见能读本块基础费 ≠ 已经给了出块者；看见跑 EVM 前就已经有这个数 ≠ 已经改了头怎么算；3198 ≠ 1559 ≠ 158（不变量 218）
- [`worked-example-blobbasefee-vs-basefee.md`](worked-example-blobbasefee-vs-basefee.md) — 看见 blob 基础费指令 ≠ 已经是执行层基础费指令；看见能读本块 blob 基础费 ≠ 已经并成一套气；看见跑 EVM 前就已经有这个数 ≠ 已经改了 4844 日程；7516 ≠ 3198 ≠ 218 ≠ 4844（不变量 219）
- [`worked-example-chainid-opcode-vs-signed.md`](worked-example-chainid-opcode-vs-signed.md) — 看见链号指令 ≠ 已经是签进哈希的链号；看见指令返回配置链号 ≠ 已经是这笔交易带了 EIP-155 标识；看见编译期写死的链号 ≠ 已经在硬分叉后仍安全；1344 ≠ 155 ≠ 161 ≠ 712（不变量 220）
- [`worked-example-extcodehash-vs-copy.md`](worked-example-extcodehash-vs-copy.md) — 看见代码哈希指令 ≠ 已经看见代码本身；看见返回 0 ≠ 已经是没代码的账户；看见空数据哈希 ≠ 已经是账户不存在；1052 ≠ 161 ≠ 180 ≠ 162（不变量 221）
- [`worked-example-create2-vs-created.md`](worked-example-create2-vs-created.md) — 看见盐创建指令 ≠ 已经是按发送者加序号占址；看见算出来的盐地址 ≠ 已经创建；看见碰撞变得可能 ≠ 已经覆盖；1014 ≠ 3860 ≠ 176 ≠ 684（不变量 222）
- [`worked-example-refund-vs-gone.md`](worked-example-refund-vs-gone.md) — 看见退款削减 ≠ 已经没有退款；看见去掉自毁退款 ≠ 已经改了自毁语义；看见退款计数 ≠ 已经能在执行当中用；3529 ≠ 2200 ≠ 160 ≠ 158（不变量 223）
- [`worked-example-deprecate-vs-changed.md`](worked-example-deprecate-vs-changed.md) — 看见弃用警告 ≠ 已经改了共识行为；看见本页 ≠ 已经改了客户端；看见「以后可能变」≠ 已经变了；6049 ≠ 6780 ≠ 160 ≠ 223（不变量 224）
- [`worked-example-net-meter-vs-transient.md`](worked-example-net-meter-vs-transient.md) — 看见净计量 ≠ 已经是瞬时存储；看见原来值 / 当前值 / 新值 ≠ 已经只有当前值；看见津贴帧禁写 ≠ 已经能改槽；2200 ≠ 1153 ≠ 159 ≠ 3529 ≠ 223（不变量 225）
- [`worked-example-calldata-cut-vs-unlimited.md`](worked-example-calldata-cut-vs-unlimited.md) — 看见非零 calldata 降价 ≠ 已经给零字节也降价；看见降价 ≠ 已经没有块大小上限；看见降价 ≠ 已经不伤延迟 / 安全；2028 ≠ 7623 ≠ 197 ≠ 4844 ≠ 145（不变量 226）
- [`worked-example-modexp-price-vs-bound.md`](worked-example-modexp-price-vs-bound.md) — 看见模幂重计价 ≠ 已经是 198 那道复杂度公式；看见更便宜 ≠ 已经改了接口或算法；看见最低气价 ≠ 已经能对小输入无限便宜；2565 ≠ 7823 ≠ 206 ≠ 198 原文（不变量 227）
- [`worked-example-bn128-cut-vs-verify.md`](worked-example-bn128-cut-vs-verify.md) — 看见 bn128 加 / 乘 / 配对降价 ≠ 已经换了算法；看见更便宜 ≠ 已经在验签；看见本页 ≠ 已经是通用曲线算术；1108 ≠ 2537 ≠ 199 ≠ 196/197 原文（不变量 228）
- [`worked-example-selfbalance-vs-balance.md`](worked-example-selfbalance-vs-balance.md) — 看见本账户余额指令 ≠ 已经是按地址查余额；看见给自己查余额 ≠ 已经按本账户价扣；看见树依赖涨价 ≠ 已经是本笔冷热 / 已经是磁盘 O(1)；1884 ≠ 2929 ≠ 169 ≠ 101 ≠ 150（不变量 229）
- [`worked-example-blake2f-vs-hash.md`](worked-example-blake2f-vs-hash.md) — 看见 BLAKE2 压缩函数 F ≠ 已经是 BLAKE2b 哈希；看见本页 ≠ 已经能验 Equihash / 已经是中继 / 已经有隐私；152 ≠ keccak / SHA3（不变量 230）
- [`worked-example-shift-vs-arithmetic.md`](worked-example-shift-vs-arithmetic.md) — 看见原生移位指令 ≠ 已经用算术拼过移位；看见算术右移 ≠ 已经是有符号除；看见更便宜 ≠ 已经是位域打包产品；145 ≠ 已经改了旧字节码（不变量 231）
- [`worked-example-returndata-vs-memory.md`](worked-example-returndata-vs-memory.md) — 看见返回数据缓冲 ≠ 已经是内存；看见本页 ≠ 已经是 calldata / 已经用两次调用先问长度；看见失败数据能再取 ≠ 已经是 140；下一次类调用 ≠ 缓冲还在（不变量 232）
- [`worked-example-delegatecall-vs-callcode.md`](worked-example-delegatecall-vs-callcode.md) — 看见委托调用 ≠ 已经是 CALLCODE；看见父作用域发送者传到子作用域 ≠ 已经是普通 CALL；看见可变代码源 ≠ 已经是 7702；能塞进调用数据 ≠ 已经是本页（不变量 233）
- [`worked-example-homestead-vs-already-done.md`](worked-example-homestead-vs-already-done.md) — 看见交易创建变贵 ≠ 已经改了 CREATE；看见交易拒高 s ≠ 已经让 ECRECOVER 拒；看见创建失败不再留空合约 ≠ 已经限制代码；看见难度朝均值 ≠ 已经没有炸弹（不变量 234）
- [`worked-example-receipt-status-vs-gas.md`](worked-example-receipt-status-vs-gas.md) — 看见收据状态码 ≠ 已经能从剩余气推断成功；看见本页 ≠ 已经是中间状态根；看见 RPC 能重放 ≠ 收据里已经有状态码（不变量 236）
- [`worked-example-call-63rds-vs-oog.md`](worked-example-call-63rds-vs-oog.md) — 看见读树涨价 ≠ 已经换成去掉六十四分之一；看见问超了 ≠ 已经耗尽气；看见建议气限 ≠ 已经是协议帽（不变量 237）
- [`worked-example-returned-vs-initcode.md`](worked-example-returned-vs-initcode.md) — 创建结束返回的运行时代码超界 ≠ 已经是 initcode 超界；这次失败是耗尽气 ≠ 已经整笔非法；规范 EIP-170 ≠ 不变量 170（不变量 185）
- [`worked-example-reserved-prefix-vs-eof.md`](worked-example-reserved-prefix-vs-eof.md) — 新创建要存上链的代码以保留首字节开头 ≠ 已经是对象格式已经部署；链上已有以该字节开头的代码 ≠ 已经被本页改语义；3541 ≠ EOF 规范 ≠ 170 ≠ 3860（不变量 188）
- [`worked-example-revert-vs-invalid.md`](worked-example-revert-vs-invalid.md) — 带回剩余气的回滚 ≠ 已经烧光剩余气；不够付自己的费 ≠ 已经留下剩余气；140 ≠ 空账户 OOG ≠ 另一条链的 REVERTED（不变量 177）
- [`worked-example-static-vs-view.md`](worked-example-static-vs-view.md) — 静态帧 ≠ 已经是高级语言只读；没转账 ≠ 已经静态；214 ≠ 140（不变量 178）
- [`worked-example-psbt-vs-broadcast.md`](worked-example-psbt-vs-broadcast.md) — 看见部分签名包 ≠ 已经能广播；有几张签 ≠ 已经凑齐；174 ≠ 173 ≠ 125（不变量 179）
- [`worked-example-psbtv2-vs-v0.md`](worked-example-psbtv2-vs-v0.md) — 看见后继版本工作包 ≠ 已经是旧版那份固定未签交易；能再加输入输出 ≠ 已经能广播；370 ≠ 174 ≠ 173 ≠ 125（不变量 186）

平台宽度尺寸检查：[`../failure-museum/cve-2025-46597.md`](../failure-museum/cve-2025-46597.md)（卡住内存池旋钮 ≠ 固定宽度）。  
外层交易上限 ≠ 内层解码已有界：[`../failure-museum/asa-2024-0012.md`](../failure-museum/asa-2024-0012.md)（`max_tx_bytes` 不管 UnpackAny / 内部消息）。  
可选模块 EndBlocker 出错 ≠ 局部失败：[`../failure-museum/isa-2025-002.md`](../failure-museum/isa-2025-002.md)。  
停链交易 ≠ 已停链：[`../failure-museum/x-crisis-no-halt.md`](../failure-museum/x-crisis-no-halt.md)。  
奖励池溢出 ≠ 只是金额：[`../failure-museum/isa-2025-005.md`](../failure-museum/isa-2025-005.md)。  
未初始化被挡账户 ≠ 可归属地址：[`../failure-museum/asa-2024-003.md`](../failure-museum/asa-2024-003.md)。  
Int/Dec ≠ 位宽已齐：[`../failure-museum/asa-2024-010.md`](../failure-museum/asa-2024-010.md)。  
跨链 ack JSON ≠ 已确定：[`../failure-museum/isa-2025-001.md`](../failure-museum/isa-2025-001.md)。  
授权代发 ≠ 内层已认证：[`../failure-museum/elderflower.md`](../failure-museum/elderflower.md)。  
ValidateBasic 读本地钟 ≠ 已确定：[`../failure-museum/jackfruit.md`](../failure-museum/jackfruit.md)。  
「停链」不是一种事故：[`../failure-museum/worked-example-halt-surfaces.md`](../failure-museum/worked-example-halt-surfaces.md)。

课：L1.4 编码、L1.6 随机与确定性、L4.4 ABCI+WAL、L5.3 多客户端同根、L9.3 存储。  
博物馆：BIP 50、CVE-2010-5139、CVE-2018-17144、CVE-2012-2459、CVE-2024-52912、CVE-2024-52913、CVE-2019-25220（含 52916）。屏蔽池可靠性：CVE-2019-7167。  
模式：canonical-encoding、multi-client-determinism。  
反模式：noncanonical-accepted、half-written-state、impl-limit-as-consensus、local-rng-in-apply、authz-sold-as-validated、local-clock-sold-as-validatebasic。
