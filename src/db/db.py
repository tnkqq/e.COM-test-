from tinydb import TinyDB, Query

db = TinyDB('forms.json')

# f1 = {'name': 'Gosuslg', 'username': 'text', 'usr_email': 'email', 'usr_phone': 'phone'}
# f2 = {'name': 'yt', 'person_name': 'text', 'person_email': 'email'}
# f3 = {'name': 'Sber', 'first_name': 'text', 'last_name': 'text', 'email': 'email', 'phone': 'phone'}


# db.insert_multiple([f1, f2, f3])


class Form:

    F = Query()

    @classmethod
    def get_form_pattern(cls, form_types: dict[str, str]) -> list[tuple[str, int]]: 

        forms = db.all()
        matched_forms = []

        for f in forms:
            flag = 0
            for field_n, field_t in f.items():
                if field_n != 'name':
                    if form_types.get(field_n) == field_t:
                        pass 
                    else:
                        flag = 1 
                        break
            if flag == 0:
                print(f.get('name'))
                matched_forms.append((f.get('name'), len(f.keys())))

        return matched_forms


# test_form = {'username': 'text', 'usr_email': 'email', 'usr_phone': 'phone'}
# test_form2 = {'username': 'text', 'usr_email': 'email', 'usr_phone': 'phone', 'first_name': 'text', 'last_name': 'text', 'email': 'email', 'phone': 'phone'}

# print(Form.get_form_pattern(test_form2))