from app.post.dao.post_dao import PostDAO,DATA_PATH
from app.post.dao.post import Post
import pytest


def chek_field(post):
        fields = ["poster_name", "poster_avatar", "position", "pic", "content", "views_count", "likes_count",
                  "pk"]

        for field in fields:
            assert hasattr(post, field), f"нет поля{field}"


# Задаем, какие ключи ожидаем получать у кандидата

class TestPostDao:

    @pytest.fixture
    def post_dao(self):
        posts_dao_instance = PostDAO(DATA_PATH)
        return posts_dao_instance

    def test_get_all_types(self, post_dao):
        """ Проверяем, верный ли список кандидатов возвращается """
        posts = post_dao.get_all()
        assert type(posts) == list, "возвращается не список"

        post = post_dao.get_all()[0]
        assert type(post) == Post, "неверный список Класса"

    def test_get_by_id(self, post_dao):
        """ Проверяем, верный ли кандидат возвращается при запросе одного """
        posts = post_dao.get_all()

        correct_pks = {1,2,3}
        pks = set([post.pk for post in posts])
        assert pks == correct_pks, "Не совпадает получение id"
###функция получения 1 по pk

    def test_get_all_fields(self,post_dao):
        post = post_dao.get_post_by_pk(1)
        chek_field(post)

    def test_get_by_pk_none(self,post_dao):
        post = post_dao.get_post_by_pk(999)
        assert post is None,"Нет такого пользолвателя"

    @pytest.mark.parametrize("pk", [1,2,3])
    def test_get_by_pk_correct_id(self,post_dao,pk):
        post = post_dao.get_post_by_pk(pk)
        assert  post.pk == pk, f"Не ключь пк для запроса пк"

        ### Функция получения постов по имени автора
    def test_search_is_correct(self, post_dao):
        posts = post_dao.search_for_posts("ага")
        assert  type(posts) == list, "Вернулся не список"

        post = post_dao.get_all()[0]
        assert type(post) == Post, "Неккоректный тип 1 поста"

    def test_search_is_correct_not_found(self, post_dao):
        posts = post_dao.search_for_posts("9999999999999")
        assert  posts == [] , "Ничего не найдено"

    @pytest.mark.parametrize("s,expected_pks",[
        ("Ага", {1}),
        ("Вышел", {2}),
        ("на", {3})
    ])

    def test_search_is_coerrect_result(self,post_dao,s,expected_pks):
        posts = post_dao.search_for_posts(s)
        pks = set([post.pk for post in posts])
        assert pks == expected_pks, f"Не найден результат для {s}"