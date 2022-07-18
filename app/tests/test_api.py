import pytest
from app.run import app


def test_api_all():
    response = app.test_client().get('/',  follow_redirects=True)
    assert response.status_code == 200, "—татус - код запроса постов не верный"

def chek_field(post):
    fields = ["poster_name", "poster_avatar", "position", "pic", "content", "views_count", "likes_count",
              "pk"]

    for field in fields:
        assert hasattr(post, field), f"нет пол€{field}"




