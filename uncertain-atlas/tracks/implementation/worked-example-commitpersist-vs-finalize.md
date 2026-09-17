# 例：看见 Signal the Application to persist application state 不是已经在 Finalize 改了就已经落盘；看见 Application is expected to persist its state at the end of this call 不是已经 Commit 不带参数就等于已经落盘；看见 Historical blocks may also be required for auditing / replay / light client verification 不是已经 retain_height 默认 0 就等于已经在剪

**层次**：实现 / Commit Usage persist signal 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Signal persist application state 不是已经在 Finalize 改了就已经落盘 / expected persist at end of this call 不是已经 Commit 不带参数就等于已经落盘 / Historical blocks required for auditing replay light client 不是已经 retain_height 默认 0 就等于已经在剪」，不是 FinalizeBlock 落盘禁令 bundled 三事，也不是 Commit 空请求 bundled 三事，也不是 Commit 保留高度 bundled 三事。不要另写怎样落盘、怎样填 retain_height。

## 官方三件事

规范把 Commit Usage 里 persist signal、expected persist at end of this call、Historical blocks may also be required 写成三件独立的实现事，不是「看见叫了 Commit 就已经落盘、已经在 Finalize 落了、已经在剪历史」一件事：

1. **看见 Signal the Application to persist application state / 看见叫 Commit 让应用落盘应用状态 不是已经在 Finalize 改了就已经落盘，也不是已经引擎 persist tx outputs / AppHash / ResultsHash。**  
   官方 Usage 写：Signal the Application to persist application state。看见 persist signal，不是已经 Finalize 改了状态就已经落盘（335）。看见叫 Commit 让应用落盘，不是已经 CometBFT persists the transaction outputs, AppHash, and ResultsHash（587）那种引擎落这三份 interchangeable。看见 signal，不是已经 When step 8 calls Commit to instruct 就已经是同一句 interchangeable——590 钉 When 第 8 步，本页钉 Commit Usage persist signal。
2. **看见 Application is expected to persist its state at the end of this call / 看见应在这次 Commit 返回前落盘应用状态 不是已经 Commit 不带参数就等于已经落盘，也不是已经 signal 就已经交差。**  
   官方写：Application is expected to persist its state at the end of this call, before returning from `Commit`。看见 expected at end of this call，不是已经 Commit Request 不带参数（399）那种能叫就等于已经落盘 interchangeable。看见返回前落盘，不是已经 Finalize + Commit 那种已经交差。看见应在 Commit 里做，不是已经 Finalize 改了就已经落盘（335） interchangeable。
3. **看见 Historical blocks may also be required for auditing, replay of non-persisted heights, light client verification, and so on / 看见历史块还可能用于审计、回放没落盘高度、轻客户端验 不是已经 retain_height 默认 0 就等于已经在剪，也不是已经全网删了就只有 state sync 能加新节点。**  
   官方写：Use `CommitResponse.retain_height` with caution! … Historical blocks may also be required for other purposes, e.g. auditing, replay of non-persisted heights, light client verification, and so on。看见 auditing / replay / light client，不是已经 retain_height defaults to 0 (retain all)（366）那种默认全留 interchangeable。看见 may also be required，不是已经能剪就等于已经没有历史。看见 other purposes，不是已经切进共识就已经有完整历史（323） interchangeable。

怎样落盘、怎样填 retain_height、怎样开 state sync 是规范里的做法，本页不抄。FinalizeBlock 落盘禁令（335）是 Finalize MUST NOT persist / MUST persist in Commit / remember last Commit height 那套另一切片，Commit 空请求（399）是 Commit 不带参数 / Echo 回包 / Echo 测实现那套另一切片，Commit 保留高度（366）是 retain_height 默认 0 / blocks below may be removed / all nodes remove 那套另一切片，FinalizeBlock When calls Commit instruct persist（590）是 When 第 8 步 calls Commit 那套另一切片，本页不抄。

## 官方为什么这样拆

- **Signal persist application state ≠ 已经在 Finalize 改了就已经落盘 / 已经引擎 persist 这三份：** 官方把应用 Commit 落盘信号和 Finalize 禁令、引擎 persist tx outputs / AppHash / ResultsHash 分开。
- **Expected persist at end of this call ≠ 已经 Commit 不带参数就等于已经落盘：** 官方把应在这次 Commit 返回前落盘和 Commit 空请求、signal 就已经交差分开。
- **Historical blocks required for auditing / replay / light client ≠ 已经 retain_height 默认 0 就等于已经在剪：** 官方把历史块还可能要用于审计 / 回放 / 轻客户端验和 retain_height 默认全留、已经在剪分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Signal persist application state | 不是已经在 Finalize 改了就已经落盘 | 不是 FinalizeBlock 落盘禁令（335） |
| Expected persist at end of this call | 不是已经 Commit 不带参数就等于已经落盘 | 不是 Commit 空请求（399） |
| Historical blocks for auditing / replay / light client | 不是已经 retain_height 默认 0 就等于已经在剪 | 不是 Commit 保留高度（366） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见叫了 Commit 就已经落盘、已经在 Finalize 落了、已经在剪历史」，必须分开 Signal persist application state 是不是已经在 Finalize 改了就已经落盘 / 已经引擎 persist 这三份、Expected persist at end of this call 是不是已经 Commit 不带参数就等于已经落盘、Historical blocks required for auditing / replay / light client 是不是已经 retain_height 默认 0 就等于已经在剪。可以跳过「看见叫了 Commit 就已经落盘」。不要另写怎样落盘、怎样填 retain_height。481 commitpersist vs finalize bundled unbundling 启动（680 item 1）；精读 [`worked-example-commitpersist-notfinpersist-vs-bundled.md`](worked-example-commitpersist-notfinpersist-vs-bundled.md)（不变量 680 item 1）。481 commitpersist vs finalize bundled unbundling 续（681 item 2）；精读 [`worked-example-commitpersist-notendofcall-vs-bundled.md`](worked-example-commitpersist-notendofcall-vs-bundled.md)（不变量 681 item 2）。

## 本页不抄

- 怎样落盘、怎样写 Commit、怎样填 retain_height、怎样开 state sync。
- FinalizeBlock 落盘禁令。那是不变量 335。
- Commit 空请求。那是不变量 399。
- Commit 保留高度。那是不变量 366。
- FinalizeBlock When lock mempool Commit recheck。那是不变量 468。
- 崩溃恢复三步。那是不变量 320。
