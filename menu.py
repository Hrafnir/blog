from Database import Database
from models.Blog import Blog

__author__ = 'jslvtr'


class Menu:
    def __init__(self):
        self.user = input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'Author': self.user})
        if blog is not None:
            self.user_blog = Blog.get_from_mongo(blog['Blog_id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_db()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Do you want to read (R) or write (W) blogs? ")
        if read_or_write == 'R':
            self._list_blogs()
            self._view_blog()
        elif read_or_write == 'W':
            self.user_blog.new_post()
        else:
            print("Thank you for blogging!")

    @staticmethod
    def _list_blogs():
        blogs = Database.find(collection='blogs',
                              query={})
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['Blog_id'], blog['Title'], blog['Author']))

    @staticmethod
    def _view_blog():
        blog_to_see = input("Enter the ID of the blog you'd like to read: ")
        blog = Blog.get_from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {}, title: {}\n\n{}".format(post['Created_date'], post['Title'], post['Content']))