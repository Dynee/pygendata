import logging

from ddl import DDL
from managers import csvmanager, tsvmanager, jsonmanager

class DataGenerator:
    """
    DataGenerator takes a manager of type (csv, tsv, json ..ect)
    DataGenerator takes an optional argument for number of rows to generate when dealing with csv
    """
    def __init__(self, manager, **kwargs):
        if manager == 'csv':
            self.manager = csvmanager.CSVManager()
            if kwargs['rows']:
                self.rows = kwargs['rows']
        elif manager == 'tsv':
            self.manager = tsvmanager.TSVManager()
        elif manager == 'json':
            self.manager = jsonmanager.JSONManager()

    def ddl(self, infile, outfile):
        """
        reads a ddl file from disk and generates a csv based on the column names
        """
        try:
            statement = self.manager.read(infile)
            ddl = DDL(statement)
            ddl.get_columns()
            ddl.create_headers()
            self.manager.headers = ddl.headers
            for _ in range(self.rows):
                ddl.create_row()
            self.manager.rows = ddl.column_data
            self.manager.write(outfile)
        except IOError as e:
            logging.warn(str(e))
        


dg = DataGenerator('csv', rows=10)
dg.ddl('../../tests/user.txt', '../../tests/users.csv')