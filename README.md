## fastapi + function_scheduling_distributed_framework 的 demo


## 部署
需要部署的脚本分为两个

```
第一个是启动 fastapiweb.py,此脚本中发布消息到消息队列

第二个是启动 run_consume.py,此脚本启动消费消息队列中的任务
```

