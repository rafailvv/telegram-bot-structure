# Структура Telegram-бота на aiogram 3

```python
├── README.md
├── bot
│   ├── __init__.py
│   ├── buttons
│   │   ├── __init__.py
│   │   ├── inline.py
│   │   └── keyboard.py
│   ├── config.py
│   ├── handlers
│   │   ├── __init__.py
│   │   ├── callback.py
│   │   ├── commands.py
│   │   └── menu.py
│   ├── message_text
│   │   ├── __init__.py
│   │   └── text.py
│   └── misc
│       ├── __init__.py
│       └── states.py
├── database
│   ├── __init__.py
│   ├── manager.py
│   ├── models.py
│   ├── queries
│   │   └── users.py
│   └── session.py
├── main.py
├── requirements.txt
└── systemd
    └── bot.service

```

## Запуск кода
Выполните следующие шаги, чтобы настроить и запустить бота с помощью этого шаблона:

1. **Создайте новый репозиторий**

    Начните с создания нового репозитория, используя этот шаблон. Вы можете сделать это, нажав [здесь](https://github.com/rafailvv/telegram-bot-stucture).

2. **Настройка переменных среды**

    Информация в виде таблицы:

    | Название переменной | Описание                                                 | Примерное значение                                      |
    |--------------------|----------------------------------------------------------|----------------------------------------------------------|
    | BOT_TOKEN          | Токен API бота Telegram.                                 | BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11 |
    | ADMINS             | Список идентификаторов пользователей Telegram для администраторов бота. | ADMINS=12345678,910111213                                     |
    | DB_NAME            | Название базы данных PostgreSQL.                         | DB_NAME=example_db_name                                  |
    | DB_USER            | Имя пользователя для аутентификации в PostgreSQL.       | DB_USER=example_db_user                                  |
    | DB_PASS            | Пароль для аутентификации в PostgreSQL.                 | DB_PASS=example_db_password                              |
    | DB_HOST            | Имя хоста или IP-адрес сервера PostgreSQL.              | DB_HOST=example_db_host                                  |
    | DB_PORT            | Номер порта для PostgreSQL (по умолчанию 5432).          | DB_PORT=5432                                             |
    | REDIS_HOST         | Имя хоста или IP-адрес сервера Redis.                   | REDIS_HOST=localhost                                     |


3. **Запуск Бота**

    Клонируйте репозиторий
    ```
    git clone https://github.com/rafailvv/telegram-bot-stucture.git
    ```

    Создайте файл переменных среды, скопировав предоставленный файл примера:

    ```
     cp .env.example .env
     ```

    Установите требуемые пакеты
    ```
    pip install -r requirements.txt
    ```

    Запустите Бота

    ```
    python3 main.py
    ```

## Благодарности

Данный репозиторий разработан в рамках курса "Создание Telegram Бота" компании [INNOPROG](https://innoprog.ru/).