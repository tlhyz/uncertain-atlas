# 例：看见 id 过滤查询绿了 is not already past-addr interchangeable / not already interactive interchangeable / not already settled interchangeable

**层次**：实现 / id 过滤查询绿了 not already past-addr / not already interactive / not already settled 正式三事（326 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Peer Filtering、Paths。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「id 过滤查询绿了 not already past-addr / not already interactive / not already settled 正式三事（326 余量）/ not 945 peerfilter-notaddr interchangeable / not 326 peerfilter-vs-query bundled interchangeable」，不是过滤 bundled（326），也不是自动封禁表已经有界（50），也不是封禁就已经没有快照 DoS（332/937）。不要另写怎样写过滤或怎样配路径。

## 官方三件事

1. **看见发了 /p2p/filter/id / 看见公钥地址对上 这份查询 is not already 已经过了 addr 那一道 interchangeable，也不是已经过滤 bundled（326） interchangeable / 945 peerfilter-notaddr interchangeable / 944 peerfilter-notaccept interchangeable / 326 peerfilter item 1 addr interchangeable，也不是已经 id 过滤查询绿了 not already past-addr / not already interactive / not already settled 正式三事 bundled（326 item 2 余量） interchangeable / 326 peerfilter item 2 interchangeable。**  
   官方写：第二道是 /p2p/filter/id/，后面跟对等节点 ID（也就是对端公钥的 Address()）。任意一道回了非零 ABCI 码，CometBFT 拒连。看见 id 绿了，不是 addr 已经绿 interchangeable——本页从 326 item 2 侧钉 not already past-addr 单句。326 peerfilter vs query bundled unbundling 在本页 item 2 续。

2. **看见公钥地址对上 / 看见拒连 / 这份查询 is not already 已经能交互 interchangeable，也不是已经过滤 bundled（326） interchangeable / 945 peerfilter-notaddr interchangeable / 326 peerfilter item 3 /store interchangeable / 946 peerfilter-notstore interchangeable，也不是已经自动封禁表已经有界 interchangeable / 50 ban-table interchangeable。**  
   官方把公钥地址对上和已经能交互分开——326 bundled 第二件事常与 50 混成「看见 id 绿了就已经过了 addr 或已经写进封禁表 interchangeable」，本页钉 not already interactive 单句。

3. **看见拒连 / 看见 id 绿了 / 这份查询 is not already 已经交差 interchangeable，也不是已经过滤 bundled（326） interchangeable / 945 peerfilter-notaddr interchangeable / 944 peerfilter-notaccept interchangeable，也不是已经封禁就已经没有快照 DoS interchangeable / 332/937 snapshot-verify-notdos interchangeable。**  
   官方把拒连和已经写进持久封禁表 / 已经交差分开。看见拒连，不是已经交差 interchangeable。326 peerfilter vs query bundled unbundling 在本页 item 2 续。

怎样写过滤逻辑、怎样配 Cosmos-SDK Query、怎样拼 IP:端口是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **id 过滤查询绿了 not already past-addr ≠ 已经过了 addr interchangeable：** 官方把地址过滤和节点 ID 过滤写成两道独立查询。
- **看见公钥地址对上 not already interactive ≠ 已经能交互 interchangeable：** 官方把公钥地址对上和已经能交互分开。
- **看见拒连 not already settled ≠ 已经交差 interchangeable：** 官方把拒连和已经写进持久封禁表分开；326 peerfilter vs query bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| id 过滤查询绿了 | 不是已经过了 addr | 不是自动封禁表已经有界（50） |
| 看见公钥地址对上 | 不是已经能交互 | 不是封禁就已经没有快照 DoS（332/937） |
| 看见拒连 | 不是已经交差 | 不是发了 addr 就已经收下（944） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 id 过滤查询绿了 not already past-addr / not already interactive / not already settled 正式三事（326 余量），必须分开是不是已经过了 addr、是不是已经能交互、是不是已经交差。可以跳过「看见 id 绿了就已经过了两道」。不要另写怎样写过滤或怎样配路径。326 peerfilter vs query bundled unbundling 在本页 item 2 续；续 [`worked-example-peerfilter-notstore-vs-bundled.md`](worked-example-peerfilter-notstore-vs-bundled.md)（不变量 946 item 3）。

## 本页不抄

- 怎样写过滤逻辑、怎样配 Cosmos-SDK Query、怎样拼 IP:端口。
- 过滤 bundled。那是不变量 326。
- 发了 addr 就已经收下。那是不变量 326 item 1 余量 / 944。
- 自动封禁表已经有界。那是不变量 50。
- 封禁就已经没有快照 DoS。那是不变量 332/937。
