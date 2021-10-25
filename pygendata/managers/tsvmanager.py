class TSVManager:
    def __init__(self):
        self.headers = []
        self.rows = []
    
    def __eq__(self, other):
        if not isinstance(other, TSVManager):
            return NotImplemented
        return self.headers == other.headers and self.rows == other.rows