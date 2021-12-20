#!/usr/bin/python3
"""
Deletes all States object with a name containing the letter a from db
"""

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    s = '%a%'
    states = session.query(State).filter(State.name.like(s))
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
