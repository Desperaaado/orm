import os
from nose.tools import *
from orm.orm import *

if os.path.exists('data.db'):
    os.remove('data.db')

connect(':memory:')
load_schema(r'C:\Users\xiao0\projects_pro\orm\orm\create.sql')

def test_Person():
    jeo = Person('Jeo', 'Flaks', 33)
    murph = Person('Murphian', 'Xiao', 27)
    jeo.create()
    murph.create()
    assert jeo.fname == 'Jeo'
    jeo.fname = 'Mama'
    jeo.update()
    assert jeo.fname == 'Mama'
    murph2 = Person.read(murph.pk)
    assert murph2.fname == 'Murphian'
    jeo.delete()