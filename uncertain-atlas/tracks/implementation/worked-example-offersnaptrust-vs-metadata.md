# 例：看见 Only AppHash can be trusted 不是已经 Snapshot 字段都可信；看见 Any other data can be spoofed / employ additional verification 不是已经 hash 比对就够 / 已经防 DoS；看见 verified AppHash automatically checked at end of restoration 不是已经装块时就 Info 对了 / 已经切进共识

**层次**：实现 / OfferSnapshot Usage trust 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Only AppHash can be trusted 不是 Snapshot 字段都可信 / Any other data can be spoofed 不是 hash 比对就够 / verified AppHash automatically checked at end 不是装块时就 Info 对了」，不是只有轻客户端验过的 AppHash 可信任 bundled 总则（38），也不是 Snapshot Verification 增量验（332），也不是 Transition to Consensus Info 核对（323）。不要另写怎样做增量验、怎样封邻居。

## 官方三件事

规范把 OfferSnapshot Usage 里 Only AppHash can be trusted、Any other data can be spoofed / employ additional verification、verified AppHash automatically checked at the end 写成三件独立的实现事，不是「看见 Offer 了 AppHash 就已经全信、已经防 DoS、已经装完对了」一件事：

1. **看见 Only `AppHash` can be trusted, as it has been verified by the light client / 看见只有 AppHash 可信任、且已由轻客户端验过 不是已经 `Snapshot.hash` / `metadata` / 五个字段都对上就可信，也不是已经 ListSnapshots 回了本地清单就可信。**  
   官方 Usage 写：Only `AppHash` can be trusted, as it has been verified by the light client。看见 only AppHash，不是已经 Snapshot 全字段（含 Metadata）对上就算同一份（368） interchangeable。看见 light client verified，不是已经引擎不解释 hash 只比较（368）那种 hash 比对就等于轻验 interchangeable。看见可信任，不是已经 OfferSnapshot 请求 `app_hash` 填了（396）就等于已经验完 interchangeable——396 钉请求栏，本页钉 Usage trust。
2. **看见 Any other data can be spoofed by adversaries, so applications should employ additional verification schemes to avoid denial-of-service attacks / 看见其它数据可被伪造、应用还应另做验真防 DoS 不是已经 hash / metadata 比对就够，也不是已经增量验 chunk 就等于已经防 DoS 交差。**  
   官方 Usage 写：Any other data can be spoofed by adversaries, so applications should employ additional verification schemes to avoid denial-of-service attacks。看见 can be spoofed，不是已经五个字段都对上就不能伪造 interchangeable。看见 employ additional verification，不是已经 Snapshot Verification 增量验 / checksum（332） bundled 就等于 Usage 这句 interchangeable——332 钉 app requirements，本页钉 Methods Usage。看见 avoid DoS，不是已经 reject_senders / refetch_chunks（378）就等于已经防无效快照 interchangeable。
3. **看见 The verified `AppHash` is automatically checked against the restored application at the end of snapshot restoration / 看见装回结束时引擎会自动核对 verified AppHash 不是已经在装 chunk 过程中 Info 对了（332），也不是已经 Transition to Consensus 那套 ChainID / 版本核对（323） interchangeable，也不是已经 Offer 收下就已经装完（321）。**  
   官方 Usage 写：The verified `AppHash` is automatically checked against the restored application at the end of snapshot restoration。看见 automatically checked at the end，不是已经在装块时就叫 Info 对 LastBlockAppHash（332） interchangeable。看见 against the restored application，不是已经切进共识就有完整历史（323） interchangeable。看见 at the end of restoration，不是已经 ApplySnapshotChunk Result ACCEPT 就已经齐（401） interchangeable。

怎样做增量验、怎样封邻居、怎样配轻客户端 RPC 是规范里的做法，本页不抄。只有轻客户端验过的 AppHash 可信任（38）是总则 bundled，Snapshot Verification（332）是 app requirements 增量验那套，Transition to Consensus（323）是装完后再凑 ChainID / Info 核对那套，Offer 收下之后（401）是 Accept 后拉块那套，本页不抄。

## 官方为什么这样拆

- **Only AppHash can be trusted ≠ Snapshot 字段都可信 / hash 比对就够：** 官方把轻客户端验过的 AppHash 和 Snapshot 元数据、引擎 hash 比较分开。
- **Any other data can be spoofed / employ additional verification ≠ hash 比对就够 / 已经防 DoS：** 官方把 Methods Usage 侧另做验真和 app requirements 增量验、ApplySnapshotChunk 再拉分开。
- **verified AppHash automatically checked at end ≠ 装块时就 Info 对了 / 已经切进共识：** 官方把装回结束时自动核对和装过程中 Info、Transition to Consensus 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Only AppHash can be trusted | 不是 Snapshot 字段都可信 | 不是只有 AppHash 可信任总则（38） |
| Any other data can be spoofed / employ additional verification | 不是 hash 比对就够 | 不是 Snapshot Verification（332） |
| verified AppHash automatically checked at end | 不是装块时就 Info 对了 | 不是 Transition to Consensus（323） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Offer 了 AppHash 就已经全信、已经防 DoS、已经装完对了」，必须分开 Only AppHash can be trusted 是不是 Snapshot 字段都可信、Any other data can be spoofed / employ additional verification 是不是 hash 比对就够 / 已经防 DoS、verified AppHash automatically checked at end 是不是装块时就 Info 对了 / 已经切进共识。可以跳过「看见 Offer 了 AppHash 就已经全信」。不要另写怎样做增量验、怎样封邻居。483 offersnaptrust unbundling 在本页 item 1 启动；精读 [`worked-example-offersnaptrust-notmetadata-vs-bundled.md`](worked-example-offersnaptrust-notmetadata-vs-bundled.md)（不变量 650 item 1）；续 [`worked-example-offersnaptrust-notverify-vs-bundled.md`](worked-example-offersnaptrust-notverify-vs-bundled.md)（不变量 651 item 2）；完成 [`worked-example-offersnaptrust-nottransition-vs-bundled.md`](worked-example-offersnaptrust-nottransition-vs-bundled.md)（不变量 652 item 3）。

## 本页不抄

- 怎样做增量验、怎样封邻居、怎样配轻客户端 RPC、怎样写 OfferSnapshot。
- 只有轻客户端验过的 AppHash 可信任。那是不变量 38。
- Snapshot Verification 增量验 / checksum / 封邻居。那是不变量 332。
- Transition to Consensus Info 核对 / 切进共识。那是不变量 323。
- Offer 收下之后拉块并装。那是不变量 401。
- Snapshot 全字段（含 Metadata）对上。那是不变量 368。
