# 反模式：看见填了证据 MaxBytes 就当成已经落在块上限下面 / 看见 > 0 就当成已经盖住解绑 / 看见证据 MaxBytes 就当成已经是块 MaxBytes

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / EvidenceParams.MaxBytes。  
**例**：[填了证据 MaxBytes ≠ 已经落在块上限下面](../../tracks/implementation/worked-example-evidence-maxbytes-vs-block.md)。

## 塌法

1. 看见填了 `EvidenceParams.MaxBytes` / 看见一块里证据有上限，就当成已经落在块 MaxBytes 下面，或当成已经扣掉开销。
2. 看见 MaxBytes > 0 / 看见合法，就当成已经盖住解绑，或当成已经够罚。
3. 看见证据 MaxBytes，就当成已经是块 MaxBytes，或当成已经是 -1 无上限，或当成已经是活性 SLA。

## 为什么会出事

官方写：这是单块能交差的证据总字节上限。它应当舒服地落在块最大字节下面，不得超过一块减去开销之后的体积。必须 `MaxBytes > 0`。

## 和相邻反模式

- [evidencemaxbytes-notunder-sold-as-bundled](evidencemaxbytes-notunder-sold-as-bundled.md) 是填了证据 MaxBytes 不是已经落在块上限下面 item 1 单句边界，不是本页 EvidenceParams.MaxBytes bundled 全段。
- [evidencemaxbytes-notunbonding-sold-as-bundled](evidencemaxbytes-notunbonding-sold-as-bundled.md) 是 > 0 不是已经盖住解绑 item 2 单句边界，不是本页 EvidenceParams.MaxBytes bundled 全段。
- [evidencemaxbytes-notblockmax-sold-as-bundled](evidencemaxbytes-notblockmax-sold-as-bundled.md) 是证据 MaxBytes 不是已经是块 MaxBytes item 3 单句边界，不是本页 EvidenceParams.MaxBytes bundled 全段。
- [evidence-sold-as-full-block](evidence-sold-as-full-block.md) 是先装证据 ≠ 已经装满交易、写成 -1 ≠ 已经没有上限，不是本页这种证据体积尺。
- [evidence-default-sold-as-unbonding](evidence-default-sold-as-unbonding.md) 是默认证据窗已经够罚，不是本页。
- [evidence-equals-slash](evidence-equals-slash.md) 是上链已经 slash，不是本页。
