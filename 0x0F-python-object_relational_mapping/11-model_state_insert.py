#!/usr/bin/python3
"""
 adds the State object "Louisiana" to the database hbtn_0e_6_usa
"""

import sys
from unicodedata import name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    obj = State(name="Louisiana")
    session.add(obj)
    session.commit()
    print(obj.id)
