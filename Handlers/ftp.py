'''

Handles getting files from ftp

Collection of low level functions to make life easier

'''

from ftplib import FTP
from StringIO import StringIO
from _base import BaseExtractor

##Low level functions

#Input: string, string, string; Output: ftpConn
def _connect_to_ftp(location, username, password):

    ftp = FTP(location)
        
    ftp.login(user = username, passwd = password)
    
    return ftp


##Main Class

class FTPExtractor(BaseExtractor):
    
    def __init__(self, location, username, password, file_name):
        
        self.file_name = file_name
        
        self.conn = _connect_to_ftp(location, username, password)

    #Input string; Output string
    def get(self):
        
        contents = StringIO()
        
        self.conn.retrbinary('RETR ' + self.file_name, contents.write)
    
        return contents.getvalue()
    