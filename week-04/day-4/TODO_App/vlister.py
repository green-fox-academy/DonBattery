# Virtual list class for todo-er
# later can be altered to control different virtual list
class Virtual_List_Controller():

    def __init__(self, raw_text, separator, character_blacklist):

        # right now it is dessigned to get a string and separate it to lines 
        # excluding the blacklisted characters
        # add a [ ] to the begining of every new line
        # and change the [ ] tag to the [X] tag by index
        # also multiple elements can be removed by index

        self.character_blacklist = character_blacklist

        self.v_list = raw_text.split(separator)

    
    # adds a string to the v_list minus the blacklisted characters
    def appender(self, s_string):
        temp_string = ''
        for i in range(len(s_string)):
            if s_string[i] not in self.character_blacklist:
                temp_string += s_string[i]
        if len(s_string) > 0:
            self.v_list.append('[ ]' + temp_string)

    # removes n item (by index found in index_list) from the virtual list (0th element will not be removed
    # also we wont get out of index range)
    def remover(self, index_list):
        temp_list = []
        temp_index = []
        for index in index_list:
            if 0 < index < len(self.v_list):
                temp_index.append(index)
        for i in range(len(self.v_list)):
            if i not in temp_index:
                temp_list.append(self.v_list[i])
        self.v_list = temp_list[:]

    # todo specific method (completing n task by index)
    # may be changed with something more generic
    def completer(self, index_list):
        for i in range(len(self.v_list)):
            for j in range(len(index_list)):
                if 0 < index_list[j] < len(self.v_list):
                    if index_list[j] == i:
                        temp_string = self.v_list[i][3:]
                        symbol = '[X]'
                        self.v_list[i] = symbol + temp_string

    # turn v_list into a one-liner using the separator
    def get_one_line(self):
        temp_string = ''        
        for i in range(len(self.v_list)):
            symbol = ''
            if i < len(self.v_list) - 1 :
                symbol = ';'
            temp_string += self.v_list[i] + symbol
        return temp_string