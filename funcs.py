import time
from funboost import task_deco, BrokerEnum

"""
如果发布者要获取消费结果一定要设置is_using_rpc_mode=True
"""
@task_deco('fastapi_add_queue', broker_kind=BrokerEnum.REDIS_ACK_ABLE,is_using_rpc_mode=True)
def add(a, b):
    time.sleep(5)
    result =  a + b
    print(f'{a} + {b} = {result}')
    return result


@task_deco('fastapi_sub_queue', broker_kind=BrokerEnum.RedisBrpopLpush,concurrent_num=100,is_using_rpc_mode=True)
def sub(a, b):
    time.sleep(3)
    result = a - b
    print(f'{a} - {b} = {result}')
    return result


if __name__ == '__main__':
    add.consume()
    sub.multi_process_consume(2)
