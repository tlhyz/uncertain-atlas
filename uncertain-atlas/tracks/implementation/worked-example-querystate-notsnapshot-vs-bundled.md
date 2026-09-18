# 例：看见对齐 / 启动握手 / Query 门 is not already already snapshot loaded interchangeable / already genesis replay interchangeable / already Snapshot connection interchangeable

**层次**：实现 / 启动对齐不是已经是快照重放 not already snapshot loaded / not already genesis replay / not already Snapshot connection 正式三事（314 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Info/Query Connection。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「启动对齐不是已经是快照重放 not already snapshot loaded / not already genesis replay / not already Snapshot connection 正式三事（314 余量）/ not 703 querystate-notsnapshot interchangeable / not 314 querystate bundled interchangeable」，不是 QueryState vs ExecuteTxState bundled（314），也不是 Query 连接不是已经是 ExecuteTxState（701 item 1 余量）或上次 Commit 不是已经跟上正在跑的块（702 item 2 余量）。不要另写怎样实现 QueryState 或怎样做 state sync。

## 官方三件事

规范把 Requirements 里这条连接有两个用途——一是让应用回答 CometBFT 从用户那里收到的查询；二是在启动或 state sync 之后，让 CometBFT 和应用对齐——和「已经是对齐就已经装了快照 interchangeable / 已经是启动握手就已经从创世重放 interchangeable / 已经是 Query 门就已经是 Snapshot 连接 interchangeable / 已经是 QueryState vs ExecuteTxState bundled interchangeable」分开写成三件独立的实现事，不是「看见对齐 就已经是快照重放 interchangeable / 就已经从创世重放 interchangeable / 就已经是 Snapshot 连接 interchangeable」一件事：

1. **看见对齐 / 看见启动时对齐 / 看见 state sync 之后对齐 is not already 已经装了快照 interchangeable / 已经 snapshot loaded interchangeable / 已经是快照重放 interchangeable / 314 querystate bundled interchangeable / 38 snapshot interchangeable / querystate-sold-as-execute interchangeable，也不是已经 QueryState vs ExecuteTxState bundled（314） interchangeable / 703 querystate-notsnapshot interchangeable / 314 querystate item 3 interchangeable，也不是已经启动对齐不是已经是快照重放 not already snapshot loaded / not already genesis replay / not already Snapshot connection 正式三事 bundled（314 item 3 余量） interchangeable / 314 querystate item 3 interchangeable，也不是已经 Query 连接不是已经是 ExecuteTxState（701） interchangeable / 702 querystate-notcaughtup interchangeable / 310 commitlock interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：在启动或 state sync 之后，让 CometBFT 和应用对齐。看见对齐，不是已经装了快照 interchangeable——314 钉 bundled 三事，本页从 item 3 侧钉 not already snapshot loaded 单句。看见启动时对齐，不是已经 QueryState vs ExecuteTxState bundled（314） interchangeable——314 钉 bundled，本页钉 item 3 第一件事。看见 state sync 之后对齐，不是已经应用快照已经从创世重放（38） interchangeable——38 另钉，本页钉 Query 门对齐边界。314 querystate vs execute bundled unbundling 在本页 item 3 启动。

2. **看见启动握手 / 看见 Info 握手 / 看见启动对齐握手 is not already 已经从创世重放 interchangeable / 已经 genesis replay interchangeable / 已经创世重放完 interchangeable / 314 querystate bundled interchangeable / 38 snapshot interchangeable，也不是已经 QueryState vs ExecuteTxState bundled（314） interchangeable / 703 querystate-notsnapshot interchangeable / 314 querystate item 1 能查 interchangeable / 314 querystate item 2 跟上 interchangeable，也不是已经启动对齐不是已经是快照重放 not already snapshot loaded / not already genesis replay / not already Snapshot connection 正式三事 bundled（314 item 3 余量） interchangeable / 314 querystate item 3 interchangeable，也不是已经装了快照（本页第一件事） interchangeable。**  
   官方把启动握手和已经从创世重放路径分开——启动握手，不等于已经从创世重放。看见启动握手，不是已经从创世重放 interchangeable——本页钉 not already genesis replay 单句。看见 Info 握手，不是已经 Query 连接不是已经是 ExecuteTxState（701） interchangeable——701 另钉 item 1，本页钉 item 3 第二件事。看见启动对齐握手，不是已经上次 Commit 不是已经跟上正在跑的块（702） interchangeable——702 另钉 item 2，本页钉 item 3 第二件事。314 querystate vs execute bundled unbundling 在本页 item 3 启动。

