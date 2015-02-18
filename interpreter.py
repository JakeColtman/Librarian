import Extractors.ftp as ftp, Extractors.local_files as local_files
import Inserters.local_files as local_files_put
from time import sleep
from dataHolder import DataState


'''
Abstract
'''

def abs_get_from_store(data, storeObj):
    
    file_name = data.get_file_name()
    
    try:
        
        content = storeObj.get()
        
    except:
        
        content = None
        
    return DataState(file_name = file_name, content = content)
    
    


'''
Local Data Store
'''

def try_get_from_local_file_store(data):
    
    return abs_get_from_store(data, local_files.LocalExtractor)
    
def try_put_into_local_file_store(file_name, content):
    
    try:
        
        file_store = local_files_pit.LocalInserter(BASE_DIR, file_name)
        
        file_store.put(content)

    except Exception, e:

        return False
    
    
'''
DEFAULT DATA STORE
'''

def try_get_file_from_base(data):
    
    return try_get_from_local_file_store(data)

def try_put_content_into_base(file_name, content):
    
    return try_put_into_local_file_store(file_name, content)


'''
Example FTP store
'''

def try_get_from_example_ftp_store(data):
    
   username, password, location = 'YOURUSERNAME', 'YOUPASSWORD', 'YOURLOCATION'

   storeObj = ftp.FTPExtractor(username = username, password = password, location = location, file_name = data.get_file_name())
   
   return abs_get_from_store(data, storeObj)
    
    
'''
Highest Level
'''
   
store_or_ftp = [try_get_file_from_base, try_get_from_example_ftp_store]

    