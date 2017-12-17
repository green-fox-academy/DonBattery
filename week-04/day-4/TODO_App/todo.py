#ToDo Controller
# We need sys for catching the arguments and pass them to the compiler 
import sys
from todoer import Todoer

# The working path of our database (it's filename will be "to.do")
file_path = ""

my_todoer = Todoer(file_path, sys.argv)

my_todoer.do_your_thing()
