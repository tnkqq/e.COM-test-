from typing import Union

from tinydb import Query, TinyDB


class FormDB:
    db = TinyDB("forms.json")

    F = Query()

    @classmethod
    def get_form_pattern(
        cls, form_types: dict[str, str]
    ) -> list[tuple[str, int]]:
        forms = cls.db.all()
        matched_forms = []

        for f in forms:
            flag = 0
            for field_n, field_t in f.items():
                if field_n != "name":
                    if form_types.get(field_n) == field_t:
                        pass
                    else:
                        flag = 1
                        break
            if flag == 0:
                matched_forms.append((f.get("name"), len(f.keys()) - 1))
        return matched_forms

    @classmethod
    def insert_patterns(cls, patterns: list[dict[str, Union[str, dict]]]):
        cls.db.insert_multiple(patterns)

    @classmethod
    def get_patterns(cls):
        return cls.db.all()
