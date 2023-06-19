from typing import Any

from starlette import status

# クライアント側にレスポンスを返すさいに用いられるエラー定義
# ref: https://github.com/takashi-yoneya/fastapi-mybest-template/blob/master/app/exceptions/error_messages.py # noqa: E501


class BaseMessage:
    """メッセージクラスのベース."""

    text: str
    status_code: int = status.HTTP_400_BAD_REQUEST

    def __init__(self, param: Any | None = None) -> None:
        self.param = param

    def __str__(self) -> str:
        return self.__class__.__name__


class ErrorMessage:
    """エラーメッセージクラス.
    Example: raise APIException(ErrorMessage.INTERNAL_SERVER_ERROR)
    ※ Expectionを継承したものをraiseしたい場合は、exceptでキャッチしてApiExceptionをraiseする.

    Notes
    -----
        BaseMessagを継承することで
        Class呼び出し時にClass名がエラーコードになり、.textでエラーメッセージも取得できるため
        エラーコードと、メッセージの管理が直感的に行える。

    """

    # 共通
    class INTERNAL_SERVER_ERROR(BaseMessage):
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        text = "システムエラーが発生しました、管理者に問い合わせてください"

    class WORD_IS_NOT_ENGLISH(BaseMessage):
        status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        text = "英語の単語を入力してください"
