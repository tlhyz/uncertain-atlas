# 模式：把 BlockParams.MaxBytes 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**例**：[-1 就按 100 MB 验 ≠ 已经没有上限](../../tracks/implementation/worked-example-maxbytes-cap-vs-unlimited.md)。

## 三个名字

1. **-1 就按 100 MB 验不是已经没有上限：** 看见引擎按 100 MB 验不是应用已经可以随便回。
2. **应用自己卡体积不是已经引擎不管了：** 看见 MAY 写成 -1 不是已经没有 100 MB 那把尺。
3. **必须 -1 或不超过 100 MB 不是已经是默认 21 MB：** 看见默认能接到 21 MB 不是已经评估过带宽。

## 为什么要分开叫

官方把 -1 仍按 100 MB 验、应用侧上限、合法范围和默认 21 MB 写成三件事。把它们叫成一个「看见写成 -1 就已经没有上限」，会把整池交给 Prepare、活性 SLA 和证据体积上限一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「写成 -1 就已经没有上限」，先数清问的是 -1 就按 100 MB 验不是已经没有上限、应用自己卡体积不是已经引擎不管了，还是必须 -1 或不超过 100 MB 不是已经是默认 21 MB，再决定要不要同一次发布。
