# 模式：相对锁必须先点名是部署名、序列字段还是脚本

**问题：** 产品把「CSV」写成一盏灯。用户把软分叉部署听成 CHECKSEQUENCEVERIFY，或把 nSequence 听成已经相对锁住，或把相对锁听成 CLTV。  
**方案：** 每个相对锁句先点名问的是这次部署、花费输入的 nSequence，还是输出脚本里的 CSV。相对锁是被花输出的年龄。关掉相对锁则没有共识含义。  
**适用：** Bitcoin 相对时间锁 / 任何「确认之后再等」的结算文案。  
**优点：** 用户能指出店庆海报、票序号和柜台上的相对锁不是同一盏灯。  
**缺点：** 句子变长；不能再用「有 CSV」交差。  
**项目：** BIP-68 + BIP-112：nSequence 的共识年龄；CSV 比的是该输入 nSequence。  
**常见 bug：** 部署名写成操作码；nSequence 写成已锁；CSV 写成 CLTV。  
**不确定：** 若做相对时间锁，必须写清锁的是被花输出的年龄。见 [工作实例](../../tracks/state-models/worked-example-csv-vs-cltv.md)。
