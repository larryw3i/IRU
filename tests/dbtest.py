
from pony import orm
import os
from pony.orm.core import Required, Set

from models.face_entry_model import  IruPerson

db = orm.Database()

db.bind(
    provider='sqlite', 
    filename= os.path.join( '..', 'data', 'iru_test.db' ) , 
    create_db=True)
    
class Person(db.Entity):
    name = Required(str)
    age = Required(int)
    cars = Set('Car')
    
class Car(db.Entity):
    make = Required(str)
    model = Required(str)
    owner = Required(Person)

IruPerson()

def test():
    db.generate_mapping(create_tables=True)
    pass