3. **看见 Query 门 / 看见 Info 或 Query 连接 / 看见 Query 连接用途 is not already 已经是 Snapshot 连接 interchangeable / 已经 Snapshot connection interchangeable / 已经快照连接 interchangeable / 314 querystate bundled interchangeable / 33 four gates interchangeable，也不是已经 QueryState vs ExecuteTxState bundled（314） interchangeable / 703 querystate-notsnapshot interchangeable / 314 querystate item 1 / 314 querystate item 2，也不是已经启动对齐不是已经是快照重放 not already snapshot loaded / not already genesis replay / not already Snapshot connection 正式三事 bundled（314 item 3 余量） interchangeable / 314 querystate item 3 interchangeable，也不是已经装了快照（本页第一件事） interchangeable / 已经从创世重放（本页第二件事） interchangeable。**  
   官方把 Query 门和已经是 Snapshot 连接路径分开——Query 门，不等于已经是 Snapshot 连接。看见 Query 门，不是已经是 Snapshot 连接 interchangeable——本页钉 not already Snapshot connection 单句。看见 Info 或 Query 连接，不是已经装了快照（本页第一件事） interchangeable——三件事分开钉。看见 Query 连接用途，不是已经四门已经结算（33） interchangeable——33 另钉。314 querystate vs execute bundled unbundling 在本页 item 3 完成。

怎样实现 QueryState、怎样做 state sync、怎样写四门是规范里的取值或做法，本页不抄。QueryState vs ExecuteTxState bundled（314）、Query 连接不是已经是 ExecuteTxState（314 item 1 余量 / 701）、上次 Commit 不是已经跟上正在跑的块（314 item 2 余量 / 702）、应用快照已经从创世重放（38）、默认锁已经 RPC 安全（310）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **对齐 not already snapshot loaded ≠ 314 / 38 interchangeable：** 官方把对齐单句和已经装了快照路径分开。
- **启动握手 not already genesis replay ≠ 已经从创世重放 interchangeable：** 官方把启动握手单句和已经从创世重放路径分开。
- **Query 门 not already Snapshot connection ≠ 已经是 Snapshot 连接 interchangeable：** 官方把 Query 门单句和已经是 Snapshot 连接路径分开；314 querystate vs execute bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 对齐 | 不是 already snapshot loaded | 不是能查 alone（701） |
| 启动握手 | 不是 already genesis replay | 不是跟上 alone（702） |
| Query 门 | 不是 already Snapshot connection | 不是快照装完 alone（38） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看启动对齐不是已经是快照重放 not already snapshot loaded / not already genesis replay / not already Snapshot connection 正式三事（314 余量），必须分开对齐 是不是 already snapshot loaded interchangeable / 314 querystate bundled interchangeable / 38 snapshot interchangeable、启动握手 是不是 already genesis replay interchangeable、Query 门 是不是 already Snapshot connection interchangeable。可以跳过「看见对齐就已经是快照重放 interchangeable / 就已经从创世重放 interchangeable / 就已经是 Snapshot 连接 interchangeable」。不要另写怎样做 state sync。314 querystate vs execute bundled unbundling 在本页 item 3 完成（701 + 702 + 703）。

## 本页不抄

- 怎样实现 QueryState、怎样做 state sync、怎样写查询字段。
- QueryState vs ExecuteTxState bundled。那是不变量 314。
- Query 连接不是已经是 ExecuteTxState。那是不变量 314 item 1 余量 / 701。
- 上次 Commit 不是已经跟上正在跑的块。那是不变量 314 item 2 余量 / 702。
- 应用快照已经从创世重放。那是不变量 38。
- 默认锁已经 RPC 安全。那是不变量 310。
- 四门已经结算。那是不变量 33。
