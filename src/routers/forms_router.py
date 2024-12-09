from fastapi import APIRouter, Request
from db.schemas import FormFields

router = APIRouter()


@router.post('/get_form')
async def get_form(request: Request):
    query_parameters_dict = request.query_params
    for k, v in query_parameters_dict:
        if FormFields(v):
            
    return {'answ': query_parameters_dict}
