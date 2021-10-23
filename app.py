import os
from pydatagen import DataGenerator

if __name__ == "__main__":
    dg = DataGenerator('csv', rows=10)
    filepath = os.path.dirname(os.path.realpath(__file__))
    dg.ddl(f"{filepath}/tests/user.txt", f"{filepath}/tests/users.csv")