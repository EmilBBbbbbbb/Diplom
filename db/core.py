from create_db import engine
from db.models import gold_table
from get_cost import get_cost, list_to_dict
from sqlalchemy import insert

def insert_data_gold():
    with engine.connect() as connection:
        candles = get_cost('BBG000VJ5YR4')
        stmt = insert(gold_table).values(list_to_dict(candles))
        connection.execute(stmt)
        connection.commit()

if __name__ == '__main__':
    insert_data_gold()