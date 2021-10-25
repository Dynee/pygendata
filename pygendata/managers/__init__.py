from .csvmanager import CSVManager
from .jsonmanager import JSONManager
from .tsvmanager import TSVManager

def manager_factory(manager_type):
    if manager_type == 'csv':
        manager = CSVManager()
    elif manager_type == 'tsv':
        manager = TSVManager()
    elif manager_type == 'json':
        manager = JSONManager()
    else:
        manager = CSVManager()
    return manager