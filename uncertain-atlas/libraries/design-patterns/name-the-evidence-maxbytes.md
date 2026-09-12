# 模式：把 EvidenceParams.MaxBytes 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / EvidenceParams.MaxBytes。  
**例**：[填了证据 MaxBytes ≠ 已经落在块上限下面](../../tracks/implementation/worked-example-evidence-maxbytes-vs-block.md)。

## 三个名字

1. **填了证据 MaxBytes 不是已经落在块上限下面：** 看见一块里证据有上限不是已经扣掉开销。
2. **> 0 不是已经盖住解绑：** 看见合法不是已经够罚。
3. **证据 MaxBytes 不是已经是块 MaxBytes：** 看见填了数不是已经是写成 -1 的那条，也不是已经是活性 SLA。

## 为什么要分开叫

官方把单块证据总字节、必须大于 0、不得超过块减去开销写成三件事。把它们叫成一个「看见填了证据体积就已经和块上限同一把尺」，会把造提案收交易、证据窗和活性 SLA 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「填了证据体积就已经落在块上限下面」，先数清问的是填了证据 MaxBytes 不是已经落在块上限下面、> 0 不是已经盖住解绑，还是证据 MaxBytes 不是已经是块 MaxBytes，再决定要不要同一次发布。
