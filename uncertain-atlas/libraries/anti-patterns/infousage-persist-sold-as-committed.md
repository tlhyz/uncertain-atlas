# 反模式：把 Info Usage last_block persisted during Commit / lane_priorities 正式三事 part 2 卖成 Info 握手 bundled interchangeable / 已经 Commit 交差 / 已经排了优先

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[last_block persisted during Commit ≠ Info 握手 bundled](../../tracks/implementation/worked-example-infousage-persist-vs-lanebundled.md)。

## 卖法

- 「看见 CometBFT expects last_block_app_hash and last_block_height updated and persisted during Commit / 引擎指望 last_block 在 Commit 里更新并落盘 就已经 Info 握手 bundled（370）第三件事 interchangeable / 已经 Info 回包 last_block 栏 interchangeable / 已经 Commit persist signal bundled interchangeable / 已经交差。」
- 「看见 The application does not have to define lane_priorities / 应用可以不定义 lane_priorities 就已经 Info 车道 bundled（367）第一件事 interchangeable / 已经排了优先 / CheckTx lane_id empty → default lane interchangeable。」
- 「看见 lane_priorities is empty if and only if default_lane is empty / lane_priorities 空当且仅当 default_lane 空 就已经 Info 车道 bundled（367）第二件事 interchangeable / 已经选型 / default_lane must be in lane_priorities interchangeable。」

## 为什么错

官方把 Info Usage 第 4–6 条核心句写成三件独立的实现事。把它们卖成 Info 握手 bundled interchangeable / 已经 Commit 交差 / 已经排了优先，会把 persist during Commit、optional lane_priorities、empty iff 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage last_block persisted during Commit / lane_priorities 正式三事 part 2，必须分开 last_block persisted during Commit、does not have to define lane_priorities、lane_priorities empty iff default_lane empty 三个名字，不要把它们卖成 Info 握手 bundled interchangeable / 已经 Commit 交差 / 已经排了优先。

## 和相邻反模式

- [infousage-sold-as-handshakebundled](infousage-sold-as-handshakebundled.md) 是 Info Usage 正式三事 part 1 就等于 QueryState / bundled / persist，不是本页 part 2 专用边界。
- [info-sold-as-handshake](info-sold-as-handshake.md) 是 Info 握手 bundled 三事，不是本页 Methods Info Usage last_block persist 单句专用边界。
- [infousage-defaultlane-sold-as-priorityzero](infousage-defaultlane-sold-as-priorityzero.md) 是 Info Usage default_lane in table / priority 0 reserved 正式二事 part 3，不是本页 part 2 专用边界。
