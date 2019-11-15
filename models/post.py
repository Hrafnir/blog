import uuid
from Database import Database
import datetime
__author__ = 'hraffy'


class Post:

    def __init__(self, blog_id, title, content, author, created_date=datetime.datetime.utcnow(), post_id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date
        self.post_id = uuid.uuid4().hex if post_id is None else post_id


    def save_to_db(self):
        Database.insert(collection='articles',
                        data=self.json())

    def json(self):
        return {
            'id': self.post_id,
            'Blog_id': self.blog_id,
            'Title': self.title,
            'Content': self.content,
            'Author': self.author,
            'Created_date': self.created_date
        }

    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection='posts', query={'id': id})
        return cls(blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   created_date=post_data['created_date'],
                   post_id=post_data['id'])

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='articles', query={'blog_id': id})]

