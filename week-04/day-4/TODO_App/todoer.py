# This class is the actual program
# It controls the file, the virtual-list, and the argumentum-compiler
from filer import File_Controller
from vlister import Virtual_List_Controller
from arger import Argument_Compiler
import sys

# let me introduce you to the mighty Todoer
class Todoer():

    def __init__(self, filepath, arglist):
        
        # we can pass these dictionaries to the argumentum-compiler so
        # it will know what commands to search for
        self.allowed_commands = ({'operator' : '-l', 'type' : 'Single', 'item' : ''},
                                {'operator' : '-a', 'type' : 'String_Chain', 'item' : ''},
                                {'operator' : '-r', 'type' : 'Int_List', 'item' : ''},
                                {'operator' : '-c', 'type' : 'Int_List', 'item' : ''})

        # we will deal with a one-line file so we need a record-separator character 
        self.row_separator = ';'

        # obviously we do not accept our separator as an input
        self.character_blacklist = (';')

        # this will be the name of our database-file
        self.file_name = 'to.do'

        # the path of the working directory
        self.file_path = filepath

        # the sys.argv list
        self.arg_list = arglist

        # this object is responsible for testing, reading and writeing the database-file
        self.file_con = File_Controller(self.file_path, self.file_name)

        # if the database-file cannot be operated the program will HALT
        # else it builds up the virtual-list in its vlist_con object
        if not self.file_con.test_file('C'): # print out errors and stops the program if database unreachable
            print(self.file_con.get_errors())
            print('TO-DO halted!')
            sys.exit()
        else:
            if len(self.file_con.file_as_lines) > 0:
                self.vlist_con = Virtual_List_Controller(self.file_con.file_as_lines[0], self.row_separator, self.character_blacklist)
            else:
                self.vlist_con = Virtual_List_Controller('', self.row_separator, self.character_blacklist)

        # this object is the argumentum-compiler: from the argv list and excepted commands
        # it puts the actual calculated commands into its command_lsit
        self.arg_con = Argument_Compiler(self.arg_list, self.allowed_commands)

    # given 0 compilable arguments todoer will print out usage
    def printusage(self):
        print("\nMiki's TO-DO App\n")  
        print("Usage:\n")
        print("-l          Lists all the tasks")
        print("-a <task>   Adds a new task")
        print("-r <index>  Removes a task")
        print("-c <index>  Completes a task")
    
    # print out the todo list, or the "empty message" if the list is empty
    def printlist(self):
        if len(self.vlist_con.v_list) < 2:
            print('\nTODO List is empty')
        else:
            print('\nTODO List :\n')
            print('No Done Task')
            for i in range(1, len(self.vlist_con.v_list)):
                symbol = ' ' + str(i) 
                if i > 9 : symbol = str(i)
                symbol += ' ' + self.vlist_con.v_list[i][0:3] + '  ' + self.vlist_con.v_list[i][3:]
                print(symbol)
    
    # compile sys.argv into actual commands then execute them step by step
    def do_your_thing(self):
            if self.arg_con.no_commands():
                self.printusage()
            else:
                for com in self.arg_con.command_list:
                    if com['command'] == '-l':
                        self.printlist()
                    elif com['command'] == '-a':
                        self.vlist_con.appender(com['item'])
                    elif com['command'] == '-r':
                        self.vlist_con.remover(com['item'])
                    elif com['command'] == '-c':
                        self.vlist_con.completer(com['item'])
            if not self.file_con.one_line_writer(self.vlist_con.get_one_line()): # print errors if writing to database fails
                print(self.file_con.get_errors())