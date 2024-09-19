import logging

def get_logging_config():
    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(levelname)s - %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
        "handlers": {
            "default": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
        },
        "root": {"handlers": ["default"], "level": "INFO"},
        "loggers": {
            "uvicorn": {"handlers": ["default"], "level": "INFO"},
            "fastapi": {"handlers": ["default"], "level": "INFO"},
        },
    }

    return logging.config.dictConfig(log_config)
