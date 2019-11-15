from Database import Database
import uuid
import datetime
import models.post


class Blog:

    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        content = input('Enter post content: ')
        title = input('Enter post title: ')
        date = input('Enter post date, or leave blank if u want to generate it automaticaly(DDMMYYYY): ')
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=datetime.datetime.strptime(date, '%d%m%Y'))
        post.save_to_db()
    def get_posts(self):
        return models.Post.from_blog(self.id)

    def save_to_db(self):
        Database.insert(collection='blogs',
                        data=self.json())

    def json(self):
        return {
            'Author': self.author,
            'Title': self.title,
            'Description': self.description,
            'Blog_id': self.id
        }
    @classmethod
    def get_from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs', query={'id': id})
        return cls(author=blog_data['author'],
                    title=blog_data['title'],
                    description=blog_data['description'],
                    id=blog_data['id'])