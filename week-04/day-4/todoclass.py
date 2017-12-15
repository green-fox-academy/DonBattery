# This class will deal with the todo.dat file also manage the virtual list (vList)
class Lister():

    def __init__(self, filepath):

        # filepath is the only parameter of this class, pointing to the file Lister shall manipulate
        self.filePath = filepath

        # present will be True if the file is already created or it can be created
        # empty will be True if the file doesnt have any todo registerted
        # read will be True if the file can be opened for read
        # write will be True if the file can be opened for write
        self.fileOK = {'present' : False, 'empty' : True, 'read' : False, 'write' : False} 

        # pos refers to the position of list item
        # todo is True if the user needs to do the task, it is False if it is already done
        # text contains the actual todo string
        self.vList = [{'pos' : 0, 'todo' : False, 'text' : ''}]    

        # let's test the file now, if it can be manipulated
        # if the file does not exist it will be created
        self.testFile()

        # fill our virtual list for easy data manipulation if there is any
        if not self.fileOK['empty']:
            self.buildVlist()

    # handle all the errors, set up fileOK booleans, also create the file if not present
    def testFile(self):
        try:
            with open(self.filePath, 'r+') as fFile:
                self.fileOK['present'] = True
                rawlist = fFile.readlines()
                self.fileOK['read'] = True
                self.fileOK['write'] = True
                if len(rawlist) > 0:
                    self.fileOK['empty'] = False
        except PermissionError:
            self.fileOK['present'] = True
            print('Permission Error ', self.filePath)
        except IOError:
            print('Cannot open ', self.filePath)
            try:
                with open(self.filePath, 'w+') as fFile:
                    self.fileOK['present'] = True
                    self.fileOK['empty'] = True
                    self.fileOK['read'] = True
                    self.fileOK['write'] = True
                    print('File has been created ', self.filePath)
            except IOError:
                print('File cannot be created', self.filePath)
        except Exception as err:
            print('As I tried to mainpulate ', self.filePath)
            print(err)

    # build the virtual list
    def buildVlist(self):
        with open(self.filePath, 'r+') as fFile:
            rawlist = fFile.readlines()
        for i in range(len(rawlist)):
            if i == len(rawlist) - 1:
                taskString = rawlist[i][3:] # last line does not need to be trimmed
            else:
                taskString = rawlist[i][3:-1] # Cut the newline char from the end of lines
            self.vList.append({'pos' : i + 1, 'todo' : True, 'text' : taskString})
            if rawlist[i][0:3] == '[X]':
                self.vList[i + 1]['todo'] = False

    # re-index the virtual list according to the items actual position on the list (needed after removal)
    def reindexVlist(self):
        for i in range(len(self.vList)):
            self.vList['pos'] = i

    # removes n item (by index found in indexlist) from the virtual list and calls reindex on it
    def remover(self, indexlist):
        tempList = []
        indexlist = list(set(indexlist)) # no funny duplications pls...       
        for i in range(len(self.vList)):
            copied = False
            for j in range(len(indexlist)):
                if 0 < indexlist[j] < len(self.vList): # do not remove the 0th element, and do not go out index plox
                    if indexlist[j] != self.vList[i]['pos'] and not copied:
                        tempList.append(self.vList[i])
                        copied = True
        self.vList = tempList
        self.reindexVlist

    def completer(self, indexlist):
        for i in range(len(self.vList)):
            for j in range(len(indexlist)):
                if 0 < indexlist[j] < len(self.vList):
                    self.vList[i]['todo'] = False

    # append the virtual list with given string (fine tuning needed for special characters)
    def appender(self, sString):
        if len(sString) > 0:    # will not append with epmpty task
            self.vList.append({'pos' : len(self.vList), 'todo' : True, 'text' : sString})
    
    # get the lenght of the longest task string
    def getlongest(self):
        max = 0
        for i in range(len(self.vList)):
            if len(self.vList[i]['text']) > max:
                max = len(self.vList[i]['text'])
        return max
    
    # write the virtual list to the file defined by self.filePath
    def writer(self):
        if len(self.vList) > 0:
            with open(self.filePath, 'w+') as fFile:
                for i in range(1, len(self.vList)):
                    symbol = ''
                    if self.vList[i]['todo'] == True:
                        symbol += '[ ]'
                    else:
                        symbol += '[X]'
                    symbol += self.vList[i]['text'] + "\n"
                    fFile.write(symbol)

