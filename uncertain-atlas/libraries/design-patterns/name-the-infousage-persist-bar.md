# 模式：把 Info Usage last_block persisted during Commit / lane_priorities 正式三事 part 2 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[last_block persisted during Commit ≠ Info 握手 bundled](../../tracks/implementation/worked-example-infousage-persist-vs-lanebundled.md)。

## 三个名字

1. **last_block persisted during Commit 不是 Info 握手 bundled：** 看见 Methods Info Usage expects during Commit，不是 370 bundled 第三件事 interchangeable。
2. **does not have to define lane_priorities 不是 Info 车道 bundled：** 看见 optional lane_priorities，不是 367 bundled 第一件事 interchangeable。
3. **lane_priorities empty iff default_lane empty 不是 Info 车道 bundled：** 看见 empty iff 规则，不是 367 bundled 第二件事 interchangeable。

## 为什么要分开叫

官方把 Info Usage 第 4–6 条、Info Usage part 1（494）、Info 握手 bundled（370）、Info 车道 bundled（367）、Commit persist signal（481）写成三个名字。把它们叫成一个「看见 Info 回了 last_block / 车道 就已经 Commit 交差、已经排了优先、已经选型」，会把 persist during Commit、optional lane_priorities、empty iff 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage last_block persisted during Commit / lane_priorities 正式三事 part 2，先数清问的是 last_block persisted during Commit 是不是 Info 握手 bundled interchangeable / 已经 Commit 交差、does not have to define lane_priorities 是不是 Info 车道 bundled interchangeable / 已经排了优先、lane_priorities empty iff default_lane empty 是不是 Info 车道 bundled interchangeable / 已经选型，再决定要不要同一次发布。
