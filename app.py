from fastapi import FastAPI
import uvicorn

from books.api import v0

from logging_config import get_logging_config


def create_app() -> FastAPI:
    app_ = FastAPI()
    app_.mount("/api/v0", v0.app)
    return app_

if __name__ == "__main__":
    app = create_app()
    LOG_CONFIG = get_logging_config()
    uvicorn.run(app, host="0.0.0.0", port=8000, log_config=LOG_CONFIG)
