#!/usr/bin/python3
'''OK'''

class Base:
    '''OK'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''class instructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects+=1
            self.id= Base.__nb_objects
