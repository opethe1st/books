from fastapi import FastAPI
import uvicorn

from books.api import v0

from logging_config import setup_logging


def create_app() -> FastAPI:
    app = FastAPI()
    app.mount("/api/v0", v0.app)
    return app

if __name__ == "__main__":
    app = create_app()
    log_config = setup_logging()
    uvicorn.run(app, host="0.0.0.0", port=8000, log_config=log_config)
