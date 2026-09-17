# 例：看见 Called once upon genesis 不是已经崩溃后再调 InitChain interchangeable；看见 If InitChainResponse.Validators is empty the initial validator set will be InitChainRequest.Validators 不是已经 InitChain 回了空名单就没有集合 interchangeable；看见 If InitChainResponse.Validators is not empty it will be the initial validator set regardless of InitChainRequest.Validators 不是已经应用可以决定接受创世集合 bundled（412）第二件事 interchangeable

**层次**：实现 / InitChain Usage formal三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Called once upon genesis 不是已经崩溃后再调 / Response Validators empty → Request Validators 不是已经空名单就没有集合 / Response Validators not empty → Response regardless of Request 不是已经应用可以决定 bundled interchangeable」，不是 InitChain Usage 余量 bundled 三事（412），也不是 InitChain 回了空名单就已经没有集合（318）。不要另写怎样写 InitChain、怎样决定接受创世集合。

## 官方三件事

规范把 InitChain Usage 前三条核心英文句写成三件独立的实现事，不是「看见 InitChain 了就已经崩溃后再调、已经没有集合、已经改了集合」一件事：

1. **看见 Called once upon genesis / 看见 InitChain 创世时只调一次 不是已经崩溃后第一块 Commit 之前再调 InitChain（320） interchangeable，也不是已经 InitChain Usage 余量 bundled（412）第一件事 bundled 就代表已经交差 interchangeable，也不是已经进程起来就已经过了 genesis_time（303） interchangeable。**  
   官方 Usage 写：Called once upon genesis。看见 called once upon genesis，不是已经第一块 Commit 之前崩了、`InitChain` 会再叫一次那种已经交差 interchangeable——320 钉崩溃恢复三步，本页钉 Methods InitChain Usage 创世只调一次单句。看见 once upon genesis，不是已经 InitChain Usage 余量 bundled（412） interchangeable——412 钉 bundled 三事，本页钉 Usage 单句。看见 genesis 时只调一次，不是已经能跳步 interchangeable。
2. **看见 If `InitChainResponse.Validators` is empty, the initial validator set will be the `InitChainRequest.Validators` / 看见 Response Validators 空就用 Request Validators 不是已经 InitChain 回了空名单就没有集合（318） interchangeable，也不是已经 InitChainResponse.Validators 不是空就无视 Request（第三件事） interchangeable，也不是已经 ValidatorUpdate 用公钥认人就已经改了集合（364） interchangeable。**  
   官方 Usage 写：If `InitChainResponse.Validators` is empty, the initial validator set will be the `InitChainRequest.Validators`。看见 response validators empty → request validators，不是已经 InitChain 回了空名单那种已经没有集合 interchangeable——318 钉空名单语义，本页钉 Usage empty response 规则。看见 will be the InitChainRequest.Validators，不是已经 response 非空就无视 request interchangeable——本页第二、三句配对，第三件事钉 not empty 规则。看见 initial validator set，不是已经 ValidatorUpdate 用公钥认人就已经改了集合 interchangeable——364 钉 ValidatorUpdate 语义，本页钉 Usage empty response 路径。
3. **看见 If `InitChainResponse.Validators` is not empty, it will be the initial validator set (regardless of what is in `InitChainRequest.Validators`) / 看见 Response Validators 非空就用 Response、不管 Request 不是已经 The application can decide to accept the initial validator set bundled（412）第二件事 interchangeable，也不是已经 InitChain 回了空名单就没有集合（318） interchangeable，也不是已经同一批重复公钥就已经能恢复（318 bundled 第二件事） interchangeable。**  
   官方 Usage 写：If `InitChainResponse.Validators` is not empty, it will be the initial validator set (regardless of what is in `InitChainRequest.Validators`)。看见 regardless of InitChainRequest.Validators，不是已经应用 can decide to accept bundled（412 第二件事） interchangeable——412 钉应用可以决定接受或算另一套，本页钉 Usage not empty response 无视 request 规则。看见 not empty → response set，不是已经 empty response 规则 interchangeable——本页第二件事钉 empty 路径。看见 initial validator set regardless of request，不是已经 InitChain 回了空名单 interchangeable——318 钉空名单，本页钉 not empty 路径。

怎样写 InitChain、怎样决定接受创世集合、怎样从空集合更新是规范里的做法，本页不抄。InitChain Usage 余量 bundled（412）、InitChain 回了空名单就已经没有集合（318）、崩溃后第一块 Commit 之前再调 InitChain 就已经交差（320）、ValidatorUpdate 用公钥认人就已经改了集合（364）、Both Request and Response Validators are ValidatorUpdate updating from empty set（412 bundled 第三件事）是另外那套，本页不抄。

## 官方为什么这样拆

- **Called once upon genesis ≠ 崩溃后再调 InitChain：** 官方把 genesis 只调一次和崩溃恢复再调分开。
- **Response Validators empty → Request Validators ≠ 空名单就没有集合：** 官方把 empty response 规则和空名单语义分开。
- **Response Validators not empty → Response regardless of Request ≠ 应用 can decide bundled interchangeable：** 官方把 not empty 无视 request 规则和应用决定接受 bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Called once upon genesis | 不是崩溃后再调 InitChain | 不是 InitChain Usage 余量 bundled（412） |
| Response Validators empty → Request Validators | 不是空名单就没有集合 | 不是 ValidatorUpdate 已经改了集合（364） |
| Response Validators not empty → Response regardless of Request | 不是应用 can decide bundled | 不是 empty response 规则 interchangeable |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage 正式三事，必须分开 Called once upon genesis 是不是崩溃后再调 InitChain interchangeable / 已经交差、Response Validators empty → Request Validators 是不是空名单就没有集合 interchangeable、Response Validators not empty → Response regardless of Request 是不是应用 can decide bundled interchangeable / 已经改了集合。可以跳过「看见 InitChain 了就已经崩溃后再调、已经没有集合」。不要另写怎样写 InitChain。495 initchainusage vs bundled unbundling 完成（695 item 1 / 696 item 2 / 697 item 3）；精读 [`worked-example-initchainusage-notcrash-vs-bundled.md`](worked-example-initchainusage-notcrash-vs-bundled.md)（不变量 695 item 1）。

## 本页不抄

- 怎样写 InitChain、怎样决定接受创世集合、怎样从空集合更新。
- InitChain Usage 余量 bundled。那是不变量 412。
- InitChain 回了空名单就已经没有集合。那是不变量 318。
- 崩溃后第一块 Commit 之前再调 InitChain 就已经交差。那是不变量 320。
- ValidatorUpdate 用公钥认人就已经改了集合。那是不变量 364。
