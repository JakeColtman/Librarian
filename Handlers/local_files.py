'''

Control system for local files

Current support:

    CSV
    XLS

'''

import xlrd, os
from _base import BaseExtractor
 

class LocalExtractor(BaseExtractor):
    
    def __init__(self, directory, file_name):
        
        print "Forming a local file name object"
        
        self.file_name = os.path.join(directory, file_name)
        
        self.file_type = self._identify_file_type()
        
        self.file_type_processing_lookup = {"csv":self._get_csv, "xls": self._get_excel}
        
        
    def get(self):
        
        '''
        Identify the file type and get accordingly
        '''
        

        try:
            
            return self.file_type_processing_lookup[self.file_type]()
        
        except KeyError:
            
            print KeyError   
            
    def _identify_file_type(self):
        '''
        This is clearly terrible, improve me
        '''
        
        return self.file_name[-3:]
        
        
    def _get_csv(self):
        
        '''
        TODO: Make the formatting more useful that one long string
              Dictionary?
        
        '''
        
        with open(self.file_name, "r") as fileOpen:
             
            contents = fileOpen.read()
             
        return contents
    
    def _get_excel(self):
        
        '''
        Ideally this would only be used on files coming in from 
        external suppliers (API, FTP etc)
        
        TODO: Make this prettier
        TODO: Make format more useful
        '''
        
        
        
        wb = xlrd.open_workbook(self.file_name)        

        output = []
        
        for s in wb.sheets()[0:1]:
            
            for row in range(s.nrows):
                
                values = []
                
                for col in range(s.ncols):
                        
                        values.append(str(s.cell(row,col).value))
                        
                output.append(",".join(values))
        
        return "\n".join(output)
    
#     #Input: string, string; Output: bool
#     def write(self, file_name, contents):
#         
#         '''
#         Exports into the data store
#         Returns true is success
#         '''
#         
#         with open(file_name, "w+b") as fileOut:
#             
#             fileOut.write(contents)
#             
#         return True
    
LocalExtractor("hkjh", "test.csv")
    
    