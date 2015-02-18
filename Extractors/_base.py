'''

Holds the abstract base class for all of the handlers

'''

from abc import ABCMeta, abstractmethod

class BaseExtractor(object):
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def get(self):
        '''
        Finds the data from the source and returns the content
        '''
        return
        
        
if __name__ == "__main__":
    
    class ExampleHandlerNumber3(BaseHandler):
        
        def get(self):
            
            return 3
        
        def write(self):
            
            return 3
        
    ExampleHandlerNumber3()
    