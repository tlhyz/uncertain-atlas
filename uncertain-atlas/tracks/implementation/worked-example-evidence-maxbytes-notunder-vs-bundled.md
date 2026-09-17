# 例：看见填了证据 MaxBytes is not already under block cap interchangeable / not already overhead-deducted interchangeable / not already settled interchangeable

**层次**：实现 / 填了证据 MaxBytes not already under block cap / not already overhead-deducted / not already settled 正式三事（331 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / EvidenceParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、mempool。本页是「填了证据 MaxBytes not already under block cap / not already overhead-deducted / not already settled 正式三事（331 余量）/ not 920 evidence-maxbytes-notunder interchangeable / not 331 evidence-maxbytes-vs-block bundled interchangeable」，不是证据尺 bundled（331），也不是先装证据已经装满交易（299），也不是 -1 就已经没有块上限（337/917）。不要另写怎样设 EvidenceParams.MaxBytes 或怎样算块开销。

## 官方三件事

1. **看见填了证据 MaxBytes / 看见一块里证据有上限 这份字段 is not already 已经落在块 MaxBytes 下面 interchangeable，也不是已经证据尺 bundled（331） interchangeable / 920 evidence-maxbytes-notunder interchangeable / 921 evidence-maxbytes-notunbond interchangeable / 331 evidence-maxbytes item 2 > 0 interchangeable，也不是已经填了证据 MaxBytes not already under block cap / not already overhead-deducted / not already settled 正式三事 bundled（331 item 1 余量） interchangeable / 331 evidence-maxbytes item 1 interchangeable。**  
   官方写：这是单块能交差的证据总字节上限。它应当舒服地落在块最大字节下面。取值不得超过一块减去开销之后的体积（约 BlockParams.MaxBytes）。看见填了这个字段，不是已经落在块上限下面 interchangeable——本页从 331 item 1 侧钉 not already under block cap 单句。331 evidence-maxbytes vs block bundled unbundling 在本页 item 1 启动。

2. **看见有上限 / 看见应当落在下面 / 这份字段 is not already 已经扣掉开销 interchangeable，也不是已经证据尺 bundled（331） interchangeable / 920 evidence-maxbytes-notunder interchangeable / 331 evidence-maxbytes item 3 两把尺 interchangeable / 922 evidence-maxbytes-notblock interchangeable，也不是已经先装证据已经装满交易 interchangeable / 299 maxbytes-pool interchangeable。**  
   官方把应当落在下面和已经扣掉开销分开——331 bundled 第一件事常与 299 混成「看见填了证据体积就已经落在块上限下面或已经装满交易 interchangeable」，本页钉 not already overhead-deducted 单句。

3. **看见应当落在下面 / 看见填了字段 / 这份字段 is not already 已经交差 interchangeable，也不是已经证据尺 bundled（331） interchangeable / 920 evidence-maxbytes-notunder interchangeable / 921 evidence-maxbytes-notunbond interchangeable，也不是已经 -1 就已经没有块上限 interchangeable / 337/917 maxbytes-cap-notunlim interchangeable。**  
   官方把应当落在下面和已经交差分开。看见应当落在下面，不是已经交差 interchangeable。331 evidence-maxbytes vs block bundled unbundling 在本页 item 1 启动。

怎样设 EvidenceParams.MaxBytes、默认取值、怎样算块开销是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **填了证据 MaxBytes not already under block cap ≠ 已经落在块上限下面 interchangeable：** 官方把「应当落在下面」和「已经填了字段」分开。
- **看见有上限 not already overhead-deducted ≠ 已经扣掉开销 interchangeable：** 官方把有上限和已经从块体积扣掉开销分开。
- **看见应当落在下面 not already settled ≠ 已经交差 interchangeable：** 官方把应当落在下面和已经交差分开；331 evidence-maxbytes vs block bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 填了证据 MaxBytes | 不是已经落在块上限下面，也不是已经扣掉开销 | 不是先装证据已经装满交易（299） |
| 看见有上限 | 不是已经扣掉开销 | 不是 -1 就已经没有块上限（337/917） |
| 看见应当落在下面 | 不是已经交差 | 不是 > 0 就已经盖住解绑（921） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了证据 MaxBytes not already under block cap / not already overhead-deducted / not already settled 正式三事（331 余量），必须分开是不是已经落在块上限下面、是不是已经扣掉开销、是不是已经交差。可以跳过「看见填了证据体积就已经和块上限同一把尺」。不要另写怎样设 EvidenceParams.MaxBytes 或怎样算块开销。331 evidence-maxbytes vs block bundled unbundling 在本页 item 1 启动；续 [`worked-example-evidence-maxbytes-notunbond-vs-bundled.md`](worked-example-evidence-maxbytes-notunbond-vs-bundled.md)（不变量 921 item 2）。

## 本页不抄

- 怎样设 EvidenceParams.MaxBytes、默认取值、怎样算块开销。
- 证据尺 bundled。那是不变量 331。
- > 0 就已经盖住解绑。那是不变量 331 item 2 余量 / 921。
- 先装证据已经装满交易。那是不变量 299。
