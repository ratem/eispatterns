from sys import path
from os.path import dirname, abspath, join

folder = abspath(dirname(__file__))
path.append(join(folder, '..'))

