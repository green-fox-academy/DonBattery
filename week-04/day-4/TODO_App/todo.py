#ToDo Controller
# We need sys for catching the system_arguments and pass them to the compiler 
import sys
from todoer import Todoer

# The working path of our database (the database-filename will be "to.do" by dessign)
# If empty the file will be created where todo.py is located
file_path = ""

my_todoer = Todoer(file_path, sys.argv)

my_todoer.do_your_thing()
