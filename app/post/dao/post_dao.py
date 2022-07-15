import json
from app.post.dao.post import Post
from json import JSONDecodeError
from exceptions.data_exceptions import DataSourceError

DATA_PATH = r"C:\Users\Павел\PycharmProjects\homeCourse2\app\data\data.json"


class PostDAO:

    def __init__(self,path):
        self.path = DATA_PATH

    def load_data(self):

      try:
        with open(self.path, "r", encoding="utf-8") as f:
            post_data = json.load(f)
      except(FileNotFoundError, JSONDecodeError):
          raise DataSourceError(f"Не удается получить данные из файла{self.path}")

      posts = []
      for post in post_data:
          posts.append(Post(
              post["poster_name"],
              post["poster_avatar"],
              post["pic"],
              post["content"],
              post["views_count"],
              post["likes_count"],
              post["pk"]
              ))
          return posts

    def get_all(self):
        return self.load_data()

    def get_posts_all(self, user_name):
        posts = self.load_data()
        users_posts = []
        post_lower = str(user_name).lower()
        for post in posts:
            post_poster_name = post.poster_name.lower()
            if post_lower in post_poster_name:
                users_posts.append(post)
        return users_posts

    def search_for_posts(self,query):
       posts = self.load_data()
       list_post = []
       post_lower = str(query).lower()

       for post in posts:
           post_content = post.content.lower()
           if post_lower in post_content:
               list_post.append(post)
       return list_post

    def get_post_by_pk(self, pk):
        posts = self.load_data()
        for post in posts:
            if post.pk == pk:
                return post

