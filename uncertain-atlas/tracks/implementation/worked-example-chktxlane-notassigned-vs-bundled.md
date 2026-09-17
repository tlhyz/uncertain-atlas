# 例：看见 assigned to the default lane is not already default_lane identifier written interchangeable / not already Priority is consensus order interchangeable / not already Check passed is in proposal interchangeable

**层次**：实现 / CheckTx Usage assigned to default lane not default_lane identifier / not Priority consensus order / not Check passed is in proposal 正式三事（482 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx Usage assigned to default lane not default_lane identifier / not Priority consensus order / not Check passed is in proposal 正式三事（482 余量）/ not 705 chktxlane-notassigned interchangeable / not 482 chktxlane-vs-default bundled interchangeable」，不是 CheckTx Usage lane_id 正式二事 bundled（482），也不是 CheckTx Priority 共识顺序（317）或四门已进提案（33）。不要另写怎样选 default_lane。

## 官方三件事

1. **看见 so the transaction will be assigned to the default lane / 看见会放进默认道 / assigned is not already 已经回包里写了 `default_lane` 那个标识本身 interchangeable，也不是已经 CheckTx Usage lane_id 正式二事 bundled（482） interchangeable / 705 chktxlane-notassigned interchangeable / 704 chktxlane-notreserved interchangeable / 482 chktxlane item 1 empty interchangeable，也不是已经 assigned to default lane not default_lane identifier / not Priority consensus order / not Check passed is in proposal 正式三事 bundled（482 item 2 余量） interchangeable / 482 chktxlane item 2 interchangeable。**  
   官方 Usage 写：so the transaction will be assigned to the default lane。看见 assigned to the default lane，不是已经回包里写了 default_lane 那个字符串 interchangeable——本页从 482 item 2 侧钉 not default_lane identifier 单句。482 chktxlane vs default bundled unbundling 在本页 item 2 续。

2. **看见放进默认道 / 看见 assigned / 看见 Usage 这句 is not already 已经 CheckTx 的 Priority 就已经是共识顺序（317） interchangeable / 317 priority interchangeable，也不是已经 CheckTx Usage lane_id 正式二事 bundled（482） interchangeable / 705 chktxlane-notassigned interchangeable / 482 chktxlane item 3 range interchangeable / 706 chktxlane-notrange interchangeable。**  
   官方把 Usage assigned to default lane 单句和 Priority 就已经是共识顺序分开——482 bundled 第二件事常与 317 混成「看见放进默认道就已经排了优先 interchangeable」，本页钉 not Priority consensus order 单句。

3. **看见会放进默认道 / 看见 Usage 这句 / assigned is not already 已经 Check 通过就是已进提案（33） interchangeable / 33 fourgates interchangeable，也不是已经 CheckTx Usage lane_id 正式二事 bundled（482） interchangeable / 705 chktxlane-notassigned interchangeable / 704 chktxlane-notreserved interchangeable。**  
   官方把 Usage assigned to default lane 单句和 Check 通过就是已进提案分开。看见放进默认道，不是已经进了块 interchangeable。482 chktxlane vs default bundled unbundling 在本页 item 2 续。

怎样填 lane_id、怎样选 default_lane、怎样写 lane_priorities 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **assigned to default lane not default_lane identifier ≠ 回包写了标识 interchangeable：** 官方把引擎分配默认道和回包里写 default_lane 标识分开。
- **assigned to default lane not Priority consensus order ≠ 317 interchangeable：** 官方把放进默认道和 Priority 就已经是共识顺序分开。
- **assigned to default lane not Check passed is in proposal ≠ 33 interchangeable：** 官方把放进默认道和 Check 通过就是已进提案分开；482 chktxlane vs default bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| assigned to the default lane | 不是 default_lane 标识写进回包 | 不是 empty lane_id（704/482 item 1） |
| 看见放进默认道 | 不是 Priority 就已经是共识顺序（317） | 不是 lane_id in range（706/482 item 3） |
| 看见 Usage 这句 | 不是 Check 通过就是已进提案（33） | 不是 CheckTx Usage lane_id bundled（482） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage assigned to default lane not default_lane identifier / not Priority consensus order / not Check passed is in proposal 正式三事（482 余量），必须分开 assigned 是不是回包写了 default_lane 标识、是不是 Priority 就已经是共识顺序 interchangeable / 317、是不是 Check 通过就是已进提案 interchangeable / 33。可以跳过「看见放进默认道就已经排了优先」。不要另写怎样选 default_lane。482 chktxlane vs default bundled unbundling 在本页 item 2 续；完成 [`worked-example-chktxlane-notrange-vs-bundled.md`](worked-example-chktxlane-notrange-vs-bundled.md)（不变量 706 item 3）。

## 本页不抄

- 怎样填 lane_id、怎样选 default_lane、怎样写 lane_priorities。
- CheckTx Usage lane_id 正式二事 bundled。那是不变量 482。
- empty lane_id。那是不变量 482 item 1 余量 / 704。
- lane_id in ResponseInfo range。那是不变量 482 item 3 余量 / 706。
- CheckTx 的 Priority 就已经是共识顺序。那是不变量 317。
- Check 通过就是已进提案。那是不变量 33。
