# 例：看见 Response Validators not empty regardless of Request is not already app can decide bundled interchangeable / not already empty list means no set interchangeable / not already duplicate pubkeys already recoverable interchangeable

**层次**：实现 / InitChain Usage Response Validators not empty regardless of Request not app can decide bundled / not empty list means no set / not duplicate pubkeys already recoverable 正式三事（495 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「InitChain Usage Response Validators not empty regardless of Request not app can decide bundled / not empty list means no set / not duplicate pubkeys already recoverable 正式三事（495 余量）/ not 697 initchainusage-notnonempty interchangeable / not 495 initchainusage-vs-bundled interchangeable」，不是 InitChain Usage 正式三事 bundled（495），也不是应用 can decide bundled（412）或空名单就没有集合（318）。不要另写怎样写 InitChain、怎样决定接受创世集合。

## 官方三件事

规范把 InitChain Usage 里 If InitChainResponse.Validators is not empty, it will be the initial validator set (regardless of what is in InitChainRequest.Validators) 和「已经 The application can decide to accept the initial validator set bundled（412）第二件事 interchangeable / 已经 InitChain 回了空名单就没有集合（318） interchangeable / 已经同一批重复公钥就已经能恢复（318 bundled 第二件事） interchangeable」分开写成三件独立的实现事，不是「看见 not empty 就已经 can decide bundled interchangeable / 就已经没有集合 interchangeable / 就已经能恢复 interchangeable」一件事：

1. **看见 If `InitChainResponse.Validators` is not empty, it will be the initial validator set (regardless of what is in `InitChainRequest.Validators`) / 看见 Response Validators 非空就用 Response、不管 Request / not empty is not already 已经 The application can decide to accept the initial validator set bundled（412）第二件事 interchangeable / 412 initonce interchangeable / 496 initchainusage-decide interchangeable / 已经用了创世文件里的验证者 interchangeable，也不是已经 InitChain Usage 正式三事 bundled（495） interchangeable / 697 initchainusage-notnonempty interchangeable / 695 initchainusage-notcrash interchangeable / 495 initchainusage item 1 once interchangeable，也不是已经 Response Validators not empty regardless of Request not app can decide bundled / not empty list means no set / not duplicate pubkeys already recoverable 正式三事 bundled（495 item 3 余量） interchangeable / 495 initchainusage item 3 interchangeable。**  
   官方 Usage 写：If `InitChainResponse.Validators` is not empty, it will be the initial validator set (regardless of what is in `InitChainRequest.Validators`)。看见 regardless of Request，不是已经应用 can decide bundled interchangeable——412 钉应用可以决定接受或算另一套，本页从 495 item 3 侧钉 not app can decide bundled 单句。495 initchainusage vs bundled unbundling 在本页 item 3 完成。

2. **看见 not empty → Response set / 看见 regardless of Request / 看见 Usage 这句 is not already 已经 InitChain 回了空名单就没有集合（318） interchangeable / 318 emptyset interchangeable / 已经 empty response 规则 interchangeable / 696 initchainusage-notempty interchangeable，也不是已经 InitChain Usage 正式三事 bundled（495） interchangeable / 697 initchainusage-notnonempty interchangeable / 495 initchainusage item 2 empty interchangeable。**  
   官方把 not empty 无视 request 规则和 empty response 规则配对分开写——495 bundled 第三件事常与第二件事混成「看见 not empty 就已经 empty 规则 interchangeable」，本页钉 not empty list means no set 单句。看见 not empty → Response，不是已经 318 interchangeable——318 钉空名单，本页钉 not empty 路径。

3. **看见 initial validator set regardless of request / 看见 not empty / 看见 Usage 这句 is not already 已经同一批重复公钥就已经能恢复（318 bundled 第二件事） interchangeable / 已经重复公钥就已经能恢复 interchangeable，也不是已经 InitChain Usage 正式三事 bundled（495） interchangeable / 697 initchainusage-notnonempty interchangeable / 695 initchainusage-notcrash interchangeable。**  
   官方把 Usage not empty 路径和重复公钥就已经能恢复路径分开——495 bundled 第三件事常与 318 bundled 第二件事混成「看见 regardless of Request 就已经能恢复 interchangeable」，本页钉 not duplicate pubkeys already recoverable 单句。看见 regardless of Request，不是已经改了集合 interchangeable——364 钉 ValidatorUpdate，本页钉 Usage not empty 规则。495 initchainusage vs bundled unbundling 在本页 item 3 完成。

怎样写 InitChain、怎样决定接受创世集合、怎样从空集合更新是规范里的做法，本页不抄。InitChain Usage 正式三事 bundled（495）、Called once upon genesis（495 item 1 余量 / 695）、Response Validators empty（495 item 2 余量 / 696）、应用 can decide（412 / 496）、空名单就没有集合（318）是另外那套，本页不抄。

## 官方为什么这样拆

- **not empty regardless of Request not app can decide bundled ≠ 412 / 496 interchangeable：** 官方把 not empty 无视 request 规则和应用决定接受 bundled 分开。
- **not empty regardless of Request not empty list means no set ≠ 318 interchangeable：** 官方把 not empty 路径和 empty 路径 / 空名单语义分开。
- **not empty regardless of Request not duplicate pubkeys already recoverable ≠ 318 bundled item 2 interchangeable：** 官方把 Usage not empty 路径和重复公钥就已经能恢复路径分开；495 initchainusage vs bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Response Validators not empty regardless of Request | 不是应用 can decide bundled（412 / 496） | 不是 once upon genesis（695/495 item 1） |
| 看见 not empty → Response | 不是空名单就没有集合（318） | 不是 empty → Request（696/495 item 2） |
| 看见 Usage 这句 | 不是重复公钥就已经能恢复 | 不是 ValidatorUpdate 已经改了集合（364） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage Response Validators not empty regardless of Request not app can decide bundled / not empty list means no set / not duplicate pubkeys already recoverable 正式三事（495 余量），必须分开 not empty 是不是应用 can decide bundled interchangeable / 412 / 496、是不是空名单就没有集合 interchangeable / 318、是不是重复公钥就已经能恢复。可以跳过「看见 InitChain 了就已经改了集合」。不要另写怎样写 InitChain。495 initchainusage vs bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 InitChain、怎样决定接受创世集合、怎样从空集合更新。
- InitChain Usage 正式三事 bundled。那是不变量 495。
- Called once upon genesis。那是不变量 495 item 1 余量 / 695。
- Response Validators empty → Request Validators。那是不变量 495 item 2 余量 / 696。
- InitChain Usage 余量 / 应用 can decide。那是不变量 412 / 496。
- InitChain 回了空名单就已经没有集合。那是不变量 318。
