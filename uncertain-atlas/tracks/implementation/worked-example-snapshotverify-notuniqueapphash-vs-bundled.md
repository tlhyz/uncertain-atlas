# 例：看见增量验了 chunk / 看见 checksum 过了 / 看见证明绿了 is not already already unique-apphash interchangeable / already metadata-unforgeable interchangeable / already replaces-final-info interchangeable

**层次**：实现 / 增量验了 chunk 不是已经是唯一可信的 AppHash not already unique-apphash / not already metadata-unforgeable / not already replaces-final-info 正式三事（332 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Verification。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「增量验了 chunk 不是已经是唯一可信的 AppHash not already unique-apphash / not already metadata-unforgeable / not already replaces-final-info 正式三事（332 余量）/ not 753 snapshotverify-notuniqueapphash interchangeable / not 332 snapshotverify bundled interchangeable」，不是 Snapshot Verification bundled（332），也不是装完又对上不是已经在装回当中验过（752 item 1 余量）或封禁邻居不是已经没有快照 DoS（754 item 3 余量）。不要另写怎样做增量默克尔证明或怎样配 checksum。

## 官方三件事

规范把 Requirements 里装回当中可另做核对、唯一可信仍是 AppHash、其余元数据都能被伪造 和「已经是增量验了 chunk 就已经是唯一可信的 AppHash interchangeable / 已经是 checksum 过了就已经不能伪造元数据 interchangeable / 已经是证明绿了就已经代替最后那次 Info interchangeable / 已经是 snapshotverify bundled interchangeable」分开写成三件独立的实现事，不是「看见增量验了 chunk 就已经是唯一可信的 AppHash interchangeable / 就已经不能伪造元数据 interchangeable / 就已经代替最后那次 Info interchangeable」一件事：

1. **看见增量验了 chunk / 看见按 chunk 对 AppHash 做增量验 / 看见绑了默克尔证明 is not already 已经是唯一可信的 AppHash interchangeable / 已经 unique-apphash interchangeable / 已经唯一可信锚交差 interchangeable / 332 snapshotverify bundled interchangeable / 33 four gates interchangeable / snapshotverify-sold-as-early interchangeable，也不是已经 Snapshot Verification bundled（332） interchangeable / 753 snapshotverify-notuniqueapphash interchangeable / 332 snapshotverify item 2 interchangeable，也不是已经增量验了 chunk 不是已经是唯一可信的 AppHash not already unique-apphash / not already metadata-unforgeable / not already replaces-final-info 正式三事 bundled（332 item 2 余量） interchangeable / 332 snapshotverify item 2 interchangeable，也不是已经装完又对上不是已经在装回当中验过（752） interchangeable / 754 snapshotverify-notnodod interchangeable / 38 apphash-only interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：装回可能很慢，应用可以在装的过程中另做核对，好早发现失败。例如按 chunk 对 AppHash 做增量验（带上捆绑的默克尔证明）。**唯一可信的信息仍是 AppHash**。看见增量验了 chunk，不是已经 unique-apphash interchangeable——332 钉 bundled 三事，本页从 item 2 侧钉 not already unique-apphash 单句。看见按 chunk 对 AppHash 做增量验，不是已经 Snapshot Verification bundled（332） interchangeable——332 钉 bundled，本页钉 item 2 第一件事。看见绑了默克尔证明，不是已经只有 AppHash 可信任（38） interchangeable——38 另钉。332 snapshotverify vs early bundled unbundling 在本页 item 2 续。

2. **看见 checksum 过了 / 看见 checksum / 看见防盘或网把数据弄坏 is not already 已经不能伪造元数据 interchangeable / 已经 metadata-unforgeable interchangeable / 已经元数据不能伪造交差 interchangeable / 332 snapshotverify bundled interchangeable / 38 apphash-only interchangeable，也不是已经 Snapshot Verification bundled（332） interchangeable / 753 snapshotverify-notuniqueapphash interchangeable / 332 snapshotverify item 1 装完又对上 interchangeable / 332 snapshotverify item 3 封禁 interchangeable，也不是已经增量验了 chunk 不是已经是唯一可信的 AppHash not already unique-apphash / not already metadata-unforgeable / not already replaces-final-info 正式三事 bundled（332 item 2 余量） interchangeable / 332 snapshotverify item 2 interchangeable，也不是已经是唯一可信的 AppHash（本页第一件事） interchangeable。**  
   官方写：checksum 防盘或网把数据弄坏；其余快照元数据都能被对手伪造。看见 checksum 过了，不是已经 metadata-unforgeable interchangeable——本页钉 not already metadata-unforgeable 单句。看见 checksum，不是已经只有 AppHash 可信任（38） interchangeable——38 另钉。看见防盘或网把数据弄坏，不是已经是唯一可信的 AppHash（本页第一件事） interchangeable——三件事分开钉。332 snapshotverify vs early bundled unbundling 在本页 item 2 续。

