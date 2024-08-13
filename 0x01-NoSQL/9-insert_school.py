#!/usr/bin/env python3
import pymongo
'''
a Python Function that inserts a ndocument in a collection based
on kwargs
'''


def insert_school(mongo_collection, **kwargs):
    '''inserts a new document in a collection based on kwargs
    '''
    for insertion in kwargs:
        mongo_collection.insert(insertion)
