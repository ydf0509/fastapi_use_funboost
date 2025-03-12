﻿## 1 fastapi + funboost 的 demo


其实不需要这个demo，funboost 和django  flask  fastapi 任意web框架搭配没有任何区别，
但是有的人老是爱问 funboost 怎么和某某web框架搭配，那就写一个项目。

funboost 和django搭配不像 django_celery 还要专门特意搞个三方插件包，完全不需要，在任何web框架中使用funboost都没有需要专门学习的三方插件包。 



## 2 部署
需要部署的脚本分为两个

```
第一个是启动 fastapiweb.py,此脚本中启动web，前端触发接口发布消息到消息队列

第二个是启动 run_consume.py或funcs.py,此脚本启动消费消息队列中的任务。
```

## 3 截图

### 3.1 浏览器请求add接口截图

[![oLI0SS.png](https://s4.ax1x.com/2021/12/13/oLI0SS.png)](https://imgtu.com/i/oLI0SS)

### 3.2 web接口发布任务截图

[![oLIui6.png](https://s4.ax1x.com/2021/12/13/oLIui6.png)](https://imgtu.com/i/oLIui6)

### 3.3 后台消费截图

[![oLIRYV.png](https://s4.ax1x.com/2021/12/13/oLIRYV.png)](https://imgtu.com/i/oLIRYV)

### 3.4 浏览器请求taskid接口获取结果截图

[![oLI8Ld.png](https://s4.ax1x.com/2021/12/13/oLI8Ld.png)](https://imgtu.com/i/oLI8Ld)


