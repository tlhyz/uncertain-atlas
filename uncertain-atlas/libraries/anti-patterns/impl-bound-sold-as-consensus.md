# 反模式：impl-bound-sold-as-consensus

**层次**：实现 / 同步参数上界。  
**分类**：反模式（会把三件事写成一件）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) SynchronyParams。  
**例**：[precision 上界 30s ≠ 已经是协议常数](../../tracks/implementation/worked-example-synchrony-bounds-vs-consensus.md)。

## 病症

把 `precision ≤ 30s` / `message_delay ≤ 24h` 这两个数抄成共识常数或产品建议值，或把「在实现里强制」写成「协议保证」，或把「防溢出」这个目的写成「活性 / 安全下界」，或在没有出处与版本的情况下把这两个数当成跨实现通用的界。

## 为什么错

官方原文把这两个上界写成 `Note:`：**在实现里强制的上界，目的是防止时间戳校验时的溢出错误**。它防的是本实现算时间戳溢出，不是投票决定的共识规则；守卫存在也不告诉你 `precision` 该填多少。把实现上限当共识，正是 GOAL.md 列入失败清单的第 6 类混用。

## 正确写法

分开三句：precision 上界 30s 不是已经是协议常数；写的是实现强制不是已经进了共识；防溢出不是已经选型。若要引用数字，标明是 CometBFT 实现的上界并写出处与版本。

## 边界

不是 [precision-sold-as-msgdelay](precision-sold-as-msgdelay.md)（那是 `Precision` 不是已经 `MessageDelay`，不变量 336），不是 [pbtsheight-sold-as-enabled](pbtsheight-sold-as-enabled.md)（那是写成 0 不是已经启用 PBTS，不变量 343），不是 [default-sold-as-cap](default-sold-as-cap.md)（那是客户端默认气限不是协议帽，不变量 211）。

## 本页不抄

- 怎样设 `precision` / `message_delay`、怎样选启用高度。
- 怎样写利用步骤。
