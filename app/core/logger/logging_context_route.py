import datetime
import json
import time
from collections.abc import Callable

from fastapi import Request, Response
from fastapi.routing import APIRoute

from core.logger.api_logger import ApiLogger


class LoggingContextRoute(APIRoute):
    def get_route_handler(self) -> Callable:  # type: ignore
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            """ログにリクエストの内容を出力する
            参考: https://blog.jicoman.info/2021/01/how-to-logging-request-and-response-body-by-fastapi/.
            """
            before = time.time()
            response: Response = await original_route_handler(request)
            duration = round(time.time() - before, 4)

            record = {}
            time_local = datetime.datetime.fromtimestamp(
                before, tz=datetime.timezone(datetime.timedelta(hours=9))
            )
            record["time_local"] = time_local.strftime("%Y/%m/%d %H:%M:%S%Z")
            if await request.body():
                record["request_body"] = (await request.body()).decode("utf-8")
            record["request_headers"] = {  # type: ignore
                k.decode("utf-8"): v.decode("utf-8") for (k, v) in request.headers.raw
            }
            record["remote_addr"] = request.client.host
            record["request_uri"] = request.url.path
            record["request_method"] = request.method
            record["request_time"] = str(duration)
            record["status"] = response.status_code
            record["response_headers"] = {  # type: ignore
                k.decode("utf-8"): v.decode("utf-8") for (k, v) in response.headers.raw
            }
            ApiLogger.info(json.dumps(record))
            return response

        return custom_route_handler
