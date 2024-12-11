from fastapi import APIRouter, Request, Depends
from db.db import FormDB
from db.schemas import FormFields, SPattern
from typing import Annotated


router = APIRouter(
)


@router.post(
    '/get_form',
    name='Паттерн формы', 
    description='Поиск паттернов формы.')
async def get_form(request: Request):
    query_parameters_dict = request.query_params
    f = (
        FormFields
        .create_form_model(query_parameters_dict)
        .model_dump()
    )

    patterns = FormDB.get_form_pattern(f)

    if len(patterns) != 0:
        return {'patterns': patterns}
    else:
        return f


@router.get(
    '/patterns', 
    description='Получение всех паттернов.',
    name='Список паттернов',
    )
async def get_patterns() -> list[dict[str, str]]:
    return FormDB.get_patterns()


@router.post(
    '/patterns',
    description=('''Создание паттерна формы.
    Fields dict[name: str, field_name: Literal[date, phone, email, text]]'''),
    name='Создание паттерна формы',
    )
async def post_pattern(p: Annotated[SPattern, Depends()]) -> None:
    try:
        p = p.model_dump()
        print(p)
        pattern = {
            k: v 
            for k, v in p.get('fields').items()
        }

        pattern['name'] = p.get('name')

        FormDB.insert_patterns(
            [pattern,]
        )
        return FormDB.get_patterns()
    except:
        return {'ERROR': 'cant insert this patter {p}'}

@router.delete(
    '/patterns',
    name='Удаление паттернов.',
    description='Удаление всех паттернов.'
)
async def delete_patterns():
    FormDB.delete_patterns()
    
