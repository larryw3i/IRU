
from datetime import datetime
import numpy as np

class IRUGender( Enum ):
    male = 0
    female = 1
    unknown = 2

class IRUPerson:
    def __init__(
        self, 
        name: str, 
        age: int,
        gender : IRUGender,
        school: str,
        enrolling_date : datetime,
        schooling_length  = 4,
        face_encodings = []
        ):

        name = name
        age = age
        gender = gender
        school = school
        enrolling_date = enrolling_date
        schooling_length = schooling_length
        face_encodings = face_encodings