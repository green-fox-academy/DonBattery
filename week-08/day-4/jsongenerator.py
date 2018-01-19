# basic JSON file generator
import os
from filer import File_Controller

   "postID" : 0,
   "point" : 0,
   "author" : 0,
   "title" : "",
   "text" : "",
   "comment_counter" : 0,
   "timestamp" : 0

class Post_generator(object):
    def __init__(self):
        self.json_file = File_Controller('', 'posts.json')

    def generate_postfile(self, post_amount):
        if not self.json_file.test_file('C'):
            print('\n')
            for err in self.json_file_con.error_log:
                print(err)
        else:
            