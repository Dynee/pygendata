# Pygendata

`pygendata` is a python library for generating test data from files (csv, tsv, ddl, json) or extending the libraries built in `template` system
to generate data

# Installation
To install pygendata you can use your favorite python package installer
```
pip install pygendata
```

The `pygendata` command automatically gets added to your path when you do pip install

To test if the installation worked correctly you can use the python repl and try importing the package
```
python

import pygendata
```

# Example Usage
Generating data from a DDL file to a CSV

1. Create a DDL File `users.txt`
```
create table users (
id INTEGER,
name TEXT ENCODING DICT(32),
email TEXT ENCODING DICT(32),
password TEXT ENCODING DICT(32)
);
```

2. Run the pygendata command
```
pygdendata --generate csv --base ddl users.txt --to users.csv --rows 1000000
```

3. You should now have a users.csv file in your current working directory with 1million users