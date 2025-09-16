from sqlalchemy import create_engine
from models import metadata

engine = create_engine('sqlite:///metals.db')

def create_db():
    metadata.create_all(engine)

if __name__ == '__main__':
    create_db()