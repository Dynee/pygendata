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

# Templates
`pygendata` has the concept of a template, a template should be just that, a template for you do generate data

`pygendata` provides a `GeoTemplate` object that generates a list of `latitude/longitude` points

```
from faker import Faker

class GeoTemplate:
    """
    A geo template generates Lat/Lon values particular to a specified region
    """

    # TODO: support more regions
    _allowed_regions = {'US': True, 'GB': True}

    def __init__(self, region):
        self.fake = Faker()
        if self.allowed_region(region):
            self.region = region
        else:
            self.region = 'US' # defaults to US
        self.keys = ['latitude', 'longitude']
        self.values = []
    
    def allowed_region(self, region):
        if region not in self._allowed_regions:
            return False
        return True
    
    def generate(self, row):
        latitude, longitude = self.fake.local_latlng(country_code=self.region, coords_only=True)
        return { 'latitude': latitude, 'longitude': longitude }
```

You can use the `pygendata` command to generate a JSON file with these values
```
pygendata --generate json --template geo US --to us_lat_lon.json --rows 1000000
```

An output file with 1000000 `lat/long` points should be created

Every json file has the key `"rows": [....]`

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


## How To Extend
1. How to add a new cli command
```
in /pygendata/cli/__init__.py 

under line 18 add something similar to parser.add_argument('--rows', type=int, help='The number of rows to generate(default=100)')

this uses the argparse api where the first argument is the command that you will call, the second is the data type that the arg accepts, and third is a help message that
you can provide

commands get added to the args object so if we created a command called hello like so
parser.add_argument('--hello', type=str, help='say a message to someone')

it would be accessible as args.hello

and then you can use some condition to run a command on the data generator object, this isn't really specific but it depends on what  you want to do w/ the new command

```

## How to Run the script
```
There is a bunch of ways to do this but you could use the makefile and just run 
`make run`

if you want to change the default run command just edit the makefile
run:
	python3 pygendata/cli/__init__.py --generate csv --base json tests/test.json --to tests/test_json_out.csv --rows 10

if you want to generate a csv file
pygendata --generate csv --base ddl <path/to/ddl> -- to <path/to/ouput> --rows <number_of_rows> 

I have mainly been using the tests directory for generating all my dummy data I would stick to using it since it works
```

## Important parts of the project
The datatypes.py file is where all of the logic on how to actually generate the data comes from
it exports 2 important structures, the datatypes dict and special_types dict, basically if you want to change the way
it generates data for a particular type in SQL i.e INTEGER you would change it inside the datatypes_dict

its important that the datatypes in the datatypes dict return a function as the value (i.e don't call the function except for specific types like TEXT_ENCODING_DICT)

this is shown in ddl.py in the create row function, basically
if the data type matches certain conditions, it will pick either the datatypes dict to get the value from
or the special_types dict, the case where this doesn't apply is when the data type name matches id it auto increments the value

the data types are generated using the faker library in python
if you want to change the way this works, i.e use a different library or make your own, all you need to do is just change the values for the keys in the datatypes dict

for example if I want BIGINT to always return the same value
I could create a function, now it will always return 1
```
def static_bigint():
    return 1

datatypes = {
    'BIGINT': static_bigint
}
```

```

datatypes = {
    'BIGINT': fake.pyint,
    'TIMESTAMP(0)': fake.date_time,
    'INTEGER': fake.pyint,
    'TEXTENCODINGDICT(32)': pick_random_str(32),
    'TEXTENCODINGDICT': pick_random_str(32),
    'FLOAT': fake.pyfloat,
    'SMALLINT': fake.pyint,
    'BIGINTENCODINGFIXED(8)': fake.pyint,
    'BIGINTENCODINGFIXED(16)': fake.pyint,
    'BIGINTENCODINGFIXED(32)': fake.pyint,
    'BOOLEAN': gen_fake_bool,
    'DATE[1]': fake.date,
    'DATEENCODINGFIXED(16)': fake.date_time,
    'DATEENCODINGFIXED(32)': fake.date_time,
    'DECIMAL': fake.pyfloat,
    'DOUBLE': fake.pyfloat,
    'EPOCH': fake.date_time,
    'FLOAT': fake.pyfloat,
    'INTEGERENCODINGFIXED(8)': fake.pyint,
    'INTEGERENCODINGFIXED(16)': fake.pyint,
    'SMALLINTENCODINGFIXED(8)': fake.pyint,
    'TEXTENCODINGDICT(8)': pick_random_str(8),
    'TEXTENCODINGDICT(16)': pick_random_str(16),
    'TEXTENCODINGNONE': text_encoding_none(),
    'TIME': fake.date_time(),
    'TIMEENCODINGFIXED(32)': fake.date_time,
    'TIMESTAMP(3)': fake.date_time,
    'TIMESTAMP(6)': fake.date_time,
    'TIMESTAMP(9)': fake.date_time,
    'TIMESTAMPENCODINGFIXED(32)': fake.date_time,
    'TIMESTAMP(0)ENCODINGFIXED(32)': fake.date_time,
    'TINYINT': fake.pyint,
    'DATEENCODINGDAYS(32)': fake.date_time
}

special_types = {
    'EMAIL': fake.email,
    'NAME': fake.name,
}

def create_row(self, current_row):
        c = {}
        for column in self.columns:
            name, *type_info = column.split(' ')
            type_info = ''.join(type_info)
            if type_info.upper() in datatypes:
                # is name special?
                patterns = re.compile(r'(email)|(name)', re.IGNORECASE)
                matches = patterns.match(name)
                id_pattern = re.compile(r'(id)', re.IGNORECASE)
                id_matches = id_pattern.match(name)
                text_pattern = re.compile(r'(TEXT\w)+', re.IGNORECASE)
                text_matches = text_pattern.match(type_info)
                if matches:
                    c[name] = special_types[name.upper()]()
                elif id_matches:
                    c[name] = current_row
                elif text_matches:
                    c[name] = datatypes[type_info.upper()]
                else:
                    print(name)
                    c[name] = datatypes[type_info.upper()]()
            else:
                print(type_info)
                pass
        return c
```