# 例：看见 TrySend 回了假 is not already stopped interchangeable / not already same-scale interchangeable / not already delivered interchangeable

**层次**：网络 / TrySend 回假 not already stopped / not already same-scale / not already delivered 正式三事（309 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / send vs enqueued。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「TrySend 回假 not already stopped / not already same-scale / not already delivered 正式三事（309 余量）/ not 1012 sendq-notsame interchangeable / not 309 send-vs-enqueued bundled interchangeable」，不是对等发送 bundled（309），也不是入站配额已经认领 ID（67），也不是 HasChannel 就已经入队（1010）。不要另写怎样入队或怎样编 protobuf。

## 官方三件事

1. **看见 TrySend 回了假 / 看见立刻失败 这份发送 is not already 已经停掉这个人 interchangeable，也不是已经对等发送 bundled（309） interchangeable / 1012 sendq-notsame interchangeable / 1010 sendq-notqueued interchangeable / 309 send item 1 HasChannel interchangeable，也不是已经 TrySend 回假 not already stopped / not already same-scale / not already delivered 正式三事 bundled（309 item 3 余量） interchangeable / 309 send item 3 interchangeable。**  
   官方写：两条发送方法的差别是什么时候回假。TrySend 不阻塞：队列满就立刻回假。看见立刻失败，不是已经停掉这个人 interchangeable——本页从 309 item 3 侧钉 not already stopped 单句。309 send vs enqueued bundled unbundling 在本页 item 3 完成。

2. **看见回了假 / 看见立刻失败 / 这份发送 is not already 已经和 Send 等过同一段时间 interchangeable，也不是已经对等发送 bundled（309） interchangeable / 1012 sendq-notsame interchangeable / 309 send item 2 Send 回假 interchangeable / 1011 sendq-notdisc interchangeable，也不是已经入站配额已经认领 ID interchangeable / 67 inbound quota interchangeable。**  
   官方把立刻回假和阻塞后再回假分开。看见回了假，不是已经和 Send 等过同一段时间 interchangeable。本页钉 not already same-scale 单句。

3. **看见非阻塞 / 看见立刻失败 / 这份发送 is not already 已经送到 interchangeable，也不是已经对等发送 bundled（309） interchangeable / 1012 sendq-notsame interchangeable / 1010 sendq-notqueued interchangeable，也不是已经 HasChannel 就已经入队 interchangeable / 1010 sendq-notqueued interchangeable。**  
   官方把非阻塞和已经送到分开。看见非阻塞，不是已经送到 interchangeable。309 send vs enqueued bundled unbundling 在本页 item 3 完成。

发送超时秒数、通道号、队列容量是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **TrySend 回假 not already stopped ≠ 已经停掉这个人 interchangeable：** 官方把立刻回假和已经停掉这个人分开。
- **看见回了假 not already same-scale ≠ 已经和 Send 等过同一段时间 interchangeable：** 官方把立刻回假和阻塞后再回假分开。
- **看见非阻塞 not already delivered ≠ 已经送到 interchangeable：** 官方把非阻塞和已经送到分开；309 send vs enqueued bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| TrySend 立刻回假 | 不是已经和 Send 同一把尺 | 不是入站配额已经认领 ID（67） |
| 看见回了假 | 不是已经和 Send 等过同一段时间 | 不是 HasChannel 就已经入队（1010） |
| 看见非阻塞 | 不是已经送到 | 不是 Send 回假就已经断开（1011） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 TrySend 回假 not already stopped / not already same-scale / not already delivered 正式三事（309 余量），必须分开是不是已经停掉这个人、是不是已经和 Send 等过同一段时间、是不是已经送到。可以跳过「看见能发就已经入队」。不要另写怎样入队或怎样编 protobuf。309 send vs enqueued bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 发送超时秒数、通道号、队列容量、信封字段表。
- 对等发送 bundled。那是不变量 309。
- 入站配额已经认领 ID。那是不变量 67。
- HasChannel 就已经入队。那是不变量 1010。
