
if __name__ == '__main__':
    import enum
    import sys

    class Supplement(enum.Enum):
        PROTEIN = 'whey'
        CREATINE = 'creatine'
        TRENBOLONE = 'tren'
        TESTOSTERONE = 'test'

        def __str__(self):
            return self.name

    arg = sys.argv[1]

    supplement = Supplement(arg)
    print(supplement)

