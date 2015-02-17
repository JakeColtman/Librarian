'''

Libraries used:

    os
    ftplib
    StringIO
    abc (abstract base class)
    
'''


import os
import interpreter

##Low level functions

def get_filename_from_data_source(file_name, source):
    
    try:
        
        return source.get_file(file_name)
    
    except:
        
        return None

def sequential_try_get_from_data_source(file_name, sourceList):
    
    '''
    Takes a list of handlers and looks in them sequentially to try to find the file
    Will return the file contents if found
    Returns None otherwise
    '''
    
    for source in sourceList:
        
        data = get_filename_from_data_source(file_name, source)
        
        if data is not None: 
            
            return data
        
        else:
            
            print "Not found in {0}".format(source)


class Librarian:
    
    '''
    Main access point to get data
    Requests come in, data is found and given out
    
    dataStore: Default place to look for data
    archiveMode: Save all data requested into the dataStore to allow faster retreival
    
    TODO: break a file out into a separate interacting class?
    
    '''
    
    def __init__(self, dataStore, archiveMode = False):
        
        #Not a pretty double storing of info on the store location
        #Change in the get_data_store_location()
        self.isArcive, self.storeLocation = archiveMode, dataStore
        self.store = local_files.LocalHandler()

        #Pretty weak way of dealing with, imporve
        os.chdir(dataStore)
        
        print self.store
        
    def is_in_archive_mode(self):
        
        return self.isArcive
    
    def get_data_store_location(self):
        
        return self.storeLocation
    
    def _is_file_in_data_store(self, file_name):
    
        '''This should eventually be pushed out to the different handlers to allow diff default environments'''
        return file_name in os.listdir(self.get_data_store_location())
    
    def try_get_from_data_store(self, file_name, ifFails = []):
        
        #Run the whole thing rather than filtering based on _is_in_data_store because the simplicity beats 
        #the speed loss at the moment (not the constraining speed factor in run time
        sourceList = [self.store] + ifFails
        
        data = sequential_try_get_from_data_source(file_name, sourceList)
        
        if not self._is_file_in_data_store(file_name) and self.is_in_archive_mode():
            
            self.store.write_data(file_name, data)
            
            pass
        
        return data
    
    
    
    
    