from enum import Enum


class ERROR_MSG(Enum):
    INVALID_PARAMETER = "パラメータが不正です"
    FAILED_TO_RETRIEVE_DATA = "データの取得に失敗しました"
    FAILED_TO_CREATE_DATA = "データの作成に失敗しました"
    FAILED_TO_LOGIN = "emailかパスワードが不正です"
    INVALID_TOKEN = "認証情報の有効期限切れです"
    PERMISSION_DENIED = "この操作の権限がありません"
