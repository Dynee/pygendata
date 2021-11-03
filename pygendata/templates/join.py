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
            t2_rows = []
            t3_rows = []
            if self.tables:
                first = self.tables[0]
                second = self.tables[1]
                third = self.tables[2]
                for i in range(rows):
                    row = first.create_row(i)
                    t1_rows.append(row)
                for j in range(rows):
                    row = second.create_row_from_table_rows(t1_rows, j)
                    t2_rows.append(row)
                for k in range(rows):
                    row = third.create_row_from_table_rows(t1_rows, k)
                    t3_rows.append(row)
                # print('Table 1:')
                # for l in range(rows):
                #     print(t1_rows[l])
                # print('Table 2:')
                # for m in range(rows):
                #     print(t2_rows[m])
                # print('Table 3:')
                # for n in range(rows):
                #     print(t3_rows[n])
            return [(first, t1_rows), (second, t2_rows), (third, t3_rows)]
        except TypeNotSupportedError as t:
            print(str(t))