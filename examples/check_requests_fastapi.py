import json

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.middleware("http")
async def log_request_data(request: Request, call_next):
    # Выводим метод запроса и URL
    print(f"Метод запроса: {request.method}")
    print(f"URL: {request.url}\n")

    # Выводим заголовки в формате JSON
    headers = dict(request.headers)
    headers_json = json.dumps(headers, indent=4, ensure_ascii=False)
    print(f"Заголовки запроса:\n{headers_json}\n")

    # Выводим параметры запроса
    query_params = dict(request.query_params)
    query_params_json = json.dumps(query_params, indent=4, ensure_ascii=False)
    print(f"Параметры запроса:\n{query_params_json}\n")

    # Выводим тип содержимого тела запроса
    content_type = request.headers.get("content-type")

    # Если тело запроса в формате JSON, выводим его
    if content_type == "application/json":
        body = await request.json()
        body_json = json.dumps(body, indent=4, ensure_ascii=False)
        print(f"Тело запроса (JSON):\n{body_json}\n")

    # Если тело запроса в формате x-www-form-urlencoded, выводим его
    elif content_type == "application/x-www-form-urlencoded":
        # Получение данных формы
        form_data = await request.form()

        # Преобразование данных формы в словарь
        data = dict(form_data)

        # Проверка и преобразование строки JSON в словарь
        if "PLACEMENT_OPTIONS" in data:
            try:
                # Преобразование строки JSON в словарь
                data["PLACEMENT_OPTIONS"] = json.loads(data["PLACEMENT_OPTIONS"])
            except json.JSONDecodeError:
                # Если JSON некорректный, оставить как есть
                data["PLACEMENT_OPTIONS"] = data["PLACEMENT_OPTIONS"]
        form_data_json = json.dumps(data, indent=4, ensure_ascii=False)
        print(f"Тело запроса (Form Data):\n{form_data_json}\n")

    # Обрабатываем запрос
    response = await call_next(request)

    # Выводим статус ответа и заголовки
    print(f"Статус ответа: {response.status_code}")
    response_headers = dict(response.headers)
    response_headers_json = json.dumps(response_headers, indent=4, ensure_ascii=False)
    print(f"Заголовки ответа:\n{response_headers_json}")

    return response


@app.post("/install")
async def install(request: Request):
    # Установка приложения

    html_content = """
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <title>Installation</title>
            <script src="//api.bitrix24.com/api/v1/"></script>
            <script>
                BX24.init(function(){
                    BX24.installFinish();
                });
            </script>
        </head>
        <body>
            <p>Installation finished</p>
        </body>
        </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/handler")
async def handler():
    # Работа приложения

    return "OK"


if __name__ == "__main__":
    uvicorn.run(
        app="check_requests_fastapi:app", host="127.0.0.1", port=8000, reload=True
    )
