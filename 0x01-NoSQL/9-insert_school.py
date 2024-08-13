#!/usr/bin/env python3
'''
a Python Function that inserts a ndocument in a collection based
on kwargs
'''


def insert_school(mango_collection, **kwargs):
    '''inserts a new document in a collection based on kwargs
    '''
    result = mango_collection.insert_one(kwargs)
    return result.inserted_id
