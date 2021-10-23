from pydatagen import DataGenerator

if __name__ == "__main__":
    dg = DataGenerator('csv', rows=10)
    dg.ddl('./tests/user.txt', './tests/user.csv')