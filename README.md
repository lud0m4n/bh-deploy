# Хакатон: BESTHACK. BPA. Команда: The Brawlers. Репозиторий деплоя финального этапа

## Проект уже развернут на сервере и в телеграме по адресу:
* https://ka.bankaban.ru/ - интерфес

* https://dash.bankaban.ru/ - сервис, аналитики с визуализацией

* https://ka.bankaban.ru/new-task - страница с созданием новой таски

* https://t.me/TheBrawlers_bot - телеграм бот для автоматической рассылкой


## Как склонировать проект

Так как проект использует подмодули, то для клонирования проекта необходимо выполнить:

```bash
git clone https://github.com/lud0m4n/bh-deploy.git --recursive
```

## Как запустить проект

Чтобы запустить этот проект, выполните следующие шаги:

1. Скопируйте файл `.env.example` и переименуйте его в `.env`.
2. Откройте файл `.env` и настройте необходимые переменные окружения. Можете оставить по умолчанию или изменить на свои значения. Вставьте свой API_TOKEN для телеграм бота.
3. Установите Docker, если вы еще этого не сделали. Вы можете скачать его с официального веб-сайта Docker.
4. Откройте терминал или командную строку и перейдите в директорию проекта.
5. Выполните следующую команду, чтобы запустить проект:

    ```bash
    docker compose up -d --build
    ```

    Эта команда создаст необходимые контейнеры Docker и запустит проект.

6. Дождитесь запуска контейнеров. Вы можете проверить журналы, чтобы отслеживать прогресс.

Вот и все! Проект теперь должен быть запущен и работать. Вы можете получить доступ к нему, используя указанные URL-адреса или порты в вашем браузере.

## Ссылки

Если вы не изменяли порты по умолчанию, вы можете получить доступ к проекту по следующим URL-адресам:
* http://localhost:5173 - интерфейс 

* http://localhost:8888 - админер, интерфейс для управления базой данных

* http://localhost:3001 - сервис аналитики с визуализацией

## Примечание
Данные для доступов по умолчанию на интерфейсах марса и земли указаны на главной странице.

Данные для доступа к админеру по умолчанию:
* Движок: PostgreSQL
* Сервер: postgres-grpc
* Пользователь: postgres
* Пароль: postgres
* Базa: grpcpostgre 

## Как остановить проект

Чтобы остановить проект, выполните следующие шаги:

1. Откройте терминал или командную строку и перейдите в директорию проекта.

2. Выполните следующую команду, чтобы остановить проект:

    ```bash
    docker compose down
    ```

    Эта команда остановит все контейнеры Docker, связанные с проектом.
## Мы реализовали:

 1. Специальный сайт для ведения задач:
* Главная страница: Здесь отображается список всех поступивших задач и их текущий статус (для конкретного юзера). Это позволит техническим специалистам эффективно управлять своей рабочей нагрузкой.
* Страница с примерами решений: На этой странице представлены шаблоны ответов или инструкции для решения на часто встречающиеся вопросы. Специалисты могут создавать новые шаблоны, редактировать существующие и делиться опытом с коллегами.
* Страница с созданием новой таски: Предназначена для менеджера, чтобы отправить новую таску техническому специалисту.

 2. Система кластеризации и анализа обращений:
* Кластеризация обращений: Каждое обращение автоматически попадает в определенный кластер, что позволяет группировать похожие проблемы и управлять ими эффективно.
* Автоматическое предложение решений: При выборе специалистом задачи, система предлагает ранее решенные кейсы из того же кластера. Это сокращает время решения и уменьшает вероятность повторных обращений.
* Сбор временны́х данных: Время реакции технического специалиста на новую таску высчитывается, как и время её решения. Эти данные анализируются и визуализируются.

 3. Телеграм бот:
* Регистрация телеграм аккаунта в базу данных пользователя интерфейса.
* Автоматическая рассылка в случае получения техническим специалистом срочного задания.

## Стэк технологий
* Frontend: React, typesscript, Mantine, i18n, Zustand, axios, clsx. 
* Сервис кластеризации: Python, Flask, torch, pandas, plotly, sklearn, dash, aiogram, aiohttp.
* Backend: Интерфейс для Тех специалистов состоит из двух серверов это REST-API сервер, который связан осуществляет запросы на сервер аналитики и на gRPC сервер, где описана вся бизнес логика, сам REST сервер выступает в виде прослойки. По стеку: REST-server написан на Go фреймворк Gin используется для http сервера, так же выступает клиентом для gRPC сервера, взаимодействие осуществляется через прото файлы, на gRPC сервере есть БД postgreSQL и Redis для хранения авторизированных токенов, используется GORM для запросов к БД, есть JWT авторизация.
