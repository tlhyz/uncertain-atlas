# 例：看见 id 绿了 / 看见公钥地址对上 / 看见拒连 is not already already addr-passed interchangeable / already can-interact interchangeable / already persistent-ban interchangeable

**层次**：实现 / id 过滤查询绿了不是已经过了 addr not already addr-passed / not already can-interact / not already persistent-ban 正式三事（326 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Peer Filtering、Paths。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「id 过滤查询绿了不是已经过了 addr not already addr-passed / not already can-interact / not already persistent-ban 正式三事（326 余量）/ not 735 peerfilter-notaddrpassed interchangeable / not 326 peerfilter bundled interchangeable」，不是 Peer Filtering bundled（326），也不是发了 addr 过滤查询不是已经收下这个人（734 item 1 余量）或有 /store 路径不是已经是引擎在用（736 item 3 余量）。不要另写怎样写过滤或怎样配路径。

## 官方三件事

规范把 Requirements 里第二道 `/p2p/filter/id/`、任意一道非零码就拒连 和「已经是 id 绿了就已经过了 addr interchangeable / 已经是公钥地址对上就已经能交互 interchangeable / 已经是拒连就已经写进持久封禁表 interchangeable / 已经是 Peer Filtering bundled interchangeable」分开写成三件独立的实现事，不是「看见 id 过滤查询绿了就已经过了 addr interchangeable / 就已经能交互 interchangeable / 就已经写进持久封禁表 interchangeable」一件事：

1. **看见 id 绿了 / 看见发了 `/p2p/filter/id` 绿了 / 看见第二道绿了 is not already 已经过了 addr 那一道 interchangeable / 已经 addr-passed interchangeable / 已经 addr 也绿交差 interchangeable / 326 peerfilter bundled interchangeable / 33 four gates interchangeable / peerfilter-sold-as-connected interchangeable，也不是已经 Peer Filtering bundled（326） interchangeable / 735 peerfilter-notaddrpassed interchangeable / 326 peerfilter item 2 interchangeable，也不是已经 id 过滤查询绿了不是已经过了 addr not already addr-passed / not already can-interact / not already persistent-ban 正式三事 bundled（326 item 2 余量） interchangeable / 326 peerfilter item 2 interchangeable，也不是已经发了 addr 不是已经收下（734） interchangeable / 736 peerfilter-notenginepath interchangeable / 305 initpeer interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：第二道是 `/p2p/filter/id/`；看见 id 绿了，不是 addr 已经绿。看见 id 绿了，不是已经 addr-passed interchangeable——326 钉 bundled 三事，本页从 item 2 侧钉 not already addr-passed 单句。看见发了 `/p2p/filter/id` 绿了，不是已经 Peer Filtering bundled（326） interchangeable——326 钉 bundled，本页钉 item 2 第一件事。看见第二道绿了，不是已经发了 addr 不是已经收下（734） interchangeable——734 另钉 item 1。326 peerfilter vs query bundled unbundling 在本页 item 2 续。

2. **看见公钥地址对上 / 看见对端公钥 Address 对上 / 看见节点 ID 对上 is not already 已经能交互 interchangeable / 已经 can-interact interchangeable / 已经 InitPeer 交互交差 interchangeable / 326 peerfilter bundled interchangeable / 305 initpeer interchangeable，也不是已经 Peer Filtering bundled（326） interchangeable / 735 peerfilter-notaddrpassed interchangeable / 326 peerfilter item 1 addr interchangeable / 326 peerfilter item 3 路径 interchangeable，也不是已经 id 过滤查询绿了不是已经过了 addr not already addr-passed / not already can-interact / not already persistent-ban 正式三事 bundled（326 item 2 余量） interchangeable / 326 peerfilter item 2 interchangeable，也不是已经过了 addr（本页第一件事） interchangeable。**  
   官方写：第二道跟对等节点 ID（对端公钥的 `Address()`）；看见公钥地址对上，不是已经能交互。看见公钥地址对上，不是已经 can-interact interchangeable——本页钉 not already can-interact 单句。看见对端公钥 Address 对上，不是已经 InitPeer 已经能交互（305） interchangeable——305 另钉 InitPeer。看见节点 ID 对上，不是已经过了 addr（本页第一件事） interchangeable——三件事分开钉。326 peerfilter vs query bundled unbundling 在本页 item 2 续。

