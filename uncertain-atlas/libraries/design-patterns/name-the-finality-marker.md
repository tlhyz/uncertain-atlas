# 模式：头上的最终标记必须点名是哪一枚

**问题：** 同一头里同时印「较快的确认」和「更强的 BFT 最终」，产品却只说「最终」。RPC 再叠 `optimistic` / `near-final` / `final`，用户只看见一盏绿。  
**方案：** 每个「到了」先点名问的是哪一枚头哈希、哪一条谓词、哪一档 RPC。较快标记与 BFT 谓词分开写。  
**适用：** 双最终标记、任何「快确认 + 慢最终」印在同一个对象上的结算文案。  
**优点：** 用户能指出绿勾对应哪一枚哈希；不会把较快章听成 commit。  
**缺点：** 句子变长；不能再用「秒最终」交差。  
**项目：** NEAR：`last_ds_final_block`（doomslug finality）≠ `last_final_block`（full BFT finality）；Nomicon 谓词是连续两高度。  
**常见 bug：** 两枚写成一枚；`near-final` 写成已经 `final`；出新头写成已经 commit。  
**不确定：** 可以参考「最终标记必须点名」；第一版不要同时卖两枚头哈希。见 [工作实例](../../tracks/finality/worked-example-doomslug-vs-bft.md)。
