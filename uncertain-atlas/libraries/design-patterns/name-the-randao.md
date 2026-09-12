# 模式：执行层读随机必须先点名是工作量、上一块 mix 还是应用公平

**问题：** 产品把「链上随机」写成已经解释了无偏骰子。用户把合并后的 `DIFFICULTY` 听成工作量，或把 `PREVRANDAO` 听成公平。  
**方案：** 每个执行层随机句先点名问的是工作量字段、上一块 RANDAO mix，还是应用公平。合并后 `difficulty` 必须为 0。旧指令返回上一块 mix。信标 RANDAO 有 1 bit 影响力，历史值可预测。  
**适用：** Ethereum 合并后的 `DIFFICULTY` / `PREVRANDAO` / 任何「执行层读共识随机」的结算文案。  
**优点：** 用户能指出旧坡度牌、昨天抽签、公平骰子不是同一盏灯。  
**缺点：** 句子变长；不能再用「链上随机」交差。  
**项目：** EIP-4399：复用旧操作码；`mixHash` 装上一块 mix；与 EIP-3675 过渡绑死。  
**常见 bug：** `DIFFICULTY` 写成工作量；`PREVRANDAO` 写成无偏。  
**不确定：** 若把共识随机暴露进执行 VM，必须写清问的是哪一种，并写清可预测与 1 bit。见 [工作实例](../../tracks/crypto/worked-example-prevrandao-vs-difficulty.md)。
