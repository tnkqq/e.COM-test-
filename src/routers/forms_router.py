from fastapi import APIRouter, Request
from db.db import FormDB
from db.schemas import FormFields, SPattern


router = APIRouter()


@router.post('/get_form')
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


@router.get('/patterns')
async def get_patterns() -> list[dict[str, str]]:
    return FormDB.get_patterns()


@router.post('/patterns',)
async def post_pattern(p: SPattern) -> None:
    try:
        p = p.model_dump()
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
