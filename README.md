
### comments
 
В forms.json уже есть несколько паттернов форм для примера, перед запуском можно удалить или продолжить работу. 

Добавил коллекцию POSTAMN с готоыыми примерами, можно удобно и быстро протестить ;).

Не знаю возможно ли добавить в openapi возможность добавления бесконечного количесвта query params, тестировал с помощью Postman.

Три вспомогательные ручки 
`GET /patterns` - список всех паттернов, 
`POST /patterns` - добавление паттаерна,
 `DELETE /patterns` - удаление всех паттернов. 

Написал автотест с помощью `pytest` на эндпоинт `/get_form`, который сам генерирует форму на основе одного из паттернов из бд и проверяет наличие паттерна в ответе.

---

## Start project local 
Создание виртуального окружения 

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

Установка пакетов

```
pip install -r requirements.txt
```

Запуск приложения

```bash
uvicorn --app-dir ./src/ app:app --reload 
```

**http://127.0.0.1:8000/docs/**

---

## Start with DOCKER

```bash 
docker-compose up
```

---
## RUN Tests

Создание виртуального окружения 

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

Установка пакетов

```
pip install -r requirements.txt
```

```
pytest . -vv
```

---
## Run Postman collection

при запуске с помощью `docker-compose` изменить порт в url на `80`. 
1. Выберите Импорт на боковой панели.
2. Выберите файл `Forms.postman_collection.json` перетащите файл  в окно импорта.
3. Выбрать коллекцию. 
4. Запустить тесты коллекции с помощью `runner` или запустить каждый тест отдельно.  
---

## Endpoints 

### POST get_form/

matches patterns from db

patterns - list of tuples[pattern_name, fields_count]

```json
{
    "patterns": [
        [
            "pattern_name1",
            3
        ],
        [
            "pattern_name3",
            6
        ],
        [
            "pattern_name2",
            2
        ]
    ]
}
```
if pattern not exist 

```
{
    "field_name": "one_of_exists_type",
    "field_name": "one_of_exists_type",
    "field_name": "one_of_exists_type",
    "field_name": "one_of_exists_type",
    "field_name": "one_of_exists_type"
}
```


### GET patterns/

response - `list` of patterns in db 

```json
[
  {
    "field_name1": "type1",
    "field_name2": "type2",
    "field_name3": "type1"
            ...
  }
]
```

### POST patterns/

post pattern in db 

PARAMS:
  `name: srt` 

BODY
    ` dict[field_name: field_type] ` 

`type` can be one of `["text", "email", "phone", "date"]`

body example

```
{
    "field_name1": "text",
    "field_name2": "email",
    "field_name3": "date",
    "field_name4": "text",
    "field_name5": "text", 
    "field_name6": "phone"
}
```

## DESCription 

В базе данных хранится список шаблонов форм.

Шаблон формы, это структура, которая задается уникальным набором полей, с указанием их типов.

Всего должно поддерживаться четыре типа данных полей: 
* email
* телефон
* дата
* текст.

На вход по урлу /get_form POST запросом передаются данные такого вида:
f_name1=value1&f_name2=value2

В ответ нужно вернуть имя шаблона формы, если она была найдена.
Чтобы найти подходящий шаблон нужно выбрать тот, поля которого совпали с полями в присланной форме. Совпадающими считаются поля, у которых совпали имя и тип значения. Полей в пришедшей форме может быть больше чем в шаблоне, в этом случае шаблон все равно будет считаться подходящим. Самое главное, чтобы все поля шаблона присутствовали в форме.

Если подходящей формы не нашлось, вернуть ответ в следующем формате

```
{
    f_name1: FIELD_TYPE,
    f_name2: FIELD_TYPE
}
```


где FIELD_TYPE это тип поля, выбранный на основе правил валидации, проверка правил должна производиться в следующем порядке дата, телефон, email, текст.


---

## forms.json EXAMPLE

```
{
    "_default": {
        "1": {
            "username": "text",
            "email": "email",
            "reg_date": "date",
            "name": "youtube"
        },
        "2": {
            "username": "text",
            "email": "email",
            "reg_date": "date",
            "bio": "text",
            "status": "text",
            "phone": "phone",
            "name": "Sber"
        },
        "3": {
            "username": "text",
            "phone": "phone",
            "name": "Gosuslug"
        }
    }
}
```

---
