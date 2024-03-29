# Микроблог "Блог номер один"

Микроблог, написанный на Flask - настольный проект блога с возможностью создавать и редактировать свой профиль, создавать, менять и удалять посты с фотографиями, комментировать чужие посты, выбирать тэги и осуществлять поиск постов. 
Проект имеет неброскую frontend часть, написанную с помощью HTML и Bootstrap. Также доступен небольшой API с ограниченным функционалом, написанный на React.
Проект доступен в режиме отладки, для запуска проекта клонируйте его в отдельную директорию, запустите виртуальное окружение и установите зависимости: 

``` 
python -m venv venv

venv\Scripts\activate.bat (для Windows)

source venv/bin/activate (Linux, MacOS)

pip install -r requirements.txt

``` 

Затем запустите сервер разработки flask: 

```
flask --app app.py run 
```
Проект будет доступен на локальном сервере http://127.0.0.1:8000

Список технологий:

- Python 3.11

- Flask 2.2.2

- Flask-SQLAlchemy 3

- SQLAlchemy 2.0.3

- PyJWT 2.6

- HTML

- CSS

- Bootstrap5

- React

