# 例：看见空 `lane_id` 不是已经 priority 0 留给不设道 / 已经从池里删掉；看见 assigned to the default lane 不是已经是 `default_lane` 标识 / 已经排了优先；看见必须在 `ResponseInfo` 车道范围内 不是已经在 Info 表就算选型 / 已经 CheckTx 回包栏 interchangeable

**层次**：实现 / CheckTx Usage lane_id 正式二事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「空 lane_id 不是 priority 0 留给不设道 / assigned to default lane 不是 default_lane 标识 / 必须在 ResponseInfo 范围内不是 Info 表选型 interchangeable」，不是 Info 车道 bundled 三事，也不是 CheckTx 回包栏 bundled 三事。不要另写怎样填 lane_id、怎样选 default_lane。

## 官方两件事

规范把 CheckTx Usage 里空 `lane_id` 分配默认道、非空 `lane_id` 必须在 Info 定义范围内写成两件独立的实现事，不是「看见 CheckTx 回了 lane_id 就已经不设道、已经排了优先、已经在 Info 表范围内交差」一件事：

1. **看见 `lane_id` 是空字符串 / 看见应用没在 CheckTx 回包里设道 不是已经 priority 0 留给不设道（367）那种不设道 interchangeable，也不是已经从池里删掉 / 已经没进池；看见 the transaction will be assigned to the default lane / 看见会放进默认道 不是已经是 `default_lane` 那个标识本身写进了回包，也不是已经排了优先 / 已经进了块。**  
   官方 Usage 写：If `lane_id` is an empty string, it means that the application did not set any lane in the response message, so the transaction will be assigned to the default lane。看见 empty string，不是已经 Info Usage 里 priority 0 留给不设道（367）那种「空 lane_id = 不设道语义」 interchangeable——367 钉 Info 侧预留，本页钉 CheckTx Usage 侧引擎分配。看见没在回包里设道，不是已经从池里删掉。看见 assigned to the default lane，不是已经回包里写了 `default_lane` 那个字符串。看见放进默认道，不是已经 CheckTx 的 Priority 就已经是共识顺序（317） interchangeable。
2. **看见 The value of `lane_id` has to be in the range of lanes defined by the application in `ResponseInfo` / 看见填了道必须在 Info 定义过的车道范围内 不是已经在 Info 回了 `lane_priorities` / `default_lane` 就算选型交差，也不是已经 CheckTx 回包栏 bundled（381）里那句就代表 Usage 已经验完 interchangeable。**  
   官方 Usage 写：The value of `lane_id` has to be in the range of lanes defined by the application in `ResponseInfo`。看见 in the range of lanes defined in ResponseInfo，不是已经 Info 车道表对上了（367）那种空表对空默认 / 没填表就已经排了优先 interchangeable。看见必须在范围内，不是已经填了 lane_id 在表里就代表已经排了优先。看见 Usage 这句，不是已经 CheckTx Response 表 `lane_id` 栏（381） bundled 第三件事 interchangeable——381 钉 Response 字段描述，本页钉 CheckTx Usage 侧约束。

怎样填 `lane_id`、怎样选 `default_lane`、怎样写 `lane_priorities` 是规范里的做法，本页不抄。Info 车道（367）是应用可以不定义 lane_priorities / 空表对空默认 / priority 0 留给不设道那套另一切片，CheckTx 回包（381）是 codespace / events / lane_id 必须在 Info 范围那套另一切片，CheckTx 的 Priority 不是共识顺序（317）是 Priority 字段那套另一切片，本页不抄。

## 官方为什么这样拆

- **空 lane_id → assigned to default lane ≠ priority 0 留给不设道 / 已经从池里删掉：** 官方把 CheckTx Usage 侧引擎分配默认道和 Info 侧 priority 0 预留、池门结果分开。
- **lane_id in ResponseInfo range ≠ Info 表选型 / CheckTx 回包栏 interchangeable：** 官方把 Usage 侧范围约束和 Info 配置、Response 字段 bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| empty lane_id → default lane | 不是 priority 0 留给不设道 | 不是 Info 车道（367） |
| assigned to default lane | 不是 default_lane 标识 / 已经排了优先 | 不是 CheckTx Priority 共识顺序（317） |
| lane_id in ResponseInfo range | 不是 Info 表选型交差 | 不是 CheckTx 回包栏（381） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 CheckTx 回了 lane_id 就已经不设道、已经排了优先、已经在 Info 表范围内交差」，必须分开 empty lane_id 是不是 assigned to default lane 而不是 priority 0 不设道 / 已经从池里删掉、assigned to default lane 是不是 default_lane 标识 / 已经排了优先、lane_id in ResponseInfo range 是不是 Info 表选型 / CheckTx 回包栏 interchangeable。可以跳过「看见 CheckTx 回了 lane_id 就已经排了优先」。不要另写怎样填 lane_id。

## 本页不抄

- 怎样填 `lane_id`、怎样选 `default_lane`、怎样写 `lane_priorities`。
- Info 车道。那是不变量 367。
- CheckTx 回包栏。那是不变量 381。
- CheckTx 的 Priority 就已经是共识顺序。那是不变量 317。
- CheckTx 技术上可选、不参与处理块。那是不变量 373。
