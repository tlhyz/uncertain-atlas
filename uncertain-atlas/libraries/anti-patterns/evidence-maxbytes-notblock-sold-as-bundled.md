# 反模式：把 证据 MaxBytes not already block MaxBytes / not already unlimited-minus-one / not already settled 正式三事（331 余量） 卖成 已经是块 MaxBytes / 已经是写成 -1 的那条 / 已经交差

**层次**：实现 / EvidenceParams.MaxBytes。  
**分类**：建议（产品）。  
**对应例**：[worked-example-evidence-maxbytes-notblock-vs-bundled.md](../../tracks/implementation/worked-example-evidence-maxbytes-notblock-vs-bundled.md)。

官方把填了证据 MaxBytes / > 0 / 证据 MaxBytes 三条核心句写成三件独立的实现事。把它们卖成已经是块 MaxBytes / 已经是写成 -1 的那条 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看证据 MaxBytes 正式三事（331 余量），必须分开 not already block MaxBytes、not already unlimited-minus-one、not already settled 三件事，不要和 331 / 63 / 337 / 920 / 921 糊成一句。

## 和相邻反模式

- [evidence-maxbytes-notunbond-sold-as-bundled](evidence-maxbytes-notunbond-sold-as-bundled.md) 是 > 0 仍未盖住解绑单句边界（921 item 2），不是本页证据尺还不是块尺边界。
- 合法范围就已经是默认 21 MB 是不变量 337/919，不是本页证据 MaxBytes 还不是块 MaxBytes 边界。
