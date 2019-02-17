import os
from nose.tools import *
from orm.orm import *

if os.path.exists('data.db'):
    os.remove('data.db')

connect(':memory:')
load_schema('create.sql')

def test_Person():
    jeo = Person('Jeo', 'Flaks', 33)
    murph = Person('Murphian', 'Xiao', 27)
    # jeo.create()
    # murph.create()
    assert jeo.fname == 'Jeo'