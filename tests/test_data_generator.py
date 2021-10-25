import pytest

from pygendata import DataGenerator
from pygendata.managers import manager_factory

@pytest.fixture
def default_data_generator():
    return DataGenerator()

@pytest.fixture
def csv_data_generator():
    return DataGenerator('csv')

@pytest.fixture
def json_data_generator():
    return DataGenerator('json')

@pytest.fixture
def tsv_data_generator():
    return DataGenerator('tsv')

def test_not_passing_in_rows_results_in_no_rows(default_data_generator):
    assert default_data_generator.rows == []

def test_not_passing_in_manager_defaults_to_csv(default_data_generator):
    assert default_data_generator.manager == manager_factory('csv')

def test_passing_in_json_sets_manager_as_jsonmanager(json_data_generator):
    assert json_data_generator.manager == manager_factory('json')
def test_passing_in_tsv_sets_manager_as_tsvmanager(tsv_data_generator):
    assert tsv_data_generator.manager == manager_factory('tsv')

def test_passing_in_csv_sets_manager_as_csvmanager(csv_data_generator):
    assert csv_data_generator.manager == manager_factory('csv')
