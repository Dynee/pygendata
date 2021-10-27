from .datatypes import datatypes, special_types
from .checker import get_value_for_column
from .exceptions import TypeNotSupportedError

class JSON:
    def __init__(self):
        self.headers = []
        self.data = {}
    
    @property
    def headers(self):
        return self._headers
    
    @headers.setter
    def headers(self, headers):
        self._headers = headers
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, rows):
        self._data = rows
    
    def get_headers(self, data):
        root_key = list(data.keys())[0] #only one root key per file
        self.data = data[root_key]
        for column in self.data:
            self.headers.append(column)
    
    def create_row(self, current_row):
        j = {}
        for column in self.headers:
            dtype = self.data[column]
            if dtype in datatypes or dtype in special_types:
                j[column] = get_value_for_column(column, dtype, current_row)
            else:
                raise TypeNotSupportedError(f"Type: {dtype} is not currently supported")
        return j
        