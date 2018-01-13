# This class controls a single file. 
# Can test it for permission, read, write and epmtynes. Also able to create it.
import os.path

class File_Controller():

    def __init__(self, file_path, file_name):

        # based on file_path and file_name File_Controller can identify on which file it needs to work on
        
        # (file_path checker needs to be implemented !!!! because we are currently assuming it is correct)       

        # the working directory
        self.file_path = file_path

        # filename
        self.file_name = file_name

        # sum of the two above
        self.true_path = os.path.join(self.file_path, self.file_name) 

        # readlines
        self.file_as_lines = []

        # !!!!!! ALL the errors will be contained here !!!!
        # get_errors() will return this list
        self.error_log = []
        
        # after running the test_file() method, the file_stat dictionary will be populated with essential info on the file
        # present will be True if the file is already created or it has been created
        # empty will be True if the file does not have any content
        # read will be True if the file can be opened for read
        # write will be True if the file can be opened for write            
        self.file_stat = {'present' : False, 'empty' : True, 'read' : False, 'write' : False}

    
    # this will try to create the file (and set file_stat(s) accordingly) and appends the error_log if exception occures
    def create_file(self):
        succes = False
        try:
            with open(self.true_path, 'w+') as sanyika:
                self.file_stat['present'] = True
                self.file_stat['empty'] = True
                self.file_stat['read'] = True
                self.file_stat['write'] = True
                succes = True
        except PermissionError:
            self.error_log.append('You have no sufficent permission to create ' + self.true_path)
        except IOError:
            self.error_log.append('File cannot be created ' + self.true_path)
        except Exception as err:
            self.error_log.append('as I tried to create ' + self.true_path + ' ' + str(err))
        return succes                    

    # all the errors goes into the error_log list
    # set up file_stat booleans
    # with the 'C' operator also creates the file if not present  
    # populates file_as_text with readlines   
    def test_file(self, operator = ''):
        succes = False
        try:
            with open(self.true_path, 'r+', encoding="utf8") as f_file:
                self.file_stat['present'] = True
                self.file_as_lines = f_file.readlines()
                self.file_stat['read'] = True
                self.file_stat['write'] = True
                succes = True
                if len(self.file_as_lines) > 0:
                    self.file_stat['empty'] = False
        except PermissionError:
            self.error_log.append('You do not have sufficent permission to manipulate ' + self.true_path)
            self.file_stat['present'] = True
        except IOError:
            self.error_log.append('Cannot open ' + self.true_path)
            if operator == 'C':
                succes = self.create_file()                
        except Exception as err:
            self.error_log.append('as I tried to manipulate ' + self.true_path + ' ' + str(err))
        return succes

    # warning right now this overwrites the whole file!
    def one_line_writer(self, line):
        succes = False
        try:
            with open(self.true_path, 'w+', encoding="utf8") as f_file:
                f_file.write(str(line))
                succes = True
        except PermissionError:
            self.error_log.append('You do not have sufficent permission to write to ' + self.true_path)
        except IOError:
            self.error_log.append('Cannot create ' + self.true_path)
        except Exception as err:
            self.error_log.append('as I tried to recreate ' + self.true_path + ' ' + str(err))
        return succes
    
    def get_errors(self):
        return self.error_log