# -*- coding:utf-8 -*- 

class Server(object):
    '''
    main server application
    '''

    def __init__(self):
        super(Server, self).__init__()
        self.__running = False
        self.__kvdb = None
        self.__dfs = None
    
    def start(self):
        if not self.__running:
            pass
    
    def stop(self):
        if self.__running:
            pass
    
    def restart(self):
        self.stop()
        self.start()
    
    def isRunning(self): return self.__running
    
class Id(object):
    
    def __init__(self):
        super(Id, self).__init__()
        self.__type = None
        self.__id = None
        
    def isValid(self): return self.__id is not None
    
    def __str__(self): 
        return "user:%s" % self.__id

class UserInfo(object):

    MALE, FEMALE = ("MALE", "FEMALE")
        
    def __init__(self):
        ''''''
        super(UserInfo, self).__init__()
        self.__id = None
        self.__nickName = u"noname"
        self.__sex = UserInfo.MALE
        self.__age = 0
        self.__email = "none@none.com"
        self.__avatar = None
        self.__creationTime = None    
    
class GroupInfo(object):
    
    def __init__(self):
        ''''''
        super(GroupInfo, self).__init__()
        self.__id = None
        self.__name = u""
        self.__tags = u""
        self.__description = u""
        self.__creator = Id()
        self.__creationTime = None
    
class UserManager(object):
    
    def __init__(self):
        super(UserManager, self).__init__()
        self.__userDb = None    # TODO: 
        self.__cache = None     # TODO: 
    
    def registerUser(self, userInfo):
        uid = self.__userDb.register(userInfo)
        return uid
    
    def retrieveUserInfo(self, uid):

        # already cached?
        userInfo = self.__cache.get(uid)
        
        if userInfo == None:
        
            # load from DB
            userInfo = self.__userDb.getUserInfo(uid)    
            if userInfo != None:
            
                # add to cache
                self.__cache.set(uid, userInfo)         
        
        return userInfo
    
    def updateUserInfo(self, uid, userInfo):
        
        # remove from cache if already cached
        self.__cache.delete(uid)
        
        # update database
        self.__userDb.update(uid, userInfo)
        
        # update cache
        self.__cache.set(uid, userInfo)
    
class Session(object):
    
    def __init__(self):
        super(Session, self).__init__()
        self.__userId = Id()
        
    def register(self, account, password):
        pass    
    
    def login(self, account, password):
        pass
    
    def logout(self):
        pass
    
    def getMyInfo(self):
        pass
    
    def setMyInfo(self, userInfo):
        pass
    
    def getJoinedGroups(self):
        pass
    
    def createGroup(self, groupInfo):
        pass
    
    def modifyGroupInfo(self, groupInfo):
        pass
    
    def deleteGroup(self, gid):
        pass
    
    def enableGroup(self, gid, enable = True):
        pass
    
    def findGroupsByTag(self, tag, maxResult = 100):
        pass
    
    def joinGroup(self, gid, applyMessage):
        pass
    
    def leaveGroup(self, gid):
        pass
    
    def getGroupInfo(self, gid):
        pass
    
    def invateUser(self, userId, groupId, message):
        pass
    
    