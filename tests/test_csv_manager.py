import pytest

from pygendata.managers import manager_factory

@pytest.fixture
def csv_manager_no_headers_no_rows():
    return manager_factory('csv')

@pytest.fixture
def csv_manager_headers_rows():
    csv_manager = manager_factory('csv')
    csv_manager.headers = ['header1', 'header2']
    csv_manager.rows = [{'header1': 'value1', 'header2': 'value2'}]
    return csv_manager

def test_defaults_csv_manager_has_no_headers_and_rows(csv_manager_no_headers_no_rows):
    assert csv_manager_no_headers_no_rows.headers == None
    assert csv_manager_no_headers_no_rows.rows == None

def setting_csv_manager_headers_and_rows_results_in_values(csv_manager_headers_rows):
    assert csv_manager_headers_rows.headers == ['header1', 'header2']
    assert csv_manager_headers_rows.rows == [{'header1': 'value1', 'header2': 'value2'}]

# this has to run in the current working dir, i should fix this
def test_reading_from_file_returns_data(csv_manager_no_headers_no_rows):
    statement = csv_manager_no_headers_no_rows.read('tests/users.txt')
    assert statement != None

def test_writing_to_file_creates_a_new_file(csv_manager_headers_rows):
    filename = 'tests/output.csv'
    csv_manager_headers_rows.write(filename)
    statement = csv_manager_headers_rows.read(filename)
    assert statement != None