# CREST PYTHON IN DEVELOPMENT

## Описание

В разработке!


## Инструкции по установке

Следуйте этим шагам, чтобы настроить и запустить проект.

### 1. Клонируйте репозиторий

Сначала клонируйте репозиторий на ваш локальный компьютер:

```sh
git clone https://github.com/prntscr-nevada/python-crest-bitrix24.git
cd python-crest-bitrix24
```

### 2. Создайте виртуальное окружение

Создайте виртуальное окружение, чтобы изолировать зависимости проекта:

```sh
python -m venv .venv
```

### 3. Активируйте виртуальное окружение

Активируйте виртуальное окружение:

- **Windows:**

  ```sh
  .venv\Scripts\activate
  ```

- **macOS/Linux:**

  ```sh
  source .venv/bin/activate
  ```

### 4. Установите зависимости

Установите необходимые зависимости из файла `requirements.txt`:

```sh
pip install -r requirements.txt
```

### 5. Скопируйте файл конфигурации окружения

Скопируйте файл `.env.example` в `.env`:

```sh
cp .env.example .env
```
Убедитесь, что вы заполнили файл `.env` правильными значениями конфигурации перед запуском проекта.

Учитывайте, что должны быть заполнены либо **CLIENT_ID** и **CLIENT_SECRET** для работы в режиме локального/тиражного приложения, либо **CLIENT_WEBHOOK** для работы с входящим в битрикс вебхуком.

### 6. Запустите проект

Запустите проект:

```sh
python run-server.py
```

## Примечания

- Дополнительная информация о проекте, включая его функции и использование, может быть добавлена в этот файл.