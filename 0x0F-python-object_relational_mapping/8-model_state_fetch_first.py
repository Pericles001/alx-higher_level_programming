#!/usr/bin/python3
"""
 prints the first State object from the database hbtn_0e_6_usa
"""

import imp
import sys
from venv import create
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
