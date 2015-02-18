'''

Holds the abstract base class for all of the handlers

'''

from abc import ABCMeta, abstractmethod

class BaseInserter(object):
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def put(self):
        '''
        Put content into the bucket
        '''
        return
        
        
if __name__ == "__main__":
    
    class ExampleInserterNumber3(BaseInserter):
        
        def put(self):
            
            return 3
        
    ExampleInserterNumber3()
     