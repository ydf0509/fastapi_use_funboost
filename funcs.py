import time
from function_scheduling_distributed_framework import task_deco, BrokerEnum

"""
如果发布者要获取消费结果一定要设置is_using_rpc_mode=True
"""
@task_deco('test_add_queue', broker_kind=BrokerEnum.SQLITE_QUEUE,is_using_rpc_mode=True)
def add(a, b):
    time.sleep(5)
    return a + b


@task_deco('test_add_queue', broker_kind=BrokerEnum.SQLITE_QUEUE,concurrent_num=100,is_using_rpc_mode=True)
def sub(a, b):
    time.sleep(3)
    return a - b


if __name__ == '__main__':
    add.consume()
    sub.multi_process_consume(2)
