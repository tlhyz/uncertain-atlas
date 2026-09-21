# 反模式：看见 -1 就按 100 MB 验就当成已经没有上限 / 看见应用自己卡体积就当成已经引擎不管了 / 看见必须 -1 或不超过 100 MB 就当成已经是默认 21 MB

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**例**：[-1 就按 100 MB 验 ≠ 已经没有上限](../../tracks/implementation/worked-example-maxbytes-cap-vs-unlimited.md)。

## 塌法

1. 看见 `MaxBytes` 写成 -1 / 看见引擎按 100 MB 验，就当成已经没有上限，或当成应用已经可以随便回。
2. 看见应用自己卡体积 / 看见 MAY 写成 -1，就当成已经引擎不管了，或当成已经只有应用这一把尺。
3. 看见必须 `MaxBytes == -1` 或 `0 < MaxBytes <= 100 MB` / 看见默认能接到 21 MB，就当成已经是默认 21 MB，或当成已经评估过带宽。

## 为什么会出事

官方写：写成 -1 时，共识仍把实际要验的值当成 100 MB，并把整池交给 Prepare。应用自己卡体积时 MAY 写成 -1，引擎那把 100 MB 尺还在。合法取值只能是 -1 或不超过 100 MB；默认 21 MB 若没评估过带宽，建议下调。

## 和相邻反模式

- [maxbytes-notengineoff-sold-as-bundled](maxbytes-notengineoff-sold-as-bundled.md) 是应用自己卡体积不是已经引擎不管了 item 2 单句边界，不是本页 MaxBytes cap bundled 全段。
- [maxbytes-notunlimited-sold-as-bundled](maxbytes-notunlimited-sold-as-bundled.md) 是 MaxBytes 写成 -1 就按 100 MB 验不是已经没有上限 item 1 单句边界，不是本页 MaxBytes cap bundled 全段。
- [evidence-sold-as-full-block](evidence-sold-as-full-block.md) 是整池都给 Prepare ≠ 已经没有上限，不是本页这种 100 MB 引擎帽。
- [maxbytes-sold-as-sla](maxbytes-sold-as-sla.md) 是仓库默认 MaxBytes ≠ 已经是活性 SLA，不是本页这种合法范围 ≠ 默认 21 MB。
- [evidencemaxbytes-sold-as-blockmax](evidencemaxbytes-sold-as-blockmax.md) 是证据 MaxBytes ≠ 已经是块 MaxBytes，不是本页。
