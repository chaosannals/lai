'''
lai.egg
'''
import re, os, setuptools

class Egg:
    '''
    '''
    # +-------------------------------------------------------------------------
    def __init__(self, **setting):
        self.__setting = setting
    # +-------------------------------------------------------------------------
    def lay(self, **setting):
        self.__setting.update(setting)
        setuptools.setup(**self.__setting)
    # +-------------------------------------------------------------------------
    def loadVersion(self, path, coding='utf-8'):
        pattern = re.compile(r'__version__\s*=\s*\'((\d|\.)+)\'')
        with open(os.path.abspath(path), 'rb') as f:
            text = f.read().decode(coding)
            match = pattern.search(text)
            if match: self.__setting['version'] = match.group(1)
    # +-------------------------------------------------------------------------
    def loadLongDescription(self, path, coding='utf-8'):
        with open(os.path.abspath(path), 'rb') as f:
            text = f.read().decode(coding)
            self.__setting['long_description'] = text
    # +-------------------------------------------------------------------------
    def pickPackage(self, root, directory):
        result = [ root ]
        folder = { root: directory }
        for other in setuptools.find_packages(directory):
            name = root + '.' + other
            result.append(name)
            folder[name] = directory + '/' + other.replace('.', '/')
        if 'packages' in self.__setting:
            self.__setting['packages'].extend(result)
        else: self.__setting['packages'] = result
        if 'package_dir' in self.__setting:
            self.__setting['package_dir'].update(folder)
        else: self.__setting['package_dir'] = folder