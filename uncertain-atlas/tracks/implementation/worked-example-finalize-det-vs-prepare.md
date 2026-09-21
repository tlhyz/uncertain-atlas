# 例：看见 Finalize 算出的状态必须只依赖上一份状态和决定块不是已经可以像 Prepare 那样依赖其它值；看见 Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头；看见两边状态机复制不是已经是 Process 对任意块同一裁决

**层次**：实现 / FinalizeBlock 确定性。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 11–12 [`FinalizeBlock`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Finalize 算出的状态必须只依赖上一份状态和决定块不是已经可以像 Prepare 那样依赖其它值 / Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头 / 两边状态机复制不是已经是 Process 对任意块同一裁决」，不是 Prepare 没有确定性要求，也不是回执已经交差。不要另写怎样写 FinalizeBlock。 342 finalizedet vs prepare bundled unbundling 启动（779）；精读 [`worked-example-finalize-notlikeprepare-vs-bundled.md`](worked-example-finalize-notlikeprepare-vs-bundled.md)（不变量 779 item 1）。

## 官方三件事

规范把 Finalize 的确定性写成三件独立的实现事，不是「看见必须确定就已经可以像 Prepare 那样、已经印进本头、已经是 Process 同判」一件事：

1. **看见 `FinalizeBlock` 算出的状态必须只依赖上一份状态和决定块 / 看见必须确定 不是已经可以像 Prepare 那样依赖其它值，也不是已经和 Prepare / ExtendVote 同一把尺。**  
   官方写：正确进程 *p* 在高度 *h* 叫 `FinalizeBlock`，把决定块 *v_{p,h}* 交进去，**造出**状态 *s_{p,h}*。Requirement 11：*s_{p,h}* **只**依赖 *s_{p,h-1}* 和 *v_{p,h}*。看见必须确定，不是已经可以依赖其它值或操作。看见只依赖上一份状态和决定块，不是已经和「Prepare 没有确定性要求」同一句。看见 Finalize 回了，不是已经交差。
2. **看见 Finalize 算出的结果必须只依赖上一份状态和决定块 / 看见 *T_h* 必须确定 不是已经是 Code/Data 印进本头，也不是已经是列表同一顺序。**  
   官方写：同一次 `FinalizeBlock` **另外**造出交易结果集合 *T_{p,h}*。Requirement 12：*T_{p,h}* 的内容 **只**依赖 *s_{p,h-1}* 和 *v_{p,h}*。看见结果必须确定，不是已经印进本头。看见只依赖这两份，不是已经是回执顺序对上。看见造出了 *T*，不是已经落盘。
3. **看见两边状态机复制 / 看见应用状态一起演化 不是已经是 Process 对任意块同一裁决，也不是已经有协议层补丁。**  
   官方写：Requirement 11 和 12 再加上共识的 Agreement，保证**状态机复制**：各正确进程上的应用状态一起演化。看见状态机复制，不是已经是 Process 对任意块同一 Accept/Reject。看见两边状态一起走，不是已经是 Prepare 可以不确定。看见 Agreement，不是已经交差。

怎样写 `FinalizeBlock`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。Prepare 没有确定性要求是不变量 338，本页不抄。

## 官方为什么这样拆

- **Finalize 算出的状态必须只依赖上一份状态和决定块 ≠ 已经可以像 Prepare 那样依赖其它值：** 官方把 Finalize 必须确定和 Prepare 可以不确定分开。
- **Finalize 算出的结果必须只依赖上一份状态和决定块 ≠ 已经是 Code/Data 印进本头：** 官方把结果集合的确定性和回执字段怎么进头分开。
- **两边状态机复制 ≠ 已经是 Process 对任意块同一裁决：** 官方把状态一起演化和提案裁决同判分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 算出的状态必须只依赖上一份状态和决定块 | 不是已经可以像 Prepare 那样依赖其它值 | 不是 Prepare 没有确定性要求（338） |
| Finalize 算出的结果必须只依赖上一份状态和决定块 | 不是已经是 Code/Data 印进本头 | 不是结果列表已经同一顺序（316） |
| 两边状态机复制 | 不是已经是 Process 对任意块同一裁决 | 不是 Process 必须只依赖请求和上一份状态（340） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见必须确定就已经可以像 Prepare 那样、已经印进本头、已经是 Process 同判」，必须分开 Finalize 算出的状态必须只依赖上一份状态和决定块是不是已经可以像 Prepare 那样依赖其它值、Finalize 算出的结果必须只依赖上一份状态和决定块是不是已经是 Code/Data 印进本头、两边状态机复制是不是已经是 Process 对任意块同一裁决。可以跳过「看见必须确定就已经可以像 Prepare 那样」。不要把造出 *s_h* 当已经落盘。不要另写怎样写 FinalizeBlock。 342 finalizedet vs prepare bundled unbundling 启动（779 item 1）；续 [`worked-example-finalize-notprinted-vs-bundled.md`](worked-example-finalize-notprinted-vs-bundled.md)（不变量 780 item 2）。

## 本页不抄

- 怎样写 `FinalizeBlock`、怎样测确定性、怎样写测试向量。
- Prepare 没有确定性要求。那是不变量 338。
- 结果列表已经同一顺序。那是不变量 316。
- Process 必须只依赖请求和上一份状态。那是不变量 340。
