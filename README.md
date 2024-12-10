## Start project 
Создание виртуального окружения 
```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```
Каталог приложения
```bash 
cd src/
```
Запуск приложения
```bash
uvicorn app:app --reload 
```

**http://127.0.0.1:8000/docs/**

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


### GET patterns/

response - list of patterns in db 

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

body fields 
* name - srt
* fields - dict[str, type] 

type can be one of [text, email, phone, date]

body example

```
{
    "name": "PatternName",
    "fields": {
        "field_name1": "text",
        "field_name2": "email",
        "field_name3": "date",
        "field_name4": "text",
        "field_name5": "text", 
        "field_name6": "phone"
    }
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