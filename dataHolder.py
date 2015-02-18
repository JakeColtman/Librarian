

class DataState:
    
    def __init__(self, file_name, content = None):
        
        self.file_name = file_name
        
        self.content = content        
        
    def get_file_name(self):
        
        return self.file_name
    
    def has_value(self):
        
        return self.content is not None
    
    def get_content(self):
        
        return self.content