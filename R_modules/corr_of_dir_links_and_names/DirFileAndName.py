import re


class DirectoryCheck:
    def __init__(self, name):
        self.name = name

    def get_expansion(self):
        p = re.compile(pattern=r'(?P<name>^[0-9а-яА-ЯёЁa-zA-Z_.])[.](?P<expansion>([s][c][n])$)',
                       flags=re.IGNORECASE | re.VERBOSE)
        p_search = p.search(self.name)
        print((p_search))
        return p_search.group("expansion")

    def get_full_name(self):
        return self.name

    def get_name(self):
        p = re.compile(pattern=r'^(?P<name>[0-9а-яА-ЯёЁa-zA-Z_.])[.](?P<expansion>([s][c][n]))$',
                       flags=re.IGNORECASE | re.VERBOSE)
        p_search = p.search(self.name)
        return p_search.group("name")

    def get_split(self):
        p = re.split(r'[.]', self.name)
        for index, expansion in enumerate(p):
            if expansion == 'scn':
                return expansion


if __name__ == '__main__':
    from icecream import ic

    test = DirectoryCheck(name='adfasdfasd.fs__.scn')
    # ic(test.get_full_name())
    # ic(test.get_name())
    # ic(test.get_expansion())
    for index, i in enumerate(test.get_split()):
        if i == 'scn':
            print(f'{i}')

    ic(test.get_split[1])
