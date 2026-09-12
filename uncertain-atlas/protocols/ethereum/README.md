# Ethereum 协议档案

优先级：重要  
完整报告：[`report.md`](report.md)

精读：[`../../tracks/light-clients/worked-example-blob-fee-vs-gas.md`](../../tracks/light-clients/worked-example-blob-fee-vs-gas.md)（不变量 145）。blob gas 不是普通执行 gas。EVM 能读承诺不是已经读到袋里的字节。处理完一块不是已经改规范头：[`../../tracks/finality/worked-example-processed-vs-forkchoice.md`](../../tracks/finality/worked-example-processed-vs-forkchoice.md)（不变量 149）。提款操作不是用户交易：[`../../tracks/economic/worked-example-withdrawal-vs-tx.md`](../../tracks/economic/worked-example-withdrawal-vs-tx.md)（不变量 154）。

一句话：

> 账户模型上的确定性状态机（EVM）加上后来拆开的执行层/共识层；用 gas 给任意程序计价，用多客户端逼规范精确。
