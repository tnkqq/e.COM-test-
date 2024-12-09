from pydantic import BaseModel, EmailStr, field_validator, create_model, validator
from pydantic_extra_types.phone_numbers import PhoneNumber
from typing import Union
from datetime import datetime
from dateutil.parser import parse
import re




class FormFields():
    @staticmethod
    def create_form_model(form: dict):
        validators = {
            f'{k}-valid': field_validator(k, mode='after')
            (FormFields.validate_field) 
            for k in form.keys()
        }

        dynamic_form = create_model(
            'DynamicField',
            __validators__= validators,

            **{k: (type(v), ...)
            for k, v in form.items()},

        )
        return dynamic_form(**form)

    def validate_field(v):
        ###
        #DATE
        ###
        try:
            parse(v, fuzzy=False)
            is_date = True
        except:
            is_date = False 

        if is_date and not v.isnumeric():
            return 'datetime'

        ###
        #PHONE
        ##
        is_phone = re.search(
            r'^(\+7|8)(\s|-)?(\()?[0-9]{3}(\))?(\s|-)?([0-9]{3})(\s|-)?([0-9]{2})(\s|-)?([0-9]{2})$',
            v
            )

        if is_phone:
            return 'phone'

        ###
        #EMAIL
        ##
        email = re.search(
            r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
            v
        )

        if email:
            return 'email'

        ###
        #TEXT
        ###
        else:
            return 'text'

a = {'name': 'Vlad', 'user_phone': '+79459843456', 'email': 'urmail@mail.ru', 'date': '2024.7.12'}

f = FormFields.create_form_model(a)

print(f.model_dump())

