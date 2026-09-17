# 模式：执行层必须先点名是处理还是改头

**问题：** 产品把「执行层收下了 / 回了 VALID」写成已经解释了规范头。用户把处理听成改头，把头听成 finalized。  
**方案：** 每个 EL/CL 句先点名问的是处理一块、`POS_FORKCHOICE_UPDATED` 点名的头，还是同一事件里的 finalized。没有该事件，不得改 fork choice。禁止乐观改头。  
**适用：** 合并后的以太坊 / 任何「执行与共识拆开、用事件改头」的结算文案。  
**优点：** 用户能指出验收、上桌、不可撤菜单不是同一盏灯。  
**缺点：** 句子变长；不能再用「EL 绿了」交差。  
**项目：** EIP-3675 Final；Engine API `newPayload` / `forkchoiceUpdated` 是事件通道。  
**常见 bug：** 刚处理写成已经是头；事件里的 head 写成已经 finalized。  
**不确定：** 第一版可以不拆 Engine API。若拆，必须写清处理不是改头。见 [工作实例](../../tracks/finality/worked-example-processed-vs-forkchoice.md)。
