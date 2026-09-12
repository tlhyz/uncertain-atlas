# 反模式：默认证据窗被写成已经盖住解绑

> 真值：[证据窗精读](../../tracks/economic/worked-example-evidence-window.md)、[ASA-2024-004](../../tracks/failure-museum/asa-2024-004.md)、[不变式 46](../invariants/README.md#46-证据有效窗必须盖住解绑且过期是合取)。

## 一句话

看见 `EvidenceParams` 有默认值，就写成「双签在解绑前都能罚」。

## 正确写法

「过期是高度且时间都超过。默认两参数可能短于解绑（ASA-2024-004，无代码补丁）。窗必须按解绑重算；大于零不是盖住。」
