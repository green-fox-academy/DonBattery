import os

class Lister():

    def __init__(self, filepath):
        self.filepath = filepath
        
        self.fileOK = False

        self.list = []

        self.tlist = []    

        try:
            with open(self.filepath, 'r') as fFile:
                self.list = fFile.readlines()
        except IOError:
            print('Cannot open ', self.filepath)
            try:
                fFile = open(self.filepath, 'w+')
                fFile.close()
            except IOError:
                print(self.filepath, ' cannot be created')
            else:
                print(self.filepath, ' has been created')
                self.fileOK = True                
        else:
            for i in range(len(self.list)):
                self.tlist.append({'isChecked' : False, 'sString' : ''})
                self.tlist[i]['sString'] = self.list[i][3:]
                if self.list[i][0:3] == '[X]':
                    self.tlist[i]['isChecked'] = True
                else:
                    self.tlist[i]['isChecked'] = False
            self.fileOK = True

    def remover(self, index):
        newlist = []
        newtlist = []
        try:
            with open(self.filepath, 'r+') as fFile:
                lines = fFile.readlines()
                fFile.seek(0)
                for i in range(0, len(lines)):
                    if i != index:
                        fFile.write(lines[i])
                        newlist.append(self.list[i])
                        print('List length :', len(self.list), ' Index:',i)
                        newtlist.append(self.tlist[i])
                        print('tList length :', len(self.tlist), ' Index:',i)
                self.list = newlist
                self.tlist = newtlist
        except IOError:
            print('Cannot remove line form ', self.filepath)

    def appender(self, sString):
        try:
            with open(self.filepath, 'a') as fFile:
                self.tlist.append({'isChecked' : False, 'sString' : sString})
                fFile.write('[ ]' + sString)
        except IOError:
            print('Cannot append ', self.filepath)

    def getlongest(self):
        max = 0
        for i in range(len(self.tlist)):
            if len(self.tlist[i]['sString']) > max:
                max = len(self.tlist[i]['sString'])
        return max

class Todoer():
    def __init__(self, filepath):
        self.lLister = Lister(filepath)        
        self.present = True

    def printusage(self):
        print("Miki's TO-DO App")
        print("Usage:\n-l   Lists all the tasks\n-a   Adds a new task\n-r   Removes a task\n-c   Completes a task")
    
    def seekString(self, args, index):
        self.sString = ''
        ended = False
        while index < len(args) and not ended:
            if args[index] not in ['-l', '-a', '-r', '-c']:
                self.sString += args[index] + ' '
            else:
                ended = True
            index += 1
        if len(self.sString) > 0:
            self.sString += '\n'
        return self.sString
    
    # Return the indexes of items the user wants to remove
    def get_remove_index(self, args, index):
        ilist = []
        ended = False
        while index < len(args) and not ended:
            if args[index] not in ['-l', '-a', '-r', '-c']:
                if args[index].isdigit:
                    if 0 < int(args[index]) <= len(self.lLister.tlist):
                        ilist.append(int(args[index]) - 1)
            else:
                ended = True
            index += 1
        return ilist

    # Compile the argv list to actual commands (and parameters)
    def compile_args(self, args):
        commandlist = []
        indexlist = []
        for i in range(len(args)):
            if args[i] == '-l':
                commandlist.append({'command' : 'l', 'index' : 0, 'sString' : ''})
            elif args[i] == '-a':
                if len(args) > i + 1:
                    commandlist.append({'command' : 'a', 'index' : 0, 'sString' : self.seekString(args, i + 1)})
            elif args[i] == '-r':
                if len(args) > i + 1:
                    indexlist = self.get_remove_index(args, i + 1)
                    if len(indexlist) > 0:
                        for i in range(len(indexlist)):
                            commandlist.append({'command' : 'r', 'index' : indexlist[i], 'sString' : ''})
        return commandlist
   
    def printlist(self):
        if len(self.lLister.tlist) == 0:
            print('TODO List is empty')
        else:
            print('\nTODO List :\n')
            print('No Done Task')
            for i in range(len(self.lLister.tlist)):
                symb = ' '
                if i >= 9:
                    symb = ''
                symb += str(i +1)
                if self.lLister.tlist[i]['isChecked']:
                    symb += '  [X] '
                else:
                    symb += '  [ ] '
                print( symb + self.lLister.tlist[i]['sString'], end = '')
            print()
    
    def appendlist(self, sString):
        self.lLister.appender(sString)
    
    def remover(self, index):
        self.lLister.remover(index)

    def doit(self, arglist, filepath):  
        commands = self.compile_args(arglist)
        if len(commands) == 0:
            self.printusage()
        else:
            for com in commands:
                if com['command'] == 'l':
                    self.printlist()
                if com['command'] == 'a':
                    self.appendlist(com['sString'])
                if com['command'] == 'r':
                    self.remover(com['index'])
        print(commands)

            

    