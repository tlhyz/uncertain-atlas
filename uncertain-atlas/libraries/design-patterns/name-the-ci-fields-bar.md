# 模式：把 CommitInfo Fields 栏正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types CommitInfo Fields。  
**例**：[CommitInfo.round 是提交轮 ≠ 已经按投票权排过](../../tracks/implementation/worked-example-cifields-vs-notes.md)。

## 三个名字

1. **CommitInfo.round 是提交轮不是已经按投票权排过 / 已经罚没：** 看见填了 round 不是 Notes 票序。
2. **CommitInfo.votes 是上一验证者集合里各人的投票信息不是已经进了块 / 已经交差：** 看见 Fields 里 votes 不是已经写进 last_commit。
3. **Fields 栏描述 round 和 votes 不是已经是 CommitInfo Notes 那套票序话：** 看见 Fields 表不是 interchangeable with Notes。

## 为什么要分开叫

官方把 CommitInfo Fields 里 round 含义、votes 列表含义、Fields 与 Notes 分开写写成三个名字。把它们叫成一个「看见 Process / Finalize 里有 CommitInfo 就已经填了提交轮、已经按投票权排好」，会把 Fields 栏和 Notes 票序一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Process / Finalize 里有 CommitInfo 就已经填了提交轮」，先数清问的是 CommitInfo.round 是提交轮不是已经按投票权排过 / 已经罚没、CommitInfo.votes 是上一验证者集合里各人的投票信息不是已经进了块 / 已经交差，还是 Fields 栏描述 round 和 votes 不是已经是 CommitInfo Notes 那套票序话，再决定要不要同一次发布。
