import logging
from typing import Any

import sentry_sdk
from fastapi import FastAPI
from mangum import Mangum
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

from api.v1 import v1_router
from core.config import settings
from core.logger.api_logger import ApiLogger
from core.logger.logging_context_route import LoggingContextRoute
from exceptions.error_handle_middleware import ErrorHandlingMiddleware

app = FastAPI()
app.router.route_class = LoggingContextRoute

app.add_middleware(ErrorHandlingMiddleware)

app.include_router(v1_router, prefix="/v1")

# ref: https://docs.sentry.io/platforms/python/guides/logging/
sentry_logging = LoggingIntegration(level=logging.INFO, event_level=logging.ERROR)
if settings.ENV not in ["local", "test"]:
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        integrations=[sentry_logging, FastApiIntegration(transaction_style="endpoint")],
        environment=settings.ENV,
        traces_sample_rate=1.0,
    )


def handler(event: Any, context: Any) -> Any:
    ApiLogger.info(event)

    asgi_handler = Mangum(app, lifespan="off")
    return asgi_handler(event, context)
