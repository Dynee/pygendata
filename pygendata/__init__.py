import logging
import json
from json import JSONDecodeError
from tqdm import tqdm
from pygendata.ddl import DDL
from pygendata.pygenjson import JSON
from pygendata.managers import manager_factory
from pygendata.templates.geo import GeoTemplate
from pygendata.templates.join import JoinTemplate
from multiprocessing import Pool, cpu_count
from pygendata.utility import generate_reusable_rows_for_column

# TODO: support reading from json, tsv
class DataGenerator:
    """
    DataGenerator takes a manager of type (csv, tsv, json ..ect)
    DataGenerator takes an optional argument for number of rows to generate when dealing with csv
    """
    def __init__(self, manager=None, **kwargs):
        if kwargs.get('rows'):
            self.rows = kwargs['rows']
        else:
            self.rows = []
        self.manager = manager_factory(manager)
    
    @property
    def manager(self):
        return self._manager
    
    @manager.setter
    def manager(self, manager):
        self._manager = manager

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
            print(self.manager.headers)
            p = Pool(cpu_count())
            print('Generating rows from ddl file')
            results = p.map(ddl.create_row, tqdm(range(self.rows)))
            self.manager.rows = list(results)
            self.manager.write(outfile)
        except IOError as e:
            logging.warn(str(e))
    
    # TODO: template for high cardinality data (cardinality column name for cli)
    # TODO: make geo data realistic? see what kind of geo data would want to be generated
    def template(self, template_type, template_arg, outfile):
        """
        Generates data using a template file, eventually this should support custom templates, currently only supports geo
        """
        template = None
        try:
            if template_type == 'geo':
                template = GeoTemplate(template_arg)
            p = Pool(cpu_count())
            self.manager.headers = template.keys
            print('Generating rows from template')
            results = p.map(template.generate, tqdm(range(self.rows)))
            self.manager.rows = list(results)
            self.manager.write(outfile)
        except IOError as e:
            logging.warn(str(e))

    def json(self, infile, outfile):
        try:
            json_str = self.manager.read(infile)
            json_data = json.loads(json_str)
            j = JSON()
            j.get_headers(json_data)
            self.manager.headers = j.headers
            p = Pool(cpu_count())
            results = p.map(j.create_row, tqdm(range(self.rows)))
            self.manager.rows = list(results)
            self.manager.write(outfile)
        except (IOError, JSONDecodeError) as e:
            logging.warning(str(e))
    
    def join(self, infile, outfile):
        try:
            jt = JoinTemplate()
            jt.parse(infile)
            tables = jt.scaffold(self.manager.rows)
            for table in tables:
                self.manager.rows = table[1]
                self.manager.headers = table[0].headers
                self.manager.write(outfile)
        except IOError as e:
            logging.warning(str(e))
    
    def cardinality(self, infile, outfile, column_list, cardinality):
        columns = column_list.split(',')
        reusable_rows = []
        for column in columns:
            col_name, col_type = column.split(':')
            reusable_rows.append(generate_reusable_rows_for_column(col_name, col_type, cardinality))
        print(reusable_rows)

