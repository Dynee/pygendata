import csv
import logging

class TSVManager:
    def __init__(self):
        self.headers = []
        self.rows = []
    
    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, headers):
        self._headers = headers
    
    @property
    def rows(self):
        return self._rows
    
    @rows.setter
    def rows(self, rows):
        self._rows = rows
    
    def read(self, file):
        try:
            with open(file, 'r') as f:
                tsv_file = csv.reader(file, delimeter='\t')
                self.headers, self.rows = tsv_file
        except IOError as e:
            logging.warning(str(e))

    def __eq__(self, other):
        if not isinstance(other, TSVManager):
            return NotImplemented
        return self.headers == other.headers and self.rows == other.rows