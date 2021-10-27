import re
from .datatypes import datatypes, special_types

def get_value_for_column(column_name, dtype, current_row):
    patterns = re.compile(r'(email)|(name)', re.IGNORECASE)
    matches = patterns.match(column_name)
    id_pattern = re.compile(r'(id)', re.IGNORECASE)
    id_matches = id_pattern.match(column_name)
    if matches:
        return special_types[column_name.upper()]()
    elif id_matches:
        return current_row
    return datatypes[dtype]()