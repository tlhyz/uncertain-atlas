# 例：看见 ExtendVoteResponse.vote_extension 只会挂在非 nil Precommit 上、precommit nil 不会叫 ExtendVote 不是已经会调 ExtendVote；看见应用可以选 0 长扩展不是已经不会叫 ExtendVote；看见造扩展的应用逻辑可以非确定不是已经必须同一份扩展

**层次**：实现 / ExtendVote Usage 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVoteResponse.vote_extension 只会挂在非 nil Precommit 上、precommit nil 不会叫 ExtendVote 不是已经会调 ExtendVote / 应用可以选 0 长扩展不是已经不会叫 ExtendVote / 造扩展的应用逻辑可以非确定不是已经必须同一份扩展」，不是一轮只能交出一份扩展就已经是每一高度一份，也不是空扩展仍会调 Verify 就已经跳过 Verify。不要另写怎样写 ExtendVote Usage 正式三事。

## 官方三件事

规范把 vote_extension 只挂非 nil Precommit、应用可以选 0 长扩展、造扩展逻辑可以非确定写成三件独立的实现事，不是「看见填了 ExtendVote Usage 就已经会调 ExtendVote、已经不会叫、已经必须同一份扩展」一件事：

1. **看见 `ExtendVoteResponse.vote_extension` 只会挂在非 nil Precommit 上 / 看见 precommit nil 不会叫 ExtendVote 不是已经会调 ExtendVote，也不是已经签了 nil 票仍带扩展。**  
   官方写：`ExtendVoteResponse.vote_extension` 只会挂在非 nil Precommit 上。若共识算法要 precommit nil，就不会叫 `ExtendVote`。When 也写：要广播 precommit nil（收到 +2/3 prevote nil，或 `timeoutPrevote`）时，CometBFT 不会叫 `ExtendVote`，nil 票也不带 `CanonicalVoteExtension`。看见 precommit nil，不是已经会调。看见不会叫，不是已经带了扩展。
2. **看见应用可以选 0 长扩展 / 看见能空 不是已经不会叫 ExtendVote，也不是已经跳过 Verify。**  
   官方写：应用可以选 0 长 vote extension。看见能空，不是已经不会叫 ExtendVote。看见选了空，不是已经跳过 Verify 那种已经不用验。看见仍会叫 ExtendVote，不是已经必须填内容。
3. **看见造扩展的应用逻辑可以非确定 / 看见可以非确定 不是已经必须同一份扩展，也不是已经是 ExtendVote 没有确定性要求那种已经是同一块。**  
   官方写：造扩展的应用逻辑可以非确定。看见可以非确定，不是已经必须同一份扩展。看见逻辑可以变，不是已经是同一块就一定是同一份。看见没有这道必须确定，不是已经 Verify 必须确定。

怎样写 ExtendVote Usage 正式三事、怎样选空扩展、怎样写非确定逻辑是规范里的做法，本页不抄。一轮只能交出一份扩展就已经是每一高度一份是不变量 350，本页不抄。

## 官方为什么这样拆

- **vote_extension 只挂非 nil Precommit / precommit nil 不会叫 ExtendVote ≠ 已经会调 ExtendVote：** 官方把 nil 票不调 ExtendVote 和已经会调分开。
- **应用可以选 0 长扩展 ≠ 已经不会叫 ExtendVote：** 官方把能空和已经跳过 Verify 分开。
- **造扩展的应用逻辑可以非确定 ≠ 已经必须同一份扩展：** 官方把可以非确定和已经是同一块就同一份分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| vote_extension 只挂非 nil Precommit / precommit nil 不会叫 ExtendVote | 不是已经会调 ExtendVote | 不是一轮只能交出一份扩展就已经是每一高度一份（350） |
| 应用可以选 0 长扩展 | 不是已经不会叫 ExtendVote | 不是空扩展仍会调 Verify 就已经跳过 Verify（353） |
| 造扩展的应用逻辑可以非确定 | 不是已经必须同一份扩展 | 不是 ExtendVote 没有确定性要求就已经是同一块（338） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ExtendVote Usage 就已经会调 ExtendVote、已经不会叫、已经必须同一份扩展」，必须分开 ExtendVoteResponse.vote_extension 只会挂在非 nil Precommit 上、precommit nil 不会叫 ExtendVote 是不是已经会调 ExtendVote、应用可以选 0 长扩展是不是已经不会叫 ExtendVote、造扩展的应用逻辑可以非确定是不是已经必须同一份扩展。可以跳过「看见填了 ExtendVote Usage 就已经会调 ExtendVote」。不要另写怎样写 ExtendVote Usage 正式三事。

## 本页不抄

- 怎样写 ExtendVote Usage 正式三事、怎样选空扩展、怎样写非确定逻辑。
- 一轮只能交出一份扩展就已经是每一高度一份。那是不变量 350。
- 空扩展仍会调 Verify 就已经跳过 Verify。那是不变量 353。
- ExtendVote 没有确定性要求就已经是同一块。那是不变量 338。
