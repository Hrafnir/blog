from Database import Database
import uuid
import datetime
from models.post import Post


class Blog:
    def __init__(self, author, title, description, id_of_blog=None):
        self.author = author
        self.title = title
        self.description = description
        self.blog_id = uuid.uuid4().hex if id_of_blog is None else id_of_blog

    def new_post(self):
        content = input('Enter post content: ')
        title = input('Enter post title: ')
        date = input('Enter post date, or leave blank if u want to generate it automaticaly(DDMMYYYY): ')
        if date == '':
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, '%d%m%Y')
        post = Post(blog_id=self.blog_id,
                    title=title,
                    content=content,
                    author=self.author,
                    created_date=date)
        post.save_to_db()

    def get_posts(self):
        return Post.from_blog(self.blog_id)

    def save_to_db(self):
        Database.insert(collection='blogs',
                        data=self.json())

    def json(self):
        return {
            'Author': self.author,
            'Title': self.title,
            'Description': self.description,
            'Blog_id': self.blog_id
        }
    @classmethod
    def get_from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs', query={'Blog_id': id})
        return cls(author=blog_data['Author'],
                   title=blog_data['Title'],
                   description=blog_data['Description'],
                   id_of_blog=blog_data['Blog_id'])
