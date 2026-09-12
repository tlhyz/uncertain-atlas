# 模式：把 Snapshot Verification 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Verification。  
**例**：[装完又对上 LastBlockAppHash ≠ 已经在装回当中验过](../../tracks/implementation/worked-example-snapshot-verify-vs-early.md)。

## 三个名字

1. **装完又对上不是已经在装回当中验过：** 看见 LastBlockAppHash 对上轻客户端那份不是已经进了网。
2. **增量验了 chunk 不是已经是唯一可信的 AppHash：** 看见 checksum 过了不是元数据已经不能伪造。
3. **封禁邻居不是已经没有快照 DoS：** 看见配了受信名单不是已经是过滤已经收下。

## 为什么要分开叫

官方把进网前最后一次 Info、装回当中可以早发现失败、封禁 / 受信名单写成三件事。把它们叫成一个「看见对上就已经早验过」，会把装回、切进共识和邻居过滤一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「快照已经对上就已经早验过」，先数清问的是装完又对上不是已经在装回当中验过、增量验了 chunk 不是已经是唯一可信的 AppHash，还是封禁邻居不是已经没有快照 DoS，再决定要不要同一次发布。