3. **看见拒连 / 看见任意一道非零码 / 看见 CometBFT 拒连 is not already 已经写进持久封禁表 interchangeable / 已经 persistent-ban interchangeable / 已经封禁表交差 interchangeable / 326 peerfilter bundled interchangeable / 50 banlist interchangeable，也不是已经 Peer Filtering bundled（326） interchangeable / 735 peerfilter-notaddrpassed interchangeable / 326 peerfilter item 1 / 326 peerfilter item 3，也不是已经 id 过滤查询绿了不是已经过了 addr not already addr-passed / not already can-interact / not already persistent-ban 正式三事 bundled（326 item 2 余量） interchangeable / 326 peerfilter item 2 interchangeable，也不是已经过了 addr（本页第一件事） interchangeable / 已经能交互（本页第二件事） interchangeable。**  
   官方写：**任意一道**回了非零 ABCI 码，CometBFT **拒连**。看见拒连，不是已经 persistent-ban interchangeable——拒连不等于已经写进持久封禁表。看见任意一道非零码，不是已经自动封禁表已经有界（50） interchangeable——50 另钉封禁表有界。看见 CometBFT 拒连，不是已经能交互（本页第二件事） interchangeable——三件事分开钉。326 peerfilter vs query bundled unbundling 在本页 item 2 完成。

怎样写过滤逻辑、怎样配 Cosmos-SDK Query、怎样拼 IP:端口是规范里的取值或做法，本页不抄。Peer Filtering bundled（326）、发了 addr 过滤查询不是已经收下这个人（326 item 1 余量 / 734）、有 /store 路径不是已经是引擎在用（326 item 3 余量 / 736）、InitPeer 已经能交互（305）、自动封禁表已经有界（50）、QueryState 已经是 ExecuteTxState（314）是另外那套，本页不抄。

## 官方为什么这样拆

- **id 绿了 not already addr-passed ≠ 326 / 33 interchangeable：** 官方把 id 绿了和 addr 已经绿分开。
- **公钥地址对上 not already can-interact ≠ 已经能交互 interchangeable：** 官方把 ID 对上和已经能交互分开。
- **拒连 not already persistent-ban ≠ 已经写进持久封禁表 interchangeable：** 官方把拒连和持久封禁表分开；326 peerfilter vs query bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| id 绿了 | 不是 already addr-passed | 不是 addr 第一道 alone（734） |
| 公钥地址对上 | 不是 already can-interact | 不是 InitPeer alone（305） |
| 拒连 | 不是 already persistent-ban | 不是封禁表有界 alone（50） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 id 过滤查询绿了不是已经过了 addr not already addr-passed / not already can-interact / not already persistent-ban 正式三事（326 余量），必须分开 id 绿了 是不是 already addr-passed interchangeable / 326 peerfilter bundled interchangeable / peerfilter-sold-as-connected interchangeable、公钥地址对上 是不是 already can-interact interchangeable、拒连 是不是 already persistent-ban interchangeable。可以跳过「看见 id 过滤查询绿了就已经过了 addr interchangeable / 就已经能交互 interchangeable / 就已经写进持久封禁表 interchangeable」。不要另写怎样写过滤。326 peerfilter vs query bundled unbundling 在本页 item 2 续（734 + 735）；续 [`worked-example-peerfilter-notenginepath-vs-bundled.md`](worked-example-peerfilter-notenginepath-vs-bundled.md)（不变量 736 item 3）。

## 本页不抄

- 怎样写过滤逻辑、怎样配 Cosmos-SDK Query、怎样拼 IP:端口。
- Peer Filtering bundled。那是不变量 326。
- 发了 addr 过滤查询不是已经收下这个人。那是不变量 326 item 1 余量 / 734。
- 有 /store 路径不是已经是引擎在用。那是不变量 326 item 3 余量 / 736。
- InitPeer 已经能交互。那是不变量 305。
- 自动封禁表已经有界。那是不变量 50。
- QueryState 已经是 ExecuteTxState。那是不变量 314。
