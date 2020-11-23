# POLL APP
### Запуск приложения
- pip3 install -r requirements.txt
- python3 manage.py collectstatic
- python3 manage.py runserver
### API
- /admin/ - панель администратора
- /api/v1/auth/ - авторизация для пользователей
- /api/v1/polls/ - получение списка активных опросов
- /api/v1/pass/ - прохождение пользователем опроса