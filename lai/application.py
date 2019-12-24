import re
from .operation import Operation

class Application:
    '''
    '''

    def __init__(self):
        '''
        '''
        self.operation = Operation(0, 0)
        self.operation.add_option('a')
        self.operation.add_option('b', 'bb', need=2, limit=2)
        self.operation.add_option('c', need=2, limit=None)

    def apply(self, arguments):
        '''
        '''
        self.operation.parse(arguments)
        for option in self.operation.options:
            print("{} {} - {}".format(option.name, option.sign, option.param))
