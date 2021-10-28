from pygendata.exceptions import TypeNotSupportedError
from pygendata.managers import CSVManager
import logging
import os
from pygendata.ddl import DDL

class JoinTemplate:
    def __init__(self):
        self.tables = []
    
    def parse(self, file):
        manager = CSVManager()
        try:
            statement = manager.read(file)
            keys, *tables = statement.split('/')
            keys = keys.strip('\n')
            keys = keys.split(',')
            tables = [x.strip() for x in tables]
            ddls = [DDL(stmt) for stmt in tables]
            for ddl in ddls:
                ddl.get_columns()
                ddl.columns = [column.strip() for column in ddl.columns]
                ddl.create_headers()
            self.tables = ddls
        except IOError as e:
            logging.warning(str(e))
    
    # TODO: Auto increment rows, make sure data is synchronized between joined tables
    def scaffold(self, rows):
        try:
            t1_rows = []
            if self.tables:
                first = self.tables[0]
                for i in range(rows):
                    t1_rows.append(first.create_row(i))
            print(t1_rows)
        except TypeNotSupportedError as t:
            print(str(t))

jt = JoinTemplate()
filepath = os.getcwd()
jt.parse(f"{filepath}/aog.sql")
jt.scaffold(10)