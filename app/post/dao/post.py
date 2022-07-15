import json

class Post:

    def __init__(self,poster_name="" , poster_avatar="",pic = "",content = "",views_count=0,likes_count=0,pk=0):
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content
        self.views_count = views_count
        self.likes_count = likes_count
        self.pk = pk

    def __repr__(self):
        return f"{self.poster_name}"

