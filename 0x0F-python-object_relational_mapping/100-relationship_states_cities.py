#!/usr/bin/python3
"""
creates the State "California" with the City "San Francisco" from the
database hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""

import sys
from unicodedata import name
from venv import create
from sqlalchemy import create_engine, true
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
    session.close()
