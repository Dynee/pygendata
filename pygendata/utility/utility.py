from pygendata.datatypes import datatypes, special_types

# 1. Define column cardinality
# pygendata --generate csv --base ddl users.ddl --column-cardinality name 50 --to users.csv --rows 100

def generate_reusable_rows_for_column(name, type, num_rows):
    rows = []
    for _ in range(num_rows):
        value = datatypes[type]() if type in datatypes else special_types[type]()
        row = {name: value}
        rows.append(row)
    return rows