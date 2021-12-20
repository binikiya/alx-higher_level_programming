#!/usr/bin/python3
"""
Lists the first State objects from the database
"""

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    firstState = session.query(State).order_by(State.id).first()
    if firstState is not None:
        print("{}: {}".format(firstState.id, firstState.name))
    else:
        print("Nothing")
    session.close()
