#!/usr/bin/python3
"""
Lists the State objects whith name passed as argument from the database
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
    states = session.query(State).filter_by(name = argv[4]).first()
    if states is not None:
        print(str(states.id))
    else:
        print("Not found")
    session.close()