# 例：看见 vote_extension 的签已由 CometBFT 验过、扩展可以空不是已经应用验完 / 已经必须填内容；看见 extension_signature 已由 CometBFT 验过、暴露给应用再处理不是已经应用验完 / 已经 Verify 过；看见扩展启用时两份签都在、没给 non_rp 就签空切片不是已经只有一份签 / 已经没 non_rp 就没有第二份签

**层次**：实现 / ExtendedVoteInfo Usage 暴露签正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「vote_extension 的签已由 CometBFT 验过、扩展可以空不是已经应用验完 / 已经必须填内容 / extension_signature 已由 CometBFT 验过、暴露给应用再处理不是已经应用验完 / 已经 Verify 过 / 扩展启用时两份签都在、没给 non_rp 就签空切片不是已经只有一份签 / 已经没 non_rp 就没有第二份签」，不是 ExtendedVoteInfo 从本进程抽出就已经从块里抽出，也不是 ExtendedVoteInfo.extension_signature 是发送验证者造、CometBFT 验过的扩展签表栏就已经把验过的签交给应用。不要另写怎样写 ExtendedVoteInfo Usage 暴露签正式三事。

## 官方三件事

规范把 `vote_extension` 可以空且签已由 CometBFT 验过、`extension_signature` 暴露给应用再处理、扩展启用时两份签都在且没给 `non_rp` 就签空切片写成三件独立的实现事，不是「看见 Prepare 里有 ExtendedVoteInfo 就已经应用验完、已经必须填内容、已经 Verify 过」一件事：

1. **看见 `vote_extension` 含发送验证者的扩展、签已由 CometBFT 验过 / 看见 can be empty 不是已经应用验完，也不是已经必须填内容。**  
   官方写：`vote_extension` contains the sending validator's vote extension, whose signature was verified by CometBFT. It can be empty. 看见签已由 CometBFT 验过，不是已经应用再验完。看见可以空，不是已经必须填内容。看见有扩展字节，不是已经 VerifyVoteExtension 已经 Accept 那种已经应用验完。
2. **看见 `extension_signature` 是扩展的签、已由 CometBFT 验过 / 看见 expose the signature to the application for further processing or verification 不是已经应用验完，也不是已经 Verify 过。**  
   官方写：`extension_signature` is the signature of the vote extension, which was verified by CometBFT. This way, we expose the signature to the application for further processing or verification. 看见已由 CometBFT 验过，不是已经应用 finished verifying。看见暴露给应用再处理，不是已经 VerifyVoteExtension 已经跑过。看见有签，不是已经按原样签。
3. **看见扩展启用时两份签都会在 / 看见没给 `non_rp_vote_extension` 时 `non_rp_extension_signature` 签空切片 不是已经只有一份签，也不是已经没 non_rp 就没有第二份签。**  
   官方写：Note that the two signatures will be present if vote extensions are enable. If no `non_rp_vote_extension` information was provided, the signature will sign an empty slice. 看见两份签都在，不是已经只有 `extension_signature`。看见签空切片，不是已经没 non_rp 就没有第二份签。看见 optional can be empty，不是已经 optional 就跳过 Verify。

怎样写 ExtendedVoteInfo Usage 暴露签正式三事、怎样再验签、怎样读空切片是规范里的做法，本页不抄。ExtendedVoteInfo 从本进程抽出就已经从块里抽出是不变量 369，本页不抄。

## 官方为什么这样拆

- **签已由 CometBFT 验过、扩展可以空 ≠ 已经应用验完 / 已经必须填内容：** 官方把引擎验签和应用再处理分开。
- **extension_signature 暴露给应用再处理 ≠ 已经应用验完 / 已经 Verify 过：** 官方把 expose for further processing 和已经跑过 Verify 分开。
- **两份签都在、没 non_rp 就签空切片 ≠ 已经只有一份签 / 已经没 non_rp 就没有第二份签：** 官方把两份签都在和 optional 没填分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| vote_extension 签已由 CometBFT 验过、可以空 | 不是已经应用验完 | 不是 ExtendedVoteInfo 从本进程抽出就已经从块里抽出（369） |
| extension_signature 暴露给应用再处理 | 不是已经 Verify 过 | 不是 ExtendedVoteInfo.extension_signature 是发送验证者造、CometBFT 验过的扩展签表栏就已经把验过的签交给应用（421） |
| 两份签都在、没 non_rp 就签空切片 | 不是已经只有一份签 | 不是 ExtendVoteResponse.non_rp_extension 按原样签就已经有重放保护（358） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Prepare 里有 ExtendedVoteInfo 就已经应用验完、已经必须填内容、已经 Verify 过」，必须分开 vote_extension 的签已由 CometBFT 验过、扩展可以空是不是已经应用验完 / 已经必须填内容、extension_signature 已由 CometBFT 验过、暴露给应用再处理是不是已经应用验完 / 已经 Verify 过、扩展启用时两份签都在、没给 non_rp 就签空切片是不是已经只有一份签 / 已经没 non_rp 就没有第二份签。可以跳过「看见 Prepare 里有 ExtendedVoteInfo 就已经应用验完」。447 ExtendedVoteInfo Usage expose signature bundled unbundling 完成（1365 item 1 / 1366 item 2 / 1367 item 3）；精读 [`worked-example-eviuse-notapp-vs-bundled.md`](worked-example-eviuse-notapp-vs-bundled.md)（不变量 1365 item 1）、[`worked-example-eviuse-notexp-vs-bundled.md`](worked-example-eviuse-notexp-vs-bundled.md)（不变量 1366 item 2）、[`worked-example-eviuse-nottwo-vs-bundled.md`](worked-example-eviuse-nottwo-vs-bundled.md)（不变量 1367 item 3）。不要另写怎样写 ExtendedVoteInfo Usage 暴露签正式三事。

## 本页不抄

- 怎样写 ExtendedVoteInfo Usage 暴露签正式三事、怎样再验签、怎样读空切片。
- ExtendedVoteInfo 从本进程抽出就已经从块里抽出。那是不变量 369。
- ExtendedVoteInfo.extension_signature 表栏就已经把验过的签交给应用。那是不变量 421。
- ExtendVoteResponse.non_rp_extension 按原样签就已经有重放保护。那是不变量 358。
