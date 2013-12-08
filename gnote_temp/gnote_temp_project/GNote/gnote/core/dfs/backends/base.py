# -*- coding:utf-8 -*- 

class Stream(object):
    
    def __init__(self):
        pass
    
    def read(self, size):
        pass
    
    def write(self, buf, size):
        pass

class DistributedFileSystem(object):

    def __init__(self):
        pass
        
    def uploadStream(self, key, stream):
        pass
    
    def deleteStream(self, key):
        pass
    
    def downloadStream(self, key):
        pass
    