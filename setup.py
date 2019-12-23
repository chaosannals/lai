import setuptools

with open('readme.md', 'r') as reader:
    long_description = reader.read()

setuptools.setup(
    name='lai',
    version='2019.0.1',
    description='yet a python demo',
    long_description=long_description,
    long_description_content_type='text/markdown',
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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        'imagehash',
        'scipy',
        'vptree',
    ],
    include_package_data=True,
    platforms='any'
)