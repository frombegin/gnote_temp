#!/usr/bin/env python
# -*- coding:utf-8 -*- 

class UserException(Exception):
    pass

class UserAlreadyExistsError(UserException):
    pass

class WrongUserOrPasswordError(UserException):
    pass

class Users(object):
    pass

class Database(object):
    
    def __init__(self):
        super(Database, self).__init__()
        self.__users = Users()
    
class DbProvider(object):
    pass

class UserDb(object):
    '''用户数据库接口'''
    
    def __init__(self):
        pass
    
    def registerUser(self, user, password):
        pass
    
    def removeUser(self, user): # only admin
        pass
    
    def lockUser(self, user): # only admin
        pass
    
    def unlockUser(self, user): # only admin
        pass

    def isUserLocked(self, userId):
        pass
    
    def changePassword(self, user, password):
        pass
    
    def getUserInfo(self, user):
        pass

    def setUserInfo(self, user, userInfo):
        pass
    
    def checkPassword(self, user, password):
        pass

# DatabaseProvider = gnote.db.SqliteProvider
       
class Cache(object):
    
    def get(self, key):
        pass
    
    def set(self, key, value):
        pass
    
    def exists(self, key):
        pass
    
    def delete(self, key):
        pass
    
    
userDb = UserDb()    
cache = Cache()
    
def registerUser(userInfo):
    try:
        userId = userDb.register(userInfo.user, userInfo.password)
        userDb.setUserInfo(userId, userInfo)
        return True
    except UserAlreadyExistsError:
        return False
    
def loginUser(user, password):
    try:
        userId = userDb.checkPassword(user, password)
        #TODO: if userDb.isLocked(userId):        
        if cache.exists(userId):
            # TODO: 异地登录, 踢掉前面登录的
            userInfo = userDb.getUserInfo(userId)
            cache.set(userId, userInfo)
        return True, userId
    except WrongUserOrPasswordError:
        return False
    except Exception:
        return False

def getUserInfo(userId):

    userInfo = cache.get(userId)
    if userInfo is None:
        userInfo = userDb.getUserInfo(userId)
        if userInfo is not None:
            cache.set(userId, userInfo)
    return userInfo
    
if __name__ == '__main__':
    pass