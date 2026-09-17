# 例：看见 Called once upon genesis is not already crash-then-InitChain interchangeable / not already InitChain Usage remainder bundled interchangeable / not already process up is past genesis_time interchangeable

**层次**：实现 / InitChain Usage Called once upon genesis not crash then InitChain / not InitChain Usage remainder bundled / not process up is past genesis_time 正式三事（495 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「InitChain Usage Called once upon genesis not crash then InitChain / not InitChain Usage remainder bundled / not process up is past genesis_time 正式三事（495 余量）/ not 695 initchainusage-notcrash interchangeable / not 495 initchainusage-vs-bundled interchangeable」，不是 InitChain Usage 正式三事 bundled（495），也不是崩溃恢复三步（320）或 InitChain Usage 余量（412）。不要另写怎样写 InitChain、怎样决定接受创世集合。

## 官方三件事

规范把 InitChain Usage 里 Called once upon genesis 和「已经崩溃后第一块 Commit 之前再调 InitChain（320） interchangeable / 已经 InitChain Usage 余量 bundled（412）第一件事 bundled 就代表已经交差 interchangeable / 已经进程起来就已经过了 genesis_time（303） interchangeable」分开写成三件独立的实现事，不是「看见 once upon genesis 就已经崩溃后再调 interchangeable / 就已经 412 bundled interchangeable / 就已经过了 genesis_time interchangeable」一件事：

1. **看见 Called once upon genesis / 看见 InitChain 创世时只调一次 / once is not already 已经崩溃后第一块 Commit 之前再调 InitChain（320） interchangeable / 320 crash interchangeable / 已经交差 interchangeable，也不是已经 InitChain Usage 正式三事 bundled（495） interchangeable / 695 initchainusage-notcrash interchangeable / 696 initchainusage-notempty interchangeable / 495 initchainusage item 2 empty response interchangeable，也不是已经 Called once upon genesis not crash then InitChain / not InitChain Usage remainder bundled / not process up is past genesis_time 正式三事 bundled（495 item 1 余量） interchangeable / 495 initchainusage item 1 interchangeable。**  
   官方 Usage 写：Called once upon genesis。看见 once upon genesis，不是已经崩溃后再调 interchangeable——320 钉崩溃恢复三步，本页从 495 item 1 侧钉 not crash 单句。495 initchainusage vs bundled unbundling 在本页 item 1 启动。

2. **看见 Called once upon genesis / 看见创世时只调一次 / 看见 Usage 这句 is not already 已经 InitChain Usage 余量 bundled（412）第一件事 bundled 就代表已经交差 interchangeable / 412 initonce interchangeable / 已经余量 bundled 就等于 Usage 单句已经验完 interchangeable，也不是已经 InitChain Usage 正式三事 bundled（495） interchangeable / 695 initchainusage-notcrash interchangeable / 495 initchainusage item 3 not empty interchangeable / 697 initchainusage-notnonempty interchangeable。**  
   官方把 Usage once upon genesis 单句和 412 余量 bundled 第一件事分开——495 bundled 第一件事常与 412 混成「看见 once 就已经 412 bundled interchangeable」，本页钉 not InitChain Usage remainder bundled 单句。看见 once upon genesis，不是已经能跳步 interchangeable。

3. **看见 Called once upon genesis / 看见 Usage 这句 / 看见创世时只调一次 is not already 已经进程起来就已经过了 genesis_time（303） interchangeable / 303 genesis interchangeable / 已经节点起来就等于已经过了 genesis_time interchangeable，也不是已经 InitChain Usage 正式三事 bundled（495） interchangeable / 695 initchainusage-notcrash interchangeable / 696 initchainusage-notempty interchangeable。**  
   官方把 Usage once upon genesis 单句和进程起来就已经过了 genesis_time 路径分开——495 bundled 第一件事常与 303 混成「看见 genesis 时只调一次 就已经过了 genesis_time interchangeable」，本页钉 not process up is past genesis_time 单句。看见 Usage 这句，不是已经 303 interchangeable——303 钉创世字段，本页钉 Usage once 单句。495 initchainusage vs bundled unbundling 在本页 item 1 启动。

怎样写 InitChain、怎样决定接受创世集合、怎样从空集合更新是规范里的做法，本页不抄。InitChain Usage 正式三事 bundled（495）、Response Validators empty（495 item 2 余量 / 696）、Response Validators not empty（495 item 3 余量 / 697）、崩溃恢复三步（320）、InitChain Usage 余量（412）是另外那套，本页不抄。

## 官方为什么这样拆

- **once upon genesis not crash then InitChain ≠ 320 interchangeable：** 官方把 genesis 只调一次和崩溃恢复再调分开。
- **once upon genesis not InitChain Usage remainder bundled ≠ 412 interchangeable：** 官方把 Usage once 单句和 412 余量 bundled 第一件事分开。
- **once upon genesis not process up is past genesis_time ≠ 303 interchangeable：** 官方把 Usage once 单句和进程起来就已经过了 genesis_time 路径分开；495 initchainusage vs bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Called once upon genesis | 不是崩溃后再调 InitChain（320） | 不是 empty response（696/495 item 2） |
| 看见创世时只调一次 | 不是 InitChain Usage 余量 bundled（412） | 不是 InitChain Usage 正式三事 bundled（495） |
| 看见 Usage 这句 | 不是进程起来就已经过了 genesis_time（303） | 不是 not empty response（697/495 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage Called once upon genesis not crash then InitChain / not InitChain Usage remainder bundled / not process up is past genesis_time 正式三事（495 余量），必须分开 once 是不是崩溃后再调 interchangeable / 320、是不是 412 bundled interchangeable、是不是进程起来就已经过了 genesis_time interchangeable / 303。可以跳过「看见 InitChain 了就已经崩溃后再调」。不要另写怎样写 InitChain。495 initchainusage vs bundled unbundling 在本页 item 1 启动；续 [`worked-example-initchainusage-notempty-vs-bundled.md`](worked-example-initchainusage-notempty-vs-bundled.md)（不变量 696 item 2）。

## 本页不抄

- 怎样写 InitChain、怎样决定接受创世集合、怎样从空集合更新。
- InitChain Usage 正式三事 bundled。那是不变量 495。
- Response Validators empty → Request Validators。那是不变量 495 item 2 余量 / 696。
- Response Validators not empty regardless of Request。那是不变量 495 item 3 余量 / 697。
- 崩溃后第一块 Commit 之前再调 InitChain。那是不变量 320。
- InitChain Usage 余量 bundled。那是不变量 412。
