from pathlib import Path
import uvicorn
from fastapi import FastAPI
import nb_log
import requests

logger = nb_log.get_logger('fastapi_demo',)
nb_log.get_logger('fastapi',log_filename='fastapi.log')  # 给fastapi增加五彩日志和写入多进程安全切片的文件。
nb_log.get_logger('urllib3')

app = FastAPI()




@app.get("/")
def read_root():
    logger.debug('绿色')
    logger.info('蓝色')
    logger.warning('黄色')
    logger.error('粉红色')
    logger.critical('血红色')

    requests.get('http://www.baidu.com')  # 日志回自动记录requests包发的任何请求，因为requests调用urllib3，而nb_log.get_logger('urllib3')对urllib3的日志命名空间添加了handler。

    return {"Hello": "World"}


if __name__ == '__main__':
    # log_config = uvicorn.config.LOGGING_CONFIG
    # log_config["handlers"]["access"]["class"] = "nb_log.handlers.ColorHandler"
    # log_config["handlers"]["default"]["class"] = "nb_log.handlers.ColorHandler"

    LOG_FILE_PATH = '/pythonlogs'
    LOGGING_CONFIG: dict = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "()": "uvicorn.logging.DefaultFormatter",
                "fmt": "%(asctime)s %(levelprefix)s %(message)s",  # 这里日志格式加了时间显示
                "use_colors": False,
            },
            "access": {
                "()": "uvicorn.logging.AccessFormatter",
                "fmt": '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s', # 这里日志格式加了时间显示
            },
        },
        "handlers": {
            "default": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stderr",
            },
            "default_file": {
                "formatter": "default",
                "class": "nb_log.handlers.ConcurrentRotatingFileHandler",  # 注意这里是多进程安全切割日志
                'filename': Path(LOG_FILE_PATH) / 'uvicorn_default.log',
                'maxBytes': 1000 * 1000 * 100,
                'backupCount': 3,
            },
            "access": {
                "formatter": "access",
                "class": "nb_log.handlers.ColorHandler",  # 这里用了nb_log的彩色控制台handler。
            },
            "access_file": {
                "formatter": "access",
                "class": "nb_log.handlers.ConcurrentRotatingFileHandler",  # 注意这里是多进程安全切割日志
                'filename': Path(LOG_FILE_PATH) / 'uvicorn_access.log',
                'maxBytes': 1000 * 1000 * 100,
                'backupCount': 3,
            },
        },
        "loggers": {
            "uvicorn": {"handlers": ["default", "default_file"], "level": "INFO"},
            "uvicorn.error": {"level": "INFO"},
            "uvicorn.access": {"handlers": ["access", "access_file"], "level": "INFO", "propagate": False},
        },
    }

    uvicorn.run(app="fastapiweb222:app", host="127.0.0.1", port=8082, reload=True, debug=True,
                log_config=LOGGING_CONFIG)
