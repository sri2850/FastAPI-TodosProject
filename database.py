from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import keyvault

username = keyvault.config_manager.get("username")
password = keyvault.config_manager.get("password")
SQLALCHEMY_DATABASE_URL = f'postgresql://{username}:{password}@localhost/dynamic'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