# as i was too lazy i have merged the controller and the arg-compiler into one class...
# let me introduce you to the mighty todoer
class Todoer():

    def __init__(self, filepath):

        # this also have one parameter the filepath which is passed to the lister object lLister
        self.lLister = Lister(filepath)        
        
        # shure what is shure
        self.present = True

    # given 0 compilable (to actual commands) arguments todoer will print out usage
    def printusage(self):
        print("\nUsage:\n-l   Lists all the tasks\n-a   Adds a new task\n-r   Removes a task\n-c   Completes a task")

    # True if given string is a command    
    def iscommand(self, sString):
        return sString in ['-l', '-a', '-r', '-c']

    # seek string part between -a another command or EOL
    def seekString(self, args, index):
        sString = ''
        ended = False
        while index < len(args) and not ended:
            if not self.iscommand(args[index]):
                sString += args[index] + ' '
            else:
                ended = True
            index += 1        
        return sString
    
    # Return the indexes of items the user wants to remove / complete
    def get_indexlist(self, args, index):
        ilist = []
        ended = False
        while index < len(args) and not ended:
            if not self.iscommand(args[index]):
                if args[index].isdigit:
                    if 0 < int(args[index]) < len(self.lLister.vList):
                        ilist.append(int(args[index]))
            else:
                ended = True
            index += 1
        return ilist

    # Compile the sys.argv list to actual commands (and parameters)
    def compile_args(self, args):
        commandlist = []
        indexlist = []
        for i in range(len(args)):
            if args[i] == '-l':
                commandlist.append({'command' : 'l', 'indexlist' : [], 'text' : ''})
            elif args[i] == '-a':
                if len(args) > i + 1:
                    commandlist.append({'command' : 'a', 'indexlist' : [], 'text' : self.seekString(args, i + 1)})
            elif args[i] == '-r':
                if len(args) > i + 1:                    
                    commandlist.append({'command' : 'r', 'indexlist' : self.get_indexlist(args, i + 1), 'text' : ''})
            elif args[i] == '-c':
                if len(args) > i + 1:                    
                    commandlist.append({'command' : 'c', 'indexlist' : self.get_indexlist(args, i + 1), 'text' : ''})                
        return commandlist
   
    def printlist(self):
        if len(self.lLister.vList) < 2:
            print('TODO List is empty')
        else:
            print('\nTODO List :\n')
            print('No Done Task')
            for i in range(1, len(self.lLister.vList)):
                symbol = ' ' + str(i)
                if i > 9 : symbol = str(i)
                if self.lLister.vList[i]['todo'] == True:
                    symbol += ' [ ]  '
                else:
                    symbol += ' [X]  '
                symbol += self.lLister.vList[i]['text']
                print(symbol)
    
    # compile sys.argv into actual commands then execute them step by step
    def doit(self, arglist):
        print("\nMiki's TO-DO App\n")  
        commands = self.compile_args(arglist)
        if len(commands) == 0:
            self.printusage()
        else:
            for com in commands:
                if com['command'] == 'l':
                    self.printlist()
                elif com['command'] == 'a':
                    self.lLister.appender(com['text'])
                elif com['command'] == 'r':
                    self.lLister.remover(com['indexlist'])
                elif com['command'] == 'c':
                    self.lLister.completer(com['indexlist'])
        print(commands)
        print(self.lLister.vList)
        self.lLister.writer()