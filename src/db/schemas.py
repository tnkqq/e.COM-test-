import re
from typing import Dict, Literal

from dateutil.parser import parse
from pydantic import (BaseModel, create_model, field_validator,)


class SPattern(BaseModel):
    name: str
    fields: Dict[str, Literal["text", "phone", "email", "date"]]


class FormFields:
    @staticmethod
    def create_form_model(form: dict):
        validators = {
            f"{k}-valid": field_validator(k, mode="after")(
                FormFields.validate_field
            )
            for k in form.keys()
        }

        dynamic_form = create_model(
            "DynamicField",
            __validators__=validators,
            **{k: (type(v), ...) for k, v in form.items()},
        )
        return dynamic_form(**form)

    def validate_field(v: str) -> str:
        ###
        # DATE
        ###
        try:
            parse(v, fuzzy=False)
            is_date = True
        except:
            is_date = False

        if is_date and not v.isnumeric():
            return "date"

        ###
        # PHONE
        ##
        is_phone = re.search(
            r"^([0-9]|\ [0-9]|\+[0-9])(\s|-)?(\()?[0-9]{3}(\))?(\s|-)?([0-9]{3})(\s|-)?([0-9]{2})(\s|-)?([0-9]{2})$",
            v,
        )

        if is_phone:
            return "phone"

        ###
        # EMAIL
        ##
        email = re.search(
            r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", v
        )

        if email:
            return "email"

        ###
        # TEXT
        ###
        else:
            return "text"
