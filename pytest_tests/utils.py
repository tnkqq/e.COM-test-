
import random 

TEST_TEXT = [
    'random_text_1',
    'random_t!ext_2',
    'r3andom_t!ext_2',
]
TEST_DATE =[
    '01.07.2004',
    '01-07-2004',
    '2004.07.01',
    '2004-07-01',
]
TEST_EMAI = [
    'test1@mail.ru',
    'test1@gmail.com',
]
TEST_PHONE = [
    '+79874567890',
    '+29874567890',
    '89874567890',
    '8(987)4567890',
    '+7-987-456-78-90',
    ]

def generate_form_by_pattern(pattern: dict):
    form = {}
    for k, v in pattern.items():
        if k != 'name':
            if v == 'text':
                form[k] = random.choice(TEST_TEXT)
            elif v =='email':
                form[k] = random.choice(TEST_EMAI)
            elif v == 'date':
                form[k] = random.choice(TEST_DATE)
            else:
                form[k] = random.choice(TEST_PHONE)
    return form