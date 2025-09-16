from sqlalchemy import Column, Table, MetaData, String, create_engine, DateTime, Float

metadata = MetaData()

gold_table = Table(
    'gold',
    metadata,
Column('date', DateTime, primary_key=True),
    Column('open', Float),
    Column('high', Float),
    Column('low', Float),
    Column('close', Float),)

silver_table = Table(
    'sliver',
    metadata,
Column('date', DateTime, primary_key=True),
    Column('open', Float),
    Column('high', Float),
    Column('low', Float),
    Column('close', Float),)