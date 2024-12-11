from http import HTTPStatus

import pytest

from fastapi import FastAPI
from httpx import AsyncClient

class TestForms:
    @pytest.mark.asyncio
    async def test_forms_matches(self, app: FastAPI, client: AsyncClient, forms):
        '''
        generate form from pattern in db 
        request with current form
        pattern in response.patterns  
        '''
        pattern = forms[0]
        form  = forms[-1]
        res = await client.post(app.url_path_for('Паттерн формы'), params=form)
        assert pattern in [_[0] for _ in res.json().get('patterns')]
