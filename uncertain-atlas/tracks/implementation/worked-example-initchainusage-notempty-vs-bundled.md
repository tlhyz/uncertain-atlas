# 例：看见 Response Validators empty → Request Validators is not already empty list means no set interchangeable / not already not-empty ignores Request interchangeable / not already ValidatorUpdate already changed set interchangeable

**层次**：实现 / InitChain Usage Response Validators empty → Request Validators not empty list means no set / not not-empty ignores Request / not ValidatorUpdate already changed set 正式三事（495 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「InitChain Usage Response Validators empty → Request Validators not empty list means no set / not not-empty ignores Request / not ValidatorUpdate already changed set 正式三事（495 余量）/ not 696 initchainusage-notempty interchangeable / not 495 initchainusage-vs-bundled interchangeable」，不是 InitChain Usage 正式三事 bundled（495），也不是 InitChain 回了空名单就没有集合（318）或 ValidatorUpdate 已经改了集合（364）。不要另写怎样写 InitChain、怎样决定接受创世集合。

## 官方三件事

规范把 InitChain Usage 里 If InitChainResponse.Validators is empty, the initial validator set will be the InitChainRequest.Validators 和「已经 InitChain 回了空名单就没有集合（318） interchangeable / 已经 InitChainResponse.Validators 不是空就无视 Request（第三件事） interchangeable / 已经 ValidatorUpdate 用公钥认人就已经改了集合（364） interchangeable」分开写成三件独立的实现事，不是「看见 empty → Request 就已经没有集合 interchangeable / 就已经 not empty 规则 interchangeable / 就已经改了集合 interchangeable」一件事：

1. **看见 If `InitChainResponse.Validators` is empty, the initial validator set will be the `InitChainRequest.Validators` / 看见 Response Validators 空就用 Request Validators / empty is not already 已经 InitChain 回了空名单就没有集合（318） interchangeable / 318 emptyset interchangeable / 已经没有集合 interchangeable，也不是已经 InitChain Usage 正式三事 bundled（495） interchangeable / 696 initchainusage-notempty interchangeable / 695 initchainusage-notcrash interchangeable / 495 initchainusage item 1 once interchangeable，也不是已经 Response Validators empty → Request Validators not empty list means no set / not not-empty ignores Request / not ValidatorUpdate already changed set 正式三事 bundled（495 item 2 余量） interchangeable / 495 initchainusage item 2 interchangeable。**  
   官方 Usage 写：If `InitChainResponse.Validators` is empty, the initial validator set will be the `InitChainRequest.Validators`。看见 empty → Request，不是已经空名单就没有集合 interchangeable——318 钉空名单语义，本页从 495 item 2 侧钉 not empty list means no set 单句。495 initchainusage vs bundled unbundling 在本页 item 2 续。

2. **看见 Response Validators empty → Request Validators / 看见 will be the InitChainRequest.Validators / 看见 Usage 这句 is not already 已经 InitChainResponse.Validators 不是空就无视 Request（第三件事） interchangeable / 697 initchainusage-notnonempty interchangeable / 已经 not empty 规则 interchangeable，也不是已经 InitChain Usage 正式三事 bundled（495） interchangeable / 696 initchainusage-notempty interchangeable / 495 initchainusage item 3 not empty interchangeable。**  
   官方把 empty response 规则和 not empty 无视 request 规则配对分开写——495 bundled 第二件事常与第三件事混成「看见 empty → Request 就已经 not empty 规则 interchangeable」，本页钉 not not-empty ignores Request 单句。看见 will be the InitChainRequest.Validators，不是已经 response 非空就无视 request interchangeable。

3. **看见 initial validator set / 看见 empty → Request / 看见 Usage 这句 is not already 已经 ValidatorUpdate 用公钥认人就已经改了集合（364） interchangeable / 364 validatorupdate interchangeable / 已经改了集合 interchangeable，也不是已经 InitChain Usage 正式三事 bundled（495） interchangeable / 696 initchainusage-notempty interchangeable / 695 initchainusage-notcrash interchangeable。**  
   官方把 Usage empty response 路径和 ValidatorUpdate 已经改了集合路径分开——495 bundled 第二件事常与 364 混成「看见 initial validator set 就已经改了集合 interchangeable」，本页钉 not ValidatorUpdate already changed set 单句。看见 empty → Request，不是已经 364 interchangeable——364 钉 ValidatorUpdate 语义，本页钉 Usage empty 路径。495 initchainusage vs bundled unbundling 在本页 item 2 续。

怎样写 InitChain、怎样决定接受创世集合、怎样从空集合更新是规范里的做法，本页不抄。InitChain Usage 正式三事 bundled（495）、Called once upon genesis（495 item 1 余量 / 695）、Response Validators not empty（495 item 3 余量 / 697）、空名单就没有集合（318）、ValidatorUpdate 已经改了集合（364）是另外那套，本页不抄。

## 官方为什么这样拆

- **empty → Request not empty list means no set ≠ 318 interchangeable：** 官方把 empty response 规则和空名单语义分开。
- **empty → Request not not-empty ignores Request ≠ 第三件事 interchangeable：** 官方把 empty 路径和 not empty 路径配对分开。
- **empty → Request not ValidatorUpdate already changed set ≠ 364 interchangeable：** 官方把 Usage empty 路径和 ValidatorUpdate 已经改了集合路径分开；495 initchainusage vs bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Response Validators empty → Request Validators | 不是空名单就没有集合（318） | 不是 once upon genesis（695/495 item 1） |
| 看见 will be Request Validators | 不是 not empty 就无视 Request | 不是 ValidatorUpdate 已经改了集合（364） |
| 看见 initial validator set | 不是已经改了集合 | 不是 not empty response（697/495 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage Response Validators empty → Request Validators not empty list means no set / not not-empty ignores Request / not ValidatorUpdate already changed set 正式三事（495 余量），必须分开 empty → Request 是不是空名单就没有集合 interchangeable / 318、是不是 not empty 规则 interchangeable、是不是 ValidatorUpdate 已经改了集合 interchangeable / 364。可以跳过「看见 InitChain 了就已经没有集合」。不要另写怎样写 InitChain。495 initchainusage vs bundled unbundling 在本页 item 2 续；完成 [`worked-example-initchainusage-notnonempty-vs-bundled.md`](worked-example-initchainusage-notnonempty-vs-bundled.md)（不变量 697 item 3）。

## 本页不抄

- 怎样写 InitChain、怎样决定接受创世集合、怎样从空集合更新。
- InitChain Usage 正式三事 bundled。那是不变量 495。
- Called once upon genesis。那是不变量 495 item 1 余量 / 695。
- Response Validators not empty regardless of Request。那是不变量 495 item 3 余量 / 697。
- InitChain 回了空名单就已经没有集合。那是不变量 318。
- ValidatorUpdate 用公钥认人就已经改了集合。那是不变量 364。
