# 反模式：signedmsgtype-sold-as-verified

**层次**：实现 / SignedMsgType。  
**分类**：反模式（会把三件事写成一件）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) SignedMsgType / Vote / CanonicalVote。  
**例**：[Vote.Type 是这张票的类型 ≠ 已经按那条路径验过](../../tracks/implementation/worked-example-signedmsgtype-vs-verify.md)。

## 病症

把「票上的 `Type` 字段写着 Prevote」写成验签已经走了 prevote 那条路径，或写成块里那张 `Vote` 和签名用的 `CanonicalVote` 是同一个对象、同一套字段顺序，或写成 `SignedMsgType` 枚举里有这三个值就等于域分离已经成立、这张签在别处一定验不过。

## 为什么错

规范把两者分开写：`Vote` 是链上和网络上的票（protobuf 编码），`CanonicalVote` 是**给验证者签名用的表示**，官方明写它**不会出现在块里**，且 `type.SignBytes` 编码时含 `ChainID`、字段顺序也不同。枚举值是枚举值；域分离能不能成立，要看被签字节里到底有没有那一步，那是不变量 19。

## 正确写法

分开三句：Vote.Type 是这张票的类型不是已经按那条路径验过；CanonicalVote.Type 是同一个枚举不是已经是同一个对象；枚举里写着 PREVOTE 不是已经证明签名只在这一步有效。

## 边界

不是 [missing-domain-separation](missing-domain-separation.md)（域分离，不变量 6），不是 [extresp-sold-as-wrap](extresp-sold-as-wrap.md)（那是把扩展签写成 `CanonicalVote`，不变量 34）。投票步类型必须进被签字节是不变量 19，精读见 [`../../tracks/consensus/worked-example-vote-signbytes.md`](../../tracks/consensus/worked-example-vote-signbytes.md)。Commit 每个槽位必须对本块本 ChainID 有效是不变量 65。

## 本页不抄

- 怎样编 `SignedMsgType`、怎样构造 `CanonicalVote`、怎样算 `SignBytes`。
- 怎样写利用步骤。
