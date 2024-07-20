import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import logging
logging.basicConfig(level=logging.DEBUG)

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://remittance_db_user:l38kqyLCA7n1BemA1s0X8WsiUpryZv0K@dpg-cqdsp9pu0jms73908ck0-a.oregon-postgres.render.com/remittance_db")
logging.debug(f'--------------- {DATABASE_URL}')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

metadata = MetaData()

