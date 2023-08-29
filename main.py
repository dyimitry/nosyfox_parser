import threading

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from script_shops import write_db_shops
from script_products import write_db_products
from script_categories import write_db_categories

if __name__ == '__main__':

    engine = create_engine('postgresql+psycopg2://postgres:example@localhost:5432/postgres', echo=True)
    # session = Session(engine)
    # engine.connect()

    # write_db_categories(session)
    # write_db_shops(session)
    # write_db_products(session)

    # init threads
    t1 = threading.Thread(target=write_db_categories, args=(engine,))
    t2 = threading.Thread(target=write_db_shops, args=(engine,))
    t3 = threading.Thread(target=write_db_products, args=(engine,))

    # start threads
    t1.start()
    t2.start()
    t3.start()

    # join threads to the main thread
    t1.join()
    t2.join()
    t3.join()

    # session.commit()
    # postgres_db.close_database()