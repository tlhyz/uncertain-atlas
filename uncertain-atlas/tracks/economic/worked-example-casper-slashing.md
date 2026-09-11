# 工作实例：两张签可罚，必须能指出是哪一种关系

> **事实 / 推断 / 建议** 已分开。
> 对照：[证据 ≠ 罚没](worked-example-evidence.md)、[投票 SignBytes](../consensus/worked-example-vote-signbytes.md)、[Altair 抽样](../light-clients/worked-example-sync-committee.md)、[phase0 `is_slashable_attestation_data`](https://github.com/ethereum/consensus-specs/blob/master/specs/phase0/beacon-chain.md)。
> 本页钉 **Casper FFG 的两票关系** 和 **谁执行 slash**。不抄现行罚金、不抄现网验证者人数。

---

## 0. 先修

- [L4.3 锁](../../courses/level-04-bft/L04-M03-locks.md)
- [L5.2 最终性](../../courses/level-05-ethereum/L05-M02-el-cl-finality.md)
- [L9.5 经济](../../courses/level-09-systems/L09-M05-economic-security.md)
- [不变式 21](../../libraries/invariants/README.md#21-双签证据形状成立-已罚没)

---

## 1. 核心问题

阿比看见两张验证者签名，说「双签，该罚」。

可能是四件不同的事：

1. 同一 target epoch，两份不同的 `AttestationData`（Casper **double vote**）。
2. 一份证明的 source/target **包住**另一份（Casper **surround vote**）。
3. 同一 slot 两份不同的信标头（**proposer slashing**）。
4. CometBFT：同一 height / round / Type，两个 `BlockID`（证据形状，应用再决定罚不罚）。

「两张签」四个字不够。必须能指出是哪一种关系、由谁改余额。

---

## 2. 直觉（ELI15）

班委对「本周课表」盖了两个不同的章——同一周两套课表。这是双投。  
班委先说「第 3 周到第 10 周锁定」，后来又说「第 5 周到第 7 周锁定」——小区间被大区间包住。这是包围。  
班长同一节课贴了两张不同的黑板。这是提议者双块。

三种都可罚，公式不同。同步委员会举手（Altair）**没有**写进同一套公式。

---

## 3. 正式对象（phase0 规范，事实）

### 3.1 证明是否可罚：`is_slashable_attestation_data`

```text
double:  data_1 != data_2 且  data_1.target.epoch == data_2.target.epoch
surround: data_1.source.epoch < data_2.source.epoch
          且 data_2.target.epoch < data_1.target.epoch
```

规范注释写明：这是 **Casper FFG rules**。

**事实：** surround 子句**不是对称的**。`process_attester_slashing` 只调用

`is_slashable_attestation_data(attestation_1.data, attestation_2.data)`

因此容器里必须让 **第一份包住第二份**（或两份构成 double）。若只有第二份包住第一份，这条 process 会 assert 失败。提交者要把「外包住」的那份放在 `attestation_1`。

### 3.2 人是否还能被罚：`is_slashable_validator`

```text
未 slashed
且 activation_epoch <= 当前 epoch < withdrawable_epoch
```

过了 `withdrawable_epoch`，协议不再用这条路径罚他——和弱主观性「旧钥匙已解绑」是同一经济牙的另一面。

### 3.3 谁执行 slash

`process_attester_slashing` / `process_proposer_slashing` 在**信标状态机里**调用 `slash_validator`。  
这是**协议层**改验证者记录，不是「引擎交个证据，应用看着办」。

`process_attester_slashing` 还要求：两份都是合法的 indexed attestation；交集里至少有一人当时 `is_slashable_validator`，否则整条操作失败。

### 3.4 提议者

`process_proposer_slashing`：两个 `SignedBeaconBlockHeader` 的 **slot 相同、proposer_index 相同、header 不同**，域是 `DOMAIN_BEACON_PROPOSER`，然后 `slash_validator`。

这不是 attestation 的 double/surround。域不同，见 [SignBytes 精读](../consensus/worked-example-vote-signbytes.md)。盲头也是头：签了 `SignedBlindedBeaconBlock` 再签另一份同 slot 头，仍走这条，见 [谁排序](../mempool/worked-example-who-orders.md)。

---

## 4. 对照表

| | Casper 证明罚没 | Casper 提议罚没 | CometBFT 双签证据 | Altair 同步委员会 |
|--|-----------------|-----------------|-------------------|-------------------|
| 可罚关系 | 同 target epoch 不同 data，或 1 包住 2 | 同 slot 两份不同头 | 同 height/round/Type，不同 BlockID | 稳定规范**没有** surround/double |
| 谁改余额 | 信标 `slash_validator` | 同上 | 引擎交 `Misbehavior`，**应用**写公式 | 无这一刀 |
| 域 | `DOMAIN_BEACON_ATTESTER` | `DOMAIN_BEACON_PROPOSER` | `CanonicalVote` 的 Type + chain_id | `DOMAIN_SYNC_COMMITTEE` |
| 「两张签」够不够 | 不够，要能对上上面两行之一 | 不够，要同 slot | 不够，还要 Type 相同 | 两张聚合也不自动可罚 |

EigenLayer 的 AVS 罚没是第四列亲戚：产品定义、不必客观可归属，见 [过滤器](../../protocols/eigenlayer/README.md)。

---

## 5. 攻击者

| 攻击 | 机制 | 规范挡的 | 规范挡不住的 |
|------|------|----------|--------------|
| 把任意两张签当 Casper 可罚 | 文案 | 只有 double / surround / 同 slot 双头 | 用户以为「签了两次就罚」 |
| surround 放反 | 外包住的那份放在 attestation_2 | process assert 失败，不上链 | 监视器以为「链拒绝惩罚」= 协议没有 surround |
| 已 slashed 或已可取款 | 再交一份 | `is_slashable_validator` 为假；证明路径还要求至少罚到一人 | 经济上人已经走了（弱主观亲戚） |
| 同步委员会作恶 | 抽样签假头 | — | 没有 attestation 那一套罚没（见抽样精读 / EIP-8390 草案主张） |
| 抄罚金数字 | 官网或某分叉的 quotient | — | 公式随分叉变；本页不填 |

---

## 6. 五层

| 层 | 本页能说的 | 不能说的 |
|----|------------|----------|
| 密码学 | 两份 σ 都要在正确域上为真 | 「BLS 自动罚双签」 |
| 协议 | 上面三行谓词；信标状态执行 slash | 现行罚多少 ETH |
| 实现 | 客户端是否把 surround 顺序放对 | 没读实现就写「都会罚」 |
| 部署 | 谁打包 slashing 进块（审查） | 「主网一定会收进下一块」 |
| 经济 | 牙在 withdrawable 之前；CometBFT 牙在应用 | 某年发行量、罚没总额 |

---

## 7. 对不确定的意义（建议）

- 结算机若有验证者票：先写 **可客观检查的两票关系**（至少「同高同轮同步不同类型值」或「同 epoch 两 checkpoint」），再写谁执行。
- 不要默认抄 surround。抄了就要写清容器顺序是否对称。
- CometBFT 骨架：证据在引擎，公式在 ABCI（不变量 21）。不要假装信标那种「协议内 slash_validator」已经存在。
- 同步委员会式抽样若存在，不要在文档里写「和证明同一刀」。
- 不填罚金数字，直到有自己的状态机和测试向量。

---

## 8. 禁句

- 「双签就会被罚」（不写是 double、surround、同 slot 头，还是应用裁量）
- 「和 CometBFT 一样，证据一上链就 slash」
- 「同步委员会也有 surround」
- 把某分叉的罚金商、现网罚没总额当规范永恒值
- 把 surround 写成对称关系（phase0 的 process 只测 1 包住 2）
