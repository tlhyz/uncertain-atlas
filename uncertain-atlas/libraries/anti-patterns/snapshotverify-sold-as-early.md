# 反模式：看见装完又对上就当成已经在装回当中验过 / 看见增量验了 chunk 就当成已经是唯一可信的 AppHash / 看见封禁邻居就当成已经没有快照 DoS

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Verification。  
**例**：[装完又对上 LastBlockAppHash ≠ 已经在装回当中验过](../../tracks/implementation/worked-example-snapshot-verify-vs-early.md)。

## 塌法

1. 看见装完又叫了 `Info` / 看见 `LastBlockAppHash` 对上轻客户端那份，就当成已经在装回当中增量验过，或当成已经进了网。
2. 看见增量验了 chunk / 看见 checksum / 看见绑了默克尔，就当成已经是唯一可信的 AppHash，或当成元数据已经不能伪造。
3. 看见让引擎封禁邻居 / 看见配了受信邻居名单，就当成已经没有快照 DoS，或当成已经收下这个人。

## 为什么会出事

官方写：chunk 都收下之后才叫 Info，对 LastBlockAppHash 和快照高度，是为了进网之前确认应用有效。装回可能很慢，可以在装的过程中另做核对，但唯一可信的仍是 AppHash。对手可以给无效或有害快照；封禁和受信名单是对策，不是已经没有这种 DoS。

## 和相邻反模式

- [snapshotverify-notduringrestore-sold-as-bundled](snapshotverify-notduringrestore-sold-as-bundled.md) 是装完又对上不是已经在装回当中验过 item 1 单句边界，不是本页 Snapshot Verification bundled 全段。
- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是 Offer 收下 ≠ 已经装完，不是本页这种进网前核对。
- [snapshotswitch-sold-as-full-history](snapshotswitch-sold-as-full-history.md) 是装完 ≠ 已经有完整历史，不是本页。
- [peerfilter-sold-as-connected](peerfilter-sold-as-connected.md) 是发了 addr 过滤查询 ≠ 已经收下这个人，不是本页这种快照 DoS。
