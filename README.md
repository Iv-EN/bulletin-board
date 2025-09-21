<div align="center">
    <h1>Доска объявлений</h1> 
    <p>
        Backend-часть для сайта объявлений
    </p>
</div>

---

## Описание

Приложение на Django. Реализован следующей функционал:

- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- Восстановление пароля через электронную почту.
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
- Под каждым объявлением пользователи могут оставлять отзывы.
- В заголовке сайта можно осуществлять поиск объявлений по названию.
  ```
    (GET запрос на http://127.0.0.1:8000/ads/?search=...)
    ```

---

<div align="center">
    <h3 align="center">
        <p>Использовались языки и инструменты:</p>
        <div>
            <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
            <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain-wordmark.svg" title="Django" alt="Django" width="40" height="40"/>&nbsp;
            <img src="https://github.com/devicons/devicon/blob/master/icons/djangorest/djangorest-original-wordmark.svg" title="DRF" alt="DRF" width="40" height="40"/>&nbsp;
            PEP8
            <img src="https://github.com/devicons/devicon/blob/master/icons/git/git-original-wordmark.svg" title="Git" alt="Git" width="40" height="40"/>
            JWT
            ORM
            <img src="https://github.com/devicons/devicon/blob/master/icons/openapi/openapi-original.svg" title="OpenAPI Docs" alt="OpenAPI Docs" width="40" height="40"/>
            Permissions
            <img src="https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original.svg" title="PostgreSQL" alt="PostgreSQL" width="40" height="40"/>
            Readme
            Serializers
            <img src="https://github.com/devicons/devicon/blob/master/icons/pytest/pytest-original.svg" title="Pytest" alt="Pytest" width="40" height="40"/>
            Viewset/Generic
            <img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original.svg" title="Docker" alt="Docker" width="40" height="40"/>
            Filter
        </div>
    </h3>
</div>

---

## Требования

Docker

## Локальная установка проекта

1. Клонируйте репозиторий:

```bash
git clone https://github.com/Iv-EN/bulletin-board.git
```

## Запуск проекта

Для запуска проекта:
Убедитесь, что Docker запущен

1. Из корневой папки проекта выполните:
    ```bash
    docker-compose up -d --build
    ```
2. Создайте супер пользователя:
   ```bash
   docker exec -it backend python manage.py createsuperuser 
   ```
Панель администратора Django доступна по адресу:
```
http://127.0.0.1:8000/admin/
```
Документация:

```
http://127.0.0.1:8000/redoc/
http://127.0.0.1:8000/swagger/
```
Для локального запуска тестов поменяйте настройку на 
```
DJANGO_SETTINGS_MODULE = config.settings_test
```
___

<h3 align="center">
    <p><img src="https://media.giphy.com/media/iY8CRBdQXODJSCERIr/giphy.gif" width="30" height="30" style="margin-right: 10px;">Автор: Евгений Иванов. </p>
</h3>
<p align="center">
     <div align="center"  class="icons-social" style="margin-left: 10px;">
            <a href="https://vk.com/engenivanov" target="blank" rel="noopener noreferrer">
                <img src="https://img.shields.io/badge/%D0%92%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D0%B5-blue?style=for-the-badge&logo=VK&logoColor=white" alt="В контакте Badge"/>
            </a>
            <a href="https://t.me/IvENauto" target="blank" rel="noopener noreferrer">
                <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>
            </a>
    </div>
