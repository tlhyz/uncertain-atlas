# 例：看见 Code≠0 会拒 / 不会广播 不是已经流言；看见不会进提案块 不是已经 Check 通过就是已进提案；看见 CometBFT attributes no other value 不是已经 Finalize Code≠0 仍在块里

**层次**：实现 / CheckTx Usage Code≠0 rejected 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Code≠0 会拒 / 不会广播 不是已经流言 / CheckTx 守卫 bundled interchangeable、不会进提案块 不是已经 Check 通过就是已进提案 / CheckTx 过了就永远有效、CometBFT attributes no other value 不是已经 Finalize Code≠0 仍在块里 / CheckTx 回包 Data 已被引擎用了」，不是 CheckTx Usage validate-no-apply bundled（486），也不是 CheckTx 技术上可选 bundled（373）。不要另写怎样挑回包码、怎样写广播谓词。

## 官方三件事

规范把 CheckTx Usage 里 Transactions where `CheckTxResponse.Code != 0` will be rejected … will not be broadcast … or included in a proposal block … CometBFT attributes no other value to the response code，写成三件独立的实现事，不是「看见 CheckTx 回了非零码就已经没进块、已经交差、已经 forever valid」一件事：

1. **看见 Transactions where `CheckTxResponse.Code != 0` will be rejected / 看见 Code≠0 会拒 不是已经进了本地池就开始 P2P 流言 interchangeable，也不是已经 CheckTx 是内存池守卫（405） bundled 就代表 Code 语义已经验完 interchangeable，也不是已经 RPC `broadcast_tx` 回了就代表别的节点也会收（301 bundled）。**  
   官方 Usage 写：Transactions where `CheckTxResponse.Code != 0` will be rejected - they will not be broadcast to other nodes。看见 will be rejected，不是已经 ProcessProposal REJECT 就等于池门也拒 interchangeable。看见 Code≠0，不是已经 CheckTx 过了就 forever valid（301） interchangeable——301 钉 mempool 交接，本页钉 Usage Code 拒路径。看见 rejected，不是已经 CheckTx 是内存池守卫（405） bundled 第一句 interchangeable——405 钉 guard 语境，本页钉 Code≠0 拒语义。
2. **看见 they will not be broadcast to other nodes / or included in a proposal block / 看见不会广播、也不会进提案块 不是已经 Check 通过就是已进提案（33） interchangeable，也不是已经 CheckTx 过了就永远有效（301），也不是已经 Finalize `Code ≠ 0` 那种仍在块里（316）。**  
   官方 Usage 写：… will not be broadcast to other nodes or included in a proposal block。看见 will not be broadcast，不是已经别的节点已经从邻居收到 interchangeable。看见 or included in a proposal block，不是已经 Check 通过就是已进提案（33） interchangeable——33 钉四门分开，本页钉 Usage Code 拒路径。看见不会进提案块，不是已经 CheckTx 过了就 forever valid（301） interchangeable。看见 Code 非零，不是已经 Finalize `ExecTxResult.Code ≠ 0` 仍在块里（316） interchangeable——316 钉 Finalize 回执，本页钉 CheckTx 池门。
3. **看见 CometBFT attributes no other value to the response code / 看见引擎对 CheckTx 回包码不再赋予别的含义 不是已经 CheckTx 回包 `Data` 就被引擎用了（317），也不是已经 CheckTx 技术上可选（373） bundled 第二句 interchangeable，也不是已经 CheckTx Usage validate-no-apply（486） bundled 第三件事 interchangeable。**  
   官方 Usage 写：CometBFT attributes no other value to the response code。看见 no other value，不是已经 CheckTx 回包 `Data` 就被引擎用了（317） interchangeable。看见 attributes no other value，不是已经 CheckTx 技术上可选（373） bundled 就代表 Code 语义已经交差 interchangeable——373 钉 optional vs block processing，本页钉 Usage Code 语义。看见 response code，不是已经 Finalize `tx_results[i].Code == 0` only if fully valid（464） interchangeable。看见 Usage 这句，不是已经 validate-no-apply（486） bundled 第三件事 interchangeable——486 钉 validate-no-apply 全段，本页钉 Code≠0 拒路径。

怎样做广播过滤、怎样写 CheckTx 回包码、怎样区分池门 Code 与 Finalize Code 是规范里的做法，本页不抄。CheckTx 技术上可选（373）、CheckTx Usage validate-no-apply（486）、CheckTx 是内存池守卫（405）是另外那套，本页不抄。

## 官方为什么这样拆

- **Code≠0 will be rejected / will not be broadcast ≠ 已经流言 / CheckTx 守卫 bundled interchangeable：** 官方把 Methods Usage Code 拒路径和 mempool guard / 流言广播分开。
- **will not be included in a proposal block ≠ Check 通过就是已进提案 / forever valid / Finalize Code≠0 仍在块里：** 官方把 CheckTx 池门 Code 语义和四门结算、Finalize 回执分开。
- **CometBFT attributes no other value ≠ CheckTx Data 已被引擎用了 / optional bundled / validate-no-apply bundled interchangeable：** 官方把 Usage Code 语义和回包 Data、optional、validate-no-apply 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Code≠0 will be rejected / will not be broadcast | 不是已经流言 | 不是 CheckTx 守卫 bundled（405） |
| will not be included in a proposal block | 不是 Check 通过就是已进提案 | 不是 Finalize Code≠0 仍在块里（316） |
| CometBFT attributes no other value | 不是 CheckTx Data 已被引擎用了 | 不是 validate-no-apply bundled（486） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 CheckTx 回了非零码就已经没进块、已经交差、已经 forever valid」，必须分开 Code≠0 会拒 / 不会广播 是不是已经流言 / CheckTx 守卫 bundled interchangeable、不会进提案块 是不是 Check 通过就是已进提案 / CheckTx 过了就 forever valid / Finalize Code≠0 仍在块里 interchangeable、CometBFT attributes no other value 是不是 CheckTx Data 已被引擎用了 / optional bundled / validate-no-apply bundled interchangeable。可以跳过「看见 CheckTx 回了非零码就已经没进块」。不要另写怎样挑回包码。489 chktxcodereject vs proposal bundled unbundling 完成（686 item 1 / 687 item 2 / 688 item 3）；精读 [`worked-example-chktxcodereject-notgossip-vs-bundled.md`](worked-example-chktxcodereject-notgossip-vs-bundled.md)（不变量 686 item 1）。

## 本页不抄

- 怎样做广播过滤、怎样写 CheckTx 回包码、怎样区分池门 Code 与 Finalize Code。
- CheckTx 技术上可选、不参与处理块。那是不变量 373。
- CheckTx Usage validate-no-apply / Technically optional bundled。那是不变量 486。
- CheckTx 是内存池守卫。那是不变量 405。
- Check 通过就是已进提案。那是不变量 33。
- 提案收了 / CheckTx 过了就 forever valid。那是不变量 301。
- Finalize `Code ≠ 0` 仍在块里。那是不变量 316。
- CheckTx 回包 `Data` 已被引擎用了。那是不变量 317。
