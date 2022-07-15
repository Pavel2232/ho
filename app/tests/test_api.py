import pytest
from app.run import app


def test_api_all():
    response = app.test_client().get('/',  follow_redirects=True)
    assert response.status_code == 200, "Статус - код запроса постов не верный"




