# Новостной портал

Новостной сайт на котором любой желающий может поделиться выдуманной новостью!

### Описание
Новостной сайт созданный с использованием микрофреймворка Flask в рамках обучения по программе Python Pro.

### Технологии
* Python
* Flask
* Flask-WTF
* Flask-SQLAlchemy

## Установка проекта
1. Клонирование репозитория
2. Создание виртуального окружения
```commandline
python -m venv venv
```
3. Запуск вирутального окружения

GitBash:
```commandline
source venv/Scripts/activate
```
Windows:
```commandline
venv\Scripts\activate
```

4. Установка зависимостей
```commandline
pip install -r requirements.txt
```

5. Добавьте файл .env и укажите настройки подключения к БД
```
DATABASE_URI=sqlite:///db.sqlite3
YOUR_SECRET_KEY=SECRET_KEY
```

6. Запуск приложения
```commandline
flask run --debug
```
