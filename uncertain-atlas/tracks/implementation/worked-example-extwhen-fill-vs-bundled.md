# 例：看见 sets ExtendVoteResponse.extension into CanonicalVoteExtension.extension / populates other fields / signs populated CanonicalVoteExtension 不是已经 return extension bundled interchangeable / 已经 ExtendVote When 正式流程 bundled interchangeable / 已经按原样签 interchangeable

**层次**：实现 / ExtendVote When fill CanonicalVoteExtension 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 4。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「sets extension into CanonicalVoteExtension / populates other fields / signs populated structure 不是 return extension bundled interchangeable / 不是 ExtendVote When 正式流程 bundled interchangeable / 不是按原样签 interchangeable」，不是 ExtendVote When return extension（509），也不是 ExtendVote When 正式流程（438）。不要另写怎样填 CanonicalVoteExtension、怎样构造 CanonicalVote、怎样广播 Precommit。

## 官方三件事

规范把 ExtendVote When step 4 里把 extension 填进 CanonicalVoteExtension、填其它字段、签 populated 结构写成三件独立的实现事，不是「看见回了 extension 就已经按原样签 interchangeable、已经验过扩展 interchangeable、已经 ExtendVote 回了 extension 就已经广播 Precommit interchangeable」一件事：

1. **看见 _p_ sets `ExtendVoteResponse.extension` as the value of the `extension` field of type `CanonicalVoteExtension` / 看见把 ExtendVoteResponse.extension 填进 CanonicalVoteExtension 的 extension 字段 不是已经 Application returns extension bytes bundled（509） interchangeable / 已经 not interpreted interchangeable，也不是已经 vote_extension 会包进 CanonicalVoteExtension（358） interchangeable / 已经按原样签 interchangeable，也不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经填进包装并签名 interchangeable / 已经广播 Precommit interchangeable，也不是已经 application-generated will be signed（439） interchangeable / 已经签过 interchangeable。**  
   官方 When step 4 写：_p_ sets `ExtendVoteResponse.extension` as the value of the `extension` field of type `CanonicalVoteExtension`。看见 sets extension into CanonicalVoteExtension.extension，不是已经 Application returns ExtendVoteResponse.extension（509） interchangeable——509 钉 step 3 return 单句，本页钉 step 4 填 extension 字段单句。看见填进 extension 字段，不是已经 vote_extension 会包进 CanonicalVoteExtension（358） interchangeable——358 钉 Usage 侧会包进包装，本页钉 When step 4 填字段单句。看见 sets as value of extension field，不是已经按应用给的字节原样签（438 第一件事） interchangeable——438 钉 When 正式流程 bundled，本页钉 step 4 填 extension 字段单句。
2. **看见 populates the other fields in `CanonicalVoteExtension` / 看见填 Height、Round、ChainID 等其它字段 不是已经 ExtendVoteResponse.extension 就是 CanonicalVoteExtension interchangeable / 已经只有 extension 字段 interchangeable，也不是已经 ExtendVoteRequest 请求栏 bundled（410） interchangeable / 已经 hash/height/time interchangeable，也不是已经 return extension bundled（509） interchangeable / 已经 not interpreted interchangeable，也不是已经 Construct and sign CanonicalVote bundled（438） interchangeable / 已经验过扩展 interchangeable。**  
   官方 When step 4 续：populates the other fields in `CanonicalVoteExtension`。看见 populates other fields，不是已经只有 extension 字节（509） interchangeable——509 钉 return+不解释，本页钉 step 4 populate 其它字段单句。看见 Height、Round、ChainID 等，不是已经 ExtendVoteRequest.hash/height/time（410） interchangeable——410 钉 Request 栏，本页钉 When step 4 populate CanonicalVoteExtension 字段。看见填其它字段，不是已经构造 CanonicalVote（438 第二件事） interchangeable——438 钉 bundled 三事，本页钉 step 4 populate 单句。
3. **看见 and signs the populated data structure / 看见签这份 populated CanonicalVoteExtension 结构 不是已经按原样签 application bytes interchangeable / 已经广播 Precommit interchangeable，也不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经构造 CanonicalVote interchangeable / 已经验过扩展 interchangeable，也不是已经 return extension bundled（509） interchangeable / 已经包进 CanonicalVoteExtension interchangeable，也不是已经 Verify 过他人扩展（353） interchangeable / 已经 Accept interchangeable。**  
   官方 When step 4 续：and signs the populated data structure。看见 signs populated CanonicalVoteExtension，不是已经按应用给的字节原样签（438 第一件事 bundled） interchangeable——438 钉填包装并签名 bundled，本页钉 step 4 signs populated structure 单句。看见签了 populated 结构，不是已经构造并签名 CanonicalVote（438 第二件事） interchangeable——438 钉 bundled，本页钉 step 4 sign CanonicalVoteExtension 单句。看见 signs，不是已经广播 Precommit（438 第三件事） interchangeable——438 钉构造 Precommit 并广播，本页钉 step 4 sign 单句。

怎样做填 CanonicalVoteExtension、怎样构造 CanonicalVote、怎样广播 Precommit 是规范里的做法，本页不抄。ExtendVote When return extension（509）、ExtendVote When 正式流程（438）、vote_extension 会包进 CanonicalVoteExtension（358）是另外那套，本页不抄。

## 官方为什么这样拆

- **sets extension into CanonicalVoteExtension.extension ≠ return extension bundled interchangeable：** 官方把 step 4 填 extension 字段单句和 step 3 return bundled 分开。
- **populates other fields ≠ ExtendVoteRequest 栏 bundled interchangeable：** 官方把 populate CanonicalVoteExtension 其它字段和 Request 栏 bundled 分开。
- **signs populated CanonicalVoteExtension ≠ ExtendVote When 正式流程 bundled interchangeable：** 官方把 step 4 sign 单句和 steps 5–7 构造 CanonicalVote/Precommit bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| sets extension into CanonicalVoteExtension.extension | 不是 return extension bundled（509） | 不是 vote_extension 会包进包装（358） |
| populates other fields in CanonicalVoteExtension | 不是只有 extension 字节 | 不是 ExtendVoteRequest 栏（410） |
| signs populated CanonicalVoteExtension | 不是按原样签 application bytes | 不是构造 CanonicalVote bundled（438） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When fill CanonicalVoteExtension 正式三事，必须分开 sets extension into CanonicalVoteExtension.extension 是不是 return extension bundled interchangeable、populates other fields 是不是 ExtendVoteRequest 栏 bundled interchangeable、signs populated CanonicalVoteExtension 是不是 ExtendVote When 正式流程 bundled interchangeable / 已经按原样签 interchangeable。可以跳过「看见回了 extension 就已经按原样签 interchangeable、已经验过扩展 interchangeable、已经 ExtendVote 回了 extension 就已经广播 Precommit interchangeable」。不要另写怎样填 CanonicalVoteExtension。

## 本页不抄

- 怎样做填 CanonicalVoteExtension、怎样构造 CanonicalVote、怎样广播 Precommit。
- ExtendVote When return extension。那是不变量 509。
- ExtendVote When 正式流程 / 构造 CanonicalVote / 广播 Precommit。那是不变量 438。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。那是不变量 358。
