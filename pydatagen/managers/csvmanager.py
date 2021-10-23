import csv
import logging
import os

class CSVManager:
    def __init__(self, headers=None, rows=None):
        self.headers = headers
        self.rows = rows
    
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
        path = os.path.dirname(os.path.realpath(__file__))
        filepath = f"{path}/{file}"
        try:
             with open(filepath, 'r') as f:
                statement  = f.read()
                return statement
        except IOError as e:
            logging.warning(str(e))
    
    def write(self, file):
        path = os.path.dirname(os.path.realpath(__file__))
        filepath = f"{path}/{file}"
        try:
            with open(filepath, 'w+') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.headers)
                writer.writeheader()
                for row in self.rows:
                    writer.writerow(row)
        except Exception as e:
            logging.warn(str(e))
            