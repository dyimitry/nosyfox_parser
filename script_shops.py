import requests
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from db import Shop


def write_db_shops(engine):
    # engine = create_engine('postgresql+psycopg2://postgres:example@localhost:5432/postgres', echo=True)
    session = Session(engine)
    engine.connect()

    count = 0
    body = {
        "limit": 10,
        "offset": 0
    }

    # result = []
    response = requests.post("https://api.nosyfox.net/query/bristol_shops", json=body, headers={
        'Api-Token': '098f7a6b-cada-448d-9a98-eef9e369c29f.8834dacc6d880fc2d808573759ad2ce0'})
    result_json = response.json()

    while result_json['total_count'] >= count:
        for i in result_json['items']:
            exem = Shop(
                adress=i['address'],
            )
            session.add(exem)
            # if isinstance(i, dict):
            #     result.append(i)
        body['offset'] += 10
        response = requests.post("https://api.nosyfox.net/query/bristol_shops", json=body, headers={
            'Api-Token': '098f7a6b-cada-448d-9a98-eef9e369c29f.8834dacc6d880fc2d808573759ad2ce0'})
        result_json = response.json()
        count += 10
    session.commit()
    # print(len(result))
    print(1)
