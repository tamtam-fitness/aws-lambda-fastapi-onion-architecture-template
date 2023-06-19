from typing import Any

from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from core.logger.api_logger import ApiLogger


# ref: https://qiita.com/sotaheavymetal21/items/508a458a70962d822cb5
class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    """エラーハンドリングをするミドルウェア
    API内で発生したエラーをキャッチして処理を施す
    Args:
        BaseHTTPMiddleware : リクエスト/レスポンスインタフェースに対するASGIミドルウェアを記述するための抽象クラス.
    """

    async def dispatch(self, request: Request, call_next: Any) -> Response:
        try:
            # 各エンドポイント内で発生したエラーに関しては
            # HttpExceptionをraiseしFastAPI側でエラーハンドリングをしエラーレスポンスが返るようになっている。
            response: Response = await call_next(request)

        # 現時点で観測できていないエラー用
        except Exception as e:
            response = JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "error_code": e.__class__.__name__,
                    "error_msg": "エラーが発生しました、システム管理者に問い合わせてください",
                },
            )
            ApiLogger.error(response, exec_info=True)

        return response
