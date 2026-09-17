# 例：看见 ExtendedVoteInfo.validator 是发了这张票的验证者不是已经带了公钥；看见 ExtendedVoteInfo.block_id_flag 标明投了上一块、nil、还是没收到票不是已经罚没；看见 ExtendedVoteInfo.non_rp_extension_signature 是发送验证者造、CometBFT 验过的非重放保护扩展签不是已经把验过的签交给应用

**层次**：实现 / ExtendedVoteInfo 表余栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendedVoteInfo.validator 是发了这张票的验证者不是已经带了公钥 / ExtendedVoteInfo.block_id_flag 标明投了上一块、nil、还是没收到票不是已经罚没 / ExtendedVoteInfo.non_rp_extension_signature 是发送验证者造、CometBFT 验过的非重放保护扩展签不是已经把验过的签交给应用」，不是 ExtendedVoteInfo 从本进程抽出就已经从块里抽出，也不是 ExtendedVoteInfo.extension_signature 是发送验证者造、CometBFT 验过的扩展签就已经把验过的签交给应用。不要另写怎样写 ExtendedVoteInfo 表余栏。

## 官方三件事

规范把 ExtendedVoteInfo 表上 `validator` 是发了这张票的验证者、`block_id_flag` 标明投了上一块、nil、还是没收到票、`non_rp_extension_signature` 是发送验证者造、CometBFT 验过的非重放保护扩展签写成三件独立的实现事，不是「看见填了 ExtendedVoteInfo 表余栏就已经带了公钥、已经罚没、已经把验过的签交给应用」一件事：

1. **看见 `ExtendedVoteInfo.validator` 是发了这张票的验证者 / 看见填了 validator 不是已经带了公钥，也不是已经从本进程抽出。**  
   官方写：`validator` 是发了这张票的验证者。看见填了 validator，不是已经 ExtendedVoteInfo 从本进程的 CometBFT 数据结构抽出那种看见有 `ExtendedVoteInfo.validator` 就已经带了公钥。看见能指发票的人，不是已经 `VoteInfo.validator` 那种已经是 ValidatorUpdate。看见能指人，不是已经交差。
2. **看见 `ExtendedVoteInfo.block_id_flag` 标明投了上一块、nil、还是没收到票 / 看见填了 block_id_flag 不是已经罚没，也不是已经是 VoteInfo 的 block_id_flag。**  
   官方写：`block_id_flag` 标明这个验证者投了上一块、投了 nil、还是票没收到。看见填了 block_id_flag，不是已经 VoteInfo 标明上一块有没有签、能按到场定奖惩那种已经罚没。看见能指没收到，不是已经交差。看见能指 nil，不是已经定奖惩。
3. **看见 `ExtendedVoteInfo.non_rp_extension_signature` 是发送验证者造、CometBFT 验过的非重放保护扩展签 / 看见填了 non_rp_extension_signature 不是已经把验过的签交给应用，也不是已经是 extension_signature。**  
   官方写：`non_rp_extension_signature` 是发送验证者造、CometBFT 验过的非重放保护扩展签。看见填了 non_rp_extension_signature，不是已经 `ExtendedVoteInfo.extension_signature` 是发送验证者造、CometBFT 验过的扩展签那种已经把验过的签交给应用。看见验过了，不是已经有重放保护。看见能指第二份签，不是已经交差。

怎样写 ExtendedVoteInfo 表余栏、怎样填 validator、怎样填 block_id_flag 是规范里的做法，本页不抄。ExtendedVoteInfo 从本进程抽出就已经从块里抽出是不变量 369，本页不抄。

## 官方为什么这样拆

- **ExtendedVoteInfo.validator 是发了这张票的验证者 ≠ 已经带了公钥：** 官方把表上这份发了这张票的验证者和 Usage 里那份从本进程抽出分开。
- **ExtendedVoteInfo.block_id_flag 标明投了上一块、nil、还是没收到票 ≠ 已经罚没：** 官方把表上这份投了上一块、nil、还是没收到票和 VoteInfo 那份按到场定奖惩分开。
- **ExtendedVoteInfo.non_rp_extension_signature 是发送验证者造、CometBFT 验过的非重放保护扩展签 ≠ 已经把验过的签交给应用：** 官方把表上这份非重放保护扩展签和表上那份 `extension_signature` 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendedVoteInfo.validator 是发了这张票的验证者 | 不是已经带了公钥 | 不是 ExtendedVoteInfo 从本进程抽出就已经从块里抽出（369） |
| ExtendedVoteInfo.block_id_flag 标明投了上一块、nil、还是没收到票 | 不是已经罚没 | 不是 VoteInfo 能按到场定奖惩就已经罚没（365） |
| ExtendedVoteInfo.non_rp_extension_signature 是发送验证者造、CometBFT 验过的非重放保护扩展签 | 不是已经把验过的签交给应用 | 不是 ExtendedVoteInfo.extension_signature 是发送验证者造、CometBFT 验过的扩展签就已经把验过的签交给应用（421） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ExtendedVoteInfo 表余栏就已经带了公钥、已经罚没、已经把验过的签交给应用」，必须分开 ExtendedVoteInfo.validator 是发了这张票的验证者是不是已经带了公钥、ExtendedVoteInfo.block_id_flag 标明投了上一块、nil、还是没收到票是不是已经罚没、ExtendedVoteInfo.non_rp_extension_signature 是发送验证者造、CometBFT 验过的非重放保护扩展签是不是已经把验过的签交给应用。可以跳过「看见填了 ExtendedVoteInfo 表余栏就已经带了公钥」。不要另写怎样写 ExtendedVoteInfo 表余栏。

## 本页不抄

- 怎样写 ExtendedVoteInfo 表余栏、怎样填 validator、怎样填 block_id_flag。
- ExtendedVoteInfo 从本进程抽出就已经从块里抽出。那是不变量 369。
- ExtendedVoteInfo.extension_signature 是发送验证者造、CometBFT 验过的扩展签就已经把验过的签交给应用。那是不变量 421。
- VoteInfo 能按到场定奖惩就已经罚没。那是不变量 365。
