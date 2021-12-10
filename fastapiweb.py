import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from funcs import add, sub
import nb_log
from function_scheduling_distributed_framework import AsyncResult, HasNotAsyncResult

logger = nb_log.get_logger('fastapi_demo')

app = FastAPI()


class TaskStatusModel(BaseModel):
    task_id: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


"""
http://127.0.0.1:8080/add/?x=1&y=2
"""


@app.get("/add/")
def add_api(x: int, y: int):
    """接口迅速返回taskid，前端页面调用下面的接口传入taskid获取结果
    """
    async_result = add.push(x, y)
    logger.debug(async_result.task_id)
    model = TaskStatusModel(task_id=async_result.task_id)
    return model


@app.get("/taskid/{taskid:str}")
def get_add_result_by_ajax(taskid: str):
    """前端每隔3秒轮训ajax，个人建议可以考虑尝试函数里面得到结果后发布到mqtt topic，前端订阅这个topic，mqtt比ajax和websocket都好用
    如果前端不需要关注结果，不需要调用此接口
    """
    try:
        return AsyncResult(task_id=taskid, timeout=1).get()
    except HasNotAsyncResult:
        logger.warning(f"taskid [ {taskid} ]还没执行完成或者taskid错误")
        return 'empty'


"""
http://127.0.0.1:8080/sub/?x=1&y=2
"""


@app.get("/sub/")
def sub_api(x: int, y: int):
    """接口直接阻塞直到任务执行完成"""
    async_result = sub.push(x, y)
    async_result.set_timeout(120)
    result = async_result.get()
    return result


if __name__ == '__main__':
    uvicorn.run(app="fastapiweb:app", host="127.0.0.1", port=8080, reload=True, debug=True)
