## fastapi + function_scheduling_distributed_framework 的 demo


## 部署
需要部署的脚本分为两个

```
第一个是启动 fastapiweb.py,此脚本中启动web，前端触发接口发布消息到消息队列

第二个是启动 run_consume.py或funcs.py,此脚本启动消费消息队列中的任务。
```

