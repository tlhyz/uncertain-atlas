# 横向：实现保证

协议对，两台诚实机器仍可能算出两个世界。  
目的 A：看见「绿勾」时能指出死的是哪一层。  
目的 B：把确定性写成可测句子，而不是「我们写得很小心」。

精读：

- [`worked-example-encoding.md`](worked-example-encoding.md) — 意思一样、字节不一样
- [`worked-example-crash.md`](worked-example-crash.md) — 写到一半断电
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
