from httpx import Client, URL, Response, QueryParams
from typing import Any, TypedDict


# Тип расширений, которые можно передать в запрос
# В нашем случае мы используем только параметр "route", но можно добавить и другие
class HTTPClientExtensions(TypedDict, total=False):
    route: str

class HTTPClient:
    """
    Базовый HTTP API клиент, принимающий объект httpx.Client.

    :param client: экземпляр httpx.Client для выполнения HTTP-запросов
    """
    def __init__(self, client: Client):
        self.client = client

    def get(
            self,
            url: URL | str,
            params: QueryParams | None = None,
            # Добавили поддержку extensions
            extension: HTTPClientExtensions | None = None
        ) -> Response:
        """
        Выполняет GET-запрос.

        :param url: URL-адрес эндпоинта.
        :param params: GET-параметры запроса (например, ?key=value).
        :return: Объект Response с данными ответа.
        """
        # Передаём extensions в httpx.Client
        return self.client.get(url, params=params, extensions=extension)

    def post(
            self,
            url: URL | str,
            json: Any | None = None,
            # Поддержка extensions для POST-запросов
            extension: HTTPClientExtensions | None = None
    ) -> Response:
        """
       Выполняет POST-запрос.

       :param url: URL-адрес эндпоинта.
       :param json: Данные в формате JSON.
       :return: Объект Response с данными ответа.
       """
        # extensions передаётся в httpx.Client
        return self.client.post(url, json=json, extensions=extension)