3. **看见证明绿了 / 看见捆绑的默克尔绿了 / 看见早发现失败核对绿了 is not already 已经代替最后那次 Info interchangeable / 已经 replaces-final-info interchangeable / 已经代替最后 Info 交差 interchangeable / 332 snapshotverify bundled interchangeable / 752 snapshotverify-notduringrestore interchangeable，也不是已经 Snapshot Verification bundled（332） interchangeable / 753 snapshotverify-notuniqueapphash interchangeable / 332 snapshotverify item 1 / 332 snapshotverify item 3，也不是已经增量验了 chunk 不是已经是唯一可信的 AppHash not already unique-apphash / not already metadata-unforgeable / not already replaces-final-info 正式三事 bundled（332 item 2 余量） interchangeable / 332 snapshotverify item 2 interchangeable，也不是已经是唯一可信的 AppHash（本页第一件事） interchangeable / 已经不能伪造元数据（本页第二件事） interchangeable。**  
   官方写：看见证明绿了，不是已经代替最后那次 Info。看见捆绑的默克尔绿了，不是已经 replaces-final-info interchangeable——本页钉 not already replaces-final-info 单句。看见早发现失败核对绿了，不是已经装完又对上不是已经在装回当中验过（752） interchangeable——752 另钉进网前最后一次 Info。看见证明绿了，不是已经不能伪造元数据（本页第二件事） interchangeable——三件事分开钉。332 snapshotverify vs early bundled unbundling 在本页 item 2 续。

怎样做增量默克尔证明、怎样配 checksum、怎样写受信邻居名单是规范里的取值或做法，本页不抄。Snapshot Verification bundled（332）、装完又对上不是已经在装回当中验过（332 item 1 余量 / 752）、封禁邻居不是已经没有快照 DoS（332 item 3 余量 / 754）、只有 AppHash 可信任（38）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **增量验了 chunk not already unique-apphash ≠ 332 / 33 interchangeable：** 官方把可以早发现失败和唯一可信锚分开。
- **checksum 过了 not already metadata-unforgeable ≠ 已经不能伪造元数据 interchangeable：** 官方把防盘或网弄坏和元数据已经不能伪造分开。
- **证明绿了 not already replaces-final-info ≠ 已经代替最后那次 Info interchangeable：** 官方把装回当中核对和进网前最后一次 Info 分开；332 snapshotverify vs early bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 增量验了 chunk | 不是 already unique-apphash | 不是只有 AppHash 可信任 alone（38） |
| checksum 过了 | 不是 already metadata-unforgeable | 不是装完又对上 alone（752） |
| 证明绿了 | 不是 already replaces-final-info | 不是进网前最后 Info alone（752） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看增量验了 chunk 不是已经是唯一可信的 AppHash not already unique-apphash / not already metadata-unforgeable / not already replaces-final-info 正式三事（332 余量），必须分开增量验了 chunk 是不是 already unique-apphash interchangeable / 332 snapshotverify bundled interchangeable / snapshotverify-sold-as-early interchangeable、checksum 过了 是不是 already metadata-unforgeable interchangeable、证明绿了 是不是 already replaces-final-info interchangeable。可以跳过「看见增量验了 chunk 就已经是唯一可信的 AppHash interchangeable / 就已经不能伪造元数据 interchangeable / 就已经代替最后那次 Info interchangeable」。不要另写怎样做增量默克尔证明。332 snapshotverify vs early bundled unbundling 在本页 item 2 续（752 + 753）；续 [`worked-example-snapshotverify-notnodod-vs-bundled.md`](worked-example-snapshotverify-notnodod-vs-bundled.md)（不变量 754 item 3）已写；完成见 754。

## 本页不抄

- 怎样做增量默克尔证明、怎样配 checksum、怎样写受信邻居名单。
- Snapshot Verification bundled。那是不变量 332。
- 装完又对上不是已经在装回当中验过。那是不变量 332 item 1 余量 / 752。
- 封禁邻居不是已经没有快照 DoS。那是不变量 332 item 3 余量 / 754。
- 只有 AppHash 可信任。那是不变量 38。
- 四门已经结算。那是不变量 33。
