import requests
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from db import Product


def write_db_products(engine):
    # engine = create_engine('postgresql+psycopg2://postgres:example@localhost:5432/postgres', echo=True)
    session = Session(engine)
    engine.connect()

    count = 0
    body = {
        "limit": 10,
        "offset": 0
    }

    # result = []
    response = requests.post("https://api.nosyfox.net/query/bristol_products", json=body, headers={
        'Api-Token': '098f7a6b-cada-448d-9a98-eef9e369c29f.8834dacc6d880fc2d808573759ad2ce0'})
    result_json = response.json()


    while result_json['total_count'] >= count:
        for i in result_json['items']:
            exem = Product(
                name=i['name'],
                volume=i['volume'],
                added_at=i['added_at'],
                strenght=i['strength'],
                country=i['country_of_origin']
            )
            session.add(exem)
            # if isinstance(i, dict):
            #     result.append(i)
        body['offset'] += 10
        response = requests.post("https://api.nosyfox.net/query/bristol_products", json=body, headers={
            'Api-Token': '098f7a6b-cada-448d-9a98-eef9e369c29f.8834dacc6d880fc2d808573759ad2ce0'})
        result_json = response.json()
        count += 10
    session.commit()
    # print(len(result))
    print(1)
