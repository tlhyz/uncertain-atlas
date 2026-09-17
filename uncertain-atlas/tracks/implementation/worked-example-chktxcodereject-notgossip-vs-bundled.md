# 例：看见 CheckTx Code≠0 will be rejected is not already in-pool gossip interchangeable / not already CheckTx guard bundled interchangeable / not already broadcast_tx received interchangeable

**层次**：实现 / CheckTx Usage Code≠0 rejected not in-pool gossip / not CheckTx guard bundled / not broadcast_tx received 正式三事（489 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx Usage Code≠0 rejected not in-pool gossip / not CheckTx guard bundled / not broadcast_tx received 正式三事（489 余量）/ not 686 chktxcodereject-notgossip interchangeable / not 489 chktxcodereject-vs-proposal bundled interchangeable」，不是 CheckTx Usage Code≠0 rejected 正式三事 bundled（489），也不是 CheckTx 守卫余量（405）或 Replay Protection（301）。不要另写怎样挑回包码、怎样写广播谓词。

## 官方三件事

规范把 CheckTx Usage 里 Transactions where `CheckTxResponse.Code != 0` will be rejected 和「已经进了本地池就开始 P2P 流言 interchangeable / 已经 CheckTx 是内存池守卫（405） bundled 就代表 Code 语义已经验完 interchangeable / 已经 RPC `broadcast_tx` 回了就代表别的节点也会收（301 bundled） interchangeable」分开写成三件独立的实现事，不是「看见 Code≠0 会拒 就已经 gossip interchangeable / 就已经 guard bundled interchangeable / 就已经 broadcast_tx received interchangeable」一件事：

1. **看见 Transactions where `CheckTxResponse.Code != 0` will be rejected / 看见 Code≠0 会拒 / will be rejected is not already 已经进了本地池就开始 P2P 流言 interchangeable / 已经 ProcessProposal REJECT 就等于池门也拒 interchangeable / 已经流言出去 interchangeable，也不是已经 CheckTx Usage Code≠0 rejected 正式三事 bundled（489） interchangeable / 686 chktxcodereject-notgossip interchangeable / 687 chktxcodereject-notproposal interchangeable / 489 chktxcodereject item 2 not in proposal interchangeable，也不是已经 Code≠0 rejected not in-pool gossip / not CheckTx guard bundled / not broadcast_tx received 正式三事 bundled（489 item 1 余量） interchangeable / 489 chktxcodereject item 1 interchangeable。**  
   官方 Usage 写：Transactions where `CheckTxResponse.Code != 0` will be rejected - they will not be broadcast to other nodes。看见 will be rejected，不是已经进了本地池就开始 P2P 流言 interchangeable。489 chktxcodereject vs proposal bundled unbundling 在本页 item 1 启动。

2. **看见 Code≠0 will be rejected / 看见会拒 / 看见 Code≠0 is not already 已经 CheckTx 是内存池守卫（405） bundled 就代表 Code 语义已经验完 interchangeable / 405 checktxguard interchangeable / 已经 Guardian 第一句 interchangeable / 已经每条节点先跑 CheckTx 才进本地池 interchangeable，也不是已经 CheckTx Usage Code≠0 rejected 正式三事 bundled（489） interchangeable / 686 chktxcodereject-notgossip interchangeable / 489 chktxcodereject item 3 no other value interchangeable / 688 chktxcodereject-notothervalue interchangeable。**  
   官方把 Usage Code≠0 拒路径和守卫 bundled 路径分开——489 bundled 第一件事常与 405 混成「看见会拒 就已经守卫 bundled 就代表 Code 语义验完 interchangeable」，本页钉 not CheckTx guard bundled 单句。看见 rejected，不是已经 Guardian 就已经交差 interchangeable——405 钉守卫余量，本页钉 Usage Code 拒。

3. **看见 Code≠0 will be rejected / 看见会拒 / 看见 rejected is not already 已经 RPC `broadcast_tx` 回了就代表别的节点也会收（301 bundled） interchangeable / 301 proposed-vs-removed interchangeable / 已经别的节点已经从邻居收到 interchangeable / 已经 CheckTx 过了就永远有效 interchangeable，也不是已经 CheckTx Usage Code≠0 rejected 正式三事 bundled（489） interchangeable / 686 chktxcodereject-notgossip interchangeable / 687 chktxcodereject-notproposal interchangeable。**  
   官方把 Usage Code≠0 拒路径和 broadcast_tx 别人也会收路径分开——489 bundled 第一件事常与 301 混成「看见会拒 就已经别人也会收 interchangeable」，本页钉 not broadcast_tx received 单句。看见 Code≠0，不是已经 CheckTx 过了就 forever valid interchangeable——301 钉 mempool 交接，本页钉 Usage item 1。489 chktxcodereject vs proposal bundled unbundling 在本页 item 1 启动。

怎样做广播过滤、怎样写 CheckTx 回包码、怎样区分池门 Code 与 Finalize Code 是规范里的做法，本页不抄。CheckTx Usage Code≠0 rejected 正式三事 bundled（489）、will not be included in a proposal block（489 item 2 余量 / 687）、no other value to the response code（489 item 3 余量 / 688）、CheckTx 守卫余量（405）、提案收了（301）是另外那套，本页不抄。

## 官方为什么这样拆

- **Code≠0 rejected not in-pool gossip ≠ 已经流言 interchangeable：** 官方把 Methods Usage Code 拒和进池就开始流言路径分开。
- **Code≠0 rejected not CheckTx guard bundled ≠ 405 checktxguard interchangeable：** 官方把 Usage Code 拒单句和守卫 bundled 就代表 Code 语义验完路径分开。
- **Code≠0 rejected not broadcast_tx received ≠ 301 bundled interchangeable：** 官方把 Usage Code 拒单句和 RPC 回了别人也会收路径分开；489 chktxcodereject vs proposal bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Code≠0 will be rejected | 不是已经进池就开始流言 | 不是 will not be in proposal（687/489 item 2） |
| 看见会拒 | 不是守卫 bundled 就代表 Code 验完（405） | 不是 CheckTx Usage Guardian（490） |
| 看见 rejected | 不是 broadcast_tx 别人也会收（301） | 不是 no other value（688/489 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage Code≠0 rejected not in-pool gossip / not CheckTx guard bundled / not broadcast_tx received 正式三事（489 余量），必须分开 Code≠0 会拒 是不是已经流言 interchangeable、是不是守卫 bundled interchangeable / 405、是不是 broadcast_tx 别人也会收 interchangeable / 301。可以跳过「看见 CheckTx 回了非零码就已经流言出去」。不要另写怎样挑回包码。489 chktxcodereject vs proposal bundled unbundling 在本页 item 1 启动；续 [`worked-example-chktxcodereject-notproposal-vs-bundled.md`](worked-example-chktxcodereject-notproposal-vs-bundled.md)（不变量 687 item 2）。

## 本页不抄

- 怎样做广播过滤、怎样写 CheckTx 回包码、怎样区分池门 Code 与 Finalize Code。
- CheckTx Usage Code≠0 rejected 正式三事 bundled。那是不变量 489。
- will not be included in a proposal block。那是不变量 489 item 2 余量 / 687。
- no other value to the response code。那是不变量 489 item 3 余量 / 688。
- CheckTx 是内存池守卫。那是不变量 405。
- 提案收了 / CheckTx 过了就永远有效。那是不变量 301。
