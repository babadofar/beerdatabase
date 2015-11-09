# -*- coding: utf-8 -*-

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from web import db


class RatebeerBeer(db.Model):
    __tablename__ = 'rb_beer'
    id = sa.Column('id', sa.Integer, primary_key=True)
    name = sa.Column('name', sa.Unicode(255))
    shortname = sa.Column('shortname', sa.Unicode(255))
    alias = sa.Column('alias', sa.Boolean)
    retired = sa.Column('retired', sa.Boolean)
    style_id = sa.Column('style_id', sa.Integer)
    score_overall = sa.Column('score_overall', sa.Float)
    score_style = sa.Column('score_style', sa.Float)
    abv = sa.Column('abv', sa.Float)
    ibu = sa.Column('ibu', sa.Float)
    brewery_id = sa.Column('brewery_id', sa.Integer, sa.ForeignKey('rb_brewery.id'), nullable=False)
    brewery = relationship('RatebeerBrewery', lazy=False)

    def __init__(self):
        pass


class RatebeerBrewery(db.Model):
    __tablename__ = 'rb_brewery'
    id = sa.Column('id', sa.Integer, primary_key=True)
    name = sa.Column('name', sa.Unicode(255))
    country = sa.Column('country', sa.Integer)
    subregion = sa.Column('subregion', sa.Integer)
    city = sa.Column('city', sa.Unicode(255))

    def __init__(self):
        pass


class PoletBeer(db.Model):
    __tablename__ = 'pol_beer'
    id = sa.Column('id', sa.Integer, primary_key=True)
    name = sa.Column('name', sa.Unicode(255))
    store_category = sa.Column('store_category', sa.Unicode(100))
    produktutvalg = sa.Column('produktutvalg', sa.Unicode(100))
    producer = sa.Column('producer', sa.Unicode(100))
    distributor = sa.Column('distributor', sa.Unicode(100))
    varenummer = sa.Column('varenummer', sa.Integer)
    abv = sa.Column('abv', sa.Float)
    volume = sa.Column('volume', sa.Float)
    color = sa.Column('color', sa.Unicode(100))
    smell = sa.Column('smell', sa.Unicode(100))
    taste = sa.Column('taste', sa.Unicode(100))
    method = sa.Column('method', sa.Unicode(255))
    cork_type = sa.Column('cork_type', sa.Unicode(100))
    packaging_type = sa.Column('packaging_type', sa.Unicode(100))
    price = sa.Column('price', sa.Float)
    country = sa.Column('country', sa.Unicode(100))
    district = sa.Column('district', sa.Unicode(100))
    subdistrict = sa.Column('subdistrict', sa.Unicode(100))
    url = sa.Column('url', sa.Unicode(100))
    vintage = sa.Column('vintage', sa.Unicode(100))
    ingredients = sa.Column('ingredients', sa.Unicode(255))
    pairs_with_1 = sa.Column('pairs_with_1', sa.Unicode(255))
    pairs_with_2 = sa.Column('pairs_with_2', sa.Unicode(255))
    pairs_with_3 = sa.Column('pairs_with_3', sa.Unicode(255))
    storage_notes = sa.Column('storage_notes', sa.Unicode(255))
    sweetness = sa.Column('sweetness', sa.Integer)
    freshness = sa.Column('freshness', sa.Integer)
    bitterness = sa.Column('bitterness', sa.Integer)
    richness = sa.Column('richness', sa.Integer)
    ratebeer_id = sa.Column('ratebeer_id', sa.Integer, sa.ForeignKey('rb_beer.id'), nullable=True)
    ratebeer = relationship('RatebeerBeer', lazy=False)

    def __init__(self):
        pass
