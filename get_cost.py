import os
from dotenv import load_dotenv
from sqlalchemy.orm.util import all_cascades

load_dotenv()

from datetime import timedelta

from tinkoff.invest import CandleInterval, Client, HistoricCandle
from tinkoff.invest.schemas import CandleSource
from tinkoff.invest.utils import now


TOKEN = os.getenv('INVEST_TOKEN')

def get_cost(id: str)->list:
    with Client(TOKEN) as client:

        all_candle = []
        for candle in client.get_all_candles(
            instrument_id=id,
            from_=now() - timedelta(days=365*7),
            interval=CandleInterval.CANDLE_INTERVAL_DAY,
            candle_source_type=CandleSource.CANDLE_SOURCE_UNSPECIFIED,
        ):
            all_candle.append(candle)

    return all_candle

def list_to_dict(arr: list[HistoricCandle]) -> list[dict]:

    all_candle = []
    for candle in arr:
        all_candle.append({'date': candle.time,
                           'open': float(f'{candle.open.units}.{candle.open.nano}'),
                           'high': float(f'{candle.high.units}.{candle.high.nano}'),
                           'low': float(f'{candle.low.units}.{candle.low.nano}'),
                           'close': float(f'{candle.close.units}.{candle.close.nano}'),
                           })

    return all_candle

if __name__ == "__main__":
    arr = get_cost('BBG000VJ5YR4')
    print(list_to_dict(arr))