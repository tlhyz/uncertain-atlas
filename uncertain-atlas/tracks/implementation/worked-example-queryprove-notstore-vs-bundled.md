# 例：看见 Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明 is not already key lookup interchangeable / not already AppHash matched interchangeable / not already settled interchangeable

**层次**：实现 / Query 回包 proof_ops not already key lookup / not already AppHash matched / not already settled 正式三事（383 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request / Query Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query 回包 proof_ops not already key lookup / not already AppHash matched / not already settled 正式三事（383 余量）/ not 780 queryprove-notstore interchangeable / not 383 queryprove-vs-proof bundled interchangeable」，不是 Query 证明回包 bundled（383），也不是 Query 回包 value 就已经对上 AppHash（380），也不是 ProofOp.data 就已经是 proof_ops（390/744），也不是 Query 回包 info 就已经是按键查（384/778）。不要另写怎样写 Query 证明回包。

## 官方三件事

1. **看见 Query 回包 `proof_ops` 是按请求回的、要对这一高 AppHash 验的序列化证明 / 看见回了证明 / Query 这份序列化证明 is not already 已经按 `/store` 按键查 interchangeable，也不是已经 Query 证明回包 bundled（383） interchangeable / 780 queryprove-notstore interchangeable / 779 queryprove-notapphash interchangeable / 383 queryprove item 1 prove interchangeable，也不是已经 proof_ops not already key lookup / not already AppHash matched / not already settled 正式三事 bundled（383 item 2 余量） interchangeable / 383 queryprove item 2 interchangeable。**  
   官方写：`proof_ops` 是按请求回的、用来对这一高 `app_hash` 验这份值的序列化证明。看见回了证明，不是已经按 `/store` 按键查 interchangeable——本页从 383 item 2 侧钉 not already key lookup 单句。383 queryprove vs proof bundled unbundling 在本页 item 2 续。

2. **看见回了证明 / 看见有序列化证明 / Query 这份序列化证明 is not already 已经对上 AppHash interchangeable / 380 queryval interchangeable，也不是已经 Query 证明回包 bundled（383） interchangeable / 780 queryprove-notstore interchangeable / 383 queryprove item 3 height interchangeable / 781 queryprove-notreqh interchangeable，也不是已经 ProofOp.data 就已经是 proof_ops interchangeable / 390 proofop / 744 proofop-notproofops interchangeable，也不是已经 Query 回包 info 就已经是按键查 interchangeable / 384 querycode / 778 querycode-notkey interchangeable。**  
   官方把回包证明和已经对上 AppHash 分开——383 bundled 第二件事常与 380 / 390 / 384 混成「看见回了证明就已经是按键查或已经对上 AppHash interchangeable」，本页钉 not already AppHash matched 单句。

3. **看见回了证明 / 看见能回 / Query 这份序列化证明 is not already 已经交差 interchangeable，也不是已经 Query 证明回包 bundled（383） interchangeable / 780 queryprove-notstore interchangeable / 779 queryprove-notapphash interchangeable。**  
   官方把能回 proof_ops 和已经交差分开。看见能回，不是已经交差 interchangeable。383 queryprove vs proof bundled unbundling 在本页 item 2 续。

怎样写 Query 证明、怎样勾 prove、怎样编 proof_ops 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **proof_ops not already key lookup ≠ 已经是按键查 interchangeable：** 官方把回包证明和回包键值分开。
- **proof_ops not already AppHash matched ≠ 380 interchangeable：** 官方把有序列化证明和已经对上 AppHash 分开。
- **proof_ops not already settled ≠ 已经交差 interchangeable：** 官方把能回 proof_ops 和已经交差分开；383 queryprove vs proof bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明 | 不是已经是按键查 | 不是 Query 请求 prove（779/383 item 1） |
| 看见回了证明 | 不是已经对上 AppHash（380） | 不是 ProofOp.data（390/744） |
| 看见能回 | 不是已经交差 | 不是 Query 回包 info（384/778） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 proof_ops not already key lookup / not already AppHash matched / not already settled 正式三事（383 余量），必须分开 proof_ops 是不是已经是按键查、是不是已经对上 AppHash interchangeable / 380、是不是已经交差。可以跳过「看见回了证明就已经是按键查」。不要另写怎样写 Query 证明回包。383 queryprove vs proof bundled unbundling 在本页 item 2 续；完成 [`worked-example-queryprove-notreqh-vs-bundled.md`](worked-example-queryprove-notreqh-vs-bundled.md)（不变量 781 item 3）。

## 本页不抄

- 怎样写 Query 证明、怎样勾 prove、怎样编 proof_ops。
- Query 证明回包 bundled。那是不变量 383。
- Query 请求 prove。那是不变量 383 item 1 余量 / 779。
- Query 回包 height。那是不变量 383 item 3 余量 / 781。
- Query 回包 value 就已经对上 AppHash。那是不变量 380。
- ProofOp.data 就已经是 proof_ops。那是不变量 390 / 744。
- Query 回包 info 就已经是按键查。那是不变量 384 / 778。
