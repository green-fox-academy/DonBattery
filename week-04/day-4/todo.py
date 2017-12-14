#Controller
import sys
from todoclass import Todoer

file_path = "C:/Users/Miki/greenfox/DonBattery/week-04/day-4/TODO.LST"

tTodoer = Todoer(file_path)

tTodoer.doit(sys.argv, file_path)