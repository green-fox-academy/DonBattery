# This class is dessigned to compile a list of arguments into commands 
# based on the allowed_commands dictionaries it gets when initialized
# hopefully this will be highly flexible / reusable with future development
class Argument_Compiler():

    def __init__(self, arg_list, allowed_commands):

        # list of arguments
        self.arg_list = arg_list

        # list of dictionaries containing allowed commands by operator and type 
        self.allowed_commands = allowed_commands

        # this will contain the commands translated from arguments
        self.command_list = []        

        # list of allowed operators, to compare with each argument
        self.actual_commands = []

        for command in self.allowed_commands:
            self.actual_commands.append(command['operator'])
       
       # upon init Argument_Compiler do its work, get_commands() will return the translated commands
        self.compile_args()        

    # seek string parts between two actual command (or end of arg_list) 
    # and return them chained together (separated by spaces and stripped at the end)
    def get_string_chain(self, index):
        string_chain = ''
        ended = False
        while index < len(self.arg_list) and not ended:
            if self.is_command(self.arg_list[index]):
                ended = True
            else:
                string_chain += self.arg_list[index] + ' '
            index += 1                    
        return string_chain.strip()
    
    # return numeric items as a list, found in between two arg-command (or end of list)
    def get_num_list(self, index):
        num_list = []
        ended = False
        while index < len(self.arg_list) and not ended:
            if self.is_command(self.arg_list[index]):
                ended = True
            else:
                if self.arg_list[index].isdigit():
                    num_list.append(int(self.arg_list[index]))
            index += 1
        return num_list
    
    # returns an allowed command's type based on its operator
    def get_command_type(self, arg):
        for command in self.allowed_commands:
            if arg == command['operator']:
                return command['type']
    
    # True if given string is an actual command    
    def is_command(self, s_string):
        return s_string in self.actual_commands
    
    # simply just returns the command_list
    def get_commands(self):
        return self.command_list

    # empty the command_list
    def reset_command_list(self):
        self.command_list = []

    def no_commands(self):
        return len(self.command_list) == 0

    # returns a list of commands translated from an argument-list
    def compile_args(self):
        self.reset_command_list()
        for i in range(len(self.arg_list)):
            item = ''
            command = ''
            command_type = ''
            empty = False
            if self.is_command(self.arg_list[i]):
                command = self.arg_list[i]
                command_type = self.get_command_type(command)
                if command_type == 'String_Chain':
                    if len(self.arg_list) > i + 1:
                        item = self.get_string_chain(i + 1)
                        if len(item) == 0: 
                            empty = True
                elif command_type == 'Int_List':
                    if len(self.arg_list) > i + 1:
                        item = self.get_num_list(i + 1)
                        if len(item) == 0: 
                            empty = True
                if not empty:
                    self.command_list.append({'command' : command, 'type' : command_type, 'item' : item})               
        return len(self.command_list)
