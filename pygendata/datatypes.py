from collections import defaultdict
from faker import Faker
import random
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

fake = Faker()

# 255 Distinct String values
def text_encoding_dict(size):
    """
    Generates distinct string values
    based on an input size
    """
    #p = Pool(cpu_count())
    values = []
    limit = 0
    if size == 8:
        limit = 255
    elif size == 16:
        limit = 64000
    elif size == 32:
        limit = 100000 # defaulting to 100k on size=32, 2bil rows is not feasible
    print('Generating reusable string values...')
    for i in range(limit):
        values.append(generate_str(i))
    return values

def generate_str(index):
    return f"default{index}"

def text_encoding_none():
    return pick_random_str(32)

values_8 = text_encoding_dict(8)
values_16 = text_encoding_dict(16)
values_32 = text_encoding_dict(32)

def pick_random_str(size):
    value = ""
    if size == 8:
        index = random.randint(0, 254)
        value = values_8[index]
    elif size == 16:
        index = random.randint(0, 64000)
        value = values_16[index]
    elif size == 32:
        index = random.randint(0, 100000)
        value = values_32[index]
    return value

def gen_fake_bool():
    return True

# Point, Polygon, and Multipolygon currently not supported
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

# we match on special types to make the data more realistic
special_types = {
    'EMAIL': fake.email,
    'NAME': fake.name,
    'AUTOINCREMENT': 0
}