import src
from src.egg import Egg

egg = Egg()
egg.loadLongDescription('README')
egg.pickPackage('lai', 'src')
egg.lay(
    name='lai',
    version=src.__version__,
    description='in order to lay python egg',
    url='https://github.com/chaosannals/lai',
    keywords='lai python package egg',
    license='MIT',
    author='chaosannals',
    author_email='chaosannals@gmail.com',
    classifiers= [
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    include_package_data=True,
    zip_safe=True,
    platforms='any'
)