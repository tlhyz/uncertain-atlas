# 反模式：KZG 承诺被写成纠删 DAS（或永存档案）

> **事实 / 推断 / 建议** 已分开。
> 真值：[blob ≠ DAS 精读](../../tracks/light-clients/worked-example-blob-vs-das.md)、[L7.2](../../courses/level-07-modular/L07-M02-data-availability.md)、[不变式 23](../invariants/README.md#23-短时承诺不是永存-da且-kzg-不是纠删-das)。

---

## 一句话

头里有 `blob_kzg_commitments` 或 versioned hash，文案写成「我们已经做了 DAS」或「数据永远可取」。

---

## 它看起来像什么

- 「以太坊有 blob 所以和 Celestia 一种数据可用」
- 「L1 已最终确定，L2 批次永久可重建」
- 「PeerDAS 抽了几列，所以这笔 L2 转账执行正确」
- 把 Deneb 的 `MAX_BLOBS_PER_BLOCK = 6`（或后来某次参数）抄进白皮书当永恒吞吐

---

## 为什么有人会这么写

EIP-4844 的动机就是给 rollup 送数据。Fulu 又把 `is_data_available()` 换成抽样。三句话都出现「DA」，不看对象就会糊成一句。

---

## 事实

- 4844：EVM 只见 versioned hash；字节在 sidecar；节点服务窗是 **4096 epoch**（`MIN_EPOCHS_FOR_BLOB_SIDECARS_REQUESTS`）。
- 4844 正文把 DAS 写成 **以后** 对 `is_data_available()` 的替换，不是 4844 当时的行为。
- PeerDAS（`fulu/das-core.md`）：一维扩成 128 列，每槽至少抽 8 组；一半列可重建。仍不是 Celestia 二维 DAS，也不是执行证明。
- KZG / 配对不是后量子；4844 用 versioned hash 预留换承诺。

---

## 正确写法

| 你验了什么 | 能说的句子 |
|------------|------------|
| versioned hash 在已接受的信标头里 | 「这个袋子的编号被该头承诺过」 |
| 服务窗内拿到 sidecar / 抽到规范要求的列 | 「按该网当前规则，此刻数据可取或抽样通过」 |
| 过了服务窗 | 「L1 共识仍在；这袋字节是否还在，看档案，不看头」 |
| 欺诈/有效性证明 + 数据 | 「L2 状态转移被证明」——这是另一层 |

---

## 对不确定的意义（建议）

产品句必须带：**承诺 / 抽样 / 存留窗** 三个词里你用了哪几个。缺窗还写「永久 DA」，这条就红。
