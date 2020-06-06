
from pony import orm
from iru import db

from models.face_entry_model import  IruPerson

IruPerson()

if __name__ == "__main__":
    db.generate_mapping(create_tables=True)
    pass