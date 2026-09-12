# 模式：应用 / 共识分离

**问题：** 把余额规则焊进投票引擎，以后换执行或换签名要翻整座庙。  
**方案：** 引擎只排序字节并提交；应用做 `Apply` 并返回状态哈希。  
**适用：** Cosmos SDK / CometBFT；「不确定」实验期。  
**优点：** 可换应用、可测、边界清晰。  
**缺点：** 应用不确定就全裂；两套存储要对齐高度。  
**项目：** CometBFT ABCI。  
**常见 bug：** CheckTx 当最终执行；Process REJECT 当免费过滤器；Prepare 立即执行写进提交状态。精读：[四门](../../tracks/consensus/worked-example-prepare-process.md)。  
**不确定：** 强烈建议。
