# -*- coding:utf-8 -*- 

from datetime import datetime

class Object(object):
    
    def __init__(self):
        super(ObjectWithTags, self).__init__()
        self.__id = None
    
    def isNewlyCreated(self):
        return self.__id == None

class ObjectWithTags(Object):
    
    def __init__(self):
        super(ObjectWithTags, self).__init__()
        self.__tags = []
    
class Group(ObjectWithTags):

    def __init__(self):
        super(Group, self).__init__()
        self.__id = ""
        self.__members = []
        self.__book = Book()    
        
class User(ObjectWithTags):
    
    def __init__(self):
        super(User, self).__init__()
        self.__id = ""
        self.__joinedGroups = []
        self.__privateBook = Book()
    
class Book(object):
    
    def __init__(self):
        super(Book, self).__init__()
        self.__owner = ""

    def addNote(self, uid, note):
        pass
            
class Note(ObjectWithTags):
    
    def __init__(self):
        super(Note, self).__init__()
        self.__id = ""
        self.__bookId = ""
        self.__text = ""

class Activity(object):
    
    UNKNOWN, GROUP_CREATED, GROUP_DELETED, USER_ENTERED, USER_LEAVED = range(5)

    def __init__(self):
        super(Activity, self).__init__()
        self.__type = Activity.UNKNOWN
        self.__creationTime = datetime.now()
    
    def __unicode__(self):
        pass

class Timeline(object):
    
    def __init__(self):
        super(Timeline, self).__init__()
        self.__activties = []

class Query(object):
    
    def __init__(self):
        super(Query, self).__init__()
        self.__resultType = "GROUP" # "USER", "BOOK", "MIXED"
        self.__maxResult = 100;

class GNote(object):

    def __init__(self):
        super(GNote, self).__init__()
        self.__timeline = Timeline()
    
    def search(self, query):
        pass

if __name__ == '__main__':
    pass