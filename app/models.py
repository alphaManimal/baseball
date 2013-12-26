#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

"""
from sqlalchemy import create_engine
from sqlalchemy.sql import table, column
import ConfigParser
import json

def connect():

    config = ConfigParser.ConfigParser()
    config.read('conf/thisbaseball.ini')
    user = config.get('db','user')
    passwd =  config.get('db','passwd')
    host = config.get('db','host')
    db = config.get('db','db')

    url =  'mysql://'+user+':'+passwd+'@'+host+'/'+db

    engine = create_engine(url,pool_recycle=3600)

    return engine.connect()
    

def dataserver(request):
    # connect
    conn = connect()
    # query
    result = conn.execute('show tables;')
    # fetch
    res = result.fetchall()
    data = []

    # serialize & return
    for row in res:
        data.append({'table':row[0]})

    return json.dumps(data)
