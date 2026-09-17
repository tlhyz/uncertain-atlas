# 例：看见增量验了 chunk is not already the only trusted AppHash interchangeable / not already unforgeable metadata interchangeable / not already settled interchangeable

**层次**：实现 / 增量验了 chunk not already the only trusted AppHash / not already unforgeable metadata / not already settled 正式三事（332 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Verification。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「增量验了 chunk not already the only trusted AppHash / not already unforgeable metadata / not already settled 正式三事（332 余量）/ not 936 snapshot-verify-notanchor interchangeable / not 332 snapshot-verify-vs-early bundled interchangeable」，不是快照验完 bundled（332），也不是只有 AppHash 可信任（38），也不是四门就已经必须实现快照（334/932）。不要另写怎样做增量默克尔证明或怎样配受信邻居。

## 官方三件事

1. **看见增量验了 chunk / 看见 checksum / 看见绑了默克尔 这份早验 is not already 已经是唯一可信的 AppHash interchangeable，也不是已经快照验完 bundled（332） interchangeable / 936 snapshot-verify-notanchor interchangeable / 935 snapshot-verify-notearly interchangeable / 332 snapshot-verify item 1 装完又对上 interchangeable，也不是已经增量验了 chunk not already the only trusted AppHash / not already unforgeable metadata / not already settled 正式三事 bundled（332 item 2 余量） interchangeable / 332 snapshot-verify item 2 interchangeable。**  
   官方写：装回可能很慢，应用可以在装的过程中另做核对，好早发现失败。例如按 chunk 对 AppHash 做增量验（带上捆绑的默克尔证明）、checksum 防盘或网把数据弄坏。唯一可信的信息仍是 AppHash，其余快照元数据都能被对手伪造。看见做了增量验，不是已经是那份唯一可信锚 interchangeable——本页从 332 item 2 侧钉 not already the only trusted AppHash 单句。332 snapshot-verify vs early bundled unbundling 在本页 item 2 续。

2. **看见 checksum 过了 / 看见证明绿了 / 这份早验 is not already 已经不能被伪造元数据 interchangeable，也不是已经快照验完 bundled（332） interchangeable / 936 snapshot-verify-notanchor interchangeable / 332 snapshot-verify item 3 封禁 interchangeable / 937 snapshot-verify-notdos interchangeable，也不是已经只有 AppHash 可信任 interchangeable / 38 apphash-trust interchangeable。**  
   官方把 checksum 过了和元数据已经不能伪造分开——332 bundled 第二件事常与 38 混成「看见增量验就已经是唯一可信锚或已经交差 interchangeable」，本页钉 not already unforgeable metadata 单句。

3. **看见证明绿了 / 看见做了增量验 / 这份早验 is not already 已经交差 interchangeable，也不是已经快照验完 bundled（332） interchangeable / 936 snapshot-verify-notanchor interchangeable / 935 snapshot-verify-notearly interchangeable，也不是已经四门就已经必须实现快照 interchangeable / 334/932 snapshot-conn-notmust interchangeable。**  
   官方把证明绿了和已经代替最后那次 Info / 已经交差分开。看见证明绿了，不是已经交差 interchangeable。332 snapshot-verify vs early bundled unbundling 在本页 item 2 续。

怎样做增量默克尔证明、怎样配 checksum、怎样写受信邻居名单是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **增量验了 chunk not already the only trusted AppHash ≠ 已经是唯一可信的 AppHash interchangeable：** 官方把可以早发现失败和唯一可信锚分开。
- **看见 checksum 过了 not already unforgeable metadata ≠ 已经不能被伪造元数据 interchangeable：** 官方把 checksum 过了和元数据已经不能伪造分开。
- **看见证明绿了 not already settled ≠ 已经交差 interchangeable：** 官方把证明绿了和已经代替最后那次 Info 分开；332 snapshot-verify vs early bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 增量验了 chunk | 不是已经是唯一可信的 AppHash | 不是只有 AppHash 可信任（38） |
| 看见 checksum 过了 | 不是已经不能被伪造元数据 | 不是四门就已经必须实现快照（334/932） |
| 看见证明绿了 | 不是已经交差 | 不是装完又对上就已经早验过（935） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看增量验了 chunk not already the only trusted AppHash / not already unforgeable metadata / not already settled 正式三事（332 余量），必须分开是不是已经是唯一可信的 AppHash、是不是已经不能被伪造元数据、是不是已经交差。可以跳过「看见增量验就已经是唯一可信锚」。不要另写怎样做增量默克尔证明或怎样配受信邻居。332 snapshot-verify vs early bundled unbundling 在本页 item 2 续；续 [`worked-example-snapshot-verify-notdos-vs-bundled.md`](worked-example-snapshot-verify-notdos-vs-bundled.md)（不变量 937 item 3）。

## 本页不抄

- 怎样做增量默克尔证明、怎样配 checksum、怎样写受信邻居名单。
- 快照验完 bundled。那是不变量 332。
- 装完又对上就已经早验过。那是不变量 332 item 1 余量 / 935。
- 只有 AppHash 可信任。那是不变量 38。
- 四门就已经必须实现快照。那是不变量 334/932。
