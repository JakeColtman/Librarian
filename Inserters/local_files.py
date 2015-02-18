'''

Control system for local files

Current support:

    CSV

'''

import xlrd, os
from _base import BaseInserter
 

class LocalInserter(BaseInserter):
    
    def __init__(self, directory, file_name):
        
        print "Forming a local file name object"
        
        self.file_name = os.path.join(directory, file_name)
        
        self.file_type = self._identify_file_type()
        
        self.file_type_processing_lookup = {"csv":self._put_csv}
        
        
    def put(self, content):
        
        '''
        Identify the file type and get accordingly
        '''

        try:
            
            return self.file_type_processing_lookup[self.file_type](content)
        
        except KeyError:
            
            print KeyError   
            
    def _identify_file_type(self):
        '''
        This is clearly terrible, improve me
        '''
        
        return self.file_name[-3:]
        
        
    def _put_csv(self, content):
        
        '''

            Puts the data if the file type is csv
        
        '''
        
        listOfStringsContent = [",".join(x) for x in content]
        
        stringContent = "\n".join(listOfStringsContent)
        
        with open(self.file_name, "w") as fileOpen:
             
            fileOpen.write(stringContent)
             
        return True
    
    