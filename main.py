'''

Libraries used:

    os
    ftplib
    StringIO
    abc (abstract base class)
    
'''


import os
import interpreter, dataHolder

try:
    
    BASE_DIR = "Yourdirectory"

    os.chdir(BASE_DIR)
    
except: pass

def extractData(data, extractionList):
    
    for extraction in extractionList:
        
        data = extraction(data)
        
        print data
        
        if data.has_value():
            
            return data.get_content()
        
        else:
            
            print "These aren't the droids you're looking for"
        