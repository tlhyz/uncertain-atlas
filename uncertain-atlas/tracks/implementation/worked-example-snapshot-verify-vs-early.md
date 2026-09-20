# 例：看见装完又对上 LastBlockAppHash 不是已经在装回当中验过；看见增量验了 chunk 不是已经是唯一可信的 AppHash；看见封禁邻居不是已经没有快照 DoS

**层次**：实现 / Snapshot Verification。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Verification。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「装完又对上 LastBlockAppHash 不是已经在装回当中验过 / 增量验了 chunk 不是已经是唯一可信的 AppHash / 封禁邻居不是已经没有快照 DoS」，不是 Offer 收下已经装完，也不是切进共识已经有完整历史。不要另写怎样做增量默克尔证明或怎样配受信邻居。 332 snapshotverify vs early bundled unbundling 续（752 + 753）；精读 [`worked-example-snapshotverify-notduringrestore-vs-bundled.md`](worked-example-snapshotverify-notduringrestore-vs-bundled.md)；[`worked-example-snapshotverify-notuniqueapphash-vs-bundled.md`](worked-example-snapshotverify-notuniqueapphash-vs-bundled.md)（不变量 753 item 2）。

## 官方三件事

规范把快照验完写成三件独立的实现事，不是「看见装完又对上就已经在装回当中验过、已经是唯一可信锚、已经没有有害快照」一件事：

1. **看见装完又叫了 Info / 看见 LastBlockAppHash 对上轻客户端那份 不是已经在装回当中增量验过，也不是已经进了网。**  
   官方写：chunk **都收下之后**，CometBFT 才叫 `Info`，取 `LastBlockAppHash`，跟轻客户端从链上取来、验过的那份 AppHash 对。还要看 `LastBlockHeight` 是不是这份快照的高度。这次核对是为了在**进网之前**确认应用有效。看见对上了，不是已经在装的时候验过。看见高度对上，不是已经切进共识。看见 Info 绿了，不是已经进了网。
2. **看见增量验了 chunk / 看见 checksum / 看见绑了默克尔 不是已经是唯一可信的 AppHash，也不是已经不能被伪造元数据。**  
   官方写：装回可能很慢，应用可以在装的过程中另做核对，好早发现失败。例如按 chunk 对 AppHash 做增量验（带上捆绑的默克尔证明）、checksum 防盘或网把数据弄坏。**唯一可信的信息仍是 AppHash**，其余快照元数据都能被对手伪造。看见做了增量验，不是已经是那份唯一可信锚。看见 checksum 过了，不是元数据已经不能伪造。看见证明绿了，不是已经代替最后那次 Info。
3. **看见让引擎封禁邻居 / 看见配了受信邻居名单 不是已经没有快照 DoS，也不是已经收下这个人。**  
   官方写：对手可以给无效或有害快照，拦节点进网。应用可以让 CometBFT 封禁邻居。最后一招，运维可以把 P2P 配成只信一份能给有效快照的邻居。看见封禁了，不是已经没有这种 DoS。看见配了受信名单，不是已经是过滤已经收下。看见能挡一家，不是已经能挡所有有害快照。

怎样做增量默克尔证明、怎样配 checksum、怎样写受信邻居名单是规范里的取值或做法，本页不抄。只有 AppHash 可信任是不变量 38，本页不抄。

## 官方为什么这样拆

- **装完又对上 ≠ 已经在装回当中验过：** 官方把进网前最后一次 Info 和装回当中的增量验分开。
- **增量验了 chunk ≠ 已经是唯一可信的 AppHash：** 官方把可以早发现失败和唯一可信锚分开。
- **封禁邻居 ≠ 已经没有快照 DoS：** 官方把封禁 / 受信名单和已经没有有害快照分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 装完又对上 LastBlockAppHash | 不是已经在装回当中验过 | 不是 Offer 收下已经装完（321），也不是 AppHash 对上已经版本也对上（323） |
| 增量验了 chunk | 不是已经是唯一可信的 AppHash | 不是只有 AppHash 可信任（38） |
| 封禁邻居 / 受信名单 | 不是已经没有快照 DoS | 不是发了 addr 过滤查询已经收下这个人（326） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「快照已经对上就已经在装回当中验过、已经是唯一可信锚、已经没有有害快照」，必须分开装完又对上是不是已经在装回当中验过、增量验了 chunk 是不是已经是唯一可信的 AppHash、封禁邻居是不是已经没有快照 DoS。可以跳过「看见对上就已经早验过」。不要另写怎样做增量默克尔证明或怎样配受信邻居。 332 snapshotverify vs early bundled unbundling 续（752 + 753 item 2）。

## 本页不抄

- 怎样做增量默克尔证明、怎样配 checksum、怎样写受信邻居名单。
- Offer 收下已经装完。那是不变量 321。
- AppHash 对上已经版本也对上、切进共识已经有完整历史。那是不变量 323。
- 只有 AppHash 可信任。那是不变量 38。
- 发了 addr 过滤查询已经收下这个人。那是不变量 326。
