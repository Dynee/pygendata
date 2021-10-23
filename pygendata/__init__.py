import logging

from tqdm import tqdm
from pygendata.ddl import DDL
from pygendata.managers import csvmanager, tsvmanager, jsonmanager
from pygendata.templates.geo import GeoTemplate

from multiprocessing import Pool, cpu_count

class DataGenerator:
    """
    DataGenerator takes a manager of type (csv, tsv, json ..ect)
    DataGenerator takes an optional argument for number of rows to generate when dealing with csv
    """
    def __init__(self, manager, **kwargs):
        if kwargs.get('rows'):
            self.rows = kwargs['rows']
        else:
            self.rows = []
        if manager == 'csv':
            self.manager = csvmanager.CSVManager()
        elif manager == 'tsv':
            self.manager = tsvmanager.TSVManager()
        elif manager == 'json':
            self.manager = jsonmanager.JSONManager()
    
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
            p = Pool(cpu_count())
            results = p.map(ddl.create_row, tqdm(range(self.rows)))
            self.manager.rows = list(results)
            self.manager.write(outfile)
        except IOError as e:
            logging.warn(str(e))
        
    def template(self, template_type, region, outfile):
        """
        Generates data using a template file, eventually this should support custom templates, currently only supports geo
        """
        template = None
        try:
            if template_type == 'geo':
                template = GeoTemplate(region)
            p = Pool(cpu_count())
            results = p.map(template.generate, tqdm(range(self.rows)))
            self.manager.rows = list(results)
            self.manager.write(outfile)
        except IOError as e:
            logging.warn(str(e))