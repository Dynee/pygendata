from pydatagen import DataGenerator
from pydatagen.managers import csvmanager, tsvmanager, jsonmanager

def test_csv_manager():
    dg = DataGenerator('csv')
    assert type(dg.manager) == type(csvmanager.CSVManager)

def test_tsv_manager():
    dg = DataGenerator('tsv')
    assert type(dg.manager) == type(tsvmanager.TSVManager)

def test_json_manager():
    dg = DataGenerator('json')
    assert type(dg.manager) == type(jsonmanager.JSONManager)

def test_not_passing_in_rows_results_in_no_rows():
    dg = DataGenerator('csv')
    assert dg.rows == None
