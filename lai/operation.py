import re


class Option:
    '''
    '''

    def __init__(self, need, limit, name=None, sign=None):
        '''
        '''
        self.need = need
        self.limit = limit
        self.name = name
        self.sign = sign
        self.param = []

    def add_param(self, item):
        '''
        加入参数
        '''
        count = len(self.param)
        if self.need > count and (self.limit == None or (self.limit != None and count < self.limit)):
            self.param.append(item)
            return True
        return False


class Operation:
    '''
    '''

    def __init__(self, need, limit):
        '''
        初始化，默认参数的限制
        '''
        bale = Option(need, limit)
        self.options = [bale]
        self.signs = {'-': bale}
        self.names = {}

    def add_option(self, sign=None, name=None, limit=0, need=0):
        '''
        添加可选参数
        '''
        option = Option(need, limit, name, sign)
        if None != name:
            self.names[name] = option
        if None != sign:
            self.signs[sign] = option
        self.options.append(option)

    def parse(self, arguments):
        '''
        分析命令行参数
        '''
        option = self.signs['-']
        for item in arguments:
            if re.match(r"-[a-zA-Z]", item):
                sign = item[1:]
                option = self.signs[sign]
            elif re.match(r"--[a-z][-a-z]*", item):
                name = item[2:]
                option = self.names[name]
            else:
                if not option.add_param(item):
                    option = self.signs['-']
                    option.add_param(item)
