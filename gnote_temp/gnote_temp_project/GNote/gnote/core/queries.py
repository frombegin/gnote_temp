# coding: utf-8

from objects import Query

class TagQuery(Query):
    
    def __init__(self, tag):
        super(TagQuery, self).__init__()
        self.__tag = tag
        
class FullTextQuery(Query):
    pass

class HotQuery(Query):
    pass