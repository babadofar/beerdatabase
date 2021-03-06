# -*- coding: utf-8 -*-

from datetime import datetime
from beertools.polchecker import check_beer

from db import Database


def find_in_list(dicts, key, value):
    try:
        return (item for item in dicts if item[key] == value).next()
    except StopIteration:
        return None


def save_stock(stock_by_pol, db):
    sql = '''
        INSERT INTO pol_stock (shop_id, pol_beer_id, stock, updated)
        VALUES (%(shop_id)s, %(pol_beer_id)s, %(stock)s, %(updated)s)
    '''
    db.run_upserts(sql, stock_by_pol)


def update_pol_stock(conn_str=None):
    db = Database(conn_str)
    beers = db.get_pol_beers()
    shops = [pol['id'] for pol in db.get_pol_shops()]

    stock_by_pol = []
    for beer in beers:
        stocks = check_beer(beer['id'])
        for stock in stocks:
            num = stock['stock']
            updated = stock['updated']
            stock_by_pol.append({
                'shop_id': stock['pol_id'],
                'pol_beer_id': beer['id'],
                'stock': num,
                'updated': updated
            })
        shops_with_beer = [int(stock['pol_id']) for stock in stocks]
        for pol_id in shops:
            if pol_id not in shops_with_beer:
                stock_by_pol.append({
                    'shop_id': pol_id,
                    'pol_beer_id': beer['id'],
                    'stock': 0,
                    'updated': datetime.now()
                })
    save_stock(stock_by_pol, db)
    db.add_log('pol_stock')

if __name__ == '__main__':
    update_pol_stock()
