import Handlers.ftp as ftp, Handlers.local_files as local_files

BASE_DIR = "EXAMPLE_DIRECTORY"   
        

'''
Local Data Store
'''

def try_get_from_local_file_store(file_name):
    
    try:
        
        return local_files.LocalExtractor(BASE_DIR, file_name).get()

    except:
        
        return False

'''
Example FTP store
'''

def try_get_from_example_ftp_store(file_name):
    
    try:
 
        return ftp.FTPExtractor(username = username, password = password, location = location, file_name = file_name).get()
    
    except:
        
        return False

    
    
if __name__ == "__main__":
    
    print try_get_from_example_ftp_store("FILE_NAME")
    