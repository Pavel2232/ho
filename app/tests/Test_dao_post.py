from app.post.dao.post_dao import PostDAO,DATA_PATH
import pytest

@pytest.fixture()
def post_dao():
    posts_dao_instance = PostDAO(DATA_PATH)
    return posts_dao_instance

# Задаем, какие ключи ожидаем получать у кандидата
keys_should_be = {"poster_name", "poster_avatar", "position", "pic", "content", "views_count", "likes_count","pk"}

class TestPostDao:

    def test_get_all(self, post_dao):
        """ Проверяем, верный ли список кандидатов возвращается """
        posts = post_dao.get_all()
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_by_id(self, post_dao):
        """ Проверяем, верный ли кандидат возвращается при запросе одного """
        posts = post_dao.get_by_pk(1)
        assert(posts["pk"] == 1), "возвращается неправильный кандидат"
        assert set(posts.keys()) == keys_should_be, "неверный список ключей"