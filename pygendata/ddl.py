from pygendata.datatypes import datatypes, special_types
from pygendata.exceptions import TypeNotSupportedError

import re
import logging


class DDL:
    def __init__(self, statement):
        self.statement = statement
        self.columns = []
        # {'name': <column_name>, 'type': <column_type> }
        self.column_data = []
        self.headers = []

    @property
    def column_data(self):
        return self._column_data

    @column_data.setter
    def column_data(self, column_data):
        self._column_data = column_data

    def get_columns(self):
        _, *cols = self.statement.split('\n')
        cols = [x.rstrip(',') for x in cols]
        cols = [x for x in cols if x != ');']  # remove );
        cols = list(filter(None, cols))  # remove empty strings
        self.columns = cols

    def create_headers(self):
        for column in self.columns:
            name, *_ = column.split(' ')
            self.headers.append(name)

    def create_row(self, current_row):
        c = {}
        for column in self.columns:
            name, *type_info = column.split(' ')
            type_info = ''.join(type_info)
            try:
                if type_info.upper() in datatypes or type_info.upper() in special_types:
                    # is name special?
                    patterns = re.compile(r'(email)|(name)', re.IGNORECASE)
                    matches = patterns.match(name)
                    id_pattern = re.compile(r'(id)', re.IGNORECASE)
                    id_matches = id_pattern.match(name)
                    if matches:
                        c[name] = special_types[name.upper()]()
                    elif id_matches or type_info == 'AUTOINCREMENT':
                        c[name] = current_row
                    else:
                        if type_info == 'TIMESTAMP(0)':
                            c[name] = datatypes[type_info]().strftime("%Y-%m-%d %H:%M:%S")
                        else:
                            c[name] = datatypes[type_info]()
            except KeyError as k:
                logging.warning(str(k))
        return c
    
    def create_row_from_table_rows(self, table_rows, current_row):
        c = {}
        for column in self.columns:
            name, *type_info = column.split(' ')
            type_info = ''.join(type_info)
            try:
                if name in table_rows[current_row]:
                    c[name] = table_rows[current_row][name]
                else:
                    if type_info in datatypes or type_info in special_types:
                    # is name special?
                        patterns = re.compile(r'(email)|(name)', re.IGNORECASE)
                        matches = patterns.match(name)
                        if matches:
                            c[name] = special_types[name.upper()]()
                        else:
                            if type_info == 'TIMESTAMP(0)':
                                c[name] = datatypes[type_info]().strftime("%Y-%m-%d %H:%M:%S")
                            else:
                                c[name] = datatypes[type_info]()
            except KeyError as k:
                logging.warning(str(k))
        return c
